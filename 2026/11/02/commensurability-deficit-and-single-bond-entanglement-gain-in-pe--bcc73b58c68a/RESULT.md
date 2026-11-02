# Commensurability deficit and single-bond entanglement gain in periodic square cluster states

## Finding
Let \(m,n\ge4\) be **even** integers. Let \(G_{m,n}=C_m\square C_n\) be the simple toroidal square grid, with vertices \((i,j)\in\mathbb Z_m\times\mathbb Z_n\), and edges between nearest neighbors in either coordinate. Form its \(mn\)-qubit graph state \(|G_{m,n}\rangle\) by applying one controlled-\(Z\) gate on each edge to \(|+\rangle^{\otimes mn}\). Partition the qubits into the checkerboard sets \(A=\{(i,j):i+j\equiv0\pmod2\}\) and \(B=V\setminus A\).

For **every** such pair \((m,n)\), the entanglement entropy (in bits) of this pure state across \(A\mid B\) is exactly
\[
S_A(|G_{m,n}\rangle)=\frac{mn}{2}-\gcd(m,n).
\]
The positive eigenvalues of the reduced density matrix are all equal to \(2^{-r}\), repeated \(2^r\) times, where \(r=mn/2-\gcd(m,n)\). Thus every order of Rényi entropy and the pure-state logarithmic negativity across this cut equals \(r\) bits.

More surprisingly, if **any one** of the \(2mn\) edges is removed *before graph-state preparation*, the entropy across the unchanged checkerboard partition increases by **exactly one bit**:
\[
S_A(|G_{m,n}-e\rangle)=\frac{mn}{2}-\gcd(m,n)+1,
\qquad e\in E(G_{m,n}).
\]
The one-edge gain is the extremal case of the general bound that toggling one cross-partition graph edge can change the binary cut rank by at most one.

## Assumptions and scope
All vector-space ranks and kernels below, unless explicitly stated otherwise, are over \(\mathbb F_2\). The cycles \(C_m,C_n\) have length at least four so that each site has four **distinct** neighbors. Both lengths must be even for the checkerboard coloring to be a well-defined graph bipartition. The graph state is a pure ideal stabilizer state; this is *not* a thermal state, quantum-walk capture probability, or the multipartite Schmidt measure optimized over all partitions.

The entropy is the von Neumann entropy \(S_A=-\operatorname{tr}(\rho_A\log_2\rho_A)\), with \(\rho_A=\operatorname{tr}_B|G\rangle\langle G|\). A missing bond means omitting its associated controlled-\(Z\) gate when preparing the graph state, not performing a local operation on a previously prepared state.

## Proof
**1. Stabilizer cut rank and the complete Schmidt spectrum.** Order the black and white vertices separately and denote their square binary biadjacency matrix by \(B\), of order \(N=mn/2\). Since all edges cross the cut, the computational-basis amplitude matrix of the graph state has entries
\[
M_{a,b}=2^{-N}(-1)^{a^{\mathsf T}Bb},\qquad a,b\in\mathbb F_2^{N}.
\]
The reduced matrix satisfies
\[
(\rho_A)_{a,a'}=2^{-N}\,\mathbf 1_{B^{\mathsf T}(a+a')=0}.
\]
Its support decomposes into the cosets of \(\ker B^{\mathsf T}\), giving \(2^{\operatorname{rank}B}\) equal positive eigenvalues \(2^{-\operatorname{rank}B}\). Consequently \(S_A=\operatorname{rank}B\), and all Rényi entropies agree. For a pure state with a flat Schmidt spectrum, logarithmic negativity also equals \(\operatorname{rank}B\).

**2. Factorization of the binary torus adjacency.** Let \(X,Y\) act on functions on \(\mathbb Z_m\times\mathbb Z_n\) by unit shifts of the first and second coordinates. The full binary adjacency operator satisfies
\[
\mathcal A=X+X^{-1}+Y+Y^{-1}
=X^{-1}(1+XY)(1+XY^{-1}).
\]
Write \(P=1+XY\), \(Q=1+XY^{-1}\), \(g=\gcd(m,n)\) and \(L=\operatorname{lcm}(m,n)=mn/g\). Both diagonal translations \((1,1)\) and \((1,-1)\) have order \(L\) and exactly \(g\) orbits. Therefore \(\dim\ker P=\dim\ker Q=g\). Each kernel is the space of functions constant on the corresponding diagonal-translation orbits.

On every orbit of \((1,-1)\), the image of \(Q\) consists precisely of binary functions with even sum on that orbit: it is the image of \(1+\)cyclic shift on a length-\(L\) cycle. An orbit of \((1,1)\), characterized by a fixed residue \(i-j\pmod g\), meets an orbit of \((1,-1)\), characterized by a fixed \(i+j\pmod g\), either not at all or in exactly \(2L/g\) sites. Indeed, along the first orbit the latter residue advances by \(2\), visiting precisely \(g/2\) residues equally often. Since \(g\) is even, every nonempty intersection has even cardinality. Thus the indicator of each \((1,1)\) orbit belongs to \(\operatorname{im}Q\), yielding
\[
\ker P\subseteq\operatorname{im}Q.
\]
For any two linear maps the preimage formula gives \(\dim\ker(PQ)=\dim\ker Q+\dim(\ker P\cap\operatorname{im}Q)\). Hence
\[
\dim\ker\mathcal A=\dim\ker(PQ)=g+g=2g.
\]

