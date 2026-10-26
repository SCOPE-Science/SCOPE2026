# Sharp arrival-order crossover and vanishing-drift scaling for advective tracer passage

## Finding

For two homogeneous, one-dimensional absorbing-boundary tracer models at the same downstream distance \(L>0\), let the strictly positive drift speeds be \(v_1,v_2\) and the strictly positive dispersion coefficients be \(D_1,D_2\). Write \(F_i(t)\) for the fraction first arriving by time \(t>0\), and \(a_i=v_i^2/D_i\). The complete first-order arrival-order classification is

\[
F_1(t)\ge F_2(t)\ \text{for every }t>0
\quad\Longleftrightarrow\quad
D_1\ge D_2\ \text{and}\ a_1\ge a_2.
\]

The inequality is strict at every finite positive time unless the parameter pairs coincide. If neither pair of inequalities holds in either direction, the curves \(F_1\) and \(F_2\) cross **exactly once**, with a transversal crossing. In particular, with a common positive speed \(v\) but distinct dispersions \(D_1>D_2\), the more dispersed tracer has larger early arrival probability but smaller sufficiently late arrival probability. The unique crossing \(t_c\) obeys the strict bound \(t_c>L/v\).

There is a singular zero-drift law in the common-speed case: keep \(L,D_1>D_2>0\) fixed and send \(v\downarrow0\). Then

\[
v^2t_c(v)\longrightarrow y_*(D_1,D_2),
\]

where \(y_*\) is the **unique** positive solution of

\[
\frac1{D_1}h\!\left(\sqrt{\frac{y}{2D_1}}\right)
=\frac1{D_2}h\!\left(\sqrt{\frac{y}{2D_2}}\right),
\qquad h(z)=\frac{\phi(z)}z-\Phi(-z),
\]

with \(\phi\) and \(\Phi\) the standard normal density and cumulative distribution function. This constant has the sharp analytic localization

\[
0<y_*<\frac{2\log(D_1/D_2)}{1/D_2-1/D_1}.
\]

At exactly \(v=0\), in contrast, the higher-dispersion arrival fraction is strictly larger at **every finite time**, so the crossover escapes to infinity when positive drift vanishes.

## Assumptions and scope

The two transport models are \(X_i(t)=v_it+\sqrt{2D_i}\,W_i(t)\), started at zero, with \(L>0\) as an absorbing downstream threshold. Here each \(W_i\) is a standard Brownian motion; coupling or independence between the two is irrelevant because only marginal first-passage distributions are compared. Define \(T_i=\inf\{t\ge0:X_i(t)=L\}\), \(F_i(t)=\Pr\{T_i\le t\}\). Each \(v_i>0,D_i>0\) ensures eventual arrival with probability one. All comparisons are for continuous time \(t>0\). The separate zero-drift boundary statement uses \(v_1=v_2=0\) only as a limit; the main classification assumes positive drifts. The quantity compared is **absorbed first-passage mass** (cumulative recovered fraction), not resident concentration or pointwise concentration in a nonabsorbing medium.

## Proof

**1. Exact transport law.** The absorbing-boundary image solution gives the classical inverse-Gaussian first-passage density and CDF:

\[
f_{v,D}(t)=\frac{L}{\sqrt{4\pi Dt^3}}
\exp\!\left[-\frac{(L-vt)^2}{4Dt}\right],
\]

\[
F_{v,D}(t)=\Phi\!\left(\frac{vt-L}{\sqrt{2Dt}}\right)
+e^{vL/D}\Phi\!\left(-\frac{vt+L}{\sqrt{2Dt}}\right).
\]

The density integrates to one for \(v>0\), and \(F(0+)=0\), \(F(+\infty)=1\).

**2. Complete order classification.** For the two densities, direct algebra gives

\[
\log\frac{f_1(t)}{f_2(t)}=\frac At+Bt+C,
\]

where

\[
A=\frac{L^2}{4}\left(\frac1{D_2}-\frac1{D_1}\right),\quad
B=\frac14\left(\frac{v_2^2}{D_2}-\frac{v_1^2}{D_1}\right),\quad
C=\frac12\log\frac{D_2}{D_1}
+\frac L2\left(\frac{v_1}{D_1}-\frac{v_2}{D_2}\right).
\]

