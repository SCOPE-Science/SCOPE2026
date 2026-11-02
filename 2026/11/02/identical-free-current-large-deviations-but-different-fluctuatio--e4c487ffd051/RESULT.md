# Identical free-current large deviations but different fluctuations for Erlang and Markov run-and-tumble motion

## Finding

A stationary run-and-tumble particle whose orientation changes after **two independent exponential phases** can have exactly the same entire long-time free-displacement large-deviation rate function as an ordinary memoryless telegraph particle, even while having strictly larger displacement variance at every positive time and strictly larger stationary position variance in every harmonic trap. This is a concrete non-identifiability boundary for using free-current large deviations to infer persistent-particle memory.

**Theorem.** Fix \(v,\lambda>0\), drift \(u\in\mathbb R\), translational diffusivity \(D\ge0\), and, when considering a trap, spring relaxation \(\kappa>0\). Define an irreducible four-phase continuous-time Markov chain \(Y_t\in\{1,2,3,4\}\) that jumps successively \(1\to2\to3\to4\to1\) at rate \(\lambda\), and set \(s(1)=s(2)=1\) and \(s(3)=s(4)=-1\). Initialize the hidden phase chain in its stationary uniform law. Let \(S_t\in\{\pm1\}\) independently denote the stationary symmetric telegraph sign that flips at rate \(\lambda\). With independent standard Brownian motions, put

\[
X^E_t=ut+v\int_0^t s(Y_a)\,da+\sqrt{2D}\,B_t,
\qquad
X^M_t=ut+v\int_0^t S_a\,da+\sqrt{2D}\,\widetilde B_t.
\]

Then for every real \(k\) their scaled cumulant-generating functions agree:

\[
\Lambda_E(k)=\Lambda_M(k)
=uk+Dk^2-\lambda+\sqrt{\lambda^2+v^2k^2}.
\tag{1}
\]

Both \(X^E_t/t\) and \(X^M_t/t\) satisfy the same full speed-\(t\) large-deviation principle with good rate function \(I_D\). For \(D=0\),

\[
I_0(j)=\begin{cases}
\lambda\left(1-\sqrt{1-((j-u)/v)^2}\right),& |j-u|\le v,\\
+\infty,&|j-u|>v.
\end{cases}
\tag{2}
\]

For \(D>0\), the exact rate is

\[
I_D(j)=\min_{-1\le z\le1}\left\{
\lambda(1-\sqrt{1-z^2})+\frac{(j-u-vz)^2}{4D}
\right\}.
\tag{3}
\]

Despite (1), for every \(t>0\) the finite-time variance has the **strict** gap

\[
\operatorname{Var}(X^E_t)-\operatorname{Var}(X^M_t)
=\frac{v^2}{\lambda^2}e^{-\lambda t}
[\sinh(\lambda t)-\sin(\lambda t)]>0.
\tag{4}
\]

Now define the stationary harmonically confined displacements by the Langevin dynamics

\[
dZ^E_t=(-\kappa Z^E_t+v s(Y_t))\,dt+\sqrt{2D}\,dB_t,
\qquad
dZ^M_t=(-\kappa Z^M_t+vS_t)\,dt+\sqrt{2D}\,d\widetilde B_t.
\]

For all \(\kappa>0\), their unique stationary variances are

\[
V_E=\frac D\kappa+
\frac{v^2(\kappa+\lambda)}{\kappa[(\kappa+\lambda)^2+\lambda^2]},
\qquad
V_M=\frac D\kappa+\frac{v^2}{\kappa(\kappa+2\lambda)},
\tag{5}
\]

and obey the **strict universal harmonic-trap witness**

\[
V_E-V_M=
\frac{v^2\lambda}{(\kappa+2\lambda)[(\kappa+\lambda)^2+\lambda^2]}>0.
\tag{6}
\]

The comparison is deliberately calibrated to identical complete free-displacement large-deviation functions, **not** to identical mean run times. Complete orientation-sojourn times have means \(2/\lambda\) and \(1/\lambda\), respectively.

## Assumptions and scope

The hidden chain is stationary at time zero, so its initial *residual* run time is not assumed to be a fresh Erlang run. After each direction change, however, the next full run consists of exactly two rate-\(\lambda\) exponential phases and has the Erlang-2 distribution. The observed Erlang orientation is a stationary semi-Markov alternating-renewal process. The comparator is a two-state, exponentially switching process with flip rate \(\lambda\). The Brownian processes are independent of the internal states, and of each other; only distributional comparisons, not a pathwise coupling, are asserted. At \(D=0\), the displacement is bounded by the speed cone \(|X_t-ut|\le vt\). At \(D>0\) the displacement is unbounded but has Gaussian tails. The harmonic models are driven by stationary, two-sided versions of their orientations; \(\kappa>0\) ensures a unique stationary solution. The drift \(u\) pertains only to the free current, not the centered harmonic trap.

