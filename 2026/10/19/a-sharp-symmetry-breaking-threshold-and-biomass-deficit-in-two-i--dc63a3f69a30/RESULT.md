# A sharp symmetry-breaking threshold and biomass deficit in two identical population patches

## Finding
For two identical Beverton–Holt patches with **decreasing logistic emigration**, there is an exact, global threshold separating one positive equilibrium from the existence of symmetry-broken positive equilibria. This threshold is independent of the common mortality fraction except through the isolated-patch carrying level; the linear reproduction spectral radius remains unchanged throughout the transition. Near onset the two asymmetric equilibria are locally attracting, and every asymmetric equilibrium has strictly less total biomass than the symmetric equilibrium.

Precisely, let \(0<c<1\), \(R>1/(1-c)\), and \(k>0\). Write \(a=1-c\), \(T=aR>1\), and \(u=T-1>0\). Set
\[
 f(z)=\frac{Rz}{1+z},\qquad p_k(z)=\frac{a}{1+\exp(2k(z-u))}\quad(z\ge0).
\]
Define the discrete-time map on \([0,\infty)^2\) by
\[
 \begin{aligned}
 F_{k,1}(x,y)&=(a-p_k(x))f(x)+p_k(y)f(y),\\
 F_{k,2}(x,y)&=p_k(x)f(x)+(a-p_k(y))f(y).
 \end{aligned}
\]
The two columns of the redistribution matrix sum to \(a<1\), and every entry lies strictly between zero and one. The map therefore has admissible positive dispersal and a fixed loss fraction \(c\). Put \(k_c=1/u\).

**Theorem.** For every parameter choice above:

1. The unique strictly positive *symmetric* equilibrium is \((u,u)\). It is locally asymptotically stable for \(0<k<k_c\), has a neutral antisymmetric multiplier at \(k=k_c\), and is linearly unstable in the antisymmetric direction for \(k>k_c\). The exact multipliers are \(1/T\) and \(ku\).
2. If \(0<k\le k_c\), \((u,u)\) is the **only** strictly positive equilibrium. If \(k>k_c\), there are **at least two** additional strictly positive equilibria, exchanged by the patch swap. No global uniqueness claim is made for those distant from threshold.
3. There is \(\varepsilon_0>0\) such that, for \(0<\varepsilon=ku-1<\varepsilon_0\), exactly two asymmetric equilibria lie in a fixed sufficiently small neighborhood of \((u,u)\). Both are locally asymptotically stable. Writing either as \((m+d,m-d)\), they obey
\[
 d=\pm\sqrt{\frac{\varepsilon}{\beta}}+O(\varepsilon^{3/2}),\qquad
 m=u-\frac{\varepsilon}{\beta uT}+O(\varepsilon^2),
 \quad
 \beta=\frac1{u^2}\left(\frac13+\frac{u+2}{T^2}\right)>0.
\]
Their two multipliers are \(1/T+O(\varepsilon)\) and \(1-2\varepsilon+O(\varepsilon^2)\).
4. At **every** asymmetric strictly positive equilibrium, \(x+y<2u\); symmetry breaking always entails an equilibrium total-biomass deficit. Yet \(\rho(DF_k(0,0))=T>1\) for every \(k>0\), so the reproduction spectral radius alone does not predict the symmetry-breaking transition.

In the transparent example \(c=1/2\), \(R=4\) one has \(u=1\), \(k_c=1\), \(\beta=13/12\), and, near onset, \(x+y=2-(12/13)(k-1)+O((k-1)^2)\).

## Assumptions and scope
The result concerns a deterministic discrete-time, two-patch single-species model, not an arbitrary network or all dispersal functions. Recruitment occurs before redistribution. Patches have identical Beverton–Holt recruitment and identical, density-decreasing emigration centered on their common no-dispersal carrying level \(u\). The positive parameter \(c\) represents density-independent mortality during redistribution. Local asymptotic stability refers to eigenvalues of the Jacobian strictly inside the complex unit circle. All asymptotic expansions use \(\varepsilon=ku-1\downarrow0\) with \(c,R\) fixed. No assertion is made about global attraction, the number or stability of remote asymmetric equilibria, or periodic and chaotic attractors.

## Proof
**1. Admissibility, change of coordinates, and homogeneous multipliers.** Let
\[
 h(z)=af(z)=\frac{Tz}{1+z},\qquad
 H_k(z)=(a-2p_k(z))f(z)=h(z)\tanh(k(z-u)).
\]
For \(m=(x+y)/2\), \(d=(x-y)/2\), the update is exactly
\[
 m'=\frac{h(m+d)+h(m-d)}2,\qquad
 d'=\frac{H_k(m+d)-H_k(m-d)}2.
\]
The positive symmetric equilibrium solves \(h(m)=m\) and hence is \(m=u=T-1\). Since \(h'(u)=1/T\) and \(H_k'(u)=ku\), the Jacobian in \((m,d)\) coordinates is diagonal at \((u,0)\), with multipliers \(1/T\) and \(ku\). This establishes the stated symmetric local stability classification (without asserting stability at the neutral endpoint).

