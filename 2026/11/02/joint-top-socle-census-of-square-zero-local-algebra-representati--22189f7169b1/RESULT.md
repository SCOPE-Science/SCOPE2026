# Joint top–socle census of square-zero local algebra representations

## Finding

For every integer \(r\geq1\), every integer \(d\geq1\), and every finite field \(\mathbb F_q\), the number of framed \(d\)-dimensional representations of the split local algebra
\[
\Lambda_r=\mathbb F_q\langle z_1,\ldots,z_r\rangle/(z_i z_j:1\leq i,j\leq r)
\]
with a prescribed pair of dimensions for their radical and socle is given by a finite Gaussian-binomial expression. Equivalently, the formula counts all ordered matrix tuples \((A_1,\ldots,A_r)\) in \(M_d(\mathbb F_q)^r\) satisfying \(A_iA_j=0\) for every ordered pair, with specified dimensions of their combined image and common kernel.

Write \(U=\sum_i\operatorname{im}A_i\), \(W=\bigcap_i\ker A_i\), and \(a=\dim U\), \(c=d-\dim W\). Define the Gaussian binomial coefficient \({n\brack k}_q\) as the number of \(k\)-dimensional subspaces of \(\mathbb F_q^n\), and take it to be zero for \(k\notin[0,n]\). Then the exact number \(R_{r,d}(a,c;q)\) is
\[
R_{r,d}(a,c;q)={d\brack a}_q{d-a\brack c}_q
\sum_{i=0}^{a}(-1)^{a-i}q^{\binom{a-i}{2}}{a\brack i}_q
\prod_{j=0}^{c-1}(q^{ri}-q^j),
\]
where empty products equal one. This holds without restrictions on the characteristic. It gives the entire joint distribution of the module-top dimension \(d-a\) and the socle dimension \(d-c\).

The nonempty pairs are exactly \((a,c)=(0,0)\) and the positive pairs satisfying
\[
a+c\leq d,\qquad a\leq rc,\qquad c\leq ra.
\]
Moreover, over any field, the corresponding **reduced** exact-rank representation locus is smooth and geometrically irreducible; it is a Zariski-locally trivial open subset of a rank-\(rac\) vector bundle over the flag variety of \(U\subseteq W\). Its dimension is
\[
a(d-a)+c(d-a-c)+rac.
\]
The point count, rather than the elementary flag parameterization alone, is the principal arithmetic assertion.

## Assumptions and scope

A framed representation means an action on a fixed vector space with a chosen basis: no quotient by change of basis is taken. The radical \(J\) of \(\Lambda_r\) is spanned by the \(z_i\) and satisfies \(J^2=0\). Thus \(JM=U\) and \(\operatorname{soc}M=W\). All \(r\) generators are labeled. The integers \(a,c\) lie between zero and \(d\); if \(a+c>d\), the count is zero. The formula concerns \(\mathbb F_q\)-points of the representation space and its reduced rank strata, not the full nonreduced scheme structure or isomorphism classes.

## Proof

**1. Rank flags.** The relations \(A_iA_j=0\) imply \(U\subseteq W\). Conversely, given any flag \(U\subseteq W\subseteq V\) with \(\dim U=a\), \(\operatorname{codim}W=c\), choose linear maps \(\bar A_i:V/W\to U\) and compose with the quotient and inclusion. Every such matrix tuple automatically has all pairwise products zero. Its aggregate image equals \(U\) exactly when the images of the \(\bar A_i\) span \(U\), and its common kernel equals \(W\) exactly when the map
\[
V/W\longrightarrow U^r,\qquad v\longmapsto(\bar A_1v,\ldots,\bar A_rv)
\]
is injective. Distinct flags are distinguished by the original tuple's combined image and common kernel, so they cannot be double-counted. There are \({d\brack a}_q{d-a\brack c}_q\) flags of the required type.

**2. Count simultaneous injectivity and spanning.** Fix \(T\) of dimension \(c\) and \(U\) of dimension \(a\), and let \(E_r(a,c;q)\) count \(r\) maps \(T\to U\) whose combined map to \(U^r\) is injective and whose images collectively span \(U\). For a fixed \(i\)-dimensional subspace \(I\subseteq U\), the number of tuples with all images contained in \(I\) and with zero common kernel is the number of injections \(T\to I^r\), namely
\[
\prod_{j=0}^{c-1}(q^{ri}-q^j).
\]
Möbius inversion on the finite lattice of subspaces of \(U\), whose interval Möbius function in codimension \(h\) equals \((-1)^h q^{\binom h2}\), yields
\[
E_r(a,c;q)=\sum_{i=0}^{a}(-1)^{a-i}q^{\binom{a-i}{2}}{a\brack i}_q\prod_{j=0}^{c-1}(q^{ri}-q^j).
\]
Multiplication by the flag number proves the announced exact count. A second independent inversion over subspaces of \(T\) gives the useful equivalent expression
\[
E_r(a,c;q)=\sum_{i=0}^a\sum_{j=0}^c(-1)^{a-i+c-j}
q^{\binom{a-i}{2}+\binom{c-j}{2}+rij}{a\brack i}_q{c\brack j}_q.
\]
This double sum is used in the accompanying exhaustive checker, independently of the single-inversion formula.

