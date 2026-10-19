# Sharp logarithmic clock and resonance accumulation at an integrable Hopf–Langford separatrix

## Finding
Consider the Hopf–Langford vector field
\[
\begin{aligned}
\dot x&=(\mu-\alpha+z)x-\beta y,\\
\dot y&=\beta x+(\mu-\alpha+z)y,\\
\dot z&=\mu z-\gamma(x^2+y^2+z^2).
\end{aligned}
\]
Fix any \(\gamma>0\), \(d>0\), and \(\beta\ne0\), and set \(\mu=2\gamma d\) and \(\alpha=(2\gamma+1)d\). Put
\[
 c=\gamma d,\quad p=1+2/\gamma,\quad Y=((\gamma+1)/\gamma)^{\gamma/2},
 \quad E_*=-c^2/[2(\gamma+1)],\quad C_\gamma=2^{1+2\gamma}c^2Y^2.
\]
Each \(E\in(E_*,0)\) labels a positive-radius oscillation with minimal radial period \(T(E)\). At the separatrix, its **physical-time period has an exact finite constant**:
\[
\boxed{T(E)=c^{-1}\log(C_\gamma/(-E))+o(1)\qquad(E\uparrow0).}
\]
In particular this is not merely a statement of logarithmic divergence: its prefactor \(C_\gamma\) is explicit for every real \(\gamma>0\).

For all sufficiently large positive integers \(n\), some energy \(E_n\in(E_*,0)\) gives a closed orbit of the full three-dimensional flow which makes one radial oscillation and \(n\) angular turns, and every selection of these resonant energies obeys
\[
\boxed{E_n=-C_\gamma\exp(-2\pi cn/|\beta|)(1+o(1))\qquad(n\to\infty).}
\]
Thus phase-locked cycles accumulate exponentially, with a sharp constant, on the separating invariant heteroclinic surface. No assertion of one resonant energy per \(n\) is made. The period also has the strictly positive local twist
\[
 T(E)=\frac{2\pi}{d\sqrt{2\gamma}}
 \left[1+\frac{p(p+3)}{12(d\sqrt{2\gamma})^2}(E-E_*)
 +O((E-E_*)^2)\right]\quad(E\downarrow E_*).
\]

## Assumptions and scope
All parameters and times are real. The assumptions are exactly \(\gamma,d>0\), \(\beta\ne0\), \(\mu=2\gamma d\), and \(\alpha=(2\gamma+1)d\). Energies are measured in the transformed, explicitly normalized oscillator below, **not** the Euclidean norm of the original three-state system. The period refers to the minimal radial/amplitude oscillation; for a phase-locked solution it is also a period of the full flow (the angular winding is \(n\)). No claim concerns off-critical parameters, all possible periodic orbits, or dynamics on the axis.

## Proof
**1. Exact oscillator reduction.** On \(r=(x^2+y^2)^{1/2}>0\), with \(w=z-d\) and \(\theta=\arg(x+iy)\), the critical parameter equations become
\[
\dot r=rw,\qquad \dot w=-\gamma(r^2-d^2+w^2),\qquad\dot\theta=\beta.
\]
Write \(q=(r/d)^\gamma\) and \(c=\gamma d\). Differentiating twice gives the **exact**, not averaged, equation
\[
\ddot q+c^2(q^p-q)=0,\qquad p=1+2/\gamma.
\]
Its conserved energy is
\[
 E=\tfrac12\dot q^2+c^2\left(\frac{q^{p+1}}{p+1}-\frac{q^2}{2}\right).
\]
The positive stable equilibrium is \(q=1\), at energy \(E_*=-c^2/[2(\gamma+1)]\). The potential on the positive half-axis has just one nonzero zero, \(q=Y=((\gamma+1)/\gamma)^{\gamma/2}\), so each \(E\in(E_*,0)\) has two strictly positive simple turning points; these produce a periodic oval and, after adjoining \(\theta\), an invariant two-torus. No averaging approximation occurs here.

**2. Boundary geometry.** The zero-energy branch is, up to a time shift and angular phase,
\[
 r(t)=d\sqrt{(\gamma+1)/\gamma}\operatorname{sech}(dt),\quad
 z(t)=d-d\tanh(dt),\quad \theta(t)=\theta_0+\beta t.
\]
Substitution verifies both reduced equations. Its trajectory joins the axis equilibrium at \(z=2d\) to the one at \(z=0\) and lies on the invariant surface
\[
 \frac{\gamma}{\gamma+1}(x^2+y^2)+(z-d)^2=d^2.
\]
This construction makes explicit the boundary against which the negative-energy oscillations accumulate. The qualitative existence of an integrable center and related heteroclinic geometry is *not* asserted to be new.

