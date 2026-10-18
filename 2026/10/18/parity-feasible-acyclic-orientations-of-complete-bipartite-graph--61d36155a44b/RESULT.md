# Parity-feasible acyclic orientations of complete bipartite graphs and exact two-row fibres

## Finding
Let \(a,b\ge1\), let \(G=K_{a,b}\) have labelled partite sets \(A,B\), and prescribe \(p:V(G)\to\{0,1\}\). An orientation realizes \(p\) if the indegree of every vertex is congruent to its prescribed bit modulo two. **An acyclic orientation realizing \(p\) exists if and only if**
\[
 \sum_{v\in V(G)}p(v)\equiv ab\pmod2
 \quad\text{and}\quad p\not\equiv1.
\]
Thus among parity-feasible signatures there is exactly one missing signature when \(a,b\) are both even (the all-odd signature), and none otherwise.

More sharply, for the labelled two-row graph \(K_{2,b}\), with \(b\ge2\), let \(t\) be the number of prescribed odd-indegree vertices in its \(b\)-vertex part. Let \(u,v\in\{0,1\}\) denote the prescribed bits on the two-vertex part, necessarily satisfying \(u+v+t\equiv0\pmod2\). The **exact number** \(N_b(u,v;t)\) of acyclic orientations with this prescribed signature is
\[
N_b(u,v;t)=\begin{cases}
 2^{b-1},&t=0,\\
 2^{b-t},&1\le t<b,\\
 2,&t=b\text{ even and }(u,v)=(0,0),\\
 0,&t=b\text{ even and }(u,v)=(1,1),\\
 1,&t=b\text{ odd}.
\end{cases}
\]
The count depends on the larger-side signature only through \(t\). Each formula counts labelled edge orientations (not topological orders). The zero in the fourth case is the unique feasible obstruction.

## Assumptions and scope
Graphs are finite, simple, undirected before orienting, with two *nonempty* distinguished labelled partite sets, and every cross-edge present. The parity of indegree is computed modulo two; sources have indegree zero. A signature is globally parity-feasible when its bit sum is congruent to the number of edges. Two orientations differing on any labelled edge are distinct. The exact counting subtheorem assumes the first side has two distinct labelled vertices and \(b\ge2\).

## Proof
**Necessity.** The sum of indegrees of any orientation equals the edge count \(ab\), giving the global congruence. Every finite acyclic digraph has a source. Such a vertex has indegree parity zero, so the all-one signature is forbidden.

**Sufficiency, by induction on \(a+b\).** If \(a=1\) or \(b=1\), we have a star. Every leaf's parity determines the direction of its unique edge. The central parity is then forced by the global congruence, producing the required acyclic orientation. Suppose now \(a,b\ge2\), and take a globally feasible signature containing a zero. If there is a zero at \(x\in A\), temporarily make \(x\) a source: direct all \(b\) edges \(x\to B\), delete \(x\), retain the bits on \(A\setminus\{x\}\), and toggle the bits on every vertex of \(B\). Call this residual signature \(p'\) on \(K_{a-1,b}\). It is globally feasible, because both its bit sum and its edge count differ from their original values by \(b\) modulo two.

If \(p'\) is not all one, the inductive hypothesis orients the smaller biclique acyclically; adding \(x\) as a source completes the construction. The only way that \(p'\) can be all one is that \(x\) was the **only** zero in \(A\) and **every** vertex of \(B\) originally had bit zero. In that exceptional configuration, choose any \(y\in B\) as a source instead. Its deletion toggles every bit on \(A\) but leaves the other bits on \(B\) unchanged. Since \(a\ge2\), at least \(a-1\) of the originally odd vertices of \(A\) now have bit zero; the new signature is globally feasible and not all one. The induction applies. If the original signature has no zero in \(A\), it has a zero in \(B\). Choosing such a vertex as source and toggling \(A\) turns **every** bit in \(A\) to zero; induction again applies. The deleted source has no incoming edges and cannot create a directed cycle, so the final orientation is acyclic. This also gives a constructive polynomial-time procedure.

