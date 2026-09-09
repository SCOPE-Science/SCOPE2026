"""Verify the emergent obstruction (stdlib only, exact integer arithmetic).

Replays:
  V1. MacMahon engine check: all-PP(5,5,3) == 731808 (validates backtracker).
  V2. D2 (symmetric except anti-diagonal) recounts at small cells incl. (5,1)=64.
  V3. Paper-formula evaluations (exact Fraction) at a=5 column: 60, 1312, 16572, ...
  V4. a=2 ratio check: printed formula == 2 x table (p_2 = 1/2).
Prints VERIFY_OK iff all hold.
"""
import sys
import time
from fractions import Fraction
from math import comb

sys.path.insert(0, '.')
from enum_qspp import count_qspp

FAIL = []


def check(name, got, exp):
    ok = (got == exp)
    print(f"{name}: got={got} expected={exp} {'OK' if ok else 'FAIL'}", flush=True)
    if not ok:
        FAIL.append(name)


def F(a, C):
    if a == 1:
        return Fraction(comb(C, 1))
    if a == 2:
        return Fraction(C * comb(C + 1, 3))
    if a == 3:
        return Fraction(comb(C + 2, 5)) * Fraction(C * C - 2, 7)
    if a == 4:
        return Fraction(C * comb(C + 3, 7)) * Fraction(41 * C**4 - 229 * C**2 - 892, 23760)
    if a == 5:
        return Fraction(comb(C + 4, 9)) * Fraction(
            683 * C**8 - 8206 * C**6 - 14473 * C**4 - 310644 * C**2 + 756000, 122522400)
    if a == 6:
        return Fraction(C * comb(C + 5, 11)) * Fraction(
            56381 * C**12 - 1850347 * C**10 + 11282865 * C**8 - 28759181 * C**6
            - 1859025278 * C**4 + 20697349128 * C**2 + 194655992832, 161911881331200)
    raise ValueError(a)


t = time.time()
# V1: engine vs MacMahon
check('V1 all-PP(5,5,3)==731808', count_qspp(5, 3, 'none'), 731808)
# V2: D2 agreement cells (definition reconstruction)
for (a, c, exp) in [(2, 2, 20), (3, 3, 272), (4, 3, 3052), (3, 4, 846), (6, 1, 164)]:
    check(f'V2 D2({a},{c})', count_qspp(a, c, 'D2'), exp)
# V2b: a=5 D2 overcounts (the obstruction itself)
for (a, c, d2, tab) in [(5, 1, 64, 60), (5, 2, 1442, 1312)]:
    check(f'V2b D2({a},{c})=={d2}', count_qspp(a, c, 'D2'), d2)
    check(f'V2b formula({a},{c})=={tab}', F(5, c + 5), tab)
# V2c: heavier a=5 cells via formula only + naive D2 (fast: (5,3) 0.0s, (5,4) 0.3s)
check('V2c D2(5,3)==18544', count_qspp(5, 3, 'D2'), 18544)
check('V2c formula(5,3)==16572', F(5, 8), 16572)
check('V2c D2(5,4)==164686', count_qspp(5, 4, 'D2'), 164686)
check('V2c formula(5,4)==145428', F(5, 9), 145428)
# V3: a=2 factor-2 (printed formula double the table => p_2 = 1/2)
for (h, tab) in [(1, 6), (2, 20), (3, 50)]:
    check(f'V3 formula(2,{h})==2*table', F(2, h + 2), 2 * tab)
# V4: beyond-table D2 values at a=7 (first unfitted slice anchors under D2)
check('V4 D2(7,0)==1', count_qspp(7, 0, 'D2'), 1)
check('V4 D2(7,1)==328', count_qspp(7, 1, 'D2'), 328)
check('V4 D2(7,2)==29297', count_qspp(7, 2, 'D2'), 29297)
print(f'elapsed {time.time()-t:.1f}s')
if FAIL:
    print('VERIFY_FAIL:', FAIL)
    sys.exit(1)
print('VERIFY_OK')
