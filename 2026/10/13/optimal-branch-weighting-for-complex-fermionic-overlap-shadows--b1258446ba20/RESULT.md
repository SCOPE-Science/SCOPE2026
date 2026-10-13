# Optimal branch weighting for complex fermionic overlap shadows
## Finding
Fix integers \(N\ge\eta\ge1\). The complex-overlap orbital-rotation shadow protocol can be extended from the equal coherent augmentation to
\[
|\Psi_\lambda\rangle=\sqrt{\lambda}|\Psi_T\rangle+\sqrt{1-\lambda}|\mathbf a\rangle,
\qquad 0<\lambda<1,
\]
where \(|\Psi_T\rangle\) is a normalized \(\eta\)-particle trial state on the physical modes and \(|\mathbf a\rangle\) is the source's normalized ancillary Slater determinant on the appended modes. A known relative phase between the two branches can be absorbed into the estimator, so it is taken to be zero here.

For a normalized target Slater determinant \(|\phi\rangle\), let \(p_j(\phi)\) denote the probability that \(|\Psi_T\rangle\) has exactly \(j\) particles outside the occupied one-particle subspace of \(|\phi\rangle\), and define
\[
S_\phi=\sum_{j=0}^{\eta}\frac{p_j(\phi)}{j+1},
\qquad
p_0(\phi)=|\langle\phi|\Psi_T\rangle|^2,
\qquad
b_{N,\eta}=\frac{(\eta+1)(N+2)}{N+\eta+2}.
\]
If \(d_1=\binom{N+\eta+1}{\eta}\) is the inverse-channel coefficient used by the source and \(v_{\mathbf q},v_{\mathbf a}\) are the corresponding determinant amplitudes of a shadow record, then
\[
\widehat o_{\phi,\lambda}
=
\frac{d_1}{\sqrt{\lambda(1-\lambda)}}v_{\mathbf q}v_{\mathbf a}^*
\]
is unbiased for \(o_\phi=\langle\phi|\Psi_T\rangle\), and
\[
\operatorname{Var}_{\mathbb C}(\widehat o_{\phi,\lambda})
=
b_{N,\eta}\left(\frac1\lambda+\frac{S_\phi}{1-\lambda}\right)-p_0(\phi).
\]

Now let \(\mu\) be any fixed probability distribution over normalized target Slater determinants whose overlaps are to be read from the same shadow data. Put \(\bar S=\mathbb E_\mu S_\phi\) and \(\bar p_0=\mathbb E_\mu p_0(\phi)\). A single global branch weight minimizes the average complex variance exactly at
\[
\lambda_*=\frac1{1+\sqrt{\bar S}},
\]
with optimum
\[
\mathbb E_\mu\operatorname{Var}_{\mathbb C}(\widehat o_{\phi,\lambda_*})
=
b_{N,\eta}(1+\sqrt{\bar S})^2-\bar p_0.
\]
Compared with the equal augmentation \(\lambda=1/2\), the exact gain is
\[
b_{N,\eta}(1-\sqrt{\bar S})^2.
\]
It is strictly positive whenever \(\bar S<1\).

The equal branch weight nevertheless has a sharp robustness property: over the unrestricted class of normalized trial states and normalized target Slater determinants, \(\lambda=1/2\) is the unique minimax choice, with exact worst-case variance \(4b_{N,\eta}-1\).

## Assumptions and scope
The statement uses the same ideal setting as the source variance theorem: \(1\le\eta\le N\), exact preparation of a normalized fixed-particle-number trial state, a normalized Slater target, Haar-random orbital rotations on the \(N+\eta\) physical-plus-ancillary modes, occupation-basis measurement, and the ideal inverse measurement channel. The only protocol change is the coherent branch probability \(\lambda\), which is fixed before the shared shadow data are collected.

The target distribution \(\mu\) may be finite or continuous and is used only to define an average variance objective. The same value of \(\lambda\) is used for all targets in \(\mu\), so the data-reuse advantage of the shadow protocol is retained. The result does not assume that \(\bar S\) is known for free; estimating or bounding \(\bar S\) is a separate calibration problem.

## Proof
The source proves the Haar identity
\[
\mathbb E_V[x_{\mathbf q}x_{\mathbf a}]=\frac1{d_0d_1}
\]
and, for the equal augmented state, obtains
\[
\mathbb E[v_{\mathbf q}v_{\mathbf a}^*]=\frac{o_\phi}{2d_1}.
\]
With branch amplitudes \(\sqrt\lambda\) and \(\sqrt{1-\lambda}\), the same phase-averaging calculation multiplies the physical-reference coherence by \(2\sqrt{\lambda(1-\lambda)}\) relative to the equal case. Hence
\[
\mathbb E[v_{\mathbf q}v_{\mathbf a}^*]
=
\frac{\sqrt{\lambda(1-\lambda)}}{d_1}o_\phi,
\]
which proves unbiasedness after multiplying by \(d_1/\sqrt{\lambda(1-\lambda)}\).

