# Strong alliance polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), vertex parts \(V_1,\ldots,V_r\), and \(N=\sum_{i=1}^r n_i\), where \(n_i=|V_i|\). For a nonempty set \(S\subseteq V(G)\), write \(s=|S|\), \(s_i=|S\cap V_i|\), and
\[
c_i=\left\lceil\frac{N-n_i}{2}\right\rceil.
\]
Then \(S\) is a strong defensive alliance if and only if
\[
s-s_i\ge c_i
\]
for every \(i\) with \(s_i>0\).

This local criterion has four structural consequences. First, every strong defensive alliance has \(s\ge\lceil N/2\rceil\), and the family of strong defensive alliances is an upper ideal: every superset of a strong defensive alliance is again a strong defensive alliance. Second, define an occupied part \(V_i\) to be tight for \(S\) when \(s-s_i=c_i\). A strong defensive alliance is inclusion-minimal if and only if it has at least two tight occupied parts. Third, its minimum possible cardinality is
\[
a(G)=
\begin{cases}
(N+1)/2, & N\text{ odd},\\
N/2, & N\text{ even and every }n_i\text{ is even},\\
N/2+1, & N\text{ even and at least one }n_i\text{ is odd}.
\end{cases}
\]
Fourth, if
\[
u_i(s)=\min\left\{n_i,\max\{0,s-c_i\}}\right\},
\]
then the complete strong alliance polynomial is
\[
a(G;x)=\sum_{s=1}^N
\left(
[y^s]\prod_{i=1}^r\sum_{j=0}^{u_i(s)}\binom{n_i}{j}y^j
\right)x^s.
\]
Thus the result classifies every contributing vertex set, not only the minimum ones. If \(a_s(G)=[x^s]a(G;x)\), upper-ideal double counting also gives
\[
\frac{a_s(G)}{\binom Ns}\le
\frac{a_{s+1}(G)}{\binom N{s+1}}
\qquad(1\le s<N).
\]

## Assumptions and scope
Graphs are finite and simple. The complete multipartite graph has at least two nonempty parts, hence is connected. A strong defensive alliance is a nonempty set \(S\) such that every \(v\in S\) has at least as many neighbors in \(S\) as outside \(S\). The strong alliance polynomial counts strong defensive alliances whose induced subgraph is connected, as in Carballosa, Hernández-Gómez, Rosario, and Torres-Nuñez. In a connected complete multipartite graph every strong defensive alliance meets at least two parts, so its induced subgraph is automatically connected; no extra connectedness condition is needed in the formula.

The theorem concerns arbitrary positive part sizes and all \(r\ge2\). The complete-bipartite case is not claimed as new: it is exactly the specialization already computed in the foundational strong-alliance-polynomial paper.

## Proof
For \(v\in S\cap V_i\), the neighbors of \(v\) lying in \(S\) are precisely the vertices of \(S\) outside \(V_i\). Hence
\[
\delta_S(v)=s-s_i.
\]
The total degree of \(v\) is \(N-n_i\), so
\[
\delta_{V(G)\setminus S}(v)=(N-n_i)-(s-s_i).
\]
Therefore \(\delta_S(v)\ge\delta_{V(G)\setminus S}(v)\) is equivalent to
\[
2(s-s_i)\ge N-n_i,
\]
or, integrally, to \(s-s_i\ge c_i\). This proves the all-set criterion.

A strong defensive alliance cannot lie in one part, because a vertex would then have zero neighbors in \(S\) and at least one neighbor outside that part. Let \(T=\{i:s_i>0\}\), with \(q=|T|\ge2\). Summing \(2(s-s_i)\ge N-n_i\) over \(i\in T\) gives
\[
2(q-1)s\ge qN-\sum_{i\in T}n_i\ge(q-1)N,
\]
so \(s\ge\lceil N/2\rceil\).

Now add one vertex to a strong defensive alliance. If the added vertex lies in an already occupied part, the quantity \(s-s_i\) for that part is unchanged and it increases by one for every other occupied part. If the added vertex lies in a previously unoccupied part \(V_k\), it has all \(s\) old vertices as neighbors; since \(2s\ge N\ge N-n_k\), it also satisfies the strong inequality. Existing vertices only gain internal support. Hence strong defensive alliances form an upper ideal.

For minimality, put \(d_i=(s-s_i)-c_i\) on occupied parts. Removing a vertex from \(V_k\) leaves the cross-part count unchanged for the remaining vertices of \(V_k\), if any, and decreases the cross-part count by one in every other occupied part. Thus removal from \(V_k\) fails exactly when some different occupied part has \(d_i=0\). This happens for every possible removed vertex exactly when at least two occupied parts have \(d_i=0\), proving the tight-part characterization of inclusion-minimal alliances.

