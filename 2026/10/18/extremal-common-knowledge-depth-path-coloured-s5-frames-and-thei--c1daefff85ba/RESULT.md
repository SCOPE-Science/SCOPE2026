# Extremal common-knowledge depth: path-coloured S5 frames and their exact census

## Finding

For integers \(n\ge1\) and \(k\ge2\), consider all tuples of \(k\) labelled equivalence relations on the labelled set of \(n\) worlds. Their classical common-knowledge operator is uniformly captured by its finite unfolding after at most \(n-1\) steps, and this worst-case cutoff has a complete exact census.

Write \(E_i\) for the knowledge relation of agent \(i\), and let \(C_0\varphi=\varphi\) and \(C_{t+1}\varphi=\varphi\wedge\bigwedge_{i=1}^k K_iC_t\varphi\). Interpret \(C\varphi\) as truth of \(\varphi\) on every world reachable by a finite chain of agent steps. Define the *uniform unfolding depth* \(h(E_1,\ldots,E_k)\) as the smallest nonnegative \(t\) for which \(C_t\varphi\leftrightarrow C\varphi\) is true at every world for every valuation and every formula \(\varphi\).

Let \(G\) be the undirected simple graph connecting distinct worlds related by at least one agent. The exact depth is the maximum graph diameter over connected components of \(G\), taking singleton diameter to be zero. Consequently \(0\le h\le n-1\). For \(n\ge2\), equality holds if and only if \(G\) is a spanning path.

Every frame of maximal depth is specified uniquely by: (i) an undirected Hamiltonian path on the labelled worlds, canonically oriented from the smaller-labelled endpoint; and (ii) for each of its \(n-1\) successive edges, a **nonempty** set \(S_j\subseteq\{1,\ldots,k\}\) of agents, with the adjacency rule \(S_j\cap S_{j+1}=\varnothing\), reading edges from the smaller-labelled endpoint. Agent \(i\) has exactly the two-element equivalence classes corresponding to edges containing \(i\), with all other worlds in singleton classes.

Let \(H_{n,k}\) be the number of these labelled, agent-labelled maximal-depth frames. Then

\[
H_{1,k}=1,\qquad H_{2,k}=2^k-1.
\]

For \(n\ge3\), set \(u_s=\binom{k}{s}\), \(1\le s\le k-1\), and define the \((k-1)\)-square matrix

\[
B_{s,t}=\begin{cases}\binom{k-s}{t},&t\le k-s,\\0,&t>k-s,\end{cases}\quad 1\le s,t\le k-1.
\]

With \(\mathbf 1\) the all-ones column,

\[
\boxed{H_{n,k}=\frac{n!}{2}\,u^{\mathsf T}B^{n-2}\mathbf 1.}
\]

In particular \(H_{n,2}=n!\) for every \(n\ge3\). For each fixed \(k\ge3\), the strictly positive matrix \(B^2\) has a Perron eigenvalue \(\lambda_k^2\), and the number of extremal frames obeys \(H_{n,k}=\Theta_k(n!\lambda_k^n)\). At \(k=3\), \(\lambda_3=1+\sqrt2\). The first values \(H_{n,3}\) for \(n=1,\ldots,6\) are \(1,7,36,360,4320,62640\).

## Assumptions and scope

The world set is finite and nonempty. The \(k\) agents are distinct and labelled; every individual accessibility relation is an equivalence relation, including its diagonal. Repeated relations between distinct agents are permitted. Worlds are labelled, and isomorphic frames are counted separately. The Boolean propositional valuation is arbitrary. No connectivity hypothesis is imposed in defining \(h\); the theorem itself characterizes equality in the upper bound. The truth conditions are **classical S5**, equivalently the discrete-order subclass of intuitionistic S5. The statements do not assert the same cutoff on arbitrary non-discrete intuitionistic preorders.

## Proof

**1. Exact semantic radius.** Fix a valuation and a formula \(\varphi\), and denote its truth set by \(S\subseteq W\). Induction on \(t\) proves that \(C_t\varphi\) is true at \(w\) exactly when \(S\) contains every vertex of graph distance at most \(t\) from \(w\). For \(t=0\) this is the definition. At stage \(t+1\), the conjunct \(\varphi\) tests \(w\) itself, and \(K_iC_t\varphi\) tests radius-\(t\) neighborhoods at every \(E_i\)-successor. These are exactly the radius-\(t+1\) neighborhood, including all shorter paths. By the reachability semantics, \(C\varphi\) is true exactly when \(S\) contains the entire connected component of \(w\). Therefore the maximum component diameter suffices for all formulae and valuations. It is also necessary: take a vertex \(w\) with a vertex \(v\) at maximum distance \(d\), assign a fresh atom \(p\) true at every world except \(v\), and obtain \(C_{d-1}p\) true at \(w\) while \(Cp\) is false there. For \(d=0\), zero steps suffice. Thus \(h=d\) exactly.

