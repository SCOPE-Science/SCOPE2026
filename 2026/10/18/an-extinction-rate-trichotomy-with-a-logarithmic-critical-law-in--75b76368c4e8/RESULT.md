# An extinction-rate trichotomy with a logarithmic critical law in a weak-Allee predator–prey system

## Finding
For the positive-population ODE below, set \(c=\gamma/e\) and assume \(\beta A>c\). For **every** fixed \(\alpha>0\), a nonempty open sector of strictly positive initial populations approaches total extinction. Its sharp asymptotic law changes at \(\alpha=c\):

* If \(0<\alpha<c\), set \(r_*=(c-\alpha)/(\beta-\alpha/A)\). Then
  \[\lim_{t\to\infty}t u(t)=\frac{A(c-\alpha)}{\alpha(\beta A-c)},\qquad \lim_{t\to\infty}t v(t)=\frac{\beta A-\alpha}{\alpha(\beta A-c)}.\]
* If \(\alpha=c\), with \(k=\beta-c/A>0\), then
  \[\lim_{t\to\infty}t v(t)=\frac1c,\qquad\lim_{t\to\infty}t\log t\,u(t)=\frac1k.\]
* If \(\alpha>c\), then
  \[\lim_{t\to\infty}t v(t)=\frac1c,\qquad \lim_{t\to\infty} t^{\alpha/c}u(t)=C(u(0),v(0))\in(0,\infty).\]

This is a theorem about a sectorial extinction basin, **not** global extinction or Lyapunov stability of the origin on the entire nonnegative quadrant. The prey-only axis has increasing prey density near the origin.

## Assumptions and scope
Fix \(A,\beta,\gamma,e,\eta,\alpha>0\), with \(\beta A>\gamma/e\), and consider positive solutions of
\[\dot u=\alpha u\left(\frac{u(1-u)}{u+A}-\frac{v}{1+\beta u}\right),\qquad
\dot v=v\left(\frac{\beta u}{1+\beta u}-\frac{\gamma v}{e+\eta v}\right).\]
Here \(u\) is prey density and \(v\) predator density. This is the spatially homogeneous, diffusion-free reaction system of Ye--Zhou (2023); no diffusion, delay, stochasticity, or claim about all initial states is included. The theorem asserts existence of constants \(R,\delta>0\), depending on the fixed parameters, such that **every** \(0<v(0)<\delta\), \(0<u(0)<R v(0)\) obeys the stated law. The constant \(C\) in the third case is strictly positive but generally depends on the initial condition. Time \(t\) is original physical ODE time.

## Proof
**1. Exact ratio system.** Put \(r=u/v>0\) and \(c=\gamma/e\). Direct differentiation gives
\[\dot v=v^2 G(r,v),\qquad \dot r=rv B(r,v),\]
with
\[G(r,v)=\frac{\beta r}{1+\beta rv}-\frac{\gamma}{e+\eta v},\]
\[B(r,v)=\frac{\alpha r(1-rv)}{A+rv}-\frac{\alpha+\beta r}{1+\beta rv}+\frac{\gamma}{e+\eta v}.\]
The values on the blown-up boundary \(v=0\) are
\[G(r,0)=\beta r-c,\qquad B(r,0)=c-\alpha+(\alpha/A-\beta)r.\]
Since \(\beta A>c\), the interval \((0,\min\{A,c/\beta\})\) is nonempty.

**2. Forward-invariant extinction sectors.** If \(0<\alpha<c\), the single positive zero of \(B(r,0)\) is
\[r_*=(c-\alpha)/(\beta-\alpha/A),\]
which lies strictly below both \(A\) and \(c/\beta\): each inequality reduces to \(c<\beta A\). Choose \(r_*<R<\min\{A,c/\beta\}\). Then \(B(R,0)<0\). If \(\alpha>c\), choose \(R>0\) sufficiently small that \(R<\min\{A,c/\beta\}\) and \(B(r,0)<0\) for \(0\le r\le R\). If \(\alpha=c\), put \(k=\beta-c/A>0\). Here \(B(r,0)=-kr\), while \(B(0,v)=\gamma/(e+\eta v)-c<0\). Moreover \(\partial_r B(0,0)=-k<0\). Hence, by continuity of \(\partial_r B\), one can choose \(R,\delta>0\) so that \(B(r,v)<0\) throughout \(0\le r\le R\), \(0<v\le\delta\). For the other two cases, continuity similarly supplies \(\delta>0\) with \(B(R,v)<0\) for \(0<v\le\delta\).

