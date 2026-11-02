# Four-regime entanglement of fourth-distance Boolean-cube graph states

## Finding

For every integer \(d\ge4\), let \(G_d\) be the graph with vertex set \(\mathbb F_2^d\) and an edge between distinct vertices precisely when their Hamming distance is four. Prepare the pure, unweighted qubit graph state \(\lvert G_d\rangle\) by applying a controlled-\(Z\) operation to every edge after preparing \(\lvert+\rangle\) at every vertex. For any one of the \(d\) coordinates, partition the qubits into the \(2^{d-1}\) vertices with coordinate zero and the \(2^{d-1}\) vertices with coordinate one.

The full nonzero spectrum of either reduced density matrix is flat: it contains exactly \(2^{r_d}\) nonzero eigenvalues, each equal to \(2^{-r_d}\), where

\[
r_d=\begin{cases}
2^{d-1},&d\equiv0\pmod4,\\
2^{d-2},&d\equiv1\pmod4,\\
2^{d-2}-2^{(d-2)/2},&d\equiv2\pmod4,\\
2^{d-3}-2^{(d-3)/2},&d\equiv3\pmod4.
\end{cases}
\]

Consequently the base-two von Neumann entropy and every positive-order Rényi entropy of this bipartition are exactly \(r_d\) bits. This four-class law includes maximal mixing of a whole side precisely when \(d\equiv0\pmod4\), and substantial deficits in the other three classes.

For instance, the entropy at dimensions \(d=4,5,6,7,8,9,10,11\) is, respectively, \(8,8,12,12,128,128,240,240\) bits, whereas the largest possible bipartite entropy is \(2^{d-1}\) bits.

## Assumptions and scope

All arithmetic ranks below are over \(\mathbb F_2\). The system is a pure state on exactly \(2^d\) **qubits**, not \(d\) qubits. The graph has no self-loops or edge weights and contains **every** distance-four edge. The cut is by one coordinate, never a general half-set cut. Permuting coordinates gives equivalent cuts. No noise, finite-temperature state, alternate hyperedge phase, or nonbinary local system is included.

## Proof

**1. Exact graph-state spectrum from the cut rank.** Put \(t=2^{d-1}\), let \(C\) be the \(t\times t\) binary adjacency submatrix across the cut, and label the computational basis strings of the two sides by \(a,b\in\mathbb F_2^t\). The normalized graph-state coefficient matrix can be written
\[
K_{a,b}=2^{-t}(-1)^{Q_A(a)+a^{\mathsf T}Cb+Q_B(b)},
\]
where the two \(Q\)'s are the internal-edge quadratic phases. These two phases are diagonal local unitaries and do not affect entanglement. After removing them, direct summation over \(b\) gives
\[
(\rho_A)_{a,a'}=2^{-t}\mathbf1_{\{C^{\mathsf T}(a+a')=0\}}.
\]
If \(r=\operatorname{rank}_{\mathbb F_2}C\), the cosets of \(\ker C^{\mathsf T}\) each form an all-ones matrix block of size \(2^{t-r}\); all other entries vanish. Every block has one eigenvalue \(2^{-r}\) and there are \(2^r\) blocks. Thus it suffices to determine \(r\).

**2. The coordinate cut is the third Hamming adjacency operator.** Identify either side with \(\mathbb F_2^n\), where \(n=d-1\). Across this cut, the distinguished coordinate already contributes distance one, hence \(C_{x,y}=1\) exactly when \(\operatorname{wt}(x+y)=3\). In the group algebra of \(\mathbb F_2^n\), this is multiplication by
\[
A_n=\sum_{|S|=3}\prod_{i\in S}g_i.
\]
Let \(g_i=1+x_i\), identifying the group algebra with the truncated commutative algebra
\[
R_n=\mathbb F_2[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2).
\]
Denote by \(e_j\) the \(j\)-th squarefree elementary symmetric polynomial in the \(x_i\), with \(e_0=1\). Counting the coefficient of any degree-\(j\) squarefree monomial yields
\[
A_n=\binom n3+\binom{n-1}2e_1+(n-2)e_2+e_3,
\qquad e_3=e_1e_2,
\]
with all coefficients reduced modulo two. The second identity follows because each cubic squarefree monomial in \(e_1e_2\) occurs three times and all repeated-variable terms vanish. Evaluating these binomial coefficients modulo two yields the exact four cases
\[
A_n=\begin{cases}
 e_1(1+e_2),&n\equiv0\pmod4,\\
 e_2(1+e_1),&n\equiv1\pmod4,\\
 e_1e_2,&n\equiv2\pmod4,\\
 (1+e_1)(1+e_2),&n\equiv3\pmod4.
\end{cases}
\]
Any \(1+e_j\) is a unit, since \(e_j\) has positive degree in a nilpotent ideal. Multiplying by a unit does not change an operator rank.

**3. Rank of multiplication by \(e_1\).** The form \(e_1=x_1+\cdots+x_n\) is nonzero. An invertible linear variable change over \(\mathbb F_2\) sends it to one coordinate \(u_1\); such changes extend to automorphisms of \(R_n\), because every linear form has square zero. Multiplication by \(u_1\) has rank exactly \(2^{n-1}\).

