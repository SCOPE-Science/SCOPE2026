# A sharp shortcut-length transition in directed-cycle multipath complexes

## Finding
Let \(n\ge 4\) and \(2\le k\le n-1\) be integers. Orient the edges of the cycle on \(\mathbb Z/n\mathbb Z\) coherently, with arcs \(e_i:i\to i+1\pmod n\). Add precisely one shortcut arc \(s:0\to k\), and denote the resulting digraph by \(D_{n,k}\). Let \(X(D)\) be the simplicial complex whose vertices are arcs of \(D\) and whose faces are arc sets forming vertex-disjoint directed paths (isolated vertices allowed).

Then
\[
X(D_{n,k})\simeq
\begin{cases}
S^{n-2}\vee S^{n-3},&k=2,\\
S^{n-2},&3\le k\le n-1.
\end{cases}
\]
The natural inclusion \(X(\overrightarrow{C}_n)\hookrightarrow X(D_{n,k})\) is a homotopy equivalence for \(k\ge3\), indeed the larger complex *simplicially collapses* onto the original boundary sphere. At the unique exceptional shortcut length \(k=2\), the same inclusion identifies the original \(S^{n-2}\) summand, while a single new integral class appears in degree \(n-3\).

## Assumptions and scope
Graphs are finite directed simple graphs without loops. The complex \(X(D)\) forbids directed cycles of any length as well as two selected arcs having the same source or the same target. All homotopy and homology assertions are integral. The shortcut is forward in the chosen coherent cyclic orientation, with a directed path of length \(k\) from its source to target along the original cycle. No assertion is made for multiple added shortcuts or arbitrary orientations. The bound \(n\ge4\) makes both displayed summands connected spheres; the three-vertex boundary case has a disconnected extra component.

## Proof
Write \(E=\{e_0,\ldots,e_{n-1}\}\). Every proper subset of \(E\) is a disjoint union of directed paths, whereas \(E\) itself is a directed cycle. Thus the deletion of the shortcut vertex \(s\) is precisely
\[
Y=X(\overrightarrow{C}_n)=\partial\Delta(E)\cong S^{n-2}.
\]
Define disjoint arc sets \(A=\{e_1,\ldots,e_{k-2}\}\) and \(B=\{e_k,\ldots,e_{n-1}\}\), of sizes \(k-2\) and \(n-k\), respectively; \(\Delta(\varnothing)\) denotes the complex consisting only of the empty face.

Any face containing \(s\) must omit \(e_0\) (same source) and \(e_{k-1}\) (same target). These are the only local arc conflicts. The sole directed cycle remaining after those omissions is the cycle formed by \(s\) and *all* arcs in \(B\). In particular, each proper subset of \(B\) is allowed, independently of every subset of \(A\). Hence the **exact simplicial link**, not merely its homotopy type, is
\[
L=\operatorname{lk}_{X(D_{n,k})}(s)
=\Delta(A)*\partial\Delta(B),
\quad X(D_{n,k})=Y\cup_L(s*L).
\]
Here \(s*L\) is the simplicial cone on \(L\), with intersection \(L\) inside \(Y\).

If \(k\ge3\), then \(e_1\in A\), so \(L\) is a simplicial cone with apex \(e_1\). More precisely, for each face containing \(s\) but not \(e_1\), pair it with the face obtained by inserting \(e_1\). Process these pairs in decreasing order of the lower face's cardinality. The lower member of each pair is a free face of the upper member at the moment it is removed: every other possible coface contains \(s\) and has already been removed at a larger cardinality. This is an explicit sequence of elementary simplicial collapses, removes **all** faces containing \(s\), and leaves exactly \(Y\). The number of free-face pairs is \(2^{k-3}(2^{n-k}-1)\).

If \(k=2\), then \(A=\varnothing\), \(|B|=n-2\), and \(L=\partial\Delta(B)\cong S^{n-4}\). The attaching inclusion \(L\to Y\cong S^{n-2}\) is nullhomotopic because \(S^{n-2}\) is \((n-3)\)-connected. (When \(n=4\), this includes maps from \(S^0\) into the path-connected \(S^2\).) The union of a CW complex with a cone attached by a nullhomotopic map has homotopy type the wedge of that CW complex with the suspension of the link. It follows that
\[
X(D_{n,2})\simeq Y\vee\Sigma L\simeq S^{n-2}\vee S^{n-3}.
\]
Under this wedge equivalence, the map from \(Y\) is the first summand inclusion, proving the integral inclusion statement. These arguments use finite simplicial complexes and hold for every parameter in the stated range.

## Verification
The standalone program `verify_shortcut.py` enumerates every arc subset independently of the closed-form link description, checks degree restrictions and directed acyclicity directly, and compares them with the proposed complete list of forbidden configurations. For all \(35\) pairs \(4\le n\le10\), \(2\le k<n\), it computes the entire reduced mod-two Betti vector, confirming the ranks in the theorem, and independently checks the exact face counts. It also replays all proposed free-face collapses for \(k\ge3\) and checks that the remaining simplicial complex is precisely \(\partial\Delta(E)\). It examined \(17,349\) nonempty faces and validated \(1,291\) elementary free-face pairs. Run `python3 verify_shortcut.py`; expected terminal line: `VERIFY_OK`. Finite checks are supplemental, not an infinite-family proof.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith identified the coherent directed cycle's multipath complex as a boundary sphere and classified the associated complexes for linear and polygonal graphs [1]. The present result *uses* that baseline and determines how one forward shortcut changes it; a chorded cycle is not an oriented polygon in their sense. Deshpande and Sawant introduced a conflict-hypergraph framework for directed linear forests and explicitly posed the task of computing homotopy types for broader cyclic digraphs [2, Problem 6.3]; their deletion/link principles are compatible with the proof, but their qualitative vertex-decomposability criteria for acyclic digraphs do not determine this two-case classification. Caputi, Collari and Smith study bidirected path and polygon complexes, a different arc set with two orientations for each cycle edge [3]. The precise shortcut-length threshold and the relative elementary-collapse statement are not obtained from those inspected classifications.

## Limitations
No independent mathematical audit has been performed. The novelty comparison covers selected primary literature and relevant mathematical records, not an exhaustive priority search; an unlocated treatment of one-chord multipath complexes remains possible. The homotopy splitting is not asserted to be natural for additional automorphisms, and the result does not classify multiple shortcuts, arbitrary orientations or the excluded three-vertex boundary case.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first posted 2022-08-09), https://arxiv.org/abs/2208.04656.
2. P. Deshpande, R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (first posted 2026-02-16), https://arxiv.org/abs/2602.14936.
3. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first posted 2026-01-09), https://arxiv.org/abs/2601.05670.
