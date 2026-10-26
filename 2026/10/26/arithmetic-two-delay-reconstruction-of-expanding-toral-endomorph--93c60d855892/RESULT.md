# Arithmetic two-delay reconstruction of expanding toral endomorphisms

## Finding
Let \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb Z)\) satisfy \(|\det A|\ge2\), and let \(T_A:\mathbb T^2\to\mathbb T^2\) be \(x\mapsto Ax\pmod{\mathbb Z^2}\). A *two-delay circle observation* from a continuous sensor \(h:\mathbb T^2\to\mathbb T\) is
\[
D_{T_A,h}(x)=(h(x),h(T_Ax))\in\mathbb T^2.
\]
**Complete classification.** Some continuous circle-valued sensor makes this map injective if and only if the integral binary quadratic form
\[
Q_A(m,n)=bm^2+(d-a)mn-cn^2
\]
represents \(1\) or \(-1\) at integer \((m,n)\). Equivalently, \(A\) is conjugate over \(\operatorname{GL}_2(\mathbb Z)\) to \(\begin{pmatrix}0&1\\-\det A&\operatorname{tr}A\end{pmatrix}\). Whenever the criterion holds a smooth character sensor suffices. For any continuous map \(F:\mathbb T^2\to\mathbb T^2\) homotopic to \(T_A\), the same arithmetic condition remains **necessary** for injective \(D_{F,h}\); positive reconstruction is stable under small \(C^1\) perturbations of the linear map with its character sensor.

**Isospectral and Bernoulli-isomorphic separation.** The two expanding integer matrices
\[
A_0=\begin{pmatrix}3&2\\-3&4\end{pmatrix},\qquad
B_0=\begin{pmatrix}0&1\\-18&7\end{pmatrix}
\]
have the same characteristic polynomial \(\lambda^2-7\lambda+18\), entropy \(\log18\), and exactly the same number of fixed points of every positive iterate. Both are one-sided Bernoulli with alphabet size \(18\) for Haar measure. Yet \(B_0\) admits a smooth sensor recovering *all* states from two consecutive observations, while **no continuous sensor** can do so for \(A_0\), nor for any continuous torus map homotopic to \(A_0\). The smallest nonzero topological degree of a two-delay observation of \(A_0\) has absolute value \(2\), realized by a smooth character that is an exactly two-to-one covering.

## Assumptions and scope
All torus coordinates are taken modulo \(\mathbb Z\), and \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\). Injectivity means pointwise global injectivity, not almost-everywhere reconstruction. Sensors may be arbitrary continuous circle-valued maps, so no linearity is assumed in the obstruction. A *character* sensor is \(h_{m,n}(x)=mx_1+nx_2\pmod1\), for \(m,n\in\mathbb Z\). The classification concerns exactly two consecutive forward samples and the specified two-dimensional observation codomain. The nonlinear necessity assumes only homotopy to \(T_A\). The positive perturbation assertion applies to \(C^1\) maps sufficiently close to \(T_A\), not all maps in its homotopy class.

## Proof
**Cohomological obstruction, for every continuous sensor.** Any continuous \(h:\mathbb T^2\to\mathbb T\) has a winding vector \((m,n)\in H^1(\mathbb T^2;\mathbb Z)\cong\mathbb Z^2\), so it is homotopic to \(h_{m,n}\). For \(F\simeq T_A\), the two coordinate classes of \(D_{F,h}\) are the integral rows \(v=(m,n)\) and \(vA\). The cup product on \(H^2(\mathbb T^2;\mathbb Z)\) therefore gives
\[
\deg D_{F,h}=\det\begin{pmatrix}v\\vA\end{pmatrix}=bm^2+(d-a)mn-cn^2=Q_A(m,n).
\]
If \(D_{F,h}\) were injective, invariance of domain makes its image open in the connected torus; compactness makes it closed, so the image is all of \(\mathbb T^2\). Thus the map would be a homeomorphism, whose degree is \(1\) or \(-1\). Necessity of representing \(\pm1\) follows even for nonlinear sensors and nonlinear maps in the homotopy class.

**Constructive sufficiency and integral companion form.** If \(Q_A(m,n)=\pm1\), then the integral matrix \(U=\begin{pmatrix}v\\vA\end{pmatrix}\) is unimodular. The character sensor \(h_{m,n}\) has delay map exactly \(x\mapsto Ux\), hence a smooth torus-group automorphism. Cayley–Hamilton gives \(vA^2=(\operatorname{tr}A)vA-(\det A)v\), and hence
\[
UA=\begin{pmatrix}0&1\\-\det A&\operatorname{tr}A\end{pmatrix}U.
\]
Conversely, if \(A\) is integrally conjugate to this companion matrix, the first row of a conjugating unimodular matrix is a sensor vector with \(Q_A=\pm1\). This proves both equivalences. If a \(C^1\) map \(F\) is sufficiently close to \(T_A\), its delay map for the same fixed character remains \(C^1\)-close to the torus automorphism \(x\mapsto Ux\). The derivative is everywhere invertible, so this delay map is a covering with degree \(\det U=\pm1\) and therefore has one sheet: it is a global diffeomorphism.

