# Sharp inversion-diameter bounds for co-two-factor bicliques

## Finding

**Theorem.** Fix any integer \(n\ge3\), and let \(H\) be a *spanning bipartite 2-factor* of \(K_{n,n}\), namely a simple spanning subgraph in which every vertex has degree two (a vertex-disjoint union of even cycles). Write \(G=K_{n,n}-E(H)\). Then
\[
\operatorname{diam}(\mathcal I(G))\le n-2=\Delta(G).
\]
For every \(n\ge3\) equality is attained by the natural Hamilton-cycle deletion:
\[
\operatorname{diam}\bigl(\mathcal I(K_{n,n}-C_{2n})\bigr)=n-2.
\]
The bound is uniform over **all** 2-factor deletion patterns, including disconnected 2-factors, and is constructive for every prescribed pair of orientations.

## Assumptions and scope

The inversion graph \(\mathcal I(G)\) has the *labelled orientations* of a fixed finite simple graph \(G\) as vertices. An inversion of a vertex subset reverses exactly the edges whose **both** endpoints belong to that subset. Inversion distance counts these operations, and the diameter maximizes distance over all pairs of orientations. All linear algebra below is over \(\mathbb F_2\). The bipartition of \(K_{n,n}\) is \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\). The result does not assert that equality holds for **every** 2-factor; only the universal upper bound and equality for Hamiltonian 2-factors are established. No connectedness hypothesis on the remaining graph is needed.

## Proof

**1. Binary-factorization interpretation (standard).** Choose a reference orientation and encode its difference from any target orientation by a bit \(d_{ij}\) for each present edge \(a_i b_j\). A subset inversion with chosen left and right vertex indicators \(\alpha_i,\beta_j\in\mathbb F_2\) toggles \(d_{ij}\) by \(\alpha_i\beta_j\). Thus \(t\) inversions are equivalent to assigning vectors \(u_i,v_j\in\mathbb F_2^t\) such that
\[
d_{ij}=u_i\cdot v_j\quad\text{for every edge }a_i b_j\in E(G).
\]
Indeed the coordinate-\(k\) supports of the vectors specify the selected vertices in inversion \(k\); conversely recording each chosen subset gives the factorization. In particular, if the prescribed edge bits force every \(n\)-by-\(n\) completion to have rank at least \(r\), then at least \(r\) inversions are necessary. This matrix formulation is from the established inversion-diameter literature [1,2], not new here.

**2. A two-check binary code from the omitted 2-factor.** Every right vertex \(b_j\) has exactly two distinct non-neighbours in \(A\); denote them \(a_{s_j}\) and \(a_{t_j}\). Form a multigraph \(T\) on \(\{1,\ldots,n\}\) containing an edge \(s_jt_j\) for each \(j\). Every left vertex is a non-neighbour of exactly two right vertices, since \(H\) is 2-regular. Hence \(T\) is a loopless 2-regular multigraph: disjoint cycles, where a 2-cycle with two parallel edges is allowed. Such a graph admits a proper colouring with three colours.

Identify those three colours with the three nonzero vectors \((1,0)\), \((0,1)\), \((1,1)\) of \(\mathbb F_2^2\). Write the colour on vertex \(i\) as \(h_i\), and form the binary matrix \(P=[h_1\ \cdots\ h_n]\) of size \(2\)-by-\(n\). Every pair \(h_{s_j},h_{t_j}\) has *different* nonzero colours and therefore forms a basis of \(\mathbb F_2^2\). In particular \(P\) has rank two.

Let \(Q\) be the \(n\)-by-\((n-2)\) matrix whose columns are a basis of \(\ker P\). Put \(S_j=\{1,\ldots,n\}\setminus\{s_j,t_j\}\). The square matrix of rows \(Q[S_j,:]\) is nonsingular. For if \(Q[S_j,:]x=0\), the vector \(y=Qx\in\ker P\) is supported on the two excluded coordinates. Consequently
\[
0=Py=y_{s_j}h_{s_j}+y_{t_j}h_{t_j},
\]
which forces both coefficients to vanish by linear independence; hence \(y=0\), and full column rank of \(Q\) gives \(x=0\).

