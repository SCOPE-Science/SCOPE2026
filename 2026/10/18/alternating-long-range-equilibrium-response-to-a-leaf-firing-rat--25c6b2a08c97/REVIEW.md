# Scientific review

## Correctness — PASS
The equilibrium problem has a strictly convex coercive potential after the transformation \(z_e=\mu_e^\alpha\). Its Hessian decomposes exactly into positive edge-diagonal terms and positive vertex-incidence rank-one terms. Differentiating the equilibrium under a leaf-rate perturbation gives a single-source Hessian Green vector. Tree-specific quadratic elimination yields strictly positive cavity coefficients and strictly negative parent-to-child transfer factors, so the alternating sign never vanishes for positive rates and \(0<\alpha<1\). Finite-increment monotonicity follows by integration. All assumptions and root-depth conventions are explicit in RESULT.md. The packaged standard-library checker passed 1,440 finite checks; these do not replace the proof.

## Originality — PASS (residual risk disclosed)
Qin's 2026 homogenization theorem gives convergence and uniqueness for this broader underlying model, not the signs of derivatives under leaf-rate perturbations. Couzinié–Hirsch's weak-regime result has unit firing rates; van der Hofstad et al. primarily study the strong-reinforcement stability regime, including path examples. Targeted searches of published mathematical findings and public literature for leaf firing rates, equilibrium sensitivities, alternating edge responses, path and tree forms, and inverse-Hessian formulations found no directly equivalent theorem. A standard tree Schur-complement principle underlies the proof, however, and another named comparative-statics model might encode the result; this is a genuine residual risk. Some later targeted research-database requests returned temporary internal failures, so their absence of results is not treated as evidence.

## Mathematical value — PASS
The result provides an all-parameter, all-size nonlocal response law for a natural interacting reinforced network. Branching does not destroy strict alternating signs, and remote responses remain nonzero however many generations separate the leaf and edge. It supplies exact sensitivity magnitudes with linear-complexity postorder elimination after an equilibrium is known, and contrasts qualitatively with the strictly local unreinforced endpoint. This is not merely a rephrasing of the already-known convergence theorem: uniqueness alone does not determine the direction of cross-edge responses.

## Scope and closest literature
Theorem: finite trees, strictly positive rates, \(0<\alpha<1\), perturb one leaf. Primary sources: Qin arXiv:2610.11780, Couzinié–Hirsch arXiv:2010.03347, van der Hofstad et al. arXiv:1406.0449. Cycles, infinite trees and internal-vertex perturbations are not claimed. Independent comparison with all potentially related comparative-statics formulations has not been performed.

Self-review: passed. Independent audit: not yet performed.
