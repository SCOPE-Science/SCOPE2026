# Monitoring edge-geodetic polynomials of unicyclic graphs

## Finding

For a finite connected simple unicyclic graph \(G\), define its monitoring edge-geodetic polynomial by
\[
\mathcal M_G(z)=\sum_{S\subseteq V(G)\,\text{monitoring}}z^{|S|}.
\]
A set \(S\) is *monitoring* if, for every edge \(e\), some pair of vertices of \(S\) has \(e\) on **every** shortest path joining that pair; equivalently, deletion of \(e\) increases their distance.

Write \(C=(c_0,\ldots,c_{n-1})\) for the unique cycle in cyclic order, let \(N=|V(G)|\), let \(\ell\) be the number of leaves, and put
\[
A=\{i\in\mathbb Z/n\mathbb Z:\deg_G(c_i)>2\},\qquad
m=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Thus \(A\) indexes exactly the cycle vertices with a nontrivial attached tree. Define the bounded-composition numbers
\[
c_m(d,r)=[t^d](t+t^2+\cdots+t^m)^r,
\qquad
R_{d,m}(z)=\sum_{j=0}^{d-1}c_m(d,j+1)z^j
\]
for positive integers \(d,r\). If \(A\ne\varnothing\), let \(d_1,\ldots,d_a\) be the positive cyclic edge-gap lengths between successive members of \(A\), including the single gap \(n\) when \(|A|=1\). If \(A=\varnothing\), set
\[
Q_{n,\varnothing}(z)=\sum_{k=3}^{n}\frac{n}{k}c_m(n,k)z^k.
\]
For nonempty \(A\), set \(Q_{n,A}(z)=\prod_{j=1}^{a}R_{d_j,m}(z)\). Then the complete polynomial, for **every** connected unicyclic graph, is
\[
\boxed{\mathcal M_G(z)=z^\ell(1+z)^{N-n-\ell+|A|}\,Q_{n,A}(z).}
\]
In particular, the polynomial depends on the off-cycle trees only through \(N\), \(\ell\), and the cyclic **multiset of gap lengths** between their attachment roots. Their rooted branching shapes and the cyclic order of the gap lengths do not affect it.

When \(A\ne\varnothing\), put \(r_j=\lceil d_j/m\rceil\). Every minimum monitoring set consists of all leaves plus precisely \(r_j-1\) previously unselected bare cycle vertices in the \(j\)-th attachment gap; its size and multiplicity are
\[
\operatorname{meg}(G)=\ell+\sum_{j=1}^{a}(r_j-1),\qquad
\#\{\text{minimum monitoring sets}\}=\prod_{j=1}^{a}c_m(d_j,r_j).
\]
For a bare cycle, the minimum size is \(4\) for \(n=4\) and \(3\) otherwise; the number of minimum monitoring sets is \(1\) for \(n=4\), and equals
\[
\begin{cases}
\dfrac{n(n^2-1)}{24},&n\ge3\text{ odd},\\[3pt]
\dfrac{n(n-2)(n-4)}{24},&n\ge6\text{ even}.
\end{cases}
\]
For example, if the six-cycle has one pendant leaf at each of two opposite cycle vertices, then \(\ell=2\), \(|A|=2\), and
\[\mathcal M_G(z)=z^2(1+z)^2(2z+z^2)^2,\]
so exactly four minimum monitoring sets have size four.

## Assumptions and scope

The graph is finite, simple, undirected, connected, and has exactly one cycle of length \(n\ge3\). Edges have unit length; distances after deletion of a bridge may be infinite. Every off-cycle vertex lies in a tree rooted at one cycle vertex. Leaves are the vertices of degree one in the full graph; there are no leaves on the cycle. All vertex subsets are distinguished by their actual labeled vertices, not up to automorphism. The variable \(z\) records the cardinality of a selected subset. The assertions cover the bare cycle case as well as arbitrary pendant-tree shapes and placements. No positivity, planarity, or upper bound on degrees is assumed beyond unicyclicity.

## Proof

**1. Forced leaves and projected terminals.** Let \(L\) denote the set of leaves of \(G\). A shortest path containing the edge incident to a leaf must have that leaf as an endpoint, so any monitoring set \(S\) contains \(L\). For \(S\supseteq L\), project each chosen vertex to the unique cycle vertex on the same rooted tree, and write \(P(S)\subseteq\mathbb Z/n\mathbb Z\) for the set of projected cycle indices. If an attached tree at \(c_i\) is nontrivial, it contains an off-cycle leaf, which is in \(S\); hence \(i\in P(S)\) automatically for \(i\in A\). At a bare cycle vertex \(i\notin A\), the projection \(i\in P(S)\) holds exactly when \(c_i\in S\).

**2. Cycle monitoring is exactly a short-gap condition.** A shortest path between two vertices projecting to distinct cycle indices \(i,j\) consists of their unique hanging-tree segments joined by a shortest \(i\)-to-\(j\) arc of the cycle. If the two vertices project to the same index, no shortest path uses a cycle edge. Consequently cycle-edge monitoring by \(S\) is equivalent to cycle-edge monitoring by \(P(S)\) on the bare cycle. For a nonempty set of cycle terminals, list the successive positive cyclic gaps \(g_1,\ldots,g_k\) (a singleton has the one gap \(n\)). If every gap satisfies \(g_j\le m\), the unique shorter cycle arc between the adjacent selected terminals covers every edge of that gap, and hence the whole cycle is monitored. Conversely, if some gap \(g\ge n/2\), any cycle path between terminal indices that traverses an edge of its interior must traverse the entire terminal-free gap. The complementary route has length at most \(n-g\le g\); therefore that gap cannot belong to every shortest path between any selected terminal pair (ties do not monitor an edge). Hence the cycle is monitored **if and only if** every successive gap is at most \(m=\lfloor(n-1)/2\rfloor\).

**3. Bridges impose no further conditions.** Remove a bridge \(e\) outside the cycle. The component away from the cycle contains a degree-one vertex of \(G\), necessarily selected. If the short-gap condition holds, \(P(S)\) contains at least three distinct cycle vertices: one terminal leaves the cyclic gap \(n\), and two terminals leave a gap of length at least \(n/2\). Thus a second selected vertex projects to a different cycle root and lies in the other component of \(G-e\). Their unique connecting path uses \(e\), so its removal changes their distance. Every bridge is monitored. Combining the first three steps gives the exact all-subset criterion
\[
S\text{ is monitoring}\quad\Longleftrightarrow\quad
L\subseteq S\text{ and every cyclic gap in }P(S)\text{ is at most }m.
\]

**4. Enumeration.** Once leaves are forced, selection of the \(N-n-\ell\) nonleaf vertices outside the cycle and selection of the \(|A|\) attached cycle roots are completely free and independent of the projected terminals. This contributes \(z^\ell(1+z)^{N-n-\ell+|A|}\). The remaining selectable vertices are exactly the bare cycle roots, subject to the short-gap criterion.

For \(A\ne\varnothing\), each fixed gap of length \(d\) between attachment roots can be split by choosing \(j\) bare roots into \(j+1\) positive consecutive gaps, all at most \(m\). There are \(c_m(d,j+1)\) such splittings, and gaps between different attachment roots are independent. This yields \(\prod R_{d_j,m}(z)\), including the case of a single attached root with its one full-circle gap.

For \(A=\varnothing\), any monitoring set has \(k\ge3\) selected vertices and gives a cyclic sequence of \(k\) positive gaps bounded by \(m\) with total length \(n\). There are \(n c_m(n,k)\) pairs consisting of a labeled starting cycle vertex and an ordered gap composition; each selected \(k\)-set occurs exactly \(k\) times, giving \((n/k)c_m(n,k)\). This is an integer and yields \(Q_{n,\varnothing}\). The displayed polynomial follows.

**5. Minimum sets and invariance.** For a fixed attachment gap \(d\), the smallest possible number of pieces of length at most \(m\) is \(r=\lceil d/m\rceil\). It requires exactly \(r-1\) selected bare roots, with \(c_m(d,r)\) choices. The independent gaps and the nonzero constant term in every free-vertex factor prove the minimum-size and multiplicity formulas. For a bare cycle, \(Q_{n,\varnothing}\) has smallest exponent three except when \(n=4\). Counting bounded compositions of \(n\) into three pieces by one-term inclusion-exclusion gives \(c_m(n,3)=\frac{(n^2-1)}8\) for odd \(n\) and \(c_m(n,3)=\frac{(n-2)(n-4)}8\) for even \(n\ge6\); multiplying by \(n/3\) yields the two displayed counts. Finally, the factorization is symmetric in the multiset \(\{d_j\}\) and uses off-cycle trees only via \(N\) and \(\ell\), proving the claimed invariance. \(\square\)

## Verification

The included standard-library Python script `verify.py` computes monitored-edge masks by comparing all-pairs graph distances before and after individual edge deletions. Independently, it evaluates the leaf-plus-cyclic-gap criterion and the factorized polynomial. It exhaustively checks **all 3,898 labeled connected unicyclic graphs on three through six vertices** (with **241,592 candidate vertex subsets**), then tests 96 deterministic additional unicyclic graphs on seven through twelve vertices (bringing the total to **370,616 subset checks**). It also compares the bounded-composition formula against direct cycle-root subset enumeration for **16,376 cycle/attachment patterns** of lengths three through thirteen. All these checks pass; they are finite corroboration, not a proof of the infinite statement.

Reproduce with `python3 verify.py`. Its expected four-line output is embedded as `verification_output.txt`. Only the Python standard library is needed.

## Relationship to prior work

Dev, Dey, Foucaud, Narayanan, and Ramasubramony Sulochana introduced monitoring edge-geodetic sets and computed their **minimum cardinalities** on cycles and unicyclic graphs (Theorems 3.4 and 3.5 of [1]). In particular, the observation that a mandatory pendant leaf can play the role of an attached cycle root is present in their proof. The present claim is the exact characterization of *every* monitoring set and its **entire cardinality generating polynomial**, including independent gap factors, minimum-set multiplicities, and invariance under rearrangement of branching and gaps. Those enumerative conclusions are not statements of [1]. Haslegrave's Cartesian/strong product analysis [2] gives a general sectional characterization for products, rather than this pendant-tree and cycle-gap factorization. Later extremal and bound results [3] concern mandatory vertices, scalar parameters, and graph operations, not the complete unicyclic enumeration. This relationship is an extension of known ideas, not an assertion that the underlying notion or the scalar unicyclic formula is new.

## Limitations

Only unweighted connected graphs with exactly one cycle are covered. The theorem does not enumerate monitoring configurations on multicyclic graphs or under edge weights, and it does not solve the general NP-hard monitoring-set problem. Published literature may contain an implicit equivalent all-set derivation not found in the searches. An independent review has not been performed; the finite verifier does not establish validity for arbitrarily large graphs, which rests on the proof.

## References

[1] S. R. Dev, S. Dey, F. Foucaud, K. Narayanan, and L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, first posted 7 October 2022, especially Definition 1.1 and Theorems 3.4–3.5. https://arxiv.org/abs/2210.03774

[2] J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955, first posted 17 October 2022; Discrete Applied Mathematics 340 (2023), 79–84. https://arxiv.org/abs/2210.08955

[3] F. Foucaud et al., *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122, first posted 14 March 2024. https://arxiv.org/abs/2403.09122
