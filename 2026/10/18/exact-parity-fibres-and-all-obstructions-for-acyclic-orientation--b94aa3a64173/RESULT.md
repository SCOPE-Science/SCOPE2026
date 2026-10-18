# Exact parity fibres and all obstructions for acyclic orientations of fan graphs

## Finding

Let \(n\ge2\), and let the labelled fan graph be \(F_n=K_1\vee P_n\), where the path has ordered vertices \(v_0,\ldots,v_{n-1}\) and its universal neighbour is \(h\). Prescribe indegree parities \(p_i\in\{0,1\}\) at \(v_i\), and \(q\in\{0,1\}\) at \(h\). Write \(A_n(\mathbf p,q)\) for the number of acyclic orientations realizing this exact signature.

**Theorem.** If \(q+\sum_{i=0}^{n-1}p_i\not\equiv1\pmod2\), there is no realizing orientation. Otherwise, exactly \(2^{n-1}\) orientations realize the prescribed signature before the acyclicity requirement. Of these, \(A_n(\mathbf p,q)\) are acyclic, and this exact number is computable by the four-state transfer recurrence below in \(O(n)\) arithmetic operations. Moreover,

\[
A_n(\mathbf p,q)=0\quad\Longleftrightarrow\quad
\begin{cases}
n\text{ is even},\\
p_0=p_{n-1}=1,\\
p_{2j-1}=p_{2j}\quad(1\le j\le n/2-1).
\end{cases}
\]

The displayed equivalence is asserted only for signatures satisfying the preceding global parity congruence. Every obstructed signature automatically has \(q=1\). Consequently, every feasible signature is acyclically realizable when \(n\) is odd; for even \(n\), exactly \(2^{n/2-1}\) of the \(2^n\) globally feasible signatures lack an acyclic realization.

The full multiplicity is obtained as follows. For binary \(s,z\), initialize \(D_0(0,1)=D_0(1,1)=1\) and all other \(D_0\)-entries to zero. For each \(0\le i\le n-2\), initialize \(D_{i+1}\) to zero and, for every state \((s,z)\) with weight \(D_i(s,z)\), set \(e=p_i\oplus s\oplus z\), where \(\oplus\) is addition modulo two. Add \(D_i(s,z)\) to \(D_{i+1}(s,e)\). If \(e\ne s\), additionally add that weight to \(D_{i+1}(1-s,e)\). Then

\[
A_n(\mathbf p,q)=\sum_{\substack{s,z\in\{0,1\}\\s\oplus z=p_{n-1}}}D_{n-1}(s,z).
\]

The calculation does not need \(q\) after verifying the global parity condition. All counts refer to orientations of the labelled edges, not linear extensions or topological orders.

## Assumptions and scope

All graphs are finite, simple and undirected before orientation. The fan has \(n+1\) labelled vertices and \(2n-1\) edges. Each edge receives one direction; an acyclic orientation is one with no directed cycle. The parity at each vertex is the indegree reduced modulo two. The result holds for all integers \(n\ge2\), all \(2^{n+1}\) binary vertex signatures (with the global-congruence exclusion), and exact integer arithmetic.

For a path edge \(v_iv_{i+1}\), let \(e_i=0\) when directed \(v_i\to v_{i+1}\) and \(e_i=1\) when reversed. For a spoke \(hv_i\), let \(s_i=0\) when directed \(h\to v_i\) and \(s_i=1\) otherwise. Use only the formal boundary bits \(e_{-1}=1\) and \(e_{n-1}=0\), representing nonexistent path edges, in parity identities. No extra graph edges are introduced.

## Proof

**1. Global congruence and unrestricted parity fibres.** Summing all indegrees counts every edge once; therefore the parity sum of the complete signature is \(2n-1\equiv1\pmod2\). At each path vertex direct counting gives

\[
p_i=s_i\oplus e_{i-1}\oplus e_i
\qquad(0\le i<n).
\]

