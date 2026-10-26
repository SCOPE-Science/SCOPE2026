# Unique nonlinear scalar closure for variance-feedback interacting diffusions and its inverse-gamma law

## Finding

Let \(N\ge 2\) particles in \(\mathbb R^d\), \(d\ge1\), have centered positions \(y_i=x_i-\overline x\), empirical variance \(S=N^{-1}\sum_i|y_i|^2\), and dissipative interaction
\[
D_{p,N}(y)=\frac1{N^2}\sum_{i,j=1}^N|y_i-y_j|^{p+2},\qquad p\ge0.
\]
**Structural classification.** There is a constant \(C=C(p,N,d)\) satisfying \(D_{p,N}(y)=C S^{(p+2)/2}\) for **every** nonzero centered configuration if and only if at least one of the following holds: \(p=0\); \(N=2\); or \((d,N,p)=(1,3,2)\). In these cases respectively \(C=2\), \(C=2^{p+1}\), and \(C=9\), consistently on overlaps.

In the unique nonlinear case with at least three particles, take the interacting-diffusion model of Hambly and Nguyen [1], with \(d=1\), \(N=3\), \(p=2\), \(q=1\), \(\kappa>0\), \(0\le\rho<1\), and deterministic \(S_0>0\). Set \(\lambda=\kappa^2(1-\rho^2)>0\) and \(\delta=2+27/\lambda\). Then the reciprocal variance
\[
Z_t=\frac3{\lambda S_t}
\]
is a squared-Bessel diffusion of dimension \(\delta\), starting at \(Z_0=3/(\lambda S_0)\). Hence, for every \(t>0\),
\[
\frac{3}{\lambda t S_t}\ \stackrel{\mathrm d}=\ \chi'^2_\delta\!\left(\frac{3}{\lambda t S_0}\right),
\]
where the right side is noncentral chi-squared with \(\delta\) degrees of freedom and the displayed noncentrality. In particular, \(S_t\to0\) almost surely, and
\[
tS_t\ \Longrightarrow\ \frac3{\lambda\chi^2_\delta}.
\]
For each \(r>0\), the moments of \(tS_t\) are finite if and only if \(r<\delta/2\); in that range,
\[
\lim_{t\to\infty}\mathbb E[(tS_t)^r]
=\left(\frac3{2\lambda}\right)^r\frac{\Gamma(\delta/2-r)}{\Gamma(\delta/2)}.
\]
In particular, \(\lim_{t\to\infty}t\mathbb E[S_t]=1/9\), independent of \(\lambda\), whereas the limiting law and its higher-moment threshold depend on \(\lambda\). At \(r\ge\delta/2\), \(\mathbb E[S_t^r]=\infty\) for every \(t>0\). The limiting random variable \(W=3/(\lambda\chi_\delta^2)\) satisfies
\[
\mathbb P(W>z)\sim
\frac{(3/(2\lambda))^{\delta/2}}{\Gamma(\delta/2+1)}z^{-\delta/2}\qquad (z\to\infty).
\]

## Assumptions and scope

In [1] the particle dynamics use independent real Brownian motions \(B^0,B^1,\dots,B^N\) and
\[
\mathrm dX_t^i=\frac1N\sum_{j=1}^N |X_t^j-X_t^i|^p(X_t^j-X_t^i)\,\mathrm dt
+\kappa(S_t)^q\bigl(\rho\,\mathrm dB_t^0+\sqrt{1-\rho^2}\,\mathrm dB_t^i\bigr).
\]
The scalar-closure classification is an identity for **all** centered deterministic configurations and any real \(p\ge0\). It does not assert that every variance process with shape-dependent drift is non-Markovian. The probability statements specialize to \(d=1\), \(N=3\), \(p=2\), \(q=1\), \(S_0>0\), and \(\lambda>0\); exact consensus initially is excluded. The Brownian dimension parameter \(\delta\) need not be an integer.

