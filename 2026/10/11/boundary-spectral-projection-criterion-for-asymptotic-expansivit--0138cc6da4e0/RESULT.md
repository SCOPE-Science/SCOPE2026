# Boundary spectral projection criterion for asymptotic expansivity of normal operators
## Finding
Let \(N\) be a bounded normal operator on a complex Hilbert space \(H\), and let \(E_N\) denote its projection-valued spectral measure. Put
\[
\overline{\mathbb D}=\{z\in\mathbb C:|z|\le 1\},\qquad \mathbb T=\{z\in\mathbb C:|z|=1\}.
\]
Then the vectors with bounded forward orbit form exactly
\[
H_b:=\{x\in H:\sup_{n\ge0}\|N^n x\|<\infty\}=E_N(\overline{\mathbb D})H.
\]
It follows that \(N\) is asymptotically expansive exactly when
\[
E_N(\mathbb T)=0.
\]
It is strongly asymptotically expansive exactly when there is some \(r<1\) for which
\[
E_N(\{z:r<|z|\le1\})=0,
\]
equivalently \(\|N E_N(\overline{\mathbb D})\|<1\).

The projection criterion cannot be replaced by the triple consisting of point spectrum, approximate-point spectrum, and whole spectrum, even for normal contractions. Let \(A=M_z\) on \(L^2(\mathbb D,m_2)\), where \(m_2\) is normalized planar area, and let \(U=M_\zeta\) on \(L^2(\mathbb T,m_1)\), where \(m_1\) is normalized arclength. Then \(A\) is asymptotically expansive but not strongly asymptotically expansive, whereas \(B=A\oplus U\) is not asymptotically expansive. Nevertheless
\[
\sigma_p(A)=\sigma_p(B)=\varnothing,
\qquad
\sigma_{ap}(A)=\sigma_{ap}(B)=\sigma(A)=\sigma(B)=\overline{\mathbb D}.
\]

## Assumptions and scope
Asymptotic expansivity and strong asymptotic expansivity are used in the one-sided linear sense of Bag--Mandal--Das: a bounded orbit lying in one fixed ball must converge to zero, respectively must do so uniformly over all such vectors. The theorem assumes a bounded normal operator on a complex Hilbert space. It does not assert a corresponding projection-valued criterion for nonnormal operators.

For \(x\in H\), write
\[
\mu_x(S)=\|E_N(S)x\|^2.
\]
The spectral theorem gives
\[
\|N^n x\|^2=\int_{\sigma(N)} |z|^{2n}\,d\mu_x(z).
\]

## Proof
First determine the bounded-orbit subspace. If \(x\in E_N(\overline{\mathbb D})H\), then
\[
\|N^n x\|^2=\int_{|z|\le1}|z|^{2n}\,d\mu_x(z)\le\|x\|^2
\]
for every \(n\ge0\). Conversely, if \(\mu_x(\{|z|>1\})>0\), then because
\[
\{|z|>1\}=\bigcup_{k\ge1}\{|z|\ge1+1/k\},
\]
there is a \(k\) for which \(c:=\mu_x(\{|z|\ge1+1/k\})>0\). Hence
\[
\|N^n x\|^2\ge c(1+1/k)^{2n},
\]
so the orbit is unbounded. This proves \(H_b=E_N(\overline{\mathbb D})H\).

Suppose \(E_N(\mathbb T)=0\). Every bounded-orbit vector \(x\) lies in \(E_N(\overline{\mathbb D})H\), and its scalar spectral measure gives zero mass to \(\mathbb T\). Thus \(|z|^{2n}\to0\) for \(\mu_x\)-almost every \(z\), while \(|z|^{2n}\le1\). Dominated convergence yields \(\|N^n x\|\to0\). By linear rescaling, this is precisely asymptotic expansivity. Conversely, if \(E_N(\mathbb T)\ne0\), choose \(0\ne x\in E_N(\mathbb T)H\). Then \(\|N^n x\|=\|x\|\) for every \(n\), so a small scalar multiple of \(x\) violates asymptotic expansivity.