First assume \(D_1>D_2\), so \(A>0\). If \(a_1>a_2\), then \(B<0\); the log-density ratio decreases strictly from \(+\infty\) to \(-\infty\), hence the densities cross once, from \(f_1>f_2\) to \(f_1<f_2\). Since their integrals agree, \(F_1-F_2\) is strictly positive everywhere. If \(a_1=a_2\), then \(B=0\) but \(v_1/v_2=\sqrt{D_1/D_2}>1\), making both terms in \(C=\frac12\log(D_2/D_1)+\frac L2(v_1/D_1-v_2/D_2)\) negative. Again the ratio falls through one exactly once and \(F_1>F_2\).

If instead \(a_1<a_2\), then \(B>0\). The ratio is \(+\infty\) near both zero and infinity. It cannot be at least one at every time, because distinct normalized densities would then have different total integrals. The function \(A/t+Bt+C\) is strictly convex and has a unique minimum, so it has exactly two simple positive zeroes. Accordingly \(f_1-f_2\) has signs \(+,-,+\). The CDF difference \(G=F_1-F_2\) starts and ends at zero. It is positive after the first density crossing, negative before the second (using \(G(t)=-\int_t^\infty(f_1-f_2)\)), and strictly decreasing between them. Therefore \(G\) has precisely one finite positive zero, which is simple and changes sign from positive to negative.

Interchanging indices handles \(D_1<D_2\). If \(D_1=D_2\), identical drifts give identical distributions; otherwise the pathwise constant-drift coupling proves strict stochastic ordering by speed (equivalently, \(A=0\) and the log-density ratio is affine with one sign change). Combining all cases proves the displayed equivalence and exact crossing count.

**3. Crossing after the common mean travel time.** Fix \(D_1>D_2\) and common \(v>0\). Step 2 guarantees a unique crossing. At the shared mean \(t_0=L/v\), the CDF reduces to

\[
F_{v,D}(t_0)=\frac12+e^s\Phi(-\sqrt{2s}),\qquad s=\frac{vL}{D}.
\]

For \(s>0\), the function \(s\mapsto e^s\Phi(-\sqrt{2s})\) decreases strictly: its derivative is \(e^s[\Phi(-\sqrt{2s})-\phi(\sqrt{2s})/\sqrt{2s}]<0\) by the strict Gaussian Mills inequality. Larger \(D\) gives smaller \(s\), so \(F_{v,D_1}(t_0)>F_{v,D_2}(t_0)\). Because the unique crossing is from positive to negative, \(t_c>t_0\).

**4. Small-drift singular scaling.** Keep \(L,D_1>D_2>0\) fixed, and set \(t=y/v^2\), \(y>0\). Expanding the exact survival function \(1-F_{v,D}\) at fixed \(y\) gives, uniformly on compact intervals of \(y\in(0,\infty)\),

\[
\frac{1-F_{v,D}(y/v^2)}{v}\longrightarrow
\frac{L}{D}\left[\frac{\phi(z)}z-\Phi(-z)\right],\qquad z=\sqrt{\frac{y}{2D}}.
\]

Write the limiting survival difference as

\[
H(y)=L\left[\frac{h(\sqrt{y/(2D_1)})}{D_1}
-\frac{h(\sqrt{y/(2D_2)})}{D_2}\right].
\]

