# Sharp edge-length sensitivity of zero forcing on powers of cycles

## Finding
Let \(k\ge1\) and \(n\ge2k+3\) be integers. Index the vertices of a cycle by \(\mathbb Z/n\mathbb Z\); its \(k\)-th power \(C_n^k\) joins two vertices precisely when their cyclic distance is at most \(k\). Remove one edge \(e=\{0,d\}\), where \(1\le d\le k\), and write \(H_{n,k,d}=C_n^k-e\). Ordinary zero forcing colors an initially chosen set black and repeatedly recolors the unique white neighbor of any black vertex.

**Theorem (length-sensitive one-edge spread and complete exceptional minimizers).** For every admissible \((n,k,d)\),
\[
Z(H_{n,k,d})=\begin{cases}2k,&1\le d<k,\\2k-1,&d=k.\end{cases}
\]
When \(d=k\), there are exactly \(4k-2\) minimum initial black sets, namely
\[
B_{u,w}=\{u\}\cup\bigl(N_{H_{n,k,k}}(u)\setminus\{w\}\bigr),\qquad u\in\{0,k\},\quad w\in N_{H_{n,k,k}}(u).
\]
These are pairwise distinct. In particular, removal of any longest-range chord decreases the zero-forcing number by one, while removal of any shorter edge leaves it unchanged.

## Assumptions and scope
All graphs are finite, undirected, simple and labeled. The cycle has \(n\) vertices, \(k\ge1\), and \(n\ge2k+3\) ensures the usual power is \(2k\)-regular and at least two vertices lie outside a closed \(k\)-neighborhood. Rotating and reflecting the cycle permits the representative removed edge \(\{0,d\}\). The notation \(N_H(u)\) means the open neighborhood. Minimum means smallest cardinality, not merely inclusion-minimal. No claim is made at the dense boundary \(n\le2k+2\) or for simultaneous deletion of multiple edges.

## Proof
**First-move bound and rigidity.** Every ordinary zero-forcing set in a nonempty graph has size at least its minimum degree: the first force by \(x\) requires \(x\) and all but one of its neighbors initially black. In \(H_{n,k,d}\), the two endpoints of the deleted edge have degree \(2k-1\), while every other vertex has degree \(2k\). Thus \(Z(H_{n,k,d})\ge2k-1\). Moreover, if a zero-forcing set \(B\) has size exactly \(2k-1\), its first forcing vertex must be an endpoint \(u\in\{0,d\}\), and
\[
B=\{u\}\cup\bigl(N_{H_{n,k,d}}(u)\setminus\{w\}\bigr)
\]
for a unique \(w\in N_H(u)\). No other initially black vertex can force, as it would need at least \(2k\) initially black vertices.

**A shorter deleted edge cannot lower the invariant.** Assume \(1\le d<k\) (so \(k\ge2\)), and by exchanging endpoints if needed let the first forcing center be \(u=0\). Its first and only available force is to \(w\); afterward the black set is exactly
\[
S=N_{C_n^k}[0]\setminus\{d\}=\{-k,-k+1,\ldots,k\}\setminus\{d\}.
\]
Vertex \(0\) now has no white neighbors in the edited graph. Every other black vertex has at least two white neighbors. Indeed, for each \(x\in\{2,\ldots,k\}\setminus\{d\}\), the vertices \(k+1\) and \(k+2\) are distinct white neighbors of \(x\); for each \(x\in\{-k,\ldots,-2\}\), the vertices \(-k-1\) and \(-k-2\) are distinct white neighbors. If \(1\) is black, its white neighbors include \(k+1\) and \(d\); if \(-1\) is black, its white neighbors include \(-k-1\) and \(d\), since \(d+1\le k\). All these assertions remain valid modulo \(n\) because \(n\ge2k+3\); the removed edge is incident with \(0\), not with any \(x\ne0,d\). Hence the process is permanently stalled, so no set of size \(2k-1\) forces.

