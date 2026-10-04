# Sharp average-roughness law for finite and infinite \(\ell_p\)-sums
## Finding
For a real Banach space \(X\), define its average-roughness modulus by
\[
\operatorname{ar}(X)=\sup\{\delta\in[0,2]: X\text{ is }\delta\text{-average rough}\}.
\]
Let \(1<p<\infty\) and let \(Z=(\bigoplus_{\gamma\in\Gamma}X_\gamma)_p\), where every \(X_\gamma\) is nonzero.

If \(\Gamma\) is finite with \(|\Gamma|=m\), then every choice of \(\delta\)-average rough factors satisfies
\[
Z\text{ is }\delta m^{-1/p}\text{-average rough},
\]
and every finite \(m\)-fold \(\ell_p\)-sum satisfies the universal upper bound
\[
\operatorname{ar}(Z)\le 2m^{-1/p}.
\]
Consequently, when all \(m\) factors are octahedral,
\[
\operatorname{ar}(Z)=2m^{-1/p}.
\]

If \(\Gamma\) is infinite, then
\[
\operatorname{ar}(Z)=0.
\]
Thus the sharp positive constant for finitely many octahedral summands decays exactly like \(m^{-1/p}\), and it collapses to zero as soon as infinitely many nonzero summands are present.

## Assumptions and scope
All spaces are real and nonzero. The exponent satisfies \(1<p<\infty\). For an index set \(\Gamma\), the notation \((\bigoplus_{\gamma\in\Gamma}X_\gamma)_p\) denotes the usual Banach \(\ell_p\)-sum. A Banach space \(X\) is \(\delta\)-average rough when, for every finite family \(x_1,\dots,x_n\in S_X\),
\[
\limsup_{\|y\|\to0}\frac1n\sum_{i=1}^n\frac{\|x_i+y\|+\|x_i-y\|-2}{\|y\|}\ge\delta.
\]
The statement concerns average roughness, not ordinary pointwise roughness. The exact finite formula requires octahedral factors because octahedrality is equivalent to \(2\)-average roughness.

## Proof
Write \(q=p/(p-1)\).

For the finite lower bound, suppose \(\Gamma=\{1,\dots,m\}\) and every \(X_j\) is \(\delta\)-average rough. Fix \(z_i=(x_{ij})_{j=1}^m\in S_Z\), \(i=1,\dots,n\), and a small parameter \(\varepsilon>0\). For each \(i\), put
\[
s_{ij}=\|x_{ij}\|,\qquad c_{ij}=s_{ij}^{p-1}.
\]
Because \(\sum_j s_{ij}^p=1\), the vector \(c_i=(c_{ij})_j\) belongs to \(S_{\ell_q^m}\), is nonnegative, and satisfies
\[
\sum_{j=1}^m c_{ij}s_{ij}=1.
\]
Let
\[
c_j=\frac1n\sum_{i=1}^n c_{ij}.
\]
Since \(\|c_i\|_1\ge\|c_i\|_q=1\), one has \(\sum_j c_j\ge1\). Whenever \(c_j>0\), define weights
\[
\mu_{ij}=\frac{c_{ij}}{n c_j},\qquad \sum_i\mu_{ij}=1.
\]
Using the weighted form of the standard equivalent characterization of \(\delta\)-average roughness, choose \(y_j\in X_j\) with \(\|y_j\|=\varepsilon\) and
\[
\sum_i\mu_{ij}\bigl(\|x_{ij}+y_j\|+\|x_{ij}-y_j\|\bigr)
\ge (\delta-\varepsilon)\varepsilon+2\sum_i\mu_{ij}\|x_{ij}\|.
\]
For indices with \(c_j=0\), choose any \(y_j\) of norm \(\varepsilon\). Put \(y=(y_j)_j\), so \(\|y\|_p=m^{1/p}\varepsilon\). Minkowski's inequality in \(\ell_p^m\), followed by the norming functional \(c_i\), gives
\[
\|z_i+y\|_p+\|z_i-y\|_p\ge\sum_j c_{ij}\bigl(\|x_{ij}+y_j\|+\|x_{ij}-y_j\|\bigr).
\]
Averaging in \(i\), regrouping by \(j\), and applying the preceding inequalities yields
\[
\frac1n\sum_i\bigl(\|z_i+y\|_p+\|z_i-y\|_p\bigr)
\ge 2+(\delta-\varepsilon)\varepsilon\sum_j c_j
\ge 2+(\delta-\varepsilon)m^{-1/p}\|y\|_p.
\]
Letting \(\varepsilon\downarrow0\) proves that the finite sum is \(\delta m^{-1/p}\)-average rough. If every factor is octahedral, take \(\delta=2\).