**3. Exact quadrature.** With \(u=q/Y\), \(\nu=2/\gamma\) and \(\varepsilon=2(-E)/(c^2Y^2)\), the turning points \(0<u_-<u_+<1\) solve \(u^2(1-u^\nu)=\varepsilon\). Energy conservation gives
\[
 T(E)=\frac2c\int_{u_-}^{u_+}\frac{du}{\sqrt{u^2(1-u^\nu)-\varepsilon}}.
\]
This integral is finite for each \(E\in(E_*,0)\). To determine its constant at \(E\uparrow0\), split at a fixed small \(a>0\) and subsequently let \(a\downarrow0\). The lower integral equals
\[
 \log(2a/\sqrt\varepsilon)+O(a^\nu)+o_\varepsilon(1),
\]
by comparison with \(\int_{\sqrt\varepsilon}^{a}du/\sqrt{u^2-\varepsilon}\). The upper integral tends to
\[
 \int_a^1\frac{du}{u\sqrt{1-u^\nu}}
 =\log(1/a)+\frac{2\log2}{\nu}+O(a^\nu).
\]
The constant follows by the substitution \(v=u^\nu\) and the elementary integral
\[
 \int_0^1\frac{(1-v)^{-1/2}-1}{v}\,dv=2\log2.
\]
The square-root singularity at the moving upper turning point is integrable and contributes no additional constant; for instance substitute the fractional distance from the moving endpoint before dominated convergence. Taking \(\varepsilon\downarrow0\) and then \(a\downarrow0\),
\[
\frac{cT}2=\log(2/\sqrt\varepsilon)+\frac{2\log2}{\nu}+o(1).
\]
Since \(\varepsilon=2(-E)/(c^2Y^2)\) and \(\nu=2/\gamma\), simplification yields the displayed \(C_\gamma=2^{1+2\gamma}c^2Y^2\). The \(o(1)\) is for fixed \(\gamma,d>0\), not asserted uniform in these parameters.

**4. Local twist.** Write \(q=1+\xi\) in the oscillator equation. Let \(\omega_0=c\sqrt{p-1}=d\sqrt{2\gamma}\); the Taylor coefficients are \(a=\omega_0^2p/2\) for \(\xi^2\) and \(b=\omega_0^2p(p-2)/6\) for \(\xi^3\). The standard Poincaré–Lindstedt calculation (obtained by removing the fundamental harmonic at second order) gives
\[
 \frac{\omega}{\omega_0}=1+
 \left(\frac{3b}{8\omega_0^2}-\frac{5a^2}{12\omega_0^4}\right)A^2+O(A^3)
 =1-\frac{p(p+3)}{24}A^2+O(A^3).
\]
Here \(A\) is the leading harmonic amplitude. Since \(E-E_*=\omega_0^2A^2/2+O(A^3)\), and the center's period is analytic as a function of energy for this analytic potential near \(q=1\), the stated first-order energy expansion and squared-energy remainder follow. Its coefficient is strictly positive for all \(\gamma>0\).

**5. Resonant exponential law.** The period is continuous on \((E_*,0)\), tends to \(2\pi/\omega_0\) at the center and to \(+\infty\) at the separatrix. Hence its range contains all sufficiently large \(2\pi n/|\beta|\); select a solution \(E_n\) to the equation \(T(E_n)=2\pi n/|\beta|\). Because periods are bounded on every compact subset of \([E_*,0)\), necessarily \(E_n\to0^-\). Inserting these values into the sharp logarithmic law gives the displayed \(E_n\) formula. The rotation \(\dot\theta=\beta\) makes these actual closed solutions, not merely amplitude-periodic trajectories.

## Verification
The accompanying `verify.py` checks the exact hyperbolic-profile identities, the local frequency-coefficient simplification, and numerical near-separatrix quadratures at four distinct positive values of \(\gamma\). The analytical arguments above, rather than the finite numerical checks, justify the all-parameter assertions. Run `python verify.py` with SymPy and SciPy installed. For \(\gamma=1\), the constant reduces to \(C_1=16c^2\), agreeing with the familiar elementary elliptic-integral limit for the Duffing separatrix; this is a consistency check, not novelty.

## Relationship to prior work
Domingues (2026) studies an averaged torus-bifurcation prediction for this flow. Vassilev and Nikolov (2024) already establish the critical integrability condition and describe phase portraits, and prior generalized Hopf–Langford work provides invariant tori and heteroclinic invariant ellipsoids in related or specialized families. A previously available analysis of the same critical family also identifies a weighted-Dulac obstruction to isolated torus birth. Those qualitative results are **not** attributed here. The contribution assessed here is specifically the exact general-\(\gamma\) physical-period **finite logarithmic constant** and the resulting sharp **energy-spacing prefactor** for phase-locked periodic orbits, together with a quantified local period twist. A full-text comparison with two earlier integrability/heteroclinic papers was unavailable, so prior implicit coverage of the sharp clock cannot be ruled out.

## Limitations
This is a theorem about one integrable parameter locus with \(r>0\) and fixed positive \(\gamma,d\). It does not prove globally monotone period, uniqueness of each resonant energy, persistence under perturbations, uniformity at parameter endpoints, or existence/stability of nearby normally hyperbolic tori. The qualitative phase portrait, integrability and separatrix existence are established elsewhere; this statement does not purport to discover them. The earlier papers on Duffing reductions and invariant heteroclinic ellipsoids are a residual bibliographic priority risk because their complete texts were not available.

## References
- G. Domingues, *Torus Bifurcation in the Hopf-Langford type system through Averaging Theory*, arXiv:2609.18010v1 (first public version September 16, 2026), https://arxiv.org/abs/2609.18010.
- P. Vassilev and I. Nikolov, *First and Second Integrals of Hopf–Langford Type Systems* (public preprint November 11, 2024; subsequent journal version), consulted full open-access article.
- H. Zhong and H. Liang, *Invariant Tori and Heteroclinic Invariant Ellipsoids of a Generalized Hopf–Langford System*, *International Journal of Bifurcation and Chaos* (2023), DOI 10.1142/S0218127423501535; publisher preview inspected, full text unavailable.
- I. Nikolov and P. Vassilev, *Completely integrable dynamical systems of Hopf–Langford type*, *Communications in Nonlinear Science and Numerical Simulation* (2021), DOI 10.1016/j.cnsns.2020.105464; abstract inspected, full text unavailable.