**Two-row enumeration.** Name the two vertices in \(A\) by \(x,y\), and write for each \(z\in B\) a column \((\alpha_z,\beta_z)\in\{0,1\}^2\), where a bit is one precisely when its corresponding edge points from \(A\) to \(z\). The prescribed parity at \(z\) is \(\alpha_z+\beta_z\pmod2\). An orientation of \(K_{2,b}\) is acyclic if and only if its columns do **not** simultaneously include \((1,0)\) and \((0,1)\): their coexistence creates a directed four-cycle; conversely, every simple directed cycle in \(K_{2,b}\) alternates between the two parts and therefore, since the first part has only two vertices, has length four; its two columns must be conflicting.

Consequently every odd-parity column must have the same mixed type \((1,0)\) or \((0,1)\), while each even-parity column can freely be \((0,0)\) or \((1,1)\). Let \(h\) count columns of type \((1,1)\), and let \(t\) count odd columns. For mixed type \((1,0)\), the parities on \(x,y\) are \((b-h-t,b-h)\pmod2\); for type \((0,1)\), they are reversed.

If \(t=0\), there are \(b\) even columns and exactly \(2^{b-1}\) ways to give \(h\) either prescribed parity (the global congruence ensures \(u=v\)). For \(1\le t<b\), there are two choices of the uniform mixed type; for each, exactly half of the \(2^{b-t}\) assignments to the remaining even columns give the required parity of \(h\). Their sum is \(2^{b-t}\). Finally, when \(t=b\), one has \(h=0\); if \(b\) is even, both mixed choices give \((u,v)=(0,0)\), while if \(b\) is odd, they give the two different signatures \((0,1)\) and \((1,0)\). This establishes all five cases, with no orientation counted twice.

## Verification
The standalone `verify.py` enumerates every literal edge orientation of \(K_{a,b}\) for the 21 graph orders \(1\le a\le4\), \(a\le b\le8\), \(ab\le20\). It tests global parity, acyclicity via a literal directed graph and Kahn topological sort, the complete existence classification, and all two-row fibre formulas, for 2,390 feasible signature comparisons. The run prints `VERIFY_OK`. The topological-sort checker does not use the column characterization or constructive induction. These finite checks support, but do not establish, the universal statements.

## Relationship to prior work
Gravier, Petiteau and Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem* (first submitted 2026-03-10, arXiv:2603.09475v1), study precisely the general prescribed-indegree-parity problem and necessary source/sink/global constraints, emphasizing Cartesian products of paths and cycles. The complete bipartite all-signature classification and two-row parity-fibre formula above do not appear in the inspected manuscript. Carballosa, Khera and Reyes (arXiv:2303.09021v2) count complete multipartite acyclic orientations without fixing indegree parities. Cameron, Glass, Rekvényi and Schumacher (arXiv:1412.3685v3) identify the total biclique orientation count with poly-Bernoulli numbers; the two-row distribution refines that total rather than claiming it anew. The local obstruction at a source and total orientation counts are prior principles, not novelty claims.

## Limitations
The classification does **not** give exact fibre counts for arbitrary \(a,b\); those counts remain outside this theorem. It requires nonempty parts and does not treat partially directed edges. The mathematical review is not independent, and bibliographic priority beyond the specifically examined sources and searches remains uncertain. Direct checking of finitely many instances is not a proof of an infinite claim.

## References
1. S. Gravier, M. Petiteau, I. Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475v1 (2026-03-10), https://arxiv.org/pdf/2603.09475.
2. W. Carballosa, J. Khera, F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021v2 (2025), https://arxiv.org/pdf/2303.09021.
3. P. J. Cameron, C. A. Glass, K. Rekvényi, R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685v3 (2022), https://arxiv.org/pdf/1412.3685.
