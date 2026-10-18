# Exact average-mixing rank of a complete bipartite quantum network with one defective bond

## Finding

Let \(a,b\ge2\) be integers, and let \(g\ge0\) be real. Starting from the complete bipartite graph \(K_{a,b}\) with all edge weights one, replace the coupling of a single edge joining the two parts by \(g\). Let \(H_g\) be the resulting real symmetric adjacency Hamiltonian and let
\[
\widehat M_g=\lim_{T\to\infty}\frac1T\int_0^T
\bigl(e^{itH_g}\circ e^{-itH_g}\bigr)\,dt
\]
be its infinite-time quantum average-mixing matrix (\(\circ\) denotes entrywise multiplication).

**Theorem.** For every such \(a,b,g\),
\[
\operatorname{nullity}\widehat M_g=
\begin{cases}
\mathbf1_{\{a=2\}}+\mathbf1_{\{b=2\}},&g=1,\\
\mathbf1_{\{a\le3\}}+\mathbf1_{\{b\le3\}}
+\mathbf1_{\{a=b\ge3\}},&g\ne1.
\end{cases}
\]
In particular, for every nonunit bond \(g\ge0\), including the severed bond \(g=0\), the rank is independent of its strength. Relative to the unmodified network, a defective bond reduces average-mixing rank by precisely
\[
\mathbf1_{\{a=3\}}+\mathbf1_{\{b=3\}}+\mathbf1_{\{a=b\ge3\}}.
\]
The average-mixing matrix for a defective bond is positive definite if and only if \(a,b\ge4\) and \(a\ne b\). Thus the balanced networks of order at least eight acquire exactly one null mode, while the \(3\)-by-\(3\) network acquires three.

## Assumptions and scope

Both bipartition sizes are at least two; all unmodified edges have real coupling one; exactly one cross-edge has nonnegative coupling \(g\). There are no onsite potentials, and evolution uses the ordinary weighted adjacency Hamiltonian, not the Laplacian. The time average is the Cesàro limit over continuous time, and the rank is over \(\mathbb R\). The theorem includes \(g=0\), \(g=1\), all nonunit positive real couplings, balanced and unbalanced parts, and the smallest allowed parts.

## Proof

**1. Kernel criterion.** For a real symmetric Hamiltonian with distinct-eigenvalue projectors \(E_\lambda\), the spectral expansion yields
\[
\widehat M=\sum_\lambda E_\lambda\circ E_\lambda.
\]
For \(x\in\mathbb R^{a+b}\), put \(D_x=\operatorname{diag}(x)\). Orthogonal projection and cyclicity of trace give
\[
x^{\mathsf T}\widehat Mx
=\sum_\lambda\operatorname{tr}(D_xE_\lambda D_xE_\lambda)
=\sum_\lambda\|E_\lambda D_xE_\lambda\|_F^2.
\]
Consequently \(x\in\ker\widehat M\) if and only if \(E_\lambda D_xE_\lambda=0\) for every distinct eigenvalue. This argument remains valid when eigenvalues are repeated.

**2. Four-cell reduction for \(g\ne1\).** Label the two endpoints of the modified edge \(u\) and \(v\), and write the remaining sets as \(A_*\), \(B_*\), of respective sizes \(p=a-1\) and \(q=b-1\). The vectors \(e_u\), \(\mathbf1_{A_*}/\sqrt p\), \(e_v\), \(\mathbf1_{B_*}/\sqrt q\) span an invariant bright subspace, on which the Hamiltonian is
\[
\mathcal H=\begin{pmatrix}0&B\\ B^{\mathsf T}&0\end{pmatrix},
\qquad
B=\begin{pmatrix}g&\sqrt q\\ \sqrt p&\sqrt{pq}\end{pmatrix}.
\]
Its orthogonal complement consists of the two zero-energy dark spaces
\[
U_A=\{z:\operatorname{supp}(z)\subseteq A_*,\ \sum_{i\in A_*}z_i=0\},
\quad
U_B=\{z:\operatorname{supp}(z)\subseteq B_*,\ \sum_{i\in B_*}z_i=0\}.
\]
Because \(\det B=\sqrt{pq}(g-1)\ne0\), the two singular values \(\sigma_1>\sigma_2>0\) are nonzero. They are distinct because \((BB^{\mathsf T})_{12}=\sqrt p(g+q)>0\) (recall \(g\ge0,q\ge1\)). Therefore the four nonzero eigenvalues are exactly \(\pm\sigma_1,\pm\sigma_2\), all simple; the entire zero eigenspace is \(U_A\oplus U_B\).

**3. Dark constraints.** On a \(k\)-vertex dark cell its zero projector is \(P_k=I_k-J_k/k\) (taken as zero for \(k=1\)). The equation \(P_k\operatorname{diag}(y)P_k=0\) imposes no restriction for \(k=1\). For \(k=2\), testing the contrast vector gives \(y_1+y_2=0\). For \(k\ge3\), testing every vector \(e_i-e_j\) gives \(y_i+y_j=0\) for all distinct \(i,j\), hence all \(y_i=0\). Thus the dark conditions leave the marked coordinate and one additional free contrast or singleton coordinate exactly when the corresponding part size is at most three. After both dark conditions, the dimension of possible \(x\) is
\[
2+\mathbf1_{\{a\le3\}}+\mathbf1_{\{b\le3\}}.
\]
Moreover the mean of the unmarked coordinates in a part of size at least three must vanish.

