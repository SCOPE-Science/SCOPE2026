# Exact identifiability of the Newton solve vector from one Hessian-vector observation

## Finding

Let \(n\ge2\), let \(A=A^{\mathsf T}\succ0\) be an unknown Hessian, and let \(g\in\mathbb R^n\) be a known gradient. A single exact Hessian-vector observation gives \(y=Av\) for a chosen nonzero vector \(v\). Define the Newton solve vector by \(p=A^{-1}g\); the conventional Newton step is \(-p\). Among all symmetric positive-definite matrices consistent with the observation, \(p\) is uniquely determined **if and only if** \(g\in\operatorname{span}\{y\}\). In that exceptional case, if \(g=\alpha y\), then \(p=\alpha v\). Otherwise, there are two positive-definite completions with the same observed product \(Av=y\) but different Newton solve vectors (and hence different Newton steps).

This is an information limit for one Hessian-vector observation, not a claim about algorithms that also use exact line searches, additional gradient samples, multiple Hessian-vector products, or other curvature information.

## Assumptions and scope

The objective is the strictly convex quadratic \(f(x)=\tfrac12 x^{\mathsf T}Ax+b^{\mathsf T}x\), so its Hessian is the constant matrix \(A=A^{\mathsf T}\succ0\). At the point of interest, the gradient \(g=\nabla f(x)\) is known. A curvature oracle returns exactly one product \(y=Av\), where the query vector \(v\ne0\) is selected without knowing the entries of \(A\). The data are consistent with at least one positive-definite matrix, which implies \(v^{\mathsf T}y>0\).

“Uniquely determined” means that every symmetric positive-definite matrix \(\widetilde A\) satisfying \(\widetilde A v=y\) yields the same vector \(\widetilde A^{-1}g\). The claim is in exact arithmetic and concerns the full Newton solve vector, not merely its projection onto a queried subspace.

## Proof

If \(g=\alpha y\), then for every consistent matrix \(\widetilde A\),
\[
\widetilde A^{-1}g=\alpha\widetilde A^{-1}y=\alpha v.
\]
Thus the Newton solve vector, and therefore the Newton step, is unique.

Conversely, suppose \(g\notin\operatorname{span}\{y\}\). Apply an orthogonal change of coordinates and rescale the query and its observed product by \(\|v\|_2\), so that \(v=e_1\); this does not change the span condition. Write the observed first column as \(y=(a,b^{\mathsf T})^{\mathsf T}\), with \(a>0\). Every matrix of block form
\[
A_D=\begin{pmatrix}a&b^{\mathsf T}\\b&D\end{pmatrix}
\]
with symmetric \(D\) satisfying \(D-bb^{\mathsf T}/a\succ0\) is positive definite and has the same observed first column \(A_De_1=y\).

Write the Newton solution as \(p_D=(p_{D,1},p_{D,\perp})\). If \(p_{D,\perp}=0\), then \(g=A_Dp_D=p_{D,1}y\), contradicting \(g\notin\operatorname{span}\{y\}\). Hence \(p_{D,\perp}\ne0\) for every such completion. Choose any admissible \(D\) and any \(\tau>0\). Both \(A_D\) and \(A_{D+\tau I}\) remain positive definite and have the same first column. If their Newton solutions were equal to a common vector \(p\), subtracting their lower block equations would give \(\tau p_\perp=0\), contradicting \(p_\perp\ne0\). Therefore the two Newton solve vectors differ, so their conventional Newton steps also differ. This proves the “only if” direction and the classification.

## Verification

A small exact-arithmetic witness uses \(v=g=e_1\) and
\[
A_2=\begin{pmatrix}2&1&0\\1&2&0\\0&0&1\end{pmatrix},\qquad
A_3=\begin{pmatrix}2&1&0\\1&3&0\\0&0&1\end{pmatrix}.
\]
Both matrices are positive definite and satisfy \(A_2v=A_3v=(2,1,0)^{\mathsf T}\), while
\[
A_2^{-1}g=(2/3,-1/3,0)^{\mathsf T},\qquad
A_3^{-1}g=(3/5,-1/5,0)^{\mathsf T}.
\]
The included standard-library script `verify_example.py` checks positive definiteness by the positive leading principal minors, the identical observed product, the two exact solutions, and their inequality using rational arithmetic. Its output is `VERIFY_OK`. The example illustrates the non-identifiability branch for the solve vector (and hence for the Newton step); the general theorem is proved analytically above.

## Relationship to prior work

Ansari-Önnestam and Forsgren study finite Newton-step generation for strictly convex quadratics when exact line search is removed. Their Proposition 4.1 constructs a subspace quasi-Newton step using curvature information on a subspace of dimension at most two; the paper recursively uses this construction to generate the full Newton step. The present statement addresses a complementary question: when is **one** observed Hessian action already sufficient to identify the full Newton direction, without assuming the paper's conjugacy history or exact-line-search information? The source establishes two-direction sufficiency in its setting, but does not state this one-observation if-and-only-if criterion. The criterion does not contradict their algorithm or imply that two directions suffice in every one-step oracle model.

## Limitations

The result concerns one exact product \(Av\) and a known gradient at a fixed point. It does not give a quantitative error bound under noisy or finite-precision products, a lower bound for multiple adaptive queries, or an impossibility theorem for the full recursive subspace quasi-Newton method. When \(g\in\operatorname{span}\{Av\}\), the exact Newton solve vector is identifiable from the observation; outside that case, the theorem shows only non-uniqueness across consistent positive-definite completions.

## References

1. A. Ansari-Önnestam and A. Forsgren, “Finite Newton-Step Generation via Subspace Quasi-Newton Methods for Quadratic Problems,” arXiv:2407.03072, first submitted 3 July 2024. https://arxiv.org/abs/2407.03072
