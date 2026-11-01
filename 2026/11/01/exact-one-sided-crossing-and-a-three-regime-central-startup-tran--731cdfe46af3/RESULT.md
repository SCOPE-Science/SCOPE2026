# Exact one-sided crossing and a three-regime central startup transition in regular polygonal oscillators

## Finding

For a regular \(N\)-gon in the piecewise-affine oscillator of Kai (2026), the forward-mode one-sector map is **exactly solvable** using the principal Lambert function. Its complete transverse section domain is \(-1<s<1/C\), it contracts every nonzero section displacement, and its one-step passage near the singular polygon center undergoes a **sharp linear / square-root / finite-ejection transition**. The transition is controlled by \(E=\lambda L^2/(2\omega)-\mu\Delta/\omega\) and occurs at \(E=1\), even though the limiting polygon's period and local Floquet multiplier are insensitive to \(\mu\).

Use counterclockwise vertices \(p_j=R(\cos(2\pi j/N),\sin(2\pi j/N))\), with cyclic indices, \(N\ge3\) and \(R>0\). Write \(d_j=p_{j+1}-p_j\), \(n_j=(d_{j,2},-d_{j,1})\), \(L^2=|d_j|^2=4R^2\sin^2(\pi/N)\), and \(\Delta=\det(p_j,p_{j+1})=R^2\sin(2\pi/N)>0\). In the open wedge between consecutive positive vertex rays, prescribe the affine field
\[
\dot x=(\omega-\mu V_j(x))d_j-\lambda V_j(x)n_j,
\qquad V_j(x)=n_j\cdot x-\Delta,
\]
with uniform \(\omega>0,\lambda>0,\mu\ge0\). The field is exactly the corresponding mode of the construction in Kai (2026), equation (9).

Define dimensionless numbers
\[
a=\frac{\lambda L^2}{\omega}>0,\qquad b=\frac{\mu\Delta}{\omega}\ge0,\qquad C=\frac a2+b>0,\qquad E=\frac a2-b,\qquad C+E=a.
\]
For a point \((1+s)p_j\) on the incoming vertex ray, select the **one-sided forward mode** \(j\); do not assume a unique global boundary solution if the two adjacent affine fields point into different sectors. For each \(-1<s<1/C\), this one-sided orbit immediately enters the open wedge, crosses the next vertex ray exactly once at \((1+F(s))p_{j+1}\), and does so transversely. The exact crossing law and time are
\[
\boxed{\ \log\!\left|\frac{s}{F(s)}\right|=a+Cs+EF(s),\qquad
\tau(s)=\frac1\omega\left(1+\frac{Cs+EF(s)}a\right)>0\ },
\]
where \(F(0)=0\) and \(\tau(0)=1/\omega\). More explicitly,
\[
\boxed{\ F(s)=
\begin{cases}
E^{-1}W_0\bigl(E s\exp(-a-Cs)\bigr),&E\ne0,\\
s\exp(-a-Cs),&E=0,
\end{cases}\ }
\]
with \(W_0\) the principal real Lambert branch. On the entire open domain, \(F\) is strictly increasing and
\[
F'(s)=\frac{F(s)}s\frac{1-Cs}{1+EF(s)}>0\quad(s\ne0),\qquad F'(0)=\exp(-a),
\]
while \(F(s)\) has the sign of \(s\) and \(0<|F(s)|<|s|\) for \(s\ne0\). Consequently, with successive forward-mode sector choices, every such initial section point undergoes infinitely many unambiguous transversal subsequent vertex-ray crossings and its section displacements converge to zero. The period of the target polygonal orbit is \(N/\omega\), and its transverse full-revolution multiplier is \(\exp(-Na)\). For \(s>1/C\), the initial \(j\)-mode field points outside the intended wedge, so \(1/C\) is the sharp *strict initial-entry* cutoff; at equality the initial contact is tangent. These one-sided and section statements make no claim about globally unique solutions on switching rays or about a full-plane attraction basin.

