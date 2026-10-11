# Pairwise-distinct norms do not force unique \(K\)-frame scalings
## Finding
Ramesan and Ravindran's Theorem 4.4(ii) and Remark 4.5 assert that a scalable \(K\)-frame whose vectors have non-uniform norms has a unique scaling. This is false even when \(K=I\), and it remains false under the stronger hypothesis that all vector norms are pairwise distinct.

Take \(H=\mathbb C^2\), \(K=I\), and
\[
F=(f_1,f_2,f_3)=(e_1,2e_1,3e_2).
\]
The norms are \(1,2,3\). For every \(t\in(0,1)\), define
\[
c_1(t)=\sqrt t,\qquad c_2(t)=\frac12\sqrt{1-t},\qquad c_3(t)=\frac13.
\]
All three coefficients are strictly positive and
\[
\sum_{i=1}^3 c_i(t)^2 f_i f_i^*
=t e_1e_1^*+(1-t)e_1e_1^*+e_2e_2^*=I.
\]
Thus every \(c(t)\) is a strict Parseval scaling, yielding a continuum of distinct scalings despite pairwise-distinct norms.

For a finite \(K\)-frame \(F=(f_i)_{i=1}^m\) in \(\mathbb C^n\) that admits a strict scaling, uniqueness is governed exactly by the real-linear independence of the outer products \(f_i f_i^*\), not by the norms of the vectors.

## Assumptions and scope
The counterexample uses the ordinary frame specialization \(K=I\), which is a special case of the source's \(K\)-frame framework. A scaling means a nonnegative vector \(c=(c_i)\) for which \( (c_i f_i)_i\) is a Parseval \(K\)-frame; it is strict when every \(c_i>0\).

The exact uniqueness statement below is restricted to finite-dimensional \(\mathbb C^n\) and to a scaling that is strict. The strictness assumption is essential for the converse direction because it permits small perturbations in every coordinate of the squared-scaling vector.

## Proof
The displayed computation in the Finding proves directly that the frame \(F=(e_1,2e_1,3e_2)\) has a continuum of strict scalings. Since \(F\) spans \(\mathbb C^2\), it is an ordinary frame and therefore an \(I\)-frame. Its vector norms are pairwise distinct, so it contradicts both Theorem 4.4(ii) and Remark 4.5.

The failure in the published proof is also visible algebraically. If \(c\) and \(d\) are two scalings, the trace identity gives
\[
\sum_i c_i^2\|f_i\|^2
=\operatorname{Tr}(KK^*)
=\sum_i d_i^2\|f_i\|^2.
\]
This is one scalar equality. When the numbers \(\|f_i\|^2\) are unequal, it does not follow that \(c_i^2=d_i^2\) coordinatewise. In the counterexample the left side equals \(2\) for every \(t\in(0,1)\):
\[
t+4\frac{1-t}4+9\frac19=2.
\]

For the exact uniqueness criterion, write \(x_i=c_i^2\) and define the real-linear map
\[
\mathcal L:\mathbb R^m\to\mathbb H_n,\qquad
\mathcal L(x)=\sum_{i=1}^m x_i f_i f_i^*,
\]
where \(\mathbb H_n\) is the real vector space of Hermitian \(n\times n\) matrices. The source's Theorem 5.1 gives the scaling equation
\[
\mathcal L(x)=KK^*,\qquad x\ge0.
\]
If the operators \(f_i f_i^*\) are real-linearly independent, then \(\mathcal L\) is injective, so the squared scaling \(x\), hence \(c\), is unique.

Conversely, suppose a strict scaling exists, so \(x_i>0\) for every \(i\), and suppose the outer products are real-linearly dependent. Choose \(0\ne z\in\ker\mathcal L\). Because there are finitely many coordinates and every \(x_i>0\), there is \(\varepsilon>0\) small enough that both \(x+\varepsilon z\) and \(x-\varepsilon z\) are coordinatewise nonnegative. Both satisfy the same operator equation because \(\mathcal L(z)=0\). Taking coordinatewise nonnegative square roots gives two distinct scalings. Therefore a strict scaling is unique if and only if the outer products are real-linearly independent.

## Verification
The target article was inspected at Theorem 4.4, its proof, Remark 4.5, and Theorem 5.1. Theorem 4.4(ii) states uniqueness for non-uniform norm vectors; its proof passes from equality of two weighted sums to coordinatewise equality. Theorem 5.1 separately gives the operator equation used above for finite-dimensional scalability.

The counterexample is symbolic and requires no numerical approximation. Substituting any \(t\in(0,1)\) gives the frame operator exactly equal to \(I\). The uniqueness boundary is proved by injectivity and a finite-dimensional kernel perturbation; no enumeration or computational exhaustion is used.

## Relationship to prior work
Cahill and Chen, *A note on scalable frames* (arXiv:1301.7292), formulate ordinary frame scalability as a nonnegative linear system in the outer products. Their Corollary 2.3 gives uniqueness when those outer products are linearly independent, and their discussion of the dependent case allows multiple solutions. Accordingly, real-linear outer-product independence is established background in ordinary scalable-frame theory and is not claimed here as a new standalone principle.

The contribution here is the explicit correction of the 2023 \(K\)-frame uniqueness theorem: pairwise-distinct norms do not imply uniqueness, the failure already occurs for \(K=I\) with a continuum of strict scalings, and the trace step in the published argument cannot support its conclusion. The source's own finite-dimensional operator equation transfers the established linear-algebraic criterion to the strict \(K\)-scaling setting.

## Limitations
This finding does not classify all non-strict scalings. If some scaling coordinates vanish, dependence of the full outer-product family need not create another nonnegative solution because a kernel direction can point outside the feasible orthant. The result therefore states an if-and-only-if uniqueness criterion only for a given strict scaling.

No claim is made that the general outer-product method is new; it is explicitly credited to earlier scalable-frame literature. The literature search cannot exclude an unindexed erratum, thesis remark, or informal note that already points out the same error in Theorem 4.4.

## References
1. S. Ramesan and K. T. Ravindran, *Some Results on Scalable K-Frames*, Matematički Vesnik 75(4) (2023), 225–234, DOI 10.57016/MV-7942HXLN. See Theorem 4.4, Remark 4.5, and Theorem 5.1.
2. J. Cahill and X. Chen, *A note on scalable frames*, arXiv:1301.7292 (2013), especially Corollary 2.3 and Section 3.
