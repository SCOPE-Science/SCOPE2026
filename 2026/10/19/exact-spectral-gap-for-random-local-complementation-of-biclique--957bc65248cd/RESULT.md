# Exact spectral gap for random local complementation of biclique graph states

## Finding

Fix integers \(m,n\ge2\) and write \(N=m+n\). In the **labeled** graph-state local-complementation orbit \(\mathcal O_{m,n}\) of the complete bipartite graph \(K_{m,n}\), at each discrete step choose one of the \(N\) vertex labels independently and uniformly, and locally complement that vertex. Let \(P\) be the resulting transition matrix, retaining null moves as self-loops. Put \(L=N(I-P)\).

The orbit has exactly \(mn+m+n+3\) elements. Define
\[
\begin{aligned}
p_{m,n}(t)={}&t^4-3(N+1)t^3
 +[2(m^2+n^2)+7mn+7N+2]t^2\\
&-[4mnN+11mn+2(m^2+n^2)+4N]t\\
&+2mn(mn+N+3).
\end{aligned}
\]
The complete spectrum of \(L\), with algebraic multiplicity, is
\[
\{0,N+1\}\ \uplus\ \{t:p_{m,n}(t)=0\}\ \uplus\
\{1^{[m+n-2]},\ (n+2)^{[m-1]},\ (m+2)^{[n-1]},\ 2^{[(m-1)(n-1)]}\}.
\]
Here the four roots are counted with multiplicity, and coincident values from different groups have their multiplicities added. All four roots of \(p_{m,n}\) are strictly greater than \(1\), so
\[
1-\lambda_2(P)=\frac{1}{m+n},\qquad
\lambda_2(P)=1-\frac{1}{m+n},
\]
where eigenvalues are arranged in **decreasing algebraic order**, not by absolute value. Thus the exact reversible-chain Poincaré relaxation time is \(m+n\), independent of the imbalance of the two parts.

## Assumptions and scope

All graphs are simple and undirected, on a **fixed labeled** vertex set split into \(X\) of size \(m\) and \(Y\) of size \(n\), where \(m,n\ge2\). Local complementation \(\tau_v\) toggles every pair of neighbors of \(v\) and leaves all other edges unchanged. In particular a move at a leaf fixes the graph. Each of the \(N\) named vertices has selection probability \(1/N\), even when different selections give the same graph. The orbit contains graphs, not all phase-distinct stabilizer vectors or all relabelings. The associated graph states are related by local Clifford operations.

## Proof

**1. An explicit closed orbit.** Let \(B=K_{m,n}\), and let \(C_X\), respectively \(C_Y\), add all within-\(X\), respectively within-\(Y\), edges to \(B\). For \(i\in X\), let \(U_i\) have a star on \(X\) centered at \(i\), a clique on \(Y\), and precisely the cross edges \(i\!\sim\!j\) for every \(j\in Y\). For \(j\in Y\), let \(V_j\) have a star on \(Y\) centered at \(j\), a clique on \(X\), and all cross edges from \(j\) to \(X\). For \((i,j)\in X\times Y\), let \(W_{ij}\) comprise a star in each part centered respectively at \(i,j\), plus the unique cross edge \(ij\). The cross-edge patterns distinguish the \(B,C_X,C_Y,U_i,V_j,W_{ij}\) types, and the two clique choices distinguish \(B,C_X,C_Y\); this uses \(m,n\ge2\).

Directly complementing each possible neighborhood gives the exhaustive rules below (each vertex outside a mentioned set is covered by its explicit alternative):

* \(B\): an \(X\)-vertex gives \(C_Y\); a \(Y\)-vertex gives \(C_X\).
* \(C_X\): \(i\in X\) gives \(U_i\), while \(j\in Y\) gives \(B\). The analogous rule interchanges \(X,Y\) for \(C_Y\).
* \(U_i\): \(i\) gives \(C_X\); the other \(X\)-vertices fix \(U_i\); \(j\in Y\) gives \(W_{ij}\).
* \(V_j\): \(j\) gives \(C_Y\); the other \(Y\)-vertices fix \(V_j\); \(i\in X\) gives \(W_{ij}\).
* \(W_{ij}\): \(i\) gives \(V_j\), \(j\) gives \(U_i\), and all other vertices fix \(W_{ij}\).

Every listed graph can be reached from \(B\), and the list is closed under all moves. This proves the claimed labeled-orbit count and transition rules. The prior literature already establishes the corresponding biclique orbit up to vertex permutations; the enumeration is used here to analyze the transition operator, not claimed independently as novel.

