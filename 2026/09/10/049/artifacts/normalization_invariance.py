# Normalization invariance replay (N- and minimality-preserving reductions).
# Checks (a) x-shift exact, (b) vertical shift exact, (c) scaling (D scaled),
# (d) linear shift (D shifted), (e) x-scaling (D scaled by b, N invariant),
# on 20 random polys, plus x^{d-1}-kill feasibility (d invertible mod 13).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direc import ndirs_of_vals, eval_coeff
import numpy as np
P = 13
if __name__ == '__main__':
    rng = np.random.default_rng(3)
    for t in range(20):
        d = int(rng.integers(1, 12))
        C = [int(v) for v in rng.integers(0, 13, size=d + 1)]
        C[d] = int(rng.integers(1, 13))
        f = eval_coeff(C)
        D0 = ndirs_of_vals(f)
        c = int(rng.integers(0, 13))
        k = int(rng.integers(0, 13))
        a = int(rng.integers(1, 13))
        m = int(rng.integers(0, 13))
        b = int(rng.integers(1, 13))
        assert ndirs_of_vals(np.array([int(f[(x + c) % P]) for x in range(P)])) == D0
        assert ndirs_of_vals((f + k) % P) == D0
        assert ndirs_of_vals((a * f) % P) == {(a * v) % P for v in D0}
        assert ndirs_of_vals((f + m * np.arange(P)) % P) == {(v + m) % P for v in D0}
        Cb = [0] * (d + 1)
        for i in range(d + 1):
            Cb[i] = (C[i] * pow(b, i, P)) % P
        # x-scaling re-indexes pairs: D(g) = b*D(f) (N invariant, N-class preserved)
        assert ndirs_of_vals(eval_coeff([int(x) for x in Cb])) == {(b * v) % P for v in D0}
    assert all((d * pow(d, -1, 13)) % 13 == 1 for d in range(1, 13))
    print('NORMALIZATION_INVARIANCE_OK (20 trials, (a)-(e) + shift feasibility)')
