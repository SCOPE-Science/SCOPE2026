# A random-radius law and conditional Gaussian fluctuations in high-dimensional harmonic run-and-tumble dynamics

## Finding

Consider the stationary, athermal, isotropic run-and-tumble particle in a harmonic trap in spatial dimension \(d\geq 2\), with fixed relaxation rate \(\mu>0\), propulsion speed \(v_0>0\), and Poisson orientation-refresh rate \(\gamma>0\). Put \(\alpha=\gamma/\mu\), and normalize its stationary position \(X_d\in\mathbb R^d\) as \(Z_d=\mu X_d/v_0\). For a common random sequence of stick-breaking masses \((P_j)_{j\geq1}\) with independent breaks \(V_j\sim\operatorname{Beta}(1,\alpha)\), set

\[
 P_j=V_j\prod_{k<j}(1-V_k),\qquad
 S=\sum_{j\geq1}P_j^2,\qquad T=\sum_{j\geq1}P_j^4.
\]

**High-dimensional stationary theorem.** With \(Q_d=\|Z_d\|^2\) and \(Y_d=\sqrt d\,(Z_d)_1\), the following assertions hold for every fixed \(\alpha>0\):

1. The exact conditional mean and mean-square error, given the masses, are
   \[
     \mathbb E[Q_d\mid(P_j)]=S,\qquad
     \mathbb E[(Q_d-S)^2\mid(P_j)]=\frac{2}{d}(S^2-T).
   \]
   Consequently \(Q_d\to S\) in \(L^2\) under the common-mass coupling, with the **exact** unconditioned error
   \[
      \mathbb E[(Q_d-S)^2]=\frac{2\alpha}{d(\alpha+1)(\alpha+2)(\alpha+3)}.
   \]
2. The joint radial and coordinate fluctuations converge *stably relative to the stick-breaking masses*:
   \[
      \left(Y_d,\sqrt d\,(Q_d-S)\right)
      \Longrightarrow
      \left(\sqrt S\,G_1,\sqrt{2(S^2-T)}\,G_2\right),
   \]
   where \(G_1,G_2\) are independent standard normal variables, independent of the full mass sequence. Thus the coordinate limit is a genuine centered Gaussian **variance mixture**, not generally a Gaussian law.
3. The limiting squared radius is random, with
   \[
   \mathbb ES=\frac1{\alpha+1},\qquad
   \operatorname{Var}(S)=\frac{2\alpha}{(\alpha+1)^2(\alpha+2)(\alpha+3)}>0.
   \]
   In particular the squared radius does **not** concentrate on a deterministic value as \(d\to\infty\), despite the asymptotic orthogonality of independent orientations. The limiting scaled-coordinate excess kurtosis is \(6\alpha/[(\alpha+2)(\alpha+3)]>0\).

A useful exact finite-dimensional diagnostic, derived in the proof from the same construction, is that the excess kurtosis of \(Y_d\) changes sign precisely as the real-valued dimension threshold \(d_c=4+6/\alpha\) is crossed: it is negative for integer \(d<d_c\), zero if an integer \(d=d_c\), and positive for integer \(d>d_c\). This diagnostic is **not separately claimed as an original formula**: prior work provides all-dimensional moment representations from which it can be calculated. The principal assertion here is the joint random-environment limit and its quantitative radial coupling.

## Assumptions and scope

For every integer \(d\ge2\), the position obeys \(\dot X_d(t)=-\mu X_d(t)+v_0U_d(t)\). The orientation \(U_d(t)\) is a unit vector refreshed at independent Poisson events of rate \(\gamma\); every refreshed direction is uniform on \(S^{d-1}\), independently of all earlier directions and event times. There is no thermal Gaussian noise, no interaction and no orientation persistence across a refresh. The parameters \(\mu,v_0,\gamma\) are independent of \(d\). Stationarity is understood via the uniquely defined infinite-past exponentially weighted integral; boundedness of the forcing makes the initial-condition term decay exponentially.

The random masses \((P_j)\) are common to all dimensions in the convergence statement, while directions may be sampled freshly and independently for each dimension. Conditional convergence means that for every bounded measurable \(h\) of the mass sequence and bounded continuous \(f\) on \(\mathbb R^2\), the expectation of \(h f(Y_d,\sqrt d(Q_d-S))\) converges to the expectation of \(h f(\sqrt S G_1,\sqrt{2(S^2-T)}G_2)\). Both \(S\) and \(T\) lie strictly between zero and one almost surely.

