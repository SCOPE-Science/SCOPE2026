# A spectral-edge transition under single-atom erasure of Cauchy Gabor frames

## Finding
Fix an integer \(q\ge2\) and \(a>0\). Form the Gabor frame in \(L^2(\mathbb R)\) with window \(g_a(t)=(t-ia)^{-1}\), translation step \(1/q\), and modulation step \(1\). Deleting any one atom preserves the frame, but may change its **sharp** lower bound. This outcome is determined exactly by a one-dimensional integrable spectral-edge test, described below. Every such deletion leaves the sharp upper bound unchanged.

Write \(r=e^{-2\pi a}\), \(\tau=-2\log r=4\pi a\), and
\[
 d(\theta)=1+r^2-2r\cos\theta,\quad
 D_q(\theta)=1+r^{2q}-2r^q\cos(q\theta),\quad
 K_q=\frac{q(1-r^{2q})}{1-r^2}.
\]
The original sharp lower and upper frame bounds are
\[
 A_{q,a}=\frac{4\pi^2 r^2K_q}{(1+r^q)^2},\qquad
 B_{q,a}=\frac{4\pi^2 K_q}{(1-r^q)^2}.
\]
Define
\[
 W_q(\theta)=\frac{D_q(\theta)}{K_qd(\theta)},\qquad
 h_q(\theta)=\frac{D_q(\theta)}{(1+r^q)^2},
\]
and the finite improper integral
\[
 E_q(a)=\frac1q+\frac1{\tau}\int_0^{2\pi}
 W_q(\theta)\log\frac{1-r^2h_q(\theta)}{1-h_q(\theta)}
 \,\frac{d\theta}{2\pi}.
\]
Its logarithmic singularities at \(\theta=(2j+1)\pi/q\), \(0\le j<q\), are integrable. If \(E_q(a)\le1\), the post-erasure sharp lower bound remains \(A_{q,a}\). If \(E_q(a)>1\), it is a unique simple eigenvalue \(\lambda_{q,a}\in(0,A_{q,a})\), determined without truncation by
\[
 \int_0^{2\pi}\!\int_0^1
 \frac{4\pi^2r^{2(1-\omega)}/d(\theta)}
 {4\pi^2r^{2(1-\omega)}K_q/D_q(\theta)-\lambda_{q,a}}
 \,d\omega\,\frac{d\theta}{2\pi}=1.
\]
In both cases the post-erasure sharp upper bound is exactly \(B_{q,a}\).

For each **fixed** integer \(q\ge2\), the edge test has the sharp limiting laws
\[
 E_q(a)\sim\frac1{q\sqrt{\pi a}}\quad(a\downarrow0),\qquad
 \lim_{a\to\infty}E_q(a)=\frac12+\frac1q.
\]
Consequently for every fixed \(q\ge3\), sufficiently shallow Cauchy poles cause a strict deterioration of the optimal lower frame bound upon erasure, whereas sufficiently deep poles cause **no change to either optimal frame bound**. No uniqueness of a depth separating these regimes is asserted.

## Assumptions and scope
Use the standard \(L^2(\mathbb R)\) inner product, Lebesgue measure, and unitary Zak transformation \((Zf)(x,\omega)=\sum_{k\in\mathbb Z}f(x+k)e^{-2\pi i k\omega}\) on \([0,1)^2\), with \(\theta=2\pi x\). For the translated/modulated atoms \(g_{m,k}(t)=e^{2\pi imt}g_a(t-k/q)\), the full positive frame operator is \(S_{q,a}=\sum_{m,k\in\mathbb Z}|g_{m,k}\rangle\langle g_{m,k}|\). Removing exactly one atom produces \(S_{q,a}^{(-1)}\). All thresholds are for the stated **unnormalized** Cauchy window; rescaling the window multiplies all spectral bounds but does not change the criterion. The limits keep \(q\) fixed. The classification is in harmonic-frame analysis, MSC2020 42C15.

