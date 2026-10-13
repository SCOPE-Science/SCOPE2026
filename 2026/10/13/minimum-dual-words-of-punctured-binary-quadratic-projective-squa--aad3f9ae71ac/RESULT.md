# Minimum dual words of punctured binary quadratic projective square-free codes
## Finding

For every integer \(m\ge 2\), let \(\widetilde C_m\) be the binary projective square-free code \(C_2^{\mathbb P},S}(m)\) after puncturing its zero coordinates.  Its coordinates are indexed by subsets \(S\subseteq[m+1]\) with \(|S|\ge2\), and a generator matrix has rows indexed by pairs \(e\in\binom{[m+1]}2\), with entry \(1\) exactly when \(e\subseteq S\).  Then \(d(\widetilde C_m^\perp)=4\).  Moreover every weight-four dual word is exactly one of two forms: (I) for a three-set \(T=\{a,b,c\}\), the support consists of the three pair coordinates \(\{a,b\},\{a,c\},\{b,c\}\) together with \(T\); or (II) for a four-set \(U\), the support consists of its four three-subsets.  Hence \(A_4(\widetilde C_m^\perp)=\binom{m+1}{3}+\binom{m+1}{4}=\binom{m+2}{4}\).

## Assumptions and scope

Work over \(\mathbb F_2\).  Carvalho, López, and San-José define the projective square-free code \(C_d^{\mathbb P},S}(m)\) by evaluating homogeneous square-free monomials of degree \(d\) on \(\mathbb P^m(\mathbb F_q)\).  For \(d=2\) and \(q=2\), every projective point is represented by a unique nonzero binary vector, hence by a nonempty subset of \([m+1]\).  Their Remark 5.2 observes that points of Hamming weight at most \(1\) give zero columns.  The code \(\widetilde C_m\) here is obtained by puncturing precisely those \(m+1\) zero coordinates, so its length is
\[
2^{m+1}-m-2.
\]
The claim concerns every integer \(m\ge2\), not merely the finite instances used in verification.

## Proof

Put \(v=m+1\).  Index the generator rows by the edges \(e\ininom{[v]}2\), and the retained columns by subsets \(S\subseteq[v]\) with \(|S|\ge2\).  Evaluating the monomial belonging to \(e\) at the binary point belonging to \(S\) gives \(1\) exactly when \(e\subseteq S\).  Thus the column \(c_S\) is the edge-incidence vector of the clique on \(S\).  In particular, the columns indexed by two-sets are the standard basis vectors, so the generator has full row rank.

Every retained column is nonzero.  If \(S
e T\), choose a pair contained in one of them but not the other: if both have size at least two and no such pair existed, their collections of two-subsets would coincide and hence \(S=T\).  Therefore no two retained columns are equal.  Consequently \(\widetilde C_m^\perp\) has no word of weight \(1\) or \(2\).

Consider a putative dependence among distinct columns \(c_{S_1},\ldots,c_{S_t}\), with \(t\in\{3,4\}\).  For each vertex \(x\in[v]\), define its membership pattern
\[
p_x=(1_{x\in S_1},\ldots,1_{x\in S_t})\in\mathbb F_2^t.
\]
The coordinate indexed by an edge \(\{x,y\}\) in \(c_{S_1}+\cdots+c_{S_t}\) is exactly \(p_x\cdot p_y\).  Hence a dependence is equivalent to
\[
p_x\cdot p_y=0\qquad	ext{for all distinct }x,y.
\]

A pattern of Hamming weight \(1\) is impossible: its unique occupied set would need another vertex because every \(S_i\) has size at least two, but that second vertex would have odd inner product with it.  A pattern of weight \(2\), say with ones in positions \(i,j\), is also impossible: orthogonality forces every other pattern to have equal \(i\)- and \(j\)-coordinates, and the pattern itself does too, so \(S_i=S_j\), contrary to distinctness.

