# Prime-characteristic entanglement of line-graph qudit states from signed component overlaps

## Finding

Let \(G=(V,E)\) be any finite undirected simple graph, with \(|V|=n\), and let \(E=A\sqcup B\) be an arbitrary partition of its edges. Put one prime-dimensional qudit at each vertex of the line graph \(L(G)\), prepare the pure unit-weight graph state, and separate the qudits indexed by \(A\) from those indexed by \(B\). The two parts may be empty.

For a prime \(p\), construct a vector family \(\mathcal T_{A,p}\subseteq\mathbb F_p^V\) from the spanning subgraph \((V,A)\). In characteristic two, assign the all-one indicator vector to *every* connected component, including isolated vertices. In odd characteristic, assign an alternating \(+1,-1\) indicator vector to *each bipartite* connected component, including isolated vertices, and no vector to any nonbipartite component. Choose either bipartite coloring for each eligible component. Define \(\mathcal T_{B,p}\) analogously. Let \(T_A,T_B\) have these vectors as columns, let \(q_A,q_B\) be the column counts, and form the signed component-overlap matrix

\[
P_p=T_A^{\mathsf T}T_B\quad\text{over }\mathbb F_p.
\]

Then the exact base-\(p\) entanglement entropy across the edge partition is

\[
\boxed{d_p(G;A,B)=n-q_A-q_B+\operatorname{rank}_{\mathbb F_p}(P_p).}
\]

More strongly, the reduced density matrix has exactly \(p^{d_p}\) nonzero eigenvalues, each \(p^{-d_p}\), and all remaining eigenvalues vanish. Thus every positive-order Rényi entropy and the von Neumann entropy equal \(d_p\) in base-\(p\) units. Changing component colorings changes some row or column signs of \(P_p\), not its rank. The formula applies to disconnected graphs, empty parts, and components with odd cycles.

A characteristic-dependent family illustrates that the formula is not merely a cut-rank upper bound. For \(n\ge5\), take \(G=K_n\) and let \(A\) consist of the \(n-1\) consecutive edges of a spanning Hamilton path; let \(B\) contain all other edges. Then

\[
\boxed{d_p(K_n;A,B)=\begin{cases}
n-2,&p=2\ \text{and }n\text{ even},\\
n-1,&\text{otherwise}.
\end{cases}}
\]

Hence for even \(n\ge6\) the path-edge qubit subsystem has a one-bit rank deficit, whereas for every odd prime the corresponding path-edge qudit subsystem is *exactly maximally mixed*. This statement compares normalized entropies in their own base-\(p\) units; it does not equate entropies in physical bits across unequal local dimensions.

## Assumptions and scope

All graphs are finite, simple, loopless and undirected. The line graph has one vertex per base edge and an unweighted edge between two distinct base edges precisely when they share an endpoint. The dimension \(p\) is prime, and the pure graph state is prepared by applying one unit-weight generalized controlled-phase gate to each line-graph edge starting from \(|+\rangle^{\otimes |E|}\), where \(|+\rangle=p^{-1/2}\sum_{j\in\mathbb F_p}|j\rangle\). No geometry, connectedness, regularity, bipartiteness, or nonemptiness condition is imposed on \(G,A,B\).

For finite \(|E|\), the graph state is equivalently

\[
|\psi\rangle=p^{-|E|/2}\sum_{z\in\mathbb F_p^E}\omega^{\sum_{\{e,f\}\in E(L(G))}z_ez_f}|z\rangle,\qquad\omega=e^{2\pi i/p}.
\]

The reduced state is obtained by tracing out the qudits in \(B\). This is a single fixed pure state and bipartition, not a claim of absolute maximal entanglement across all cuts.

## Proof

