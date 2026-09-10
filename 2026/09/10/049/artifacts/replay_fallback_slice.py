# Independent replay of the preset-fallback slice (pure-Python set-of-slopes).
# Family: monic degree-7, f(0)=0, x^6 coeff 0, a1 FREE -> 13^5 = 371293 reps.
# Prints FALLBACK_SLICE_REPLAY_OK iff zero reps have exactly 9 directions.
# (Executed 2026-09-10: total 371293 hist {8:13, 11:117, 12:1196, 13:369967} n9 0.)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direc import ndirs_of_vals, eval_coeff
P = 13
if __name__ == '__main__':
    n9 = 0
    hist = {}
    idx = 0
    for a5 in range(P):
        for a4 in range(P):
            for a3 in range(P):
                for a2 in range(P):
                    for a1 in range(P):
                        C = [0, a1, a2, a3, a4, a5, 0, 1]
                        n = len(ndirs_of_vals(eval_coeff(C)))
                        hist[n] = hist.get(n, 0) + 1
                        if n == 9:
                            n9 += 1
                            print('SURVIVOR', C)
                        idx += 1
    print('total', idx, 'hist', hist, 'n9', n9)
    assert idx == 13 ** 5 and n9 == 0
    print('FALLBACK_SLICE_REPLAY_OK')
