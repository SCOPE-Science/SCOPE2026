# A Boolean-cube enumeration of binary weight-at-most-two universal cycles

## Finding

For every integer \(k\ge2\), let
\[
\mathcal B_k=\{w\in\{0,1\}^k:\operatorname{wt}(w)\le2\},\qquad
L_k=|\mathcal B_k|=1+k+\binom{k}{2}.
\]
An **oriented universal cycle** for \(\mathcal B_k\) is a circular binary word of length \(L_k\) whose \(L_k\) cyclic length-\(k\) factors are exactly the members of \(\mathcal B_k\), each once. Identify circular rotations, but do not identify reversal or complementation. Then the exact number of universal cycles is
\[
\boxed{U_k=2^{\lfloor(k-1)/2\rfloor}}\qquad(k\ge2).
\]
More strongly, the cycles are canonically in bijection with the \(\lfloor(k-1)/2\rfloor\) independent binary choices described below. In particular the count for \(k=2,3,4,5,6,7,8,9\) is \(1,2,2,4,4,8,8,16\). Every universal cycle contains exactly \(k\) ones.

## Assumptions and scope

All symbols are \(0\) or \(1\). Length-\(k\) factors are **indexed** at each position before quotienting the circular word by rotation. Overlaps may wrap around the period. Word weight means the ordinary number of ones, not an algebraic sum. The family contains all length-\(k\) words with zero, one, or two ones, including the all-zero word. This is **not** a statement about exact weight two alone, necklaces of source factors, or unrestricted binary de Bruijn cycles. The theorem concerns the entire family of integers \(k\ge2\), with no asymptotic assumption.

## Proof

Write \(m=k-1\). Construct a directed labeled overlap graph \(G_k\). Its vertices are all length-\(m\) binary words of weight at most two. For each \(w\in\mathcal B_k\), insert the directed edge from its length-\(m\) prefix to its length-\(m\) suffix, retaining the edge's length-\(k\) word as a unique label. Cyclic universal cycles correspond bijectively to directed Euler circuits, modulo cyclic reindexing of edges. The graph is balanced: a vertex of weight at most one has two incoming and two outgoing edges; a vertex of weight two has one incoming and one outgoing edge. All vertices reach the root \(r=0^m\) by repeated appending of zero, and every vertex is reachable from \(r\) by appending its bits. Thus the graph is strongly connected and Eulerian.

The edge labeled \(0^k\) is unique and is a loop at \(r\), so every cyclic Euler circuit has a unique rotation whose **first edge** is \(0^k\). The fixed-first-edge version of the BEST correspondence counts these circuits by rooted in-arborescences: for a rooted Euler tour, the final outgoing edge from each nonroot vertex is a tree edge toward the root, and the remaining outgoing edges may be ordered arbitrarily. Here every outdegree is one or two; hence each \((d^+(v)-1)!\) factor is one. At the root the starting loop is fixed and its other outgoing edge is consequently last. Therefore
\[
U_k=\tau_r(G_k),
\]
where \(\tau_r\) counts directed spanning in-arborescences to \(r\). This correspondence also proves there is no rotation or starting-edge multiplicity.

In every such tree, each weight-two vertex is forced to select its sole outgoing edge, obtained by appending zero. Following these forced edges eventually removes the **leftmost** one and reaches either a weight-one vertex or the root: the selected edges alone cannot form a directed cycle consisting entirely of weight-two vertices. The only choices are at the \(m\) weight-one vertices, labeled \(s_j\) for \(0\le j<m\), where the single one occupies zero-based position \(j\) from the left.

From \(s_j\), choosing the outgoing edge that appends zero gives the next branching vertex \(s_{j-1}\) if \(j>0\), and \(r\) when \(j=0\). Choosing the edge that appends one, then following forced zero edges through the intermediate weight-two states, gives \(s_{m-1-j}\). This remains true when \(j=0\), where the original one drops immediately and there are no intermediate weight-two states. Thus, after contracting each forced path, the two possible successor choices at index \(j\) are
\[
Z(j)=j-1\quad(0\mapsto r),\qquad O(j)=m-1-j.
\]

