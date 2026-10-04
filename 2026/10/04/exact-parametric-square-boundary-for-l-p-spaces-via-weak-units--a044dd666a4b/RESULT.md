# Exact parametric square boundary for \(L_p\) spaces via weak units
## Finding
Let \(X=L_p(\mu)\) be an infinite-dimensional real \(L_p\) space, let \(2\le p<\infty\), and let \(r,s\in(0,1]\). For the finite-set parametric property \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\), if \(p=2\) then \(X\) has the property exactly when \(r^2+s^2\le1\). If \(p>2\), then \(X\) has the property exactly when either \(r^p+s^p<1\), or \(r^p+s^p=1\) and \(X\) has no weak unit in its Banach-lattice order. Equivalently, at the critical boundary for \(p>2\), the property holds exactly when every positive element of \(L_p(\mu)\) has a nonzero lattice-disjoint positive element.

Here a weak unit is a positive element \(u\in L_p(\mu)\) such that \(u\wedge v=0\) for \(v\in L_p(\mu)_+\) forces \(v=0\). Thus the critical surface \(r^p+s^p=1\) has a sharp structural dichotomy when \(p>2\): it is attained precisely when the lattice has no weak unit. In particular, every infinite-dimensional \(\sigma\)-finite \(L_p(\mu)\) has a weak unit, so for \(p>2\) it satisfies the property exactly in the strict region \(r^p+s^p<1\). For \(\ell_p(\Gamma)\), the boundary criterion becomes the familiar distinction that an infinite \(\Gamma\) admits a weak unit exactly when \(\Gamma\) is countable.

## Assumptions and scope
All spaces and functions are real. The measure space \((\Omega,\Sigma,\mu)\) is arbitrary subject only to \(L_p(\mu)\) being infinite-dimensional and nonzero; no \(\sigma\)-finiteness or nonatomicity is assumed. The exponent satisfies \(2\le p<\infty\), and \(r,s\in(0,1]\).

For a Banach space \(X\), the finite-set parametric property \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\) means that for every finite set \(F\subset S_X\) there is \(y\in S_X\) such that
\[
\lVert r x\pm s y\rVert\le1\qquad(x\in F).
\]
A weak unit of \(L_p(\mu)\) means a positive \(u\in L_p(\mu)\) with the property that \(u\wedge v=0\), \(v\ge0\), implies \(v=0\). This intrinsic lattice formulation avoids any auxiliary semifiniteness convention.

## Proof
For real scalars \(a,b\) and \(p\ge2\), Clarkson's scalar inequality gives
\[
\frac{|a+b|^p+|a-b|^p}2\ge |a|^p+|b|^p.
\]
When \(p>2\), equality holds exactly when \(ab=0\). For completeness, if \(A=|a|\ge B=|b|>0\), put \(t=B/A\in(0,1]\) and
\[
h(t)=(1+t)^p+(1-t)^p-2-2t^p.
\]
Writing \(q=p-1>1\), strict superadditivity of \(x\mapsto x^q\) on positive scalars gives
\[
(1+t)^q-(1-t)^q>2t^q,
\]
so \(h'(t)>0\) for \(t>0\), while \(h(0)=0\). Hence the equality characterization follows.

Integrating the scalar inequality yields, for \(x,y\in S_{L_p(\mu)}\),
\[
\frac{\lVert r x+s y\rVert_p^p+\lVert r x-s y\rVert_p^p}2\ge r^p+s^p. \tag{1}
\]
Therefore \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\) is impossible whenever \(r^p+s^p>1\): applying the definition to a singleton would make both terms on the left of (1) at most one.

Next use the standard lattice fact that every infinite-dimensional \(L_p\) space with \(p<\infty\) contains a sequence \((y_n)\subset S_{L_p(\mu)}\) of pairwise lattice-disjoint vectors. Indeed, otherwise the measure algebra visible to \(L_p\) would have only finitely many atoms, forcing \(L_p(\mu)\) to be finite-dimensional. Let \(E_n\) denote the essential support of \(|y_n|\). For each fixed \(x\in L_p(\mu)\), disjointness of the \(E_n\) gives
\[
\lVert x\mathbf 1_{E_n}\rVert_p\longrightarrow0.
\]
Moreover,
\[
\lVert r x\pm s y_n\rVert_p^p
=r^p\lVert x\mathbf 1_{E_n^c}\rVert_p^p
 +\lVert r x\mathbf 1_{E_n}\pm s y_n\rVert_p^p,
\]
and the triangle and reverse-triangle inequalities imply
\[
\left|\lVert r x\mathbf 1_{E_n}\pm s y_n\rVert_p-s\right|
\le r\lVert x\mathbf 1_{E_n}\rVert_p.
\]
Consequently
\[
\lVert r x\pm s y_n\rVert_p^p\longrightarrow r^p+s^p.
\]
The convergence is simultaneous for every member of a fixed finite set. Hence \(r^p+s^p<1\) implies \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\).

