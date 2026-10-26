# Three-distance seating matchings: a complete cyclic classification

## Finding
Let \(n\ge 3\) be an integer. On the cyclically ordered vertex set \(\mathbb Z/(2n)\mathbb Z\), give each unordered pair \(\{u,v\}\) its circular length
\[
\ell(u,v)=\min\bigl(|u-v|,2n-|u-v|\bigr),
\]
where representatives are taken in \(\{0,1,\ldots,2n-1\}\). For nonnegative integers \(a,b,c\) with \(a+b+c=n\), write \(L(a,b,c)\) for the multiset containing \(a\) copies of length \(1\), \(b\) copies of length \(2\), and \(c\) copies of length \(3\).

**Theorem (complete three-distance classification).** A perfect matching of these \(2n\) vertices with length multiset \(L(a,b,c)\) exists if and only if
\[
 b\equiv 0\pmod 2
 \quad\text{and}\quad
 \neg\bigl(3\mid n,\ a=1,\ b=0,\ c=n-1\bigr).
\]
In particular, whenever \(a,b,c\) are all positive, the sole condition is that \(b\) be even. For every odd prime \(p\ge5\), the parity condition alone is sufficient for every prescribed list of \(p\) circular lengths drawn from \(\{1,2,3\}\). Thus the three-shortest-distance instance of the prime-order conjecture in [1] holds, while the stronger all-order statement detects a genuine modular obstruction at composite orders divisible by three.

The theorem is constructive: all but one class of feasible instances have perfect matchings formed by concatenating six fixed local tiles, and the remaining class is matched along a step-three Hamiltonian cycle.

## Assumptions and scope
The graph is the complete graph on \(2n\) labeled, cyclically ordered seats, not the path or cycle graph alone. A requested length is the shorter cyclic distance. A matching consists of \(n\) disjoint unordered edges covering every seat. The restrictions \(n\ge3\) and \(a,b,c\ge0\), \(a+b+c=n\), are part of the theorem; in particular, all three requested lengths are legal even for \(n=3\).

The result is an exact existence classification and an explicit construction, not an enumeration of all matchings and not a statement about larger prescribed distances.

## Proof
**Necessity of even \(b\).** There are \(n\) even and \(n\) odd seats. Edges of lengths \(1\) and \(3\) join opposite parities. Edges of length \(2\) join seats of equal parity, including possible wraparound edges because the total order is even. If there are \(x\) even-even edges and \(y\) odd-odd edges, the remaining parity-class sizes are \(n-2x\) and \(n-2y\), and must be equal since all remaining edges cross parity. Hence \(x=y\) and \(b=x+y=2x\) is even.

**The modular obstruction.** Suppose \(3\mid n\), \(a=1\), \(b=0\), and \(c=n-1\). As \(3\mid2n\), the seats split into three residue classes modulo three, each of even size \(2n/3\). Every length-three edge stays inside one residue class, whereas a length-one edge joins two different residue classes (also when it wraps across the end of the labeling). After taking the unique length-one edge, the two affected classes have odd remaining cardinality, and hence cannot be perfectly matched by length-three edges. No required perfect matching exists.

**Six matching tiles.** On a consecutive block labeled starting at zero, consider the following explicit perfect matchings; the accompanying triple lists the numbers of edges of ordinary lengths \(1,2,3\), respectively:

| Tile | Matched pairs | Length triple |
|---|---|---|
| A | \((0,1)\) | \((1,0,0)\) |
| B | \((0,3),(1,2)\) | \((1,0,1)\) |
| C | \((0,2),(1,3)\) | \((0,2,0)\) |
| D | \((0,3),(1,4),(2,5)\) | \((0,0,3)\) |
| E | \((0,2),(1,4),(3,5)\) | \((0,2,1)\) |
| F | \((0,2),(1,4),(3,6),(5,7)\) | \((0,2,2)\) |

Every row covers exactly the consecutive labels from zero through one less than twice its number of edges, with no repeated endpoint. Translating a row to its own consecutive block, and juxtaposing blocks without overlap, therefore yields a perfect matching of the full interval of \(2n\) seats. Every edge in these rows has ordinary difference at most three, so for \(n\ge3\) its circular length in the full graph is unchanged.

**Construction when \(b>0\).** Since \(b\) is even, write \(b=2t\) with \(t\ge1\), and \(c=3q+r\), \(0\le r\le2\). Use one E tile if \(r=1\), or one F tile if \(r=2\), together with \(t-1\) C tiles in either of those cases. If \(r=0\), instead use \(t\) C tiles. Then add \(q\) D tiles and \(a\) A tiles. The concatenated matching has length counts exactly \((a,b,c)\). All coefficients of tiles are nonnegative and no extra divisibility condition occurs.

