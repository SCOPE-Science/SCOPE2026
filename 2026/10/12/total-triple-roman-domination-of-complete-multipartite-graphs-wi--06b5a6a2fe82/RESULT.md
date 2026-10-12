# Total triple Roman domination of complete multipartite graphs without universal vertices
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\) and \(n_i\ge2\) for every \(i\). Put \(s=\min_i n_i\). Then
\[
\gamma_{[t3R]}(G)=
\begin{cases}
7,&s=2,\\
8,&s\ge3.
\end{cases}
\]
Thus, among complete multipartite graphs with no universal vertex, total triple Roman domination has a single structural threshold: a part of size two saves exactly one unit.

## Assumptions and scope
A total triple Roman dominating function is a map \(f:V(G)\to\{0,1,2,3,4\}\) such that, whenever \(f(v)<3\),
\[
f(N[v])\ge |AN(v)|+3,
\]
where \(AN(v)\) is the set of neighbors of \(v\) that receive a positive label, and such that the subgraph induced by the positive-labeled vertices has no isolated vertex. Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\), and \(\gamma_{[t3R]}(G)\) is the minimum weight. The theorem concerns all finite complete multipartite graphs with at least two parts and with every part of size at least two.

## Proof
For the upper bound when \(s=2\), choose a part \(A=\{a,b\}\) of size two and a vertex \(c\) in another part. Set \(f(a)=3\), \(f(b)=2\), \(f(c)=2\), and assign zero elsewhere. The positive vertices meet two parts, so none is isolated. A zero in the part containing \(c\) sees labels \(3\) and \(2\) in \(A\), giving closed-neighborhood weight \(5\) with two active neighbors. A zero in any other part sees all three positive vertices, giving weight \(7\) with three active neighbors. The vertex \(b\), whose label is below \(3\), sees \(c\), so its closed-neighborhood weight is \(4\) with one active neighbor; the analogous inequality for \(c\) is also satisfied. Hence \(\gamma_{[t3R]}(G)\le7\).

Because every part has size at least two, \(G\) has no universal vertex. Proposition 11 of Valenzuela-Tripodoro et al. characterizes weight \(5\) by the existence of a universal vertex, while Proposition 12 proves that no nontrivial connected graph has total triple Roman domination number \(6\). Their general lower bound \(\gamma_t(G)+3\le\gamma_{[t3R]}(G)\), together with \(\gamma_t(G)=2\) for these complete multipartite graphs, excludes weights below \(5\). Consequently the displayed weight-seven construction is optimal whenever \(s=2\).

Now suppose \(s\ge3\). Two vertices chosen from different parts and labeled \(4\), with every other vertex labeled zero, form a total triple Roman dominating function of weight \(8\). Indeed, the two positive vertices are adjacent; a zero in one of their two parts sees the other label \(4\), and a zero in any remaining part sees both labels \(4\). Hence \(\gamma_{[t3R]}(G)\le8\).

It remains to exclude weight at most \(7\). Assume such a function \(f\) exists. Let \(P=\{v:f(v)>0\}\), let \(q=|P|\), and define the excess
\[
E=\sum_{v\in P}(f(v)-1)=w(f)-q.
\]
For a part \(V_i\), put
\[
E_i=\sum_{v\in P\cap V_i}(f(v)-1).
\]
If \(z\in V_i\) is a zero vertex, then cancellation of the one unit contributed by each active neighbor converts the triple-Roman inequality exactly into
\[
E-E_i\ge3. \tag{1}
\]
If \(x\in V_i\) is positive with \(f(x)<3\), the corresponding reduced inequality is
\[
f(x)+E-E_i\ge3. \tag{2}
\]
The total condition forces \(P\) to meet at least two parts.

First, every part contains a zero. Otherwise let a part \(A\) be entirely positive and choose another supported part \(B\). If \(B\) is also entirely positive, then \(q\ge6\), so \(E\le1\). Since weight at most \(7\) prevents all vertices of \(A\) from having label at least \(2\), some \(x\in A\) has label \(1\), and (2) gives at most \(1+E\le2\), a contradiction. If \(B\) is not entirely positive, take a zero \(z\in B\). Equation (1) implies \(E\ge3\). Since \(q\ge4\) and the total weight is at most \(7\), necessarily \(E=3\) and \(q=4\). Thus \(A\) has exactly three positive vertices, \(B\) has the unique positive vertex outside \(A\), and (1) forces \(E_B=0\). Hence all excess lies in \(A\). Equation (2) then forces every vertex of \(A\) to have label at least \(3\), already contributing weight at least \(9\), again a contradiction.

Therefore every supported part has a zero to which (1) applies. If \(P\) meets exactly two parts, say \(V_i,V_j\), then (1) gives \(E_i\ge3\) and \(E_j\ge3\), so \(w(f)=q+E\ge2+6=8\). If \(P\) meets at least three parts, choose three supported parts. Summing (1) over their zero vertices gives
\[
3E-(E_i+E_j+E_k)\ge9.
\]
Because \(E_i+E_j+E_k\le E\), this implies \(E\ge5\); since \(q\ge3\), again \(w(f)\ge8\). This contradiction proves the lower bound and completes the theorem.

## Verification
The proof is analytic for arbitrary part sizes. A standalone verifier included with this result checks the definition directly on every nondecreasing multipartite profile with all part sizes at least two and total order at most eight. It exhaustively searches all labelings in \(\{0,1,2,3,4\}\), confirms the claimed minima, and separately checks the two explicit constructions on a larger deterministic family of profiles. These finite checks corroborate, but do not replace, the infinite proof.

## Relationship to prior work
Valenzuela-Tripodoro, Mateos-Camacho, Cera, and Álvarez-Ruiz introduced total triple Roman domination in a preprint posted on 17 March 2025 and in the peer-reviewed article *On the Total Version of Triple Roman Domination in Graphs*, Mathematics 13 (2025), 1277, DOI 10.3390/math13081277. The published article lists MSC 05C78. Its exact-value section proves the universal-vertex characterization of value \(5\), the nonexistence of value \(6\), and exact formulas for paths and cycles. The accessible full text contains no theorem for complete multipartite graphs; its discussion explicitly proposes determining exact values on further graph families. The present theorem uses the paper's general small-value results only for the \(s=2\) lower bound and supplies the complete multipartite structure and the new \(s\ge3\) excess argument.

Searches under the phrases “total triple Roman domination complete multipartite graph”, “total triple Roman domination complete bipartite graph”, “gamma t3R complete multipartite exact value”, and the aliases “t3RDN”, “complete bipartite”, and “Turan” found no statement implying the theorem. The closest indexed complete-multipartite results concern different invariants, including total Roman domination and total strong Roman domination; neither implication direction yields the total triple Roman values above.

## Limitations
The theorem deliberately excludes parts of size one. Those graphs have universal vertices, and the initiating paper already characterizes the resulting minimum value \(5\). The proof concerns the minimum weight only; it does not enumerate all optimal functions. The literature comparison cannot rule out an older or poorly indexed equivalent statement under unusual terminology, although searches covered the invariant's standard name, abbreviation, complete-bipartite specialization, and complete-multipartite terminology.

## References
1. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera, and M. P. Álvarez-Ruiz, “On the Total Version of Triple Roman Domination in Graphs,” *Mathematics* 13 (2025), 1277. DOI: 10.3390/math13081277.
2. Preprint version 1, posted 17 March 2025: https://www.preprints.org/manuscript/202503.1111.
