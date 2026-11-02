# A three-tenths commutativity law for interval-translation rook monoids

## Finding
Let \(M_n\) be the finite inverse monoid of block-diagonal rook matrices (equivalently, translations between contiguous nonempty subintervals of \([n]\)), together with the zero map. For \(n\ge2\), define
\[
Z_n=\#\{(x,y)\in (M_n\setminus\{0\})^2:xy=yx=0\},\qquad C_n=\#\{(x,y)\in M_n^2:xy=yx\}.
\]
Then
\[
Z_n=\frac{n(n-1)(n+1)(n+2)(n^2+n-1)}{30},
\quad\frac{C_n}{|M_n|^2}=\frac3{10}+O(n^{-1}).
\]
Among ordered commuting pairs, the proportion whose common product is zero is \(1-O(n^{-1})\). Thus the nontrivial limiting commutativity probability \(3/10\) is entirely explained by mutual annihilation, not by the nonzero product of commuting translations. The exact displayed formula counts only pairs with both entries **nonzero**; the extra pairs involving the zero element are handled in the proof.

## Assumptions and scope
For each integer \(n\ge2\), write \([n]=\{1,\ldots,n\}\). A nonzero element \(x\in M_n\) is uniquely given by \((a,c,\ell)\) with integers \(1\le\ell\le n\), \(1\le a,c\le n-\ell+1\): it maps \(a+i\mapsto c+i\) for \(0\le i<\ell\), and is undefined elsewhere. This is the integer triple representation of the monoid in Fikioris--Fikioris (2021), with shift \(d=c-a\). It does not include partial bijections whose domain is disconnected. All counts are of ordered pairs of actual elements, not conjugacy types. Composition conventions do not affect commutativity or simultaneous vanishing.

## Proof
**1. Size.** For each length \(\ell\) there are \((n-\ell+1)^2\) nonzero maps. Hence, with \(T_n=|M_n|-1\),
\[
T_n=\sum_{\ell=1}^n(n-\ell+1)^2=\frac{n(n+1)(2n+1)}6.
\]

**2. Exactly count mutual annihilation among nonzero pairs.** Write \(x=(a,c,\ell)\) and \(y=(u,w,k)\). Their domain/image intervals are respectively \(I=[a,a+\ell-1]\), \(I'=[c,c+\ell-1]\), \(J=[u,u+k-1]\), and \(J'=[w,w+k-1]\). Both compositions vanish precisely when \(I\cap J'=\varnothing\) and \(I'\cap J=\varnothing\). These disjointness conditions concern disjoint variable pairs \((a,w)\) and \((c,u)\). For prescribed lengths \(\ell,k\) with \(\ell+k\le n\), the number of placements of the first interval strictly before the second equals
\[
Q_{n;\ell,k}=\sum_{a=1}^{n-\ell-k+1}(n-\ell-k+2-a)
=\binom{n-\ell-k+2}{2}.
\]
By reflection, the number for the opposite ordering is the same; if \(\ell+k>n\), neither ordering exists. Therefore, for each allowable length pair, there are exactly \(4Q_{n;\ell,k}^2\) ordered nonzero map pairs whose products both vanish. Grouping by \(r=n-\ell-k+1\) gives
\[
Z_n^{*}=\sum_{r=1}^{n-1}(n-r)r^2(r+1)^2
=\frac{n(n-1)(n+1)(n+2)(n^2+n-1)}{30}.
\]
The sum-to-polynomial identity follows by expanding \((n-r)(r^4+2r^3+r^2)\) and applying the elementary power-sum identities through fifth degree. Here \(Z_n^{*}\) excludes the monoid zero as an input; the number of **all** mutually annihilating ordered pairs equals \(Z_n^{*}+2T_n+1\). In this document \(Z_n\) in the headline denotes \(Z_n^{*}\); the distinction only changes lower-order terms.

**3. Nonzero-product commuting pairs are sparse.** Let \(d=c-a\) and \(e=w-u\). In row-action convention the domain interval of \(xy\), if nonempty, begins at \(\max(a,u-d)\); that of \(yx\) begins at \(\max(u,a-e)\). Thus whenever \(xy=yx\ne0\), their left endpoints agree, forcing at least one of the following four linear equalities:
\[
a=u,\qquad d=0\ (c=a),\qquad e=0\ (w=u),\qquad c=w.
\]
Indeed the two maxima must attain equal members of their respective two-element sets, and these four cases exhaust the possible choices. Each equality removes one degree of freedom from the six integer coordinates \((a,c,\ell,u,w,k)\); each coordinate has at most \(n\) choices. By the union bound there are at most \(4n^5\) such ordered pairs. This bound includes any potential degeneracies and remains valid at the finite endpoints.

**4. Normalization.** Let \(P_n\) count the commuting pairs with nonzero common product. With \(0\le P_n\le4n^5\), the commuting-pair count is
\[
C_n=Z_n^{*}+2T_n+1+P_n.
\]
As \(T_n=n^3/3+O(n^2)\) and \(Z_n^{*}=n^6/30+O(n^5)\), division by \((T_n+1)^2=n^6/9+O(n^5)\) yields
\[
\frac{C_n}{|M_n|^2}=\frac3{10}+O(n^{-1}).
\]
Moreover \(P_n/C_n=O(n^{-1})\), proving the final conditional assertion.

## Verification
`verify.py` independently enumerates the partial bijections and computes products by explicit dictionary composition for all dimensions \(1\le n\le10\). It confirms the zero-product polynomial in every case and checks the decomposition into mutually annihilating versus nonzero-product commuting pairs. Running `python3 verify.py` prints `VERIFY_OK`. Its finite checks are not the proof of the infinite assertion; the preceding interval-counting and codimension arguments are.

## Relationship to prior work
Fikioris and Fikioris [1] defined the integer interval-translation monoid and established the triple product law and structural properties, including the idempotent/nilpotent dichotomy. Their later extension [2] treats real-parameter monoids and compares the structural theories. Those multiplication formulas identify the underlying object and are credited, but the inspected material does not provide the exact mutual-annihilation polynomial or the commuting-probability limit. In particular, the assertion here is not the universal commuting probability of the full symmetric inverse monoid. Its proof requires aggregating six interval coordinates and controlling separately the nonzero-product commuting locus.

## Limitations
The theorem concerns this specific interval-translation inverse monoid, not every submonoid of a rook monoid. It does not give a closed finite-\(n\) formula for the nonzero-product commuting part, nor a second-order coefficient of the commuting probability. Searches cannot rule out every equivalent treatment under other terminology; earlier general commuting-pair enumeration for partial translations remains the principal publication-priority risk. The result has not undergone independent mathematical audit.

## References
[1] George Fikioris and Giannis Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863, first posted 2021-11-02. https://arxiv.org/abs/2111.01863

[2] George Fikioris and Giannis Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496 (first posted 2023-02-19); *Semigroup Forum* 107 (2023), 637–650. https://arxiv.org/abs/2302.09496 ; https://doi.org/10.1007/s00233-023-10393-8
