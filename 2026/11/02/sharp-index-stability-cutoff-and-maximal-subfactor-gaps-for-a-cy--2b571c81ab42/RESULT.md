# Sharp index-stability cutoff and maximal-subfactor gaps for a cyclic three-point set

## Finding
Let \(n\ge 5\), let \(G=\mathbb Z/n\mathbb Z\), and let \(A=\{0,1,4\}\subset G\). A **subfactor of \(G\) relative to \(A\)** means an inclusion-maximal subset \(B\subseteq G\) for which the translates \(A+b\), \(b\in B\), are pairwise disjoint. Such subsets are necessarily nonempty. Write the elements of \(B\) in positive cyclic order and let \(g_1,\ldots,g_k\) be their positive successive gaps, with \(k=|B|\) and \(\sum_i g_i=n\). Indices on gaps are cyclic, including when \(k=1\) or \(k=2\).

**Complete gap theorem.** The set \(B\) is a subfactor if and only if all three conditions hold:

1. Each gap belongs to \(\{2,5,6,7,8,9\}\).
2. No gap of length \(2\) has another gap of length \(2\) immediately before or after it.
3. Every gap of length \(7\), \(8\), or \(9\) has gaps of length \(2\) on both sides.

Consequently the subset \(A\) is **index stable** (all its subfactors have the same cardinality) exactly for
\[
\boxed{n\in\{5,6,7,8,9,10,11,13\}.}
\]
It is index unstable for \(n=12\) and for every \(n\ge14\). More strongly, for each \(n\ge14\) there are subfactors with two consecutive cardinalities: if \(n=n_0+5j\), where \(n_0\in\{14,15,16,17,18\}\) and \(j\ge0\), the two cardinalities are \(3+j\) and \(4+j\).

The gap rule determines the **entire subfactor-size distribution**. Let \(W_{n,k}\) be the number of ordered \(k\)-tuples satisfying the three cyclic gap conditions and summing to \(n\). Then the number \(N_{n,k}\) of subfactors of cardinality \(k\) is exactly
\[
\boxed{N_{n,k}=\frac nk W_{n,k}.}
\]
This is a finite, six-symbol enumeration formula for each \(n,k\), not merely a decision criterion.

## Assumptions and scope
The cyclic group \(G\) is additive. The ground set \(A\) has exactly three distinct elements for every \(n\ge5\). The result makes no assertion about other normalized triples \(\{0,1,t\}\), arbitrary subsets, noncyclic groups, or the full classification of three-element index-stable subsets. The integer \(k\) is always positive. Positive cyclic gaps are measured using integer lifts \(b_1<\cdots<b_k<b_1+n\) and \(b_{k+1}=b_1+n\), so \(g_i=b_{i+1}-b_i\).

## Proof
**1. Reformulation.** The difference set of \(A\) is
\[
A-A=\{0,\pm1,\pm3,\pm4\}\pmod n.
\]
The translates indexed by \(B\) are pairwise disjoint if and only if no two distinct elements of \(B\) differ by a nonzero residue represented by \(\pm1,\pm3,\pm4\). Hence \(B\) is independent in the Cayley graph with this difference connection set. It is inclusion-maximal exactly when every element outside \(B\) is within one of those difference steps of an element of \(B\), equivalently \((A-A)+B=G\). These are the independent-dominating sets of the circulant.

**2. Necessary gaps.** In the periodic integer lift of the selected vertices, any successive gap cannot have length \(1\), \(3\), or \(4\), by independence. No gap can have length \(10\) or more: the vertex five steps to the right of its left endpoint is at distances at least \(5\) from both endpoints and at least \(7\) from every selected lift beyond the endpoints (because every other gap is at least \(2\)). It is therefore undominated. Only \(2,5,6,7,8,9\) remain.

Two successive gaps of length \(2\) would yield two selected vertices at distance \(4\), contrary to independence. For a gap of length \(g\in\{7,8,9\}\), the unselected vertex at offset \(2\) from its left endpoint cannot be dominated by either endpoint or by any selected lift to its right. To be dominated it must have a selected lift four steps to its left, which forces the preceding gap to equal \(2\). Applying the symmetric argument to the vertex two steps from the right endpoint forces the following gap to equal \(2\). Thus all three conditions are necessary.

**3. Sufficiency.** Suppose a cyclic gap word meets the three conditions. A pair of successive selected vertices is not separated by \(1,3,4\). A pair of nonsuccessive selected vertices has at least two gaps between it in each direction unless it is also successive in the opposite direction; such a sum is at least \(2+5=7\), because adjacent \(2\)'s are forbidden. Thus no pair of selected vertices differs by a prohibited step, including modulo \(n\).

Interior vertices of a gap of length \(2\), \(5\), or \(6\) are dominated by its endpoints using offsets \(1\), \(3\), and \(4\). For a gap of length \(7\), \(8\), or \(9\), the preceding and following selected vertices lie two steps beyond the endpoints. Together with the two endpoints these dominate every interior vertex: from the left, offsets \(1,2,3,4\) are covered, and from the right, offsets \(1,2,3,4\) are covered; for \(g\le9\) these cover all interior positions. Hence \(B\) is maximal and is a subfactor.

