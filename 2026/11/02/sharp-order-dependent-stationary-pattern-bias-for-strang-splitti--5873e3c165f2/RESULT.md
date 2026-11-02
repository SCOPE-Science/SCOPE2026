# Sharp order-dependent stationary-pattern bias for Strang splitting on bipartite reaction–diffusion graphs

## Finding

Let \(G\) be any finite connected, unweighted, \(d\)-regular bipartite graph, with \(d\ge1\), and write its graph Laplacian as \(L=dI-\mathrm{Adj}(G)\). For any integer \(p\ge1\), consider the graph reaction–diffusion flow
\[
\dot u=-\kappa L u+u-u^{\circ(2p+1)},\qquad
0<\lambda:=2\kappa d<1.
\]
Let \(s\) be the sign vector of the two bipartition classes. The checkerboard line \(\{xs:x\in\mathbb R\}\) is invariant, and its continuous-time positive equilibrium has amplitude \(x_*=(1-\lambda)^{1/(2p)}\).

For every step length \(\tau>0\), let \(D_t=\exp(-\kappa tL)\) be the exact diffusion propagator and \(R_t\) the componentwise exact reaction propagator of \(\dot u=u-u^{\circ(2p+1)}\). Compare both palindromic Strang compositions
\[
S_D=D_{\tau/2}\circ R_\tau\circ D_{\tau/2},\qquad
S_R=R_{\tau/2}\circ D_\tau\circ R_{\tau/2}.
\]
On the invariant line, each map has precisely three fixed points, zero and a sign pair. Write their positive amplitudes as \(x_D\) and \(x_R\). Then
\[
\boxed{x_D^{2p}=\frac{\sinh(p(1-\lambda)\tau)}{\sinh(p\tau)},\qquad
x_R^{2p}=\frac{\sinh(p(1-\lambda)\tau)}{\sinh(p(1-\lambda)\tau)+\sinh(p\lambda\tau)}.}
\]
Both positive equilibria attract every strictly positive initial amplitude on the checkerboard line, both negative equilibria attract every strictly negative initial amplitude there, and both nonzero equilibria have the *same* scalar derivative \(\exp(-2p(1-\lambda)\tau)\). The origin is repelling on the line.

The stationary-amplitude bias obeys a sharp three-way classification:
\[
0<x_D^{2p}<1-\lambda\quad(0<\lambda<1),\qquad
\operatorname{sgn}\bigl(x_R^{2p}-(1-\lambda)\bigr)=\operatorname{sgn}(1-2\lambda).
\]
Thus the reaction-outside order overestimates the continuous checkerboard equilibrium for \(0<\lambda<1/2\), preserves it *exactly for every step length* when \(\lambda=1/2\), and underestimates it for \(1/2<\lambda<1\); the diffusion-outside order always underestimates it. The physical amplitude ratio satisfies
\[
\boxed{\left(\frac{x_R}{x_D}\right)^{2p}
=\frac{\cosh(p\tau/2)}{\cosh(p(1-2\lambda)\tau/2)}>1,\qquad
\lim_{\tau\to\infty}\frac1\tau\log\frac{x_R}{x_D}
=\frac12\min\{\lambda,1-\lambda\}.}
\]
The exponential separation rate in the last formula is independent of the odd reaction exponent \(2p+1\).

## Assumptions and scope

The graph is finite, connected, unweighted, regular and bipartite; no fixed number of vertices is assumed. Only the invariant checkerboard line is classified. The diffusion is exact graph-heat propagation, the reaction is the exact scalar nonlinear flow, and arithmetic is exact. The parameters satisfy \(p\in\{1,2,3,\ldots\}\), \(\kappa>0\), \(\lambda=2\kappa d\in(0,1)\), and \(\tau>0\). The motivating Allen–Cahn nonlinearity is the case \(p=1\). The model is a semidiscrete graph analogue, not an identification with the infinite-dimensional periodic PDE.

## Proof

**1. Invariant reduction.** Every vertex has all its \(d\) neighbors in the opposite bipartition. Hence \(Ls=2ds\), and pointwise odd powers preserve the sign vector: \((xs)^{\circ(2p+1)}=x^{2p+1}s\). Both exact subflows preserve the checkerboard line. The restricted original equation is \(\dot x=(1-\lambda)x-x^{2p+1}\), whose positive nonzero equilibrium has \(x_*^{2p}=1-\lambda\).