**Construction when \(b=0\).** Write \(c=3q+r\) with \(0\le r\le2\). Whenever \(a\ge r\), take \(r\) B tiles, \(q\) D tiles, and \(a-r\) A tiles. This leaves only two types of still-unmatched feasible triples: \(a=0\), \(r\in\{1,2\}\), or \(a=1\), \(r=2\). In the second case \(n=a+c\) is divisible by three and the modular obstruction already excludes it. In the first case all \(n\) edges have length three and \(3\nmid n\). Consequently \(\gcd(3,2n)=1\); adding three modulo \(2n\) runs through one Hamiltonian cycle of all seats. Pair consecutive vertices along this cycle, explicitly
\[
\left\{\left\{6j\bmod 2n,\ (6j+3)\bmod 2n\right\}:0\le j<n\right\}.
\]
Its \(n\) edges are disjoint, span the entire vertex set, and have circular length three. Every feasible case is constructed, proving sufficiency and the theorem. \(\square\)

## Verification
The standalone Python program `verify.py` includes an explicit implementation of all six tiles, their concatenation, and the step-three cycle construction. It verifies all \(20{,}309\) feasible multiplicity triples with \(3\le n\le60\), checking every endpoint exactly once and the full length histogram. Separately, a bitmask recurrence generates **all** attainable histograms from perfect matchings whose circular lengths lie in \(\{1,2,3\}\) for each \(3\le n\le10\), finding precise agreement with the theorem, including the excluded multiples-of-three case. Running `python3 verify.py` ends with `VERIFICATION_OK`. Finite checks independently test implementation and small boundaries; the preceding proof establishes all integer parameters.

## Relationship to prior work
Meszka, Pasotti and Pellegrini [1, Theorem 1.4 and Section 3] solve the even seating-couples problem when the prescribed list has at most two distinct distances; their Corollary 4.9 handles a consecutive set of lengths with **equal** multiplicities, and Corollary 4.2 covers a class of nonincreasing multiplicities. Their Conjecture 3 asserts parity sufficiency for arbitrary lists of distances below an odd prime. The new contribution is an exact classification for **all multiplicity profiles supported on the first three distances**, including the genuinely three-distinct-distance cases with a positive even number of length-two edges. This is stronger than the three-distance restriction of that conjecture, because it treats every \(n\ge3\) and identifies the exceptional composite-order profile.

Kohen and Sadofschi Costa [2] establish arbitrary prescribed differences coprime to \(2n\). Their theorem implies portions of our \(b=0\) case when \(3\nmid n\), but not the genuinely three-distance cases, which all contain a nonunit distance two. The odd-seat theorem [3] concerns a different cyclic order and does not cover these even-seat matchings. The binary-vector-space prescribed-difference problem [4] is mathematically related but takes place in \(\mathbb F_2^s\), not \(\mathbb Z/(2n)\mathbb Z\).

## Limitations
The structural theorem does not count the number of matchings realizing a profile, address distances four or larger, or prove the full arbitrary-distance prime-order conjecture. Some two-distinct-distance and coprime cases are already subsumed by [1] and [2] and are included only for a complete unified characterization. Literature indexing is incomplete, so priority for the precise three-distance classification remains subject to further independent scrutiny.

## References
[1] M. Meszka, A. Pasotti, and M. A. Pellegrini, *The seating couple problem in even case*, arXiv:2308.16553v1, first posted 31 August 2023; *Discrete Mathematics* 347 (2024), 114182. https://arxiv.org/pdf/2308.16553

[2] D. Kohen and I. Sadofschi Costa, *On a generalization of the seating couples problem*, arXiv:1603.06625v1, first posted 21 March 2016; *Discrete Mathematics* 339 (2016), 3017–3019. https://arxiv.org/pdf/1603.06625

[3] A. Pasotti and M. A. Pellegrini, *A generalization of the problem of Mariusz Meszka*, *Graphs and Combinatorics* 32 (2016), 333–350. doi:10.1007/s00373-015-1563-0.

[4] A. Kreindel and A. L. Zabokritskiy, *Prescribed-difference matchings with four and eight holes: Fourier filters for compatible boundaries*, arXiv:2608.27547v1 (2026). https://arxiv.org/pdf/2608.27547
