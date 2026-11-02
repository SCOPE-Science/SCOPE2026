# Zero-product loci of star incidence algebras: components and finite-field enumeration

## Finding

**Theorem.** Let \(k\) be an arbitrary field and \(r\ge1\). Let \(A_r(k)\) be the unital incidence algebra of the poset with one least element and \(r\) incomparable maximal elements. Concretely it is the algebra of \((r+1)\)-by-\((r+1)\) matrices whose only potentially nonzero entries are the diagonal entries and the entries in the first row. Its dimension is \(2r+1\). For \(a,b\in A_r(k)\), write their diagonal coordinates as \(a_0,a_1,\ldots,a_r\) and \(b_0,b_1,\ldots,b_r\), and their first-row off-diagonal coordinates as \(\alpha_i,\beta_i\) for \(1\le i\le r\).

The **reduced zero-product locus** \(\mathcal Z_r=\{(a,b)\in A_r(k)^2:ab=0\}_{\mathrm{red}}\) has exactly \(2^{r+1}\) geometrically irreducible components, all defined over \(k\). They form two families indexed by subsets \(S,T\subseteq\{1,\ldots,r\}\):

\[
\begin{aligned}
X_S=\{(a,b):\;&b_0=0;\quad a_i=0,\ a_0\beta_i+\alpha_i b_i=0\ (i\in S);\\
&b_i=\beta_i=0\ (i\notin S)\},\\
Z_T=\{(a,b):\;&a_0=0;\quad a_i=\alpha_i=0\ (i\in T);\\
&b_i=0\ (i\notin T)\}.
\end{aligned}
\]

Their dimensions are

\[
\dim X_S=2r+1,\qquad \dim Z_T=3r+1-|T|.
\]

In particular, there is one top-dimensional component of dimension \(3r+1\), while exactly \(2^r+1\) components have the smallest dimension \(2r+1\). Every intermediate dimension \(3r+1-j\), for \(0\le j<r\), occurs with multiplicity \(\binom rj\). Consequently the reduced zero-product locus is non-equidimensional for every \(r\ge1\).

Writing \(\mathbb L=[\mathbb A^1_k]\), its class in the Grothendieck ring of varieties over \(k\) is

\[
[\mathcal Z_r]=(\mathbb L-1)[\mathbb L(2\mathbb L-1)]^r
+\mathbb L[\mathbb L(\mathbb L^2+\mathbb L-1)]^r.
\]

Over every finite field \(k=\mathbb F_q\), including all extension fields and characteristics, the **exact number of ordered zero-product pairs** is therefore

\[
\boxed{\#\{(a,b)\in A_r(\mathbb F_q)^2:ab=0\}
=(q-1)q^r(2q-1)^r+q^{r+1}(q^2+q-1)^r.}
\]

Equivalently, if \(P_r(u)\) denotes the displayed polynomial with \(q\) replaced by \(u\), then the local Hasse–Weil zeta function of this reduced locus over \(\mathbb F_q\) is \(\exp(\sum_{m\ge1}P_r(q^m)t^m/m)\). In particular it is rational; if \(P_r(u)=\sum_j c_j u^j\), it equals \(\prod_j(1-q^jt)^{-c_j}\).

## Assumptions and scope

There are no restrictions on the characteristic of \(k\). The poset consists of a single minimal element with \(r\) incomparable elements above it; equivalently its Hasse quiver is an outward-pointing star. All products are ordinary associative multiplication, and **ordered** pairs satisfying \(ab=0\) are counted; the reverse condition \(ba=0\) is not imposed. Assertions about components and dimensions concern the underlying reduced affine variety over an algebraic closure. No claim about nilpotent or embedded structure of the scheme defined by the multiplication equations is made.

## Proof

**1. Matrix product.** Direct multiplication of the given sparse matrices shows that \(ab=0\) is equivalent to

\[
a_0b_0=0,\qquad a_i b_i=0,\qquad a_0\beta_i+\alpha_i b_i=0\quad(1\le i\le r).
\tag{1}
\]

