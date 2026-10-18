# Minimum dual words of punctured binary quadratic projective square-free codes

## Finding

Let \(m\ge 2\), put \(v=m+1\), and let \(\widetilde C_m\) be the binary projective square-free degree-two evaluation code after puncturing all its zero coordinates. Its generator matrix \(G\) has rows indexed by the edges \(e\in\binom{[v]}{2}\) and columns indexed by the subsets \(S\subseteq[v]\) with \(|S|\ge2\), where
\[
G_{e,S}=\begin{cases}1,&e\subseteq S,\\0,&\text{otherwise}.\end{cases}
\]
Then the dual code has minimum Hamming distance exactly four:
\[
\boxed{d(\widetilde C_m^\perp)=4.}
\]
Every weight-four word in the binary dual has one of precisely two disjoint support forms:

1. **Triangle and its edges:** for a three-element set \(T=\{a,b,c\}\subseteq[v]\), take the columns indexed by \(\{a,b\},\{a,c\},\{b,c\},T\).
2. **Tetrahedral faces:** for a four-element set \(U\subseteq[v]\), take the columns indexed by the four three-element subsets of \(U\).

There are no other dual words of minimum weight, so the number is
\[
\boxed{A_4(\widetilde C_m^\perp)=\binom{v}{3}+\binom{v}{4}=\binom{m+2}{4}.}
\]

## Definitions and scope

The projective square-free evaluation code \(C_2^{\mathbb P,S}(m)\) is formed by evaluating all homogeneous degree-two square-free monomials at binary projective points. Every projective point of \(\mathbb P^m(\mathbb F_2)\) has a unique nonzero binary representative, equivalently a nonempty subset \(S\subseteq[m+1]\). The monomial \(X_aX_b\) evaluates to one precisely when \(\{a,b\}\subseteq S\). The \(m+1\) points corresponding to singletons therefore give zero columns and are punctured. The punctured length is \(2^{m+1}-m-2\); the pair-indexed columns form an identity submatrix, so its rank is \(\binom{m+1}{2}\).

A dual word is a linear dependence among distinct columns of \(G\) over \(\mathbb F_2\); because the field is binary, any chosen support specifies exactly one nonzero word. No unpunctured dual-distance assertion is made: retaining a zero column would instead create a weight-one dual word. The result covers all integers \(m\ge2\), and no assertion is made about higher-weight dual words or nonbinary parameters.

## Proof

**Clique-column representation and distances one and two.** The column \(c_S\) indexed by \(S\) is the edge-incidence vector of the complete graph induced on \(S\). Every retained column is nonzero because \(|S|\ge2\). Distinct subsets \(S,T\) of size at least two yield distinct sets of pairs: their complete collections of two-subsets recover \(S\) and \(T\). Hence there are neither zero columns nor two equal columns. In particular, the dual has no nonzero word of weight one or two.

**Orthogonal membership-pattern criterion.** Suppose the distinct columns \(c_{S_1},\ldots,c_{S_t}\), for \(t=3\) or \(t=4\), sum to zero. At each vertex \(x\in[v]\), set
\[
p_x=(\mathbf1_{x\in S_1},\ldots,\mathbf1_{x\in S_t})\in\mathbb F_2^t.
\]
The row indexed by the edge \(\{x,y\}\) in \(\sum_i c_{S_i}\) equals the dot product \(p_x\cdot p_y\). Thus the dependence is equivalent to
\[
p_x\cdot p_y=0\quad\text{for all distinct }x,y\in[v].\tag{1}
\]
We can exclude membership-pattern weights one and two. If \(p_x\) has a single one in position \(i\), condition (1) forces every other vertex's pattern to have zero in position \(i\); then \(S_i=\{x\}\), contradicting \(|S_i|\ge2\). If \(p_x\) has weight two, with support \(\{i,j\}\), condition (1) forces \(p_y(i)=p_y(j)\) for every \(y\ne x\), and this equality also holds for \(y=x\). Hence \(S_i=S_j\), contradicting distinct columns.