**2. Exact subflows.** The restricted diffusion sends \(x\mapsto e^{-\lambda t}x\). Solving \(\dot x=x-x^{2p+1}\) by setting \(w=|x|^{-2p}\) on a nonzero orbit yields
\[
R_t(x)=\frac{e^t x}{\bigl(1+(e^{2pt}-1)|x|^{2p}\bigr)^{1/(2p)}}
\]
for all real \(x\), with zero understood by continuity. Put \(\mu=1-\lambda>0\). Direct composition gives
\[
S_D(xs)=F_D(x)s,\quad F_D(x)=\frac{e^{\mu\tau}x}{\bigl(1+b_D|x|^{2p}\bigr)^{1/(2p)}},\quad
b_D=(e^{2p\tau}-1)e^{-p\lambda\tau},
\]
\[
S_R(xs)=F_R(x)s,\quad F_R(x)=\frac{e^{\mu\tau}x}{\bigl(1+b_R|x|^{2p}\bigr)^{1/(2p)}},\quad
b_R=(e^{p\tau}-1)\bigl(1+e^{p(1-2\lambda)\tau}\bigr).
\]
Both coefficients are strictly positive.

**3. Equilibria and attraction.** A scalar map \(F(x)=a x/(1+b|x|^{2p})^{1/(2p)}\) with \(a>1,b>0\) has fixed points \(0,\pm((a^{2p}-1)/b)^{1/(2p)}\), and no others. For \(x\ne0\), the exact reciprocal-amplitude recurrence is
\[
|F(x)|^{-2p}=a^{-2p}\bigl(|x|^{-2p}+b\bigr).
\]
Since \(a=e^{\mu\tau}>1\), this affine contraction converges from every finite positive reciprocal amplitude to its unique fixed point, while preserving the sign of \(x\). Differentiation at a nonzero fixed point gives \(F'(x)=a^{-2p}=e^{-2p\mu\tau}\); at zero the derivative is \(a>1\).

**4. Closed forms.** Substitute \(a=e^{\mu\tau}\) and the two expressions for \(b\). Elementary exponential identities give
\[
\frac{e^{2p\mu\tau}-1}{(e^{2p\tau}-1)e^{-p\lambda\tau}}
=\frac{\sinh(p\mu\tau)}{\sinh(p\tau)},
\]
and
\[
\frac{e^{2p\mu\tau}-1}{(e^{p\tau}-1)(1+e^{p(1-2\lambda)\tau})}
=\frac{\sinh(p\mu\tau)}{\sinh(p\mu\tau)+\sinh(p\lambda\tau)}.
\]
These are precisely the asserted positive fixed-point powers.

**5. Sharp bias sign.** The function \(z\mapsto\sinh z/z\) is strictly increasing on \(z>0\); its derivative has numerator \(z\cosh z-\sinh z>0\). Since \(0<\mu<1\), this gives \(\sinh(p\mu\tau)/\sinh(p\tau)<\mu\). For the other order,
\[
\frac{\sinh(p\mu\tau)}{\sinh(p\mu\tau)+\sinh(p\lambda\tau)}\gtrless\mu
\quad\Longleftrightarrow\quad
\frac{\sinh(p\mu\tau)}{\mu}\gtrless\frac{\sinh(p\lambda\tau)}{\lambda}.
\]
Strict monotonicity again makes this inequality equivalent to \(\mu\gtrless\lambda\), with equality only at \(\lambda=1/2\).

**6. Order separation and limits.** The addition formula \(\sinh(a)+\sinh(b)=2\sinh((a+b)/2)\cosh((a-b)/2)\) yields
\[
\frac{x_R^{2p}}{x_D^{2p}}
=\frac{\sinh(p\tau)}{\sinh(p\mu\tau)+\sinh(p\lambda\tau)}
=\frac{\cosh(p\tau/2)}{\cosh(p(1-2\lambda)\tau/2)}.
\]
Because \(|1-2\lambda|<1\), this is strictly greater than one. Finally, \(\log\cosh(ct)=|c|t+O(1)\) as \(t\to\infty\) for nonzero \(c\), and \(\log\cosh0=0\). Therefore the logarithm of the powered ratio grows as \(p\tau\min\{\lambda,\mu\}+O(1)\), and division by \(2p\tau\) proves the stated exponent.

The small-step leading stationary-amplitude-power errors follow additionally from Taylor expansion:
\[
x_D^{2p}=\mu-\frac{p^2\mu\lambda(2-\lambda)}6\tau^2+O(\tau^4),\qquad
x_R^{2p}=\mu+\frac{p^2\mu\lambda(1-2\lambda)}6\tau^2+O(\tau^4).
\]
These expansions reconcile the sharp long-step discrepancies with second-order local splitting behavior.

## Verification

The accompanying `CHECK.py` independently symbolically checks all three closed hyperbolic identities, the critical fixed-point identity, and both quadratic Taylor coefficients for each of \(p=1,2,3,4\). It also performs reproducible direct exact-subflow comparisons on the four-cycle, fixed-point substitutions, derivatives, and signed-order tests for 640 seeded parameter instances (7,704 reported probes). SymPy is used only for supplementary symbolic algebra; the argument above proves the theorem for **every** integer \(p\ge1\), every eligible graph and every positive step length.

For a concrete example, on the four-cycle \(d=2\), setting \(\kappa=1/8\) gives \(\lambda=1/2\). With the cubic reaction \(p=1\), the reaction-outside step fixes the exact checkerboard equilibria \(\pm s/\sqrt2\) for every \(\tau>0\), while the diffusion-outside step fixes \(\pm\sqrt{\sinh(\tau/2)/\sinh\tau}\,s\), strictly smaller in amplitude.

## Relationship to prior work

Luo, Quan, Tan and Wu (2026) study the diffusion-outside Strang order for the periodic Allen–Cahn PDE and prove uniform long-time Sobolev stability and finite-time error bounds. The present result does **not** extend those PDE conclusions to general graphs; it instead classifies exact stationary-pattern amplitudes on a distinct but natural graph-semigroup test class, including the reversed Strang order.

Li, Quan and Xu (2021) establish the maximum principle, modified-energy dissipation and finite-time convergence for scalar Allen–Cahn Strang splitting; those results neither specify these bipartite checkerboard amplitudes nor compare the two symmetric orders. Quan, Tan and Wu (2025) likewise treat stability and convergence under Neumann conditions.

Bösenhofer (2023) explicitly demonstrates order- and stepsize-dependent equilibrium bias for general **linear affine** reaction–diffusion splits. Thus broad steady-state nonpreservation by Strang splitting is well known and is not a novelty claim here. Its linear-affine analysis does not imply the odd-cubic nonlinear fixed-point powers, globally attracting checkerboard branches, sharp contrast crossing at \(\lambda=1/2\), or exponent-independent separation rate proved above. Available published mathematics was compared for those implications, not merely for matching terminology; historical priority is not exhaustively certified.

## Limitations

Attraction is only established *within the invariant checkerboard line*: transverse stability of the patterns in the full vertex state space may differ. The positive branches require \(0<\lambda<1\); neither behavior at \(\lambda=1\) nor the supercritical decay regime \(\lambda>1\) is classified here. This is an exact semidiscrete graph result, not an infinite-dimensional PDE or arbitrary spatial mesh theorem. Long-time fixed-point biases do not contradict fixed-finite-time second-order convergence as \(\tau\downarrow0\), and no universal claim about numerical roundoff or the full energy landscape is made.

## References

- R. Luo, C. Quan, Z. Tan, Y. Wu, *Stability and Error Estimates with Optimal ε-Dependence for Strang Splitting of the Allen–Cahn Equation*, arXiv:2610.14867v1 (first public 2026-10-10), https://arxiv.org/html/2610.14867v1.
- D. Li, C. Quan, J. Xu, *Stability and convergence of Strang splitting. Part I: Scalar Allen-Cahn equation*, arXiv:2108.05214, https://arxiv.org/abs/2108.05214.
- C. Quan, Z. Tan, Y. Wu, *Stability and Convergence of Strang Splitting Method for the Allen–Cahn Equation with Homogeneous Neumann Boundary Condition*, arXiv:2504.07520v1, https://arxiv.org/html/2504.07520v1.
- M. Bösenhofer, *Analysis and evaluation of steady-state and non-steady-state preserving operator splitting schemes for reaction-diffusion(-advection) problems*, Combustion and Flame **255** (2023), article 112881, https://doi.org/10.1016/j.combustflame.2023.112881.