These identities are valid over every field; in characteristic two the same plus sign is used.

**2. The closed slice \(a_0=0\).** Equation (1) becomes \(b_i a_i=b_i\alpha_i=0\) independently for each \(i\), with \(b_0\) and all \(\beta_i\) free. For each \(i\) this is the union of the linear spaces \(b_i=0\) and \(a_i=\alpha_i=0\). Distributing products of these unions gives precisely \(\bigcup_{T} Z_T\). Each \(Z_T\) is a linear affine space. For an index in \(T\), the two free coordinates are \(b_i,\beta_i\); for an index outside \(T\), the three free coordinates are \(a_i,\alpha_i,\beta_i\). Together with \(b_0\), this yields \(\dim Z_T=1+2|T|+3(r-|T|)=3r+1-|T|\).

**3. The open slice \(a_0\ne0\).** Equation (1) forces \(b_0=0\). For each \(i\), either \(a_i=0\) or \(b_i=0\). When \(b_i=0\), equation (1) further forces \(\beta_i=0\). Thus this open slice decomposes into \(2^r\) irreducible closed-in-the-open subsets, one for every \(S\), with \(a_i=0\) for \(i\in S\) and \(b_i=\beta_i=0\) for \(i\notin S\). Each is isomorphic to \(\mathbb G_m\times\mathbb A^{2r}\): for \(i\in S\), \(b_i,\alpha_i\) are free and \(\beta_i=-\alpha_i b_i/a_0\); for \(i\notin S\), \(a_i,\alpha_i\) are free.

**4. Their closures.** The displayed \(X_S\) are indeed the closures of these open pieces, not larger unions. To verify this critical point, fix \(S\) of size \(s\). After removing the irrelevant free coordinates, the defining equations become \(xw_i+u_iv_i=0\) for \(1\le i\le s\), where \(x=a_0\). In the affine space of dimension \(1+3s\), the open part \(x\ne0\) is irreducible of dimension \(1+2s\), while the closed fiber \(x=0\) is \(\prod_i\{u_iv_i=0\}\times\mathbb A^s\), of dimension \(2s\). Hence the whole zero set has dimension \(1+2s\), and the ideal of its \(s\) equations has height \(s\). Since a polynomial ring is Cohen–Macaulay, an ideal of height \(s\) generated by \(s\) equations is a complete intersection and is unmixed: all its irreducible components have dimension \(1+2s\). No component can therefore lie inside the smaller-dimensional fiber \(x=0\). The dense open \(x\ne0\) is irreducible, proving the whole zero set is irreducible and is precisely the closure of that open part. Restoring the \(2(r-s)\) free coordinates proves \(X_S\) geometrically irreducible of dimension \(2r+1\).

**5. No redundancy.** Two different \(X_S\) are not contained in one another, as witnessed on \(a_0\ne0\) by choosing \(b_i\ne0\) for \(i\in S\) and \(a_i\ne0\) for \(i\notin S\). Similarly, on the open set \(b_0\ne0\), different \(Z_T\) have distinct generic choices \(b_i\ne0\) for \(i\in T\) and \(a_i\ne0\) for \(i\notin T\). No \(X_S\) contains any \(Z_T\), because \(b_0=0\) throughout \(X_S\) but \(b_0\) is free on \(Z_T\). No \(Z_T\) contains any \(X_S\), because \(a_0=0\) throughout \(Z_T\) but not throughout \(X_S\). Since the two slices exhaust (1), these are exactly all geometrically irreducible components.

