# Parity-controlled Schmidt spectra of two-coordinate Johnson graph-state cuts

## Finding
For every integer \(n\ge4\) and \(1\le k\le n-1\), let \(J(n,k)\) be the Johnson graph whose vertices are the \(k\)-subsets of \([n]\), with adjacency when two sets differ by one exchange. Prepare the standard unweighted qubit graph state on this graph. Fix any two coordinates, and assign a graph-state qubit to subsystem \(A\) exactly when the corresponding subset contains zero or both of the two coordinates; assign all other qubits to \(B\).

Let \(s_{n,k}\) be the base-two von Neumann entropy of the reduced state on \(A\). Then
\[
s_{n,k}=\begin{cases}
\binom{n-2}{k-1},&n\text{ odd},\\
\binom{n-2}{k-1}-\binom{n-4}{k-2},&n\text{ even}.
\end{cases}
\]
Binomial coefficients with lower index outside the range from zero to the upper index are defined to vanish. The complete reduced-state spectrum consists of exactly \(2^{s_{n,k}}\) eigenvalues equal to \(2^{-s_{n,k}}\), with all remaining eigenvalues zero. Thus the base-two Rényi entropies of all positive orders, including the limiting von Neumann case, equal \(s_{n,k}\).

When \(n\) is even, the fractional entanglement-rank deficit relative to the odd-\(n\) expression at the same Boolean middle layer is
\[
\frac{\binom{n-4}{k-2}}{\binom{n-2}{k-1}}
=\frac{(k-1)(n-k-1)}{(n-2)(n-3)}.
\]
For central layers this fraction tends to one quarter as the number of coordinates grows. This order-one parity effect is not a finite-size perturbative correction.

## Assumptions and scope
The graph is simple, and its pure graph state has one qubit per Johnson-graph vertex and a controlled-phase gate on each graph edge applied to the initial product state of \(|+\rangle\) qubits. Subsystems contain qubits (not Johnson-graph coordinates). Entropies are base-two. The two distinguished coordinates are arbitrary; graph automorphisms make their choice immaterial. The theorem includes \(k=1\) and \(k=n-1\) under the stated binomial convention. Only this distinguished two-coordinate parity bipartition is claimed.

## Proof
**Step 1 (exact cross-cut matrix).** Set \(N=n-2\), \(r=k-1\), and let \(E\) be the \(N\) undistinguished coordinates. The \(B\)-vertices are exactly \(\{1\}\cup R\) and \(\{2\}\cup R\) for \(R\subset E\) with \(|R|=r\). The \(A\)-vertices are the subsets \(T\subset E\) with \(|T|=r+1\), and \(\{1,2\}\cup Q\) with \(Q\subset E\), \(|Q|=r-1\). A Johnson edge crosses the cut precisely when \(R\subset T\) in the first class or \(Q\subset R\) in the second. In particular, the two cross-cut columns indexed by the same \(R\) are identical, so deleting one from each pair preserves the rank over \(\mathbb F_2\). The remaining linear map is the vertical stack \((U_r,D_r)\) of the unsigned up- and down-incidence maps on the \(r\)-th Boolean layer of \(E\).

**Step 2 (exterior-algebra computation).** Let \(V=\mathbb F_2^N\) with standard basis \(e_i\), and identify the Boolean \(r\)-layer with \(\bigwedge^r V\). Put \(u=\sum_{i=1}^N e_i\) and let \(f\in V^*\) send every basis vector to one. Because the field has characteristic two, the unsigned incidence maps are \(U\omega=u\wedge\omega\) and \(D\omega=\iota_f\omega\), respectively. They satisfy the contraction identity
\[
D U+U D=f(u)I=(N\bmod 2)I.
\]
For odd \(N\), simultaneous annihilation by \(U\) and \(D\) therefore forces \(\omega=0\), so the stack is injective and its rank is \(\binom Nr\).