**2. Every asymmetric positive equilibrium straddles \(u\) and loses biomass.** At any fixed point the sum relation is
\[
 h(x)+h(y)=x+y.
\]
Since \(h(z)-z=z(u-z)/(1+z)\), a strictly positive fixed point with \(x>y\) must satisfy \(x>u>y\). Strict concavity of \(h\) gives
\[
 2m=h(x)+h(y)<2h(m),
\]
so \(m<u\). In particular, writing \(s=x-u>0\), \(t=u-y>0\) yields \(t>s\) and \(x+y<2u\). The same conclusion holds after swapping the two patches.

**3. Global exclusion at and below threshold.** For \(x>u>y\) as above, the fixed-point difference equation would require
\[
 x-y=H_k(x)-H_k(y)=h(x)\tanh(ks)+h(y)\tanh(kt).
\]
For \(v>0\), \(\tanh(v)<v\), whence the right side is strictly smaller than \(k[h(x)s+h(y)t]\). Using the exact identities
\[
 h(x)-u=\frac{s}{T+s},\qquad h(y)-u=-\frac{t}{T-t},
\]
we get
\[
 h(x)s+h(y)t=u(s+t)+\frac{s^2}{T+s}-\frac{t^2}{T-t}<u(s+t),
\]
because \(t>s>0\) and \(0<T-t<T+s\). Thus \(H_k(x)-H_k(y)<ku(x-y)\). For \(ku\le1\) this contradicts the stationary difference equation. No asymmetric positive equilibrium exists for \(k\le k_c\).

