# Right invertibility repairs an operator-perturbation theorem for woven frames
## Finding
Li--Jiang--Xu Theorem 4, which is Theorem 2.7 in the original preprint, states that a frame \(F=(f_j)_{j\in J}\) with bounds \(A,B\) gives a woven family \((U_iF)_{i=1}^m\) whenever one distinguished \(U_k\) has a bounded left inverse \(V\) and
\[
\max_{i\ne k}\|U_i-U_k\|
<
\frac{\sqrt A}{\|V\|\sqrt{(m-1)B}}.
\]
The assertion is false as stated.

Let \(H=\ell^2(\mathbb N)\), let \(F=(e_j)_{j\ge1}\) be the standard orthonormal basis, let \(m=2\), and let
\[
U_1=U_2=S,\qquad Se_j=e_{j+1}.
\]
Choose \(k=1\) and \(V=S^*\). Then
\[
VS=S^*S=I,\qquad \|V\|=1,
\]
and \(A=B=1\). Hence the source hypothesis becomes
\[
0=\|U_2-U_1\|<1.
\]
Every printed quantitative hypothesis is satisfied.

But
\[
U_iF=(e_2,e_3,\ldots),
\]
so for \(f=e_1\),
\[
\sum_{j\ge1}|\langle e_1,U_ie_j\rangle|^2=0.
\]
Thus \(U_iF\) is not even a frame for \(H\), and the family cannot be woven.

The exact one-operator boundary is surjectivity: for any frame \(F\) and bounded operator \(U\), \(UF\) is a frame for the ambient Hilbert space if and only if \(U\) is surjective. Accordingly, replacing the source's left inverse by a bounded right inverse repairs the perturbation theorem while preserving its numerical threshold.

Suppose \(U_kV=I\) and set
\[
\delta=\max_{i\ne k}\|U_i-U_k\|.
\]
If
\[
\delta<
\frac{\sqrt A}{\|V\|\sqrt{(m-1)B}},
\]
then every weaving has valid universal bounds
\[
\left(
\frac{\sqrt A}{\|V\|}
-\sqrt{B(m-1)}\,\delta
\right)^2
\]
and
\[
B\left(\|U_k\|+\sqrt{m-1}\,\delta\right)^2.
\]

## Assumptions and scope
The counterexample is infinite dimensional because left invertibility and surjectivity coincide for square matrices in finite dimension. It uses the canonical unilateral shift, an isometry with a bounded left inverse but proper closed range.

The repaired result assumes only that \(F\) is a frame with bounds \(A,B\), that \(U_1,\ldots,U_m\) are bounded operators, and that the distinguished \(U_k\) has a bounded right inverse \(V\). No invertibility or injectivity of \(U_k\) is required.

The threshold above is a sufficient perturbation condition. The finding does not assert that this particular sufficient threshold is necessary for wovenness.

## Proof
First, let \(T_F:\ell^2(J)\to H\) be the synthesis operator of a frame \(F\). Since \(T_F\) is surjective, the synthesis operator of \(UF\) is
\[
T_{UF}=UT_F.
\]
Therefore \(UF\) is a frame for \(H\) exactly when \(UT_F\) is surjective. If \(UT_F\) is surjective then \(U\) is surjective because
\[
R(UT_F)\subseteq R(U).
\]
Conversely, if \(U\) is surjective, then the composition of the two surjective operators \(T_F\) and \(U\) is surjective. This proves the exact one-operator boundary.

The unilateral-shift counterexample now follows immediately, but it can also be checked coefficientwise as in the finding.

For the repaired perturbation theorem, let \((\sigma_i)_{i=1}^m\) be an arbitrary partition of \(J\). Define the weaving analysis vector
\[
\mathcal A_\sigma f
=
\big(\langle f,U_if_j\rangle\big)_{j\in\sigma_i,\ 1\le i\le m}
\]
and the baseline vector
\[
\mathcal B_\sigma f
=
\big(\langle f,U_kf_j\rangle\big)_{j\in\sigma_i,\ 1\le i\le m}.
\]
Because the partition contains every \(j\) exactly once,
\[
\|\mathcal B_\sigma f\|^2
=
\sum_{j\in J}|\langle U_k^*f,f_j\rangle|^2
\ge
A\|U_k^*f\|^2.
\]
From \(U_kV=I\) we get
\[
V^*U_k^*=I,
\]
hence
\[
\|U_k^*f\|\ge \|V\|^{-1}\|f\|.
\]
Thus
\[
\|\mathcal B_\sigma f\|
\ge
\frac{\sqrt A}{\|V\|}\|f\|.
\]