For the strong statement, put \(P=E_N(\overline{\mathbb D})\). If \(E_N(\{z:r<|z|\le1\})=0\) for some \(r<1\), every bounded-orbit vector lies spectrally in \(|z|\le r\), and
\[
\|N^n x\|\le r^n\|x\|.
\]
This is uniform convergence on every fixed bounded-orbit ball, hence strong asymptotic expansivity. Conversely, assume strong asymptotic expansivity with ball radius \(\delta>0\). Since \(N|_{PH}\) is a contraction, every \(x\in PH\) with \(\|x\|\le\delta\) stays in that ball. The strong definition therefore implies
\[
\|(N|_{PH})^n\|\longrightarrow0.
\]
The restriction is normal, so
\[
\|(N|_{PH})^n\|=\|N|_{PH}\|^n.
\]
Thus \(q:=\|N|_{PH}\|<1\). Choosing \(r\) with \(q<r<1\) gives \(E_N(\{z:r<|z|\le1\})=0\). This also proves the stated norm equivalence.

For the separating example, the essential range of the coordinate function on planar area measure is \(\overline{\mathbb D}\), so \(\sigma(A)=\overline{\mathbb D}\). A singleton has planar area zero, hence \(\sigma_p(A)=\varnothing\). Normality gives \(\sigma_{ap}(A)=\sigma(A)\). Also \(E_A(\mathbb T)=0\), while \(\|A\|=1\); therefore the two criteria above show that \(A\) is asymptotically expansive but not strongly asymptotically expansive.

For \(U\), the essential range is \(\mathbb T\), every singleton has arclength zero, and \(E_U(\mathbb T)=I\). Hence \(B=A\oplus U\) is normal, \(E_B(\mathbb T)\ne0\), and \(B\) is not asymptotically expansive. Direct-sum spectral identities give \(\sigma(B)=\overline{\mathbb D}\) and \(\sigma_p(B)=\varnothing\); normality again gives \(\sigma_{ap}(B)=\overline{\mathbb D}\).

## Verification
The proof uses only the spectral theorem for bounded normal operators, countable additivity of scalar spectral measures, dominated convergence, and the standard identity \(\|T^n\|=\|T\|^n\) for a normal operator \(T\). Each implication was checked against the exact one-sided definitions in arXiv:2610.01196v1. No finite experiment is used to establish an infinite statement.

The example was checked directly from essential ranges and nonatomicity of the two measures. The distinction between ordinary and strong asymptotic expansivity is witnessed exactly by \(E_A(\mathbb T)=0\) together with \(\|A\|=1\).

## Relationship to prior work
Bag--Mandal--Das define asymptotic and strong asymptotic expansivity for linear operators and show that ordinary spectral sets do not characterize asymptotic expansivity: their Example 4.4 gives two nonnormal forward shifts with the same point, approximate-point, and whole spectra but different asymptotic-expansivity behavior. They explicitly raise the problem of finding a more suitable spectral characterization. The theorem above answers that question for the normal class by identifying the unit-circle spectral projection as the exact datum, and it strengthens their spectral-set obstruction by giving a pair of normal contractions with the same three spectral sets and different behavior.

Morales introduced the linear one-sided definition in earlier notes and related asymptotic expansivity to hyperbolicity under additional shadowing hypotheses. Mazur's classical work treats ordinary expansivity, hyperbolicity, and shadowing for normal operators. Neither inspected source states the boundary-projection criterion above or the strong asymptotic spectral-gap criterion.

## Limitations
The result is confined to bounded normal operators on complex Hilbert spaces. It does not classify asymptotic expansivity for general subnormal, hyponormal, or arbitrary Banach-space operators. The ingredients concerning strong stability of normal contractions are classical spectral-theorem facts; the claim here is their exact synthesis for the newly studied asymptotic-expansivity notions and the normal same-spectrum separation. An equivalent formulation may exist in older operator-stability literature under different terminology; no such implication-equivalent statement was found in the checked searches.

## References
1. P. Bag, P. N. Mandal, P. K. Das, *Asymptotic Expansive and Hyperbolic Linear Operators*, arXiv:2610.01196v1, 2026.
2. C. A. Morales, *Recent Topics on Linear Dynamics*, arXiv:2502.20666, 2025.
3. M. Mazur, *Hyperbolicity, expansivity and shadowing for the class of normal operators*, Functional Differential Equations 7 (2000), 147--156.