**4. Global existence above threshold.** For each \(y\in(0,u)\), the positive number \(q(y)=h(y)-y=y(u-y)/(1+y)\) can be matched by a unique \(x(y)>u\) satisfying \(x(y)-h(x(y))=q(y)\). Indeed \(x-h(x)=x(x-u)/(1+x)\) is continuous and strictly increasing from zero to infinity for \(x\ge u\). Moreover \(x(y)\to u\) as \(y\to0\) or \(y\to u\). Every resulting pair satisfies the equilibrium sum equation. Define the continuous difference quotient
\[
 Q_k(y)=\frac{H_k(x(y))-H_k(y)}{x(y)-y}.
\]
The two endpoint limits are \(\lim_{y\downarrow0}Q_k(y)=0\) and \(\lim_{y\uparrow u}Q_k(y)=H_k'(u)=ku\). When \(k>k_c\), the intermediate value theorem supplies a \(y\in(0,u)\) for which \(Q_k(y)=1\). That pair solves both equilibrium equations and has positive unequal coordinates. Patch-swap symmetry supplies a second such equilibrium. This is an existence argument for every \(k>k_c\), not a numerical continuation argument.

**5. Supercritical, locally attracting onset.** Near \(d=0\), the equilibrium mean equation \(m=[h(m+d)+h(m-d)]/2\) has a unique even analytic solution by the implicit-function theorem, since \(1-h'(u)=u/T>0\). Taylor expansion gives
\[
 m(d)=u-\frac{d^2}{uT}+O(d^4).
\]
At \(z=u\) the derivatives required for the difference equation are
\[
 H_k'(u)=ku,\quad H_k''(u)=\frac{2k}{T},\quad
 H_k'''(u)=-\frac{6k}{T^2}-2uk^3.
\]
Substitution into the equilibrium difference equation, followed by division by \(d\ne0\), yields
\[
 0=ku-1-B(k)d^2+O(d^4),\qquad
 B(k)=\frac{k}{T^2}\left(1+\frac2u\right)+\frac{uk^3}{3}.
\]
At \(k_c=1/u\), this coefficient equals \(\beta=(1/3+(u+2)/T^2)/u^2>0\). Applying the implicit-function theorem to the analytic equation in \(z=d^2\) yields a unique nearby positive solution \(z=\varepsilon/\beta+O(\varepsilon^2)\) for \(\varepsilon>0\), and none for \(\varepsilon<0\). The two signs of \(d\) yield exactly the two nearby equilibria and the stated expansions.

For completeness, the Jacobian at \((m+d,m-d)\) in mean-difference coordinates has entries
\[
 A=\frac{h'(x)+h'(y)}2,\ B=\frac{h'(x)-h'(y)}2,\ C=\frac{H_k'(x)-H_k'(y)}2,\ D=\frac{H_k'(x)+H_k'(y)}2.
\]
At the bifurcating branch, \(A=1/T+O(d^2)\), \(B=h''(u)d+O(d^3)\), \(C=H_k''(u)d+O(d^3)\), and \(D=ku+[H_k''(u)(-1/(uT))+H_k'''(u)/2]d^2+O(d^4)\). The eigenvalue approaching one satisfies \(\lambda=D+CB/(\lambda-A)\), so direct substitution gives \(\lambda=ku-3B(k)d^2+O(d^4)=1-2\varepsilon+O(\varepsilon^2)\). The other eigenvalue equals \(1/T+O(\varepsilon)\). Both lie strictly inside the unit circle for all sufficiently small positive \(\varepsilon\), proving local asymptotic stability.

**6. Reproduction spectral radius.** At extinction, \(DF_k(0,0)=R D_k(0)\). The strictly positive redistribution matrix \(D_k(0)\) has each column summing to \(a\), so Perron–Frobenius theory gives \(\rho(DF_k(0,0))=Ra=T>1\), independent of \(k\). This quantity therefore cannot detect the symmetry-breaking threshold.

## Verification
The companion `verify.py` is executable using the Python 3 standard library only. It checks the exact rational cubic coefficient \(\beta=13/12\) for \(T=2\), reconstructs five pairs of asymmetric fixed points above onset using a one-dimensional bracket, checks both original equilibrium equations and the local Jacobian eigenvalues numerically, and confirms a strict biomass deficit in each test. The global threshold and existence assertions, the all-equilibrium biomass inequality, and the local branch expansions are analytical proofs above, not consequences of finite computation.

## Relationship to prior work
McGrane-Corrigan, Mason, and de Andrade Moral (2024), arXiv:2405.04505, introduce the relevant bounded-Kolmogorov, density-dependent, column-substochastic discrete population-map class; their Section 5 establishes existence and persistence under a spectral condition, and their numerical section studies heterogeneous source-sink situations. They explicitly do not establish uniqueness or stability of positive equilibria in that class. The present result selects a biologically interpretable **identical-patch** Beverton–Holt/logistic-emigration family and proves an exact global equilibrium multiplicity boundary plus stable symmetry breaking and a strict biomass penalty.

Tromeur, Rudolf, and Gross (2013/2016), arXiv:1305.2769, study linear stability for generalized **continuous-time** metapopulation flux laws and discuss density-dependent dispersal elasticities. Silva, de Castro, and Justo (2001) analyze stability effects of **positive density-dependent migration** and do not, in the available abstract, state this discrete logistic-emigration equilibrium threshold. Aarset and Pötzsche (2020) establish abstract bifurcation criteria for **integrodifference equations with fixed dispersal kernels**; their Beverton–Holt pitchfork examples concern a different spatial operator and different bifurcation parameters. O'Connell and Wang (2024 early access) study equilibrium biomass under an **inverse-fitness continuous-time logistic dispersal** law, not this discrete homogeneous-patch switch. Classical local pitchfork and implicit-function methods are not claimed as new.

## Limitations
This analysis establishes neither globally attracting basins nor uniqueness of all asymmetric equilibria for arbitrarily large \(k\). The critical symmetric equilibrium is nonhyperbolic; its nonlinear asymptotic behavior is not asserted. No conclusions are claimed for more than two patches, unequal habitat parameters, a different transfer function, or noisy demographic processes. Some historical relevant articles were accessible only as abstracts, and a fully exhaustive literature-priority determination is not claimed. The result is a mathematical statement about the specified ecological model, not an empirical prediction without parameter calibration.

## References
1. B. McGrane-Corrigan, O. Mason, and R. de Andrade Moral, *A density-dependent metapopulation model: Extinction, persistence and source-sink dynamics*, arXiv:2405.04505, initially submitted May 7, 2024. https://arxiv.org/abs/2405.04505
2. E. Tromeur, L. Rudolf, and T. Gross, *Impact of dispersal on the stability of metapopulations*, arXiv:1305.2769 (2013; revised 2016). https://arxiv.org/html/1305.2769v2
3. J. A. L. Silva, M. L. de Castro, and D. A. R. Justo, *Stability in a Metapopulation Model with Density-dependent Dispersal*, Bulletin of Mathematical Biology 63 (2001), 485–506. https://doi.org/10.1006/bulm.2000.0221
4. C. Aarset and C. Pötzsche, *Bifurcations in periodic integrodifference equations in C(Omega) I: Analytical results and applications*, Discrete and Continuous Dynamical Systems B 26 (2021), 1–60; first online July 24, 2020. https://doi.org/10.3934/dcdsb.2020231
5. E. O'Connell and L. Wang, *Total equilibrium biomass of a two-patch logistic equation with density-dependent dispersal*, Discrete and Continuous Dynamical Systems S 18 (2025), 3661–3682; early access September 11, 2024. https://doi.org/10.3934/dcdss.2024165
