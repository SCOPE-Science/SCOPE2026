"""Core knot-diagram library: PD parsing, orientation trace, writhe,
Kauffman bracket state-sum, Jones, state circles, adequacy, Turaev genus.
Stdlib only.

REPAIRED version (auditor repair, lane-292):
- A/B convention is POSITIONAL per KnotTheory X[a,b,c,d] naming
  (positions 0,1,2,3 = a,b,c,d, counterclockwise from the incoming lower edge):
    A-smoothing = P_ad P_bc = pairs (0,3) & (1,2), at EVERY crossing;
    B-smoothing = P_ab P_cd = pairs (0,1) & (2,3), at EVERY crossing.
  Uniform all-A / all-B states, circle counts |s_A|, |s_B|, and the
  single-flip adequacy tests are all taken w.r.t. these positional smoothings.
- Bracket weights (fixed so the pipeline reproduces the tabulated Jones values
  801/801 with the true geometric writhe): the A-smoothing carries A^{-1} and
  the B-smoothing carries A^{+1}, i.e.
      <X> = A^{-1} <A-smoothing> + A <B-smoothing>,
  <unknot> = 1, <L u O> = (-A^2 - A^-2) <L>.
  Jones: V(q) = (-A^3)^{-w} <K> at A = q^{-1/4}, w = geometric writhe.
  (Exchanging the A/B names maps A <-> A^-1; the stated weights are exactly
  what reproduces the reference Jones polynomials with the true writhe, proved
  by the 801/801 exact-match gate in verify.py.)
- Component count: the straight-through arrival walk visits every directed
  arrival; each link component contributes exactly two directed cycles
  (forward + reverse traversal), so ncomp = (#cycles)/2. All 801 prime-knot
  rows give ncomp = 1 (asserted in the census run).
- Orientation/writhe: straight-through trace (under 0<->2, over 1<->3);
  crossing sign = cross product of (over, under) tangents. Signs agree with
  the independent local consecutive-edge rule on all 801 rows (verify.py V5).
"""
import re


def parse_pd(s):
    """Parse KnotAtlas PD presentation into list of (i,j,k,l) int tuples."""
    cells = re.findall(r"X<sub>(.*?)</sub>", s)
    out = []
    for c in cells:
        c = c.strip()
        if "," in c:
            out.append(tuple(int(x) for x in c.split(",")))
        else:
            out.append(tuple(int(x) for x in c))
    return out


def parse_dt(s):
    return [int(x) for x in s.strip().split()]


def parse_jones(s):
    """Parse KnotAtlas <math> Jones string into {exp: coeff} in q."""
    t = s.replace("<math>", "").replace("</math>", "").strip()
    t = t.replace(" ", "")
    # brace-aware split on +/- term separators (exponent minuses are inside {})
    terms, cur, depth = [], "", 0
    for ch in t:
        if ch == "{":
            depth += 1
            cur += ch
        elif ch == "}":
            depth -= 1
            cur += ch
        elif ch in "+-" and depth == 0 and cur not in ("", "+", "-"):
            terms.append(cur)
            cur = ch
        else:
            cur += ch
    if cur:
        terms.append(cur)
    terms = [x for x in terms if x not in ("", "+", "-")]
    poly = {}
    for term in terms:
        term = term.lstrip("+")
        m = re.fullmatch(r"(-?\d*\.?\d*)(q(\^\{(-?\d+)\}|(\^(-?\d+))?)?)?", term)
        assert m, f"unparsed term {term!r} in {s!r}"
        coef_s, qpart, _, exp_braced, _, exp_bare = m.groups()
        if coef_s in ("", "+"):
            coef = 1
        elif coef_s == "-":
            coef = -1
        else:
            coef = float(coef_s) if "." in coef_s else int(coef_s)
        if not qpart:
            exp = 0
        elif exp_braced is not None:
            exp = int(exp_braced)
        elif exp_bare is not None:
            exp = int(exp_bare)
        else:
            exp = 1
        poly[exp] = poly.get(exp, 0) + coef
    return {e: c for e, c in poly.items() if c != 0}


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb

    def count(self):
        return len(set(self.find(a) for a in range(len(self.p))))


# Positional smoothings (KnotTheory convention): A = P_ad P_bc, B = P_ab P_cd.
A_PAIRS = ((0, 3), (1, 2))
B_PAIRS = ((0, 1), (2, 3))


