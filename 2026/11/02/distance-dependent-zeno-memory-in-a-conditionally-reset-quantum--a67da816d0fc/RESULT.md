# Distance-dependent Zeno memory in a conditionally reset quantum chain

## Finding
For the symmetric two-site *conditional* Poisson reset of an infinite tight-binding quantum particle, the stationary left–right site-occupation imbalance is zero, but the transient imbalance from the right reset site has a strictly positive, sharp exponential relaxation law. Writing \(F_R(t)=\Pr(X_t>0)-\Pr(X_t<0)\), its exact decay is
\[
F_R(t)\sim A_R e^{-\Delta_Rt},\qquad \Delta_R=\lambda-q_R,\qquad A_R=\frac1{\lambda^2\int_0^\infty t e^{-q_Rt}c_R(t)\,dt}>0,
\]
where the unique \(q_R\in(0,\lambda)\) solves
\[
\lambda\int_0^\infty e^{-q_Rt}c_R(t)\,dt=1,\qquad
c_R(t)=J_0(\gamma t)^2+2\sum_{j=1}^{R-1}J_j(\gamma t)^2+J_R(\gamma t)^2.
\]
The positive decay rate is strictly **decreasing** with reset-site distance: \(0<\Delta_{R+1}<\Delta_R<\lambda\), and \(\Delta_R\downarrow0\) as \(R\to\infty\) for fixed positive rates. Its strong-reset and weak-reset boundary laws are, respectively,
\[
\Delta_R\sim\binom{2R}{R}\frac{\gamma^{2R}}{4^R\lambda^{2R-1}}\quad(\lambda\to\infty),\qquad
\lim_{\lambda\downarrow0}\lambda\log\frac{\gamma}{q_R}=\frac{\pi\gamma}{2R},
\]
with \(R\) and \(\gamma\) fixed. Thus each additional lattice step between the origin and the reset site raises the strong-reset suppression power by two.

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb Z)\), with orthonormal site kets \(|m\rangle\) and the time-independent Hamiltonian
\[
H=-\frac{\gamma}{2}\sum_{m\in\mathbb Z}\bigl(|m\rangle\langle m+1|+|m+1\rangle\langle m|\bigr),\qquad \gamma>0.
\]
The initial pure state is \(|R\rangle\langle R|\), where \(R\) is a fixed integer \(R\ge1\). At independent Poisson times of rate \(\lambda>0\), the position sign is measured and the particle is re-prepared at \(+R\) if positive or \(-R\) if negative; the zero site sends it to either reset state with probability \(1/2\). Between events the particle evolves unitarily. The probabilities in \(F_R(t)\) are ensemble-averaged occupation probabilities at observation time \(t\), not first-detection probabilities. The conclusions describe this specified observable, not all components of the density matrix. Units use \(\hbar=1\).

## Proof
**1. One-run sign memory.** The unreset propagator gives \(\Pr(X_t=m\mid X_0=R)=J_{m-R}(\gamma t)^2\), a standard identity [1]. Using \(J_{-j}^2=J_j^2\) and \(J_0^2+2\sum_{j\ge1}J_j^2=1\), direct subtraction of the two half-line masses gives exactly the stated finite Bessel-square sum \(c_R(t)\). In particular \(c_R(0)=1\) and \(0<c_R(t)<1\) for \(t>0\): strict upper inequality comes from nonzero negative-side propagation, while strict lower follows because at least one of two consecutive Bessel functions is nonzero. The same identity gives
\[
1-c_R(t)=J_R(\gamma t)^2+2\sum_{j\ge R+1}J_j(\gamma t)^2.
\]
For each fixed \(R\), the standard fixed-order large-argument Bessel expansion, with alternating oscillatory leading terms cancelling under the displayed weights, gives
\[
c_R(t)=\frac{2R}{\pi\gamma t}+O(t^{-2})\qquad(t\to\infty).
\]
Consequently its positive Laplace transform \(C_R(q)=\int_0^\infty e^{-qt}c_R(t)\,dt\) is finite for \(q>0\), continuously strictly decreasing, tends to infinity as \(q\downarrow0\), and satisfies \(C_R(\lambda)<1/\lambda\). Thus \(\lambda C_R(q_R)=1\) has precisely one root in \((0,\lambda)\).

**2. Renewal and sharp coefficient.** Reflection of the dynamics swaps the two reset states, reversing the sign imbalance. Conditioning on the first Poisson reset gives the exact scalar equation
\[
F_R(t)=e^{-\lambda t}c_R(t)+\lambda\int_0^t e^{-\lambda u}c_R(u)F_R(t-u)\,du.
\]
Set \(\Delta_R=\lambda-q_R\) and \(G_R(t)=e^{\Delta_Rt}F_R(t)\). The tilted renewal equation has a strictly positive continuous **probability-density** kernel \(k_R(u)=\lambda e^{-q_Ru}c_R(u)\), with finite mean
\[
\mu_R=\int_0^\infty uk_R(u)\,du=\lambda\int_0^\infty u e^{-q_Ru}c_R(u)\,du.
\]
Its forcing \(e^{-q_Rt}c_R(t)\) is directly Riemann integrable (continuous and bounded by \(e^{-q_Rt}\)), with integral \(C_R(q_R)=1/\lambda\). The nonarithmetic key renewal theorem yields \(G_R(t)\to1/(\lambda\mu_R)=A_R\). Positivity of the original renewal series implies \(F_R(t)>0\) for every finite \(t\), and the proved limit implies stationarity of the sign imbalance is zero.

