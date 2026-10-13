# Self-review

## Correctness — PASS
The claim is restricted to a deterministic noneigenvector and independent finite-row real Gaussian sketch. The orthogonal Gaussian decomposition gives the exact Student law including normalization; the endpoint quadratic bound gives the attained sharp positivity probability; beta endpoint asymptotics and the Student central limit theorem give both sample-budget limits. The positive density at every distinct eigenvalue gives the complete \(p<1\) moment threshold and the logarithmic safeguard coefficient. Reproduction from the actual standalone `verify.py` returned `VERIFY_OK` with 74 checks. Those calculations are supporting evidence, not substitutes for the general proof.

## Originality — PASS, with residual risks
The closest inspected papers concern sketched Jacobi–Davidson under separation (Grigori–Park–Simunec, arXiv:2609.29651v1), square complex-Gaussian randomized Petrov–Galerkin eigenpair extraction (Shao, arXiv:2604.01037v3), and general sketched eigensolver stability (Nakatsukasa–Tropp, arXiv:2111.00113v2). Their material findings do not imply the exact law **for the stated real, tall, fixed-vector quotient**, the attained optimal spectral-ratio positivity envelope, and especially the conditioned shift's entire inverse-gap moment spectrum and regularization coefficient. Student tails and the spectral interval variance bound are classical and receive no separate novelty credit. Equivalent results could occur under regression, ratio-of-Gaussian or spectral shifting terminology; absence from searched sources is not proof of uniqueness.

## Mathematical value — PASS
The exact probability budget quantifies how many rows are needed for positive one-vector Ritz shifts in SPD systems at a fixed spectral ratio. The inverse-gap theorem reveals a nontrivial moment pathology unaffected by any finite sketch width and measures precisely the benefit of a spectral-gap floor. These are actionable mathematical risk descriptors of a natural sketched eigenvalue extraction primitive, not arbitrary parameter slices. No claim is made about adaptive or structured-sketch solvers or observed finite-precision failure.

Self-review: passed. Independent audit: not yet performed.