Shrink \(\delta\) as needed so that on the closed wedge \(0\le r\le R\), \(0<v\le\delta\), both \(G(r,v)\le -d_0<0\) and \((\dot u)/(uv)<0\) for \(u>0\). These follow from the strict limiting inequalities \(\beta R<c\), \(R<A\). Along \(r=R\), \(\dot r<0\); along \(v=\delta\), \(\dot v<0\). Thus the positive open wedge is forward invariant, and both populations strictly decrease. Because the vector field is smooth there and each per-capita rate is bounded, positivity and global forward existence follow. Also
\[-cv^2\le\dot v\le-d_0v^2,\]
so \(v(t)\to0\), and \(\tau(t)=\int_0^t v(s)\,ds\to\infty\). Indeed \(v(t)\ge(1/v(0)+ct)^{-1}\).

**3. Subcritical exponent.** For \(0<\alpha<c\), reparametrize by \(\tau\). Then \(dr/d\tau=r B(r,v)\), with \(v\to0\), and the limiting right side is logistic with attracting positive equilibrium \(r_*\): \(B(r,0)>0\) for \(0<r<r_*\), and \(B(r,0)<0\) for \(r_*<r\le R\). Uniform convergence of \(B(r,v)\to B(r,0)\), trapping between \(r_*\pm\varepsilon\) for arbitrary \(\varepsilon>0\), and \(B(0,v)>0\) for small \(v\) rule out convergence to zero and establish \(r(t)\to r_*\). Consequently
\[\frac{\dot v}{v^2}\to \beta r_*-c=-d,\qquad d=\frac{\alpha(\beta A-c)}{\beta A-\alpha}>0.\]
Integrating \((1/v)'=-\dot v/v^2\to d\) gives \(t v(t)\to1/d\). As \(u=rv\), \(t u(t)\to r_*/d\), yielding both displayed constants.

**4. Critical logarithm.** For \(\alpha=c\), the sector construction gives \(r\) decreasing. Its limit cannot be positive because \(B(r,0)=-kr<0\) for \(r>0\); hence \(r\to0\). Then \(G(r,v)\to-c\), and \(t v(t)\to1/c\). With \(\tau=\int v\,dt\), this implies \(\tau\sim(1/c)\log t\). In \(\tau\)-time, \(dv/d\tau=vG(r,v)\), and eventually \(G\le-c/2\); hence \(v(\tau)\) decays exponentially and \(\int_0^\infty v(\tau)\,d\tau<\infty\). Taylor's theorem on the compact small wedge gives \(B(r,v)=-kr+O(v)\). Thus \(dr/d\tau\ge-kr^2-Cvr\). Multiplying by the integrating factor \(\exp(C\int_0^\tau v(s)ds)\), which remains bounded above and below, and comparing with \(w'=-k w^2\), shows \(r(\tau)\ge c_0/(1+\tau)\) for some \(c_0>0\). Therefore \(v/r\to0\). The exact reciprocal derivative now satisfies
\[\frac{d}{d\tau}\left(\frac1r\right)=-\frac{B(r,v)}r=k+O(v/r)\to k.\]
It follows that \(\tau r(\tau)\to1/k\), and therefore \(r(t)\sim c/(k\log t)\). Multiplication by \(v(t)\sim1/(ct)\) establishes \(t\log t\,u(t)\to1/k\).

