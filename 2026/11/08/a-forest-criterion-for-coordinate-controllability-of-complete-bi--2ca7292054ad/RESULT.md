# A forest criterion for coordinate controllability of complete-bipartite subdivision networks

## Finding

For integers \(p,q\ge2\), let \(H_{p,q}=S(K_{p,q})\) denote the simple graph obtained by subdividing every edge of the complete bipartite graph exactly once. It has two kinds of vertices: \(p+q\) *original vertices* and \(pq\) *inserted vertices* indexed by pairs \((i,j)\), \(1\le i\le p\), \(1\le j\le q\). All \(2pq\) edges of \(H_{p,q}\) have unit weight. For any controlled-vertex set \(S\), let \(B_S\) have the distinct corresponding standard-basis columns, and consider the full-state dynamics
\[
\dot z(t)=-L_{H_{p,q}}z(t)+B_Su(t).
\]
Define \(U(S)\subseteq E(K_{p,q})\) to consist exactly of those pairs \((i,j)\) whose inserted vertex is **not** in \(S\). Regard \(U(S)\) as an ordinary bipartite graph on all \(p+q\) original labels, including isolated vertices.

**Complete criterion.** The pair \((-L_{H_{p,q}},B_S)\) is Kalman controllable if and only if both conditions hold:

1. \(U(S)\) is a forest, i.e. contains no undirected cycle;
2. if \(p=q\), then \(S\) contains at least one original vertex. There is no such extra requirement when \(p\ne q\).

In particular, the exact minimum number of independently driven vertex coordinates and the number of labeled minimum-cardinality controlling sets are
\[
M(p,q)=\begin{cases}
(p-1)(q-1),&p\ne q,\\
(p-1)^2+1,&p=q,
\end{cases}
\qquad
N(p,q)=\begin{cases}
p^{q-1}q^{p-1},&p\ne q,\\
2p^{2p-1},&p=q.
\end{cases}
\]
For \(p\ne q\), a minimum set consists precisely of inserted vertices for the edges outside a spanning tree of \(K_{p,q}\). For \(p=q\), a minimum set consists precisely of such inserted vertices together with **any one** original vertex; every spanning tree and every choice of the single original vertex work, including the case \(p=q=2\). In particular, for balanced networks one extra vertex actuator is unavoidable even when the largest eigenvalue multiplicity equals \((p-1)^2\) (for \(p\ge3\)).

More generally, if \(\mathcal F_{p,q}\) is the set of all labeled forests of \(K_{p,q}\), the controlling-set size enumerator is
\[
\sum_{S\text{ controllable}}t^{|S|}
=\begin{cases}
(1+t)^{p+q}\displaystyle\sum_{F\in\mathcal F_{p,q}}t^{pq-|F|},&p\ne q,\\
\big((1+t)^{2p}-1\big)\displaystyle\sum_{F\in\mathcal F_{p,p}}t^{p^2-|F|},&p=q.
\end{cases}
\]
The sets and counts refer to vertex labels, not graph-isomorphism orbits, and count a separate independent input for each controlled vertex.

## Assumptions and scope

The graph is exactly the **once-subdivided, unit-edge, simple** complete bipartite graph, not the original \(K_{p,q}\), its line graph \(K_p\square K_q\), a weighted subdivision, or a general incidence design. The dynamics is continuous-time, linear, full-state Laplacian consensus; an input column is the canonical unit vector of one vertex. Controllability means Kalman controllability over \(\mathbb R\) for arbitrary initial/final full-state vectors in finite positive time. There is no requirement to preserve nonnegativity of the applied inputs, and an original vertex and an inserted vertex are different permitted actuator sites. All quantifiers cover every integer \(p,q\ge2\) and every subset of the \(p+q+pq\) labeled graph vertices.

## Proof

**1. Spectral setup.** Write an eigenvector in blocks \((a,b,y)\), where \(a\in\mathbb R^p\), \(b\in\mathbb R^q\), and \(y\in\mathbb R^{p\times q}\). The equation \(L(a,b,y)=\lambda(a,b,y)\) is equivalent to
\[
(q-\lambda)a_i=\sum_{j=1}^q y_{ij},\quad
(p-\lambda)b_j=\sum_{i=1}^p y_{ij},\quad
(2-\lambda)y_{ij}=a_i+b_j. \tag{1}
\]
For \(\lambda\ne2\), eliminate \(y\). Define
\[
f_d(\lambda)=\lambda^2-(d+2)\lambda+d,\qquad
g(\lambda)=\lambda^2-(p+q+2)\lambda+pq+p+q.
\]
The constant-on-each-part subspace yields the simple eigenvalue \(0\) and the two real roots of \(g\). Contrasts \(\sum_i a_i=0\), \(b=0\) yield the two roots of \(f_q\), each of multiplicity \(p-1\); similarly \(\sum_j b_j=0\), \(a=0\) yield the roots of \(f_p\), each of multiplicity \(q-1\). If \(p=q\), the two contrast families coincide in eigenvalue and form a direct sum of dimension \(2(p-1)\) at each root of \(f_p\). For unequal \(p,q\), all these eigenvalues are distinct: \(f_p-f_q=(q-p)(\lambda-1)\), while \(f_d(1)=-1\), and \(g-f_q=p(q+1-\lambda)\), while \(f_q(q+1)=-1\), with the analogous identity for \(f_p\). The two roots of \(g\) are simple because its discriminant is \((p-q)^2+4\). Every quotient eigenvector has a constant inserted-vertex coordinate; for \(p\ne q\) this coordinate cannot vanish unless the whole eigenvector vanishes. For \(p=q\), the quotient eigenvalue \(\lambda=p\) has the original-only eigenvector \((\mathbf1_p,-\mathbf1_p,0)\), while quotient eigenvalues \(0\) and \(p+2\) have nonzero constant inserted coordinates.