For even \(N\), the nonzero vector \(u\) lies in \(\ker f\). Choose \(v\) with \(f(v)=1\) and a complementary subspace \(W\) such that \(V=\langle v\rangle\oplus\langle u\rangle\oplus W\) and \(\ker f=\langle u\rangle\oplus W\), where \(\dim W=N-2\). The contraction kernel on exterior degree \(r\) is \(\bigwedge^r\ker f\), and an element of this kernel decomposes uniquely as \(a+u\wedge b\), with \(a\in\bigwedge^r W\), \(b\in\bigwedge^{r-1}W\). Wedge multiplication by \(u\) kills this element exactly when \(a=0\). Hence
\[
\ker U\cap\ker D=u\wedge\bigwedge^{r-1}W,
\qquad \dim(\ker U\cap\ker D)=\binom{N-2}{r-1}.
\]
Rank-nullity gives \(\binom Nr-\binom{N-2}{r-1}\), including boundary layers. Since \(N\) and \(n\) have the same parity, this proves the stated entropy exponent.

**Step 3 (full reduced-state spectrum).** Let \(C\) be the binary cross-cut adjacency matrix with rows indexed by \(A\). The computational-basis graph-state amplitudes have the form \(2^{-|V(J)|/2}(-1)^{q_A(x)+q_B(y)+x^T C y}\), where \(q_A,q_B\) depend only on internal edges on their respective sides. After tracing out \(B\), a diagonal unitary conjugation removes \(q_A\). The remaining reduced matrix has entries \(2^{-|A|}\) when \(C^T(x+x')=0\), and zero otherwise, by character orthogonality over \(\mathbb F_2\). Let \(s=\operatorname{rank}_{\mathbb F_2}C\). The kernel of \(C^T\) has \(2^{|A|-s}\) elements; grouping basis vectors by its cosets gives exactly \(2^s\) constant all-ones blocks, each of size \(2^{|A|-s}\) and scaled by \(2^{-|A|}\). Thus the spectrum is flat with \(2^s\) positive eigenvalues, each \(2^{-s}\). The formula for all positive Rényi entropies follows.

## Verification
The standalone standard-library program `verify_johnson_cut.py` constructs Johnson-graph adjacency from distinct subsets, forms the actual cross-cut binary matrix, and computes its rank via independent bitset Gaussian elimination. It passed all 75 pairs with \(4\le n\le13\) and \(1\le k<n\). Separately, for each of seven configurations with \(n=4\) or \(n=5\), it forms all controlled-phase graph-state amplitudes and computes the partial trace as an exact integer matrix; the projector equation and trace are checked without floating-point arithmetic. Running `python3 verify_johnson_cut.py` prints `VERIFY_OK`. These finite computations corroborate, but do not replace, the preceding all-parameter proof.

## Relationship to prior work
Hein, Eisert and Briegel establish graph-state entanglement connections to binary adjacency ranks and the general stabilizer framework. The original contribution here is not that general identity, but its exact evaluation and complete Schmidt spectrum for the specified all-parameter Johnson-graph cut, including a parity-controlled rank defect. Ghorbani and collaborators analyze subset-inclusion matrices and associated normal forms; their work underpins the broader finite-set incidence context, but its examined single-inclusion statements do not directly supply the simultaneous up/down kernel evaluation in this graph-state cut. Bernard, Crampé and Vinet study entanglement of free-fermion ground states on Johnson graphs, a different state and correlation operator from the controlled-phase graph state considered here. An indexed account of Johnson two-coordinate harmonic concentration treats rational band-limited function spaces rather than this binary graph-state cut; its full source was unavailable, so no claim of exhaustive exclusion is made. Historical rank results for single inclusion matrices remain a possible route to an equivalent derived identity; priority against specialized prior literature has not been independently established.

## Limitations
This result concerns pure, uniform, unweighted **qubit** graph states and one automorphism-invariant bipartition. It neither treats arbitrary Johnson-graph cuts nor qudits of odd local dimension, mixed states, noisy dynamics, or physical preparation cost. The proof establishes the exact mathematical statement, not the historical uniqueness of the formula; some relevant older papers were accessible only through abstracts or summaries. Independent scientific validation has not been performed.

## References
1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (publicly posted 2003-07-18), https://arxiv.org/abs/quant-ph/0307130.
2. E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, *Inclusion Matrices and Chains*, arXiv:0709.3144 (2007-09-20), https://arxiv.org/abs/0709.3144.
3. P.-A. Bernard, N. Crampé, L. Vinet, *Entanglement of Free Fermions on Johnson Graphs*, arXiv:2104.11581 (2021-04-23), https://arxiv.org/abs/2104.11581.
4. N. Linial, B. Rothschild, *Incidence Matrices of Subsets—A Rank Formula* (1981), https://doi.org/10.1137/0602037 (abstract-level comparison only).
