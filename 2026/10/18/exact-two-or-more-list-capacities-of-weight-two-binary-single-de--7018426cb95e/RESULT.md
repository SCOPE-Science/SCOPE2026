# Exact two-or-more-list capacities of weight-two binary single-deletion codes

## Finding
For integers \(n\ge2\) and \(\ell\ge2\), write \(A_{2,\ell}(n)\) for the greatest size of a binary code of blocklength \(n\), every codeword of Hamming weight exactly two, that admits list decoding of capacity \(\ell\) after **one arbitrary deletion**. More precisely, each length-\(n-1\) word must have at most \(\ell\) distinct codeword supersequences in the code. Put \(m=n-1\) and \(d=\min\{\ell-1,m-1\}\). Then
\[
 A_{2,\ell}(n)=m+\left\lfloor\frac{md}{2}\right\rfloor,
\]
except that \(A_{2,2}(3)=2\) rather than \(3\). In particular, the complete two-list curve is \(1,2,4,6,7,9,10,12,\ldots\) for blocklengths \(2,3,4,5,6,7,8,9,\ldots\), and for \(\ell\ge n-1\) all \(\binom n2\) constant-weight-two words may be selected (apart from the stated exception).

## Assumptions and scope
Indices are zero-based. Each weight-two word is identified with its two distinct positions \((i,j)\), \(0\le i<j<n\). A deletion may remove either a zero or a one; repeated outputs from deleting different coordinates of the **same** word count only once. A list capacity bounds the number of distinct codewords consistent with an output, not the number of deletion paths. There are no restrictions on the alphabet beyond binary or on the list capacity beyond \(\ell\ge2\).

## Proof
**Step 1: the necessary capacity bound.** Classify codewords as adjacent ones \((i,i+1)\) and nonadjacent ones \((i,j)\), \(j\ge i+2\). Let their numbers be \(a\) and \(b\), respectively. A word with adjacent ones has precisely one deletion output of weight one; a word with nonadjacent ones has precisely two distinct weight-one deletion outputs. There are exactly \(m=n-1\) possible weight-one output words. Hence \(a+2b\le\ell m\) and \(a\le m\). Consequently
\[
 |C|=a+b\le \left\lfloor\frac{\ell m+a}{2}\right\rfloor\le m+\left\lfloor\frac{(\ell-1)m}{2}\right\rfloor.
\]
Also \(|C|\le\binom n2=m+\binom m2\). These yield \(|C|\le m+\lfloor md/2\rfloor\). For \((n,\ell)=(3,2)\), all three weight-two words \(110,101,011\) delete to \(11\); therefore at most two can be selected.

**Step 2: reduction to a bounded-degree graph.** Select all \(m\) adjacent-one words \(A_i=(i,i+1)\), \(0\le i<m\). Let \(H\) be a simple undirected graph on the index set \(\{0,\ldots,m-1\}\). For every edge \(\{i,j\}\), \(i<j\), add the word \(B_{i,j}=(i,j+1)\). The distinct weight-one deletion outputs of \(B_{i,j}\) have their ones at positions \(i\) and \(j\). Thus output \(i\) has exactly \(1+\deg_H(i)\) selected preimages. If \(\Delta(H)\le\ell-1\), all these outputs obey the list bound.

For a weight-two output with its ones at \(a<b\) in a word of length \(m\), the **complete** list of possible weight-two superwords obtained by inserting a zero consists of
\[
 (a,b),\qquad(a,b+1),\qquad(a+1,b+1).
\]
Consequently every weight-two output has at most three possible preimages in the *entire* weight-two input space. For \(\ell\ge3\), no additional restriction is needed.

For \(\ell=2\), take \(H\) to be a matching with no edge joining two consecutive indices. If a weight-two output has adjacent ones, its three possible preimages comprise the two adjacent-one words \(A_a,A_{a+1}\) and the nonadjacent-one word \(B_{a,a+1}\); the latter is excluded by the condition on \(H\). If a weight-two output has nonadjacent ones, none of its three preimages is an \(A_i\). Its middle candidate \((a,b+1)\), when selected, corresponds to the edge \(\{a,b\}\); the other two correspond to edges meeting it at \(a\) and \(b\), respectively. A matching cannot contain the middle edge together with either of the other two. Thus at most two of the candidates are selected. Every output therefore obeys the two-list requirement.

**Step 3: attaining the edge bound.** If \(\ell\ge3\), there exists a simple graph on \(m\) vertices with maximum degree \(d\) and exactly \(\lfloor md/2\rfloor\) edges. Explicitly, arrange the vertices around a circle and include all edges of circular offsets \(1,\ldots,\lfloor d/2\rfloor\). When \(d\) is odd, add the antipodal perfect matching for even \(m\), or for odd \(m\) a near-perfect matching from the Hamiltonian cycle of offset \((m-1)/2\); these added edges are disjoint from the previous offsets. All degrees are \(d\), except possibly one vertex of degree \(d-1\) in the odd-by-odd case. The cases \(m=1,2\) are included by direct inspection.

If \(\ell=2\) and \(m\ge3\), take the \(\lfloor m/2\rfloor\) matching edges
\[
 \left\{\left\{i,i+\left\lceil\frac m2\right\rceil\right\}:0\le i<\left\lfloor\frac m2\right\rfloor\right\}.
\]
Their endpoints are distinct and differ by at least two. This yields \(m+\lfloor m/2\rfloor\) codewords. At \(m=1\), the sole weight-two word is a valid one-element code. At \((m,\ell)=(2,2)\), the two adjacent-one words are feasible and optimal by Step 1's extra obstruction. All displayed upper bounds are therefore attained, completing the proof.

## Verification
The standalone file `verify.py` constructs witnesses and checks every distinct one-deletion output, for 150 parameter combinations through blocklength \(24\). It also performs a direct exhaustive enumeration of **all** constant-weight-two code subsets at each length \(2\) through \(6\) for each list size from \(2\) through \(n+1\). The output is in `verification_output.txt`. These computations corroborate the constructions and boundary cases; the unrestricted theorem follows from Steps 1–3, not finite extrapolation.

## Relationship to prior work
Lin [1] studies the general \(\ell\)-list \(k\)-deletion channel and gives asymptotic existential bounds for unrestricted binary codes. It does not state an exact all-blocklength formula in the Hamming-weight-two one-deletion slice. Guruswami and Håstad [2] give explicit general two-deletion codes (including two-list constructions), not this one-deletion low-weight extremum. Unique decoding corresponds to \(\ell=1\) and is different: the simple graph degree bound alone is insufficient for one-list decoding. The present theorem covers every list size \(\ell\ge2\) and gives the exact transition to selecting the entire constant-weight-two space.

## Limitations
This theorem is for **exactly one deletion**, **binary constant weight two**, and lists of capacity at least two. It does not determine unrestricted code sizes, rates for positive relative weight, or capacities for two or more deletions. Its finite checks do not certify literature priority, and no independent scientific audit has been performed.

## References
[1] A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650, first submitted September 22, 2026. https://arxiv.org/abs/2609.26650

[2] V. Guruswami and J. Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592 (2020). https://arxiv.org/abs/2007.10592
