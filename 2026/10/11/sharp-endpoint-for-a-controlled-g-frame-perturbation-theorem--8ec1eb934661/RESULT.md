# Sharp endpoint for a controlled g-frame perturbation theorem
## Finding
The perturbation statement in Theorem 3.4 of Li and Leng is valid with the strict hypothesis \(0\le \lambda<A\), but it is false at the included endpoint \(\lambda=A\). If \(\Lambda\) is a \((T,T)\)-controlled g-frame with bounds \(A,B\), \(\Gamma\) is a \((U,U)\)-controlled g-Bessel family, and
\[
\|(S_{T\Gamma\Lambda U}-S_{T\Lambda\Lambda T})f\|\le \lambda\|f\|,
\]
then for \(0\le\lambda<A\) the mixed operator is invertible and \(\Gamma\) has controlled lower bound
\[
\frac{(A-\lambda)^2}{B}.
\]
The strict threshold is sharp.

## Assumptions and scope
The setting is a complex Hilbert space \(H\), coefficient Hilbert spaces \(H_i\), invertible bounded controllers \(T,U\), and the mixed controlled operator
\[
S_{T\Gamma\Lambda U}f=\sum_i U^*\Gamma_i^*\Lambda_iTf.
\]
The counterexample already occurs in the ordinary scalar-coefficient specialization \(H_i=\mathbb C\) and \(T=U=I\). It therefore refutes the endpoint of the general theorem without relying on any controller-specific pathology.

## Proof
For the positive result, the source hypothesis and the lower controlled-frame inequality give, for every \(f\in H\),
\[
\|S_{T\Gamma\Lambda U}f\|
\ge \|S_{T\Lambda\Lambda T}f\|-\|(S_{T\Gamma\Lambda U}-S_{T\Lambda\Lambda T})f\|
\ge (A-\lambda)\|f\|.
\]
The adjoint identity \(S_{T\Gamma\Lambda U}^*=S_{U\Lambda\Gamma T}\) gives the same lower bound for the adjoint. When \(\lambda<A\), both the operator and its adjoint are bounded below. Hence the operator is injective with closed range, while its adjoint has trivial kernel, so its range is dense. The range is therefore all of \(H\), and the mixed operator is invertible. The Cauchy--Schwarz argument in the source then yields
\[
\frac{(A-\lambda)^2}{B}\|f\|^2\le \sum_i\|\Gamma_iUf\|^2.
\]

To show that strictness is necessary, take \(H=\ell^2(\mathbb N)\) with standard basis \(e_n\), put \(T=U=I\), and define
\[
\Lambda_n f=\langle f,e_n\rangle,
\qquad
\Gamma_n f=\frac1n\langle f,e_n\rangle.
\]
Then \(\Lambda\) is Parseval, so \(A=B=1\). Also
\[
\sum_n|\Gamma_n f|^2=\sum_n\frac{|\langle f,e_n\rangle|^2}{n^2}\le\|f\|^2,
\]
so \(\Gamma\) is g-Bessel. Every coefficient operator is nonzero, and \(\Gamma_n f=0\) for all \(n\) forces \(f=0\), so the family is complete. It is not a g-frame because for \(f=e_N\) its coefficient energy is \(N^{-2}\), which has no positive uniform lower bound.

The mixed operator is the diagonal contraction
\[
S_{\Gamma\Lambda}f=\sum_n\frac1n\langle f,e_n\rangle e_n,
\]
so
\[
\|S_{\Gamma\Lambda}-I\|=\sup_{n\ge1}|1/n-1|=1=A.
\]
Thus the theorem's endpoint condition holds with \(\lambda=A=1\), yet \(S_{\Gamma\Lambda}\) is not bounded below and is not invertible, while \(\Gamma\) is not a g-frame.

## Verification
All calculations are symbolic. The Parseval identity for \(\Lambda\), the Bessel estimate for \(\Gamma\), and the failure of a lower g-frame bound follow directly from the standard basis. The mixed-operator formula is coordinatewise, and its norm defect from the identity is exactly one. No finite computation is used to infer an infinite-dimensional conclusion.

For the repaired theorem, the only point requiring strictness is positivity of \(A-\lambda\). The source's subsequent Proposition 3.5 independently uses a strict perturbation parameter \(0<\varepsilon<1\), consistent with this boundary.

## Relationship to prior work
Li and Leng state Theorem 3.4 with \(0\le\lambda\le A\) and conclude invertibility of the mixed controlled operator and the controlled g-frame property of \(\Gamma\). Their proof derives the lower estimate \((A-\lambda)\|f\|\) and then treats it as a positive lower bound; at \(\lambda=A\) it is zero. The same paper's Proposition 3.5 uses a strict perturbation condition \(\varepsilon<1\). Earlier controlled-g-frame work of Rahimi and Fereydooni develops the controlled g-frame and multiplier framework but does not supply this endpoint correction.

Targeted searches for the theorem number, source identifier, endpoint equality, mixed-operator invertibility, diagonal counterexamples, and strict perturbation threshold did not locate a published correction or an equivalent counterexample. The closest indexed results found were mathematically unrelated operator-stability findings and do not imply this statement.

## Limitations
The result corrects the perturbation threshold in this theorem; it does not classify all perturbations of controlled g-frames. The counterexample uses the scalar-coefficient specialization and therefore says nothing additional about phenomena that depend essentially on nontrivial controllers. An unindexed erratum, thesis remark, or informal observation could contain the same endpoint correction.

## References
1. D. Li and J. Leng, *Generalized frames and controlled operators in Hilbert space*, arXiv:1709.00585v1, 2017; published as *Generalized frames for controlled operators in Hilbert spaces*, Annals of Functional Analysis 10 (2019), 537--552, doi:10.1215/20088752-2019-0012.
2. A. Rahimi and A. Fereydooni, *Controlled G-Frames and Their G-Multipliers in Hilbert spaces*, arXiv:1204.1359; Analele Stiintifice ale Universitatii Ovidius Constanta, Seria Matematica 21 (2013), 223--236, doi:10.2478/auom-2013-0035.