**4. Exact cutoff.** With one selected point the only possible gap lengths are \(5,6\). With two points the admissible cyclic gap words have total lengths \(7,8,9,10,11,12\); for \(7\) through \(11\) these are the only possible cardinalities (a three-gap admissible word has sum at least \(2+5+5=12\)). At \(n=12\), the words \((6,6)\) and \((2,5,5)\) give sizes \(2\) and \(3\). At \(n=13\), an admissible word has exactly three gaps, necessarily a rotation of \((2,5,6)\): one or two gaps cannot sum to \(13\), and a four-gap admissible word has sum at least \(2+5+2+5=14\). Therefore precisely \(5,6,7,8,9,10,11,13\) are stable among \(n\le13\).

For the five base orders \(n=14,15,16,17,18\), respectively, the following paired words are admissible, with three and four gaps:

| \(n\) | Three-gap word | Four-gap word |
|---|---|---|
| 14 | \((2,6,6)\) | \((2,5,2,5)\) |
| 15 | \((5,5,5)\) | \((2,5,2,6)\) |
| 16 | \((5,5,6)\) | \((2,5,2,7)\) |
| 17 | \((5,6,6)\) | \((2,5,2,8)\) |
| 18 | \((6,6,6)\) | \((2,5,2,9)\) |

Each displayed word contains an adjacent pair of gaps both at most \(6\). Inserting a new \(5\)-gap between such a pair increases the sum by \(5\) and the number of gaps by \(1\), without violating either adjacency restriction. The new word still has such a pair, so the operation can be iterated. Thus every order \(n\ge14\) has two admissible words with cardinalities differing by exactly one, proving the sharp cutoff and the asserted consecutive sizes.

**5. Size counts.** The cyclic gap word of a subfactor \(B\) with one distinguished starting selected vertex is an ordered admissible tuple. Conversely, any admissible tuple with any of the \(n\) choices of starting residue determines a subfactor with a distinguished selected vertex. Counting these rooted objects in two ways gives \(nW_{n,k}=kN_{n,k}\), proving the enumeration formula.

## Verification
The standalone script `verify.py` makes two independent exact enumerations for every \(5\le n\le18\): it tests every vertex subset directly for independence and maximality in the difference graph, and it separately enumerates all admissible cyclic gap tuples. Both algorithms return the same number of subfactors of each cardinality in all fourteen orders. It also constructs and tests the two separate witness families for thirty successive \(+5\) extensions of each base order, through \(n=163\). Run with `python verify.py` in an ordinary Python 3 environment. The observed output is `VERIFY_OK`. These finite tests are corroboration; the all-\(n\) theorem follows from the preceding symbolic argument.

## Relationship to prior work
Hooshmand, *Subindices and subfactors of \(\mathbb Z_n\) and \(k\)-index stability of finite groups* (arXiv:2607.08805, first submitted 9 July 2026), develops subindex theory, classifies two-element index stability, and explicitly proposes examining normalized three-element subsets \(\{0,1,t\}\). The present claim is an exact specialization to \(t=4\): the smallest positive \(t\) beyond \(2,3\) for which the distinct difference lengths are not a consecutive interval. For \(t=2\) or \(3\), the difference set is the interval of step sizes \(1\) through \(t\), so cycle-power results already apply; \(t=4\) is the first omitted-step case.

Brown and Hoshino, *Well-covered circulant graphs* (Discrete Mathematics 311 (2011), 244–251, DOI:10.1016/j.disc.2010.11.007), prove the general difference-sequence correspondence and characterize cycle powers, their complements, and cubic circulants. Their general correspondence is used here; their three complete family classifications do not provide this all-order result for the noninterval step set \(\{1,3,4\}\). Their small-order table and general well-covered terminology are acknowledged as partial prior coverage. No unconditional claim of historical priority over all independent-domination literature is made.

## Limitations
The theorem treats exactly one normalized three-point family as \(n\) varies, not all three-subsets. Its six-gap mechanism may be useful for other fixed supports, but no such classification is asserted. An older treatment of the identical step-set circulant under independent-domination terminology could reduce its originality; exact broader historical coverage cannot be excluded merely from unsuccessful searches. The computational tests do not prove the infinite extension.

## References
1. M. H. Hooshmand, *Subindices and subfactors of \(\mathbb Z_n\) and \(k\)-index stability of finite groups*, arXiv:2607.08805v2 (2026), https://arxiv.org/html/2607.08805.
2. J. Brown and R. Hoshino, *Well-covered circulant graphs*, Discrete Mathematics 311 (2011), 244–251, https://doi.org/10.1016/j.disc.2010.11.007; author-accessible copy at https://www.mscs.dal.ca/~hoshino/wellcov.pdf.