**2. Maximal diameter.** Any connected component of size \(r\) has diameter at most \(r-1\), hence \(h\le n-1\). If \(h=n-1\) with \(n\ge2\), two worlds are joined by a shortest path of length \(n-1\). This path uses all \(n\) worlds. An edge between nonconsecutive vertices would shorten the endpoint-to-endpoint distance, a contradiction. Thus the entire union graph is precisely the spanning path. Conversely its diameter is \(n-1\).

**3. Equivalence relations on a path.** If \(G\) is a path, any nonsingleton class of an \(E_i\) is a clique in \(G\); a path contains no clique of three vertices. Hence the nonsingleton \(E_i\)-classes are disjoint pairs of adjacent worlds, and the set of path edges belonging to each \(E_i\) is a matching. Label edge \(j\) by the set \(S_j\) of agents that identify its endpoints. Coverage of the union graph makes every \(S_j\) nonempty. The matching condition is exactly \(S_j\cap S_{j+1}=\varnothing\). Conversely, any such nonempty disjoint-consecutive subset word defines for each agent a matching of edges; declaring each matched pair an equivalence class and leaving the other vertices singleton yields an equivalence relation. Their union is exactly the prescribed path. The construction is inverse in both directions, and no parameter choice is counted twice.

**4. Exact enumeration.** There are \(n!/2\) undirected paths on \(n\ge2\) labelled vertices. Orient each uniquely from its smaller-labelled endpoint to index the edges without double counting. For \(n=2\), its one edge permits any of the \(2^k-1\) nonempty agent subsets. For \(n\ge3\), the first edge may have any \(s\)-element agent subset in \(\binom{k}{s}\) ways, with \(1\le s\le k-1\). After a subset of size \(s\), the next subset of size \(t\) must be chosen from the \(k-s\) remaining agents, in \(\binom{k-s}{t}\) ways. Thus the number of admissible words of length \(n-1\) is \(u^{\mathsf T}B^{n-2}\mathbf 1\). Multiplying by \(n!/2\) proves the formula. For \(k=2\), the only admissible long words alternate the two singleton colors, so their number is two.

**5. Fixed-agent asymptotic.** For \(k\ge3\), every size state \(s\in\{1,\ldots,k-1\}\) can transition to state one, and state one can transition to any allowed size \(t\). Therefore every entry of \(B^2\) is positive. The Perron–Frobenius theorem gives a simple dominant positive eigenvalue \(\lambda_k\) of \(B\) and strictly positive associated left/right eigenvectors; its contribution to the positive scalar \(u^{\mathsf T}B^{n-2}\mathbf1\) has a strictly positive coefficient. The exact estimate follows. For \(k=3\), \(B=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)\), so \(\lambda_3=1+\sqrt2\). This completes the proof.

## Verification

The accompanying self-contained standard-library program `checker.py` generates every set partition on the labelled carrier for small sizes, forms all tuples of the corresponding equivalence relations, computes maximum component diameters from breadth-first search, tests the spanning-path and disjoint-edge-color characterizations, and compares the exhaustive counts with the transfer formula. It checks all \(7108\) tuples across \((n,k)=(1,2),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(2,4),(3,4)\). It separately tests \(234098\) finite-approximant truth-set steps from the stated recursion, and directly counts admissible disjoint-subset words for \(18\) parameter pairs. The checker passed. These are finite consistency checks; the proofs above establish all \(n,k\).

## Relationship to prior work

The accessibility semantics of individual knowledge and common knowledge, and the classical S5 specialization of an intuitionistic system, are standard. Zenger's 2026 *Intuitionistic Common Knowledge*, especially Definitions 2.6, 4.1, 4.2 and 4.9 and Lemma 4.11, sets out this semantic framework and the connection between classical and intuitionistic S5, while concentrating on axiomatizations, cyclic proofs, finite-model properties and decision complexity. The common-knowledge-as-reachability fact, and elementary graph diameter bound, are prior context, **not** claimed new here. The result is the complete structural description of **all** finite S5 frames attaining the maximum uniform unfolding depth together with their exact labelled enumeration and fixed-agent asymptotic growth. Related published work on proper S5 bounded-morphic covers concerns replication and quotient maps rather than finite common-knowledge unfolding maxima.

## Limitations

The theorem treats labelled classical S5 frames and does not enumerate isomorphism classes, arbitrary intuitionistic S5 partial-order frames, or other epistemic modalities. It describes exactly the maximal-depth stratum, not a census of every possible intermediate depth. No independence or external validation is claimed. A logically equivalent enumeration under a different combinatorial name may exist outside the inspected literature; the finite program does not establish originality.

## References

1. Lukas Zenger, *Intuitionistic Common Knowledge*, arXiv:2605.00523, first posted 1 May 2026; especially Sections 2.2 and 4.1–4.2. https://arxiv.org/html/2605.00523v1
2. *Common Knowledge*, Stanford Encyclopedia of Philosophy, first published 2001, revised 2022. https://plato.stanford.edu/entries/common-knowledge/
