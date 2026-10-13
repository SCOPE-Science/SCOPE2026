# Critical-point law for weak-disorder decay on a lossy quantum star

## Finding
For every integer \(k\geq3\), let a quantum star have one hub \(|0\rangle\), leaves \(|1\rangle,\ldots,|k\rangle\), identical nonzero real hopping \(g\), and hub absorption rate \(\gamma>0\). Give its leaves pairwise distinct real detunings \(\varepsilon v_1,\ldots,\varepsilon v_k\). The effective Hamiltonian is
\[
H_\varepsilon=g\sum_{i=1}^{k}(|0\rangle\langle i|+|i\rangle\langle0|)+\varepsilon\sum_{i=1}^{k}v_i|i\rangle\langle i|-\frac{i\gamma}{2}|0\rangle\langle0|.
\]
Define the polynomial \(P(z)=\prod_{i=1}^{k}(z-v_i)\). Its derivative has exactly \(k-1\) distinct, real roots \(\theta_j\), one in each interval between consecutive sorted detunings. Put
\[
S_j=\sum_{i=1}^{k}(\theta_j-v_i)^{-2},\qquad
|d_j\rangle=S_j^{-1/2}\sum_{i=1}^{k}(\theta_j-v_i)^{-1}|i\rangle.
\]
For each \(\varepsilon\ne0\), **every initial state is eventually absorbed**, even though at \(\varepsilon=0\) the dark subspace has dimension \(k-1\). More precisely, for every density matrix \(\rho\) on the \((k+1)\)-dimensional space and every fixed \(\tau>0\),
\[
\boxed{\lim_{\varepsilon\to0^+}\operatorname{Tr}\!\left[e^{-iH_\varepsilon\tau/\varepsilon^2}\rho\,e^{iH_\varepsilon^*\tau/\varepsilon^2}\right]
=\sum_{j=1}^{k-1}e^{-\gamma\tau/(g^2S_j)}\langle d_j|\rho|d_j\rangle.}
\]
The \(k-1\) initially dark eigenvalues have the expansions
\[
\boxed{\lambda_j(\varepsilon)=\varepsilon\theta_j-\frac{i\gamma\varepsilon^2}{2g^2S_j}+O(\varepsilon^3).}
\]
Thus the entire weak-disorder, rescaled survival curve is a positive mixture of explicitly determined exponentials. Their decay rates are governed by the critical points of the detuning polynomial, not merely by its mean or variance.

## Assumptions and scope
All parameters \(k\), \(g\), \(\gamma\), and \(v_1,\ldots,v_k\) are fixed as \(\varepsilon\to0^+\); \(g\in\mathbb R\setminus\{0\}\), \(\gamma>0\), and the \(v_i\) are pairwise distinct real numbers. The evolution is a single-excitation, Markovian loss model with a vacuum sink represented by \(-i\gamma|0\rangle\langle0|/2\). The survival probability is the total trace of the unnormalized state on the star. The limit is asserted for each fixed \(\tau>0\), not at \(\tau=0\), where the rapidly absorbed bright component produces an initial boundary layer.

## Proof
**1. No dark eigenvector for nonzero disorder.** For an eigenvector \(u\) with eigenvalue \(\lambda\), the identity
\[
\operatorname{Im}\lambda\,\|u\|^2=-\frac{\gamma}{2}|\langle0|u\rangle|^2
\]
implies \(\operatorname{Im}\lambda\le0\). Equality forces the hub coordinate to vanish. The leaf eigenvalue equations then require \((\varepsilon v_i-\lambda)u_i=0\). For \(\varepsilon\ne0\) and distinct \(v_i\), at most one leaf coordinate is nonzero, while the hub equation \(g\sum_i u_i=0\) forces it to vanish. Thus every eigenvalue lies strictly in the lower half-plane. In finite dimensions the evolution decays to zero even at exceptional points, proving complete eventual absorption.

**2. The exact secular equation.** With \(\kappa=\gamma/2\), expansion of the block determinant gives
\[
\det(\lambda I-H_\varepsilon)=(\lambda+i\kappa)\prod_i(\lambda-\varepsilon v_i)
-g^2\sum_i\prod_{\ell\ne i}(\lambda-\varepsilon v_\ell).
\]
At \(\lambda=\varepsilon z\), the polynomial equation for the small spectral cluster is exactly
\[
g^2P'(z)=\varepsilon(i\kappa+\varepsilon z)P(z).
\]
Rolle's theorem makes all roots \(\theta_j\) of \(P'\) simple and strictly interlacing. At each such root, the implicit-function theorem yields an analytic root \(z_j(\varepsilon)\) with
\[
z_j(\varepsilon)=\theta_j+\frac{i\kappa P(\theta_j)}{g^2P''(\theta_j)}\varepsilon+O(\varepsilon^2).
\]
Logarithmically differentiating \(P\) at a critical point gives
\[
-\frac{P''(\theta_j)}{P(\theta_j)}=\sum_i(\theta_j-v_i)^{-2}=S_j,
\]
which proves the claimed eigenvalue expansions. The other two eigenvalues converge to those of the lossy hub/uniform-leaf block
\[
\begin{pmatrix}-i\kappa&g\sqrt{k}\\g\sqrt{k}&0\end{pmatrix};
\]
both have strictly negative imaginary part, including at their possible exceptional-point collision.

