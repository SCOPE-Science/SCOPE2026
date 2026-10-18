# Independent mathematical audit

## correctness

PASS

Residual identity I−AX_k=(I−αA)^{2^k} gives X_k=q_{2^k}(A) with q_m(λ)=[1−(1−αλ)^m]/λ>0 on spectrum (0,2/α). For every even m the geometric-series derivative is strictly decreasing in λ: numerator 1−mu^{m−1}+(m−1)u^m>0 for −1<u<1, u=1−αλ. For 2×2 SPD Stieltjes A, q_m(A)=c0I+c1A, c1<0, so off-diagonal is nonnegative and diagonal positive; n1 trivial. Exact independent rational recurrence confirms example A SPD det1267/500, 2I−A SPD det73/500 (so spectral convergence), inverse entries positive, X2_13=−1/500 while X1≥0. Finite witness plus all-input n≤2 analytic proof establishes sharp dimension.

## originality

PASS

PASS for sharp entrywise sign preservation vs loss under convergent scalar-start Newton–Schulz on SPD Stieltjes matrices; standard iteration and convergence were known.

## value

PASS

Entrywise positivity matters for M-matrix numerical schemes (monotone comparison and positivity-constrained approximate inverse/preconditioning). The exact two-dimensional safe regime and explicit stable three-dimensional failure sharply delimit a natural structural property of a classical inverse iteration. Sign defects are strict and robust, not floating-point artifacts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