## Proof

**1. Tilted generator and exact spectral coincidence.** Adopt the row generator \(Q\), with \(Q_{jj}=-\lambda\) and \(Q_{j,j+1}=\lambda\), cyclically, and the velocity diagonal \(V=v\operatorname{diag}(1,1,-1,-1)\). Direct determinant expansion gives the factorization, for all complex \(z\) and real \(k\),

\[
\det(zI-Q-kV)
=\big[z(z+2\lambda)-v^2k^2\big]
\big[(z+\lambda)^2+\lambda^2-v^2k^2\big].
\tag{7}
\]

The first factor has roots \(-\lambda\pm\sqrt{\lambda^2+v^2k^2}\). The second has roots \(-\lambda\pm\sqrt{v^2k^2-\lambda^2}\) when \(|vk|\ge\lambda\), or a conjugate pair with real part \(-\lambda\) otherwise. Thus, for every real \(k\), the strict dominant real eigenvalue is

\[
\psi(k)=-\lambda+\sqrt{\lambda^2+v^2k^2}.
\]

The Feynman–Kac formula and Perron–Frobenius theory for the irreducible finite-state tilted semigroup give the scaled cumulant-generating function of the phase-integrated velocity as \(\psi(k)\), independently of positive initial phase probabilities. The stationary two-state telegraph tilted generator has eigenvalues \(-\lambda\pm\sqrt{\lambda^2+v^2k^2}\), hence the same dominant root. Independent drift and Brownian motion add \(uk+Dk^2\). This proves (1).