## Proof

**1. Algebraic characterization.** For arbitrary \(N\) and \(d\), \(\sum_{i,j}|y_i-y_j|^2=2N^2S\), so \(p=0\) gives \(D_{0,N}=2S\). For \(N=2\), centered positions are opposites, giving \(D_{p,2}=2^{p+1}S^{(p+2)/2}\). For three centered real positions, Newton's identities imply
\[
\sum_{i=1}^3 y_i^4=\frac12\left(\sum_{i=1}^3y_i^2\right)^2.
\]
Expanding \(\sum_{i,j}(y_i-y_j)^4\) yields
\[
\sum_{i,j=1}^3(y_i-y_j)^4
=6\sum_i y_i^4+6\left(\sum_i y_i^2\right)^2
=9\left(\sum_i y_i^2\right)^2.
\]
Thus \(D_{2,3}=9S^2\) in one spatial dimension.

To exclude all other cases let \(s=p+2>2\). For \(N\ge4\), compare the two centered collinear configurations
\[
A=(-u,u,0,\ldots,0),\qquad
B=(-u/\sqrt2,-u/\sqrt2,u/\sqrt2,u/\sqrt2,0,\ldots,0)
\]
for \(u>0\). Both have \(S=2u^2/N\). If \(v=2^{s/2}>2\), the difference between their **unordered** pairwise \(s\)-power sums is exactly
\[
u^s\,\frac{(v-2)(v^2-2v+2N-8)}v>0.
\]
Indeed the second factor is \(v(v-2)>0\) for \(N=4\), and is strictly positive for all \(N\ge5\). Hence no shape-free constant is possible for \(N\ge4\).

For \(N=3\), \(d\ge2\), compare an equilateral centered triangle with three centered collinear points, normalized to equal \(S>0\). The three unordered squared distances average \(3S\) for either configuration, but are all equal only in the equilateral case. Since \(w\mapsto w^{s/2}\) is strictly convex, their \(s\)-power sums differ.

It remains to treat \(N=3\), \(d=1\), \(s>2\). Compare \((a,0,-a)\) and \((-2b,b,b)\) with \(a=\sqrt3b>0\), so their variances agree. Equality of their \(s\)-power sums requires \(2+2^s=2\cdot3^{s/2}\). Setting \(h=s/2\) gives \(g(h)=(4/3)^h+2\cdot3^{-h}-2=0\). Since
\[
g''(h)=(\log(4/3))^2(4/3)^h+2(\log3)^2 3^{-h}>0,
\]
and \(g(1)=g(2)=0\), these are its only roots. With \(s>2\), necessarily \(s=4\), i.e. \(p=2\). The classification follows.

**2. Exact variance diffusion.** The centered Itô calculation gives (see [1, Proposition 2.2])
\[
\mathrm dS_t=\bigl[-D_{p,N}(Y_t)+c_N S_t^{2q}\bigr]\mathrm dt
+a_N S_t^{q+1/2}\mathrm d\beta_t,
\]
where \(c_N=d\kappa^2(1-\rho^2)(1-1/N)\), \(a_N=2\kappa\sqrt{(1-\rho^2)/N}\), and \(\beta\) is a Brownian motion while \(S_t>0\). At the stated parameters, \(c_3=2\lambda/3\), \(a_3=2\sqrt{\lambda/3}\), and the newly established identity gives
\[
\mathrm dS_t=\left(-9+\frac{2\lambda}{3}\right)S_t^2\,\mathrm dt
+2\sqrt{\lambda/3}\,S_t^{3/2}\,\mathrm d\beta_t.
\]
For \(Z_t=3/(\lambda S_t)\), Itô's formula gives
\[
\mathrm dZ_t=\left(2+\frac{27}{\lambda}\right)\mathrm dt+2\sqrt{Z_t}\,\mathrm dW_t,
\qquad W_t=-\beta_t.
\]
This is the squared-Bessel equation of dimension \(\delta>2\). Its paths remain positive and finite at every finite time; hence the inverted variance does likewise. The full particle system cannot explode on a finite interval while the variance stays bounded, since its drift and center-noise coefficient then remain bounded on that interval. The squared-Bessel process of dimension \(\delta>2\) tends to infinity almost surely, proving \(S_t\to0\).