**3. Construct all required inversions.** For each right index \(j\), list the prescribed bits \(d_{ij}\) for \(i\in S_j\), and solve the uniquely solvable system
\[
Q[S_j,:]v_j=(d_{ij})_{i\in S_j},\qquad v_j\in\mathbb F_2^{n-2}.
\]
Take \(u_i\in\mathbb F_2^{n-2}\) to be row \(i\) of \(Q\). Then \(u_i\cdot v_j=d_{ij}\) on every edge. By Step 1, the \(n-2\) coordinate supports give a valid inversion sequence from the reference orientation to the target. The construction uses a three-colouring of disjoint cycles, one nullspace basis and \(n\) square binary-system solutions, all of polynomial complexity. Since each vertex of \(G\) has degree \(n-2\), the asserted degree bound follows.

**4. A sharp Hamilton-cycle example.** When \(H\) is a Hamilton cycle, relabel the vertices cyclically so that the missing edges are \(a_i b_i\) and \(a_i b_{i+1}\), taking the second index modulo \(n\). Define prescribed edge bits by \(d_{i,i+2}=1\) for \(1\le i\le n-2\), and \(d_{ij}=0\) for every other present edge. In any binary matrix completion with arbitrary values on the missing entries, restrict to rows \(i=1,\ldots,n-2\) and columns \(j=3,\ldots,n\). The resulting \((n-2)\)-square submatrix is lower triangular with every diagonal entry one: at position \((i,i+2)\), the prescribed bit is one; for \(j>i+2\), the entry is a *present* edge and its prescribed bit is zero. Therefore every completion has rank at least \(n-2\), even though all entries below the diagonal are unrestricted. By Step 1, this difference pattern needs at least \(n-2\) inversions. Step 3 supplies at most \(n-2\). This proves equality for every \(n\ge3\). \(\square\)

## Verification

The included standalone Python program `verify.py` independently generates inversion move masks and performs breadth-first search over all edge-difference vectors for Hamilton-cycle deletion at \(n=3,4,5\). The exact diameters are respectively \(1,2,3\), with BFS distance distributions
\[
(1,7),\quad(1,89,166),\quad(1,591,21106,11070)
\]
where entries are the counts at successive distances starting with distance zero. It separately constructs inversion factors for every difference vector for these orders, checks the forced-minor rank against every filling of all missing entries at those orders, and checks 32 pseudorandom differences for each \(6\le n\le32\). A second family of tests independently encodes general 2-factors by derangements of \([n]\); it checks all derangements through \(n=7\) and 200 derangements at \(n=8\), with three target differences per case. The script requires only Python's standard library and is run as `python3 verify.py`. These checks concern finite instances; the unrestricted result follows from the proof above.

## Relationship to prior work

Havet, Hörsch and Rambaud [1] introduce the binary-factorization characterization and evaluate inversion diameters for balanced complete multipartite graphs, including complete bicliques. In particular their result determines the undeleted case, not the family with a bipartite 2-factor removed. Bo, Li, Lian and Yan [2] improve general bounds and evaluate complete bicliques; their first public version of 16 June 2026 motivates the degree-parameter question examined here. Arana and collaborators [3] develop degree-sensitive bounds through 2-edge-coloured homomorphisms. Those general estimates do not directly yield the sharp degree bound for every co-2-factor or the equality case of Hamiltonian-cycle deletion. The present contribution is the tailored two-check binary-code construction and its matching unit-triangular lower-bound witness. Prior literature is credited for the inversion-to-factorization reduction. Accessible mathematical searches did not locate this exact theorem; this is not a proof of bibliographic uniqueness.

## Limitations

The upper bound is established only when the deleted bipartite graph is a spanning 2-factor; equality for arbitrary disconnected 2-factors is **not asserted**. The lower-bound certificate is for a spanning Hamilton cycle, and the theorem does not resolve the degree bound for arbitrary graphs. Although the proof is unrestricted in the stated family, independent review and a definitive complete-literature novelty determination have not been performed. Searches may miss equivalent formulations under different terminology.

## References

[1] Frédéric Havet, Florian Hörsch and Clément Rambaud, *Diameter of the inversion graph*, arXiv:2405.04119, first posted 7 May 2024, https://arxiv.org/abs/2405.04119.

[2] Jiawen Bo, Anqi Li, Xiaopan Lian and Xin Yan, *Edge-Number Bounds for the Inversion Diameter of Graphs*, arXiv:2606.17974v1, first posted 16 June 2026, https://arxiv.org/abs/2606.17974.

[3] *Inversion diameter and 2-edge-colored homomorphisms*, arXiv:2602.24171v1, first posted 27 February 2026, https://arxiv.org/abs/2602.24171.