The **central startup trichotomy** is for \(u=1+s\downarrow0\), i.e. ray states tending to the origin but never equal to it, and \(v(u)=1+F(-1+u)\). For the crossing radius and flight time, the three exact alternatives are:
\[
\begin{array}{c|c|c}
\text{Condition}&\text{Next radius }v(u)&\text{Flight time }\tau(-1+u)\\\hline
E<1&\dfrac{1+C}{1-E}u+O(u^2)&\dfrac{u}{\omega(1-E)}+O(u^2)\\[5pt]
E=1&\sqrt{2a\,u}+O(u)&\dfrac{\sqrt{2a\,u}}{a\omega}+O(u)\\[5pt]
E>1&v_*(E)+O(u)&\dfrac{E v_*(E)}{a\omega}+O(u)
\end{array}
\]
Here \(v_*(E)\in(0,1)\) is the strictly positive solution of \(-\log(1-v_*)=Ev_*\), equivalently
\[
\boxed{\quad v_*(E)=1+\frac1E W_0(-E\exp(-E))>0,\qquad E>1.\quad}
\]
The finite-ejection case represents the **selected one-sided forward-mode passage**, not a uniquely defined trajectory starting at the origin itself.

For a concrete design comparison, take a square of circumradius one and \(\omega=1,\lambda=3/2\). Then \(a=3\) and \(E=3/2-\mu\). The choices \(\mu=0,1/2,1\) give, respectively, finite-ejection radius \(v_*(3/2)=0.5828116438658\ldots\), critical square-root startup \(v(u)\sim\sqrt{6u}\), and linear startup \(v(u)\sim7u\); all have the same target-cycle period \(4\) and multiplier \(\exp(-12)\).

## Assumptions and scope

Fix arbitrary \(N\in\{3,4,5,\ldots\}\), \(R,\omega,\lambda>0\), and \(\mu\ge0\). The mode equations apply in an open planar wedge bounded by the positive rays through \(p_j\) and \(p_{j+1}\); on a boundary, the one-sided mode is part of the data. Section radius is \(1+s>0\), and the first sector must be entered strictly in positive time, giving \(-1<s<1/C\). Transverse continuation through later switching rays is well defined. The origin, negative radial coordinates, other switching conventions, and arbitrary initial points in the plane are excluded from the section conclusion. In particular, if the incoming boundary is repelling for a particular parameter regime, the two-sided hybrid initial-value problem may not be unique there; no uniqueness assertion is made for that problem.

The singular limits as \(u\downarrow0\) have constants fixed while \(u\) varies. All big-O statements refer to this fixed-parameter limit, not uniform estimates as \(E\to1\). The eigenvalue statement is the transverse derivative of the full vertex-ray Poincaré map at the polygon orbit; it is not a claim about a global linearization away from that orbit.

## Proof

**Step 1: Exact affine flow.** In each wedge, \(d_j\cdot n_j=0\), \(|d_j|^2=|n_j|^2=L^2\), and \(n_j\cdot p_j=\Delta\). The mode equation immediately yields \(\dot V_j=-\lambda L^2 V_j\). Introduce barycentric coordinates \(x=\alpha(t)p_j+\beta(t)p_{j+1}\) and dimensionless time \(z=\omega t\). For the prescribed initial point \(x(0)=(1+s)p_j\), direct integration gives
\[
\boxed{\quad\beta(z)=z-\frac Ca s(1-\exp(-az)),\qquad
\alpha(z)=1-z+\frac Ca s+\frac Ea s\exp(-az).\quad}
\]
The identities follow either by differentiating or by writing \(x=p_j+\xi d_j+(V_j/L^2)n_j\), using \(V_j(0)=s\Delta\) and \(\xi(0)=-s/2\), and solving \(\dot\xi=\omega-\mu V_j\). In particular, \(\alpha(0)=1+s>0\) and \(\beta(0)=0\).

