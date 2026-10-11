# Sharp finite-factor upper-\(p\) estimate constant for Banach-lattice free products
## Finding
For every \(1<p<\infty\) and integer \(r\ge 1\), suppose \(X_1,\ldots,X_r\) are real Banach lattices with upper \(p\)-estimate constant at most \(1\). If
\[
Y=*_{i=1}^r X_i
\]
is their free product in the category of Banach lattices and contractive lattice homomorphisms, then
\[
M^{(p,\infty)}(Y)\le r^{1-1/p}.
\]
Equivalently, every finite family \(z_1,\ldots,z_m\in Y\) satisfies
\[
\left\|\bigvee_{j=1}^m |z_j|\right\|_Y
\le r^{1-1/p}
\left(\sum_{j=1}^m\|z_j\|_Y^p\right)^{1/p}.
\]
The coefficient is universally sharp: for \(X_1=\cdots=X_r=\mathbb R\), the upper \(p\)-estimate constant of the free product is exactly \(r^{1-1/p}\).

## Assumptions and scope
The free product is the coproduct introduced by Martínez-Fernández and Tradacete: each factor has a canonical isometric lattice homomorphism \(\varphi_i:X_i\to Y\), and bounded families of lattice homomorphisms out of the factors extend uniquely to \(Y\). The upper \(p\)-estimate constant is the least \(C\) for which
\[
\left\|\bigvee_{j=1}^m|x_j|\right\|
\le C\left(\sum_{j=1}^m\|x_j\|^p\right)^{1/p}
\]
for every finite family. The result concerns finite numbers of factors and \(1<p<\infty\). No assertion is made here about countably infinite free products or the endpoint \(p=\infty\).

## Proof
Let \(D\) be the solid convex hull of
\[
\bigcup_{i=1}^r\varphi_i(B_{X_i}).
\]
Proposition 3.14 of Martínez-Fernández--Tradacete says that the unit ball of \(Y\) is the norm closure of \(D\). Consequently, for every \(z\in Y\) and every \(\eta>0\), there is \(w\in Y\) with \(\|z-w\|<\eta\) and positive vectors \(a_i\in X_i\) such that
\[
|w|\le \sum_{i=1}^r\varphi_i(a_i),
\qquad
\sum_{i=1}^r\|a_i\|\le \|z\|.
\]
Indeed, after scaling to the unit ball, a member of the solid convex hull is dominated by a finite convex combination of absolute values of canonical factor vectors; grouping terms from the same factor gives the displayed \(a_i\). The closure is handled by choosing \(w\) arbitrarily close to \(z\).

Apply this to each \(z_j\), choosing approximants \(w_j\) and positive vectors \(a_{i,j}\in X_i\). Put
\[
A_i=\bigvee_{j=1}^m a_{i,j}.
\]
Then
\[
\bigvee_{j=1}^m|w_j|
\le \sum_{i=1}^r\varphi_i(A_i).
\]
Proposition 3.10 of the focal paper identifies the closed linear span of the canonical factor copies with their \(\ell_1\)-sum. Therefore
\[
\left\|\sum_{i=1}^r\varphi_i(A_i)\right\|_Y
=
\sum_{i=1}^r\|A_i\|_{X_i}.
\]
Using the upper \(p\)-estimate with constant \(1\) in each factor gives
\[
\|A_i\|_{X_i}
\le
\left(\sum_{j=1}^m\|a_{i,j}\|^p\right)^{1/p}.
\]
Hölder's inequality in the factor index now yields
\[
\begin{aligned}
\sum_{i=1}^r\|A_i\|_{X_i}
&\le
\sum_{i=1}^r
\left(\sum_{j=1}^m\|a_{i,j}\|^p\right)^{1/p}\\
&\le
r^{1-1/p}
\left(\sum_{i=1}^r\sum_{j=1}^m\|a_{i,j}\|^p\right)^{1/p}\\
&\le
r^{1-1/p}
\left(\sum_{j=1}^m
\left(\sum_{i=1}^r\|a_{i,j}\|\right)^p
\right)^{1/p}\\
&\le
r^{1-1/p}
\left(\sum_{j=1}^m\|z_j\|_Y^p\right)^{1/p}.
\end{aligned}
\]
Finally, lattice suprema are norm-continuous: for positive families \(u_j,v_j\),
\[
\left|\bigvee_j u_j-\bigvee_j v_j\right|
\le \bigvee_j|u_j-v_j|
\le \sum_j|u_j-v_j|.
\]
Letting the approximation errors tend to zero proves the upper bound.

