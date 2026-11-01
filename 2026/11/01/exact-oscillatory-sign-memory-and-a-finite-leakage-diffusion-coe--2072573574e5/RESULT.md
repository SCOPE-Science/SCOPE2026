# Exact oscillatory sign memory and a finite-leakage diffusion coefficient for a paired tent map

## Finding

Consider the symmetric paired tent map at the first postcritical Markov parameter \(q=(\sqrt3-1)/2\), as defined below. Under its stationary absolutely continuous probability \(\mu\), the left/right sign observable \(\sigma(x)=\operatorname{sgn}(x)\) has exact correlations, for every integer \(n\ge0\),

\[
C_n:=\int\sigma(x)\sigma(T^n x)\,d\mu(x)
=\bigl(\sqrt2q\bigr)^n\left[\cos\frac{n\pi}{4}+\frac1{\sqrt3}\sin\frac{n\pi}{4}\right].
\]

In particular, the decay rate \(\sqrt{2-\sqrt3}\) and oscillatory phase \(\pi/4\) are exact. The stationary occupation-sign sum \(S_N=\sum_{j=0}^{N-1}\sigma(T^jx)\) satisfies

\[
\frac{S_N}{\sqrt N}\ \Longrightarrow\ \mathcal N\!\left(0,1+\frac2{\sqrt3}\right),
\qquad
\operatorname{Var}_{\mu}(S_N)=\left(1+\frac2{\sqrt3}\right)N-\frac1{\sqrt3}+O\!\left((\sqrt{2-\sqrt3})^N\right).
\]

Moreover, the observed left/right sign process is **not a one-step Markov chain**: \(C_1=1/\sqrt3\) while \(C_2=2/\sqrt3-1\ne C_1^2=1/3\). This is an exact finite-leakage example in which a Markov interval itinerary produces a non-Markov coarse two-state observation. Matching its exact one-step flip probability to a symmetric two-state Markov surrogate overestimates the true long-run sign variance by the exact factor \(\sqrt3\).

## Assumptions and scope

Let \(q=(\sqrt3-1)/2\), \(s=2(1+q)=1+\sqrt3\), and define \(T:[-1,1]\to[-1,1]\) by

\[
T(x)=\begin{cases}
s(x+1)-1,&-1\le x\le-1/2,\\
-sx-1,&-1/2<x<0,\\
0,&x=0,\\
-sx+1,&0<x\le1/2,\\
s(x-1)+1,&1/2<x\le1.
\end{cases}
\]

Set \(\sigma(x)=-1\) for \(x<0\), \(\sigma(0)=0\), and \(\sigma(x)=1\) for \(x>0\). The probability \(\mu\) has Lebesgue density

\[
h(x)=\frac{1}{2(3-\sqrt3)}\begin{cases}
\sqrt3,&|x|<q,\\1,&q<|x|<1,
\end{cases}
\]

with arbitrary boundary values. Statements about \(C_n\), the Gaussian limit, and finite-time variance use \(X_0\sim\mu\), not arbitrary deterministic initial data; values at partition endpoints have zero \(\mu\)-measure. In the first two formulas the variance is with respect to \(X_0\sim\mu\). This is a *deterministic*, exactly evaluated real interval map, not a randomly switched cocycle.

The six open partition cells in increasing order are

\[
I_0=(-1,-1/2),\ I_1=(-1/2,-q),\ I_2=(-q,0),\ I_3=(0,q),\ I_4=(q,1/2),\ I_5=(1/2,1).
\]

## Proof

**Step 1 — full finite Markov structure.** Since \(2q(1+q)=1\), the images of the six partition cells cover respectively the unions with indices

\[
(0,1,2,3),\quad (3),\quad(0,1,2),\quad(3,4,5),\quad(2),\quad(2,3,4,5).
\]

Every branch is affine of absolute slope \(s\). Let \(\ell_i=|I_i|\). The symbolic itinerary, conditional on its current cell under \(\mu\), is a stationary Markov chain with transition probabilities \(P_{ij}=\ell_j/(s\ell_i)\) for a covered target cell and zero otherwise. That property follows from the constant conditional density on each cell and the affine full-cell image. Its invariant state weights are

\[
\boldsymbol\pi=\left(\frac18+\frac{\sqrt3}{24},\ \frac18-\frac{\sqrt3}{24},\ \frac14,\ \frac14,\ \frac18-\frac{\sqrt3}{24},\ \frac18+\frac{\sqrt3}{24}\right).
\]

Direct matrix multiplication gives \(\boldsymbol\pi P=\boldsymbol\pi\), which also proves invariance of the stated piecewise-constant spatial density. Every entry of \(P^5\) is positive; hence the six-state chain is primitive, mixing and stationary under \(\boldsymbol\pi\).

**Step 2 — signed symmetry block.** Reflection about zero permutes the six cells in reverse order. Set \(J\) to be the \(3\times3\) coordinate-reversal matrix and write \(R=P_{0:3,0:3}-P_{0:3,3:6}J\), using zero-based cell indices. On antisymmetric cell observables, the six-state transition matrix reduces exactly to \(R\). Its characteristic polynomial is

\[
\det(\lambda I-R)=\lambda\bigl(\lambda^2-2q\lambda+2q^2\bigr).
\]

The two nonzero odd eigenvalues are \(q(1\pm i)\). Symmetry and the invariant weights give

