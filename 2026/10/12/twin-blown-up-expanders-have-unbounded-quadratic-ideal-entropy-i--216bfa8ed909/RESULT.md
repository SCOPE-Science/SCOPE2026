# Twin-blown-up expanders have unbounded quadratic ideal entropy in evolution algebras

## Finding
For a connected finite simple \(d\)-regular graph \(G\) with \(N\ge3\) vertices, independently duplicate every vertex into two nonadjacent *twins*, replacing each old edge with the four edges between its two twin pairs. Call the resulting graph \(H=G[\overline K_2]\). Let \(E_K(H)\) be the symmetric evolution algebra with its standard graph natural basis.

For **every field** \(K\), set \(r=\operatorname{rank}_K(A_G)\). Then
\[
\dim_K E_K(H)^2=r,\qquad
\operatorname{Id}(E_K(H))=\{0\}\cup\{I:E_K(H)^2\subseteq I\subseteq E_K(H)\}.
\]
In particular the nonzero-ideal interval is the **entire subspace lattice** of a quotient of dimension \(c=2N-r\ge N\). Over \(\mathbb F_q\) this gives the *exact* formula
\[
\#\operatorname{Id}(E_{\mathbb F_q}(H))
=1+\sum_{j=0}^{c}{c\brack j}_q,
\qquad c=2N-\operatorname{rank}_{\mathbb F_q}A_G.
\]
Here \({c\brack j}_q=\prod_{i=0}^{j-1}(q^{c-i}-1)/(q^{j-i}-1)\). In particular \(\#\operatorname{Id}(E)\ge1+q^{\lfloor N^2/4\rfloor}\), and for fixed \(q\) its logarithm is \((c^2/4)+O_q(\log(c+1))\) to base \(q\).

This ideal growth persists under **uniform graph expansion**. If \((G_m)\) is any family of \(d\)-regular graphs with orders \(N_m\to\infty\) and Cheeger constants \(h(G_m)\ge h_0>0\), then the corresponding twin-blowups have degree \(2d\) and
\[
h(H_m)\ge \frac{h_0^2}{2d}>0.
\]
For every fixed finite field, their evolution algebras have at least \(q^{\lfloor N_m^2/4\rfloor}\) ideals while remaining bounded-degree expanders in the graph sense.

A small **basic-ideal counterexample** is \(G=K_4\), \(H=K_{2,2,2,2}\) over \(\mathbb F_5\): \(h(H)=3\), \(r=4\), \(c=4\), and the number of ordinary ideals is \(1+\sum_{j=0}^{4}{4\brack j}_5=1121\). Here \(E^2\) is a proper **basic evolution ideal**. Thus positive Cheeger expansion does not imply simplicity, even when ``ideal'' is restricted to natural-basis-extendable evolution ideals.

## Assumptions and scope
Let \(G\) be a finite, connected, loopless, undirected, \(d\)-regular graph, with \(N\ge3\) vertices and \(d\ge2\). Its Cheeger constant is \(h(G)=\min_{0<|S|\le N/2}|\partial_G S|/|S|\). Set \(H=G[\overline K_2]\) with vertex set \(V(G)\times\{0,1\}\) and edge \((u,a)(v,b)\) precisely when \(uv\in E(G)\), for any choices of \(a,b\). Distinct natural basis elements \(e_{u,a}\) multiply to zero, and
\[
e_{u,a}^{2}=\sum_{v\sim_Gu}\left(e_{v,0}+e_{v,1}\right).
\]
The ideal lattice refers to ordinary two-sided algebra ideals; here the algebra is commutative. A *basic evolution ideal* means an ideal with a natural basis extendable to one of the whole algebra. Graphs are unweighted with all nonzero structure constants equal to \(1\). The bound on graph expansion requires a fixed-degree graph expander family as explicit input; no claim is made about all natural bases of singular evolution algebras.

## Proof
**1. Square and rank.** Ordering the twins consecutively gives the adjacency and evolution structure matrix
\[
A_H=A_G\otimes J_2,\qquad J_2=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Since the matrix \(J_2\) has rank \(1\) over every field (including characteristic two), the square of the algebra, spanned by the basis squares, has dimension \(r=\operatorname{rank}_K A_G\). The ambient dimension is \(2N\), so \(c=2N-r\ge N>0\).

**2. Entire ideal lattice.** Let \(0\ne I\lhd E\), and choose \(0\ne x=\sum_i x_i e_i\in I\). For one \(i\) with \(x_i\ne0\), the multiplication rule yields \(e_ix=x_ie_i^2\in I\), whence \(e_i^2\in I\). For any edge \(i\sim j\) of \(H\), multiplication by \(e_j\) gives \(e_je_i^2=e_j^2\in I\). Because \(H\) is connected, propagation along paths shows \(e_j^2\in I\) for every \(j\). Hence \(E^2\subseteq I\). Conversely \(E\cdot E\subseteq E^2\), so **every** vector subspace containing \(E^2\) is an ideal. This proves the lattice equality, and identifies the interval with \(L_K(E/E^2)\). This propagation uses symmetric nonzero edge weights; it need not hold for arbitrary directed evolution graphs.

**3. Exact finite-field counts and growth.** The number of \(j\)-dimensional subspaces of \(\mathbb F_q^c\) is the Gaussian coefficient \({c\brack j}_q\); summing over all dimensions counts the interval, then the separate zero ideal contributes one. To obtain a uniform lower bound, note that \(c\ge N\); a fixed \(N\)-subspace quotient contains at least \(q^{a(N-a)}\) subspaces of dimension \(a\) given by graphs of arbitrary linear maps from a fixed \(a\)-space to a complementary \((N-a)\)-space. Setting \(a=\lfloor N/2\rfloor\) proves the stated bound. The standard product estimate \(q^{j(c-j)}\le {c\brack j}_q\le C_q q^{j(c-j)}\), with \(C_q=\prod_{i\ge1}(1-q^{-i})^{-1}<\infty\), gives the logarithmic asymptotic; the factor \((c+1)\) from summing coefficients contributes only \(O_q(\log(c+1))\).

**4. Expansion does not collapse.** Since \(H\) is \(2d\)-regular, its real adjacency eigenvalues are the \(N\) values \(2\lambda_i(A_G)\), together with \(N\) zero eigenvalues (counted with multiplicity). Thus
\[
2d-\lambda_2(H)=2\min\{d,\,d-\lambda_2(G)\}.
\]
Here \(\lambda_2\) is the second largest adjacency eigenvalue, not the second largest absolute eigenvalue, and \(\lambda_1(G)=d\). For a finite regular graph of degree \(D\), the Cheeger inequalities give
\[
\frac{D-\lambda_2}{2}\le h\le\sqrt{2D(D-\lambda_2)}.
\]
Applying the upper inequality to \(G\) yields \(d-\lambda_2(G)\ge h_0^2/(2d)\), and the lower inequality to \(H\) yields
\[
h(H)\ge\min\{d,\,d-\lambda_2(G)\}\ge\frac{h_0^2}{2d},
\]
because \(h_0\le d\). This bound and the ideal count hold uniformly along any fixed-degree expander family.

**5. Proper basic evolution ideal in eight dimensions.** Take \(G=K_4\) and \(K=\mathbb F_5\). For its four vertices define \(s_i=e_{i,0}+e_{i,1}\) and \(t_i=e_{i,0}-e_{i,1}\). The eight vectors \((s_1,\ldots,s_4,t_1,\ldots,t_4)\) form a new natural basis: products of distinct vectors vanish, including \(s_it_i=e_{i,0}^2-e_{i,1}^2=0\). Moreover
\[
s_i^2=t_i^2=2\sum_{j\ne i}s_j.
\]
Since the adjacency matrix of \(K_4\) is \(J_4-I_4\), with determinant \(-3\ne0\) in \(\mathbb F_5\) up to sign, the four squares span \(\langle s_1,\ldots,s_4\rangle\). Thus \(E^2=\langle s_1,\ldots,s_4\rangle\) is a nonzero proper ideal admitting a natural basis that extends to the whole algebra's natural basis. It is a basic evolution ideal.

For clarity, the Cheeger constant can be computed directly. If a vertex subset contains \(a_i\in\{0,1,2\}\) vertices from the four twin parts and has size \(s=\sum_i a_i\le4\), its edge boundary has size \(6s-s^2+\sum_i a_i^2\). The ratio is at least \(3\); equality occurs for \((a_1,a_2,a_3,a_4)=(1,1,1,1)\). Hence \(h(K_{2,2,2,2})=3\). The resulting proper basic ideal contradicts the assertion that connected symmetric expander evolution algebras must be simple even in the evolution-ideal sense.

## Verification
Run the embedded `verify.py` with standard Python 3; it requires no nonstandard packages. It enumerates all \(2825\) binary subspaces of dimension \(6\), checks each against the ideal condition for \(K_{2,2,2}\), and finds exactly \(68\) ideals, agreeing with the Gaussian formula. It verifies the binary structure-matrix ranks for twin blowups of \(K_3\) and \(K_4\), exhaustively computes their Cheeger constants \(2\) and \(3\), and checks the \(\mathbb F_5\) natural-basis, modular-rank, and \(1121\)-ideal claims for the eight-vertex construction. The output terminates in `VERIFY_OK`. Finite checks support the proof; they do not prove the arbitrary-field and infinite-family statements.

## Relationship to prior work
Giacomelli's 2026 *Expander Evolution Algebras* (arXiv:2605.12672v1, first posted 12 May 2026) defined graph Cheeger expansion for evolution algebras. Its Theorem 3.8 states that a symmetric graph-expander evolution algebra is simple. The concrete eight-dimensional proper basic ideal and the all-family construction identify a counterexample and quantify how many ordinary ideals persist under strong expansion. The counterexamples concern the same symmetric unweighted graph construction and algebraic setting.

Cabrera Casado, Martín Barquero, Martín González, and Tocino (2024) already proved important general connections between evolution ideals, graph hereditary sets, and the interval of ideals above \(E^2\). In particular, the general mechanism that subspaces above \(E^2\) are ideals **is prior background, not a new theorem**. The all-ideal propagation on a connected symmetric support graph is an elementary application of that theory. García-Martínez and Pérez-Rodríguez (2026) also discuss the necessity of perfectness for simplicity in finite-dimensional evolution algebras. The specific new contribution advanced here is the explicit two-twin **uniform-expander counterfamily**, its exact finite-field ideal count and quadratic ideal abundance, and a direct basic-ideal witness contradicting the proposed expander-to-simplicity implication. The standard graph spectral and Cheeger tools are likewise prior mathematics.

## Limitations
This construction is deliberately restricted to the independent-twin blowup of a **symmetric** regular support graph. The ideal-lattice propagation does not claim to cover arbitrary directed evolution algebras. The expansion estimate presupposes an existing fixed-degree expander family, rather than constructing one from scratch. The Gaussian count is for **ordinary** ideals, not for all subalgebras or all basic ideals. The eight-dimensional proper \(E^2\) ideal is separately shown to be basic only over the stated field. The graph's expansion is defined using the displayed natural basis; for singular evolution algebras basis-independence is not asserted. Earlier equivalent formulations using graph twins, lexicographic products, or other algebraic vocabulary remain a literature risk.

## References
1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1, original public version 12 May 2026, https://arxiv.org/html/2605.12672v1. See Definitions 2.9 and 3.5, Theorem 3.8 and Sections 7–9.
2. Y. Cabrera Casado, D. Martín Barquero, C. Martín González, A. Tocino, *Connecting ideals in evolution algebras with hereditary subsets of its associated graph*, *Collectanea Mathematica* 76 (2025), 357–372, first published online 14 March 2024, DOI 10.1007/s13348-024-00435-x. See Proposition 3.4 and Sections 3 and 6.
3. A. García-Martínez, M. Pérez-Rodríguez, *A note on complete evolution algebras*, *Archiv der Mathematik* (2026), DOI 10.1007/s00013-026-02251-0.
4. Standard discrete Cheeger inequalities and adjacency spectra of regular graph products, as used in reference 1 (Section 7).
