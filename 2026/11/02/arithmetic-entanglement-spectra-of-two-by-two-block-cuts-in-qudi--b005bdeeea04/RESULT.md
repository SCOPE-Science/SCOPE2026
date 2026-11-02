# Arithmetic entanglement spectra of two-by-two block cuts in qudit rook-graph states

## Finding

Let \(p\) be any prime and \(a,b,c,d\geq1\) integers. Set \(m=a+b\) and \(n=c+d\). Partition the rows of an \(m\)-by-\(n\) array into nonempty sets \(R_0,R_1\) of sizes \(a,b\), and its columns into nonempty sets \(C_0,C_1\) of sizes \(c,d\). On the \(mn\) array cells, form the **rook graph** \(G=K_m\square K_n=L(K_{m,n})\): two distinct cells are adjacent exactly when they share a row or a column. Let \(|G;p\rangle\) be the pure, unit-weight, prime-dimensional qudit graph state constructed by applying a generalized controlled-phase gate along every edge to \(|+_p\rangle^{\otimes mn}\).

Split the qudits into the diagonal blocks
\[
A=(R_0\times C_0)\cup(R_1\times C_1),\qquad
B=(R_0\times C_1)\cup(R_1\times C_0).
\]
Write \(M_p\) for the following two-by-two matrix over \(\mathbb F_p\):
\[
M_p=\begin{pmatrix}a&c\\d&b\end{pmatrix}\pmod p,
\qquad r_p=\operatorname{rank}_{\mathbb F_p}M_p,
\qquad e_p=m+n-4+r_p.
\]

**Exact result.** The reduced density matrix on \(A\) has exactly \(p^{e_p}\) nonzero eigenvalues, each equal to \(p^{-e_p}\). Its other eigenvalues are zero. The Schmidt rank is \(p^{e_p}\); every positive-order Rényi entropy and the von Neumann entropy equal \(e_p\) base-\(p\) dits, or \(e_p\log_2p\) bits. Thus only the four block sizes modulo \(p\), not their placement or the full \(mn\)-qudit scale, control the nontrivial arithmetic correction to \(m+n-4\).

In particular, \(r_p=0\) exactly when \(p\) divides each of \(a,b,c,d\); \(r_p=2\) exactly when \(ab-cd\not\equiv0\pmod p\); in all remaining cases \(r_p=1\). For the literal alternating checkerboard of an even-by-even array, \(a=b=m/2\) and \(c=d=n/2\). For qubits, its entropy in bits is
\[
S_A=\begin{cases}
m+n-4,&m\equiv n\equiv0\pmod4,\\
m+n-3,&m\equiv n\equiv2\pmod4,\\
m+n-2,&m,n\text{ even and }m\not\equiv n\pmod4.
\end{cases}
\]
For example, the four equal blocks of size \(2\) give \(4\) bits at \(p=2\) but \(5\) trits at \(p=3\), whereas four equal blocks of size \(3\) give \(9\) bits at \(p=2\) and \(8\) trits at \(p=3\). If both \(m,n\to\infty\), this structured bipartition has at most \(m+n-2\) dits of entropy despite containing \(mn\) qudits and quadratically many crossing adjacency relations.

## Assumptions and scope

The local Hilbert space at every cell is \(\mathbb C^p\), with computational basis labelled by the finite field \(\mathbb F_p\) and \(\omega=e^{2\pi i/p}\). The controlled-phase on an edge \(uv\) acts by \(|x_u,x_v\rangle\mapsto\omega^{x_ux_v}|x_u,x_v\rangle\), and \(|+_p\rangle=p^{-1/2}\sum_{x\in\mathbb F_p}|x\rangle\). There are no self-loops, repeated gates, edge weights other than one, or environmental interactions. The theorem is for every prime \(p\) and every ordered positive quadruple \((a,b,c,d)\); no assumptions about equal row/column block sizes or parity are made. All entropies are those of the stated pure state under the fixed cut \(A\mid B\), not an optimization over bipartitions.