If \(p=2\), the preceding necessity gives \(r^2+s^2\le1\). Conversely, for a finite \(F\subset S_{L_2(\mu)}\), infinite dimensionality provides a unit vector \(y\) orthogonal to \(\operatorname{span}F\). Then
\[
\lVert r x\pm s y\rVert_2^2=r^2+s^2\le1
\]
for every \(x\in F\), proving the Hilbert-space clause including the boundary.

Assume now \(p>2\) and \(r^p+s^p=1\). If \(x,y\in S_{L_p(\mu)}\) satisfy both \(\lVert r x\pm s y\rVert_p\le1\), then (1) is an equality. The strict equality characterization in the pointwise Clarkson inequality therefore forces \(x y=0\) almost everywhere, equivalently \(|x|\wedge|y|=0\). Thus, if \(L_p(\mu)\) has a weak unit \(u\), applying the property to the normalized vector \(u/\lVert u\rVert_p\) would require a nonzero unit vector disjoint from \(u\), which is impossible.

Conversely, suppose \(L_p(\mu)\) has no weak unit. Given a nonempty finite \(F\subset S_{L_p(\mu)}\), let
\[
h=\sum_{x\in F}|x|.
\]
The positive vector \(h\) is not a weak unit, so there is a nonzero \(v\ge0\) with \(h\wedge v=0\). With \(y=v/\lVert v\rVert_p\), every \(x\in F\) is lattice-disjoint from \(y\), and hence
\[
\lVert r x\pm s y\rVert_p^p=r^p+s^p=1.
\]
The empty finite set is trivial. This proves the boundary clause and completes the classification.

## Verification
The proof was checked separately in the three exhaustive regimes \(r^p+s^p>1\), \(r^p+s^p<1\), and \(r^p+s^p=1\), with a separate treatment of \(p=2\) and \(p>2\). The critical equality step uses the strict scalar Clarkson equality characterization proved above, not a finite experiment. The strict-interior construction uses an actual disjoint normalized sequence and the exact support decomposition; no compactness or separability assumption is inserted implicitly.

The lattice boundary criterion was also checked against the canonical sequence spaces: an infinite \(\ell_p(\Gamma)\) has a weak unit precisely when \(\Gamma\) is countable, so the theorem specializes to boundary failure for countably infinite \(\Gamma\) and boundary attainment for uncountable \(\Gamma\) when \(p>2\), while \(p=2\) is governed by orthogonality.

## Relationship to prior work
Oja, Saealle and Zolk introduced the one-parameter quantitative \(s\)-ASQ property. Avilés, Ciaci, Langemets, Lissitsin and Rueda Zoca then introduced the exact two-parameter \((r,s)\)-\(\mathrm{SQ}_{<\kappa}\) framework. Their Definition 6.1 is the definition used here, and their Example 6.11 records the single diagonal parameter pair \((2^{-1/n},2^{-1/n})\) for \(\ell_n(\kappa)\). The inspected statements do not give a full \((r,s)\) phase diagram for general \(L_p\) spaces or a weak-unit boundary criterion.

Rodríguez and Rueda Zoca study weak almost squareness in Banach function spaces, especially \(L_1\)-type spaces. Their discussion notes that reflexive spaces such as \(L_p[0,1]\) for \(1<p<\infty\) lie in the relevant Banach-lattice framework, but it concerns WASQ/LASQ phenomena rather than the exact finite-set two-parameter property above.

## Limitations
The theorem is restricted to real \(L_p\) spaces with \(2\le p<\infty\) and infinite dimension. It does not classify finite-dimensional \(L_p\) spaces, exponents \(1\le p<2\), complex scalars, or other Banach lattices. The originality comparison cannot exclude an equivalent result hidden under substantially different terminology or in unindexed literature. The proof uses the standard disjoint-sequence structure of infinite-dimensional \(L_p\) spaces; the statement is phrased intrinsically with lattice weak units so that no \(\sigma\)-finiteness assumption is needed.

## References
1. E. Oja, N. Saealle, I. Zolk, *Quantitative versions of almost squareness and diameter 2 properties*, Acta Comment. Univ. Tartu. Math. 24 (2020), 131–145, DOI: 10.12697/ACUTM.2020.24.09.
2. A. Avilés, S. Ciaci, J. Langemets, A. Lissitsin, A. Rueda Zoca, *Transfinite almost square Banach spaces*, arXiv:2204.13449v1 (2022).
3. J. Rodríguez, A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943v1 (2023).
