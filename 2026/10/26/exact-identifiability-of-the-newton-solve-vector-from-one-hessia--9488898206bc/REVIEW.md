# Review

## Correctness — PASS

The claim is an exact characterization over all symmetric positive-definite completions consistent with one observed product. The forward implication follows from \(A^{-1}g=\alpha A^{-1}(Av)=\alpha v\). For the converse, after choosing coordinates with \(v=e_1\), the family \(A_D=\begin{psmallmatrix}a&b^{\mathsf T}\\b&D\end{psmallmatrix}\) preserves the observed first column while varying the positive-definite Schur complement. Since \(g\notin\operatorname{span}\{y\}\), every solution has a nonzero component orthogonal to \(v\); replacing \(D\) by \(D+\tau I\) cannot leave the solution unchanged. The exact rational witness is checked by `verify_example.py`.

## Originality — PASS

The closest primary source is Ansari-Önnestam and Forsgren, “Finite Newton-Step Generation via Subspace Quasi-Newton Methods for Quadratic Problems” (arXiv:2407.03072). Its Proposition 4.1 establishes sufficiency of curvature information on a subspace of dimension at most two for a recursive subspace quasi-Newton construction. It does not state the one-observation identifiability classification proved here. published-finding corpus searches returned no direct equivalent among the closest retrieved findings; nearby BFGS/Hessian-recovery records concern convergence along a trajectory, not ambiguity among SPD completions sharing one Hessian-vector product. This is a complementary oracle statement, not a claim that the source's two-direction algorithm is necessary in every setting.

## Value — PASS

The criterion gives a precise exception to the general ambiguity of one Hessian-vector observation: exact recovery of the Newton solve vector is possible precisely when the gradient is parallel to the observed image \(Av\). This isolates when a single curvature query suffices and provides a rigorous information limit motivating additional curvature information when the condition fails. The result is deliberately narrow and does not claim a general complexity lower bound for adaptive multi-query methods.

## Closest literature and residual risk

The full arXiv text was inspected, including the abstract, introduction, and Section 4 Proposition 4.1. published-finding corpus searches targeted one-product Newton-step identifiability and the two-direction finite-Newton-step result. Classical oracle-complexity literature may contain an equivalent lemma; no such direct coverage was identified in the checked results. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