For fixed cardinality \(s\), the criterion is equivalent to
\[
0\le s_i\le u_i(s),\qquad \sum_i s_i=s.
\]
Choosing \(s_i\) vertices from each part contributes \(\prod_i\binom{n_i}{s_i}\), so coefficient extraction gives the displayed polynomial.

It remains to simplify the minimum. The half-order lower bound was already proved. If \(N=2m+1\), then at \(s=m+1\) one has \(u_i(s)=\lceil n_i/2\rceil\), and therefore \(\sum_i u_i(s)\ge m+1\); a feasible profile exists. If \(N=2m\), then at \(s=m\), \(u_i(s)=\lfloor n_i/2\rfloor\), whose sum is \(m-o/2\), where \(o\) is the number of odd part sizes. Thus \(s=m\) is feasible exactly when \(o=0\). If \(o>0\), then at \(s=m+1\), \(u_i(s)=\min\{n_i,\lfloor n_i/2\rfloor+1\}\), and their sum is at least \(m+1\), so the minimum is \(m+1\).

Finally, let \(a_s(G)\) be the number of strong alliances of size \(s\). Count inclusion edges from strong \(s\)-sets to strong \((s+1)\)-sets. The upper-ideal property gives exactly \((N-s)a_s(G)\) such edges from below, while each strong \((s+1)\)-set has at most \(s+1\) predecessors. Hence \((N-s)a_s(G)\le(s+1)a_{s+1}(G)\), which is the normalized coefficient inequality.

## Verification
The accompanying `verify.py` constructs every ordered complete-multipartite profile of total order at most \(9\). For every nonempty vertex subset it checks the strong defensive alliance condition directly from literal graph adjacency, independently checks the part-capacity criterion, checks induced connectivity, tests upward closure, tests the two-tight-part characterization of inclusion-minimal alliances, reconstructs every polynomial coefficient by dynamic coefficient extraction, checks the parity formula for the minimum, checks the normalized level-density inequality, and separately verifies the published complete-bipartite specialization.

The exact replay result is:

`VERIFY_OK profiles=502 subset_checks=173238 criterion_checks=173238 coefficient_checks=4554 upset_checks=179490 minimal_checks=62544 density_checks=3550 bipartite_checks=36 max_order=9`

The finite census is a regression check. The infinite statement is established by the proof above.

## Relationship to prior work
Carballosa, Hernández-Gómez, Rosario, and Torres-Nuñez introduced the strong alliance polynomial and explicitly computed it for paths, cycles, complete graphs, stars, complete bipartite graphs, and double stars. Their Theorem 3.3 gives the complete-bipartite factorization and the minimum \(\lceil n/2\rceil+\lceil m/2\rceil\). The theorem here specializes exactly to that result when \(r=2\), but extends from two parts to arbitrary complete multipartite graphs, identifies the upper-ideal structure and all inclusion-minimal alliances, collapses the arbitrary-part minimum to a parity law, and gives the exact all-cardinality polynomial.

A later defensive-alliance-polynomial paper again treats complete bipartite graphs among its explicit graph classes and recovers the strong alliance polynomial as a specialization. The inspected literature and database searches did not locate an arbitrary complete-multipartite statement implying the theorem above. This is evidence of non-coverage, not a proof of bibliographic uniqueness.

## Limitations
The proof is specific to complete multipartite adjacency: all vertices outside a vertex's own part are neighbors and none inside its part are. It does not extend unchanged to multipartite graphs with missing cross edges. No claim is made here that the resulting polynomial is always log-concave or unimodal for arbitrary complete multipartite graphs, although the published complete-bipartite case has that property. Bibliographic residual risk remains because older alliance literature can be indexed under the synonym “cohesive set” and some journal mirrors are incomplete; the closest primary preprint was nevertheless inspected in full at the defining and complete-bipartite theorem sections.

## References
1. W. Carballosa, J. C. Hernández-Gómez, O. Rosario, Y. Torres-Nuñez, “Computing the strong alliance polynomial of a graph,” arXiv:1507.08654v1, first publicly posted 2015-07-30; later published in *Investigación Operacional* 37(2), 115–123 (2016).
2. H. Ibrahim, “Defensive alliance polynomial,” arXiv:1811.10089v1 (2018); later *Journal of Combinatorial Mathematics and Combinatorial Computing* 115, 35–60.