Indeed the spoke contributes \(1-s_i\), the previous path edge (when present) contributes \(1-e_{i-1}\), and the next edge (when present) contributes \(e_i\); the chosen formal boundary values make the identity valid also at both ends. Arbitrarily choose the \(n-1\) actual path-edge bits \(e_0,\ldots,e_{n-2}\). The displayed identity uniquely determines all \(n\) spoke bits, and the parity at the hub is then forced by the global congruence. Thus each globally feasible signature is realized by exactly \(2^{n-1}\) orientations, while an infeasible signature is never realized.

**2. Detecting directed cycles.** The fan is chordal: any cycle of length at least four contains the hub and has a chord from the hub to an internal path vertex. In any orientation of a chordal graph, choose a shortest directed cycle. If it had a chord, orienting that chord one way or the other would close one of the two directed paths into a shorter directed cycle. Therefore every directed cycle in a fan contains a directed triangle. Its triangles are exactly \(h,v_i,v_{i+1}\) for \(0\le i<n-1\).

For a triangle \(h,v_i,v_{i+1}\), a directed three-cycle occurs precisely when either \((s_i,e_i,s_{i+1})=(0,0,1)\) or \((1,1,0)\). Thus, given \(s_i\) and \(e_i\), the next spoke bit \(s_{i+1}\) may equal \(s_i\) unconditionally, and it may switch to \(1-s_i\) exactly when \(e_i\ne s_i\). This condition is necessary and sufficient for global acyclicity.

**3. Four-state exact recurrence.** A state just before processing \(v_i\) consists of its spoke bit \(s_i=s\) and its preceding path bit \(e_{i-1}=z\). The parity identity uniquely forces \(e_i=p_i\oplus s\oplus z\). The preceding triangle criterion then gives exactly the one or two next-state choices specified in the theorem. At \(i=0\), either spoke direction is possible with formal previous bit \(1\); at \(i=n-1\), the terminal parity identity with formal next bit \(0\) is \(p_{n-1}=s_{n-1}\oplus e_{n-2}\). Every eligible state path determines exactly one orientation and vice versa, proving the transfer count and \(O(n)\) arithmetic complexity.

**4. All zero-count signatures.** For existence rather than multiplicity, keep only the support of nonzero transfer states. Write

\[
\begin{aligned}
U&=\{(0,0),(0,1),(1,0),(1,1)\},\\
A&=\{(0,0),(1,1)\},\\
B&=\{(0,0),(1,0)\},\\
C&=\{(0,1),(1,1)\}.
\end{aligned}
\]

The initial support is \(C\). Applying the transitions of part 3 gives the entire exact subset-automaton table:

| Current support | Next input \(0\) | Next input \(1\) |
|:--|:--|:--|
| \(C\) | \(U\) | \(A\) |
| \(A\) | \(B\) | \(C\) |
| \(B\) | \(A\) | \(U\) |
| \(U\) | \(U\) | \(U\) |

In particular, after an odd number of inputs the support is \(A\) or \(U\), and after a positive even number it is \(B\), \(C\) or \(U\). The support \(A\) occurs at an odd step precisely when the first processed parity is \(1\) and each subsequent completed consecutive pair of processed parities is equal: from \(A\) either \(00\) or \(11\) returns to \(A\), while \(01\) or \(10\) enters the absorbing full support \(U\).

The terminal parity of a state \((s,z)\) is \(s\oplus z\). Both values occur in \(B\), \(C\) and \(U\), whereas only \(0\) occurs in \(A\). If \(n\) is odd, the \(n-1\) processed inputs are even in number and every terminal parity is possible. If \(n\) is even, a terminal parity is impossible exactly when the support is \(A\) and \(p_{n-1}=1\). Rewriting the exact return-to-\(A\) condition gives \(p_0=p_{n-1}=1\) and \(p_{2j-1}=p_{2j}\) for all \(1\le j\le n/2-1\). This includes \(n=2\), where there are no internal paired constraints. Each of the \(n/2-1\) equal pairs can have either common value, giving exactly \(2^{n/2-1}\) forbidden globally feasible signatures. The hub bit of every such signature equals one by the global congruence. This proves the theorem.