**4. Rank of multiplication by \(e_2\).** The alternating bilinear form associated with the quadratic exterior element \(e_2\) has matrix with off-diagonal entries one, i.e. \(I+J\). Its rank is \(2m\) for \(n=2m\) or \(n=2m+1\). There is therefore a linear variable change in which
\[
e_2=u_1v_1+\cdots+u_mv_m,
\]
with one unused variable when \(n\) is odd. Multiplication by this element is a square-zero map. On each two-variable tensor factor \(\mathbb F_2[u_i,v_i]/(u_i^2,v_i^2)\), multiplication by \(u_iv_i\) is a square-zero differential whose homology has dimension two, represented by \(u_i,v_i\). The elementary tensor-product Künneth identity over a field gives homology dimension \(2^m\) for the \(2m\)-variable ring, doubled for the unused variable when \(n\) is odd. If a square-zero linear endomorphism acts on a vector space of dimension \(N\) and has homology dimension \(h\), its rank is \((N-h)/2\). Therefore
\[
\operatorname{rank}(e_2\cdot)=
\begin{cases}
2^{n-1}-2^{n/2-1},&n\text{ even},\\
2^{n-1}-2^{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
In particular, the needed \(n\equiv1\pmod4\) case has the second expression.

**5. Rank of multiplication by \(e_1e_2\) for \(n\equiv2\pmod4\).** In this case \(n=2m\ge6\), so \(e_2\) is nondegenerate. A symplectic change of linear variables can arrange simultaneously \(e_1=u_1\) and \(e_2=\sum_{i=1}^m u_iv_i\). Hence
\[
e_1e_2=u_1\sum_{i=2}^m u_iv_i.
\]
Multiplication by \(u_1\) on the first two-variable factor has rank two (its images are \(u_1,u_1v_1\)). Multiplication by \(\sum_{i=2}^m u_iv_i\) on the remaining \(2(m-1)\) variables has rank \(2^{2m-3}-2^{m-2}\) by step 4. Tensor-product ranks multiply, giving
\[
\operatorname{rank}(e_1e_2\cdot)=2^{2m-2}-2^{m-1}=2^{n-2}-2^{(n-2)/2}.
\]
Finally combine the four residue cases in step 2, including the unit case \(n\equiv3\), and replace \(n=d-1\). This gives the displayed \(r_d\), and step 1 gives its entire reduced spectrum for every integer \(d\ge4\). \(\square\)

## Verification

A self-contained exact-rank checker is included as `checker.py`, with dependency information in `requirements.txt`. Run `python checker.py` in an environment with Python 3.9 or later and NumPy at least 1.20. It independently constructs (i) every binary distance-three convolution row, (ii) the truncated-ring multiplication by the explicitly expanded element, and (iii) literal distance-four adjacency cuts of the original \(2^d\)-vertex graph. It compares all three to the closed formula for \(4\le d\le11\), using every coordinate cut for \(4\le d\le8\). Separately, for \(d=4\), it constructs the normalized 16-qubit state directly from all controlled-phase edges and diagonalizes a reduced density matrix without using the cut-rank method.

The recorded run passed 49 independent exact binary-rank comparisons and one direct density-spectrum check. Computations cover only the specified finite dimensions and do not replace the all-dimensional proof.

## Relationship to prior work

The general identity between a pure graph state's Schmidt spectrum and a binary cut-adjacency rank is an established result of Hein, Eisert and Briegel (2003). Hashizume, Bentsen, Weber and Daley (2021) construct and study standard distance-one hypercube graph states, not the full fourth-distance shell treated here. Parez, Bernard, Crampé and Vinet (2022) study free-fermion many-body states on Hamming graphs rather than controlled-\(Z\) graph states. The standard Hamming association scheme supplies the distance relations and complex Krawtchouk eigenvalues, but these alone do not give the nonsemisimple characteristic-two rank of the distance-three cut relation.

Yoshikawa's 2004 work describes modular Hamming adjacency algebras, which is the closest broad algebraic setting. Its abstract does not state the four-regime rank evaluation or graph-state spectrum; the full article could not be inspected, so an existing implication is not definitively excluded. Likewise, a published 2026 result on parity automata computes ranks for the *distance-two* Boolean-cube operator, not this distance-three cut operator. The contribution assessed here is the explicit all-dimension cut-rank and flat-spectrum classification, not the general graph-state rule or the standard Hamming-scheme setup.

## Limitations

Only the pure unweighted qubit graph state on the fourth-distance relation and a one-coordinate cut is classified; no result is asserted for arbitrary subsets of qubits, other distance shells, heterogeneous edge phases, noisy states, or composite local dimensions. The proof does not demonstrate independent priority, nor does a failed search establish that no broader result implies it. The Yoshikawa paper and specialized modular-incidence literature leave a documented originality risk. The included numerical verification is finite, while the mathematical proof applies to every \(d\ge4\).

## References

- M. Hein, J. Eisert, and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first public version 2003-07-18, https://arxiv.org/abs/quant-ph/0307130 .
- T. Hashizume, G. S. Bentsen, S. Weber, and A. J. Daley, *Deterministic Fast Scrambling with Neutral Atom Arrays*, arXiv:2102.13117, first public version 2021-02-25, https://arxiv.org/abs/2102.13117 .
- G. Parez, D. Bernard, N. Crampé, and L. Vinet, *Multipartite information of free fermions on Hamming graphs*, arXiv:2212.09158, first public version 2022-12-18, https://arxiv.org/abs/2212.09158 .
- M. Yoshikawa, *Modular Adjacency Algebras of Hamming Schemes*, Journal of Algebraic Combinatorics 20 (2004), 331–340, DOI 10.1023/B:JACO.0000048521.68503.2b, https://doi.org/10.1023/B:JACO.0000048521.68503.2b (abstract inspected; full text inaccessible).
- E. W. Weisstein, *Hamming Scheme*, MathWorld, https://mathworld.wolfram.com/HammingScheme.html (definitions and complex-eigenvalue context only).