**Two matching-spectrum examples with distinct reconstruction behavior.** Both displayed matrices have trace \(7\) and determinant \(18\), with eigenvalues \((7\pm i\sqrt{23})/2\), each of modulus \(\sqrt{18}>1\). Consequently both toral maps are expanding and have entropy \(\log18\); their periodic point counts are identical for every \(k\ge1\) because
\[
\#\operatorname{Fix}(T_A^k)=|\det(A^k-I)|=|(\lambda_+^k-1)(\lambda_-^k-1)|.
\]
The published Bernoulli criterion for expanding toral endomorphisms identifies both Haar systems with the uniform one-sided Bernoulli shift on \(18\) symbols. For \(B_0\), the sensor \(h(x)=x_1\) has delays \((x_1,x_2)\) exactly, so it is reconstructing. For \(A_0\), direct multiplication yields
\[
Q_{A_0}(m,n)=2m^2+mn+3n^2,
\qquad8Q_{A_0}(m,n)=(4m+n)^2+23n^2.
\]
When \(n\ne0\), \(Q_{A_0}>2\); when \(n=0\), it equals \(2m^2\). Thus no integer vector represents \(\pm1\), while \(Q_{A_0}(1,0)=2\) is the smallest positive nonzero value. The character \(x\mapsto x_1\) has delay matrix \(\begin{pmatrix}1&0\\3&2\end{pmatrix}\), giving a smooth two-sheet covering. The cohomological obstruction applies unchanged to every continuous \(F\) homotopic to \(T_{A_0}\), proving the nonlinear-negative assertion.

## Verification
The included standalone Python script `checks/verify.py` performs exact integral matrix and quadratic-form checks, verifies the completed-square identity, compares the two characteristic polynomials and fixed-point counts through period twelve, and checks the explicit double covering. Its finite tests are reproducibility supplements; the all-map and all-sensor statements follow from the preceding cohomological and topological proof.

## Relationship to prior work
Leuridan's *Linear toral endomorphisms, exactness, Bernoulliness and generators* (arXiv:2610.01642v1, first public 2026-10-01, primary MSC 37A05) supplies the expanding-map one-sided Bernoulli criterion and concerns measurable finite generators. It does not classify minimal-length circle-valued topological delays. The established time-delay literature of Botvinick-Greenhouse, Martin and Yang analyzes dynamical identification via longer delay embeddings, rather than this complete two-delay integer-conjugacy test. A previous published three-dimensional arithmetic degree obstruction uses the same standard cup-product method for a **fixed nonexpanding three-torus family and three delays**; it neither classifies all two-dimensional integer torus matrices nor supplies the expanding same-spectrum contrast here. The conjugacy-to-companion equivalence is classical integral cyclic-vector algebra; the specifically assessed observation classification and same-spectrum distinction are the contributions claimed, not invention of that algebraic tool.

## Limitations
No claim is made about real-valued scalar sensors into \(\mathbb R\), three or more delays, nonconsecutive delays, arbitrary two-dimensional manifolds, or injectivity on full-measure subsets. A nonzero topological degree does not itself force an arbitrary nonlinear delay map to be a covering; the precise two-sheet assertion applies to the exhibited linear character. The positive nonlinear assertion needs a small \(C^1\) perturbation; homotopy alone guarantees only the negative criterion. The observational interpretation may have historical precedents under integer observability or cyclic-module terminology beyond the inspected sources; an independent literature audit has not been performed.

## References
1. C. Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators*, arXiv:2610.01642v1 (2026), https://arxiv.org/abs/2610.01642 .
2. J. Botvinick-Greenhouse, R. Martin, Y. Yang, *Invariant Measures in Time-Delay Coordinates for Unique Dynamical System Identification*, arXiv:2412.00589v2, https://arxiv.org/html/2412.00589v2 .
3. *Arithmetic degree obstruction and robust three-delay reconstruction for exact toral maps* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-arithmetic-degree-obstruction-and-robust-three-delay-reconstruct--858b240ce20c .
4. T. H. Hughes, *Behavioral Realizations using Companion Matrices and the Smith Form*, SIAM J. Control Optim. 54 (2016), 845–865, DOI 10.1137/140991911 .
