# Complete minimal strong-total-cover enumerator of complete bipartite graphs

## Finding

Let \(K_{m,n}\) have fixed labelled partite classes \(A,B\), with \(m,n\ge 2\). A strong total cover is a set of graph elements (vertices and edges) such that each vertex is selected or incident to a selected edge, and each edge is selected or has a selected endpoint. Call a strong total cover *minimal* if deletion of any one of its selected elements destroys the cover. Let \(\mathcal M_{m,n}(z)=\sum_C z^{|C|}\), summed over all inclusionwise minimal strong total covers.

**Complete enumerator.** For every pair of integers \(m,n\ge2\),
\[
\mathcal M_{m,n}(z)=\sum_{a=1}^{m}\sum_{b=1}^{n}\binom ma\binom nb z^{m+n-a-b+ab}+\left[1+\sum_{a=1}^{m}\binom ma(n^a-n)+\sum_{b=1}^{n}\binom nb(m^b-m)\right]z^{m+n}.
\]
This counts actual subsets of the labelled vertex-edge ground set, with no quotient by graph automorphisms.

**Extremal and structural consequences.** The number of minimum covers of size \(m+n-1\) is
\[
 m(2^n-1)+n(2^m-1)-mn.
\]
The exact set of sizes of inclusionwise minimal covers is
\[
\{m+n\}\cup\{m+n-1+uv:0\le u\le m-1,\ 0\le v\le n-1\}.
\]
For \(m,n\ge3\), the unique largest inclusionwise minimal cover is the set of all \(mn\) edges (without vertices). Its size is \(mn\), while the next-largest size is \(mn-\min\{m,n\}+1\). Thus the \(\min\{m,n\}-2\) consecutive cardinalities strictly between these two sizes are absent. In particular, the minimal-cover cardinality spectrum has arbitrarily long gaps on this natural graph family.

## Assumptions and scope

Graphs are finite, simple and complete bipartite; \(m,n\ge2\). The symbol minimal means *inclusionwise minimal*, not minimum cardinality. The generating variable records the total number of selected vertices and selected edges, each counting once. A strong total cover is also a dominating set in the subdivision/incidence graph of the host, under its usual closed-neighborhood definition; the enumerator therefore simultaneously counts inclusionwise minimal dominating sets of the corresponding incidence graphs.

## Proof

Write an arbitrary strong total cover as \(X\cup Y\), with selected vertices \(X\subseteq A\cup B\) and selected edges \(Y\subseteq A\times B\). Put \(U=A\setminus X\), \(W=B\setminus X\), and \(a=|U|\), \(b=|W|\).

**Case 1: both \(a,b\ge1\).** Every edge joining \(U\) to \(W\) has neither endpoint selected, so its own selection is mandatory: \(U\times W\subseteq Y\). Any other selected edge has a selected endpoint, hence is already covered by that endpoint; moreover, both its endpoints are either selected or, if omitted, already covered by mandatory edges (because \(U,W\) are nonempty). Deleting such an extra edge preserves coverage. Minimality therefore forces \(Y=U\times W\). Conversely, for any nonempty \(U,W\), this cover is minimal: a selected edge is indispensable to cover itself (both endpoints unselected), and a selected vertex \(v\in A\setminus U\) is indispensable because its edges to \(W\) otherwise become uncovered; the symmetric argument applies to selected vertices in \(B\setminus W\). Such a cover has \(m+n-a-b+ab\) elements. Independently choosing \(U,W\) gives exactly \(\binom ma\binom nb\) covers, proving the double-sum contribution.

**Case 2: \(U\ne\varnothing\), \(W=\varnothing\).** All vertices of \(B\) are selected. Any edge selected from a selected vertex of \(A\) is redundant. For each omitted vertex \(u\in U\), at least one incident edge must be selected; if at least two are selected then one is redundant because its other endpoint in \(B\) is already selected. Therefore the selected edges of a minimal cover take exactly the form \(Y=\{(u,f(u)):u\in U\}\) for a function \(f:U\to B\). Every selected vertex of \(A\) is essential because it has no incident selected edge. The selected vertices in \(B\) are all essential precisely when \(f\) is nonconstant: if \(f\) is constant with value \(b_0\), then \(b_0\) is redundant; if \(f\) is not constant, for every \(b\in B\) some omitted \(u\in U\) has \(f(u)\ne b\), so removing \(b\) uncovers \((u,b)\). Each selected edge is needed to cover its unique omitted endpoint. Hence exactly \(n^a-n\) choices of \(f\) give minimal covers for a fixed \(U\) with \(a\ge1\), and the total contribution is \(\sum_{a=1}^{m}\binom ma(n^a-n) z^{m+n}\), since \(|X|=m+n-a\) and \(|Y|=a\).