## Proof

**Step 1: common-mass stationary representation.** Solve the linear equation from the infinite past. With backward Poisson interarrival intervals \(\tau_j\overset{\mathrm{iid}}\sim\operatorname{Exp}(\gamma)\), and independent uniform spherical directions \(U_j^{(d)}\), it yields

\[
 Z_d=\sum_{j\ge1}P_jU_j^{(d)},\qquad
 P_j=(1-e^{-\mu\tau_j})\prod_{k<j}e^{-\mu\tau_k}.
\]

Indeed \(V_j=1-e^{-\mu\tau_j}\) has distribution \(\operatorname{Beta}(1,\gamma/\mu)\). The weights are positive, telescope to one almost surely, and are independent of the directions. The series converges absolutely. This is the vector version of the exact stationary stick-breaking construction already established for component marginals in Guéneau, Majumdar and Schehr (2026).

**Step 2: radial identities and quantitative convergence.** Conditionally on \((P_j)\), use \(\mathbb E U_j^{(d)}=0\), \(\mathbb E(U_i^{(d)}\cdot U_j^{(d)})^2=1/d\) for \(i\ne j\), and the fact that distinct unordered-pair dot products are uncorrelated (also when they share an index). Expanding gives

\[
 Q_d=S+2\sum_{i<j}P_iP_j(U_i^{(d)}\cdot U_j^{(d)}),
 \qquad \operatorname{Var}(Q_d\mid P)=\frac4d\sum_{i<j}P_i^2P_j^2=\frac2d(S^2-T).
\]

These identities hold for the infinite series by \(L^2\)-approximation because \(\sum_jP_j=1\).

**Step 3: moments of the random limiting radius.** A fresh stick-breaking factor \(V\sim\operatorname{Beta}(1,\alpha)\) gives the fixed-point relations

\[
 S\overset{\mathrm{law}}=V^2+(1-V)^2S',\quad
 T\overset{\mathrm{law}}=V^4+(1-V)^4T',
\]

with independent copies on the right. Applying beta moments \(\mathbb E V^k=k!/\prod_{j=1}^k(\alpha+j)\) and \(\mathbb E(1-V)^k=\alpha/(\alpha+k)\), including the mixed moment \(\mathbb E[V^2(1-V)^2]=2\alpha/[(\alpha+2)(\alpha+3)(\alpha+4)]\), gives

\[
 \mathbb ES=\frac1{\alpha+1},\quad
 \mathbb ET=\frac6{(\alpha+1)(\alpha+2)(\alpha+3)},\quad
 \mathbb ES^2=\frac{\alpha+6}{(\alpha+1)(\alpha+2)(\alpha+3)}.
\]

Subtracting the square of \(\mathbb ES\) proves the asserted strictly positive variance; subtracting \(\mathbb ET\) from \(\mathbb ES^2\) proves the exact \(L^2\) error. These formulas for the classical stick-breaking diversity index are used, not presented as a novel probability identity.

**Step 4: conditional joint central limit.** For any fixed number \(K\) of directions, write \(U_i^{(d)}=g_i/\|g_i\|\) with independent standard Gaussian \(d\)-vectors \(g_i\). Joint multivariate central limit theory for the centered products \(d^{-1/2}\sum_{a=2}^d g_{ia}g_{ja}\), together with the law of large numbers \(\|g_i\|/\sqrt d\to1\), implies that the finite array

\[
 \bigl(\sqrt d\,(U_i^{(d)})_1,\sqrt d\,U_i^{(d)}\cdot U_j^{(d)}:1\le i<j\le K\bigr)
\]

converges to mutually independent standard normals. The first-coordinate Gaussian terms are independent of the sums over coordinates \(2,\ldots,d\), and their own contributions to the pair dot products vanish at rate \(d^{-1/2}\). Distinct pair-product summands have zero covariance; their multivariate normal limit is therefore independent across pairs.

The finite weighted sums converge to independent normals with conditional variances \(S_K=\sum_{i\le K}P_i^2\) and \(4\sum_{i<j\le K}P_i^2P_j^2\). To pass to the infinite sums **uniformly in dimension**, note that the conditional variance of the omitted coordinate sum is \(S-S_K\), while the conditional variance of the omitted radially scaled pair sum is at most \(4S(S-S_K)\). Both vanish as \(K\to\infty\) for every realized positive mass sequence. Conditional characteristic functions, then dominated convergence against any bounded observable of the masses, give the stated stable joint limit with two independent normals.

