# Independent mathematical audit

## correctness

PASS

Found a material error in assigned RESULT.md: finite grid covariance eigenvalues Λ_{r,q}^{(k)} are exactly [16k² sin²(pi r/(2k)) sin²(pi q/(2k))]^{-1}, hence Λ_{r,q}^{(k)}∼k²/(π⁴r²q²); unscaled fixed-mode eigenvalues do NOT tend to (π⁴r²q²)^{-1}. Confirmed Λ_11 numerically at k=4,8,16,32,64 as 0.18213835,0.67415093,2.64503815,10.52926762,42.06635391, while Λ/k²→π^{-4}. Complete corrected RESULT.md supplies the entire original scientific theorem and six-stage proof with *mesh-normalized* limit k^-2Λ→(π⁴r²q²)^-1. Reconstructed permutation finite-population covariance and Dirichlet 1/(m+1) factor; independent exact grid covariance by all permutation enumeration for k=3,4,5. Lyapunov factorial bound gives finite-dimensional Gaussian limits, eighth-moment Rosenthal + Kolmogorov gives continuous tightness, and summable union bound gives coupling-independent almost-sure unscaled collapse; finite checks alone are not the infinite proof.

## originality

PASS

The *corrected final claim* adds functional Gaussian convergence, full continuous covariance kernel, mesh-area-normalized discrete-sine spectrum, and coupling-independent unscaled uniform collapse for Dirichlet permutation copulas; primary Kokol Bukovšek–Mojškerc–Stopar supply related pointwise grid variance and covariance reduction but not the fully asserted functional result in inspected full text. The raw fixed-index eigenvalue convergence statement in assigned RESULT was mathematically false and is replaced by the true k^-2 eigenvalue limit.

## value

PASS

A functional two-parameter Gaussian limit for a new permutation-copula distribution, exact finite-dimensional covariance kernel, complete grid sine spectrum, and almost-sure uniform collapse are natural probabilistic invariants. The corrected k^-2 scaling matters for comparing discrete covariance matrices to a continuum operator; this is not merely a cosmetic error. The result remains substantial after genuine repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
