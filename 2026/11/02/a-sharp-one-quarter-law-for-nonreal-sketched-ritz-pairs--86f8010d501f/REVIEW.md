# Review of the circular sketched Ritz law

## Correctness

**PASS.** The reduction \(H=K+gr^{\mathsf T}\) follows directly from exact trial-plane embedding and the rank-one residual decomposition. The two-by-two characteristic discriminant is calculated explicitly. Independent sign changes permit nonnegative residual coordinates; a nonreal pair then requires the single angular quadrant \(g_1>0>g_2\). For balanced residual coordinates, the event becomes a one-variable trigonometric inequality whose exact angular measure gives the displayed probability, unique maximizing ratio, and limiting behavior. A Sylvester-criterion proof checks positive definiteness of the attaining example, and its sketch Gram matrix has explicit eigenvalues. The standalone symbolic verifier and rational checks passed. Numerical simulation is supplementary, not the proof of the one-quarter law.

## Originality

**PASS, with historical-priority risk.** The direct source arXiv:2610.22261v1 introduces real Schur extraction for possible complex sketched Ritz values but the inspected definitions, main contributions, and algorithm sections do not supply a sharp isotropic-angle probability. Nakatsukasa–Tropp (2024), §6.8, establishes the qualitative phenomenon but not its exact angular frequency or arbitrarily-near-isometric attaining family. Standard symmetric-matrix perturbation theory can imply the half-gap sufficient condition and that part is not claimed as independently new. The claim is the exact universal one-quarter measure and its sharp probabilistic profile for the stated sketch ensemble. The remaining sections of the 2026 paper could not be checked line by line; the residual risk of an equivalent older special computation remains.

## Mathematical value

**PASS.** Nonreal projected eigenvalues force a choice between complex eigensolvers and real Schur treatment. The theorem gives a finite-dimensional, reproducible, sharp risk law and illustrates a gap-dependent limitation of embedding distortion alone. The fixed-norm isotropic cross-coupling distribution is specified exactly, making clear when the law is applicable. The result does not make a universal claim about industrial random sketches or full eigensolver convergence.

## Closest coverage and limits

Primary comparisons: Liu–Liu (2026), https://arxiv.org/html/2610.22261, §§1–3 and accessible theoretical overview; Nakatsukasa–Tropp (2024), https://tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf, §6.8; Shao (2026), https://arxiv.org/abs/2604.01037. Distinctive assertion: the exact sharp \(1/4\) upper bound over uniformly oriented fixed-length rank-one cross-couplings, attained while whole-space embedding distortion tends to zero on a varying SPD family. Limits: rank-one residual, dimension-two trial space, circular sketch ensemble, and lack of independent historical-priority certification.

Self-review: passed. Independent audit: not yet performed.
