# Independent audit — 2026-10-01

## Record

**Reverse-order averaging cancels first-order underrelaxation bias in cyclic block Kaczmarz**

Final claim: For finite-dimensional cyclic relaxed orthogonal projections with \(S=\sum_iP_i\succ0\), the cyclic fixed point has \(z_\pi(\lambda)=x_*+\lambda h_\pi+O(\lambda^2)\), where \(h_\pi=S^{-1}\sum_{p<q}P_{\pi_q}r_{\pi_p}\); reversing the order gives \(h_{\pi^R}=-h_\pi\), so the midpoint of the two opposite cyclic fixed points is \(x_*+O(\lambda^2)\), and this order is sharp.

Disposition: **PASSED**

## Correctness — PASS

For \(0<\lambda<2\), each factor has an exact norm-decrease identity and the positive-definite sum of projectors makes the full linear sweep a strict contraction. Expanding the ordered product and affine term through second order gives the stated analytic fixed-point branch. The residual identities \(\sum_i r_i=0\) and \(P_ir_i=r_i\) make the forward and reverse coefficients cancel exactly. Direct expansion of the scalar three-block example gives a nonzero quadratic midpoint error, proving sharpness.

## Originality — PASS

The complete 1983 Censor–Eggermont–Gordon paper was inspected at the pages deriving the complete-cycle matrix, fixed point, and strong-underrelaxation asymptotics. It proves convergence to weighted least squares using only the leading \(O(\lambda)\) perturbation and does not state the explicit first-order order bias or reverse-order cancellation. Later symmetric Kaczmarz/SOR compositions are algorithmically different from averaging two separately converged cyclic fixed points. No earlier equivalent statement was found in Resultary or the inspected Kaczmarz literature.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Source inspections distinguish material actually read from inaccessible full text.

## Scientific value — PASS

The theorem turns a qualitative underrelaxation limit into an explicit error model, isolates the block-order effect, and gives a simple symmetrization that gains one asymptotic order with a sharp example. This is a motivated numerical-analysis refinement with direct diagnostic and correction value.

## Checked scientific sources

- Y. Censor, P. P. B. Eggermont and D. Gordon, Strong underrelaxation in Kaczmarz's method for inconsistent systems, Numer. Math. 41 (1983), DOI:10.1007/BF01396307.
- C. Popa, Least-squares solution of overdetermined inconsistent linear systems using Kaczmarz's relaxation, Int. J. Comput. Math. 55 (1995), DOI:10.1080/00207169508804364.
- Resultary semantic search for Kaczmarz reverse-order underrelaxation bias, cyclic fixed-point expansions, and strong underrelaxation.

## Residual risks

- The full Popa 1995 article was not inspected end-to-end; a specialized opposite-order fixed-point correction there remains a residual coverage risk. Generic forward/reverse symmetrization is known in splitting theory, but it does not itself imply the audited fixed-point coefficient.

## Verification boundary

The audit reconstructed the mathematical argument from the record and performed fresh logical or algebraic checks where needed. Existing package logs were treated only as reproducibility evidence. No formal proof-assistant verification or expert attestation is asserted.
