# Commuting-pair polynomial and a three-tenths law for consecutive-diagonal rook monoids

## Finding
For every integer \(n\ge 2\), let \(M_n\) be the inverse monoid consisting of the zero matrix and every \(n\)-by-\(n\) zero-one rook matrix whose ones form a nonempty uninterrupted block on one diagonal. With multiplication given by ordinary matrix multiplication, the number of **ordered commuting pairs** is
\[
C_n=\bigl|\{(x,y)\in M_n^2:xy=yx\}\bigr|=\frac{2n^6+8n^5+25n^4+50n^3+63n^2+32n+60}{60}.
\]
Since \(|M_n|=1+n(n+1)(2n+1)/6\), uniform independent \(X,Y\in M_n\) satisfy
\[
\Pr(XY=YX)=\frac{C_n}{(1+n(n+1)(2n+1)/6)^2}
=\frac{3}{10}+\frac{3}{10n}+O(n^{-2}).
\]
Thus the limiting commuting probability is exactly \(3/10\). More precisely, among ordered pairs of nonzero elements, there are
\[
Z_n=\frac{n(n-1)(n+1)(n+2)(n^2+n-1)}{30}
\]
pairs with both products zero, and
\[
N_n=\frac{n(n+1)(2n^3+23n^2-3n+8)}{60}
\]
pairs with equal **nonzero** products. These are disjoint, and \(C_n=2|M_n|-1+Z_n+N_n\).

## Assumptions and scope
An element is zero or is specified uniquely by three integers \((a,b,k)\), where \(k\ge1\), \(1\le a,b\le n-k+1\), and its nonzero entries occur at \((a+i,b+i)\) for \(0\le i<k\). It is the partial translation carrying the integer interval \(I=[a,a+k-1]\) onto \(J=[b,b+k-1]\) by displacement \(b-a\). This is precisely the integer consecutive-diagonal rook monoid of Fikioris and Fikioris, not the whole symmetric inverse monoid or the real-parameter extension.

Pairs are ordered and the zero matrix and identity matrix are included. The original semigroup \(S_n=M_n\setminus\{1\}\) consequently has \(C_n-2|M_n|+1\) commuting ordered pairs, since deleting the identity deletes exactly \(2|M_n|-1\) commuting pairs. No assertion is made about a different sampling measure or the full rook monoid.

## Proof
**1. Both products zero.** Write another nonzero element as an interval translation from \(K=[c,c+j-1]\) to \(L=[d,d+j-1]\). The product \(xy\) is zero exactly when \(J\cap K\) is empty; the reverse product \(yx\) is zero exactly when \(L\cap I\) is empty. Fix lengths \(k,j\). If \(k+j\le n\), the number of ordered positions of two disjoint integer intervals of lengths \(k,j\) is
\[
H_{k,j}=(n-k-j+1)(n-k-j+2),
\]
and otherwise it is zero. This follows by separately summing the cases in which the first interval lies strictly left or right of the second. The choices of positions \((b,c)\) and \((d,a)\) are independent, so the number with both products zero is \(H_{k,j}^2\). There are \(s-1\) positive length pairs with sum \(s\); hence
\[
Z_n=\sum_{s=2}^{n}(s-1)(n-s+1)^2(n-s+2)^2
=\frac{n(n-1)(n+1)(n+2)(n^2+n-1)}{30}.
\]
The equality follows by summing fourth-degree polynomials or standard power sums.

**2. Nonzero commuting products, both factors idempotent.** A nonzero element is idempotent exactly when \(a=b\), so there are \(E=n(n+1)/2\) interval-identity maps. Every two such maps commute; their product is nonzero precisely when their intervals intersect. The number of ordered disjoint pairs of nonempty intervals is \(2\binom{n+2}{4}\). Thus the contribution is \(E^2-2\binom{n+2}{4}\).

**3. Exactly one factor idempotent.** Let \(e_I\) be identity on an interval \(I\), and let \(y\) translate \(K\) to \(L\) by a nonzero displacement. Comparing the domains of \(e_Iy\) and \(ye_I\) shows that these products are equal and nonzero exactly when \(I\) contains the convex hull \(K\cup L\). Indeed, equality requires the nonempty intersections \(K\cap I=K\cap (I-(d-c))\); because these two equal-length enclosing intervals have different endpoints, their intersections with the connected interval \(K\) can coincide nontrivially only when \(K\) is contained in both.