**5. Supercritical power and positive amplitude.** For \(\alpha>c\), the chosen wedge satisfies \(B(r,v)\le-\sigma<0\) for some \(\sigma>0\). Thus \(r(\tau)\le r(0)e^{-\sigma\tau}\), and \(r\to0\). Again \(tv\to1/c\), while \(dv/d\tau=vG\) gives exponential decay of \(v(\tau)\). Both \(r\) and \(v\) are integrable over \(\tau\in[0,\infty)\). A direct cancellation yields
\[\frac{d}{dt}\log\left(\frac{u}{v^{\alpha/c}}\right)
=\alpha u\left(\frac{1-u}{u+A}-\frac{\beta}{c(1+\beta u)}\right)
+\alpha v\left(\frac{e}{e+\eta v}-\frac1{1+\beta u}\right).\]
On the small wedge its absolute value is bounded by \(K_0(u+v^2)\). Since \(dt=d\tau/v\), its absolute time integral is bounded by \(K_0\int_0^\infty(r(\tau)+v(\tau))d\tau<\infty\). Thus \(u(t)/v(t)^{\alpha/c}\) converges to a **strictly positive, finite** constant. Combining this with \(tv\to1/c\) proves the stated \(t^{\alpha/c}\)-law.

**6. Coexistence alongside extinction (exact witness).** For \(A=3/8\), \(\beta=6\), \(\gamma=\eta=2\), \(e=1\), the reaction system has positive equilibria \((u,v)=(1/12,1/4)\) and \((1/4,3/4)\) for all \(\alpha>0\), obtained by substitution. At \(\alpha=1/2\), the smaller equilibrium is a saddle (negative Jacobian determinant), while the larger has trace \(-11/100\) and determinant \(3/625\), hence is a locally attracting coexistence equilibrium. The sector above is an open extinction basin for these same parameters. These are genuinely distinct local outcomes despite the absence of a prey-only Allee extinction threshold.

## Verification
`verify.py` uses exact symbolic arithmetic to reconstruct the ratio dynamics and its boundary expansion, both asymptotic constants, and the two equilibrium/stability calculations. Its additional finite numerical integration checks only illustrate trends; they do not establish the \(t\to\infty\) limits. Run `python verify.py` with SymPy and SciPy installed. The proof above, not the numerical checks, establishes the infinite-time claims.

## Relationship to prior work
Ye and Zhou (2023, arXiv:2306.11818, originally submitted 2023-06-20) study this exact prey-growth and hyperbolic-mortality reaction law with network diffusion, computing positive equilibria, local stability and Turing regions, and illustrating spatial patterns. Sections 1--3 of their open HTML version were inspected; the relevant ODE/stability and network-Turing sections do not provide an origin-sector extinction-rate trichotomy. Liu et al. (2019), a precursor treating weak Allee effects and delay, emphasize Turing thresholds and spatial patterns; an accessible abstract and indexed concluding material were compared, but its complete article was not accessible for review and remains an originality risk. Broader mathematical literature on degenerate planar systems may contain equivalent local asymptotics. The present theorem is specifically about the original ODE's positive-sector extinction basin and its logarithmic critical point, not the source's positive-equilibrium Turing criterion.

## Limitations
The initial data must lie in a sufficiently small parameter-dependent open sector; no explicit optimal wedge boundary, global basin partition, effects of spatial diffusion, or stochastic finite-population interpretation is claimed. Existence of a stable positive equilibrium is proved only for the exact witness parameters and the indicated \(\alpha\). At \(\alpha>c\) the leading prey amplitude depends on the initial condition. This is a mathematical finding with self-review only, and its priority remains subject to full specialist literature inspection.

## References
1. Y. Ye and J. Zhou, *Pattern formation in a predator-prey model with Allee effect and hyperbolic mortality on networked and non-networked environments*, arXiv:2306.11818 (first public version 2023-06-20), https://arxiv.org/abs/2306.11818 , https://arxiv.org/html/2306.11818 .
2. H. Liu et al., *Pattern Formation in a Reaction-Diffusion Predator-Prey Model with Weak Allee Effect and Delay*, Complexity (2019), Article 6282958, https://doi.org/10.1155/2019/6282958 .
3. H. Liu et al., *Turing instability and pattern induced by weak Allee effect and prey harvesting in a predator-prey model*, Advances in Continuous and Discrete Models (2026), https://doi.org/10.1186/s13662-025-04046-z .