**Step 1: The cut matrix and complete quantum spectrum.** Let \(U_A\) and \(U_B\) be the unsigned vertex-by-edge incidence matrices of the spanning subgraphs \((V,A)\) and \((V,B)\), viewed over \(\mathbb F_p\). Their columns have a \(1\) at each of their two endpoints. Since \(G\) is simple and no edge belongs to both parts, a base edge in \(A\) and a base edge in \(B\) share either zero or one endpoint. Therefore the line-graph cut-adjacency matrix is **exactly**

\[
C=U_A^{\mathsf T}U_B\pmod p.
\]

Internal graph-state phases from edges entirely in \(A\) or entirely in \(B\) are local diagonal unitaries and do not affect the Schmidt spectrum. After removing them, the normalized amplitude at \((x,y)\in\mathbb F_p^A\times\mathbb F_p^B\) is \(p^{-|E|/2}\omega^{x^{\mathsf T}Cy}\). For \(x,x'\in\mathbb F_p^A\), character orthogonality gives the reduced-state matrix entry

\[
\rho_A(x,x')=p^{-|A|}\,\mathbf1_{\{C^{\mathsf T}(x-x')=0\}}.
\]

The index set splits into \(p^r\) cosets of the kernel of \(C^{\mathsf T}\), where \(r=\operatorname{rank}_{\mathbb F_p}C\). Every coset block is the all-ones matrix of size \(p^{|A|-r}\) multiplied by \(p^{-|A|}\), so contributes one eigenvalue \(p^{-r}\) and otherwise zeros. Thus the claimed full spectrum follows once \(r\) is evaluated.

**Step 2: Exact left kernels of unsigned incidence.** A vector \(z\in\mathbb F_p^V\) is in \(\ker(U_A^{\mathsf T})\) precisely when \(z_u+z_v=0\) on every edge \(uv\in A\). Within each connected component this forces an alternating value. If \(p=2\), the alternating values coincide, so every component contributes one degree of freedom. If \(p\) is odd, a component with an odd cycle forces its value to vanish, whereas each bipartite component contributes exactly one degree of freedom. Isolated vertices each contribute one. The component vectors defined in the finding have disjoint supports and are independent; consequently

\[
\ker(U_A^{\mathsf T})=\operatorname{im}T_A,\qquad
\ker(U_B^{\mathsf T})=\operatorname{im}T_B.
\]

**Step 3: The overlap identity.** Put \(X=\operatorname{im}U_A\) and \(Y=\operatorname{im}U_B\) inside \(\mathbb F_p^V\). By the nondegenerate standard dot product, \(X^\perp=\operatorname{im}T_A\) and \(Y=\ker T_B^{\mathsf T}\). The rank of \(U_A^{\mathsf T}U_B\) equals the rank of the pairing restricted to \(X\times Y\), hence

\[
\operatorname{rank}C=\dim Y-\dim(Y\cap X^\perp).
\]

We have \(\dim Y=n-q_B\). The intersection \(Y\cap X^\perp\) consists of \(T_Ac\) satisfying \(T_B^{\mathsf T}T_Ac=0\). Since \(T_A\) has independent columns, the intersection dimension is \(q_A-\operatorname{rank}(T_B^{\mathsf T}T_A)\). Substitution gives \(\operatorname{rank}C=n-q_A-q_B+\operatorname{rank}P_p\), completing the general proof. This argument also covers zero-column matrices and empty partitions.

**Step 4: The Hamilton-path characteristic jump.** With \(A\) a Hamilton path in \(K_n\), \((V,A)\) is connected and bipartite, so \(q_A=1\) in every characteristic. For \(n\ge5\), the complementary subgraph \((V,B)\) is connected: a vertex outside the triangle at coordinates \(1,3,5\) is adjacent in \(B\) to at least one of those three vertices. That triangle lies entirely in \(B\), so \((V,B)\) is nonbipartite. Thus \(q_B=0\) for odd primes and the formula gives \(d_p=n-1\). For \(p=2\), both connected components contribute the all-one vector, and \(P_2=[n\bmod 2]\). Therefore \(d_2=n-2+(n\bmod2)\), yielding the stated split.

