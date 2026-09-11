"""Jones polynomial of plat closures via Kauffman bracket; calibrated: trefoil [2,2,2] -> m3_1."""
import itertools, sys
sys.path.insert(0, 'extlib')
from collections import defaultdict

def bracket_of_closure(word, nstrands, a_smooth='horiz'):
    n = nstrands; c = len(word)
    def count_circles(choices):
        parent = list(range(n + 4*c + n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        def union(x,y):
            parent[find(x)]=find(y)
        T = list(range(n))
        cur = list(T)
        for k,i in enumerate(word):
            i0 = i-1
            base = n+4*k
            in0, in1, out0, out1 = base, base+1, base+2, base+3
            union(cur[i0], in0); union(cur[i0+1], in1)
            if (choices[k]==0) == (a_smooth=='horiz'):
                union(in0,in1); union(out0,out1)
            else:
                union(in0,out0); union(in1,out1)
            cur[i0],cur[i0+1] = out0,out1
        B0 = n+4*c
        B = [B0+j for j in range(n)]
        for j in range(n):
            union(cur[j], B[j])
        for j in range(0,n-1,2):
            union(T[j],T[j+1]); union(B[j],B[j+1])
        return len(set(find(x) for x in range(n+4*c+n)))
    terms = defaultdict(int)
    for bits in itertools.product([0,1], repeat=c):
        na = bits.count(0); nb = c - na
        circles = count_circles(bits)
        exp0 = na - nb
        poly = {0:1}
        for _ in range(circles-1):
            new = defaultdict(int)
            for e,cf in poly.items():
                new[e+2] -= cf; new[e-2] -= cf
            poly = new
        for e,cf in poly.items():
            terms[exp0+e] += cf
    return {e:c for e,c in terms.items() if c != 0}

def trace_writhe(word, nstrands):
    n = nstrands; c = len(word)
    cross_dirs = [[] for _ in range(c)]
    seen = set(); pos = ('T', 0); steps = 0
    while True:
        side, s = pos
        if (side, s) in seen: break
        seen.add((side, s))
        s2 = s ^ 1
        if side == 'T':
            cur = s2
            for k, i in enumerate(word):
                if cur == i-1 or cur == i:
                    cross_dirs[k].append('D')
                    cur = i-1 + i - cur
            pos = ('B', cur)
        else:
            cur = s2
            for k in range(c-1, -1, -1):
                i = word[k]
                if cur == i-1 or cur == i:
                    cross_dirs[k].append('U')
                    cur = i-1 + i - cur
            pos = ('T', cur)
        steps += 1
        if steps > 2*n+2: break
    nvis = sum(len(v) for v in cross_dirs)
    is_knot = (nvis == 2*c)
    w = 0
    for k in range(c):
        ds = cross_dirs[k]
        if len(ds) == 2:
            w += 1 if ds[0]==ds[1] else -1
    return w, is_knot

def jones_t_exps(word, nstrands):
    """Return Jones polynomial as {t-exponent (int, t=q): coeff} using t=A^-4 and w_eff=-w_trace."""
    br = bracket_of_closure(word, nstrands)
    w, is_knot = trace_writhe(word, nstrands)
    weff = -w
    out = defaultdict(int)
    for e, cf in br.items():
        out[e - 3*weff] += cf * ((-1)**(-weff))
    # convert A^e -> t^(-e/4); require e % 4 == 0
    res = {}
    for e, cf in out.items():
        if cf == 0: continue
        assert e % 4 == 0, (word, e)
        res[-e//4] = cf
    return res, is_knot

def fmt(p):
    return ' + '.join(f'{c}*t^{e}' for e,c in sorted(p.items()))

if __name__ == '__main__':
    # Jones(7_2) = -q^-8+q^-7-q^-6+2q^-5-2q^-4+2q^-3-q^-2+q^-1 (katlas)
    # Jones(m7_2) mirrors: -q^8+q^7-q^6+2q^5-2q^4+2q^3-q^2+q
    J72 = {-8:-1,-7:1,-6:-1,-5:2,-4:-2,-3:2,-2:-1,-1:1}
    Jm72 = {-e:c for e,c in J72.items()}
    print('target m7_2:', fmt(Jm72))
    print('trefoil check:', fmt(jones_t_exps([2,2,2],4)[0]), '(expect mirror trefoil: t^-1+t^-3-t^-4)')