\[
C_n=2\,\boldsymbol\pi_{0:3}R^n\mathbf1,
\qquad C_0=1,\quad C_1=\frac1{\sqrt3},\quad C_2=\frac2{\sqrt3}-1.
\]

Cayley–Hamilton establishes the second-order recurrence \(C_{n+2}=2qC_{n+1}-2q^2C_n\) for \(n\ge1\); the displayed initial values verify that recurrence also at \(n=0\). Solving the recurrence proves the claimed exact all-lag formula. Equivalently,

\[
G(z):=\sum_{n\ge0}C_nz^n=\frac{1+(1/\sqrt3-2q)z}{1-2qz+2q^2z^2}
\]

for \(|z|<1/(\sqrt2q)\). In particular, \(G(1)=1+1/\sqrt3\) and \(G'(1)=1/(2\sqrt3)\).

**Step 3 — fluctuation law and boundary correction.** Because the symbolic process is a primitive finite-state Markov chain and \(\sigma\) is bounded and centered, the stationary finite-state Markov-chain central limit theorem applies. The Green–Kubo variance equals

\[
C_0+2\sum_{n\ge1}C_n=2G(1)-C_0=1+\frac2{\sqrt3}>0.
\]

Stationarity gives the exact finite identity

\[
\operatorname{Var}_{\mu}(S_N)=N C_0+2\sum_{n=1}^{N-1}(N-n)C_n.
\]

The exponential correlation bound permits extending both sums to infinity: the resulting constant is \(-2\sum_{n\ge1}nC_n=-2G'(1)=-1/\sqrt3\), and the omitted tail is \(O((\sqrt2q)^N)\). For a symmetric stationary two-state one-step Markov chain, the centered sign correlation at lag two must be the square of its lag-one correlation. Since the two values here differ, the sign process is not one-step Markov. The one-step flip probability is \(p=(1-C_1)/2=(1-1/\sqrt3)/2\). A symmetric stationary two-state Markov chain fitted to this value has correlations \(C_n^{\mathrm{Markov}}=(1-2p)^n=(1/\sqrt3)^n\) and long-run variance \(v_{\mathrm{Markov}}=(1+1/\sqrt3)/(1-1/\sqrt3)=2+\sqrt3\). Since \(v=1+2/\sqrt3\), division gives \(v_{\mathrm{Markov}}/v=\sqrt3\).

## Verification

The standalone `verify_paired.py` reconstructs every cell, its exact length, the transition matrix and stationary cell weights in \(\mathbb Q(\sqrt3)\). It checks the positivity of \(P^5\), the reduced characteristic polynomial, correlations at lags \(0\) through \(10\), the exact correlation generating function, the Green–Kubo coefficient, the finite-time constant, the exact two-state-surrogate variance ratio, and the lag-two non-Markov discrepancy. It uses exact symbolic identities, not floating-point fitting. Execute `python verify_paired.py` with SymPy installed. The finite-state CLT step is a standard theorem; symbolic identities alone do not prove it.

## Relationship to prior work

Horan (2019), Definition 4.1 and Section 4.6/Proposition 4.16, already introduced these paired tent maps, the first symmetric Markov parameter, its **six-cell Markov partition** and general finite transfer matrices and spectra. None of these structural ingredients is claimed as new. The finding instead identifies the *signed observable's* spectral weights, its exact oscillatory covariance at all lags, the closed-form finite-leakage Green–Kubo variance, the finite-time offset and the sharp \(\sqrt3\)-factor overestimate by the one-step-calibrated two-state Markov surrogate. Knowing eigenvalues without observable projections does not give these coefficients. Dolgopyat–Wright (2010/2012), González-Tokman–Peters (2024), and the later diffusion analysis of González-Tokman and collaborators provide general or small-leakage asymptotic information, not this particular finite-parameter exact sign law in the inspected results. Thus the new computation is **model-specific exact observable statistics**, not a new general CLT or general spectral theorem.

## Limitations

The formulas hold only at the specified symmetric postcritical Markov parameter and under the stated stationary absolutely continuous initialization. The result does not describe arbitrary driving, general perturbation parameters, transient initial densities, or a new mixing-rate bound for the entire family. The Markov partition and finite spectral framework were previously published. Direct symbolic derivability from this framework is a genuine originality/value boundary; an unindexed published computation of the exact sign covariance would cover the claim. Independent mathematical verification has not been performed.

## References

1. J. Horan, *Asymptotics for the second-largest Lyapunov exponent for some Perron–Frobenius operator cocycles*, arXiv:1910.12112, first posted 2019-10-26; Definition 4.1 and Section 4.6/Proposition 4.16. https://arxiv.org/abs/1910.12112
2. D. Dolgopyat and P. Wright, *The Diffusion Coefficient for Piecewise Expanding Maps of the Interval With Metastable States*, arXiv:1011.5330, first posted 2010-11-24; asymptotic diffusion coefficient at small leakage. https://arxiv.org/abs/1011.5330
3. C. González-Tokman and J. Peters, *Averaging for random metastable systems*, arXiv:2406.09672, first posted 2024-06-14; averaging and invariant densities for randomly driven paired tent maps. https://arxiv.org/abs/2406.09672
4. *Jumping for Diffusion in Random Metastable Systems*, *Annales Henri Poincaré*, doi:10.1007/s00023-026-01738-4; quenched CLT and small-leakage diffusion approximation. https://doi.org/10.1007/s00023-026-01738-4
