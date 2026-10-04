# Exact dimer reduction and EP2 rigidity for balanced bipartite gain-loss Hamiltonians
## Finding
For every real \(m\times m\) matrix \(U\) and \(\gamma\ge 0\), the balanced bipartite Hamiltonian \[H_\gamma(U)=\begin{pmatrix}i\gamma I_m&U\\U^T&-i\gamma I_m\end{pmatrix}\] is orthogonally similar, after a permutation, to the direct sum \[\bigoplus_{j=1}^m\begin{pmatrix}i\gamma&\sigma_j\\\sigma_j&-i\gamma\end{pmatrix},\] where \(\sigma_j\) are the singular values of \(U\). Hence \[\det(\lambda I-H_\gamma)=\prod_{j=1}^m(\lambda^2+\gamma^2-\sigma_j^2),\] every eigenvalue lies on the real or imaginary axis, the exact real/imaginary eigenvalue fractions are the empirical singular-value counts above/below \(\gamma\), and for \(\gamma>0\) every exceptional point occurs exactly when \(\gamma\) equals a positive singular value and consists only of independent size-two Jordan blocks; higher-order Jordan blocks cannot occur within this model.

This gives an exact all-size reduction of the balanced gain-loss bipartite matrix used in the literature. In particular, if \(n_>(\gamma)\), \(n_<(\gamma)\), and \(n_=(\gamma)\) count singular values of \(U\) that are respectively greater than, less than, and equal to \(\gamma\), then the matrix has \(2n_>(\gamma)\) nonzero real eigenvalues, \(2n_<(\gamma)\) nonzero purely imaginary eigenvalues, and algebraic zero multiplicity \(2n_=(\gamma)\). For \(\gamma>0\), each singular value equal to \(\gamma\) contributes one size-two Jordan block at zero.

## Assumptions and scope
Let \(U\in\mathbb{R}^{m\times m}\) and \(\gamma\ge 0\). The two bipartite parts have equal size, the off-diagonal blocks are \(U\) and \(U^T\), and the gain/loss blocks are scalar \(\pm i\gamma I_m\). These are exactly the structural assumptions in the bipartite Hamiltonian of Moreno-Rodriguez, Martinez-Martinez, Mendez-Bermudez, and Benisty. The result does not require \(U=U^T\), so it applies both to their PT-symmetric subfamily and to their more general pseudo-Hermitian subfamily.

The claim concerns the finite-dimensional spectral problem only. It does not assert a closed radical formula for the singular values of an arbitrary random matrix, nor does it cover unequal gain/loss strengths, non-scalar diagonal blocks, directed couplings with an independent lower-left block, or nonlinear dynamics.

## Proof
Take a singular-value decomposition \(U=P\Sigma Q^T\), where \(P,Q\) are real orthogonal and \(\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_m)\) with \(\sigma_j\ge0\). With \(S=\operatorname{diag}(P,Q)\), orthogonal similarity gives
\[
S^T H_\gamma(U)S=
\begin{pmatrix}
i\gamma I_m&\Sigma\\
\Sigma&-i\gamma I_m
\end{pmatrix}.
\]
Permuting the basis to interlace the two singular-vector coordinates yields the direct sum of \(2\times2\) matrices
\[
B_j=\begin{pmatrix}i\gamma&\sigma_j\\\sigma_j&-i\gamma\end{pmatrix}.
\]
Each block satisfies
\[
B_j^2=(\sigma_j^2-\gamma^2)I_2,
\qquad
\det(\lambda I_2-B_j)=\lambda^2+\gamma^2-\sigma_j^2.
\]
Therefore its eigenvalues are \(\pm\sqrt{\sigma_j^2-\gamma^2}\). They are real when \(\sigma_j>\gamma\), purely imaginary when \(\sigma_j<\gamma\), and both zero when \(\sigma_j=\gamma\). Multiplying the block characteristic polynomials proves the stated factorization and the exact eigenvalue counts.