For \(t=3\), a weight-three pattern forces every other nonzero pattern to have even weight.  Weight two is already impossible, and a second weight-three pattern cannot occur because its self-inner-product is odd.  Thus the only possible nonzero pattern would occur at a single vertex, making all three sets have size one.  Hence no three-column dependence exists.

Now let \(t=4\).  A weight-four pattern forces every other pattern to have even weight.  Weight two is impossible, so all nonzero patterns would then have weight four, which would make the four sets identical.  Thus every nonzero membership pattern has weight exactly \(3\).  Two equal weight-three patterns cannot occur at distinct vertices because their inner product is \(1\).  There are only four such patterns, namely the vectors with one zero coordinate.

If exactly three of these four patterns occur, the four sets are, after relabeling, the three two-subsets of a three-set together with that three-set.  This is type I.  If all four patterns occur, the four sets are exactly the four three-subsets of a four-set, which is type II.  One or two occurring patterns cannot give four distinct sets all of size at least two.  This proves that every four-column dependence has one of the two stated forms.

Conversely, each type-I support is dependent because every edge of its three-set occurs exactly twice among its four clique vectors.  Each type-II support is dependent because every edge of its four-set lies in exactly two of the four three-subsets.  Hence the dual minimum distance is \(4\), and the two disjoint support families are counted by
\[
inom{v}3+inom{v}4=inom{v+1}4=inom{m+2}4.
\]

## Verification

`artifacts/verify.py` constructs the exact binary generator columns from the definition.  For \(3\le v\le6\), it checks that all retained columns are nonzero and distinct, exhausts every triple of columns to rule out weight-three dual words, exhausts every four-set of columns, and confirms that the dependent four-sets are exactly the two families in the theorem.  The resulting counts are \(1,5,15,35\), agreeing with \(inom{v+1}4\).  This finite computation is a stress test only; the all-\(m\) conclusion follows from the membership-pattern proof above.

## Relationship to prior work

Carvalho, López, and San-José introduce Cartesian square-free codes, define the projective family, identify the zero columns for projective degree greater than one, and derive generalized Hamming-weight formulas.  Their article does not state the minimum distance of the punctured degree-two binary projective dual or classify its minimum dual words.

A prior finding from the same source determined a complete generalized-weight hierarchy in the opposite high-degree regime \(d=m\) projectively, and another prior finding classified minimizers in one ternary torus example.  Neither statement implies the present degree-two binary dual circuit classification: the present invariant is the complete family of minimal column dependencies after puncturing, and its proof uses the clique-incidence representation specific to \(q=2,d=2\).

Earlier work of Patanker and Singh concerns generalized Hamming weights of toric codes over hypersimplices and square-free affine evaluation codes.  It does not state this projective binary dual minimum-word classification.  Focused searches under dual-distance, minimum-dual-word, clique-incidence, projective-square-free, and equivalent circuit terminology found no covering statement.  The remaining originality risk is that the same binary matroid circuit classification could exist under unrelated incidence-matrix terminology in an unindexed source.

## Limitations

The theorem is specific to the binary, homogeneous projective degree-two family after deleting the source's zero columns.  It does not classify higher-weight dual words, higher generalized dual weights, or analogous minimum dual words for \(q>2\) or \(d>2\).  The literature search cannot exclude an unindexed equivalent formulation in matroid or incidence-geometry language.

## References

1. Cícero Carvalho, Hiram H. López, and Rodrigo San-José, *Cartesian square-free codes*, arXiv:2511.08304v1, first public 2025-11-11; later published in *Boletín de la Sociedad Matemática Mexicana* 32 (2026), Article 125, DOI 10.1007/s40590-026-00963-5.
2. Nupur Patanker and Sanjay Kumar Singh, *Generalized Hamming weights of toric codes over hypersimplices and squarefree affine evaluation codes*, *Advances in Mathematics of Communications* 17 (2023), 626--643, DOI 10.3934/amc.2021013.
