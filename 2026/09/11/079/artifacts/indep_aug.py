"""Independent brute-force augmentation checker: parses printed differential, no library solver."""
import itertools, re, sys

def parse_diff(text):
    diffs = {}
    for line in text.strip().split('\n'):
        m = re.match(r'\s*d\(a\[(\d+)\]\)\s*=\s*(.*)', line)
        if not m: continue
        i, rhs = int(m.group(1)), m.group(2).strip()
        if rhs == '0':
            diffs[i] = []
            continue
        terms = [t.strip() for t in rhs.split('+')]
        polys = []
        for t in terms:
            if t == '1':
                polys.append(())
            elif t == 'LAM':
                polys.append(('LAM',))
            else:
                factors = [f.strip() for f in t.split('*')]
                w = []
                for f in factors:
                    mm = re.match(r'a\[(\d+)\]', f)
                    assert mm, (line, t)
                    w.append(int(mm.group(1)))
                polys.append(tuple(w))
        diffs[i] = polys
    return diffs

def brute_force(diffs, gradings, grading_mod=0):
    # gradings: dict gen -> degree. deg0 test.
    def is0(x):
        return x == 0 if grading_mod == 0 else x % grading_mod == 0
    def is1(x):
        if grading_mod == 0: return x == 1
        if grading_mod == 1: return True
        return x % grading_mod == 1
    deg0 = sorted(g for g, x in gradings.items() if is0(x))
    deg1 = sorted(g for g, x in gradings.items() if is1(x))
    deg0set = set(deg0)
    # filter conditions
    conds = []
    for g in deg1:
        terms = [w for w in diffs[g] if all((f == 'LAM') or (f in deg0set) for f in w)]
        conds.append(terms)
    sols = []
    for bits in itertools.product([0,1], repeat=len(deg0)):
        e = dict(zip(deg0, bits)); e['LAM'] = 1
        ok = True
        for terms in conds:
            tot = 0
            for w in terms:
                t = 1
                for f in w:
                    t &= e[f]
                tot ^= t
            if tot != 0:
                ok = False; break
        if ok:
            sols.append(sorted(g for g in deg0 if e[g]))
    return sols

ATLAS_GR = [3,4,-4,4,-2,-1,-4,-3,-3,-2,-2,-2,-1,-1,0,-1,-1,0,0,0,0,0,1,1,1,1,1]
GRID_GR = [-5,-4,4,-4,-4,-4,-3,-3,-2,-2,-1,-3,-3,-2,-2,-1,-1,0,0,0,0,0,1,1,1,1,1]
ATLAS_DIFF = """
  d(a[1]) = 0
  d(a[2]) = a[1]
  d(a[3]) = 0
  d(a[4]) = a[1]
  d(a[5]) = 0
  d(a[6]) = a[5]
  d(a[7]) = 0
  d(a[8]) = 0
  d(a[9]) = a[3] * a[2] * a[7] + a[7] + a[3] + a[3] * a[4] * a[7]
  d(a[10]) = a[8]
  d(a[11]) = a[3] * a[2] * a[8] + a[8] + a[3] * a[4] * a[8]
  d(a[12]) = 0
  d(a[13]) = a[11] + a[10] + a[3] * a[2] * a[10] + a[3] * a[4] * a[10]
  d(a[14]) = a[5] * a[2] * a[7] + a[5] + a[5] * a[4] * a[7]
  d(a[15]) = a[6] * a[2] * a[7] + a[6] * a[4] * a[7] + a[6] + a[14]
  d(a[16]) = a[12] + a[3] * a[2] * a[12] + a[3] * a[4] * a[12]
  d(a[17]) = a[12]
  d(a[18]) = a[16] + a[3] * a[2] * a[17] + a[17] + a[3] * a[4] * a[17]
  d(a[19]) = 0
  d(a[20]) = 0
  d(a[21]) = a[5] * a[2] * a[8] + a[5] * a[4] * a[8]
  d(a[22]) = 0
  d(a[23]) = 1 + a[19] * a[3] * a[2] + a[19] + a[19] * a[3] * a[4]
  d(a[24]) = 1 + a[20] * a[19]
  d(a[25]) = 1 + a[21] * a[20] + a[5] * a[2] * a[12] + a[5] * a[2] * a[10] * a[20] + a[5] * a[4] * a[12] + a[5] * a[4] * a[10] * a[20]
  d(a[26]) = 1 + a[22] * a[6] * a[2] * a[8] + a[22] * a[6] * a[4] * a[8] + a[22] * a[21]
  d(a[27]) = lam_1 + a[2] * a[7] * a[22] + a[22] + a[4] * a[7] * a[22]
"""
GRID_DIFF = """
  d(a[1]) = 0
  d(a[2]) = a[1]
  d(a[3]) = 0
  d(a[4]) = a[1]
  d(a[5]) = 0
  d(a[6]) = 0
  d(a[7]) = a[6]
  d(a[8]) = 0
  d(a[9]) = a[8]
  d(a[10]) = 0
  d(a[11]) = a[10]
  d(a[12]) = a[4] + a[4] * a[3] * a[5] + a[2] + a[5] + a[2] * a[3] * a[5]
  d(a[13]) = a[4] * a[3] * a[6] + a[2] * a[3] * a[6] + a[6]
  d(a[14]) = a[13] + a[4] * a[3] * a[7] + a[2] * a[3] * a[7] + a[7]
  d(a[15]) = a[4] * a[3] * a[8] + a[2] * a[3] * a[8] + a[8]
  d(a[16]) = a[15] + a[4] * a[3] * a[9] + a[9] + a[2] * a[3] * a[9]
  d(a[17]) = a[4] * a[3] * a[10] + a[10] + a[2] * a[3] * a[10]
  d(a[18]) = a[17] + a[4] * a[3] * a[11] + a[11] + a[2] * a[3] * a[11]
  d(a[19]) = 0
  d(a[20]) = 0
  d(a[21]) = 0
  d(a[22]) = 0
  d(a[23]) = 1 + a[19] * a[4] * a[3] + a[19] + a[19] * a[2] * a[3]
  d(a[24]) = 1 + a[20] * a[19]
  d(a[25]) = 1 + a[21] * a[20]
  d(a[26]) = 1 + a[22] * a[21]
  d(a[27]) = lam_1 + a[3] * a[6] + a[3] * a[5] * a[22] + a[22]
"""
if __name__ == '__main__':
    for tag, diff, gr in [('ATLAS', ATLAS_DIFF, ATLAS_GR), ('GRID', GRID_DIFF, GRID_GR)]:
        diffs = parse_diff(diff.replace('lam_1', 'LAM').replace('λ_1', 'LAM'))
        gradings = {i+1: gr[i] for i in range(len(gr))}
        sols = brute_force(diffs, gradings, 0)
        print(tag, 'Z-augs:', sols)
        sols2 = brute_force(diffs, gradings, 2)
        print(tag, '#2-augs:', len(sols2))
