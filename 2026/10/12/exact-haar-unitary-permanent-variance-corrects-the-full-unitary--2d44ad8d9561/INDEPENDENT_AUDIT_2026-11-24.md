# Independent mathematical audit

## correctness

PASS

On full U(n) with normalized Haar measure, the unit symmetrization of e_1⊗…⊗e_n has diagonal matrix coefficient perm(U) in Sym^n(C^n): each of the n! summands in the bra contributes the same sum of permanent monomials. This irreducible representation has dimension binom(2n−1,n); the Haar average of the rank-one projector is the identity divided by that dimension. Scalar phase invariance gives mean zero, so the second moment is the variance. The ratio equals the product of (n+j)/n over j=0,…,n−1, strictly above one for n≥2 and one at n=1; Stirling's ratio Γ(2n)/[Γ(n)n^n] gives the stated 2^(−1/2)(4/e)^n. The central-binomial estimate gives the stated RMS, and Markov gives exactly q(n)/R_n for any fixed positive polynomial q. Rivin v3 really applies the erroneous variance to the entire Haar unitary; §8.3 separately writes n!/poly(n) as the PACC threshold and then argues using σ²/poly(n). The original review claim controls the latter variance-based scale (and a fortiori the larger threshold on a literal full-Haar reading); it does not identify these two source thresholds or refute Gaussian-submatrix PACC. No conclusion about Gaussian shape at correct full-Haar scale. Inspected VERIFICATION.md and artifacts/verify.py; finite arithmetic script not run or needed for the analytic proof.

## originality

PASS

The exact moment is prior coverage, and the ratio and Markov estimate are routine once the true scale is known. Pass applies to the specific diagnosis and propagation of Rivin v3's incompatible full-Haar normalization through its typical-size/anti-concentration discussion, not to the second-moment formula as a new theorem.

## value

PASS

The correction reverses a specific published-in-preprint probability inference for a standard ensemble, from near one to exponentially small even with any polynomial slack. It sets the RMS benchmark necessary to interpret full-Haar numerical experiments and avoids transferring a Gaussian-entry conjecture to a different ensemble at an incompatible scale. The specific quantitative error and its consequence justify the correction; the standalone classical identity or generic use of Markov would not.

The dated certificate retains the supplied scientific assessment, sources and limitations.