class Diagram:
    def __init__(self, pd):
        self.pd = [tuple(x) for x in pd]
        self.c = len(pd)
        # edge -> list of (crossing_idx, position 0..3)
        self.edge_ends = {}
        for ci, (a, b, cc, d) in enumerate(self.pd):
            for pos, e in enumerate((a, b, cc, d)):
                self.edge_ends.setdefault(e, []).append((ci, pos))
        for e, v in self.edge_ends.items():
            assert len(v) == 2, f"edge {e} appears {len(v)} times"
        self.nedges = max(self.edge_ends)
        # orientation trace: straight-through walk (under 0<->2, over 1<->3)
        self.ori = self._trace()  # ori[ci] = (under_dir, over_dir)
        self.signs = [self._sign(ci) for ci in range(self.c)]
        self.writhe = sum(self.signs)

    def _trace(self):
        # directed walk over arrivals: state = (edge, end_index 0/1).
        # arrival at (e,k) -> depart via straight-through paired edge,
        # travel to the other end. The transition is a permutation; each
        # link component gives exactly 2 cycles (forward/reverse), so
        # components = #cycles / 2.
        c = self.c
        other = {}
        for e, v in self.edge_ends.items():
            other[(e, 0)] = (e, 1)
            other[(e, 1)] = (e, 0)
        end_of = {}  # (e,k) -> (ci,pos)
        for e, v in self.edge_ends.items():
            for k, (ci, pos) in enumerate(v):
                end_of[(e, k)] = (ci, pos)
        PAIR = {0: 2, 2: 0, 1: 3, 3: 1}  # straight through
        trans = {}
        for e, v in self.edge_ends.items():
            for k in (0, 1):
                ci, pos = end_of[(e, k)]
                e2 = self.pd[ci][PAIR[pos]]
                v2 = self.edge_ends[e2]
                k2 = 0 if v2[0] == (ci, PAIR[pos]) else 1
                assert v2[k2] == (ci, PAIR[pos])
                trans[(e, k)] = other[(e2, k2)]
        visited = set()
        under_dir = {}
        over_dir = {}
        ncyc = 0
        for start in trans:
            if start in visited:
                continue
            ncyc += 1
            cur = start
            while cur not in visited:
                visited.add(cur)
                e, k = cur
                ci, pos = end_of[cur]
                if pos == 0:
                    under_dir[ci] = +1  # pos0 -> pos2
                elif pos == 2:
                    under_dir[ci] = -1
                elif pos == 1:
                    over_dir[ci] = +1  # pos1 -> pos3
                else:
                    over_dir[ci] = -1
                cur = trans[cur]
        assert ncyc % 2 == 0, ncyc
        self.ncomp = ncyc // 2
        return {ci: (under_dir[ci], over_dir[ci]) for ci in range(c)}

    def _sign(self, ci):
        du, do = self.ori[ci]
        # under vector pos0->pos2 = (0,+); over vector pos1->pos3 = (-,0)
        ux, uy = 0.0 * du, 1.0 * du
        ox, oy = -1.0 * do, 0.0 * do
        cr = ox * uy - oy * ux
        assert cr != 0
        return +1 if cr > 0 else -1

    def smooth_pairings(self, ci, kind):
        """Positional smoothings (same at every crossing, independent of sign)."""
        if kind == "A":
            return A_PAIRS
        if kind == "B":
            return B_PAIRS
        raise ValueError(kind)

    def circles(self, state):
        """state: tuple of 0(A)/1(B) per crossing. Return # circles."""
        d = DSU(4 * self.c)
        for ci in range(self.c):
            for p, q in self.smooth_pairings(ci, "B" if state[ci] else "A"):
                d.union(4 * ci + p, 4 * ci + q)
        for e, v in self.edge_ends.items():
            (c1, p1), (c2, p2) = v
            d.union(4 * c1 + p1, 4 * c2 + p2)
        return d.count()

    def bracket(self):
        """Kauffman bracket as {expA: coeff}; A-smoothing carries A^{-1}."""
        c = self.c
        res = {}
        for mask in range(1 << c):
            nB = bin(mask).count("1")  # bit=1 -> B-smoothing (weight A^{+1})
            nA = c - nB
            state = tuple((mask >> ci) & 1 for ci in range(c))
            ncirc = self.circles(state)
            base = {2: -1, -2: -1}
            pw = {0: 1}
            for _ in range(ncirc - 1):
                npw = {}
                for e1, c1 in pw.items():
                    for e2, c2 in base.items():
                        npw[e1 + e2] = npw.get(e1 + e2, 0) + c1 * c2
                pw = npw
            shift = nB - nA  # A-smoothing (bit 0) carries A^{-1}
            for e, cf in pw.items():
                res[shift + e] = res.get(shift + e, 0) + cf
        return {e: v for e, v in res.items() if v != 0}

    def jones(self):
        """Jones V(q) as {exp: coeff} via V = (-A^3)^{-w} <K>, A=q^{-1/4}."""
        br = self.bracket()
        w = self.writhe
        sgn = -1 if (w % 2) else 1
        out = {}
        for e, cf in br.items():
            e2 = e - 3 * w
            assert e2 % 4 == 0, f"bracket exp {e2} not divisible by 4 (w={w})"
            q = -e2 // 4
            out[q] = out.get(q, 0) + sgn * cf
        return {e: v for e, v in out.items() if v != 0}

    def state_data(self):
        sA = self.circles(tuple([0] * self.c))
        sB = self.circles(tuple([1] * self.c))
        A_ad = True
        for ci in range(self.c):
            st = [0] * self.c
            st[ci] = 1
            if self.circles(tuple(st)) != sA - 1:
                A_ad = False
                break
        B_ad = True
        for ci in range(self.c):
            st = [1] * self.c
            st[ci] = 0
            if self.circles(tuple(st)) != sB - 1:
                B_ad = False
                break
        gT_num = 2 + self.c - sA - sB
        assert gT_num % 2 == 0 and gT_num >= 0, (sA, sB, self.c)
        return {"sA": sA, "sB": sB, "A_adequate": A_ad, "B_adequate": B_ad,
                "adequate": bool(A_ad and B_ad), "gT": gT_num // 2}


def local_rule_signs(pd):
    """Independent writhe cross-check: KnotAtlas numbers edges increasingly
    along each component (1..2c), so at the under-pair {a,c} resp. over-pair
    {b,d} the incoming edge is the one whose cyclic successor is the other.
    Returns sign list using the same cross-product convention as Diagram."""
    N = max(max(x) for x in pd)

    def incoming(x, y):
        if y == x % N + 1 or (x == N and y == 1):
            return x
        if x == y % N + 1 or (y == N and x == 1):
            return y
        raise AssertionError(f"non-consecutive pair {{{x},{y}}}, N={N}")

    out = []
    for (a, b, cc, d) in pd:
        uin = incoming(a, cc)
        oin = incoming(b, d)
        du = +1 if uin == a else -1
        do = +1 if oin == b else -1
        cr = (-1.0 * do) * (1.0 * du)
        out.append(+1 if cr > 0 else -1)
    return out