**6. Arithmetic and motivic counts.** For \(a_0\ne0\), there are \(q-1\) choices of \(a_0\), \(b_0=0\), and independently for each index either \(b_i=0\), contributing \(q^2\) choices for \((a_i,\alpha_i,\beta_i)\), or \(b_i\ne0\), contributing \(q(q-1)\) choices. Thus this slice has \((q-1)[q(2q-1)]^r\) points. For \(a_0=0\), there are \(q\) choices of \(b_0\), and each index contributes \(q^3\) choices when \(b_i=0\), or \(q(q-1)\) when \(b_i\ne0\). Thus this slice has \(q[q(q^2+q-1)]^r\) points. Adding them proves the formula. The same disjoint constructible stratifications, replacing point counts by \([\mathbb A^1_k]=\mathbb L\) and \([\mathbb G_{m,k}]=\mathbb L-1\), prove the Grothendieck-class identity. Replacing \(q\) by \(q^m\) gives all extension-field counts, and the standard logarithmic expansion gives the zeta identity.

## Verification

The standalone script `verify_star_zero_pairs.py` performs a finite exhaustive check using direct dense matrix products and independently tests the component equations. Run `python3 verify_star_zero_pairs.py`. It covers \((q,r)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(5,1),(7,1)\), with a direct polynomial-basis implementation of \(\mathbb F_4\). It verifies exact point counts, coverage by the proposed components, and witnesses showing all proposed components are distinct on the indicated dense opens. Expected final marker: `STAR_INCIDENCE_ZERO_PRODUCT_GEOMETRY_OK 9`. Finite checks corroborate, but do not replace, the geometric complete-intersection argument.

For example, \(r=2\) gives eight components: four of dimension five, one of dimension seven, two of dimension six, and one further component of dimension five. Over \(\mathbb F_2\) there are exactly \(236\) ordered zero-product pairs, and over \(\mathbb F_3\) there are \(3717\).

## Relationship to prior work

The star incidence algebra is a radical-square-zero path algebra of a star quiver, a standard object in the representation-theory literature. A separately available full-upper-triangular-algebra result enumerates annihilators and ordered zero-product pairs in \(T_n(\mathbb F_q)\), but it counts unrestricted triangular factors and gives only top-dimensional component information; restricting both factors to the sparse star subalgebra is not an instance of its stated formula or geometric classification. Lanzilotta, Marcos and Mata study homological invariants of such algebras; they do not state this pair-multiplication-locus census. Brice and Huang study when bilinear maps vanishing on zero products factor through multiplication; that zero-product-determined property does not itself enumerate ordered zero-product pairs or classify the geometry of their locus. Schröer classifies components of varieties of pairs of full matrices subject to **both** annihilation equations \(AB=BA=0\) and nilpotency constraints, a different ambient problem that does not directly imply the stated star-incidence one-sided calculation.

A closely relevant paper on zero-product-determined triangular algebras is known from its accessible abstract; its full text was not inspected, so an unrecognized enumeration there remains a priority risk. A search without a matching result is not proof of novelty. The assessed contribution is the joint exact component classification, motivic class, and finite-field enumeration for the specified star-incidence family—not the background constructions or general geometric tools.

## Limitations

The theorem does not concern the scheme structure before reduction, arbitrary posets, general orientations of trees, or pairs constrained by both \(ab=0\) and \(ba=0\). Its arithmetic statement is a closed formula, not an enumeration of isomorphism orbits of pairs. The literature comparison is best knowledge, not a certificate of publication priority, and independent validation has not been performed.

## References

1. M. Lanzilotta, E. N. Marcos and G. Mata, *Igusa-Todorov functions for radical square zero algebras*, arXiv:1506.05894v1, publicly submitted 2015-06-19. Primary MSC 16W50, 16E30.
2. D. Brice and H. Huang, *Direct sums of zero product determined algebras*, arXiv:1110.5848, publicly submitted 2011-10-26.
3. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293, publicly submitted 2002-11-19; *Commentarii Mathematici Helvetici* 79 (2004), 396–426.
4. H. Ghahramani, *Zero product determined triangular algebras*, *Linear and Multilinear Algebra* 61 (2013), 741–757, DOI:10.1080/03081087.2012.703193, publicly posted 2012-07-18 (abstract inspected; full text not inspected).