**2. Symmetry decomposition.** Set \(A=NP\). Each \(\tau_v\) is an involution, so \(A\) is symmetric; its row sums equal \(N\). The independent permutations of \(X\) and \(Y\) make the space of functions constant on each of the six families \(B,C_X,C_Y,U,V,W\) invariant. In this order, the matrix of \(A\) on that subspace is
\[
Q=\begin{pmatrix}
0&n&m&0&0&0\\
n&0&0&m&0&0\\
m&0&0&0&n&0\\
0&1&0&m-1&0&n\\
0&0&1&0&n-1&m\\
0&0&0&1&1&N-2
\end{pmatrix}.
\]
The remaining space decomposes orthogonally, with respect to the counting inner product, into: \((m-1)\) independent row-zero pairs of coordinates \((U_i,W_{ij})\), \((n-1)\) independent column-zero pairs \((V_j,W_{ij})\), and the \((m-1)(n-1)\)-dimensional space of \(W\)-arrays with every row and column sum zero. On each row-zero pair, \(A\) acts by
\[
\begin{pmatrix}m-1&n\\1&N-2\end{pmatrix},
\]
whose eigenvalues are \(N-1\) and \(m-2\). Column-zero pairs instead give \(N-1\) and \(n-2\). On the doubly zero-sum \(W\)-space, \(A\) acts as the scalar \(N-2\).

A direct determinant of \(NI_6-Q\) gives
\[
\det(tI_6-(NI_6-Q))=t(t-(N+1))p_{m,n}(t).
\]
The other blocks give Laplacian eigenvalues \(1,n+2,m+2,2\) with the displayed multiplicities. Their dimensions sum to \(mn+m+n+3\), so the list is complete. The quotient \(Q\) is similar to a real symmetric matrix (multiply its six coordinate axes by weights \(1,1,1,\sqrt m,\sqrt n,\sqrt{mn}\)); thus all roots of \(p_{m,n}\) are real.

**3. Positivity of the spectral gap.** Put \(u=m-2\ge0\), \(v=n-2\ge0\), and \(h\ge0\). Direct expansion gives
\[
\begin{aligned}
p_{m,n}(1-h)={}&h^4+(3u+3v+11)h^3\\
&+(2u^2+7uv+20u+2v^2+20v+35)h^2\\
&+(4u^2v+6u^2+4uv^2+29uv+33u+6v^2+33v+33)h\\
&+2(u+1)(u+2)(v+1)(v+2).
\end{aligned}
\]
Every coefficient is positive for \(u,v\ge0\), hence \(p_{m,n}(t)>0\) whenever \(t\le1\). The quartic eigenvalues are therefore all larger than \(1\). The sole zero Laplacian eigenvalue is simple, and the eigenvalue \(1\) occurs with positive multiplicity \(m+n-2\). It is exactly the first positive Laplacian eigenvalue. Division by \(N\) proves the gap formula.

## Verification

The included standalone `checker.py` reconstructs graph edges from their definitions, performs independent breadth-first orbit enumeration, recomputes every local complementation directly from graph neighborhoods, checks the predicted transition rules and reversibility, and exactly verifies the full characteristic polynomial using integer symbolic arithmetic. Running `python3 checker.py` with SymPy reproduces all checks for every \(2\le m,n\le5\), a total of 16 independent finite cases. In particular the full orbit sizes are 11 for \(m=n=2\), 18 for \(m=n=3\), and 38 for \(m=n=5\). The **infinite-family proof** is the symbolic invariant-space decomposition and positivity argument above, not those finite computations.

## Relationship to prior work

I. Tzitrin, arXiv:1805.05968, Section III.1, explicitly identifies a complete biclique local-complementation orbit **up to vertex permutation** and relates bicliques to binary stars. This covers the qualitative structural orbit input and eliminates any claim of novelty for it. J. C. Adcock, S. Morley-Short, A. Dahlberg and J. W. Silverstone, arXiv:1910.03969, Sections 2–4, tabulate and analyze LC orbits for small numbers of qubits, and explicitly propose investigating the mixing rates of random local-complementation walks. Those sources do not present the full labeled biclique random-walk Laplacian spectrum or the uniform-in-imbalance closed gap derived here. The theorem concerns a **classical random process on quantum graph-state representatives**, not a quantum random-walk Hamiltonian on \(K_{m,n}\).

## Limitations

The orbit depends on fixed labels and both part sizes at least two. Selection of vertices must be exactly uniform, and the self-loops must be retained. The proved gap is the one-sided/Poincaré gap \(1-\lambda_2(P)\); it is not a bound on the magnitude of every nontrivial eigenvalue. No exact absolute gap, total-variation mixing cutoff, purification rate, or physical implementation error budget is asserted. Distinct literature might contain equivalent spectral identities under another parametrization; the cited original papers and identified closest comparison results do not exhibit this statement. Independent validation has not been performed.

## References

1. I. Tzitrin, “On the local equivalence of complete bipartite and repeater graph states,” arXiv:1805.05968 (first public version 2018-05-15); https://arxiv.org/html/1805.05968v1 .
2. J. C. Adcock, S. Morley-Short, A. Dahlberg, J. W. Silverstone, “Mapping graph state orbits under local complementation,” arXiv:1910.03969 (first public version 2019-10-09), *Quantum* **4**, 305 (2020); https://arxiv.org/html/1910.03969v2 .