**3. Distribution and moments.** The classical squared-Bessel transition kernel [2] says \(Z_t/t\) has noncentral chi-square distribution with degrees of freedom \(\delta\) and noncentrality \(Z_0/t\). As \(t\to\infty\), the latter parameter vanishes; continuity of the kernel yields the inverse-central-chi-square limit.

For \(r>0\), a noncentral chi-square is the Poisson mixture of central chi-squares with degrees \(\delta+2J\), where \(J\sim\operatorname{Poisson}(Z_0/(2t))\). The \(J=0\) component has positive probability at every \(t>0\). Since a central chi-square has finite inverse \(r\)-moment exactly when \(r<\delta/2\), this proves the sharp finite-time threshold. Below the threshold the inverse moments decrease with the degrees of freedom and the mixture converges termwise as its Poisson mean tends to zero, giving
\[
\mathbb E[(\chi^2_\delta)^{-r}]
=2^{-r}\frac{\Gamma(\delta/2-r)}{\Gamma(\delta/2)}.
\]
The \(r=1\) specialization simplifies to \(1/9\). Finally, the central chi-square density at zero is asymptotic to \(z^{\delta/2-1}/(2^{\delta/2}\Gamma(\delta/2))\), which yields the stated tail constant by integration.

## Verification

Run `python3 verify.py` from the extracted package. The script checks the exact three-point quartic identity for 361 integer triples, the linear-interaction identity at multiple population sizes, 216 strict nonclosure witnesses for \(N\ge4\), several distinct exponent witnesses for \(N=3\), six rational Itô normalizations, and gamma-moment identities. It is a finite algebraic supplement, not a substitute for the strict-convexity, diffusion, or asymptotic arguments above.

## Relationship to prior work

Hambly and Nguyen [1, Section 2] establish the general variance semimartingale and emphasize that its nonlinear dissipation is **generally** shape-dependent; [1, Theorem 3.5] provides a critical-homogeneity phase trichotomy through averaged shape dissipation, and [1, Section 7] derives explicit one-dimensional variance diffusions for **linear** interaction. Those results do not give the all-population/all-exponent scalar-closure classification or the noncentral-chi-square and inverse-gamma laws for the exceptional nonlinear three-particle case. The identity for centered three-point fourth powers is classical algebra; the squared-Bessel transition law is classical [2]. The contribution is the exhaustive shape-closure classification and its application to an exact nonlinear feedback model, not invention of either classical ingredient.

## Limitations

The inverse-gamma law applies only to the stated one-dimensional three-particle cubic interaction and critical feedback exponent. It is convergence in distribution, not almost-sure convergence of \(tS_t\). The classification concerns an identity across **every** configuration, not all possible alternative scalar Markov projections. General nonlinear feedback regimes, particle counts above three, and positive initial consensus are not solved by the limiting law. Similar reductions in unindexed literature remain a priority risk; an independent audit has not been performed.

## References

[1] B. Hambly and V. Nguyen, *Variance-Feedback Noise in Interacting Diffusions: Shape Dynamics and Mean-Field Limits*, arXiv:2610.20771v1 (first submitted 14 October 2026), https://arxiv.org/html/2610.20771v1 . Specifically Proposition 2.2, Lemma 2.3, Theorem 3.5, and Section 7.

[2] S. J. A. Malham, A. Wiese, and Y. Xu, *Direct Inversion for the Squared Bessel Process and Applications*, arXiv:2412.16655 (2024), https://arxiv.org/abs/2412.16655 , Section 2, Theorem 2.1.