**2. The cycle eigenvectors.** For \(\lambda=2\), equation (1) gives \(a_i+b_j=0\) for all \(i,j\), hence \(a=t\mathbf1_p\), \(b=-t\mathbf1_q\). Summing the other two equations gives \((pq-p-q)t=0\). As \(pq-p-q=(p-1)(q-1)-1\), the only exceptional pair is \((2,2)\). Outside that pair \(t=0\) and the \(\lambda=2\) eigenspace is
\[
\mathcal Z=\{(0,0,y):\sum_j y_{ij}=0\ \forall i,\quad \sum_i y_{ij}=0\ \forall j\},
\]
of dimension \(k=(p-1)(q-1)\). At \((2,2)\), an additional independent original-only eigenvector appears at the same eigenvalue. The space \(\mathcal Z\) is the signed cycle space of \(K_{p,q}\): its elements supported on a subset of inserted vertices are precisely the real circulations supported on that underlying bipartite subgraph. In particular, \(\mathcal Z\) has a nonzero vector supported in \(U(S)\) exactly when \(U(S)\) contains a cycle.

By the PBH eigenvector test for a real symmetric matrix, controllability is equivalent to the absence of any nonzero Laplacian eigenvector that vanishes at all controlled vertices. A cycle in \(U(S)\) therefore prevents controllability, even if all original vertices are controlled. If \(p=q\), the original-only vector \((\mathbf1_p,-\mathbf1_p,0)\) also proves that at least one original vertex must be controlled. This establishes both necessary conditions.

**3. Unbalanced sufficiency at the minimal size.** Assume \(p\ne q\), and let \(T\) be any spanning tree of \(K_{p,q}\). Control exactly the \(k=pq-(p+q-1)\) inserted vertices corresponding to \(E(K_{p,q})\setminus E(T)\). There is no unseen cycle vector by step 2. Each left original vertex other than at most one is incident to at least one controlled pair: otherwise two left vertices and any two right vertices would form a four-cycle in \(T\). The analogous statement holds on the right. For a root of \(f_q\), every inserted coordinate is proportional to its own row contrast \(a_i\), so vanishing on controlled inserted vertices and \(\sum_i a_i=0\) imply \(a=0\). The roots of \(f_p\) are eliminated similarly. Each quotient mode has a nonzero constant inserted coordinate, hence is detected by any controlled inserted vertex. This exhausts the spectrum and proves controllability for \(p\ne q\).

**4. Balanced sufficiency at the minimal size.** Assume \(p=q=n\), let \(T\) be any spanning tree of \(K_{n,n}\), control its complementary \((n-1)^2\) inserted vertices, and also control an arbitrary single original vertex \(v\). The cycle space has no invisible vector by acyclicity of \(T\). The original-only quotient mode is detected by \(v\); the other quotient modes have nonzero inserted coordinates. At \(n=2\), the quotient mode at \(\lambda=2\) coincides with the cycle eigenvalue, but the selected original and inserted coordinates separately annihilate its original and cycle components.

It remains to treat the two contrast eigenspaces. An eigenvector in either of them is determined by \(a_i,b_j\), with \(\sum_i a_i=\sum_j b_j=0\), and its inserted coordinate is \((a_i+b_j)/(2-\lambda)\). Let \(F\) be the bipartite graph consisting of the **controlled inserted pairs**. On each connected component \(C\) of \(F\), equations \(a_i+b_j=0\) force all left values to equal one scalar \(t_C\) and all right values to equal \(-t_C\), with the same convention for isolated vertices. If \(\alpha_C\) and \(\beta_C\) count the two vertex types in \(C\), the sum-zero conditions become
\[
\sum_C\alpha_Ct_C=0,\qquad \sum_C\beta_Ct_C=0. \tag{2}
\]
For \(n\ge3\), any nontrivial component of \(F\) with exactly one left vertex and at least two right vertices would force a four-cycle into the complementary tree \(T\); the same holds with sides swapped. Thus each nontrivial component is either a single edge or has at least two vertices on each side. Because \(|E(F)|=(n-1)^2>n\), the entire \(F\) cannot be a matching; some component has at least two vertices on each side. The complementary-tree acyclicity now forces this component to contain at least \(n-1\) left and at least \(n-1\) right vertices. There are at most two outside vertices, one of each type. Accordingly \(F\) has one of the following component patterns: connected; one isolated left vertex plus a connected remainder; one isolated right vertex plus a connected remainder; one isolated left and one isolated right plus a connected remainder; or two components consisting of one isolated pair edge and a connected remainder. These patterns distinguish the two possible sides for a single isolated vertex.