Let the convex hull have length \(h\) and begin at \(u\). For each \(h\in\{2,\dots,n\}\), there are \(2(h-1)\) choices of the nonzero displacement and the common source/target length for each position \(u\). The number of intervals \(I\) containing the hull is \(u(n-u-h+2)\). Therefore the count with the idempotent in a specified position is
\[
T_n=2\sum_{h=2}^{n}(h-1)\sum_{u=1}^{n-h+1}u(n-u-h+2)
=2\sum_{h=2}^{n}(h-1)\binom{n-h+3}{3}
=\frac{n(n-1)(n+1)(n+2)(n+3)}{60}.
\]
Both orderings together contribute \(2T_n\).

**4. Both factors nilpotent.** Put \(t=b-a\), \(v=d-c\), which are nonzero. The two composition domains, when nonempty, have endpoints
\[
[\max(a,c-t),\min(a+k-1,c+j-1-t)]
\quad\hbox{and}\quad
[\max(c,a-v),\min(c+j-1,a+k-1-v)].
\]
If \(t>0>v\), the second lower endpoint is strictly larger than the first. The other opposite-sign case follows by exchanging factors, so commuting nonzero products require equal signs. If \(t,v>0\), equality of lower endpoints forces \(a=c\), and equality of nonempty upper endpoints is equivalent to \(j-t=k-v=\ell\ge1\). All such ordered pairs are uniquely parametrized by positive integers \((a,t,v,\ell)\) with \(a+t+v+\ell\le n+1\); there are \(\binom{n+1}{4}\) of them. Reflection of the chain accounts for an equal number of negative-negative pairs. Thus the nilpotent-nilpotent contribution is \(2\binom{n+1}{4}\).

**5. Combine.** The four nonzero-product cases yield
\[
N_n=\left(E^2-2\binom{n+2}{4}\right)+2T_n+2\binom{n+1}{4}
=\frac{n(n+1)(2n^3+23n^2-3n+8)}{60}.
\]
There are \(2|M_n|-1\) ordered pairs with at least one zero factor; all commute. The remaining commuting pairs are disjointly partitioned into those counted by \(Z_n\) and \(N_n\). Substituting the identities above gives the claimed \(C_n\). Finally, dividing the leading two polynomial coefficients of \(C_n\) by those of \(|M_n|^2\) gives the displayed limit and first correction.

## Verification
The standalone file `verify_commuting.py` constructs the actual partial-translation matrices as finite maps and computes their two products independently by dictionary composition. It exhaustively checks every ordered pair for \(1\le n\le12\), comparing the counts of zero-zero products and of four categories of nonzero equal products with the formulas above. There are 986,374 ordered pairs across these twelve sizes. Run `python3 verify_commuting.py` in the directory containing this file. The expected terminal line is `ALL_CONSECUTIVE_DIAGONAL_COMMUTATION_CHECKS_PASSED 12 986374`. These tests are finite corroboration; the proof is the all-\(n\) argument above.

## Relationship to prior work
Fikioris and Fikioris (2021; subsequently published in 2022) introduced \(M_n\), proved its triplet product law, determined idempotents, nilpotents, ideals, and other properties, and separately treated commuting subsemigroups. The 2023 follow-up extends the parameters from integers to reals and studies inverse-monoid structure, nilpotency, and ideals. Neither examined source presents an ordered commuting-pair enumerator for the integer \(M_n\). Prior work on centralizers in the full symmetric inverse semigroup treats a larger monoid; its centralizer descriptions do not by themselves count commuting pairs internal to this specified consecutive-diagonal submonoid. The one-direction nonzero-product enumeration for this very \(M_n\) is also prior work, but does not determine whether the two products agree, including the joint zero-zero event.

## Limitations
The priority comparison cannot rule out an equivalent formula in unexamined semigroup-counting literature. Full text of the 2020 symmetric-inverse centralizer article and the 2015 partial-isometry article was not materially inspected. The theorem is specific to matrices with a single uninterrupted diagonal block; it does not claim a count for all partial isometries. The code has exhaustive finite scope only. No independent mathematical audit has been performed.

## References
1. G. Fikioris and G. Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863 (first posted 2021-11-02); *Semigroup Forum* 105 (2022), 191–216. https://arxiv.org/abs/2111.01863
2. G. Fikioris and G. Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496 (first posted 2023-02-19); *Semigroup Forum* 107 (2023), 637–650. https://doi.org/10.1007/s00233-023-10393-8
3. J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, *Communications in Algebra* 48 (2020), 5181–5194. https://doi.org/10.1080/00927872.2020.1782926
4. F. Al-Kharousi, R. Kehinde, and A. Umar, *On the semigroup of partial isometries of a finite chain*, *Communications in Algebra* 44 (2016), 639–647. https://doi.org/10.1080/00927872.2014.984838