**No three-column dependence.** For \(t=3\), any nonzero pattern left after excluding weights one and two must be \((1,1,1)\). Two distinct vertices cannot both carry that pattern because their dot product would equal one, contrary to (1). Thus each \(S_i\) could contain at most one vertex, impossible. No three selected distinct columns are dependent.

**Complete four-column classification.** For \(t=4\), a weight-four pattern at one vertex forces all other patterns to have even weight. Since weights one and two are excluded, every other nonzero pattern would have weight four. The four chosen sets would then be identical, a contradiction. Therefore all nonzero vertex patterns have weight exactly three. There are exactly four such patterns, each obtained by placing its sole zero in one of the four positions. Each can occur at most once: two identical weight-three patterns have dot product three, which is one modulo two, contradicting (1). Let \(k\) be the number of distinct nonzero patterns that occur, so \(k\le4\).

If \(k\le2\), the membership columns cannot be four distinct subsets of cardinality at least two: with two different weight-three patterns, the four subset-memberships consist of two patterns with at least one singleton, and with only one pattern each membership set has at most one vertex. Hence \(k=3\) or \(k=4\). With exactly three patterns, the four subsets \(S_i\) are the three two-subsets of their three supporting vertices and the full three-set. This is the triangle-with-edges family. With all four patterns, each \(S_i\) contains every supporting vertex except the one whose pattern has its zero in position \(i\); the four subsets are exactly the four three-faces of a four-set. This is the tetrahedral-face family. Vertices with zero pattern occur in none of the selected sets and do not create any further configurations.

Conversely, the four clique columns of each listed family sum to zero: in the triangle family, every edge belongs once to its own two-element column and once to the triangle column; in the tetrahedral family, every edge is contained in exactly two of the four three-element faces. These are valid dual words of weight four. The prior exclusions establish that four is the minimum weight, and the necessity argument establishes that all minimum words have these forms. Choosing their underlying three- or four-element vertex sets counts their distinct supports without overlap, giving \(\binom{v}{3}+\binom{v}{4}=\binom{v+1}{4}\), as asserted.

## Independent finite corroboration

Reconstructing the columns directly from the displayed definition, independent exact finite enumeration checked all column subsets of sizes one, two, three, and four for \(v=3,4,5,6\). No dependencies of size below four were found, and every size-four dependency belongs to one of the two described families. The respective counts were \(1,5,15,35\), matching \(\binom{v+1}{4}\). The repository also includes `artifacts/verify.py` as a separate finite check. These enumerations do not prove the unbounded claim; the proof above handles every \(m\ge2\).

## Relationship to existing results and limitations

Carvalho, López, and San-José introduced the projective square-free evaluation-code family and identified the zero-column phenomenon in their Remark 5.2; their generalized Hamming-weight results concern the primal evaluation codes. The present statement is a classification of shortest dependencies among the punctured binary degree-two generator columns. The earlier projective high-degree and ternary torus specializations do not imply this circuit classification. Patanker and Singh's toric hypersimplex and affine square-free weight-hierarchy work addresses different evaluation settings. Relevant publications and targeted searches did not reveal the exact binary dual classification, but an unindexed equivalent theorem in clique-incidence or binary matroid language remains a genuine originality risk.

The classification is specific to binary projective quadratic square-free evaluation with its zero coordinates removed. It does not determine generalized dual weights, higher-weight dual words, or behavior for \(q>2\) or \(d>2\). Neither a finite check nor absence of a search result is offered as evidence of infinite correctness or absolute priority.

## References

1. C. Carvalho, H. H. López, and R. San-José, *Cartesian square-free codes*, arXiv:2511.08304 (2025); *Boletín de la Sociedad Matemática Mexicana* 32 (2026), Article 125, DOI: 10.1007/s40590-026-00963-5. See §5, in particular Remark 5.2.
2. N. Patanker and S. K. Singh, *Generalized Hamming weights of toric codes over hypersimplices and squarefree affine evaluation codes*, *Advances in Mathematics of Communications* 17 (2023), 626–643, DOI: 10.3934/amc.2021013.