**4. Bright constraints and their rank.** Choose orthonormal left and right singular vectors \(u_k=(u_{k1},u_{k2})\) and \(v_k=(v_{k1},v_{k2})\) for \(B\), indexed by the singular values \(\sigma_k\). The normalized bright eigenvectors for \(\pm\sigma_k\) are \((u_k,\pm v_k)/\sqrt2\), and the two signs have the same componentwise squares. Writing \(m_A=p^{-1}\sum_{A_*}x_i\), \(m_B=q^{-1}\sum_{B_*}x_i\), the four nonzero-eigenvalue kernel equations reduce to precisely two equations:
\[
u_{k1}^2x_u+u_{k2}^2m_A+v_{k1}^2x_v+v_{k2}^2m_B=0,
\qquad k=1,2.
\]
Let \(\Delta=\sigma_1^2-\sigma_2^2>0\). From the spectral projectors of \(BB^{\mathsf T}\) and \(B^{\mathsf T}B\),
\[
u_{11}^2-v_{11}^2=\frac{(BB^{\mathsf T})_{11}-(B^{\mathsf T}B)_{11}}{\Delta}
=\frac{q-p}{\Delta}.
\]
If \(p,q\ge2\), the dark constraints give \(m_A=m_B=0\). As \(u_{21}^2=1-u_{11}^2\), \(v_{21}^2=1-v_{11}^2\), the two bright equations on \((x_u,x_v)\) are independent exactly when \(p\ne q\); when \(p=q\), they impose the single condition \(x_u+x_v=0\). Note that \(p=q\ge2\) means \(a=b\ge3\).

If \(p=1\), the columns corresponding to \(x_u,m_A\) in the two bright equations are independent, since
\[
u_{11}^2-u_{12}^2
=\frac{(BB^{\mathsf T})_{11}-(BB^{\mathsf T})_{22}}{\Delta}
=\frac{g^2-1}{\Delta}\ne0.
\]
If \(q=1\), the analogous determinant on the \((x_v,m_B)\) columns is \((g^2-1)/\Delta\ne0\). This also proves the bright rank is two when both \(p=q=1\). Thus the rank of the bright constraints on the remaining variables is two except when \(a=b\ge3\), when it is one. Subtracting this rank from the dimension in Step 3 proves the nonunit-bond nullity formula.

**5. Unit bond.** For \(g=1\), the unweighted complete bipartite Hamiltonian has nonzero eigenvalues \(\pm\sqrt{ab}\) and zero projector \(P_a\oplus P_b\). The preceding contrast argument shows \((P_a\oplus P_b)D_x(P_a\oplus P_b)=0\) leaves exactly one difference coordinate in each part of size two and none for parts of size at least three. These differences have zero sum on their respective parts and hence also annihilate both bright rank-one compressions. This establishes the unit-bond nullity formula and completes the proof.

## Verification

Run `python verify.py` with Python 3, SymPy and NumPy installed. The checker constructs the full Hamiltonian from its definition, solves the **exact rational commutant equations** to recover the rank of the average-state Gram matrix, and separately constructs spectral projectors numerically, including grouped repeated eigenvalues. It checks the stated rank for \(2\le a,b\le7\) at \(g\in\{0,1/2,1,2,3\}\) using exact arithmetic, and for \(g\in\{0,1/4,1/2,1,3/2,2,3,7\}\) spectrally. No interpolation or extrapolation is used in the proof. The checker is corroborative rather than an exhaustive verification over all integers or real couplings.

## Relationship to prior work

Coutinho, Godsil, Guo and Zhan [1] establish the commutant/average-mixing correspondence used in Step 1, along with general restrictions for Hamiltonians with simple eigenvalues; the latter simple-spectrum hypothesis does not hold in most of this family because the zero eigenspace is repeated. Coutinho, Baptista, Godsil, Spier and Werner [2] provide exact spectral algorithms for quantum average mixing, but no closed single-bond biclique rank law. Godsil, Guo, Kempton and Lippner [3] analyze edge perturbations of strongly regular graphs for state transfer and characteristic polynomials. Their framework intersects the balanced biclique case, but the inspected work does not give the rank/nullspace classification above. Carlson et al. [5] study instantaneous universal mixing on weighted complete multipartite graphs; their global weight-design property does not supply an all-start-vertex Cesàro-rank classification for one modified bond. The unmodified \(g=1\) baseline is included to make the discontinuity precise; the classification under one nonunit edge is the contribution here.

## Limitations

This theorem concerns only a **single** defective cross-edge, with nonnegative real weight and unchanged unit weights elsewhere. No result is asserted for signed couplings, multiple defective edges, onsite potentials, Laplacian evolution, instantaneous state transfer, or numerical mixing times. The claim is a mathematical derivation, not an assertion of absolute publication priority; an unlocated specialized edge-defect result could overlap despite the recorded searches. Finite checks cover only the explicit sample range and do not prove the unrestricted theorem.

## References

[1] G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix* (2018), Electronic Journal of Combinatorics 25(4), P4.14; arXiv:1709.03591. https://arxiv.org/abs/1709.03591

[2] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks* (first public version 2022-08-18), SIAM Journal on Applied Algebra and Geometry 7 (2023); arXiv:2208.08971, primary MSC 81P68. https://arxiv.org/abs/2208.08971

[3] C. Godsil, K. Guo, M. Kempton, G. Lippner, *State transfer in strongly regular graphs with an edge perturbation*, Journal of Combinatorial Theory, Series A (2020); arXiv:1710.02181. https://arxiv.org/abs/1710.02181

[4] G. Coutinho, *Selected open problems in continuous-time quantum walks* (2024), section on average mixing and rank. https://doi.org/10.1515/spma-2024-0025

[5] W. Carlson, A. Ford, E. Harris, J. Rosen, C. Tamon, K. Wrobel, *Universal Mixing of Quantum Walk on Graphs* (2007), Quantum Information and Computation 7, 738–751; arXiv:quant-ph/0608044. https://arxiv.org/abs/quant-ph/0608044