Conversely the \(2k\)-vertex interval \(I=\{-k,\ldots,k-1\}\) forces all of \(H_{n,k,d}\): use successively the forces \(0\to k\), \(1\to k+1\), and so on in the positive cyclic direction until every vertex is black. Each used edge has cyclic distance \(k\), and none is the deleted shorter edge \(\{0,d\}\). Thus \(Z(H_{n,k,d})=2k\).

**A longest deleted edge lowers the invariant.** Now \(d=k\). Choose either endpoint \(u\) of \(e\) and any \(w\in N_H(u)\). The proposed seed \(B_{u,w}\) has \(2k-1\) vertices, and \(u\) immediately forces \(w\). After this step, the black set is \(N_{C_n^k}[u]\setminus\{v\}\), where \(v\) is the other endpoint of \(e\) at cyclic distance \(k\). This is a block of \(2k\) consecutive cycle vertices. Its standard counterclockwise outward forcing chain can be chosen to use only edges of distance exactly \(k\), never the removed edge; specifically, for \(u=0,v=k\), the successive forcing sources are \(-1,-2,\ldots,-(n-2k)\), each forcing its distance-\(k\) neighbor further counterclockwise. The mirrored construction handles \(u=k\). Consequently every \(B_{u,w}\) forces the whole graph, and \(Z(H_{n,k,k})=2k-1\).

By the first-move rigidity argument, every set of this minimum cardinality must be one of these sets. For each endpoint there are exactly \(2k-1\) choices of \(w\), producing distinct sets. Moreover, a seed centered at \(0\) omits vertex \(k\), whereas one centered at \(k\) omits vertex \(0\); thus the two families are disjoint. The exact count is \(2(2k-1)=4k-2\), completing the proof. The case \(k=1\) specializes to breaking an ordinary cycle into a path, with its two endpoint seeds.

## Verification
The accompanying standalone `verify.py` reconstructs the adjacency sets and repeatedly performs **all** available forcing moves to closure. It exhausts every \((2k-1)\)-vertex candidate for \(1\le k\le4\), \(2k+3\le n\le2k+10\), \(1\le d\le k\), comparing the actual minimum-size forcing configurations against exactly the two predicted endpoint families. For shorter deleted edges, it also directly validates a size-\(2k\) witness. This is 80 parameter cases and 341272 tested subsets; finite checks are corroboration, not the general proof. Run `python3 verify.py` with Python 3, using only its standard library.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker (2026) prove \(Z(C_n^k)=2k\) in the noncomplete range, and establish general properties of zero forcing on powers. This scalar zero-forcing value is **not** claimed here as new. Edholm, Hogben, Huynh, LaGrange, and Row (2012) prove the general bound that deletion of one edge changes the zero-forcing number by at most one; this general edge-spread bound is likewise prior work. The present theorem identifies exactly **which cycle-power edges** realize the positive spread and gives the complete count and structure of the resulting smaller forcing sets. The minimum-rank work of Deaett and Meyer concerns symmetric circulant graphs themselves and does not imply one-edge-deleted zero-forcing outcomes.

## Limitations
The statement excludes \(n\le2k+2\), where the power is complete or almost complete and the combinatorics change. There is no assertion for multiple deleted edges, nonconsecutive circulant generators, or other forcing variants. The finite verifier does not certify infinitely many instances. Searches of accessible publications and mathematical records do not prove absolute historical novelty; an unindexed equivalent remains possible. Independent mathematical review has not been performed.

## References
- A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1 (first posted 2026-10-02), especially Proposition 8.
- C. J. Edholm, L. Hogben, M. Huynh, J. LaGrange, D. D. Row, *Vertex and edge spread of zero forcing number, maximum nullity, and minimum rank of a graph*, Linear Algebra and its Applications 436 (2012), 4352–4372, especially Theorem 2.17, DOI:10.1016/j.laa.2010.10.015.
- L. Deaett, S. A. Meyer, *The minimum rank problem for circulants*, arXiv:1511.07920v1 (2015).