**3. Precise support.** If both ranks vanish, all maps vanish. If exactly one of \(a,c\) is zero, no simultaneously spanning and injective tuple exists. For positive ranks, injectivity of \(T\to U^r\) requires \(c\leq ra\), and spanning of the images requires \(a\leq rc\). These plus \(a+c\leq d\) are necessary. They are sufficient: if \(a\geq c\), assign each of the \(a\) target basis vectors to one of the \(c\) source basis vectors so that every source vector is used at most \(r\) times and at least once. Place the corresponding matrix unit in a distinct generator for each fixed source vector. Then every target basis vector belongs to the combined image and the aggregate map is injective. If \(c>a\), assign each source basis vector to a target basis vector with at most \(r\) assignments per target, and use distinct generators for assignments to a fixed target. Again the two rank conditions hold. This works over every field, including \(\mathbb F_2\).

**4. Geometry.** The set of pairs \(U\subseteq W\) is the smooth geometrically irreducible flag variety \(\mathrm{Fl}(a,d-c;V)\), of dimension \(a(d-a)+c(d-a-c)\). Over it, tuples of maps \((V/W)^r\to U\) constitute a vector bundle of rank \(rac\). The combined injectivity and spanning conditions are nonvanishing maximal-minor conditions, hence define an open subbundle. For the feasible ranks the explicit construction above proves this open is nonempty over every field. Locally on the flag variety it is the product with a fixed nonempty open subset of affine \(rac\)-space. It is therefore smooth and geometrically irreducible. The aggregate image and common kernel are recovered regularly on each fixed-rank locus, so the construction identifies the reduced exact-rank representation locus with that open bundle. Its dimension is the sum of the displayed flag dimension and \(rac\). No assertion is made about the original possibly nonreduced representation scheme.

## Verification

The self-contained program `verify.py` uses the double Möbius expression to compute the predicted bivariate count, and separately enumerates all tuples of matrices whose ordered products vanish. It calculates the rank of horizontal block concatenation to recover \(a\), and of vertical concatenation to recover \(c\). Thirteen configurations were exhaustively checked: \((d,r,q)=(1,1,2),(2,1,2),(3,1,2),(4,1,2),(2,2,2),(3,2,2),(2,3,2),(2,2,3),(2,2,4),(3,2,3),(2,3,3),(2,2,5),(3,2,4)\). All agree, including the extension field \(\mathbb F_4\). In particular, for \((d,r,q)=(3,2,2)\), the counts at \((a,c)=(0,0),(1,1),(1,2),(2,1)\) are respectively \(1,63,42,42\). Run `python3 verify.py`; successful output ends in `RADICAL_SQUARE_ZERO_TOP_SOC_CENSUS_OK 13`.

## Relationship to prior work

Bleher, Chinburg and Huisgen-Zimmermann (2014) study the geometry, realizable radical/socle patterns, and irreducible components of representation varieties for radical-square-zero algebras. The flag geometry and qualitative rank constraints here are placed in that established setting; this report's arithmetic assertion is a **joint framed top–socle point-count formula** for the local multiple-loop family, not a new general classification of components. Huang (2021) counts mutually annihilating matrix pairs with a different collection of relations, notably without imposing all self-products zero in its main family; its individual formulas do not give this entire rank-refined multiple-loop distribution. Quiver nilpotent point-count formulas of Bozec, Schiffmann and Vasserot (2017) concern different doubled-quiver/moment-map conditions, and Drozd's later categorical treatment does not state this distribution. These comparisons are based on the specific accessible full texts; absence of a search result alone is not proof of priority.

## Limitations

This counts framed representations, not simultaneous-conjugacy orbits or module isomorphism classes, and only algebras with one vertex and square-zero radical. The reduced geometric statement does not determine embedded or nilpotent scheme structure, or all irreducible components of the full representation variety. Finite-field tests are corroboration, not an infinite-family proof. Historical priority of the explicit arithmetic formula remains to be independently checked in specialized quiver-counting literature; independent scientific audit has not been performed.

## References

1. F. M. Bleher, T. Chinburg and B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045v1 (first public 2014-07-11).
2. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566v1 (2021).
3. T. Bozec, O. Schiffmann and E. Vasserot, *On the number of points of nilpotent quiver varieties over finite fields*, arXiv:1701.01797 (2017).
4. Yu. A. Drozd, *On representations of algebras with radical square zero*, arXiv:2602.14171 (2026).
