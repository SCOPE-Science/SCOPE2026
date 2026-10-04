# Arbitrary-index \(\ell_p\)-sums of Daugavet spaces have exactly one SCD point
## Finding
Let \(\Gamma\) be any infinite index set, let \(1<p<\infty\), and let \((X_\gamma)_{{\gamma\in\Gamma}}\) be nonzero real Banach spaces. Define
\[
X=\left(\bigoplus_{{\gamma\in\Gamma}}X_\gamma\right)_p.
\]
Then \(0\) is a slicely countably determined point of \(B_X\). If every \(X_\gamma\) has the Daugavet property, then
\[
\operatorname{{SCD}}(B_X)=\{{0\}}.
\]
Thus the countably indexed result extends to arbitrary index cardinality: even a nonseparable \(\ell_p\)-sum of arbitrarily large density has a countable slice witness for its unique SCD point when every coordinate has the Daugavet property.

## Assumptions and scope
All spaces are real. The index set \(\Gamma\) is infinite, and \(1<p<\infty\). The direct sum consists of families \(x=(x_\gamma)_{{\gamma\in\Gamma}}\) satisfying
\[
\sum_{{\gamma\in\Gamma}}\|x_\gamma\|^p<\infty,
\]
with the usual \(\ell_p\)-norm. A point \(a\) of a bounded convex set is SCD when it admits a countable determining family of slices: every choice of one point from each slice has \(a\) in the closed convex hull of the chosen points.

The first assertion needs only nontriviality of the coordinate spaces. The second assertion additionally assumes the Daugavet property for every coordinate space. The endpoints \(p=1\) and \(p=\infty\) are excluded.

## Proof
Choose pairwise distinct coordinates \(\gamma_1,\gamma_2,\ldots\in\Gamma\). For each \(n\), choose \(x_n^*\in S_{{X_{{\gamma_n}}^*}}\). For integers \(n,k\ge 2\), let \(f_n\in S_{{X^*}}\) be the coordinate functional
\[
f_n((x_\gamma))=x_n^*(x_{{\gamma_n}}),
\]
and define the slice
\[
S_n^k=\{x\in B_X: f_n(x)>1-1/k\}.
\]
We show that the countable family \(\{S_n^k:n,k\ge2\}\) determines \(0\).

Choose arbitrary points \(z_n^k\in S_n^k\). Fix \(K\ge2\) and, for \(1\le n\le K\), let \(u_n=P_{{\gamma_n}}z_n^K\) be the vector supported only on coordinate \(\gamma_n\), and put \(r_n=z_n^K-u_n\). Since \(z_n^K\in S_n^K\),
\[
\|u_n\|>1-1/K.
\]
Because \(\|z_n^K\|\le1\),
\[
\|r_n\|^p
=\|z_n^K\|^p-\|u_n\|^p
\le1-(1-1/K)^p
\le p/K,
\]
where the final inequality is Bernoulli's inequality. Hence
\[
\left\|\frac1K\sum_{{n=1}}^K r_n\right\|
\le (p/K)^{{1/p}}.
\]
The vectors \(u_1,\ldots,u_K\) have disjoint coordinate supports, so
\[
\left\|\frac1K\sum_{{n=1}}^K u_n\right\|^p
=\frac1{{K^p}}\sum_{{n=1}}^K\|u_n\|^p
\le K^{{1-p}},
\]
and therefore
\[
\left\|\frac1K\sum_{{n=1}}^K z_n^K\right\|
\le (p/K)^{{1/p}}+K^{{1/p-1}}\longrightarrow0.
\]
Each displayed average belongs to the convex hull of the selected points. Thus \(0\) belongs to their closed convex hull, proving \(0\in\operatorname{{SCD}}(B_X)\).

Now assume every \(X_\gamma\) has the Daugavet property and let \(x=(x_\gamma)\in\operatorname{{SCD}}(B_X)\). Fix \(\gamma\in\Gamma\) and regroup the direct sum isometrically as
\[
X=X_\gamma\oplus_p
\left(\bigoplus_{{\eta\in\Gamma\setminus\{\gamma\}}}X_\eta\right)_p.
\]
Langemets--Lõo--Martín--Rueda Zoca, Proposition 3.11, states that in \(E\oplus_pY\), with \(E\) a Daugavet space and \(1<p<\infty\), every SCD point has zero \(E\)-coordinate. Applying that proposition to the displayed regrouping gives \(x_\gamma=0\). Since \(\gamma\) was arbitrary, \(x=0\). Together with the first part this proves \(\operatorname{{SCD}}(B_X)=\{0\}\).

The nonstandard input just invoked was checked in the full public text of the cited source: its Proposition 3.11 is stated for a Daugavet factor and an arbitrary complementary Banach space, so no separability or countability assumption enters this coordinatewise obstruction.

## Verification
The determining-family argument is uniform in the cardinality of \(\Gamma\): only a chosen countable subset of coordinates is used, while selected points may have arbitrary support elsewhere. The error estimate
\[
(p/K)^{{1/p}}+K^{{1/p-1}}
\]
tends to zero for exactly \(1<p<\infty\). No finite experiment or enumeration is used as evidence for the infinite-dimensional claim.

For uniqueness, the only external lemma needed is the source's Proposition 3.11. Its hypotheses match after regrouping: the selected coordinate is a Daugavet space, the complement is arbitrary, and the sum exponent lies strictly between \(1\) and \(\infty\).

## Relationship to prior work
The 2023 source formally proves the countable-sequence versions. Its Theorem 3.6 states that for a sequence \(\{X_n:n\in\mathbb N\}\) of Daugavet spaces, the \(\ell_p\)-sum has exactly the SCD point \(0\). Its Proposition 3.7 proves \(0\) is SCD for a countable sequence of arbitrary nontrivial summands, and Proposition 3.11 supplies the one-coordinate Daugavet obstruction. The source's notation for infinite direct sums is explicitly sequence-indexed.

The present statement removes the countability of the index set. This is not a change of notation only: the ambient ball may be nonseparable and have arbitrarily large density, yet a countable coordinate subsystem still determines \(0\), while the coordinatewise obstruction eliminates every nonzero point when all factors are Daugavet. Searches for the arbitrary-index, uncountable, and equivalent SCD formulations did not locate a published statement covering this extension.

## Limitations
The claim does not treat \(p=1\) or \(p=\infty\); the cited source records that the analogous existence statement for \(0\) can fail at those endpoints. Originality remains subject to the usual literature-search risk: the extension is short once the countable proof and the coordinate obstruction are known, and an equivalent arbitrary-index formulation could exist under different terminology. No independence or external certification is claimed.

## References
1. M. Lõo, *Slicely countably determined points in Banach spaces*, Master's thesis, University of Tartu, 2023. Repository record available from 2023-07-03, handle 10062/91236.
2. J. Langemets, M. Lõo, M. Martín, A. Rueda Zoca, *Slicely countably determined points in Banach spaces*, arXiv:2311.03064v1, submitted 2023-11-06; Journal of Mathematical Analysis and Applications 537 (2024), 128248. Primary MSC 2020: 46B20.
