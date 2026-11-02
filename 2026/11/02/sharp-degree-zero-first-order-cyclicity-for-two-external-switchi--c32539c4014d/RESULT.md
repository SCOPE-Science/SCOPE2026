# Sharp degree-zero first-order cyclicity for two external switching circles

## Finding
Consider the piecewise holomorphic perturbation of the planar linear center
\[
\dot z=iz+\varepsilon c_j,
\]
with complex constants \(c_-\), \(c_+\), \(c_0\) in the disks \(D_-:=\{|z+2|<1\}\), \(D_+:=\{|z-2|<\sqrt2\}\), and their common exterior, respectively. The disks are disjoint. Put
\[
A=-\operatorname{Re}(c_--c_0),\qquad B=\operatorname{Re}(c_+-c_0),\qquad
\eta_* = \sqrt{\frac{47-\sqrt{161}}{64}}.
\]
For every unperturbed circle \(|z|=r\) that crosses one or both disk boundaries transversely, its first-order radial return displacement is \(\varepsilon M(r)+O(\varepsilon^2)\). Across **all three transversal crossing annuli**, \(M\) has at most two simple zeros. More precisely, if \(A B<0\), then \(M\) has exactly two simple zeros when \(0<-B/A<\eta_*\), one double zero when \(-B/A=\eta_*\), and no zeros when \(-B/A>\eta_*\). If \(AB\ge0\), it has no simple zeros. When \(A=B=0\), \(M\) vanishes identically and first-order theory is inconclusive.

The bound two is attained using \(c_0=0\), \(c_-=-1\), \(c_+=-1/2\). Its two simple Melnikov zeros occur at the exact radii
\[
r_1=\frac{2}{\sqrt3},\qquad r_2=2\sqrt2.
\]
For every sufficiently small positive \(\varepsilon\), there are two corresponding hyperbolic crossing limit cycles, the inner one repelling and the outer one attracting, tending to those two circles as \(\varepsilon\to0^+\). This is a **sharp first-order bifurcation count**, not a global maximum for all possible cycles of the perturbed system.

## Assumptions and scope
We use the conventional crossing solution of a planar piecewise-smooth vector field. Every unperturbed trajectory of \(\dot z=iz\) is the circle \(|z|=r\), traversed counterclockwise with unit angular speed. Its intersections with each disk boundary are transverse except at the tangencies \(r=1\), \(r=3\), \(r=2-\sqrt2\), and \(r=2+\sqrt2\). The three annuli of transverse crossing trajectories are
\[
(2-\sqrt2,1),\qquad(1,3),\qquad(3,2+\sqrt2).
\]
The first and last cross only \(D_+\); the middle annulus crosses both disks. The parameter \(\varepsilon\) is sufficiently small for the relevant transversal return maps to be defined smoothly on compact subannuli; no claim is made for grazing orbits, sliding orbits, or higher-order cycles hidden when \(M\equiv0\).

## Proof
Parameterize an unperturbed circle as \(z=r e^{i\theta}\). For any constant perturbation \(c\), the radial variation at first order is \(\operatorname{Re}(e^{-i\theta}c)\), while \(\dot\theta=1+O(\varepsilon)\). Integrating over a full revolution, the background constant \(c_0\) contributes zero. Thus only the differences from \(c_0\) inside the disks matter. The angular arc inside \(D_+\) is centered at \(0\) and has half-angle \(\phi_+(r)\), where \(\cos\phi_+=(r^2+2)/(4r)\). The angular arc inside \(D_-\) is centered at \(\pi\) and has half-angle \(\phi_-(r)\), where \(\cos\phi_-=(r^2+3)/(4r)\). The sine components of \(c_j\) cancel on each symmetric arc. Therefore, for \(1<r<3\),
\[
M(r)=2[A f_-(r)+B f_+(r)],\quad
f_-(r)=\sqrt{1-\frac{(r^2+3)^2}{16r^2}},\quad
f_+(r)=\sqrt{1-\frac{(r^2+2)^2}{16r^2}}.
\]
On either single-disk crossing annulus, \(M(r)=2Bf_+(r)\), with \(f_+(r)>0\); it has no simple zero there. The two functions in the shared annulus are strictly positive. Setting \(t=r^2\) gives
\[
\left(\frac{f_-(r)}{f_+(r)}\right)^2
=\frac{p(t)}{q(t)},\qquad
p(t)=-t^2+10t-9=(t-1)(9-t),\quad
q(t)=-t^2+12t-4.
\]
For \(1<t<9\), both polynomials are positive. Their quotient has derivative
\[
\frac{d}{dt}\frac{p(t)}{q(t)}
=\frac{-2(t^2+5t-34)}{q(t)^2}.
\]
It rises strictly from zero to a single maximum at \(t_*=(\sqrt{161}-5)/2\) and decreases strictly to zero. Substitution gives \(p(t_*)/q(t_*)=(47-\sqrt{161})/64\). Consequently a horizontal level \(-B/A\) intersects \(f_-/f_+\) twice, tangentially once, or never, according as it belongs to \((0,\eta_*)\), equals \(\eta_*\), or exceeds \(\eta_*\), provided \(AB<0\). Other coefficients give no simple roots; the completely degenerate case gives \(M\equiv0\). This proves the sharp first-order count.

