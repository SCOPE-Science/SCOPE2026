# Global selection and sharp critical relaxation in a neutral-consensus model

## Finding
For the exact two-dimensional, deterministic, three-stance consensus flow of Sontag–Hoffmann–Rogers–Yates, specified below, every strictly interior initial condition converges to an equilibrium. The entire basin boundary is the equal-opinion diagonal in the polarized regime, and at the symmetry-breaking threshold the squared opinion imbalance has a **universal, initial-condition-independent inverse-time amplitude**.

Put \(w_0=(\sqrt{1+\gamma}-1)/(\sqrt{1+\gamma}+1)\). For \(0<\alpha<w_0\), all initial states with \(x(0)>y(0)\) tend to one positive-polarization equilibrium, all with \(x(0)<y(0)\) tend to its reflected counterpart, and only \(x(0)=y(0)\) tends to the unpolarized saddle. For \(\alpha\geq w_0\), every interior initial state converges to the sole unpolarized equilibrium. At the exact threshold \(\alpha=w_0\), for every initially unequal pair of opinions,
\[
\lim_{t\to\infty}t\,[x(t)-y(t)]^2=\frac{B}{2\rho c},\qquad c=\frac{\beta\gamma}{2},\quad B=2c(1-\alpha)+2\beta+\rho(1-\alpha).
\]
In particular, \(\beta=\rho=1\), \(\gamma=8\) and \(\alpha=1/2\) give the exact critical amplitude \(13/16\). Symmetric initial conditions have identically zero imbalance and are deliberately excluded from the algebraic-amplitude assertion.

