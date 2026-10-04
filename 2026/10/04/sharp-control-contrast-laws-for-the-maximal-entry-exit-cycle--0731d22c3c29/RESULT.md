# Sharp control-contrast laws for the maximal entry-exit cycle
## Finding
For the singular toy model studied by Borsotti--Kuehn--Sensi, put \(R=\sqrt{u_M/u_m}>1\). Write the entry coordinate of the maximum-amplitude controlled limit cycle as
\[
y_{\infty}^{\mathrm{cycle}}=-b\,a(R),\qquad a(R)\in(1-R^{-1},1).
\]
The cycle equation in Proposition 3 becomes
\[
G(a,R):=\log\!\left(\frac{1-a}{1+Ra}\right)+(1+R)a=0.
\]
Its nonzero solution \(a(R)\) is strictly increasing on \((1,\infty)\). The maximal fast-flow height on this cycle, which is the ceiling used in the source's target-admissibility analysis for trajectories inside the cycle, is
\[
Z(R):=\frac{z_{\max}^{\mathrm{cycle}}}{b}=Ra(R)-\log(1+Ra(R)),
\]
and \(Z(R)\) is also strictly increasing.

With \(R=1+\delta\) and \(\delta\downarrow0\),
\[
a(R)=\frac32\delta-\frac32\delta^2+\frac{27}{20}\delta^3+O(\delta^4),
\]
\[
Z(R)=\frac98\delta^2-\frac98\delta^3+\frac{333}{320}\delta^4+O(\delta^5).
\]
Hence an arbitrarily small control contrast creates a cycle whose entry/exit amplitude is linear in the contrast, while its reachable fast-variable peak grows only quadratically.

As \(R\to\infty\),
\[
1-a(R)=(R+1)e^{-(R+1)}+O\!\left(R^3e^{-2(R+1)}\right),
\]
\[
Z(R)=R-\log(R+1)-R^2e^{-(R+1)}+O\!\left(R^4e^{-2(R+1)}\right).
\]
Thus strong control contrast drives the entry point exponentially close to the boundary \(y=-b\), whereas the normalized fast-variable peak grows as \(R-\log R+o(1)\).

## Assumptions and scope
The statement concerns the singular limit \(\varepsilon\to0\) of the toy model
\[
\dot y=\varepsilon u(t)-z(y+b),\qquad \dot z=zy,
\]
with \(b>0\) and measurable control satisfying \(0<u_m<u_M\). It uses the source's maximum-exit control and its resulting stable maximum-amplitude limit cycle. The parameter \(R\) is the square root of the control dynamic range, not the ratio itself. The asymptotics do not claim uniform error bounds for fixed positive \(\varepsilon\); the source estimates its singular strategies only up to the stated small-\(\varepsilon\) errors.

## Proof
Substituting \(y_{\infty}^{\mathrm{cycle}}=-ba\) and \(R=\sqrt{u_M/u_m}\) into the source's fixed-point equation gives \(G(a,R)=0\). The source already proves that the relevant nonzero root lies in \((1-R^{-1},1)\) and is unique there.

Direct differentiation gives
\[
G_a=\frac{a(R+1)(Ra-R+1)}{(a-1)(Ra+1)},\qquad
G_R=\frac{Ra^2}{Ra+1}.
\]
On the relevant root interval, \(Ra-R+1>0\), so \(G_a<0<G_R\). Therefore
\[
a'(R)=-\frac{G_R}{G_a}=\frac{Ra(1-a)}{(R+1)(Ra-R+1)}>0.
\]
Since \(x\mapsto x-\log(1+x)\) is strictly increasing for \(x>0\), and \(R\mapsto Ra(R)\) is strictly increasing, \(Z(R)\) is strictly increasing.

For the weak-contrast limit, divide \(G(a,R)\) by \(a^2\) and extend analytically to \(a=0\). At \((a,R)=(0,1)\), the extended equation vanishes and its derivative with respect to \(a\) equals \(-2/3\), so the implicit-function theorem gives an analytic nonzero branch. Substituting
\[
a=c_1\delta+c_2\delta^2+c_3\delta^3+O(\delta^4),\qquad R=1+\delta,
\]
and matching powers gives \(c_1=3/2\), \(c_2=-3/2\), and \(c_3=27/20\). Composition with \(Z=Ra-\log(1+Ra)\) gives the displayed expansion for \(Z\).

For strong contrast, put \(s=R+1\) and \(\epsilon=1-a\). The cycle equation is exactly
\[
\frac{\epsilon}{s-(s-1)\epsilon}=e^{-s+s\epsilon}.
\]
Because the source's root interval gives \(0<\epsilon<1/R\), this identity first yields \(\epsilon=O(se^{-s})\). Substitution back into the same identity then gives
\[
\epsilon=se^{-s}+O(s^3e^{-2s}).
\]
Finally, with \(x=R(1-\epsilon)\), Taylor expansion of \(x-\log(1+x)\) at \(x=R\) yields
\[
Z(R)=R-\log(R+1)-R^2e^{-(R+1)}+O(R^4e^{-2(R+1)}).
\]

## Verification
The normalization was checked directly against Proposition 3, equation (50), and the cycle-height formula in equation (52) of arXiv:2609.25747v1. The derivative factorization shows the monotonicity without numerical assumptions. The weak-contrast coefficients follow from coefficient matching through fourth order in \(a(R)\) and fifth order in \(Z(R)\); the strong-contrast estimate follows from the exact \(\epsilon\)-equation before any expansion. Numerical spot checks at \(R=1.01\), \(R=1.1\), \(R=2\), \(R=5\), and \(R=10\) were used only as consistency checks, not as proof.

## Relationship to prior work
Borsotti--Kuehn--Sensi prove existence, uniqueness within the relevant interval, and stability of the maximum-amplitude singular cycle, and they give its defining equation together with the exact fast-variable peak used to decide target admissibility. Their paper does not analyze dependence of that cycle on the control contrast \(R\), nor does it state the weak- or strong-contrast laws above. Earlier entry-exit and relaxation-oscillation work develops existence, stability, and entry-exit maps in uncontrolled or structurally different systems; it does not supply this parameter-sensitivity classification for the controlled toy model.

## Limitations
The result is specific to the source's toy model and to its singular maximum-exit cycle. It does not establish corresponding contrast asymptotics for the paper's general planar model, and it does not resolve the source's open uniqueness question for optimal multi-stage strategies. An equivalent calculation could exist in unindexed notes or application-specific control literature; targeted searches found no such statement.

## References
1. J. Borsotti, C. Kuehn, M. Sensi, *On the optimal control of entry-exit phenomena in planar fast-slow dynamical systems*, arXiv:2609.25747v1 (2026), especially Proposition 3, equations (50)--(52), and Section 4.1.
2. S. Ai, S. Sadhu, *The entry-exit theorem and relaxation oscillations in slow-fast planar systems*, Journal of Differential Equations 268 (2020), 7220--7249, DOI: 10.1016/j.jde.2019.11.067.
3. T.-H. Hsu, S. Ruan, *Relaxation Oscillations and the Entry-Exit Function in Multidimensional Slow-Fast Systems*, SIAM Journal on Mathematical Analysis 53 (2021), 3717--3758, DOI: 10.1137/19M1295507.
