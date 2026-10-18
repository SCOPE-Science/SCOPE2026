# Independent mathematical audit

## correctness

PASS

For the centered transition operator, T phi_{i+1}=lambda_i phi_i and T h=0 off the finite span. Therefore lag-k covariance is a^T J^(k) a, with J^(k)_(i,i+k)=(product lambda)/2. Its graph is a disjoint union of paths with alternating-sign conjugation DJD=-J, so its eigenvalue extrema are ±||J|| and achieved by real finite-span scores. Expanding Var(sum_0^{N-1} f(X_i))/N gives the real symmetric H_N with diagonal 1 and offdiagonal (1-|i-j|/N) product lambda when |i-j|<N; the orthogonal h component contributes ||h||², while min eig(H_N)<=1<=max eig(H_N). Rayleigh proves sharp finite-N and limiting endpoints for every nonconstant real L² score. The admissible trigonometric example m=2, lambda=(1/4,1/4), score vector (1/2,1/sqrt(2),1/2) gives covariance sqrt(2)/8>1/8; its H eigenvalues are 15/16 and (33±sqrt(129))/32, independently recomputed with SymPy. Copula density remains nonnegative since |phi_i phi_{i+1}|<=2. Zero coefficients and N=1 are included.

## originality

PASS

Longla (2026) Theorem 4.4(2) explicitly asserts a coefficient-half upper bound, and its proof optimizes a single adjacent basis pair, missing constructive interference from two neighboring links. The claimed spectral repair, exact sharp lag profile and finite/asymptotic score-uniform variance endpoints are not provided there; they genuinely contradict the printed general upper bound, as checked against the open-access full article. Classical Rayleigh and Toeplitz spectra are prior mathematical ingredients, not claimed new.

## value

PASS

The exact sharp same-score dependence envelopes and all-N variance inflation/deflation factors correct a quantitatively false published theorem in a nonreversible finite-memory model; the same family covers all m and all real L² scores, rather than a tiny isolated negative check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
