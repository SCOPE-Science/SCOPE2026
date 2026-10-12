# Full-rank quantum average mixing on inhomogeneous stars: an exact boundary classification
## Finding
For weighted quantum star Hamiltonians with a common leaf on-site energy, there is an exact positive-definiteness threshold at three nonzero spokes. The following theorem includes arbitrary coupling inhomogeneity and an arbitrary central detuning. The sharp one- and two-spoke exceptions are described by an explicit determinant.

For every \(m\ge1\), every \(g_i>0\), and \(\alpha,\beta\in\mathbb R\), let
\[
H=\begin{pmatrix}\alpha&g^{\mathsf T}\\g&\beta I_m\end{pmatrix},\qquad
 g=(g_1,\dots,g_m)^{\mathsf T},
\]
with the central vertex indexed first. Define
\[
G^2=\sum_{i=1}^{m}g_i^2,\quad
w_i=\frac{g_i^2}{G^2},\quad
\delta=\alpha-\beta,\quad
s=\frac{G^2}{\delta^2+4G^2}.
\]
The infinite-time Cesàro average of \(\exp(itH)\circ\exp(-itH)\) is
\[
\boxed{\widehat M=\begin{pmatrix}
1-2s&2s w^{\mathsf T}\\
2s w&\operatorname{diag}(1-2w_i)+2(1-s)ww^{\mathsf T}
\end{pmatrix}.}
\]
It has rank \(m+1\) and is positive definite for all \(m\ge3\). When \(m=2\),
\[
\boxed{\det\widehat M=\frac{\delta^2}{\delta^2+4G^2}
\left(\frac{g_1^2-g_2^2}{G^2}\right)^2,\quad
\operatorname{rank}\widehat M=
\begin{cases}3,&\delta\ne0\ \text{and}\ g_1\ne g_2,\\2,&\text{otherwise}.\end{cases}}
\]
When \(m=1\), the rank is \(2\) for \(\delta\ne0\) and \(1\) for \(\delta=0\).

## Assumptions and scope
The Hamiltonian is a finite real-symmetric matrix on the central site and \(m\) leaves. Every leaf communicates only with the center, all spoke couplings are strictly positive, every leaf has the same on-site energy \(\beta\), and the central energy is arbitrary. Independent phases of nonzero real spoke couplings can be removed by a diagonal sign gauge, so the same mixing statement also holds for nonzero signed real spokes when equality of their **magnitudes** is used in the two-spoke condition. There are no claims for unequal leaf energies, zero spoke couplings, or complex flux-bearing edges.

A common scalar energy shift \(\beta I_{m+1}\) does not alter transition probabilities. Accordingly the proof uses \(\delta=\alpha-\beta\). The limit exists because the spectrum is finite: expanding the exponential in spectral idempotents annihilates every unequal-eigenvalue frequency in the Cesàro limit.

## Proof
Write \(u=g/G\), so \(\|u\|=1\), and let the zero-eigenspace projector after subtracting the common leaf energy be
\[
E_0=\begin{pmatrix}0&0\\0&I_m-uu^{\mathsf T}\end{pmatrix}.
\]
For \(m=1\), this projector is zero. For every \(m\), the two-dimensional subspace spanned by the central vector and the normalized radial leaf vector \(u\) is invariant. There the Hamiltonian minus \(\beta I\) is the matrix
\[
\begin{pmatrix}\delta&G\\G&0\end{pmatrix},
\]
with two distinct eigenvalues \(\lambda_\pm=(\delta\pm\sqrt{\delta^2+4G^2})/2\), both nonzero because \(G>0\). Thus the projectors \(E_+,E_-,E_0\) are mutually orthogonal, and there are exactly two radial eigenvalues plus the possibly absent zero eigenvalue.

Write \(\Delta=\sqrt{\delta^2+4G^2}\). The squared central coordinates of normalized eigenvectors for the two radial eigenvalues are
\[
p_\pm=\frac12\left(1\pm\frac{\delta}{\Delta}\right).
\]
Their squared radial-leaf coordinates are \(1-p_\pm\), and \(p_+p_-=s\). For each leaf index \(i\), the squared site coordinate in these eigenvectors is \((1-p_\pm)w_i\). Direct Schur-squaring of the three projectors therefore gives the displayed exact block matrix. In particular, the central entry is \(p_+^2+p_-^2=1-2s\); the center-to-leaf entry is \(2sw_i\); and the leaf block is the Schur square of \(I_m-uu^{\mathsf T}\) plus \((1-2s)ww^{\mathsf T}\).