**3. Strict distance ordering.** From the exact Bessel sums,
\[
c_{R+1}(t)-c_R(t)=J_R(\gamma t)^2+J_{R+1}(\gamma t)^2>0 \qquad(t>0).
\]
Thus \(C_{R+1}(q)>C_R(q)\), forcing \(q_{R+1}>q_R\) and \(\Delta_{R+1}<\Delta_R\). At each fixed \(t\), \(c_R(t)\uparrow1\) as \(R\to\infty\); monotone convergence gives \(C_R(q)\uparrow1/q\) and hence \(q_R\uparrow\lambda\), establishing the limiting claim.

**4. Strong-reset power.** The power series \(J_R(z)=\frac{(z/2)^R}{R!}+O(z^{R+2})\) gives
\[
1-c_R(t)=\frac{(\gamma t)^{2R}}{4^R(R!)^2}+O(t^{2R+2})\qquad(t\downarrow0).
\]
Let \(p_R(q)=q\int_0^\infty e^{-qt}(1-c_R(t))\,dt\). The root equation rearranges to \(q_R=\lambda[1-p_R(q_R)]\). Because \(C_R(q)\sim1/q\) as \(q\to\infty\), it follows that \(q_R/\lambda\to1\) as \(\lambda\to\infty\). Watson's Laplace lemma gives \(p_R(q)\sim\binom{2R}{R}\gamma^{2R}/(4^R q^{2R})\). Since \(\Delta_R=\lambda p_R(q_R)\), the stated strong-reset asymptotic follows.

**5. Weak-reset exponential scale.** The large-time expansion in Step 1 and elementary Laplace estimates give
\[
C_R(q)=\frac{2R}{\pi\gamma}\log\!\left(\frac\gamma q\right)+O(1)\qquad(q\downarrow0).
\]
As \(\lambda\downarrow0\), its unique root tends to zero, so substituting \(C_R(q_R)=1/\lambda\), multiplying by \(\lambda\), and taking the limit yields the second displayed boundary law. This is an exponentially small complementary root \(q_R\), not an assertion that \(\Delta_R\) itself is exponentially small at weak resetting.

## Verification
The standalone `verify_quantum_relaxation.py` uses only Python, NumPy and SciPy. Execute `OPENBLAS_NUM_THREADS=1 python verify_quantum_relaxation.py`. It reproduces 85 finite numerical consistency checks: direct quantum-walk Bessel occupation sums, positive root and strict gap ordering, strong-reset leading coefficients, numerical Volterra renewal solutions approaching the analytic prefactor, and an **independent** finite-interval Markovian measurement-and-repreparation master-equation computation. For \(\gamma=\lambda=1\), root/decay/prefactor triples for \(R=1,2,3\) are approximately \((0.653540891230,0.346459108770,1.145952602844)\), \((0.915521882191,0.084478117809,1.112017869091)\), and \((0.974834046086,0.025165953914,1.053985494917)\). The infinite-lattice theorem follows from the analytical proof, not from finite numerical tests; floating quadrature may issue tolerance warnings.

## Relationship to prior work
Acharya and Gupta [1] introduced the exact conditional tight-binding reset model and derived general time-dependent site-occupation and Laplace-transform formulas, including its stationary distribution; these are **prior results**, not new contributions. Perfetto and collaborators [2] give a more general conditional-quantum-reset renewal framework, particularly for an Ising chain, so the existence of a renewal equation is likewise prior. Rose and collaborators [3] obtain a uniform spectral shift for *unconditional* state-independent resetting, which does not impose this two-site sign-conditioned memory equation. Carollo and collaborators [4] study generalized reset-trajectory ordering probabilities rather than the present tight-binding relaxation rate. The assessed addition is the **sharp positive prefactor, unique rate, strict reset-distance ordering, and both rate-regime asymptotic constants** for this natural sign observable. The original general Laplace formula implicitly contains information about the sign sector; originality is the explicit, proved characterization, not the mere existence of its transform.

## Limitations
This is a statement about an ensemble-averaged left–right sign observable in an infinite, homogeneous, one-particle chain with nearest-neighbour hopping, symmetric reset sites, a fair zero tie, and exponentially distributed event times. It is not a universal spectral-gap theorem for the entire density-matrix semigroup or an optimal-reset theorem. The finite-lattice checker has a cutoff and cannot certify the infinite-lattice or infinite-time statements; those are established analytically. Broader general renewal/spectral reductions may reproduce some formulas, so independent publication-priority assessment remains necessary.

## References
[1] A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, arXiv:2308.14040 (first posted 2023-08-27), https://arxiv.org/abs/2308.14040 ; full-text https://arxiv.org/html/2308.14040v2 .
[2] G. Perfetto, F. Carollo, M. Magoni and I. Lesanovsky, *Designing non-equilibrium states of quantum matter through stochastic resetting*, arXiv:2106.13761, https://arxiv.org/abs/2106.13761 .
[3] D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298, https://arxiv.org/abs/1806.01298 .
[4] F. Carollo, I. Lesanovsky and J. P. Garrahan, *Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes*, arXiv:2310.06981, https://arxiv.org/html/2310.06981v2 .
