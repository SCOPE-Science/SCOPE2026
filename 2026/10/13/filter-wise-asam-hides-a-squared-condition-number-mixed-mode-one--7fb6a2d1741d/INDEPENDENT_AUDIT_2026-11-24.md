# Independent mathematical audit

## correctness

PASS

In Kwon et al. arXiv v1 p.8, the paragraph following Eq. (5) explicitly prescribes T_w + eta I rather than T_w for stability; Eq. (5) alone is the unshifted definition. In Algorithm 1 at p.12 the p=2 perturbation and shifted outer gradient give the frozen expression on setting weight decay to zero and using one filter. At Rv, put b=rho(1+tau/R)/||Av||. Direct substitution gives x^+/R=v-alpha(A+b A^2)v. The inner product with v is m1+b m2 and the squared norm of the update direction is m2+2b m3+b^2 m4, where v^T A^j v=1-kappa^-2+kappa^(j-2). These give exactly the stated positive coefficients, strict contraction below 2A_{kappa,R}/B_{kappa,R}, equality at the boundary and expansion above it. At fixed positive rho, the large-radius coefficients have A tending to 1+rho sqrt(2) as kappa grows and B/kappa^2 tending to rho^2/2. The axes have multiplier 1-alpha lambda[1+rho(1+tau/R)]. Even a uniform-in-R reading of the large-R separation holds: the kappa expansions are uniform for s=1+tau/R in a fixed compact interval [1,1+tau/R0], and the limiting scaled mixed threshold 4(1+rho s sqrt(2))/(rho s)^2 decreases with s. The calculation excludes x=0, where the normalized gradient is undefined; it is neither an orbit-divergence result nor an optimality claim over all directions. Inspected frozen verify.py as a numerical guard, not as a proof. Independent exact rational replay: python3 /workspace/review_evidence/3_exact_witness.py, giving threshold 2597/25969, mixed squared ratio 3348049/3062500 > 1 at alpha=11/100, and pure norm ratios 81/125 and 19/25.

## originality

PASS

The distinct claim supported here is the high-condition-number mixed-direction one-step Euclidean threshold and its explicit separation from both axes for one-filter p=2 ASAM. No inspected source gives it or a stronger result under the same hypotheses; the source algorithm itself is fully credited.

## value

PASS

The balanced-gradient state is motivated by the interaction of the inner normalized gradient and the outer Hessian; it is not an arbitrary parameter slice. Its exact threshold shows that testing both eigenvectors can miss an entire condition-number factor even under the published additive stabilizer at large radius. That is useful as a sharp counterexample to an axis-based one-step contraction heuristic, without claiming general convergence or practical learning-rate prescriptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