For the full-rank assertion, note that each \(E\circ E\) is positive semidefinite. Let \(P=I_m-uu^{\mathsf T}\) and \(m\ge3\). We prove \(P\circ P\) positive definite. If a real vector \(x=(x_i)\) satisfies \(x^{\mathsf T}(P\circ P)x=0\), then
\[
0=\|P\operatorname{diag}(x)P\|_{\mathrm F}^2.
\]
In particular \(z^{\mathsf T}\operatorname{diag}(x)z=0\) for each \(z\perp u\). Choose \(z=u_j e_i-u_i e_j\) for each pair of distinct leaf indices. It follows that
\[
x_i u_j^2+x_j u_i^2=0
\quad\Longleftrightarrow\quad
\frac{x_i}{u_i^2}+\frac{x_j}{u_j^2}=0.
\]
All \(u_i\) are nonzero. For any three distinct indices, these pairwise equations force the three ratios to vanish; hence every \(x_i=0\). Thus \(P\circ P\) is strictly positive definite on the leaf coordinates. If a vector in the full space has zero quadratic form under \(\widehat M\), its leaf component must therefore vanish. The radial projector squares have positive center-center entries \(p_\pm^2\), so its remaining central component also vanishes. This proves \(\widehat M\succ0\) for all \(m\ge3\), including all coupling ratios and all detunings.

For \(m=2\), substitute \(w_1+w_2=1\) into the three-by-three block expression and expand its determinant:
\[
\det\widehat M=(1-4s)(w_1-w_2)^2=
\frac{\delta^2}{\delta^2+4G^2}
\left(\frac{g_1^2-g_2^2}{G^2}\right)^2.
\]
If this determinant is nonzero, the rank is three. When it is zero, the rank is exactly two rather than one, since the matrix is symmetric, nonnegative, stochastic and its center diagonal entry \(1-2s\ge1/2>1/3\); a rank-one symmetric stochastic matrix would be \(J_3/3\). Finally, for \(m=1\), the mixing matrix is the two-by-two stochastic matrix with diagonal \(1-2s\) and off-diagonal \(2s\). Its eigenvalues are \(1\) and \(1-4s=\delta^2/(\delta^2+4G^2)\), giving the claimed final boundary.

## Verification
The standalone `verify_star.py` computes the exact-rational block formula and its exact rank for 315 parameter profiles with one through seven leaves. It independently diagonalizes the original star Hamiltonian for 405 profiles with one through nine leaves, assembles the average mixing matrix from each *distinct full spectral projector*, and checks all 17,280 entries against the formula, with maximum absolute discrepancy below \(1.3\times10^{-15}\). This checks cases of zero and nonzero detuning, repeated spoke magnitudes, and heterogeneous positive spokes. Run `python verify_star.py` with Python, NumPy and SciPy installed. The infinite-parameter result comes from the proof, not from finite sampling.

## Relationship to prior work
The general spectral-projector identity for quantum average mixing and its commutant interpretation were established by Coutinho, Godsil, Guo and Zhan (2017/2018). Coutinho and collaborators (2022) give exact methods for average mixing of integral graph Hamiltonians. Carlson and collaborators (2006) treat *instantaneous universal mixing* on weighted stars, a different property from positive-definite infinite-time mixing. Kimmerling (2023) establishes full rank for unweighted simple star graphs, which is recovered here only as the equal-coupling, zero-detuning subcase for three or more leaves. The present theorem makes the long-time positivity stable under **arbitrary** heterogeneous positive edge weights and central detuning, and classifies the two smaller-star degeneracies exactly. It does not purport to rediscover the unweighted star conclusion or the Schur-projector formula.

## Limitations
No claim is made for nonuniform leaf on-site energies, general arrowhead matrices with distinct leaf potentials, complex fluxes, or stars with inactive spokes. Positive definiteness concerns the Cesàro-averaged mixing matrix; it does not imply instantaneous uniform mixing, perfect state transfer, or uniform long-time probabilities. No positive lower bound on its smallest eigenvalue is asserted uniformly as a spoke coupling tends to zero. The closest dissertation's open-access PDF could not be inspected in full through the available retrieval route, so beyond its abstract an explicit comparison remains a literature risk. A stronger unlocated theorem might encompass the weighted and detuned form. No independent audit has been performed.

## References
- G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first posted 2022-08-18), https://arxiv.org/abs/2208.08971 .
- G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1; Electronic Journal of Combinatorics 25 (2018), P4.14, https://arxiv.org/abs/1709.03591 .
- W. Carlson, A. Ford, E. Harris, J. Rosen, C. Tamon, K. Wrobel, *Universal Mixing of Quantum Walk on Graphs*, arXiv:quant-ph/0608044v1, https://arxiv.org/abs/quant-ph/0608044 .
- P. R. Kimmerling, *Continuous-Time Quantum Walks on Windmill Graphs*, Washington State University dissertation (2023), doi:10.7273/000006322, https://doi.org/10.7273/000006322 .