For the error vector,
\[
\|\mathcal A_\sigma f-\mathcal B_\sigma f\|^2
=
\sum_{i=1}^m\sum_{j\in\sigma_i}
|\langle (U_i-U_k)^*f,f_j\rangle|^2.
\]
The upper frame inequality gives
\[
\|\mathcal A_\sigma f-\mathcal B_\sigma f\|^2
\le
B\sum_{i\ne k}\|(U_i-U_k)^*f\|^2
\le
B(m-1)\delta^2\|f\|^2.
\]
By the reverse triangle inequality,
\[
\|\mathcal A_\sigma f\|
\ge
\left(
\frac{\sqrt A}{\|V\|}
-\sqrt{B(m-1)}\,\delta
\right)\|f\|.
\]
The assumed strict inequality makes the coefficient positive and yields the displayed universal lower frame bound.

For the upper bound,
\[
\|\mathcal A_\sigma f\|
\le
\|\mathcal B_\sigma f\|
+
\|\mathcal A_\sigma f-\mathcal B_\sigma f\|
\le
\sqrt B\left(\|U_k\|+\sqrt{m-1}\,\delta\right)\|f\|,
\]
which gives the displayed upper bound.

## Verification
The earliest public preprint was inspected at Theorem 2.7 and its proof. It states the left-inverse hypothesis \(VU_k=I\), concludes that the nearby \(U_i\) are left invertible, and then claims that \(U_iF\) is a frame. The 2023 journal version retains the same statement as Theorem 4.

The journal proof was also inspected at the operator inequality and the page containing its lower weaving estimate. It treats bounded-below \(U_i\) as though this controlled the frame operator of \(U_iF\), whereas the analysis coefficients of \(U_iF\) involve \(U_i^*\). It also uses a squared-modulus subtraction estimate that is not a generally valid scalar inequality.

The counterexample is exact:
\[
S^*S=I,\qquad SS^*\ne I,
\]
and \(e_1\) is orthogonal to every \(Se_j\). The repaired proof is independent of both problematic proof steps and uses only frame analysis inequalities, the adjoint identity \(V^*U_k^*=I\), and the triangle inequality in the direct-sum coefficient space.

## Relationship to prior work
The general fact that the image of a frame under a bounded operator is a frame for the same ambient Hilbert space exactly when the operator is surjective is standard operator-frame theory; it is not claimed here as new.

A later 2025 paper by Xiang--Lin studies operator perturbations of woven \(g\)-frames and explicitly corrects several operator-preservation statements in other \(g\)-frame sources. That paper reinforces the importance of the correct one-sided operator condition, but the inspected results concern different cited propositions and do not state the present source-specific counterexample or the repaired Li--Jiang--Xu threshold.

The accepted contribution is therefore restricted to the precise failure of the 2019/2023 theorem, the zero-perturbation unilateral-shift witness, and a proof that changing the distinguished hypothesis from a left inverse to a right inverse makes the same published threshold valid with explicit universal bounds.

## Limitations
The repaired threshold is sufficient, not asserted to be best possible. The result does not classify all tuples \((U_1,\ldots,U_m)\) that preserve wovenness.

The literature search cannot rule out an unindexed erratum, thesis remark, or informal correction. The later operator-weaving literature inspected here does not provide whole-literature uniqueness evidence.

## References
1. D. Li, J. Jiang and Y. Xu, *On weaving frames in Hilbert spaces*, arXiv:1901.01360v1, first posted 5 January 2019; published in *Operators and Matrices* 17(3) (2023), 809--822, DOI 10.7153/oam-2023-17-53.
2. Z.-Q. Xiang and C.-X. Lin, *A New View on the Wovenness of g-Frames Under Operators*, *Journal of Mathematics* (2025), article 7185421, DOI 10.1155/jom/7185421.
