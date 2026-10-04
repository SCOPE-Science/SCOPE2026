# Same-model review of Exact Hessian recovery inside a Q-order-one BFGS trajectory

## Correctness
PASS. The proof reconstructs all needed identities from the cited trajectory. The key perturbation estimate is \(y_k-s_k=\Delta_k-\Delta_{k+1}\), and the source's limits \(|\delta_k|/r_k\to0\) and \(r_{k+1}/r_k\to0\) imply \(\|y_k-s_k\|/\|s_k\|\to0\). The two-dimensional block structure, secant relation, and exact orthogonality \(y_{k-1}^\top s_k=0\) then give the displayed determinant identity. Combining determinant convergence with the next secant relation forces every entry of the active \(2\times2\) block to converge to the identity. The orthogonal complement is exactly the identity throughout.

The determinant identity for Hessian-form BFGS is standard and is also recorded in Jin-Jiang-Mokhtari. All denominators are strictly positive by positive definiteness and strong convexity. The source's final scaling leaves the quasi-Newton matrices unchanged and preserves \(\nabla^2F(0)=I_n\).

## Originality
PASS. Full-text inspection of arXiv:2609.00596 found its stated conclusions to concern the iterate sequence: nontermination, Q-superlinear convergence, and exact minimum adjacent Q-order one. The construction establishes positivity and a two-dimensional block form for the BFGS matrices, but does not state \(B_k\to I_n\). Targeted statement-level searches for matrix convergence, Hessian-approximation convergence, and Q-order-one BFGS did not locate the determinant consequence proved here. The closest recent exact-line-search BFGS rate paper treats global linear/superlinear function-value rates and the determinant potential, not this matrix-recovery property of the counterexample.

Residual risk remains that an older or less-indexed quasi-Newton source contains an equivalent special-case lemma, so the claim is limited to the mathematical implication established for this trajectory and does not assert exhaustive historical priority.

## Value
PASS. The result separates two notions that are often conflated in quasi-Newton convergence discussions. The Liu-Li-Wen trajectory has the weakest possible fixed adjacent Q-order compatible with Q-superlinearity, yet its entire approximate Hessian converges to the true Hessian in operator norm. Thus poor full-matrix recovery cannot explain the Q-order-one boundary in this construction. This is a structural clarification stronger than the usual directional Dennis-Moré approximation condition.

## Closest literature and limitations
The primary comparison is arXiv:2609.00596. Dennis-Moré (1974) supplies the classical directional characterization of superlinear quasi-Newton convergence. Jin-Jiang-Mokhtari (2026) supplies non-asymptotic exact-line-search BFGS rates and the standard determinant identity. None of the inspected statements covers the simultaneous combination of exact Q-order one and full operator-norm Hessian recovery on the Liu-Li-Wen trajectory.

Same-model review: passed. Independent audit: not yet performed.