**2. The full large-deviation principle, including ballistic endpoints.** The common function in (1) is finite and differentiable on the whole real line. The finite-state Feynman–Kac limit and the Gärtner–Ellis theorem give the full speed-\(t\) LDP when \(D>0\), because \(\Lambda'(k)\) is unbounded at both signs of infinity. For \(D=0\), the same theorem gives the lower bound in the open interior of the speed cone and the upper bound everywhere. Explicit Legendre transformation yields (2) in the interior. At either endpoint \(j=u\pm v\), each model has a positive stationary probability of maintaining the same orientation for time \(t\), with probability \(e^{-\lambda t}\) times a positive polynomial factor of degree at most one: in the Erlang model this probability is \(e^{-\lambda t}(2+\lambda t)/4\) for either sign, while in the Markov comparator it is \(e^{-\lambda t}/2\). These events yield endpoint rate \(\lambda\), matching the Legendre transform there. This fills the possible non-steep endpoint gap and establishes the full LDP including both edges. Independence of Brownian motion and the LDP contraction principle then alternatively give (3) for \(D>0\).

**3. Exact autocorrelation and transient variance.** With \(s=(1,1,-1,-1)^\top\) and stationary phase distribution \(\pi=(1/4,1/4,1/4,1/4)\), the phase correlation is \(C_E(t)=\frac14s^\top e^{Qt}s\). Direct matrix multiplication shows \(Q^2s+2\lambda Qs+2\lambda^2s=0\). Consequently the scalar correlation solves \(C_E''+2\lambda C_E'+2\lambda^2C_E=0\) with \(C_E(0)=1\), \(C_E'(0)=-\lambda\); therefore

\[
C_E(t)=e^{-\lambda t}\cos(\lambda t),
\qquad C_M(t)=e^{-2\lambda t}.
\tag{8}
\]

For stationary zero-mean velocity, the active displacement variance is \(2v^2\int_0^t(t-a)C(a)\,da\). Explicit integration, including the common Brownian contribution, gives

\[
\operatorname{Var}(X^E_t)
=2Dt+\frac{v^2t}{\lambda}-\frac{v^2}{\lambda^2}e^{-\lambda t}\sin(\lambda t),
\]
\[
\operatorname{Var}(X^M_t)
=2Dt+\frac{v^2t}{\lambda}-\frac{v^2}{2\lambda^2}(1-e^{-2\lambda t}).
\tag{9}
\]

Subtracting yields (4), since \(\sinh x-\sin x>0\) for every \(x>0\): its derivative \(\cosh x-\cos x\) is strictly positive there. Both models have effective diffusivity \(D+v^2/(2\lambda)\). Their transient variance gap tends to \(v^2/(2\lambda^2)\), not to zero.

**4. Harmonic filter and strictly positive steady-state witness.** The stationary centered solutions are the exponentially weighted filters of their two-sided velocity processes plus independent Ornstein–Uhlenbeck Brownian terms. For either stationary correlation \(C\), Fubini and symmetry give the convergent identity

\[
\operatorname{Var}(Z)=\frac{D}{\kappa}
+\frac{v^2}{\kappa}\int_0^\infty e^{-\kappa a}C(a)\,da.
\tag{10}
\]

Inserting (8) yields (5); subtraction gives (6). All denominators are strictly positive for the stated parameters. The stationary solutions exist uniquely by exponential stability of the linear drift and stationarity of the bounded velocity input. This completes the proof.

## Verification

The accompanying `verify.py` builds the actual four-phase generator, independently diagonalizes numerically tilted matrices, checks their characteristic determinants against (7), computes the stationary correlation by matrix exponentiation, and quadratures the displacement and trapped variances against (4)–(6) over multiple positive parameter values. Numerical Legendre optimization independently checks the athermal rate function. Running `python verify.py` with NumPy and SciPy available yielded `PASS 432 independent deterministic matrix, quadrature and Legendre checks`. The universal statements are established by the proof above, not by the finite test grid.

## Relationship to prior work

Singh and Aghion (2026, arXiv:2610.08029v1, publicly posted October 6, 2026) study a thermal run-and-tumble particle in a bistable potential using exponential switching; their outlook identifies non-Markovian tumbling as a further direction. The present four-phase model is a deliberately isolated free/harmonic diagnostic, **not** an asserted solution of their bistable first-passage problem.

Farago and Smith (2024, arXiv:2401.01576) provide a general non-Markovian trapped-particle framework using arbitrary sojourn distributions and numerical stationary densities. Their freely accessible paper considers exponential, semi-Gaussian and half-\(t\) examples, not this exact Erlang-2/Markov *long-time-current equality with strict fluctuation gaps*. Di Crescenzo (2001) obtains exact Erlang-alternating telegraph transition densities, and Di Crescenzo, Iuliano and Verasani (2026) analyze Erlang-2 sojourns with a Bernoulli resetting mechanism, including zero-reset limits and moment formulas; these studies cover the underlying Erlang motion and some individual statistics, which are **not** claimed as new. Their accessible comparisons do not state the combined identical-SCGF / strict finite-time-and-trapped-variance theorem. Van Gisbergen and Redig (2019) establish large deviations for a lattice run-and-tumble model, including the standard Markov tilted-generator method; that method and the Markov formula are prior art.

A previous published mathematical finding entitled *Markov two-time laws do not identify memorylessness in stationary alternating renewal processes* constructs a different non-Markov renewal mixture with the **same two-time law** as a Markov chain. That does not imply the present claim: here the two-time laws differ, yet the complete level-one free-current large-deviation functions agree. These are complementary, not equivalent, non-identifiability mechanisms.

## Limitations

This is a statement about level-one long-time **free-displacement** large deviations and second moments of a **linear** harmonic trap, not path-space large deviations, full one-time distributions, first-passage statistics, entropy production, or arbitrary confining potentials. Matching is to a Poisson flip rate \(\lambda\) rather than equal mean reversal duration; imposing equal mean durations would produce a different comparison. The initial Erlang phase is stationary, not a newly started complete Erlang run. The conclusions do not establish that this exact equivalence is unique among renewal laws. Publication priority requires further inspection of inaccessible potentially relevant primary full texts, particularly Di Crescenzo (2001) and Macci (2016); only their abstracts were accessible in this review. Independent external validation has not been performed.

## References

1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential* (2026), arXiv:2610.08029v1, https://arxiv.org/abs/2610.08029. First public date: 2026-10-06.
2. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics* (2024), arXiv:2401.01576, https://arxiv.org/abs/2401.01576.
3. A. Di Crescenzo, *On random motions with velocities alternating at Erlang-distributed random times*, Advances in Applied Probability **33** (2001), 690–701, https://doi.org/10.1239/aap/1005091360.
4. A. Di Crescenzo, A. Iuliano and M. Verasani, *A Generalized Telegraph Process with Resetting to the Origin Driven by Bernoulli Trials* (2026), https://doi.org/10.1007/s10955-026-03670-7.
5. B. van Gisbergen and F. Redig, *Central limit theorem and large deviations for run and tumble particles on a lattice* (2019), arXiv:1910.03350, https://arxiv.org/abs/1910.03350.
6. C. Macci, *Large deviations for some non-standard telegraph processes*, Statistics & Probability Letters **110** (2016), 119–127, https://doi.org/10.1016/j.spl.2015.12.016.
