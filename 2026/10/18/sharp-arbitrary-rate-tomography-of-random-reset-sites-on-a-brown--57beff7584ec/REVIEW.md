# Scientific review: Sharp arbitrary-rate tomography of random reset sites on a Brownian ring

## Correctness — PASS

The killed-diffusion boundary-value problem and renewal formula are derived with all boundary conditions. The strict total positivity lemma uses an absolutely convergent cosh power series and a positive Cauchy–Binet Vandermonde term. This proves arbitrary-rate injectivity for at most \(N\) atoms, including folded distance zero. A Chebyshev/Hankel/Prony extraction, the open-parameter invariance-of-domain lower bound, and compact moment uniqueness close the proof. The supplied executable tests reconstruct up to four atoms exactly, exercise high-precision inverse and PDE checks, and sample cosh-kernel determinants. The theorem remains an exact-noiseless statement, not a stable statistical estimation guarantee.

## Originality — PASS (residual uncertainty)

Julián-Salgado et al. (arXiv:2605.08414v1, May 8, 2026) already give the ring reset forward mean first-passage identity and mirror symmetry (section IV, equations 27–28). These are NOT new. Méndez et al. (arXiv:2401.01125) treat random resetting locations; Abundo (arXiv:2410.16889) studies other inverse FPT observations; classical Prony reconstruction is known (Kunis et al., doi:10.5802/smai-jcm.53). No comparison directly yielded the conjunction of unknown multi-site recovery from any \(2N-1\) scalar rate-resolved means, a sharp minimality proof, and complete mirror quotient. The full text of the Abundo source was not established as accessible, and general inverse-transform theory might implicitly cover components; an unlocated dominating result remains possible. The exact comparisons and accessible inspection scopes are recorded in AUDIT.json.

## Value — PASS

The result establishes a minimum natural experimental observation count for determining unknown reset-site mixtures, with a constructive design and a physical nonidentifiability theorem for orientation. It distinguishes information recoverable from transport measurements from information fundamentally unavailable, and is not merely another forward simulation. The initial/reset distributions must agree, and diffusivity and ring length must be known.

Self-review: passed. Independent audit: not yet performed.
