# Heavy-tailed planar dynamics and exact dyadic post-burst recovery at a logistic endpoint

## Finding

Consider the autonomous positive rational map
\[
F_b(x,y)=\left(\frac{\alpha x}{y},\frac{\alpha y}{b y-c\alpha x}\right),
\qquad \alpha,c>0,\quad 0<b\le4,
\]
on the open wedge \(W_b=\{(x,y):x>0,\ y>0,\ by>c\alpha x\}\). This is the negative-quadratic-coefficient, autonomous subfamily of the planar folding example in [1].

**Theorem (critical endpoint and conditional recovery).** For every initial condition in \(W_b\), the first image lies on the positive graph \(\Gamma_b=\{(x,\alpha/(b-cx)):0<x<b/c\}\), parametrized by \(t=cx/b\). For \(0<b<4\), every subsequent iterate is positive and well-defined, and
\[
  y_n\le \frac{4\alpha}{b(4-b)}\quad(n\ge2),
\]
with the uniform bound sharp over initial conditions. At \(b=4\), apart from a countable family of critical-preimage values of the graph parameter, all forward iterates exist. The map has a physical invariant probability \(\pi\) supported on \(\Gamma_4\), with graph coordinate \(t\) having density
\[
  \frac{1}{\pi\sqrt{t(1-t)}}\,dt\qquad(0<t<1).
\]
For Lebesgue-almost every initial point in \(W_4\), all bounded continuous empirical averages converge to \(\pi\), and \(\limsup_{n\to\infty}y_n=+\infty\). Under \(\pi\), the vertical observable \(Y=y\) has, for every \(R\ge\alpha/4\),
\[
 \pi(Y>R)=\frac2\pi\arcsin\sqrt{\frac{\alpha}{4R}},
 \quad
 \pi(Y>R)\sim\frac{\sqrt\alpha}{\pi\sqrt R},
\]
and its moments satisfy
\[
 \mathbb E_\pi[Y^s]=\left(\frac\alpha4\right)^s
 \frac{\Gamma(\tfrac12-s)}{\sqrt\pi\,\Gamma(1-s)}
 \quad\text{if }s<\tfrac12,
\]
while \(\mathbb E_\pi[Y^s]=+\infty\) for \(s\ge\tfrac12\).

Condition on an extreme vertical observation \(Y_0>R\), where \(R>\alpha/2\), in the stationary system. Let \(\tau=\min\{n\ge1:y_n\ge\alpha/2\}\), the first return to the upper half \(t_n\ge1/2\) of the logistic-coordinate interval. Define
\[
 \beta_R=\arcsin\sqrt{\frac{\alpha}{4R}},\qquad
 q_R=\frac{\pi}{4\beta_R}>1,\qquad
 L_R=\lfloor\log_2 q_R\rfloor,\qquad
 \rho_R=q_R2^{-L_R}\in[1,2).
\]
Then **the entire conditional integer-valued law is exact**:
\[
 \mathbb P_\pi(\tau>n\mid Y_0>R)
    =\min\{1,q_R2^{-n}\}\qquad(n=0,1,2,\ldots),
\]
\[
 \mathbb E_\pi[\tau\mid Y_0>R]=L_R+1+\rho_R,
 \qquad L_R=\tfrac12\log_2 R+O(1).
\]
Moreover, for every fixed integer \(k\), the centered survival law is
\[
 \mathbb P_\pi(\tau-L_R>k\mid Y_0>R)
    =\min\{1,\rho_R2^{-k}\}
\]
for all sufficiently large \(R\). As \(R\to\infty\), every phase \(\rho\in[1,2]\) is the limit of some sequence \(\rho_R\); these phases give different centered discrete distributions. Consequently, the centered recovery time \(\tau-L_R\) **has no single limiting law**: its family of subsequential limits is governed by the dyadic lattice phase \(\rho\). The leading waiting time is logarithmic in burst height, but its order-one correction is asymptotically log-periodic.