## Proof

**1. Reduction to a cut matrix.** Order the cells in \(A\) and \(B\) arbitrarily and let \(\Gamma\) be the \(|A|\)-by-\(|B|\) matrix over \(\mathbb F_p\) that records exactly the edges crossing the cut. Controlled-phase gates wholly within \(A\) or wholly within \(B\) act as local unitaries for this bipartition, so they do not alter the reduced-state eigenvalues. With the internal gates suppressed, the state is
\[
|\psi\rangle=p^{-(|A|+|B|)/2}\sum_{x\in\mathbb F_p^A}\sum_{y\in\mathbb F_p^B}
\omega^{x^{\mathsf T}\Gamma y}|x\rangle|y\rangle.
\]
Summing over \(y\) gives
\[
\langle x|\rho_A|x'\rangle
=p^{-|A|}\,\mathbf1_{\{\Gamma^{\mathsf T}(x-x')=0\}}.
\]
If \(R=\operatorname{rank}_{\mathbb F_p}\Gamma\), the kernel of \(\Gamma^{\mathsf T}\) has size \(p^{|A|-R}\). The matrix above has one equal-entry block for each coset of this kernel, so it has \(p^R\) eigenvalues \(p^{-R}\) and all others zero. Hence it remains to compute \(R\) exactly.

**2. All relevant margins.** For a vector supported on \(A\), write \(X=(x_{ij})\) on \(R_0\times C_0\) and \(Y=(y_{ij})\) on \(R_1\times C_1\). Let \(r\in\mathbb F_p^a\) and \(s\in\mathbb F_p^c\) be the row and column sums of \(X\), and let \(u\in\mathbb F_p^b\) and \(t\in\mathbb F_p^d\) be the row and column sums of \(Y\). Necessarily
\[
\sum r_i=\sum s_j,\qquad \sum u_i=\sum t_j.
\]
These are the only constraints on the four margin vectors: on each nonempty rectangular block, arbitrary row and column sums with equal totals are realized by assigning the designated first row and first column, and correcting the common corner. Consequently the joint margin map is onto a vector space of dimension \((a+c-1)+(b+d-1)=m+n-2\).

**3. Image of the cut adjacency.** The image of a supported vector under \(\Gamma^{\mathsf T}\) at a cell \((i,j)\in R_0\times C_1\) is \(r_i+t_j\). At a cell \((i,j)\in R_1\times C_0\), it is \(u_i+s_j\). Indeed, a rook edge crosses the cut only when it stays in the cell's row or column, and these are exactly the two relevant sums. Thus the cut matrix factors through the margin map of Step 2, and its rank equals the rank of this induced margin-to-output map.

**4. Exact kernel of that induced map.** Because each of the four row/column sets is nonempty, the output on \(R_0\times C_1\) vanishes exactly when \(r_i=\alpha\) for every \(i\) and \(t_j=-\alpha\) for every \(j\), for some \(\alpha\in\mathbb F_p\). Similarly, the output on \(R_1\times C_0\) vanishes exactly when \(u_i=\beta\) and \(s_j=-\beta\) for some \(\beta\in\mathbb F_p\). The two margin compatibility conditions become
\[
a\alpha+c\beta=0,\qquad d\alpha+b\beta=0,
\]
which is precisely \(M_p(\alpha,\beta)^{\mathsf T}=0\). Hence the kernel of the induced map has dimension \(2-r_p\). Rank-nullity now yields
\[
\operatorname{rank}_{\mathbb F_p}\Gamma
=(m+n-2)-(2-r_p)=m+n-4+r_p.
\]

**5. Arithmetic and spectral conclusions.** The rank of a two-by-two matrix is zero when all entries vanish, two when its determinant is nonzero, and one otherwise. Since \(\det M_p=ab-cd\), the stated modular trichotomy follows. Applying Step 1 gives the exact flat reduced-state spectrum and every asserted entropy. The even-by-even qubit checkerboard cases follow from \(M_2=\bigl(\begin{smallmatrix}m/2&n/2\\n/2&m/2\end{smallmatrix}\bigr)\bmod2\). No finite-size limit or unproved spectral approximation is used.

## Verification

The standalone standard-library script `verify_rook.py` reconstructs rook-graph cut adjacency matrices directly from pairs of cell coordinates, performs independent finite-field Gaussian elimination, and compares its rank against the two-by-two formula. It verifies \(768\) exhaustive parameter choices (all \(a,b,c,d\in\{1,2,3,4\}\) for \(p=2,3,5\)) and \(400\) additional deterministic parameter choices for \(p=2,3,5,7\), for a total of \(1168\) rank comparisons. It also constructs the pure graph-state complex amplitudes directly, traces the complementary partition numerically for four small examples, and checks unit trace and the predicted reduced-state purity \(p^{-e_p}\). The exact checkerboard examples for \(p=2,3\) and four equal blocks of size \(2\) or \(3\) are separately asserted. All checks passed. These finite tests supplement the all-parameter algebraic proof; they do not establish it by enumeration.

## Relationship to prior work

Hein, Eisert and Briegel's original graph-state entanglement analysis gives the foundational binary cut-adjacency rank relationship for qubit graph states (arXiv:quant-ph/0307130, first posted 18 July 2003; Phys. Rev. A 69, 062311 (2004), section on bipartite splits). Looi, Yu, Gheorghiu and Griffiths extend graph-state constructions to arbitrary qudit dimensions (arXiv:0712.1979, first posted 12 December 2007). Helwig (arXiv:1306.2879, 12 June 2013) gives general graph-state bipartite-entanglement methods and AME constructions. These general methods are antecedents; the claim here is specifically the evaluated, all-block-size **rook-graph cut spectrum**, including the two-by-two determinant obstruction and its prime-dependent arithmetic regimes, not the general rank rule itself.

Liao, Sanders and Feder (arXiv:2112.02502, first posted 5 December 2021) explicitly study graph states on line graphs of complete bipartite graphs, including topological-order and code questions. That is a particularly important same-object comparison. The accessible abstract concerns topological order, not the tensor-product block-cut spectrum. Its full text was not accessible for inspection, so it cannot be asserted that it omits the present result; this is a residual priority risk requiring external full-text comparison before any publication-level novelty claim. Published mathematical-record searches using both rook-graph and qudit-entropy aliases did not disclose the same determinant formula, but negative search results alone cannot establish priority.

## Limitations

The result treats ideal pure prime-dimensional graph states with unit controlled-phase interactions and the specified tensor-product two-by-two row/column block cuts. It does not classify arbitrary bipartitions, disordered or weighted graph states, mixed states, gate errors, code distance, or entanglement after measurements. The asymptotic entropy bound concerns this chosen cut and does not imply that the global multiparty entanglement is small. Historical priority needs direct comparison with the unavailable same-object full text.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (initial public version 2003-07-18); Phys. Rev. A **69**, 062311 (2004), https://doi.org/10.1103/PhysRevA.69.062311.
2. S. Y. Looi, L. Yu, V. Gheorghiu and R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979 (initial public version 2007-12-12); Phys. Rev. A **78**, 042303 (2008), https://doi.org/10.1103/PhysRevA.78.042303.
3. W. Helwig, *Absolutely Maximally Entangled Qudit Graph States*, arXiv:1306.2879 (initial public version 2013-06-12), https://arxiv.org/abs/1306.2879.
4. P. Liao, B. C. Sanders and D. L. Feder, *Topological graph states and quantum error correction codes*, arXiv:2112.02502 (initial public version 2021-12-05); Phys. Rev. A **105**, 042418 (2022), https://doi.org/10.1103/PhysRevA.105.042418.