## Verification

A standalone exact checker `check.py` independently builds the line-graph cut-adjacency matrix and the component-signature prediction over prime fields. It completed 179,427 exhaustive graph/edge-partition/prime cases for all base graphs through five vertices, 20,000 random checks for six to fifteen vertices, and 112 complete-graph Hamilton-path tests. A separate direct construction of ten small quantum-state amplitude matrices and reduced-density-matrix eigenspectra agreed with the flat-spectrum law with largest absolute numerical eigenvalue error \(2.22\times10^{-16}\). The exhaustive bounds apply only to the stated finite sizes; the proof above, not the computations, establishes the unrestricted theorem.

Reproduce with `python3 check.py`; optional direct eigenspectrum checks require NumPy, while all finite-field tests use only the Python standard library. The recorded output is included in `CHECK_OUTPUT.txt`.

## Relationship to prior work

Hein, Eisert and Briegel established the general binary graph-state cut-rank/Schmidt-rank correspondence; that correspondence is explicitly used and is **not** claimed as new. Higher-dimensional graph-state and maximally entangled-state frameworks are also established in Looi et al., Helwig, and Chen--Zhou. Severini's full article treats multipartite Schmidt measure of two-colorable graph states and discusses line graphs, but does not state this arbitrary base-edge cut formula. Oum's full graph/rank-width analysis gives a binary line-graph cut-rank upper bound in terms of boundary vertices and reports a known full adjacency-rank theorem; those are not the exact signed-overlap identity for every cut and prime. A previously derived formula for rectangular cuts of rook-graph states, equivalent to a specialized cut of \(L(K_{m,n})\), is subsumed by the present general statement; no novelty is claimed for that special case.

The assessed contribution is the exact all-graph, all-edge-partition signed component-overlap evaluation across prime characteristics, the resulting full reduced-state spectrum, and the explicit characteristic-dependent maximality transition for complete-graph Hamilton-path cuts. The component nullspace and rank identities are elementary once the correct quantum-to-incidence reduction is found; the mathematical contribution is their uniform synthesis and exact classification, rather than a new general graph-state formalism.

## Limitations

Only pure, unit-weight, prime-dimensional graph states on line graphs of finite simple graphs are covered. Non-prime local dimensions, weighted entangling edges, mixed/noisy states, graph dynamics, multigraphs, and arbitrary non-line-graph networks are not treated. The result does not imply that every line-graph state is absolutely maximally entangled. The literature comparison is finite and cannot prove absolute historical uniqueness; specialized earlier incidence-rank or quantum-network literature remains a residual priority risk. No independent scientific audit has been performed.

## References

1. M. Hein, J. Eisert, and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first submitted 18 July 2003; particularly Sec. III.2 and Proposition 3. https://arxiv.org/abs/quant-ph/0307130
2. S. Severini, *Two-colorable graph states with maximal Schmidt measure*, arXiv:quant-ph/0511147, first submitted 15 November 2005; particularly Secs. III and IV.2. https://arxiv.org/abs/quant-ph/0511147
3. S. Oum, *Excluding a Bipartite Circle Graph from Line Graphs*, author manuscript (2006), particularly Secs. 3 and 6, Lemma 14, and Corollary 16. https://sangil.dimag.kr/pdf/2006line.pdf
4. S. Y. Looi, L. Yu, V. Gheorghiu, and R. B. Griffiths, *Quantum-error-correcting codes using qudit graph states*, arXiv:0712.1979 (2007). https://arxiv.org/abs/0712.1979
5. W. Helwig, *Absolutely Maximally Entangled Qudit Graph States*, arXiv:1306.2879 (2013). https://arxiv.org/abs/1306.2879
6. L. Chen and D. L. Zhou, *Graph states of prime-power dimension from generalized CNOT quantum circuit*, arXiv:1507.05386 (2015), *Scientific Reports* 6, 27135 (2016). https://arxiv.org/abs/1507.05386