In the connected and one-isolate cases, equations (2) alone force all \(t_C=0\). In the latter two cases, their nullspace is one-dimensional and every nonzero solution has every component scalar nonzero: for the separate isolated vertices the ratios are \((-n+1,-n+1,1)\), and for the isolated pair edge they are \((-(n-1),1)\), after normalization. Since \(v\) lies in one of the components, the controlled original coordinate forces its component scalar to vanish, which kills the remaining solution. For \(n=2\), \(F\) has one edge and two isolated original-label vertices; equations (2) give the same all-components-nonzero one-dimensional obstruction, eliminated by any one original actuator. Thus every contrast mode is detected for all \(n\ge2\).

**5. From spanning trees to forests, and counting.** If \(U(S)\) is a forest in \(K_{p,q}\), it extends to a spanning tree \(T\). Hence \(S\) contains the controlling inserted-vertex complement of \(T\), together with an original vertex if balanced. Adding input columns cannot destroy controllability. Combined with step 2, this proves the full if-and-only-if criterion. The cycle space has dimension \(k\), so at least \(k\) inserted vertices must be controlled. In the unbalanced case the spanning-tree construction attains that bound. In the balanced case the original-only mode forces an additional original actuator, and the construction attains \(k+1\). At equality the unactuated pairs have \(p+q-1\) edges and are a forest, thus a spanning tree. The matrix-tree theorem gives exactly \(\tau(K_{p,q})=p^{q-1}q^{p-1}\) labeled spanning trees; multiplying by \(2p\) choices of a single original vertex in the balanced case gives the displayed counts. The size enumerator follows by independently choosing any original vertices subject to the balanced nonempty requirement, and choosing a forest of unactuated inserted vertices.

## Verification

The accompanying `verify.py` uses only the Python standard library. It constructs the exact integer Laplacian, tests finite-field Kalman/Krylov ranks modulo \(1000000007\), enumerates spanning-tree complements, and compares these independent rank outcomes to the stated forest/original-vertex criterion. Running `python3 verify.py` gave `VERIFIED 734`, including all \(256\) actuator choices for \((p,q)=(2,2)\), sampled general actuator choices, and selected spanning-tree complements for \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). The tree counts were separately enumerated exhaustively in those six cases: respectively \(4,12,32,81,432,4096\). The critical infinite statements rest on the analytic eigenvector proof; a modular rank computation can have exceptional primes and is only a supplementary finite check.

## Relationship to prior work

The PBH condition and general multiplicity-based controllability theory are classical; Yuan et al. (2013) explicitly discuss geometric eigenvalue multiplicities and driver-selection algorithms for general networks. The theorem here does not claim that PBH or the cycle-space dimension is novel. It instead classifies **every node-local coordinate input set** in the specific once-subdivided complete bipartite family, with a sharp balanced/unbalanced distinction and exact counts. In particular, the need for both cycle-space-actuating inserted vertices and an original-vertex actuator at equal part sizes is not supplied by an eigenvalue-multiplicity number alone.

The line/rook graph \(K_p\square K_q\) has the same \(pq\) edge labels but is a different dynamical graph from \(S(K_{p,q})\): it has no \(p+q\) original state coordinates. Coincidence of cycle-space counting arguments is not an equivalence of the two PBH problems. Mousavi–Haeri–Mesbahi's cograph controllability theorem applies to \(P_4\)-free graphs, whereas the subdivision graph here has induced \(P_4\) paths. Dai's leader-selection study develops graphical tests and exact results for self-similar scale-free networks and Cayley trees; those are different families. These are substantive comparisons of domains and conclusions, not a claim that a failed search proves publication priority.

## Limitations

The statement does not cover generic weighted subdivision graphs, directed systems, dynamics based on the adjacency matrix instead of the combinatorial Laplacian, shared/broadcast controls, bounded-sign inputs, structured uncertainty, or energy-optimal control. It is not a claim about minimal arbitrary dense input matrices; an actuator here is exactly one independently driven vertex coordinate. An independent audit and exhaustive publication-priority review have not been performed. General incidence-graph controllability literature may contain equivalent formulations not found among the accessible sources.

## References

1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications 4, 2447 (published 12 September 2013), https://doi.org/10.1038/ncomms3447 ; authorized full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/ .
2. S. S. Mousavi, M. Haeri, and M. Mesbahi, *Laplacian Dynamics on Cographs: Controllability Analysis Through Joins and Unions*, arXiv:1802.03599 (first posted 10 February 2018), https://arxiv.org/abs/1802.03599 .
3. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications 17 (2023), 505–515 (first published 29 October 2022), https://doi.org/10.1049/cth2.12385 .
4. S. Zhang, M. K. Camlibel, and M. Cao, *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies*, CDC/ECC 2011, pp. 759–764, https://doi.org/10.1109/CDC.2011.6160658 . Only publisher abstract/metadata were accessible in this review.
