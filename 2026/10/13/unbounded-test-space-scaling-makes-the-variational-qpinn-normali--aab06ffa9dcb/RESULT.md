# Unbounded test-space scaling makes the variational QPINN normalization degenerate
## Finding
In the variational QPINN formulation of Hernandez and De Palma, the stated test space is the full finite-dimensional linear space
\[
\mathcal H_M=\operatorname{span}\{v_1,\ldots,v_M\},\qquad M>0,
\]
and the variational observable is
\[
\mathcal E(\Theta,v)=\sum_{i,j=1}^d\int_B a_{ij}(x)\,\partial_i u(\Theta,x)\,\partial_j v(x)\,dx.
\]
Assumption A8 takes a finite normalization over every \(w=(v,\hat x)\in\mathcal H_M\times\partial B\). On that literal domain the normalization is scale-degenerate: if one test vector has nonzero second moment, scaling that vector makes the second moment arbitrarily large. Therefore A8 can hold on all of \(\mathcal H_M\) only when the variational component vanishes in \(L^2\) for every test vector.

The same scaling obstruction applies to the uniform variational lazy-training statement in Theorem 4.3, Eq. (4.109). Its first-component nonlinear-minus-linearized discrepancy is linear in \(v\), so a finite supremum over the whole vector space is possible only when that discrepancy is identically zero on \(\mathcal H_M\), or when the test domain is replaced by a bounded normalized set. The paper's intermediate estimates already impose \(\|v\|_{1,B}\le1\). Thus a unit ball, a normalized basis, or another bounded test set is a necessary domain repair for the advertised nontrivial uniform statement.

## Assumptions and scope
The claim concerns arXiv:2609.19239v1 and its variational formulation with \(M>0\). It uses the definitions in Eqs. (4.13)--(4.16), Assumption A8, Assumption A10, the unit-norm hypothesis used in Lemmas 4.1--4.2, and Theorem 4.3, Eq. (4.109). It does not challenge the strong-form QPINN theorem, and it does not claim that restricting the variational test set to a unit ball by itself proves every later estimate.

## Proof
Let \(v_0\in\mathcal H_M\). Since \(\mathcal H_M\) is a vector space, \(cv_0\in\mathcal H_M\) for every real \(c\). The integral defining \(\mathcal E\) is linear in the test function, so
\[
\mathcal E(\Theta,cv_0)=c\,\mathcal E(\Theta,v_0).
\]
Consequently
\[
\mathbb E\!\left|\mathcal E(\Theta,cv_0)\right|^2
=c^2\,\mathbb E\!\left|\mathcal E(\Theta,v_0)\right|^2.
\]
If the right-hand second moment is positive, the left-hand side is unbounded as \(|c|\to\infty\). The first diagonal entry of the matrix appearing in A8 is precisely such a second moment. Hence A8's finite normalization over all \(\mathcal H_M\times\partial B\) forces \(\mathbb E|\mathcal E(\Theta,v)|^2=0\) for every \(v\in\mathcal H_M\); otherwise the stated maximum is infinite.

For the theorem-level uniform bound, define the first-component discrepancy at time \(t\) by
\[
D_t(v)=\mathcal E(\Theta_t,v)-\mathcal E^{\rm lin}(\Theta_t^{\rm lin},v).
\]
The parameter linearization differentiates only with respect to \(\Theta\). Because \(\mathcal E(\Theta,v)\) and each parameter derivative of it are linear in \(v\), \(D_t\) is a linear functional on \(\mathcal H_M\). If \(D_t(v_0)\ne0\) for one \(v_0\), then \(|D_t(cv_0)|=|c|\,|D_t(v_0)|\), so the supremum in Eq. (4.109) is infinite. A finite all-space supremum therefore implies \(D_t\equiv0\) for every \(t\), unless the test vectors are restricted to a bounded normalized set.

## Verification
This is an all-parameter scaling argument; no finite experiment is used as an infinite proof. The source definitions and theorem domains were checked directly in the full text. The paper defines \(\mathcal H_M\) as a span, defines \(\mathcal E\) linearly in \(v\), states A8 over all \(\mathcal H_M\times\partial B\), assumes only the basis-vector bound in A10, and then states Eq. (4.109) with the same unrestricted test-space supremum. In contrast, the local estimates used in the proof explicitly fix test functions with \(\|v\|_{1,B}\le1\).

## Relationship to prior work
The correction is source-specific. Earlier VPINN work treats finite test families in a Petrov--Galerkin framework, while recent stochastic variational work formulates weak residual control through a normalized dual-norm viewpoint. Those frameworks motivate normalization but do not state or imply a published correction of A8 or Eq. (4.109) in arXiv:2609.19239v1. The mathematical fact used here is elementary homogeneity; the substantive point is that it applies directly to the domain of the paper's principal variational lazy-training statement.

## Limitations
A normalized test domain is shown to be necessary for a nontrivial uniform variational statement, not sufficient for every constant and probability estimate in the paper. The finding does not assess whether a corrected theorem over the unit ball is true, and it does not affect statements whose domains are already finite or normalized. An unindexed author correction or later revision could remove the defect without changing the present statement about version 1.

## References
1. A. Melchor Hernandez and G. De Palma, “Lazy training of quantum physics informed neural networks,” arXiv:2609.19239v1 (2026), especially Eqs. (4.13)--(4.16), Assumptions A8--A10, Lemmas 4.1--4.2, and Theorem 4.3.
2. S. Berrone, C. Canuto, and M. Pintore, “Variational Physics Informed Neural Networks: the Role of Quadratures and Test Functions,” Journal of Scientific Computing 92, 100 (2022), DOI:10.1007/s10915-022-01950-4.
3. D. Marcondes, “Random test functions, \(H^{-1}\) norm equivalence, and stochastic variational physics-informed neural networks,” arXiv:2605.03542v1 (2026).