For sharpness, take every factor equal to \(\mathbb R\). Proposition 3.13 identifies \(*_{i=1}^r\mathbb R\) with continuous functions on the positive part of the \(\ell_\infty^r\)-unit sphere, where the canonical generators are the coordinate functions \(u_i(t)=t_i\) and
\[
\|f\|_*
=
\inf\left\{
\sum_{i=1}^r c_i:
|f|\le\sum_{i=1}^r c_i u_i,\ c_i\ge0
\right\}.
\]
On that positive sphere, \(\bigvee_i u_i=1\). The norm formula gives \(\|1\|_*\le r\) by taking every \(c_i=1\), while evaluation at the coordinate point \(e_i\) forces \(c_i\ge1\) for every admissible majorant, so \(\|1\|_*=r\). Since \(\|u_i\|_*=1\), the ratio is
\[
\frac{r}{(\sum_{i=1}^r1^p)^{1/p}}=r^{1-1/p}.
\]
Thus no smaller universal coefficient can hold.

## Verification
The proof uses only the focal paper's exact unit-ball description (Proposition 3.14), the exact \(\ell_1\)-sum norm on the linear span of the factor copies (Proposition 3.10), and the explicit scalar-factor norm formula (Proposition 3.13), together with the defining upper \(p\)-estimate and Hölder's inequality. The approximation step is norm-stable because finite lattice suprema are Lipschitz with respect to the sum of the coordinate norm errors. The sharpness calculation is exact and contains no numerical approximation or finite-search surrogate.

## Relationship to prior work
Martínez-Fernández and Tradacete prove in Proposition 8.5 that the free product of two Banach lattices with upper \(p\)-estimate constant \(1\) again has an upper \(p\)-estimate, but their statement is qualitative and gives no constant. In the same paper, Proposition 8.3 and Remark 8.4 give the sharp coefficient \(2^{1-1/p}\) for \(p\)-convexity of two factors; that result assumes the stronger \(p\)-convexity condition and controls \((\sum |x_j|^p)^{1/p}\), not the lattice supremum governed by upper \(p\)-estimates. The present result supplies the missing quantitative upper-\(p\) law for every finite number of factors and proves its universal optimality.

Earlier work on free Banach lattices with upper \(p\)-estimates constructs and analyzes the corresponding free objects over Banach spaces, including functional representations and push-outs. Those results do not state the sharp upper \(p\)-estimate constant of the ordinary Banach-lattice coproduct. A previously indexed result for \(C(K_1)*C(K_2)\) gives a two-slice formula for the norm in that special class; it does not imply the finite-factor upper-\(p\) estimate for arbitrary Banach-lattice factors.

## Limitations
The theorem is restricted to finitely many factors and \(1<p<\infty\). It gives the best universal coefficient under the normalization that every factor has upper \(p\)-estimate constant at most \(1\); it does not claim an optimal formula when the factor constants are unequal. The originality comparison found no covering statement, but an older equivalent categorical formulation under different terminology remains a residual literature risk.

## References
1. G. Martínez-Fernández and P. Tradacete, *Free Products of Banach Lattices*, arXiv:2605.28988v1, 27 May 2026. In particular Propositions 3.10, 3.13, 3.14, 8.5 and Remark 8.4.
2. E. García-Sánchez, D. H. Leung, M. A. Taylor and P. Tradacete, *Banach lattices with upper p-estimates: free and injective objects*, Mathematische Annalen 391 (2025), 3363--3398, DOI 10.1007/s00208-024-03002-8; first published online 2 October 2024.
3. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices under convexity conditions*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas 116 (2022), article 15, DOI 10.1007/s13398-021-01155-8.
