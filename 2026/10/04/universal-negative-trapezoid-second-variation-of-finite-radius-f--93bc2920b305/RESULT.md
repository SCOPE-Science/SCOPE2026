# Universal negative trapezoid second variation of finite-radius Funk–Santaló volume
## Finding
For \(R>0\), set \(\lambda=1-e^{-R}\in(0,1)\) and \(A=\operatorname{artanh}\lambda\). Consider the affine-normalized trapezoid family
\[
T_\delta=\operatorname{conv}\left\{(-1,-1),(1,-1),\left(\frac{1+\delta}{1-\delta},1\right),\left(-\frac{1+\delta}{1-\delta},1\right)\right\},\qquad -1<\delta<1.
\]
Every nondegenerate trapezoid is affinely equivalent to one such \(T_\delta\), with interchange of the two parallel bases sending \(\delta\) to \(-\delta\). Let the unique radius-\(R\) Funk–Santaló center be \((0,s_R(\delta))\), and define the center-minimized, normalization-free quantity
\[
\Phi_R(\delta)=\omega_2\operatorname{Vol}_{T_\delta}\!\left(B_{T_\delta}((0,s_R(\delta)),R)\right).
\]
Then
\[
s_R(\delta)=c_R\delta+O(\delta^3),\qquad c_R=\frac{(1+\lambda)A-\lambda}{2\lambda A},
\]
and
\[
\Phi_R''(0)=-\frac{4N_R}{A\lambda(1+\lambda)^2}<0,
\]
where
\[
N_R=A^2(\lambda^2+6\lambda+1)-2A\lambda(3\lambda+1)+\lambda^2.
\]
Thus the affine-parallelogram class is a strict local maximum of the optimally centered finite-radius Funk-ball volume along the full affine moduli of trapezoids, for every \(R>0\). Moreover \(c_R\to 1/2\) as \(R\downarrow0\) and \(c_R\to1\) as \(R\to\infty\).

## Assumptions and scope
The volume is Holmes–Thompson volume in the Funk geometry. The factor \(\omega_2\) is included so that the integral is exactly the Euclidean area of the polar tangent unit ball integrated over the Funk ball; deleting this positive constant does not affect the extremum or its sign. The statement is local in the affine trapezoid parameter \(\delta\). It makes no global claim for all \(\delta\), no claim for arbitrary quadrilateral deformations, and no claim about the global finite-radius extremizers among all convex bodies.

The symmetry axis of \(T_\delta\) forces the unique Funk–Santaló center onto the vertical axis. The transformation obtained by interchanging the two bases and applying an affine rescaling sends \(T_\delta\) to \(T_{-\delta}\) and \((0,s)\) to \((0,-s)\). Consequently \(s_R\) is odd and \(\Phi_R\) is even near zero.