## Assumptions and scope
Let \(\alpha,\beta,\gamma,\rho>0\) be fixed and let \(x(0),y(0),w(0)>0\) with \(x+y+w=1\). Consider the *noise-free*, infinite-population ODE
\[
\dot x=\beta(w-\gamma xy)+\rho x(w-\alpha),\qquad
\dot y=\beta(w-\gamma xy)+\rho y(w-\alpha),\qquad w=1-x-y.
\]
There is no direct stance-reversal term (the source's parameter \(\delta\) is zero). All conclusions quantify over every strictly interior initial condition and the full positive parameter range. The simplex is forward invariant: at \(x=0\) or \(y=0\), the missing stance has nonnegative derivative \(\beta w\); at \(w=0\), \(\dot w=2\beta\gamma xy+\rho\alpha(x+y)>0\). Smoothness and compactness yield global forward solutions; positivity holds at every finite time for strictly interior starts.

Define \(z=x-y\), \(q=z^2\), \(c=\beta\gamma/2\), and
\[
G(w)=c(1-w)^2-2\beta w-\rho(1-w)(w-\alpha).
\]
The reduced equations, obtained **exactly rather than by slow-manifold approximation**, are
\[
\dot q=2\rho q(w-\alpha),\qquad \dot w=G(w)-cq.
\]
Since \(G(0)>0\), \(G(1)<0\), and the leading quadratic coefficient is \(c+\rho>0\), there is exactly one root \(w_s\in(0,1)\); the other root lies above one. The unpolarized equilibrium is \(E_s=((1-w_s)/2,(1-w_s)/2)\). If \(\alpha<w_0\), there are in addition the two polarized equilibria
\[
E_\pm:\quad w=\alpha,\quad z=\pm\sqrt{q_*},\qquad
q_*=(1-\alpha)^2-\frac{4\alpha}{\gamma}>0,
\]
with \(x=(1-\alpha+z)/2\) and \(y=(1-\alpha-z)/2\). No additional equilibria occur in the simplex.

## Proof
**1. Unique threshold and exact invariant reductions.** Subtracting the two population equations gives \(\dot z=\rho z(w-\alpha)\), which preserves the sign of any nonzero imbalance. Substituting \(x=((1-w)+z)/2\), \(y=((1-w)-z)/2\) gives the displayed exact \((q,w)\) flow. At \(w=\alpha\), the equilibrium relation becomes \(q=G(\alpha)/c=(1-\alpha)^2-4\alpha/\gamma\). The equation \(q_*=0\) has one solution in \((0,1)\), namely \(w_0\). For \(\alpha<w_0\), \(G(\alpha)=cq_*>0\), so \(w_s>\alpha\); for \(\alpha=w_0\), \(w_s=\alpha\); for \(w_0<\alpha<1\), \(G(\alpha)<0\), so \(w_s<\alpha\). The latter inequality also holds for \(\alpha\ge1\) because \(w_s<1\).

**2. Global polarized basins.** Suppose \(0<\alpha<w_0\), hence \(q_*>0\). For any \(q>0\) define
\[
V(q,w)=\frac{c}{2\rho}\left[q-q_*-q_*\log\left(\frac q{q_*}\right)\right]+\frac12(w-\alpha)^2.
\]
The bracket is nonnegative and tends to infinity as \(q\downarrow0\). Its exact orbital derivative is
\[
\dot V=-(w-\alpha)^2\left[c(2-w-\alpha)+2\beta+\rho(1-w)\right]\le0.
\]
The factor in brackets is strictly positive on the closed physical simplex because \(\alpha<1\). Any initial \(q>0\) lies in a compact invariant sublevel of \(V\) bounded away from \(q=0\). The largest invariant subset of \(\{\dot V=0\}\) there is \(\{(q,w)=(q_*,\alpha)\}\): indeed on \(w=\alpha\) one has \(\dot w=c(q_*-q)\). LaSalle's invariance principle therefore gives \(q(t)\to q_*\), \(w(t)\to\alpha\). Preservation of the sign of \(z\) selects exactly \(E_+\) or \(E_-\). For \(z(0)=0\), one has \(z(t)\equiv0\) and \(\dot w=G(w)\), so \(w\to w_s\). Thus the diagonal is the full interior basin boundary, and there are no nonstationary compact recurrent states in the interior.

**3. Global unpolarized selection, including criticality.** Suppose \(\alpha\ge w_0\), so \(w_s\le\alpha\). Use
\[
W(q,w)=\frac{c}{2\rho}q+\frac12(w-w_s)^2.
\]
Its exact derivative is
\[
\dot W=(w-w_s)G(w)+cq(w_s-\alpha)\le0.
\]
Because \(G\) has a single zero in \([0,1]\), \((w-w_s)G(w)<0\) whenever \(w\ne w_s\). If \(w_s<\alpha\), the only vanishing point of \(\dot W\) is \((q,w)=(0,w_s)\). If \(w_s=\alpha\), the zero set is \(w=\alpha\), but on this line \(\dot w=-cq\), so its largest invariant subset again is \((q,w)=(0,\alpha)\). Compactness and LaSalle yield \((q(t),w(t))\to(0,w_s)\) for every strictly interior state.

**4. Exact critical decay coefficient.** Let \(\alpha=w_0\) and assume \(z(0)\ne0\), so \(q(t)>0\) at every finite time. Put \(u=w-\alpha\) and \(B=2c(1-\alpha)+2\beta+\rho(1-\alpha)>0\). Since \(G(\alpha)=0\), the exact equations become
\[
\dot q=2\rho qu,\qquad \dot u=-Bu+(c+\rho)u^2-cq.
\]
Part 3 proves \(q,u\to0\). Eventually \(u<0\): if \(u\ge0\) indefinitely then \(q\) is nondecreasing, contradicting \(q\to0\); at any zero of \(u\), \(\dot u=-cq<0\), so an established negative sign cannot revert. For all sufficiently large times define \(s=-u/q>0\). Differentiation gives the **exact** scalar equation
\[
\dot s=c-[B+(c-\rho)qs]s.
\]
Here \(qs=-u\to0\), so the bracket tends to \(B>0\). Comparison with scalar linear equations having coefficients \(B\pm\varepsilon\) first bounds \(s\) and then forces \(s(t)\to c/B\). Consequently
\[
\frac{d}{dt}\left(\frac1q\right)=2\rho s(t)\longrightarrow\frac{2\rho c}{B}.
\]
Integrating and dividing by \(t\) gives \(1/(tq(t))\to2\rho c/B\), which is equivalent to the claimed universal amplitude. The displayed example follows by \(c=4\), \(B=13/2\). This argument uses the exact planar flow and does not infer an infinite-time law from a finite simulation or a formal center-manifold truncation.

## Verification
The accompanying executable `verification/check_consensus.py` checks seven symbolic identities (including both Lyapunov derivatives, the exact reduced ODE and the critical ratio equation), two exact-rational examples, and nine deterministic trajectory comparisons in the polarized, critical and unpolarized regimes. The tests run with Python 3, SymPy and SciPy. Analytical Parts 1–4, not the finite numerical examples, justify the universal and infinite-time assertions.

## Relationship to prior work
Sontag, Hoffmann, Rogers and Yates (2026) formulate precisely this deterministic drift as their noise-free, \(\delta=0\) case of Methods equations (7)–(9), derive the associated line and hyperbola and classify local consensus configurations. Their main paper studies stochastic noise, heteroclinic switching, and fast/slow reductions; it states that supplementary Section SI.1 contains a full equilibrium/phase-portrait classification. Those fixed-point and local-geometry insights are **prior**, not claimed as new. The distinct assertion here is an explicit global, all-timescale basin proof by two closed-form Lyapunov functions, joined to a sharp **threshold amplitude valid on every asymmetric full-system trajectory**. Unlike a projected one-variable approximation, no separation \(\beta\gg\rho\) or \(\rho\gg\beta\) is required. Svenkeson and Swami (2015) study a different three-stance indecision model; their general qualitative observation of consensus with neutral actors does not furnish the coefficient for the specific 2026 flow.

## Limitations
This is an exact deterministic, homogeneous, infinite-population result, not a theorem about finite-size noise, switching times, spatial networks, direct \(X\leftrightarrow Y\) stance changes, or human experimental outcomes. The source's 18.4-MB supplementary file could not be inspected through the available lawful browser route (access gate); consequently an equivalent global portrait inside SI.1 remains a residual originality risk. The novel critical prefactor has not been independently audited. Numerical integrations cannot replace the universal analytical argument. No conclusion is claimed for parameter values outside the stated strictly positive domain or for initially unequal trajectories on the exactly symmetric diagonal.

## References
1. A. Sontag, J. A. Hoffmann, T. Rogers, C. A. Yates, “Consensus Formation and Change are Enhanced by Neutrality,” *Advanced Science*, first online 22 March 2026, DOI: 10.1002/advs.202512301. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13325515/ .
2. E. Svenkeson, A. Swami, “Reaching Consensus by Allowing Moments of Indecision,” *Scientific Reports* **5**, 14839 (2015), https://www.nature.com/articles/srep14839 .
3. J. Reyn, *Phase Portraits of Planar Quadratic Systems*, Springer (2007). General planar quadratic-flow background; no model-specific threshold amplitude is attributed to this reference.