Differentiation yields \(H'(y)=k_{D_2}(y)-k_{D_1}(y)\), where

\[
k_D(y)=\frac{L}{\sqrt{4\pi D y^3}}e^{-y/(4D)}.
\]

The ratio \(k_{D_1}(y)/k_{D_2}(y)=\sqrt{D_2/D_1}\exp[\frac y4(1/D_2-1/D_1)]\) increases strictly through one at

\[
y_p=\frac{2\log(D_1/D_2)}{1/D_2-1/D_1}.
\]

As \(y\downarrow0\), \(H(y)\sim L(1/\sqrt{D_1}-1/\sqrt{D_2})/\sqrt{\pi y}<0\). As \(y\to\infty\), the exponentially slower-decaying \(D_1\) term makes \(H(y)>0\) for large \(y\), with \(H(y)\to0^+\). Thus \(H\) increases strictly up to \(y_p\), decreases thereafter, and has exactly one simple zero \(y_*\in(0,y_p)\). Uniform convergence and the already-proved uniqueness of the finite-\(v\) crossing, bracketed at any two fixed scaled times on opposite sides of \(y_*\), give \(v^2t_c(v)\to y_*\).

Finally, at \(v=0\) the classical reflection-principle CDF is \(F_{0,D}(t)=\operatorname{erfc}(L/\sqrt{4Dt})\), strictly increasing with \(D\) for each finite \(t\). This establishes the asserted discontinuous ordering at the vanishing-drift boundary and completes the proof.

## Verification

The independent executable file `check_first_passage.py` uses only the Python standard library. Invoke `python check_first_passage.py` alongside this document. It checks 300 numerical derivatives of the exact CDF against the first-passage density, 300 algebraic density-ratio identities, the illustrative single crossing, four small-drift scaled crossing values, and a drift–dispersion tradeoff example. For \(L=1\), \(D_1=4\), \(D_2=1\), and common \(v=1\), the crossing is \(t_c\simeq2.558169017584\), whereas the small-drift limit is \(y_*\simeq1.415604396416\) and \(y_p\simeq3.696784962986\). Numerical checks neither establish uniqueness nor certify the infinite-parameter assertions; those follow from the proof above.

## Relationship to prior work

The inverse-Gaussian passage law is classical and **is not claimed as new**. Molini, Talkner, Katul and Porporato (2010) derive first-passage laws and method-of-images conditions, including the constant-coefficient specialization. Bodin (2015), Sections 2–4, develops time-domain particle methods based on analytical transport breakthrough functions, and Russian, Dentz and Gouze (2016), Sections 2 and 4, compare advection–dispersion breakthrough curves under several parameter choices. These sources motivate the observable and provide its standard formulas; the inspected material does not state the two-parameter necessary-and-sufficient stochastic order, one-crossing theorem, strict common-speed mean bound, or singular \(v^{-2}\) crossover law. A distribution-free single-crossing theorem does not by itself supply these parameter boundaries, and the general inverse-Gaussian density formula alone requires further sign analysis and a singular-limit argument.

## Limitations

This result applies only to homogeneous one-dimensional Fickian advection–dispersion with an absorbing threshold, positive constant drifts in the main theorem, and a common detection distance. It does not cover resident concentration, sorption, reactions, variable velocity or dispersivity, finite injection durations, partially absorbing boundaries, or spatially heterogeneous media. The first-order stochastic dominance classification is not a statement about pairwise sample-path ordering under arbitrary couplings. Historical priority beyond the inspected sources is not independently established; a general comparison theorem for inverse-Gaussian laws may subsume the order classification, although the explicit singular crossover is a distinct additional statement.

## References

1. A. Molini, P. Talkner, G. G. Katul and A. Porporato, *First passage time statistics of Brownian motion with purely time dependent drift and diffusion*, arXiv:1009.0557, publicly posted 2010-09-02, https://arxiv.org/abs/1009.0557 .
2. J. Bodin, *From analytical solutions of solute transport equations to multidimensional time-domain random walk (TDRW) algorithms*, Water Resources Research 51 (2015), 1860–1871, doi:10.1002/2014WR015910, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014WR015910 .
3. A. Russian, M. Dentz and P. Gouze, *Time domain random walks for hydrodynamic transport in heterogeneous media*, Water Resources Research 52 (2016), 3309–3323, doi:10.1002/2015WR018511, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015WR018511 .
4. A. Kreft and A. Zuber, *On the physical meaning of the dispersion equation and its solutions for different initial and boundary conditions*, Chemical Engineering Science 33 (1978), 1471–1480, doi:10.1016/0009-2509(78)85196-3; historical reference consulted via bibliographic and secondary literature, not full text.