## Assumptions and scope

All variables and parameters are real. Only the positive wedge \(W_b\) is considered. At \(b=4\), points whose logistic coordinate eventually equals \(1/2\) form a countable exceptional set of forward singularities on \(\Gamma_4\); their preimage in \(W_4\) is a countable union of one-dimensional level curves. Statements about typical trajectories exclude this measure-zero set. The stationary law \(\pi\) is a measure on the invariant graph, not an absolutely continuous planar measure. The entry into that graph occurs in one step; no assertion is made about invariant measures on other components of the rational map's maximal real domain.

## Proof

**1. Exact graph reduction and boundedness boundary.** For \((x,y)\in W_b\), write \(x'=\alpha x/y\). Then \(0<x'<b/c\), and direct algebra in the second coordinate gives
\[
 y'=\frac{\alpha y}{by-c\alpha x}=\frac{\alpha}{b-cx'}.
\]
Thus the first iterate belongs to \(\Gamma_b\). On this graph, \(x'=bx-cx^2\), and \(t=cx/b\) satisfies \(t'=bt(1-t)\). Conversely, the graph lift \((x,y)=(bt/c,\alpha/[b(1-t)])\) obeys the original rational recurrence at every nonsingular logistic iterate. For \(b<4\), every \(t\in(0,1)\) has \(0<t'\le b/4<1\), giving \(y_n\le\alpha/[b(1-b/4)]\) for \(n\ge2\). Initial points with \(t_1=1/2\) attain equality at \(n=2\). At \(b=4\), the original second-coordinate denominator vanishes at the current graph parameter \(t=1/2\), whose logistic image would be \(t'=1\); this corresponds to a pole in the next graph lift. Thus the singular initial parameters are exactly the countable preimages of the logistic critical point, and have zero one-dimensional Lebesgue measure.

**2. Physical measure and vertical moments at the endpoint.** The substitution \(t=\sin^2(\pi\theta)\) semiconjugates \(t\mapsto4t(1-t)\) to \(\theta\mapsto2\theta\pmod1\). Lebesgue measure on the circle is invariant and ergodic under doubling, and its pushforward has density \(dt/[\pi\sqrt{t(1-t)}]\). The map \((x,y)\mapsto t_1=c\alpha x/(4y)\) is a smooth submersion on \(W_4\), so, by Fubini/local change of variables, Lebesgue-almost every initial point produces a coordinate typical for the arcsine law. The physical-measure assertion follows by Birkhoff and the one-step graph reduction. Every neighborhood of \(t=1\) has positive arcsine measure; generic orbits visit each one infinitely often, which forces \(\limsup y_n=\infty\). Since \(Y=\alpha/[4(1-t)]\), the change of variables \(t=\cos^2\phi\), with \(\phi\) uniform on \((0,\pi/2)\), gives
\[
 \pi(Y>R)=\mathbb P\!\left(0<\phi<\arcsin\sqrt{\alpha/(4R)}\right)=2\beta_R/\pi.
\]
The Taylor expansion \(\arcsin z\sim z\) proves the tail coefficient. Integrating \((1-t)^{-s}\) against the beta \((1/2,1/2)\) density gives the displayed beta/gamma ratio when \(s<1/2\); near \(t=1\) the integrand is asymptotic to a constant times \((1-t)^{-s-1/2}\), proving divergence otherwise.