For the Jordan statement, suppose \(\gamma>0\) and \(\sigma_j=\gamma\). Then \(B_j^2=0\), while \(B_j\ne0\) and \(\operatorname{rank}B_j=1\). Hence \(B_j\) is similar over \(\mathbb{C}\) to the single nilpotent block \(J_2(0)\). If the singular value \(\gamma\) has multiplicity \(r\), the SVD reduction produces exactly \(r\) independent copies of \(J_2(0)\), never a block larger than two. When \(\gamma=0\), the Hamiltonian is Hermitian; a zero singular value contributes a zero \(2\times2\) block and is semisimple rather than exceptional.

## Verification
The proof is algebraic and does not rely on numerical experiments. Two independent identities provide a direct replay: first, block multiplication gives
\[
H_\gamma(U)^2=\operatorname{diag}(UU^T-\gamma^2I_m,\ U^TU-\gamma^2I_m),
\]
whose two diagonal blocks have eigenvalues \(\sigma_j^2-\gamma^2\); second, the explicit SVD similarity above resolves the square-root ambiguity and the Jordan structure at threshold.

As a boundary check, the archive-era birefringent PT coupler of Li, Zezyulin, Konotop, and Kevrekidis has a linear spectrum consisting of two double eigenvalues \(\pm\sqrt{2k^2-\gamma^2}\), with threshold \(\gamma=\sqrt{2}k\). This is consistent with the same dimer square-root mechanism. The later bipartite-graph paper writes its Hamiltonian with off-diagonal blocks \(U\) and \(U^T\), derives explicit formulas only for \(N=4\), and then numerically studies real/imaginary eigenvalue fractions at larger \(N\); the present reduction applies at every even \(N\).

## Relationship to prior work
The Jordan-Wielandt/Hermitian-dilation observation that the eigenvalues of \(\begin{psmallmatrix}0&U\\U^T&0\end{psmallmatrix}\) are the signed singular values of \(U\) is standard matrix analysis. The contribution here is not that zero-gain fact by itself. The literature-specific point is that adding the balanced scalar gain/loss term preserves a complete SVD-mode decoupling, so the non-Hermitian model used for large random bipartite networks has an exact all-size spectral reduction, exact real/imaginary counts, and an EP-order restriction that are not stated in the inspected source paper.

Li et al. (arXiv:1212.1676, first public 2012-12-07) give an archive-era four-mode PT example with an exact square-root transition. Moreno-Rodriguez et al. (arXiv:2212.13642, first public 2022-12-27; later Chaos 34, 053116 (2024), DOI 10.1063/5.0199771) formulate the equal-part bipartite Hamiltonian used here and numerically characterize fractions of real and imaginary eigenvalues for larger systems. Direct inspection of the latter found no singular-value reduction.

## Limitations
The algebraic reduction is elementary once the SVD is tried, so there is residual literature risk that the same application has appeared under different terminology despite targeted searches. The originality claim is therefore limited to the explicit reduction and consequences for this balanced bipartite gain-loss model relative to the inspected literature, not to SVD or Jordan-Wielandt theory generally.

The statement that no higher-order exceptional point occurs is conditional on remaining inside the exact block family above. Additional couplings, unequal diagonal gain/loss, nonlinearities, or parameter-dependent perturbations can couple the dimer sectors and may permit larger Jordan blocks.

## References
1. K. Li, D. A. Zezyulin, V. V. Konotop, and P. G. Kevrekidis, “Parity-time symmetric optical coupler with birefringent arms,” arXiv:1212.1676; Physical Review A 87, 033812 (2013), DOI 10.1103/PhysRevA.87.033812.
2. L. A. Moreno-Rodriguez, C. T. Martinez-Martinez, J. A. Mendez-Bermudez, and H. Benisty, “Stability mapping of bipartite tight-binding graphs with losses and gain: PT-symmetry and beyond,” arXiv:2212.13642; Chaos 34, 053116 (2024), DOI 10.1063/5.0199771.