For the explicit coefficients \(A=1\), \(B=-1/2\), the zero equation is \(p(t)=q(t)/4\). Its exact factorization is
\[
p(t)-\frac{q(t)}4=-\frac{(t-8)(3t-4)}4,
\]
so the two radii are exactly those stated. Direct differentiation, using that \(f_-/f_+=1/2\) at each zero, yields
\[
M'(r_1)=\frac{15}{2\sqrt{23}}>0,\qquad
M'(r_2)=-\frac{5}{2\sqrt7}<0.
\]
The return map is \(P_\varepsilon(r)=r+\varepsilon M(r)+O(\varepsilon^2)\) in \(C^1\) near these transverse crossings. The implicit function theorem produces one hyperbolic fixed point close to each simple zero, with multiplier \(1+\varepsilon M'(r_j)+O(\varepsilon^2)\). Thus for positive \(\varepsilon\) the inner cycle is repelling and the outer cycle attracting.

## Verification
The accompanying pure-Python checker, `verify.py`, reconstructs the polynomial identities with exact rational coefficients, verifies the two exact roots and derivative signs, and compares independent numerical angular arc quadrature against \(M(r)\) on test circles. Run with `python3 verify.py` from the directory containing the files. The exact symbolic identities support the proof; numerical integration is a diagnostic only. The analytical zero count uses the sign of a quadratic over the entire open interval, not finite enumeration. The general persistence step is the standard implicit-function theorem for smooth transverse crossing return maps.

## Relationship to prior work
Silva and da Silva, *Bifurcation of limit cycles in piecewise holomorphic systems separated by two external circles* (arXiv:2610.08725, first public October 6, 2026), introduce these precise disks in their Theorem B and obtain many small-amplitude limit cycles using fourth-degree perturbations. Their Melnikov framework justifies the return-map calculation, but their stated fourth-degree lower bounds do not give the complete first-order zero count, exact threshold, or stability pairing for degree-zero perturbations. The present result isolates the lowest-degree polynomial stratum and determines its sharp first-order bifurcation count.

Silva and da Silva, *On the Piecewise Holomorphic Systems with Three Zones* (arXiv:2509.01377), study parallel lines and **tangent**, rather than separated, circular interfaces, with different polynomial families. Earlier results for **concentric** circles and for a **single** circular interface likewise do not imply a bound for the disjoint, externally separated disks here. General Melnikov bifurcation theory is used rather than claimed to be new.

## Limitations
The upper bound counts simple zeros of the **first-order** return displacement on transversal crossing annuli. It is not an upper bound on all limit cycles at fixed nonzero \(\varepsilon\). A double zero at the threshold may split at higher orders; identically zero first-order displacement, or cycles near tangent radii, require separate analysis. Other parameter choices may have cycles not perturbing from the specified annuli. Historical priority remains subject to independent specialist examination, particularly for previous general treatments of piecewise circular interfaces.

## References
1. C. V. das Neves Silva and P. R. da Silva, *Bifurcation of limit cycles in piecewise holomorphic systems separated by two external circles*, arXiv:2610.08725 (2026), https://arxiv.org/abs/2610.08725.
2. C. V. das Neves Silva and P. R. da Silva, *On the Piecewise Holomorphic Systems with Three Zones*, arXiv:2509.01377 (2025), https://arxiv.org/abs/2509.01377.
3. G. Rondón, P. R. da Silva and J. Llibre, *Limit cycles in piecewise smooth systems with circular switching manifold*, arXiv:2604.26061 (2026), https://arxiv.org/abs/2604.26061.
4. C. Buzzi, C. Pessoa and J. Torregrosa, *Piecewise linear perturbations of a linear center*, Discrete Contin. Dyn. Syst. 33 (2013), 3915–3936, DOI 10.3934/dcds.2013.33.3915.