For the universal finite upper bound, choose unit vectors \(u_j\in X_j\) and let \(e_j u_j\in S_Z\) be the vector supported only in coordinate \(j\). Given \(h=(h_k)_k\in Z\), write \(\eta=\|h\|_p\) and \(a_j=\|h_j\|\). Then
\[
\|e_j u_j\pm h\|_p^p\le (1+a_j)^p+\eta^p-a_j^p.
\]
There are constants \(C_p>0\) and \(r=\min\{p,2\}>1\) such that, uniformly for \(0\le a\le\eta\le1\),
\[
\bigl((1+a)^p+\eta^p-a^p\bigr)^{1/p}\le 1+a+C_p\eta^r.
\]
Indeed, Taylor's formula gives \((1+a)^p\le1+pa+C'_p a^r\), and concavity of \(t\mapsto t^{1/p}\) gives the displayed estimate. Hence
\[
\frac1m\sum_{j=1}^m\bigl(\|e_j u_j+h\|_p+\|e_j u_j-h\|_p\bigr)
\le 2+\frac{2}{m}\sum_j a_j+2C_p\eta^r.
\]
By Hölder's inequality,
\[
\sum_j a_j\le m^{1-1/p}\eta,
\]
so after subtracting \(2\), dividing by \(\eta\), and letting \(\eta\downarrow0\), the defining limsup for this test family is at most \(2m^{-1/p}\). Therefore \(\operatorname{ar}(Z)\le2m^{-1/p}\), proving equality for octahedral factors.

Finally suppose \(\Gamma\) is infinite. For every positive integer \(m\), choose \(m\) distinct indices and the corresponding \(m\) axis vectors. The same upper-bound argument allows arbitrary additional coordinates of \(h\), because their total contribution is already included in \(\eta^p-a_j^p\). Thus any positive average-roughness constant \(\delta\) would have to satisfy
\[
\delta\le2m^{-1/p}
\]
for every \(m\). Letting \(m\to\infty\) forces \(\delta=0\). Hence \(\operatorname{ar}(Z)=0\).

## Verification
The proof was checked against the definition and weighted equivalent formulation of average roughness in Haller--Langemets--Nadel. The finite lower bound specializes at \(m=2\) to their published constant \(2^{1-1/p}\) for two octahedral summands. The upper-bound scalar estimate uses only Taylor's formula, concavity of \(t^{1/p}\), and Hölder's inequality, and its error term is \(o(\eta)\) because \(r=\min\{p,2\}>1\). The infinite case uses the same finite-axis test for arbitrary \(m\); no finite computation is being promoted to an infinite proof.

## Relationship to prior work
Haller, Langemets, and Nadel proved the two-summand theorem: if \(X\) and \(Y\) are \(\delta\)-average rough, then \(X\oplus_pY\) is \(2^{-1/p}\delta\)-average rough, and they proved the universal two-summand upper bound \(2^{1-1/p}\). Their paper explicitly formulates and proves the result for two Banach spaces. The present result identifies the sharp dependence on the number \(m\) of summands, improves what one obtains by repeated binary application when \(m>2\), and adds the infinite-index collapse \(\operatorname{ar}=0\). Searches for the exact \(m\)-summand law, its \(m^{-1/p}\) constant, the infinite-sum collapse, and dual slice formulations did not locate a published statement covering these conclusions.

## Limitations
The result is restricted to real Banach spaces and \(1<p<\infty\). The finite exact identity uses octahedrality of every factor; with merely \(\delta\)-average rough factors, the proof gives the lower bound \(\delta m^{-1/p}\), not a general exact formula. The infinite conclusion is only that no positive average-roughness constant exists; it does not classify other roughness moduli. The literature search cannot exclude an unindexed or inaccessible source stating an equivalent multi-summand result.

## References
1. R. Haller, J. Langemets, R. Nadel, “Stability of average roughness, octahedrality, and strong diameter 2 properties of Banach spaces with respect to absolute sums,” arXiv:1702.03140v1, 10 February 2017; Banach Journal of Mathematical Analysis 12 (2018), 222–239, DOI 10.1215/17358787-2017-0040.
2. M. D. Acosta, J. Becerra-Guerrero, G. López-Pérez, “Stability Results of Diameter Two Properties,” Journal of Convex Analysis 22 (2015), 1–17.