For the second moment, the source's diagonal operator for the equal-weight estimator has eigenvalue \(4b_{N,\eta}/(j+1)\) on a physical occupation configuration with \(j\) particles outside the target occupied subspace, and eigenvalue \(4b_{N,\eta}\) on the ancillary reference configuration. Replacing the estimator coefficient \(2d_1\) by \(d_1/\sqrt{\lambda(1-\lambda)}\) rescales this second-moment operator by \(1/[4\lambda(1-\lambda)]\). Since the operator is diagonal, the coherence between the physical and ancillary branches makes no contribution. Therefore
\[
\begin{aligned}
\mathbb E|\widehat o_{\phi,\lambda}|^2
&=
\frac{1}{4\lambda(1-\lambda)}
\left[
\lambda\sum_{j=0}^{\eta}p_j(\phi)\frac{4b_{N,\eta}}{j+1}
+(1-\lambda)4b_{N,\eta}
\right]\\
&=
b_{N,\eta}\left(\frac1\lambda+\frac{S_\phi}{1-\lambda}\right).
\end{aligned}
\]
Subtracting \(|o_\phi|^2=p_0(\phi)\) gives the variance formula.

Averaging over \(\mu\) gives
\[
\bar V(\lambda)
=b_{N,\eta}\left(\frac1\lambda+\frac{\bar S}{1-\lambda}\right)-\bar p_0.
\]
Because \(S_\phi>0\), this function diverges at both endpoints and is strictly convex on \((0,1)\). Its derivative vanishes exactly when
\[
\frac{1-\lambda}{\lambda}=\sqrt{\bar S},
\]
which yields \(\lambda_*=1/(1+\sqrt{\bar S})\). Substitution gives the stated optimum. At \(\lambda=1/2\), the average variance is \(2b_{N,\eta}(1+\bar S)-\bar p_0\); subtracting the optimum gives \(b_{N,\eta}(1-\sqrt{\bar S})^2\).

For minimaxity, consider the admissible special case in which the trial state is itself the target Slater determinant. Then \(S_\phi=p_0(\phi)=1\), so every branch weight obeys
\[
\operatorname{Var}_{\mathbb C}(\widehat o_{\phi,\lambda})
=
\frac{b_{N,\eta}}{\lambda(1-\lambda)}-1
\ge
4b_{N,\eta}-1,
\]
with equality only at \(\lambda=1/2\). The source theorem proves that the equal-weight protocol has variance at most \(4b_{N,\eta}-1\) for every allowed normalized trial-target pair. Thus \(\lambda=1/2\) attains the universal lower bound on worst-case variance and is the unique minimax choice.

## Verification
The algebra was replayed with exact rational arithmetic for \(b_{N,\eta}\) and numerical convexity checks over representative \((N,\eta)\) pairs and sector distributions. The standalone verifier checks the weighted second-moment identity, the stationary point, the exact gain relative to \(\lambda=1/2\), and the minimax lower-bound witness. These finite checks support but do not replace the analytic proof above.

## Relationship to prior work
Low introduced the coherent-reference augmentation for extracting complex overlaps from particle-number-preserving fermionic shadows, using the equal superposition \((|\psi\rangle+|\mathbf a\rangle)/\sqrt2\). Zhao, Goings, Epifanovsky and Roetteler specialize that construction to QC-AFQMC and derive the exact equal-weight complex variance, including the diagonal second-moment spectrum and the sharp universal upper bound \(4b_{N,\eta}-1\). Their Appendix A explicitly attributes its lower bound to the fixed reference weight.

The present result changes the measured state and estimator by introducing a free coherent branch probability \(\lambda\). The equal-weight variance theorem does not contain the \(\lambda\ne1/2\) measurement distribution. The new calculation gives the full one-parameter variance law, solves the average-variance design problem for a shared target ensemble, and proves that the source's equal superposition is nevertheless uniquely optimal in the unrestricted worst case.

West, Cerezo and Larocca study particle-preserving shadows for squared Slater overlaps and establish mode-independent sample complexity for that different observable. The 2026 QC-AFQMC source explicitly distinguishes squared-overlap estimation from the phase-sensitive complex overlap treated by the augmented-reference protocol.

## Limitations
The improvement is an average-variance statement for a specified target distribution and requires a usable estimate or bound for \(\bar S\). It does not reduce the universal worst-case variance: the equal source weight is already uniquely minimax. It does not analyze imperfect preparation, finite-design orbital rotations, hardware noise, relative-error behavior near overlap zeros, nonlinear AFQMC ratios, or the cost of calibrating \(\bar S\). It also does not claim that the optimized branch weight is optimal among all possible measurement ensembles or all possible overlap estimators.

## References
1. L. Zhao, J. Goings, E. Epifanovsky, and M. Roetteler, "Orbital-Rotation Shadow Tomography Reduces the Classical Cost of Quantum-Classical Auxiliary-Field Quantum Monte Carlo," arXiv:2610.03103v1, 2026. In particular Sec. II B, Theorem 3, and Appendix A, Eqs. (A62)--(A70).
2. G. H. Low, "Classical shadows of fermions with particle number symmetry," arXiv:2208.08964v2, 2024 version of the 2022 preprint. In particular the equal coherent augmentation in Eqs. (132)--(133).
3. M. West, M. Cerezo, and M. Larocca, "Particle-preserving fermionic shadows with mode-independent sample complexity," arXiv:2606.27254v1, 2026.