**5. Unconstrained-across-signatures check.** The total number of acyclic orientations of \(F_n\), summing the positive parity fibres, is \(2\cdot3^{n-1}\). For \(n=1\), the fan is a single edge with two acyclic orientations. Adding the last path vertex to an acyclic orientation of \(F_{n-1}\) attaches it to two adjacent old vertices. Exactly three of the four edge-direction choices avoid a directed triangle, and the chordal argument shows these choices remain acyclic. Induction gives the stated total. This classical type of total-orientation count is included as an independent consistency check, not the novel assertion.

## Verification

Run `python3 verify.py` in the directory containing this document. The standard-library program constructs each orientation as a literal directed graph, computes indegree parities directly, and determines acyclicity independently by topological deletion; it does not use the directed-triangle test to decide acyclicity. For every \(2\le n\le10\) it checks all \(2^{2n-1}\) edge orientations against the four-state recurrence, verifies every feasible signature has \(2^{n-1}\) unrestricted orientations, and checks the exact forbidden-signature criterion. In total these runs inspect \(699{,}048\) literal edge orientations and compare \(2{,}044\) feasible parity fibres. Additional transfer-only checks cover every signature for \(11\le n\le16\). The independent exhaustive tests are finite checks and are not substituted for the unrestricted proof above.

## Relationship to prior work

Gravier, Petiteau and Sivignon (arXiv:2603.09475v1, March 10, 2026) formulate acyclic orientations with prescribed indegree parity, give general necessary-condition frameworks, and characterize Cartesian grids, cylinders and large tori. Their source/sink framework and elimination formulation address the existence problem, but the inspected main results do not state the fan-specific adjacent-pair obstruction or count every fan parity fibre. The proof here uses a different direct orientation transfer on a chordal graph whose maximal cliques are overlapping triangles. The general parity-feasibility congruence and the \(n=2\) complete-graph base case predate this theorem; neither is claimed separately as novel.

The classical identification of total acyclic orientations with evaluations of the chromatic polynomial (Stanley, 1973) implies the total count but does not refine it by indegree parity. Cardinal, Hoang, Merino, Mička and Mütze (arXiv:2212.03915) study generation of acyclic orientations of chordal graphs, not the present prescribed-vertex-parity fibres. An existing formula for prescribed indegree parities of a wheel \(K_1\vee C_n\) addresses a different graph, which includes an additional rim edge and has different parity and directed-cycle conditions. Removing that edge does not preserve the wheel parity fibres or provide the fan obstruction criterion as a specialization.

## Limitations

Only simple fan graphs \(K_1\vee P_n\), with \(n\ge2\), are covered. The theorem does not classify prescribed-parity acyclic orientations of arbitrary 2-trees, chordal graphs, or cones over general trees. The four-state recurrence counts orientations, not their topological sorts. Finite tests are corroboration only. Bibliographic novelty is based on the specified inspected works, targeted literature queries, and mathematical-record overlap comparisons; differently named or inaccessible prior results may exist, and no independent review has occurred.

## References

1. Sylvain Gravier, Matthieu Petiteau and Isabelle Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475v1, publicly posted 2026-03-10. https://arxiv.org/abs/2603.09475 ; https://arxiv.org/pdf/2603.09475 .
2. Richard P. Stanley, *Acyclic orientations of graphs*, Discrete Mathematics 5 (1973), 171–178. https://doi.org/10.1016/0012-365X(73)90108-8 .
3. Jean Cardinal, Hung P. Hoang, Arturo Merino, Ondřej Mička and Torsten Mütze, *Combinatorial generation via permutation languages. V. Acyclic orientations*, arXiv:2212.03915 (2022). https://arxiv.org/abs/2212.03915 .
