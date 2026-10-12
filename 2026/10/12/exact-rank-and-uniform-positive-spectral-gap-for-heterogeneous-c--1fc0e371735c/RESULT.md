# Exact rank and uniform positive spectral gap for heterogeneous clique-cored windmills

## Finding
Let \(b\ge 2\), \(a\ge 1\), and \(r_1,\ldots,r_b\ge 2\) be integers. Consider the unweighted simple graph
\[
G=K_a\vee\bigl(K_{r_1}\sqcup\cdots\sqcup K_{r_b}\bigr),
\]
where the vertices of the core clique are joined to every vertex of every peripheral clique, with no edges between different peripheral cliques. Write \(C_0,C_1,\ldots,C_b\) for the disjoint core/peripheral vertex cells, with sizes \(a,r_1,\ldots,r_b\), and let \(N=a+\sum_{j=1}^b r_j\).

Let \(A\) be the ordinary adjacency matrix. The continuous-time adjacency quantum walk has infinite-time Cesàro average mixing matrix
\[
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T
 e^{\mathrm i tA}\circ e^{-\mathrm i tA}\,dt.
\]
Its **complete real kernel** is
\[
\boxed{\ker\widehat M
 =\bigoplus_{\substack{0\le j\le b\\ |C_j|=2}}
    \operatorname{span}\{e_{x_j}-e_{y_j}\},}
\]
where \(C_j=\{x_j,y_j\}\) when the cell has two vertices. In particular,
\[
\boxed{\operatorname{rank}\widehat M
=N-\mathbf 1_{\{a=2\}}-\sum_{j=1}^b\mathbf 1_{\{r_j=2\}}.}
\]
Hence \(\widehat M\) is positive definite precisely when \(a\ne 2\) and every \(r_j\ge3\).

There is also a quantitative, size-independent conclusion. If \(a\ge2\), every positive eigenvalue of \(\widehat M\) is at least \(1/3\). The bound is sharp: whenever any cell \(C_j\) has size three, its zero-sum internal modes are eigenvectors of \(\widehat M\) of eigenvalue exactly \(1/3\). The same eigenmode statement holds for a three-vertex peripheral cell even when \(a=1\), although the global gap bound is only asserted for \(a\ge2\).

## Assumptions and scope
All edges have weight one, the Hamiltonian is \(A\) rather than the Laplacian, and averaging uses the ordinary infinite-time Cesàro limit. The core size is at least one, the number of peripheral cliques is at least two, and each peripheral clique has at least two vertices. Peripheral sizes may differ arbitrarily. Neither weighted joins, a single peripheral clique, nor singleton peripheral cells are included. Zero eigenvalues of \(\widehat M\) are counted with their full multiplicity.

## Proof
**1. Spectral-projector identity.** For a real symmetric adjacency matrix with distinct eigenvalues \(\lambda\) and orthogonal projectors \(E_\lambda\), spectral expansion and Cesàro integration give
\[
\widehat M=\sum_{\lambda}E_\lambda\circ E_\lambda.
\]
Every summand is positive semidefinite by the Schur product theorem, so the kernel of the sum is the intersection of the kernels of its summands.

**2. Exact eigenprojector at \(-1\).** For each cell \(C_j\), write \(t_j=|C_j|\), and put \(S_j=\sum_{x\in C_j}v_x\). If \(Av=-v\), then, for a vertex of peripheral cell \(C_j\), the eigenvalue equation is \(S_j+S_0=0\). At every core vertex it is \(S_0+\sum_{j=1}^b S_j=0\). Thus \((1-b)S_0=0\); since \(b\ge2\), all cell sums vanish. Conversely, any vector whose sum in every cell vanishes is a \(-1\)-eigenvector because the induced subgraphs on all cells are cliques and the cross-cell sum is zero.

Consequently the **entire** \(-1\)-projector (without an unproved eigenvalue-noncollision assumption) is the block diagonal matrix
\[
E_{-1}=\bigoplus_{j=0}^b R_{t_j},\qquad
 R_t=I_t-\frac1t J_t.
\]
This includes \(R_1=0\) when \(a=1\).

**3. Exact positivity of one Schur square.** Writing \(F=E_{-1}\circ E_{-1}\), its cell block is
\[
R_t\circ R_t
=\left(1-\frac2t\right)I_t+\frac1{t^2}J_t.
\]
The all-ones direction has eigenvalue \((t-1)/t\). Each of the \(t-1\) orthogonal internal directions has eigenvalue \((t-2)/t\). Therefore, when \(t\ge3\) the block is positive definite, when \(t=2\) its kernel is exactly the one-dimensional cell difference direction, and when \(t=1\) the block is zero. It follows that
\[
\ker F=\left(\bigoplus_{\substack{0\le j\le b\\t_j=2}}
 \operatorname{span}\{e_{x_j}-e_{y_j}\}\right)
 \oplus\begin{cases}
 \operatorname{span}\{e_h\},&a=1,\\
 \{0\},&a\ge2,
 \end{cases}
\]
where \(h\) is the sole core vertex if \(a=1\).

