# Sharp sixth-moment variance asymptotics for random unimodular Fourier polynomials

## Finding
Let \(U_0,U_1,\ldots\) be independent variables uniformly distributed on the unit circle and, for every integer \(n\ge1\), define \(P_n(e^{it})=\sum_{j=0}^{n-1}U_j e^{ijt}\). With normalized Haar measure \(dt/(2\pi)\), let \(S_n=\int_0^{2\pi}|P_n(e^{it})|^6\,dt/(2\pi)\). Then
\[
\mathbb E S_n=6n^3-9n^2+4n,\qquad
\operatorname{Var}(S_n)=\frac{1179}{5}n^5+O(n^4),
\]
where the implied constant is absolute. More precisely the two leading contributors to the variance come from disjoint balanced two-pair phase characters, with contribution \(216n^5+O(n^4)\), and disjoint balanced triple phase characters, with contribution \((99/5)n^5+O(n^4)\). Consequently
\[
\mathbb E\left|\frac{S_n}{n^3}-6\right|^2=\frac{1179}{5n}+O(n^{-2}).
\]
The result concerns Haar complex phases, not independent real signs.

## Assumptions and scope
All indices lie in \(\{0,1,\ldots,n-1\}\); the Fourier integral is probability-normalized and the variance is with respect to the independent phases. The asymptotics hold as the positive integer \(n\to\infty\). No Gaussian or independent-in-\(t\) assumption is made. The theorem gives the sharp leading variance coefficient but not a central limit theorem or an exact polynomial formula for all finite \(n\).

## Proof
Expansion and circle orthogonality show that \(S_n\) equals the sum of \(U_aU_bU_c\overline{U_dU_eU_f}\) over all ordered triples with \(a+b+c=d+e+f\). Regard each product as the character \(\chi_\delta(U)=\prod_j U_j^{\delta_j}\), where \(\delta\) is the difference of the two multiplicity vectors of the triples. For a nonconstant character, the positive and negative coordinate masses are equal to some \(s\in\{2,3\}\), and \(\sum_j\delta_j=\sum_j j\delta_j=0\). Write the positive integer multiplicity of \(\chi_\delta\) in \(S_n\) as \(c_\delta\). The Steinhaus characters are orthonormal, hence
\[
\operatorname{Var}(S_n)=\sum_{\delta\ne0}c_\delta^2.
\]
The constant Fourier coefficient comes from matching multisets of triples: \(36\binom n3+9n(n-1)+n=6n^3-9n^2+4n\), proving the mean.

If \(s=2\) and the four nonzero coordinates of \(\delta\) are distinct with signs \(+,+,-,-\), their index pairs have the same sum. To realize this character, a common third index is added to each ordered triple. There are \(n-4\) choices outside the four indices, each of multiplicity \(6\cdot6=36\), and four choices inside, each of multiplicity \(3\cdot6=18\). Thus exactly
\[
 c_\delta=36(n-4)+4\cdot18=36(n-2).
\]
Let \(w_2(q)\) count ordered pairs with sum \(q\). Since \(\sum_qw_2(q)^2=(2n^3+n)/3\), and coincident-index solutions number \(O(n^2)\), the number of these signed, four-distinct characters is
\[
 \frac14\sum_qw_2(q)^2+O(n^2)=\frac{n^3}{6}+O(n^2).
\]
Their total squared coefficient is therefore \(216n^5+O(n^4)\).

If \(s=3\) and all six nonzero coordinates are distinct, there are three positive and three negative unit entries, with equal index sums. Each such character is represented by its uniquely determined positive and negative index multisets, which have \(3!\) orderings each, so \(c_\delta=36\). Let \(w_3(q)\) count ordered triples of indices with sum \(q\). Standard lattice counting, or the elementary piecewise quadratic formula for threefold convolution of the indicator of \([0,1]\), gives
\[
\sum_q w_3(q)^2=n^5\int_0^3 f_3(x)^2\,dx+O(n^4),
\]
where
\[
f_3(x)=\begin{cases}x^2/2,&0\le x\le1,\\(-2x^2+6x-3)/2,&1\le x\le2,\\(3-x)^2/2,&2\le x\le3,\\0,&\text{otherwise.}\end{cases}
\]
Direct polynomial integration yields \(\int_0^3 f_3(x)^2\,dx=11/20\). The six-index distinctness exclusions are \(O(n^4)\) ordered solutions: after a coincidence, at most four of the remaining free indices may be selected and the last is fixed by the sum equation. Each signed character is counted \((3!)^2=36\) times in the ordered six-tuple count. Therefore their number equals \((11/720)n^5+O(n^4)\), and their squared-coefficient contribution is \((99/5)n^5+O(n^4)\).

Every other nonconstant character with \(s=2\) has support at most three. There are \(O(n^2)\) of these because the weighted sum gives a genuine linear relation on at most three distinct support indices. Every associated coefficient is \(O(n)\), since its representations are determined by a common third index and finitely many permutations. These contribute \(O(n^4)\). Other characters with \(s=3\) have support at most five, hence number \(O(n^4)\) by the same linear-relation argument; their coefficients are bounded by \(36\), giving another \(O(n^4)\). These cases exhaust the nonconstant Fourier characters. The sum of the two leading contributions is \(216+99/5=1179/5\), proving the variance estimate. The final mean-square assertion follows by dividing by \(n^6\) and adding the squared bias \((\mathbb E S_n/n^3-6)^2=O(n^{-2})\).

## Verification
The accompanying standalone Python script `check_variance.py` enumerates all balanced triple-pair phase characters for integers \(4\le n\le16\) using exact integer arithmetic. It checks every four-distinct balanced-pair multiplicity against \(36(n-2)\) and every six-distinct balanced-triple multiplicity against \(36\), and prints their separate variance contributions. These finite checks corroborate the counting mechanism but do not prove the asymptotic error bounds; those follow from the support-dimension estimates and the elementary Riemann sum above. The integral \(11/20\) follows by integrating the three displayed quadratic pieces.

## Relationship to prior work
The flat-polynomial existence theorem of Balister, Bollobás, Morris, Sahasrabudhe and Tiba (2019) studies deterministic unimodular-polynomial flatness, while Cook and Nguyen (2021) study minimum-modulus universality for random trigonometric polynomials. Neither statement asserts the variance of the circle-integrated sixth power for iid Haar phases. Previously known fourth-moment variance calculations do not imply the sixth-moment coefficient: the latter requires additional six-distinct balanced triple-sum characters. The present theorem isolates two separately quantified leading mechanisms.

## Limitations
Historical priority under different terminology has not been conclusively excluded. Only Haar complex phases and consecutive frequencies are treated; no central limit theorem, all-order expansion, or exact finite-degree variance polynomial is asserted. Independent validation has not been performed.

## References
1. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba, *Flat Littlewood Polynomials Exist*, arXiv:1907.09464 (first posted 2019-07-22), https://arxiv.org/abs/1907.09464.
2. N. A. Cook, H. H. Nguyen, *Universality of the minimum modulus for random trigonometric polynomials*, arXiv:2101.07203 (first posted 2021-01-18), https://arxiv.org/abs/2101.07203.