## Proof
**Step 1: exact diagonalization.** Poisson summation or the residue computation for the Cauchy kernel yields, almost everywhere,
\[
 |Zg_a(x,\omega)|^2=\frac{4\pi^2r^{2(1-\omega)}}{d(2\pi x)}.
\]
The lattice with translations \(k/q\) is the union of \(q\) translates of the critically sampled integer lattice. Under the Zak transform its frame operator is multiplication by the sum of the \(q\) shifted squared Zak magnitudes. The elementary roots-of-unity identity
\[
 \sum_{j=0}^{q-1}\frac1{|1-re^{i(\theta-2\pi j/q)}|^2}
 =\frac{q(1-r^{2q})}{(1-r^2)|1-r^qe^{iq\theta}|^2}
\]
therefore gives the exact multiplier
\[
 s_{q,a}(\theta,\omega)=\frac{4\pi^2r^{2(1-\omega)}K_q}{D_q(\theta)}.
\]
Its essential minimum and maximum are the displayed \(A_{q,a}\) and \(B_{q,a}\). These baseline spectral formulas belong to the existing theory of integer-density Cauchy and one-sided-exponential Gabor frames, and are used here as an input/rederivation rather than claimed as new.

**Step 2: the deletion perturbation.** By Gabor covariance any one atom may be moved to \(g_a\) by a unitary operator commuting with the full frame operator. Thus it suffices to study \(S_{q,a}-|g_a\rangle\langle g_a|\). For \(0\le\lambda<A_{q,a}\), the rank-one positivity criterion gives
\[
 S_{q,a}-|g_a\rangle\langle g_a|-\lambda I\ge0
 \quad\Longleftrightarrow\quad
 \Phi_{q,a}(\lambda):=\langle g_a,(S_{q,a}-\lambda I)^{-1}g_a\rangle\le1.
\]
The Zak integral for \(\Phi\) is the expression in the Finding with \(\lambda_{q,a}\) replaced by \(\lambda\). It is continuous and strictly increasing on \([0,A_{q,a})\). At \(\lambda=0\), the cancellation of factors yields
\[
 \Phi_{q,a}(0)=\int_0^{2\pi}W_q(\theta)\,\frac{d\theta}{2\pi}=\frac1q.
\]
Indeed \(D_q(\theta)/d(\theta)=|\sum_{j=0}^{q-1}r^je^{ij\theta}|^2\), whose circle integral is \(\sum_{j=0}^{q-1}r^{2j}=K_q/q\). Hence \(\Phi(0)<1\), proving deletion leaves a positive lower frame bound. The rank-one difference is compact, so essential spectral edges \(A_{q,a}\) and \(B_{q,a}\) are unaffected. Since the perturbation is negative, the sharp upper bound remains \(B_{q,a}\).

**Step 3: edge threshold and uniqueness.** In the integral for \(\Phi(\lambda)\), set \(t=r^{2(1-\omega)}\), so \(d\omega=dt/(\tau t)\). At \(\lambda=A_{q,a}\), the resulting logarithm is exactly the displayed formula for \(E_q(a)\), including the term \(1/q\). The only singularities occur at the \(q\) angles where \(h_q=1\); there \(1-h_q(\theta)\) is a positive constant times squared angular distance, making the logarithms integrable. Monotone convergence shows that \(E_q(a)=\lim_{\lambda\uparrow A}\Phi_{q,a}(\lambda)\). If this limit is at most one, \(\Phi(\lambda)<1\) for all \(\lambda<A\), so the essential lower edge stays sharp. Otherwise there is a unique root of \(\Phi(\lambda)=1\), necessarily the simple eigenvalue below the essential spectrum; the eigenvector is proportional to \((S_{q,a}-\lambda I)^{-1}g_a\).