**3. Limiting dark vectors.** The normalized leaf vectors \(|d_j\rangle\) are orthonormal because, for \(j\ne\ell\),
\[
\sum_i\frac1{(\theta_j-v_i)(\theta_\ell-v_i)}=
\frac{\sum_i(\theta_j-v_i)^{-1}-\sum_i(\theta_\ell-v_i)^{-1}}{\theta_\ell-\theta_j}=0.
\]
Each sum in the numerator vanishes by \(P'(\theta)/P(\theta)=0\). Also \(\langle0|d_j\rangle=0\) and \(\sum_i\langle i|d_j\rangle=0\), so the vectors span precisely the \((k-1)\)-dimensional dark subspace of \(H_0\). A small-cluster right eigenvector satisfies \((\lambda-\varepsilon v_i)u_i=gu_0\); hence its normalized form tends to \(|d_j\rangle\). The corresponding spectral projector, obtained from the simple isolated eigenvalue, tends to \(|d_j\rangle\langle d_j|\) in operator norm.

**4. Survival at the metastable timescale.** The complementary spectral cluster stays in a fixed compact subset of the lower half-plane. Its propagator tends to zero at \(t=\tau/\varepsilon^2\), even when the two bright eigenvalues coalesce: use a contour-resolvent representation around that cluster to obtain a uniform exponential bound. The remaining propagator is the sum of its \(k-1\) simple spectral terms. For the term indexed by \(j\), the squared modulus of the exponential converges to \(\exp[-\gamma\tau/(g^2S_j)]\) by step 2. Cross terms \(j\ne\ell\) vanish in the trace because their spectral projectors converge to mutually orthogonal rank-one projections; the potentially rapidly oscillating phases have modulus at most one. Taking the trace against any fixed density matrix gives exactly the displayed limit.

## Verification
The standalone `verify.py` reconstructs the complex Hamiltonian directly, independently diagonalizes it for multiple irregular leaf-detuning arrays, evaluates the exact matrix exponential at \(t=\tau/\varepsilon^2\), and compares the survival probabilities with the polynomial critical-point formula. It also verifies orthogonality of the critical-point vectors and the leading imaginary-eigenvalue coefficients. Dependencies are declared in `requirements.txt`. These finite checks are corroboration, not substitutes for steps 1–4 of the proof.

For example, if \(k=3\) and \((v_1,v_2,v_3)=(-1,0,1)\), then \(\theta_{1,2}=\mp1/\sqrt3\), \(S_1=S_2=9\), and every initially dark component decays on the rescaled timescale with rate \(\gamma/(9g^2)\).

## Relationship to prior work
Novo et al. (arXiv:1412.7209, first posted 2014-12-22) establish the relation between quantum transport, detector-visible invariant subspaces, and Krylov reduction; their homogeneous-site analysis does not give the present weak-disorder, timescale-resolved law. Novo, Mohseni, and Omar (arXiv:1312.6989, posted 2013-12-25) study disorder-assisted transport in trees and hypercubes with dephasing, rather than deterministic star detunings and the critical-point decay formula. Yalouz and Pouthier (DOI:10.1103/PhysRevE.101.012310; OA manuscript HAL:hal-02434409, first online 2020) numerically observe complete absorption and long-lived modes for disordered extended stars, but their inspected model, weak-disorder discussion, and decay-rate figures do not provide the explicit polynomial-critical-point rates or the all-initial-state scaling limit above. The classical facts on root interlacing and analytic finite-matrix perturbations are used as mathematical tools, not claimed as discoveries.

## Limitations
The theorem does not assert a disorder-uniform rate as distinct detunings coalesce, nor uniformity when \(k\), \(g\), or \(\gamma\) vary with \(\varepsilon\). The limit is for fixed positive \(\tau\), after the bright-state boundary layer, and it does not describe the full finite-time transient, additional dephasing, multiple sinks, or spatially extended arms. The originality comparison cannot exclude an unlocated general perturbative theorem that specializes to the same formula; independent priority review has not been performed.

## References
1. L. Novo, S. Chakraborty, M. Mohseni, H. Neven, and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (v1 2014-12-22), https://arxiv.org/abs/1412.7209 ; Scientific Reports 5, 13304 (2015), https://doi.org/10.1038/srep13304.
2. L. Novo, M. Mohseni, and Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, arXiv:1312.6989 (v1 2013-12-25), https://arxiv.org/abs/1312.6989 ; Scientific Reports 6, 18142 (2016), https://doi.org/10.1038/srep18142.
3. S. Yalouz and V. Pouthier, *Continuous-time quantum walk on an extended star graph: Disorder-enhanced trapping process*, Physical Review E 101, 012310 (2020), https://doi.org/10.1103/PhysRevE.101.012310 ; OA manuscript https://hal.science/hal-02434409 .