## Proof
Write \(\tau=e^{-R}=1-\lambda\). For a point \(z=(x,y)\) in \(T_\delta\), put
\[
d(y)=\frac{2}{1-\delta}(1+\delta y).
\]
The four vertices of \((T_\delta-z)^\circ\) are obtained from the two horizontal supporting lines and the two sloping supporting lines. Splitting the polar quadrilateral along its vertical diagonal gives the exact polar-area formula
\[
\left|(T_\delta-z)^\circ\right|=
\frac{4d(y)}{(1-y^2)(d(y)^2-4x^2)}.
\]
The radius-\(R\) forward Funk ball centered at \((0,s)\) is the affine copy \((0,s)+\lambda(T_\delta-(0,s))\). Parameterize it by \(q=(q_x,u)\in T_\delta\), so \(y=\tau s+\lambda u\). The horizontal half-width of \(T_\delta\) at height \(u\) is \(d(u)/2\). Integrating first in \(q_x\) therefore yields
\[
V_R(\delta,s):=\omega_2\operatorname{Vol}_{T_\delta}\!\left(B_{T_\delta}((0,s),R)\right)
=4\lambda\int_{-1}^{1}
\frac{\operatorname{artanh}\!\left(\frac{\lambda(1+\delta u)}{1+\delta(\tau s+\lambda u)}\right)}{1-(\tau s+\lambda u)^2}\,du.
\]
This formula is analytic in \((\delta,s)\) near \((0,0)\). Direct differentiation under the integral, followed by elementary rational integration, gives
\[
V_{ss}(0,0)=\frac{16\lambda A}{(1+\lambda)^2},
\]
\[
V_{\delta s}(0,0)=\frac{8\bigl(\lambda-(1+\lambda)A\bigr)}{(1+\lambda)^2},
\]
and
\[
V_{\delta\delta}(0,0)=\frac{16(\lambda-A)}{(1+\lambda)^2}.
\]
Because \(V_{ss}(0,0)>0\), the implicit-function theorem applies to the minimizing-center equation \(V_s(\delta,s)=0\). Hence
\[
s_R'(0)=-\frac{V_{\delta s}(0,0)}{V_{ss}(0,0)}=rac{(1+\lambda)A-\lambda}{2\lambda A}.
\]
For the optimized value \(\Phi_R(\delta)=V_R(\delta,s_R(\delta))\), the Schur-complement formula gives
\[
\Phi_R''(0)=V_{\delta\delta}(0,0)-\frac{V_{\delta s}(0,0)^2}{V_{ss}(0,0)}=-\frac{4N_R}{A\lambda(1+\lambda)^2}.
\]
It remains only to prove \(N_R>0\). Viewed as a quadratic in \(A\), its two roots are
\[
r_\pm=\frac{\lambda\bigl(1+(3\pm2\sqrt2)\lambda\bigr)}{1+6\lambda+\lambda^2}.
\]
For \(0<\lambda<1\),
\[
r_+<\lambda<\operatorname{artanh}\lambda=A,
\]
because the denominator minus the numerator factor defining \(r_+/\lambda\) is \((3-2\sqrt2)\lambda+\lambda^2>0\), while \(\operatorname{artanh}\lambda>\lambda\). Since the quadratic has positive leading coefficient, \(N_R>0\), proving \(\Phi_R''(0)<0\).

Finally, the displayed formula for \(c_R\), together with \(\operatorname{artanh}\lambda=\lambda+O(\lambda^3)\) as \(\lambda\downarrow0\), gives \(c_R\to1/2\). As \(\lambda\uparrow1\), \(A\to\infty\), giving \(c_R\to1\).

## Verification
The bundled verifier independently evaluates the integral formula by composite Simpson quadrature near \((\delta,s)=(0,0)\), compares finite-difference Hessian entries with the three closed forms above at several radii, and checks the exact positivity mechanism \(r_+<\lambda<A\). Its numerical role is corroborative: the proof of the sign is the exact quadratic-root argument above.

Replay with `python3 artifacts/verify.py`.

## Relationship to prior work
Faifman introduced the finite-radius Holmes–Thompson Funk-ball volume and its affine inequalities in arXiv:2012.12159. That work gives the basic integral identity and finite-radius extremal results for unconditional bodies, but it does not analyze trapezoids, quadrilaterals, or a shape Hessian at the parallelogram class.

Faifman, Vernicos, and Walsh, arXiv:2306.09268, prove that for a polygon the second-highest large-radius coefficient, after optimal centering, is uniquely maximized by affine images of the regular polygon. They also treat uniqueness of the finite-radius Funk–Santaló center and give explicit planar volume formulas. Their polygon extremality is an asymptotic statement in the radius; it does not imply the uniform finite-radius second variation proved here. The present result supplies an exact finite-radius transverse curvature along the complete affine one-parameter family of trapezoids and recovers the expected endpoint motion of the center.

## Limitations
The theorem is a local second-variation result at \(\delta=0\). It does not prove that \(\Phi_R(\delta)\) is globally monotone in \(|\delta|\), nor that the affine-parallelogram class is a local maximum under every quadrilateral deformation. It also does not settle any global finite-radius Funk-volume conjecture. The numerical verifier checks representative radii only and is not used to justify the universal quantifier.

## References
D. Faifman, “A Funk perspective on billiards, projective geometry and Mahler volume,” arXiv:2012.12159v1, first public 2020-12-22. Primary MSC 52A40.

D. Faifman, C. Vernicos, C. Walsh, “Volume growth of Funk geometry and the flags of polytopes,” arXiv:2306.09268v1, first public 2023-06-15; later Geometry & Topology 29 (2025), 3773–3811. Primary MSC 52A40.
