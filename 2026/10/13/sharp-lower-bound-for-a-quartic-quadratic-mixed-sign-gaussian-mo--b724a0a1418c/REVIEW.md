# Independent mathematical audit

## correctness

PASS

For centered unit-variance jointly Gaussian X,Y,Z and 0<u<1, put t=1−u, r=E[XY]² and T=t(t+2). Gaussian orthogonal coordinates realize Y=aX+√(1−r)W and Z=kX+ℓW+mV with a=E[XY] and k²+ℓ²+m²=1; at r=1 the independent coordinates can be chosen for the residual of Z. Dividing by M=E|X|^{−u}, the weighted even X-moment of order 2j is t(t+2)…(t+2j−2). Independent expansion of the sixth-degree polynomial yields the stated block quadratic form. A−T>0: r²(t²−1)≥r(t²−1), and the stated lower bound has positive constant 1−t after factoring t. The shifted 2×2 determinant is t(1−r)(1−t)(t+5)K, with K a strictly positive Bernstein combination on 0≤r≤1. Also D−T=(1−r)(1−t)(3+t−r(3−t)), strictly positive for r<1. These show strictness for r<1 and positive semidefiniteness at r=1. At r=1, Y=±X and the shifted form equals (A−T)k², so equality is exactly k=0, which by joint Gaussianity means Z independent of X. Taking Z independent and r↑1 yields positive-definite approximants, also proving the nonattained infimum in that restricted class. The marginal product normalization divides T by 3. Ran the independent symbolic replay `python3 -B /workspace/reviews/replay_3.py` (SymPy 1.14.0), expanding the Gaussian moment and checking the determinant and diagonal identities as polynomial identities, including r=1. Inspected but did not execute the packaged rational diagnostic. The signs over all real parameters are analytic, not certified by samples.

## originality

PASS

The precise supported addition is the optimal covariance-free lower constant and complete equality classification for (−u,4,2), not a general mixed-sign Gaussian inequality. The inspected broadly applicable comparison bounds degenerate near the extremizer and cannot provide this infimum. No equivalently strong claim was found in the adjacent indexed records or available primary statements.

## value

PASS

The first unequal even positive power pair in a published mixed-sign comparison regime is a motivated nontrivial test. Its exact positive uniform lower constant fills a quantitative gap left by the degenerating bounds, and the equality description explains why a positive-definite search would only approach the minimum. This is useful without a claim about all exponent patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