**Step 4: shallow-pole asymptotic.** Put \(\theta_j=(2j+1)\pi/q\). As \(\tau\downarrow0\), uniformly in small neighborhoods of these points,
\[
 1-h_q(\theta_j+u)=\frac{q^2u^2}{4}+o(u^2)+O(\tau u^2),\quad
 1-r^2=\tau+O(\tau^2),\quad
 W_q(\theta_j)\longrightarrow\frac1{q^2\sin^2(\theta_j/2)}.
\]
In the scale \(u=\sqrt\tau\,v\), each logarithmic singularity converges to \(\log(1+4/(q^2v^2))\). The elementary integral \(\int_{\mathbb R}\log(1+c^2/v^2)\,dv=2\pi c\) implies a contribution \(2W_q(\theta_j)/(q\sqrt\tau)\) to the edge test. Outside fixed neighborhoods the contribution is \(O(1)\); on the neighborhoods the scaled integrands are dominated after splitting the regions \(|u|\lesssim\sqrt\tau\) and \(|u|\gtrsim\sqrt\tau\), using \(\log(1+C\tau/u^2)\le C\tau/u^2\) away from the center. The finite identity
\[
 \sum_{j=0}^{q-1}\csc^2\frac{(2j+1)\pi}{2q}=q^2
\]
now gives \(\sum_jW_q(\theta_j)\to1\), so \(E_q(a)\sim2/(q\sqrt\tau)=1/(q\sqrt{\pi a})\).

**Step 5: deep-pole asymptotic.** As \(r\downarrow0\), \(W_q\to1/q\) uniformly and
\[
 1-h_q(\theta)=\frac{2r^q(1+\cos(q\theta))}{(1+r^q)^2}.
\]
The logarithmic singularity of \(1+\cos(q\theta)\) is integrable. Since \(1-r^2h_q\to1\), integration of the edge logarithm equals \(-q\log r+O(1)\) after averaging; division by \(\tau=-2\log r\) gives a limit of \(1/2\) for the integral term. Therefore \(E_q(a)\to1/q+1/2\). For fixed \(q\ge3\) this is strictly below one, while the shallow-pole limit diverges; continuity of \(E_q(a)\) on \((0,\infty)\) establishes the two nonempty erasure regimes. The borderline case \(q=2\) is intentionally not assigned a deep-pole stability regime by this argument.

## Verification
The standalone Python 3 standard-library script `verify_erasure.py` numerically checks the exact multiplier against finite shifted-Zak sums, the leverage identity \(\Phi(0)=1/q\), representative strict edge inequalities at \(q=3,4\), and the small-/large-pole edge limits. The script is supplementary: quadrature does not prove strict inequalities for all parameters or any infinite-dimensional spectral assertion. All analytical claims follow from the explicit Zak identity, rank-one positivity criterion and asymptotic estimates above.

## Relationship to prior work
Belov, Kulikov and Lyubarskii determine Gabor frame operators for Cauchy kernels and provide the underlying transform framework; Faulhuber and Shafkulovska study sharp Gabor bounds for Fourier-related one-sided exponential windows at integer oversampling. Both give input/background for the exact unperturbed spectral bounds. The classical Gabor-frame excess literature establishes qualitative atom removability. The claim here concerns a **different invariant**: whether removing one prescribed atom strictly changes the **optimal** lower bound, with an explicit edge criterion and two limiting regimes. The general rank-one resolvent criterion is classical; the Cauchy-specific evaluation and limiting sharp comparison are the distinct content. Unindexed overlapping results remain a priority risk.

## Limitations
The complete criterion holds for every integer \(q\ge2\) and real \(a>0\), but the existence of both strict and unchanged-bound regimes is established only for fixed \(q\ge3\). Uniqueness or monotonicity of transitions as \(a\) varies is unproved. The result treats one deleted atom, not an arbitrary finite erasure pattern, and no claims are made for noninteger redundancy, non-Cauchy windows, or a uniform joint \(q,a\) limit. Independent audit has not been performed.

## References
1. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915, first public 17 December 2022. https://arxiv.org/abs/2212.08915
2. M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first public 6 April 2022. https://arxiv.org/abs/2204.02917
3. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, *Inventiones Mathematicae* 231 (2023), 431–466, online 22 August 2022. https://doi.org/10.1007/s00222-022-01151-8
4. R. Balan, P. G. Casazza, C. Heil, Z. Landau, *Excesses of Gabor frames*, *Applied and Computational Harmonic Analysis* 14 (2003), 87–106. https://doi.org/10.1016/S1063-5203(03)00006-X