**3. Exact post-burst passage law.** The representation \(t_0=\cos^2\phi\) makes \(Y_0=\alpha/[4\sin^2\phi]\). Conditional on \(Y_0>R\), the angle \(\phi\) is uniform on \((0,\beta_R)\), with \(\beta_R<\pi/4\). At later integer times \(n\ge1\),
\[
 t_n=\sin^2(2^n\phi).
\]
Before \(\tau\), the iterated angle remains strictly below \(\pi/4\); at the first crossing it lies in \([\pi/4,\pi/2)\). Hence
\[
 \tau=\left\lceil\log_2\frac{\pi}{4\phi}\right\rceil
\]
outside the probability-zero boundary angles. In particular, \(\{\tau>n\}=\{\phi<\pi/(4\cdot2^n)\}\) for every integer \(n\ge0\); taking the proportion of the conditioned uniform interval proves the exact survival formula. Summing it over \(n\ge0\) gives \(\mathbb E[\tau\mid Y_0>R]=L_R+1+\rho_R\), because the first \(L_R+1\) terms are one and the remaining geometric tail has sum \(\rho_R\). Subtracting \(L_R\) yields the centered law. Finally, \(\beta_R\sim(\sqrt\alpha/2)R^{-1/2}\) proves \(L_R=\tfrac12\log_2 R+O(1)\).

For every \(\rho\in[1,2)\), set \(\beta_j=\pi/[4\cdot2^j\rho]\) and \(R_j=\alpha/[4\sin^2\beta_j]\). Then \(L_{R_j}=j\), \(\rho_{R_j}=\rho\), and \(R_j\to\infty\). Choosing phases \(\rho_j\uparrow2\) gives the additional endpoint \(\rho=2\) as a limit. Distinct phase values give distinct survival probabilities already at \(k=1\), establishing the complete family of subsequential laws and failure of a unique centered weak limit.

## Verification

The included standalone checker `verify.py` uses rational arithmetic to verify several graph identities and the sharp precritical bound. It also compares exact conditional passage probabilities and the mean with angle-interval partitions, checks the vertical-tail asymptotic numerically at a finite threshold, and reports `VERIFY_OK` if all checks pass. The proof above, rather than finite numerical checks, certifies the all-parameter and infinite-time statements. Reproduce with `python verify.py` (Python standard library only).

## Relationship to prior work

Sedaghat [1], especially equations (20)–(24), Theorem 10, and the paragraph after equation (31), gives the folding into a quadratic logistic core and the lifted graph \(y=\alpha/(ax+b)\). Its stated bounded-orbit theorem assumes \(0<b<4\) and does not assert an endpoint stationary law or conditional burst recovery. We use its folding transparently rather than claiming it as a discovery. The arcsine law and doubling conjugacy of the fully chaotic logistic map are classical. Freitas–Freitas–Todd [2] study hitting times of asymptotically small targets and extreme-value laws, not the exact law for the first return to the fixed macroscopic threshold after conditioning on a tall singular-observable burst. Lazaryan–Sedaghat [3] study a different semilinear–rational planar system; neither its model nor its reduction implies the present endpoint vertical-observable law. The individual background ingredients are known; the claimed model-specific contribution is their sharp combination at the previously excluded rational-system endpoint, particularly the complete conditional passage law and its log-periodic centered family.

## Limitations

This is a deterministic exact-solvable subfamily, not a general theorem on all rational planar maps. The physical measure is singular in ambient planar area; the set of finite-time poles is excluded. The endpoint formula uses the specific natural critical-point return threshold \(t=1/2\); other thresholds are not classified. The probability statements use invariant stationary initial data, except for the generic-orbit assertion. Historical originality may require additional specialist checking; no independent audit has been performed.

## References

[1] H. Sedaghat, “Folding, Cycles and Chaos in Discrete Planar Systems,” arXiv:1406.6721, first posted 2014-06-25, https://arxiv.org/abs/1406.6721. See Theorem 10, equations (20)–(24), (31), and the discussion of the graph following (31).

[2] A. C. M. Freitas, J. M. Freitas, and M. Todd, “Hitting Time Statistics and Extreme Value Theory,” arXiv:0804.2887, first posted 2008-04-17, https://arxiv.org/abs/0804.2887; Probability Theory and Related Fields 147 (2010), 675–710.

[3] N. Lazaryan and H. Sedaghat, “On Periodic and Chaotic Orbits in a Rational Planar System,” arXiv:1405.3124, first posted 2014-05-13, https://arxiv.org/abs/1405.3124.