**Step 2: Exactly one transverse first crossing.** For \(-1<s<1/C\),
\[
\frac{d\beta}{dz}=1-Cs\exp(-az)>0
\]
for every \(z\ge0\); thus \(\beta(z)>0\) whenever \(z>0\). Also
\[
\frac{d\alpha}{dz}=-1-Es\exp(-az),\qquad
\frac{d^2\alpha}{dz^2}=aEs\exp(-az).
\]
Its derivative has at most one zero. Since \(\alpha(0)>0\) and \(\alpha(z)\to-\infty\), \(\alpha\) has precisely one positive zero \(z_*\), at which \(d\alpha/dz<0\). Before that zero both barycentric coordinates are positive, hence the affine orbit stays in the intended open wedge. At \(z_*\), it crosses the next ray transversely and \(\beta(z_*)=1+s'\) with \(s'=s\exp(-az_*)\). Thus \(s'>-1\) and \(1+Es'>0\), \(s'\) has the sign of \(s\), and \(0<|s'|<|s|\) if \(s\ne0\). A later initial ray displacement is again in \((-1,1/C)\), so this argument iterates indefinitely. The displacement magnitudes decrease, and a positive limiting magnitude would imply a positive limiting traversal time bound by the explicit crossing equation; equivalently, continuity of the increasing section map and the absence of a nonzero fixed point force the limit to zero.

