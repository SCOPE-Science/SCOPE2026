# Eccentric subgraph index and antipodal minimizers of every sunlet

## Finding
For every integer \(n\ge3\), let \(S_n=C_n\circ K_1\) have labelled cycle vertices \(c_i\) and their pendant leaves \(\ell_i\), indexed modulo \(n\). For vertices \(u,v\), let \(f(u,v)\) count all connected (not necessarily induced) subgraphs containing them; let \(\epsilon(u)=\min_v f(u,v)\) and \(ES(S_n)=\sum_u\epsilon(u)\). Put
\[
L_n=(2n-3)2^{n-2}+\begin{cases}
2^{n/2},&n\text{ even},\\
3\cdot 2^{(n-3)/2},&n\text{ odd}.
\end{cases}
\]
Then each pendant leaf satisfies \(\epsilon(\ell_i)=L_n\), each cycle vertex satisfies \(\epsilon(c_i)=2L_n\), and
\[
ES(S_n)=3nL_n.
\]
The minimizing witnesses are precisely the pendant leaves at cycle distance \(\lfloor n/2\rfloor\) from the indicated leaf or cycle vertex. In particular the eccentric-subgraph center (the vertices maximizing \(\epsilon\)) is exactly the core cycle, and the minimizing pair-distance exhibits an even/odd antipodal distinction.

## Assumptions and scope
Graphs are finite, labelled, undirected and simple. A subgraph is specified by both its vertex set and edge set; it need not be induced. A connected subgraph on one vertex and no edges is counted. The sunlet has exactly \(2n\) vertices and \(2n\) edges. Its underlying cycle is a simple cycle, so \(n\ge3\). Here \(f(u,v)\) includes the case \(u=v\). This definition follows De and Patra (2026), not distance eccentricity and not the number of connected *induced* subgraphs.

## Proof
Fix two different indices \(0,d\), with \(1\le d\le\lfloor n/2\rfloor\). Every connected subgraph containing \(\ell_0\) and \(\ell_d\) must contain both of their pendant edges. Removing the pendant edges leaves a connected cycle-edge subgraph containing \(c_0,c_d\); its selected edges are either a proper contiguous path of \(j\) cycle vertices, \(2\le j\le n-1\), one of the \(n\) spanning paths obtained by deleting one cycle edge, or the entire cycle. Other pendant edges can be selected independently at cycle vertices in the path (but not at absent core vertices).

For a proper path of \(j\) vertices, both required leaf edges are selected, while its other \(j-2\) pendant edges are optional. The number of cyclic arcs of \(j\) vertices containing both indices is
\[
a_j(d)=2j-n+\max(d-j,0)+\max(n-d-j,0).
\]
Indeed an arc misses vertex \(i\) in exactly \(n-j\) of its \(n\) positions. By inclusion-exclusion for the forbidden positions, the intersection of the two missing-position sets has size \(\max(d-j,0)+\max(n-d-j,0)\). The \(n+1\) spanning paths and cycles each allow \(2^{n-2}\) selections of the other pendant edges. Thus
\[
F_n(d):=f(\ell_0,\ell_d)=(n+1)2^{n-2}+\sum_{j=2}^{n-1}a_j(d)2^{j-2}.
\]
For \(d\) in the indicated range, \(a_j(d)\) never increases with \(d\): the function \(\max(d-j,0)+\max(n-d-j,0)\) is nonincreasing up to the midpoint. The decrease from \(d-1\) to \(d\), for \(2\le d\le\lfloor n/2\rfloor\), is strict already for \(j=d\). Consequently \(F_n(d)\) decreases strictly with distance, and is minimized at \(d=\lfloor n/2\rfloor\).

If \(n=2m\), the arc numbers at \(d=m\) vanish for \(j\le m\) and equal \(2s\) at \(j=m+s\) for \(1\le s\le m-1\). Using the geometric sum and its derivative gives
\[
F_{2m}(m)=(2m+1)2^{2m-2}+\sum_{s=1}^{m-1}2s\,2^{m+s-2}=(4m-3)2^{2m-2}+2^m.
\]
If \(n=2m+1\), at distance \(m\) the arc numbers vanish through \(j=m\) and equal \(2s-1\) at \(j=m+s\), \(1\le s\le m\). Hence
\[
F_{2m+1}(m)=(2m+2)2^{2m-1}+\sum_{s=1}^{m}(2s-1)2^{m+s-2}=(4m-1)2^{2m-1}+3\cdot2^{m-1}.
\]
Together these are exactly \(L_n\).

For unequal core indices, including or excluding the pendant edges at the endpoints freely gives
\[
f(c_0,\ell_d)=2F_n(d),\qquad f(c_0,c_d)=4F_n(d),\qquad f(\ell_0,c_d)=2F_n(d).
\]
For the same core index, direct enumeration of paths containing it, plus spanning paths/cycle, gives
\[
T_n=f(c_0,\ell_0)=(2n-1)2^{n-1}+1.
\]
The diagonal count for \(\ell_0\) is \(T_n+1\), from the additional singleton-leaf subgraph; the diagonal count for \(c_0\) is at least \(T_n\). Direct subtraction shows \(T_n>2L_n\) for every \(n\ge3\): the difference is \(2^n+1-2^{n/2+1}>0\) for even \(n\), and \(2^n+1-3\cdot2^{(n-1)/2}>0\) for odd \(n\). For each leaf, therefore, the unique minimizing *index distances* are the farthest leaf indices (one or two depending on parity), and for each core vertex the minimum is attained precisely by those farthest leaves. The stated vertex profiles and their sum follow from rotational symmetry.

## Verification
The standalone \(\texttt{verify.py}\) enumerates connected **edge-defined** subgraphs of each \(S_n\) for \(3\le n\le8\), counts co-occurrences for all vertex pairs, and adds singleton subgraphs on the diagonal. It checks both the leaf/core minima, their total, and the pair counts for antipodal witnesses. Outputs: \(ES(S_3)=81\), \(ES(S_4)=288\), \(ES(S_5)=930\), \(ES(S_6)=2736\), \(ES(S_7)=7644\), and \(ES(S_8)=20352\). The finite exhaustive checks corroborate, but are not a substitute for, the preceding proof for all \(n\).

## Relationship to prior work
Akash De and Kamal Lochan Patra, *On the sum of eccentric subgraph numbers of the vertices of a connected graph* (arXiv:2610.19694, first posted 14 October 2026) define the same pair-count invariant and study graph-extremal questions for unicyclic graphs, trees, and prescribed pendant vertices. This result instead gives the full vertex profile, center, farthest-witness description, and parity-explicit evaluation for the canonical distributed-leaf unicyclic family. Earlier work counting connected induced subgraphs is not equivalent, because the present object counts edge-defined connected subgraphs. The exact present formula has not been identified in the checked literature; that statement is not a proof of historical priority.

## Limitations
The result is restricted to a cycle with exactly one pendant leaf per cycle vertex and does not optimize the invariant over all unicyclic graphs or provide a general tree attachment formula. The checked literature does not establish definitive novelty; potentially unindexed or differently formulated prior results remain possible. No independent mathematical audit has been performed.

## References
1. A. De and K. L. Patra, *On the sum of eccentric subgraph numbers of the vertices of a connected graph*, arXiv:2610.19694v1 (14 October 2026), https://arxiv.org/abs/2610.19694.
2. D. Pandey and K. L. Patra, *On the number of connected subgraphs of graphs*, Indian J. Pure Appl. Math. 52 (2021), 571–583, https://doi.org/10.1007/s13226-021-00061-4.