**Case 3: \(U=\varnothing\), \(W\ne\varnothing\).** Interchanging the parts yields \(\sum_{b=1}^{n}\binom nb(m^b-m)z^{m+n}\).

**Case 4: \(U=W=\varnothing\).** All vertices are selected, and minimality forbids every selected edge. This is one minimal cover of size \(m+n\).

The four cases are exhaustive and disjoint; adding their contributions proves the displayed polynomial. The nondegenerate part of the first-case characterization also appears in Claim 13 of Aprile–Ferrarini and is not asserted as an independent novelty here.

For the minimum size, the double-sum exponent is \(m+n-1+(a-1)(b-1)\); the degenerate cases have size \(m+n\). Therefore the minimum \(m+n-1\) arises exactly for \(a=1\) or \(b=1\). Summing the respective choices and subtracting the \(mn\) double-counted \(a=b=1\) cases yields the minimum multiplicity. The full support follows immediately. If \(m,n\ge3\), the maximal product \((a-1)(b-1)=(m-1)(n-1)\) is uniquely attained at \(a=m,b=n\), producing the all-edge cover of size \(mn\). The second-largest product is \(\max\{(m-2)(n-1),(m-1)(n-2)\}\), so the second-largest size is \(mn-\min\{m,n\}+1\); the degenerate size \(m+n\) is no larger than this value. The claimed terminal gap follows.

## Verification

The accompanying Python 3 verifier `verify.py` explicitly enumerates every subset of vertices and edges, checks the covering inequalities independently, rejects covers from which any selected element can be removed, and compares the resulting size distribution with the formula. The enumerated tests cover \((m,n)=(1,1),(1,2),(2,2),(2,3),(2,4),(3,3),(3,4)\); the \(m=1\) tests are auxiliary only, outside the asserted theorem's scope. The last test checks \(2^{19}\) candidate sets. It prints `VERIFY_OK 7 complete_bipartite_cases` if all comparisons succeed. This finite verification is an independent check of small inputs; the preceding case classification proves the general claim.

As a representative noninterval example, \(\mathcal M_{3,3}(z)=33z^5+94z^6+6z^7+z^9\); no inclusionwise minimal cover has size eight.

## Relationship to prior work

Aprile and Ferrarini, *The Strong Total Cover Problem*, arXiv:2610.23312v1 (first posted October 16, 2026), introduce this formulation. Their Proposition 12 proves the minimum size \(m+n-1\) for complete bipartite graphs, and their Claim 13 proves that each inclusionwise minimal nondegenerate cover is canonical. Both findings are explicitly used as prior foundations. The present theorem extends from minimum cardinality and a structural trichotomy to the full coefficient enumeration, complete degenerate-case census, exact number of minimizers and a sharp family of arbitrarily long missing-cardinality intervals. The incidence-graph reformulation is also in their Proposition 3; it is not claimed as new.

The ordinary mixed domination/total covering problem, in which vertices or edges also dominate adjacent elements, has different feasibility rules and cannot be substituted for the strong-total-cover enumerator.

## Limitations

The theorem is restricted to complete bipartite hosts. The above cardinality-gap statement assumes both parts have size at least three. No counting formula for arbitrary graphs, complete multipartite graphs, or arbitrary weighted objectives is proved. The historical-priority search, while involving the initiating primary full text, alternative terminology, and mathematical-record queries, is not a guarantee of global novelty. No independent mathematical audit has been performed.

## References

1. M. Aprile and L. Ferrarini, *The Strong Total Cover Problem*, arXiv:2610.23312v1, October 16, 2026, especially Proposition 3, Proposition 12 and Claim 13. https://arxiv.org/abs/2610.23312
2. E. Castelo, O. Defrain and G. C. M. Gomes, *Enumerating minimal dominating sets and variants in chordal bipartite graphs*, 2025 preprint. Related general enumeration setting, not known to provide the present exact coefficient formula.