**Step 3: Crossing law and principal branch.** The equation \(\alpha(z_*)=0\) reads \(az_*=a+Cs+Es'\); meanwhile \(s'=s\exp(-az_*)\). Elimination gives the boxed logarithmic relation and the time formula. Rearrangement is \(Es'\exp(Es')=Es\exp(-a-Cs)\). The actual crossing satisfies \(1+Es'>0\), so if \(E>0\) and \(s<0\) it lies on the real branch \(Es'>-1\). The unique real solution with this inequality is the principal Lambert branch; when \(E\le0\) the same branch is the continuous solution chosen by the proved crossing. Implicit differentiation gives the derivative formula, extended continuously at \(s=0\). Strict positivity follows from \(s'/s>0\), \(1-Cs>0\) and \(1+Es'>0\). At \(s=0\) the crossing is \(z_*=1\), yielding \(F'(0)=\exp(-a)\). The full revolution consists of \(N\) identical rotated maps, hence its derivative is \(\exp(-Na)\); the segment travel time on the cycle is \(1/\omega\). If \(s>1/C\), the initial derivative of \(\beta\) is negative, so the purported forward-mode itinerary immediately exits the prescribed wedge. At \(s=1/C\), that derivative is zero and its second derivative is positive. These are sharp strict-entry assertions only.

**Step 4: Selection at the singular center.** Put \(s=-1+u\), \(s'=-1+v\) with \(u,v>0\). The first crossing equation becomes
\[
\boxed{\quad \log(1-u)-Cu=\log(1-v)+Ev.\quad}
\]
The left-hand side is \(-(1+C)u+O(u^2)\). The right-hand side is \(-(1-E)v-v^2/2+O(v^3)\). If \(E<1\), the implicit function theorem at \(v=0\) yields the stated linear coefficient. If \(E=1\), quadratic cancellation yields \(v=\sqrt{2(1+C)u}+O(u)=\sqrt{2au}+O(u)\). If \(E>1\), the function \(\log(1-v)+Ev\) increases initially and has exactly one further zero \(v_*(E)\in(0,1)\) on its strictly decreasing branch. The actual exit satisfies \(1+Es'>0\), which is equivalent to \(v>1-1/E\); hence the outgoing root, not the zero-time root \(v=0\), is selected. Its simple zero gives \(v=v_*(E)+O(u)\). The principal Lambert identity yields the explicit expression. Finally, the exact time identity is \(a\omega\tau=Cu+Ev\), and substitution gives all three flight-time laws. In the square example, the definitions give \(L^2=2,\Delta=1,a=3\), and the stated substitutions follow. This completes the proof.

## Verification

The standalone file `verify.py` evaluates the one-sector first-exit problem both from the principal Lambert formula and by independently integrating the original two-dimensional affine differential equation, locating the crossing with a directional event function. The executed checker completed 864 parameter/section cases with maximum observed absolute position or time discrepancy less than \(4.8\cdot10^{-12}\), as well as central-limit and implicit-identity checks. The tests use four polygon sizes and varying radii, positive contraction and rotation parameters, and nonnegative tangential gains. These finite numerical checks are corroboration; **the parameter-uniform results are established by the preceding analytic proof**.

For reproducibility, run `python verify.py` in an environment containing NumPy and SciPy. The script includes its selected parameters and tolerances. It does not rely on any unbundled research artifacts. No external independent scientific validation has been performed.

## Relationship to prior work

Kai (2026), especially §§3.1–3.3 and equations (9), (13), (27), and (29), supplies the underlying piecewise-affine construction, exponential decay of the edge-normal displacement, and the prescribed polygonal cycle period. Those are **not new claims here**. The analysis above additionally integrates the tangential motion into a complete **one-sided vertex-ray first-exit map**, proves its entire strict-entry domain, and identifies a sharp three-way singular-origin transition whose regime depends on the tangential design parameter. The full text of Kai (2026) was inspected; its local invariant-neighborhood stability and transient-design statements do not supply the claimed exact section map, Lambert branch selection, or three-regime startup classification.

Earlier piecewise-affine limit-cycle synthesis papers by Kai and Masuda (2012) and Kai (2013) are relevant background. Their available bibliographic material and abstracts were inspected, but a full comparison to the inaccessible 2012 and 2019 papers remains a **historical priority limitation**. They cannot be treated as having been ruled out by title or abstract search alone. A comparison of nearby published mathematical results on other piecewise-affine and relay oscillators likewise identified different flow laws and different periodic structures, not a statement entailing this specific regular-polygon theorem. No general novelty or priority certification is asserted.

## Limitations

The conclusion is a **one-sided mode-selected** first-exit and sectional continuation theorem. For states on switching rays, especially arbitrarily close to the origin in the finite-ejection regime, adjacent vector fields can point into distinct sectors; an unqualified global uniqueness or basin statement would be false or unsupported. The origin itself is excluded. The theorem assumes regular geometry, uniform mode parameters, strictly positive \(\omega,\lambda\), and \(\mu\ge0\). The sharp outer cutoff concerns strict initial entry into the prescribed forward wedge, not impossibility of every other hybrid path. The singular asymptotics are not claimed uniformly across the threshold \(E=1\). Related older primary papers remain partially inaccessible and independent review is outstanding.

## References

1. T. Kai, *Piecewise affine oscillators with polygonal limit cycles*, International Journal of Dynamics and Control **14**, article 392 (first public 8 October 2026), DOI: 10.1007/s40435-026-02340-6. Full open-access source: https://doi.org/10.1007/s40435-026-02340-6.
2. T. Kai and R. Masuda, *Limit cycle synthesis of multi-modal and 2-dimensional piecewise affine systems*, Mathematical and Computer Modelling **55** (2012), 505–516, DOI: 10.1016/j.mcm.2011.08.028 (abstract and bibliographic record inspected; full text unavailable).
3. T. Kai, *Limit Cycle Generation for Multi-Modal and 2-Dimensional Piecewise Affine Control Systems*, International Journal of Advanced Computer Science and Applications **4**(9) (2013), https://thesai.org/Downloads/IJACSA_Volume4No9.pdf (relevant indexed metadata and abstract examined).
4. T. Kai, S. Chiku and K. Maehara, *Derivation and mathematical analysis of piecewise affine oscillators with desired polygonal limit cycles*, European Control Conference (2019), pp. 2632–2637, DOI: 10.23919/ECC.2019.8795666 (abstract examined; full text unavailable).