**Step 5: non-Gaussianity and finite-dimensional diagnostic.** The limit \(Y=\sqrt S G_1\) has \(\mathbb EY^2=\mathbb ES\) and \(\mathbb EY^4=3\mathbb ES^2\). Its excess kurtosis equals \(3\operatorname{Var}(S)/(\mathbb ES)^2=6\alpha/[(\alpha+2)(\alpha+3)]\), so it cannot be normal. For finite \(d\), the spherical identity \(\mathbb E[(\sqrt d\,U_{j1}^{(d)})^4]=3d/(d+2)\) gives

\[
 \mathbb EY_d^4=3\mathbb ES^2-\frac6{d+2}\mathbb ET,
\quad
 \operatorname{ExKurt}(Y_d)=\frac{6[\alpha(d-4)-6]}{(d+2)(\alpha+2)(\alpha+3)},
\]

which verifies the stated sign criterion and converges to the positive mixture excess kurtosis.

## Verification

The supplied `verify.py` independently evaluates exact beta-moment fixed-point identities using rational arithmetic for seven parameter values and exact finite-dimensional fourth-moment identities for five dimensions. It also samples independent beta breaks and normalized Gaussian sphere directions, checking the radial squared-error formula, coordinate second moments, and conditional radial-fluctuation variance. Executing `python verify.py` from a directory containing the standalone file completes 123 assertions using its fixed random seed. The proof above, not the finite random experiment, establishes all infinite-dimensional limits. The simulation uses a finite stick-breaking truncation whose remainder is allocated to its last mass; it is not an exact infinite-sequence realization.

## Relationship to prior work

Guéneau, Majumdar and Schehr (arXiv:2602.08436v1, February 9, 2026) introduce the exact stationary Dirichlet-process/stick-breaking representation and the all-dimensional coordinate distribution and moment formulas. Their result is **stronger for finite-dimensional stationary distributions** than any isolated moment calculation here; in particular the finite-dimensional kurtosis identity is an accessible consequence of that work. The added assertion is a **joint dimension-asymptotic limit** conditional on the common persistent-run weights, quantifying a random limiting radius, a Gaussian variance-mixture coordinate, their simultaneous fluctuation scaling, and exact radial mean-square convergence. It requires an infinite-array conditional CLT, not a direct parameter substitution in a fixed-dimensional density.

Frydel (arXiv:2309.12537, 2023) also derives stationary moment recursions for harmonic run-and-tumble oscillators, including general-dimensional moments, without presenting the joint random-environment limit. Smith, Le Doussal, Majumdar and Schehr (arXiv:2207.10445, 2022) analyze a different finite-orientation switching mechanism; their higher-dimensional extensions have decoupled coordinate chains, not independent uniformly resampled spherical directions. Classical Dirichlet-process theory already studies the Simpson concentration statistic \(S\). No originality is claimed for its general combinatorial moments or for the elementary fact that a finite collection of random high-dimensional sphere vectors becomes asymptotically orthogonal.

## Limitations

The direction law must be fully refreshed uniformly on the sphere at every independent Poisson event. For anisotropic or correlated directions, state-dependent tumbling, active Brownian angular diffusion, an added thermal bath, or dimension-dependent rates, the stated limits need not hold. The theorem concerns stationary distributions, not temporal mixing, hitting times, or many-particle thermodynamic limits. The law of \(S\) is specified by the stick-breaking construction; no elementary density for it is asserted. Full originality of the explicit physical interpretation remains subject to possible broader theorems about random Dirichlet means on growing spheres; prior full-dimensional stationary representations are acknowledged.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (February 9, 2026), especially Secs. II–IV and Appendix C; published in Physical Review E 114, 014144 (2026), DOI 10.1103/mlkm-vgbd.
2. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537 (2023), especially Secs. IV, VI and VII.
3. N. R. Smith, P. Le Doussal, S. N. Majumdar and G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445 (2022), especially Sec. IV.6.
4. T. S. Ferguson, *A Bayesian analysis of some nonparametric problems*, Annals of Statistics 1 (1973), 209–230; original Dirichlet-process framework.
5. D. M. Cifarelli and E. Regazzini, *Distribution functions of means of a Dirichlet process*, Annals of Statistics 18 (1990), 429–442; Dirichlet-process mean functionals.