Let \(h=\lfloor(m-1)/2\rfloor\). **Necessity:** if any low index \(j\le h\) chooses the \(O\)-edge, the nonempty index interval \(I_j=\{j,j+1,\ldots,m-1-j\}\) is forward-invariant under every possible chosen successor: for indices greater than \(j\), \(Z\) remains in this interval, and \(O\) reflects the interval onto itself; at its lower endpoint the chosen \(O\) also remains inside. Consequently no vertex in \(I_j\) can reach \(r\), a contradiction. Every such low index must choose \(Z\).

**Sufficiency:** if all indices \(j\le h\) choose \(Z\), every chosen edge from a high index \(j>h\) strictly decreases its index: \(Z(j)=j-1<j\) and \(O(j)=m-1-j<j\). Low indices also decrease under their required \(Z\)-choices. Every selected path therefore reaches \(r\) and cannot cycle. Together with the forced weight-two edges these selections form exactly one rooted in-arborescence.

There are \(m-(h+1)=\lfloor m/2\rfloor\) high indices, each with either choice independent. Hence
\[
U_k=2^{\lfloor m/2\rfloor}=2^{\lfloor(k-1)/2\rfloor}.
\]
The choice set \(\{j:h<j<m\}\) itself gives the Boolean-cube parametrization; the standard last-exit traversal reconstructs the unique cycle starting with \(0^k\).

Finally, each one in a circular word contributes to exactly \(k\) cyclic length-\(k\) factors. Summing factor weights over \(\mathcal B_k\) gives \(k+2\binom{k}{2}=k^2\); therefore every universal cycle has exactly \(k^2/k=k\) ones. This identity is also a useful independent verification restriction.

## Verification

Run `python3 verify.py` for exact integer Bareiss matrix-tree cofactors of the **uncontracted** graph for \(2\le k\le11\), an exhaustive enumeration of the contracted singleton choices for \(2\le k\le15\), and independent direct cyclic-word enumeration for \(2\le k\le5\). The program ends with `VERIFY_OK`.

For a second implementation, compile `verify_large.cpp` with a C++17 compiler and run its executable. It independently enumerates all binary circular words of the **necessarily exact total Hamming weight** \(k\), for \(2\le k\le7\), and checks the count modulo rotation; it ends with `VERIFY_LARGE_OK`. These computations are finite checks; the preceding proof establishes the theorem for every \(k\ge2\).

## Relationship to prior work

Sawada, Williams and Wong (2013) establish efficient universal-cycle constructions for **general binary weight ranges** and therefore already settle the existence question for this family; they do not give the number of all circular cycles or a complete inverse-tree classification. Gabrić, Sawada, Williams and Wong's July 24, 2018 manuscript proves successor-rule constructions for bounded-weight words, again establishing specific cycles rather than evaluating all possible cycles. Sawada and Gabrić (2025) develop uniform random generation through general Eulerian-graph arborescences, which provides the general counting principle but does not evaluate the sharp \(\{0,1,2\}\)-weight specialization or its reflection-interval classification. The present contribution is precisely that all-orders exact enumeration and explicit free-choice parametrization; the Eulerian correspondence and BEST theorem are standard ingredients, not new claims.

## Limitations

The formula is limited to binary length-\(k\) windows of weight at most two. Reversal and complementation are not factored out. No analogous closed count for higher weight bounds is asserted. The novelty assessment is based on inspected papers and searches, and cannot rule out an unindexed equivalent formula or reduction. Finite checks are not substitutes for the combinatorial proof; independent external mathematical review has not been performed.

## References

1. J. Sawada, A. Williams, D. Wong, *Universal cycles for weight-range binary strings*, IWOCA 2013. Full text: https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf
2. D. Gabrić, J. Sawada, A. Williams, D. Wong, *A successor rule framework for constructing k-ary de Bruijn sequences and universal cycles*, manuscript dated July 24, 2018; IEEE Transactions on Information Theory 66 (2020), 679–687. Full text: https://socs.uoguelph.ca/~dgabric/papers/kary-successor.pdf
3. J. Sawada, D. Gabrić, *Las Vegas algorithms to generate universal cycles and de Bruijn sequences uniformly at random*, arXiv:2510.16545 (first posted October 18, 2025). Full text: https://arxiv.org/pdf/2510.16545
4. *De Bruijn Sequence and Universal Cycle Constructions*, reference and random-generation overview: https://debruijnsequence.org/db/random
5. The BEST theorem for directed Euler tours and the directed matrix-tree theorem, standard graph-theoretic results.