**4. Why all pair-difference directions genuinely vanish.** Let \(t_j=2\) and \(\delta_j=e_{x_j}-e_{y_j}\). The transposition of \(x_j\) and \(y_j\) is a graph automorphism, and \(\delta_j\) belongs to the \(-1\)-eigenspace. For every \(\lambda\ne-1\), the projector \(E_\lambda\) annihilates \(\delta_j\), so its columns at \(x_j\) and \(y_j\) agree. Their entrywise squares also agree, giving \((E_\lambda\circ E_\lambda)\delta_j=0\). For \(\lambda=-1\), the relevant block of \(F\) is \(J_2/4\), which also kills \(\delta_j\). Thus \(\delta_j\in\ker\widehat M\) for every size-two cell.

**5. The singleton core cannot add a kernel vector.** Suppose \(a=1\). The graph is connected, so the Perron eigenvector \(u\) of \(A\) can be chosen strictly positive and normalized. The corresponding simple spectral projector \(uu^{\mathsf T}\) has Schur square \(pp^{\mathsf T}\), with \(p_x=u_x^2>0\). Since every permutation inside each peripheral clique is an automorphism, \(p\) is constant within each cell. Hence \(p\) is orthogonal to all the pair differences, but \(p_h>0\). For a vector in \(\ker F\), vanishing of its quadratic form against \(pp^{\mathsf T}\) forces its singleton-core coefficient to vanish. Combining this with Step 4 proves the stated full kernel equality for \(a=1\), while Steps 3–4 already prove it for \(a\ge2\).

**6. Uniform sharp positive gap.** When \(a\ge2\), every block of \(F\) has all nonzero eigenvalues at least \(1/3\), since the smallest for \(t\ge3\) is \((t-2)/t\ge1/3\) and the sole positive eigenvalue for \(t=2\) is \(1/2\). Since \(\ker F=\ker\widehat M\) and \(\widehat M\succeq F\), the Rayleigh quotient on the orthogonal complement of the kernel is at least \(1/3\). For any size-three cell \(C_j\), a vector supported on that cell with zero coordinate sum has \(Fz=z/3\). The orthogonal projectors for every other adjacency eigenvalue annihilate the cell's internal zero-sum subspace; equivalently, their columns are equal within the cell. Therefore their Schur squares annihilate \(z\), so \(\widehat Mz=z/3\). This proves sharpness and the claimed explicit modes.

## Verification
Run the self-contained Python script `verify.py` with NumPy and SymPy installed, from the directory containing this document. It constructs adjacency matrices directly from the graph definition, groups numerical eigenvalues, constructs long-time mixing independently from all spectral projectors, and compares ranks, explicit null directions and gap bounds. Six additional symbolic cases verify the exact \(-1\)-projector, its eigenvalue equation, rank, and internal Schur-square eigenvalues using rational arithmetic.

A replay of the embedded script produced:

`VERIFY_OK exact_projectors=6 independent_graphs=77 max_null_residual=6.106e-16 max_projector_residual=2.220e-16 max_three_clique_mode_residual=1.388e-15`

Finite tests corroborate, but do not constitute, the proof for arbitrary integer parameters; that proof is Steps 1–6 above.

## Relationship to prior work
Godsil's foundational average-mixing theory provides the spectral-idempotent formula and positive-semidefinite framework. Coutinho, Godsil, Guo and Zhan connect mixing rank to spectral commutants and automorphisms. Coutinho, Baptista, Godsil, Spier and Werner provide exact methods for arbitrary integral Hamiltonians. Kimmerling's dissertation establishes full rank for **uniform French windmills** with a single central vertex and equal clique blades; those previously established cases are credited, not presented as new.

The statement here is instead an exhaustive classification for **arbitrary unequal clique-blade sizes and arbitrary core-clique size**, including the sharp core-size-two and blade-size-two defects and an explicit dimension-free lower spectral bound. Neither the general projector identity nor the existing uniform French-windmill full-rank result states these conclusions for the entire defined family. The dissertation's online abstract and indexed excerpts were accessible; its complete PDF was not, so incidental prior coverage beyond the stated published claims remains a residual risk.

## Limitations
No claim is made about a single peripheral clique, singleton peripheral cliques, weighted edges, Laplacian walks, finite-time averages. Complete diagonalization of \(\widehat M\) outside the identified kernel, internal cell modes, and sharp lower bound is not claimed. A sufficiently general unlocated theorem about Schur squares of equitable-partition projectors could potentially imply this classification.

## References
1. C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578, v3 (2011), https://arxiv.org/abs/1103.2578.
2. G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (first posted 2017), https://arxiv.org/abs/1709.03591.
3. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational Quantum Walks*, arXiv:2208.08971 (first posted 2022-08-18), https://arxiv.org/abs/2208.08971; primary MSC 81P68.
4. P. R. Kimmerling, *Continuous-Time Quantum Walks on Windmill Graphs*, Washington State University dissertation (2023), DOI:10.7273/000006322, https://doi.org/10.7273/000006322.