**3. Converting the full rank into cut rank.** The grid is bipartite, so \(\mathcal A\) is represented by \(\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}\). Both color classes have size \(N\), hence \(\dim\ker\mathcal A=2(N-\operatorname{rank}B)\). Comparing with the preceding identity gives
\[
\operatorname{rank}B=N-g=\frac{mn}{2}-\gcd(m,n),
\]
which proves the entropy formula and its spectrum statement.

**4. Deleting one arbitrary bond.** Every black or white vertex has degree four; therefore \(B\mathbf1=0\) and \(\mathbf1^{\mathsf T}B=0\). Let \(e\) join black vertex \(u\) to white vertex \(v\), and let \(e_u,e_v\) be the corresponding standard basis vectors. The graph with that bond omitted has matrix \(B_e=B+e_ue_v^{\mathsf T}\) over \(\mathbb F_2\). Given any \(y=Bx\), replace \(x\) by \(x+\mathbf1\) if needed to enforce \(e_v^{\mathsf T}x=0\), without altering \(Bx\). This shows \(\operatorname{im}B\subseteq\operatorname{im}B_e\). On the other hand \(B_e\mathbf1=e_u\), and \(e_u\notin\operatorname{im}B\), since every vector in \(\operatorname{im}B\) has even coordinate sum. Thus \(\operatorname{rank}B_e\ge\operatorname{rank}B+1\). The rank-one difference gives the reverse bound. This proves the exact one-bit gain for every edge.

The last argument applies more generally to deletion of any single edge from any finite bipartite graph in which all vertex degrees are even (even if the two color classes have unequal sizes), with entropy interpreted across its graph-coloring bipartition.

## Verification
`checker.py` independently constructs the binary biadjacency matrix directly from the four nearest neighbors and computes ranks by integer-bit Gaussian elimination; it does not use the diagonal-orbit proof, closed-form rank algorithm, or a graph-state library. The actual included run covers all \(64\) even rectangle sizes with \(4\le m,n\le18\), including all \(703\) tested one-bond deletions (all bonds when both sizes are at most eight, one representative otherwise). The script asserts the predicted ranks rather than trusting a precomputed table. The command is `python checker.py`. `checker-output.txt` records the completed run.

Representative exact ranks are \(4\) for \((m,n)=(4,4)\), \(10\) for \((4,6)\), \(12\) for \((6,6)\), \(28\) for \((6,10)\), \(44\) for \((8,12)\), and \(40\) for \((10,10)\). Every sampled one-bond deletion raises its rank by one. The finite checks validate implementation examples but do not substitute for the all-size proof.

## Relationship to prior work
Hein, Eisert and Briegel (arXiv:quant-ph/0307130, initially public July 18, 2003) establish graph-state entanglement and graph-theoretic rank methods; their worked cluster-state families use finite open lattices and concern multipartite Schmidt measure or chosen maximal-rank cuts, not the stated **periodic checkerboard cut**. Hein and collaborators (arXiv:quant-ph/0602096, February 11, 2006), especially Proposition 10 and the edge-rule discussion, give the general identification of bipartite Schmidt rank with binary cross-adjacency rank and a bound of one for the change caused by an edge toggle. Those general facts are used explicitly here, not asserted as original. The result supplied here is the exact all-even-size toroidal arithmetic rank evaluation and the universal direction (gain rather than a mere upper bound) for the bond-deletion operation.

The classical toroidal Lights Out literature, including A. E. Brouwer's 'Button Madness and Lights Out on rectangles', mainly examines the **closed-neighborhood** operator \(I+\mathcal A\); this differs from the off-diagonal adjacency \(\mathcal A\) required for graph-state entanglement. Hunziker, Machiavelo and Park's 2004 study of \(\sigma\)-automata and Chebyshev polynomials is a related but incompletely inspected mathematical source; no priority claim is made about all possible binary-grid nullity results.

## Limitations
The theorem assumes even side lengths of at least four and homogeneous, unweighted graph-state controlled-\(Z\) edges. It does not classify odd-sided grids, arbitrary checkerboard-like partitions, arbitrary bond-deletion sets, noisy state preparation, or generic quantum many-body Hamiltonian ground states. The cut entropy is not the maximum of the multipartite Schmidt measure over bipartitions, and no claim is made that this bipartition is globally optimal. A general stronger rank theorem in older binary-grid/cellular-automata literature may yet subsume the arithmetic part; historical priority has not been independently established.

## References
1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first public July 18, 2003); Phys. Rev. A 69, 062311 (2004). https://arxiv.org/abs/quant-ph/0307130
2. M. Hein et al., *Entanglement in Graph States and its Applications*, arXiv:quant-ph/0602096 (first public February 11, 2006). https://arxiv.org/abs/quant-ph/0602096
3. A. E. Brouwer, *Button Madness and Lights Out on rectangles*, https://aeb.win.tue.nl/ca/madness/madrect.html (accessed October 29, 2026 UTC; distinct \(I+\mathcal A\) model).
4. M. Hunziker, A. Machiavelo and J. Park, *Chebyshev polynomials over finite fields and reversibility of \(\sigma\)-automata on square grids*, Theor. Comput. Sci. 320 (2004), 465–483, doi:10.1016/j.tcs.2004.03.031 (full text not verified in this review).
