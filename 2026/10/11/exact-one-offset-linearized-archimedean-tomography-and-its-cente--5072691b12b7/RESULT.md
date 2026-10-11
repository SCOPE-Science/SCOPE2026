# Exact one-offset linearized Archimedean tomography and its centered blind spot

## Finding

Fix a Euclidean slab width
\[
0<h<2.
\]
For a smooth real function \(\varphi\in C^\infty(S^2)\), consider the normal/radial deformation of the unit sphere
\[
\Sigma_\varepsilon
=\{(1+\varepsilon\varphi(\omega))\omega:\omega\in S^2\},
\]
for sufficiently small \(|\varepsilon|\). For \(u\in S^2\) and \(s\in(-1,1-h)\), write
\[
A_\varepsilon(u,s;h)
=\mathcal H^2\bigl(\{x\in\Sigma_\varepsilon:s\le x\cdot u\le s+h\}\bigr).
\]
Thus \(A_0(u,s;h)=2\pi h\), independently of \(u,s\).

Let \(\Pi_\ell\) denote spherical-harmonic projection in degree \(\ell\) on \(S^2\), and let \(P_\ell\) be the Legendre polynomial with \(P_\ell(1)=1\). Then the *exact first variation* is
\[
\boxed{
\left.\frac{d}{d\varepsilon}A_\varepsilon(u,s;h)\right|_{\varepsilon=0}
=2\pi\sum_{\ell=0}^{\infty}
J_\ell(s,h)(\Pi_\ell\varphi)(u),
\quad
J_\ell(s,h)=\int_s^{s+h}\bigl(P_\ell(t)-tP_\ell'(t)\bigr)\,dt.
}
\]

The multipliers have the following exact algebraic properties:
\[
J_0(s,h)=h,\qquad J_1(s,h)=0,
\]
while, for every \(\ell\ge2\), \(J_\ell(\cdot,h)\) is a nonzero polynomial in \(s\) of degree exactly \(\ell\).

Consequently, if
\[
E_h=\bigcup_{\ell\ge2}\{s\in(-1,1-h):J_\ell(s,h)=0\},
\]
then \(E_h\) is countable (in fact the degree-\(\ell\) summand contributes at most \(\ell\) offsets). For every
\[
s\in(-1,1-h)\setminus E_h,
\]
the **full angular slab-area linearization at that single offset** has kernel exactly
\[
\boxed{\ker D A_{(h,s)}=\mathcal H_1(S^2),}
\]
the three-dimensional space of infinitesimal translations. The same kernel conclusion holds if linearized slab areas vanish for every \(u\) and all \(s\) in **any nonempty open interval** inside \((-1,1-h)\). In particular, generic single offsets form a dense \(G_\delta\) set of full Lebesgue measure.

For an arbitrary fixed offset, the kernel is characterized precisely by the harmonic coefficient rule
\[
\Pi_\ell\varphi=0
\quad\text{for every}\quad
\ell\notin \{1\}\cup\{j\ge2:J_j(s,h)=0\}.
\]
There is a sharp qualitative obstruction at the centered offset:
\[
\boxed{
s=-h/2\quad\Longrightarrow\quad
\bigoplus_{j\ge0}\mathcal H_{2j+1}(S^2)
\subseteq\ker D A_{(h,-h/2)}.
}
\]
Thus measuring every direction with a centered slab can miss infinitely many independent shape modes, although almost every other fixed offset detects all shape modes at first order.

## Assumptions and scope

All areas are ordinary Euclidean surface areas. The unit sphere is centered at the fixed origin; the two bounding planes of each slab have signed heights \(s\) and \(s+h\) in direction \(u\). The offset is an absolute height, not a moving fraction of the deformed body's support width. Both planes meet the undeformed unit sphere transversally because
\[
-1<s<s+h<1.
\]
For any fixed such offset and smooth \(\varphi\), they continue to meet the deformed surface transversally for sufficiently small \(|\varepsilon|\). The deformation is a smooth strictly convex surface when \(|\varepsilon|\) is sufficiently small, because strict convexity is open at the sphere in the \(C^2\) topology.

The operator is the derivative at \(\varepsilon=0\), evaluated with the slab width and offset held fixed. It is **not** a claim that the nonlinear map of a general surface can be reconstructed from one offset. It gives no inverse norm bound; small nonzero multipliers may cause ill conditioning.

## Proof

**First variation and moving boundaries.** Put \(t=\omega\cdot u\) and \(r_\varepsilon(\omega)=1+\varepsilon\varphi(\omega)\). The radial-graph area element is
\[
 dA_\varepsilon
=r_\varepsilon^2\sqrt{1+\frac{|\nabla_{S^2}r_\varepsilon|^2}{r_\varepsilon^2}}\,d\omega
=\bigl(1+2\varepsilon\varphi(\omega)\bigr)d\omega+O(\varepsilon^2).
\]
The slab condition is \(s\le r_\varepsilon(\omega)t\le s+h\). Applying the elementary moving-boundary differentiation rule, justified by the implicit function theorem and transversality at each bounding circle, gives
\[
\begin{aligned}
L_{h,s}\varphi(u)
&:=\left.\frac{d}{d\varepsilon}A_\varepsilon(u,s;h)\right|_0\\
&=\int_{S^2}\varphi(\omega)
\Bigl[2\mathbf1_{[s,s+h]}(t)+t\delta(t-s)-t\delta(t-s-h)\Bigr]d\omega.
\end{aligned}
\]
The delta notation is a concise form of the classical boundary-integral formula. In particular its two boundary contributions have coefficients \(s\) and \(-(s+h)\), respectively.

**Harmonic diagonalization.** The Funk--Hecke identity on \(S^2\), with the standard surface measure and \(P_\ell(1)=1\), says that integrating against a zonal kernel \(k(u\cdot\omega)\) multiplies every degree-\(\ell\) spherical harmonic by
\[
2\pi\int_{-1}^1 k(t)P_\ell(t)\,dt.
\]
The identity holds here also for the two Dirac boundary terms, either by approximation or directly by circular integration. Therefore
\[
\begin{aligned}
L_{h,s}(\Pi_\ell\varphi)
&=2\pi\left[
2\int_s^{s+h}P_\ell(t)\,dt
+sP_\ell(s)-(s+h)P_\ell(s+h)
\right]\Pi_\ell\varphi\\
&=2\pi\left[\int_s^{s+h}(P_\ell(t)-tP_\ell'(t))\,dt\right]\Pi_\ell\varphi,
\end{aligned}
\]
where the second equality is integration by parts. Smoothness of \(\varphi\) and polynomial growth of the multipliers allow termwise harmonic summation, proving the displayed expansion.

**The exact multiplier zeros.** The first two Legendre polynomials are
\[
P_0(t)=1,\qquad P_1(t)=t,
\]
so \(J_0=h\) and \(J_1=0\) for every offset. For \(\ell\ge2\), the leading term of \(P_\ell\) is
\[
c_\ell t^\ell,\qquad c_\ell=\frac{(2\ell)!}{2^\ell(\ell!)^2}>0.
\]
Consequently the leading term of the polynomial \(P_\ell(t)-tP_\ell'(t)\) is \((1-\ell)c_\ell t^\ell\), and the leading term of its integral from \(s\) to \(s+h\), viewed as a polynomial in \(s\), is
\[
h(1-\ell)c_\ell s^\ell.
\]
Because \(h>0\) and \(\ell\ge2\), this coefficient is nonzero. Thus \(J_\ell(\cdot,h)\) has degree exactly \(\ell\) and has at most \(\ell\) real roots.

**Every exceptional kernel.** The spherical harmonics form an orthogonal complete decomposition of smooth functions. Projecting \(L_{h,s}\varphi\) onto degree \(\ell\) yields exactly
\[
2\pi J_\ell(s,h)\Pi_\ell\varphi.
\]
Thus the vanishing operator condition is equivalent, degree by degree, to the coefficient rule above. Outside the countable union of zeros \(E_h\), only degree one survives. If the operator vanishes for all offsets in a nonempty open interval, each polynomial \(J_\ell(\cdot,h)\), \(\ell\ne1\), cannot vanish throughout that interval, again forcing only degree one. The degree-one functions \(\varphi(\omega)=a\cdot\omega\) are precisely the normal velocities of translations of the unit sphere; an exact translation does not change the area of any transversal width-\(h\) spherical band.

**Centered slabs.** Legendre parity implies
\[
P_\ell(-t)=(-1)^\ell P_\ell(t),
\]
and hence \(P_\ell(t)-tP_\ell'(t)\) is odd when \(\ell\) is odd. At \(s=-h/2\), the integration interval is symmetric about zero, so \(J_\ell(-h/2,h)=0\) for every odd \(\ell\). Their direct sum is infinite-dimensional. This proves the centered blind spot and finishes the argument.

## Verification

The standalone \(verify.py\) performs exact polynomial checks for degrees \(0\) through \(12\): it reproduces both equivalent formulas for \(J_\ell\), checks the claimed degree and leading coefficient for \(\ell\ge2\), and checks odd-degree centered cancellation. These finite checks are **not** the proof for arbitrary degrees; that is the leading-coefficient argument above.

It also performs independent centered finite-difference checks against the actual radial-graph area integral for zonal harmonics of degrees \(0\) through \(4\), at one nonsymmetric width and offset. The direct area calculation solves for the moving boundary circles and includes the slope term in the surface Jacobian. The numerical replay tests sign conventions and the \(2\pi\) normalization, but does not replace the analytic moving-boundary proof.

## Relationship to prior work

Lai's 2026 preprint proves a nonlinear characterization of the sphere from the fixed-width Archimedean slab-area property in the class of smooth connected closed embedded surfaces. It concerns *all allowed translations of the slab* and all directions, whereas the present statement classifies the Fréchet derivative of the measurement made at **one fixed absolute height**. Nonlinear uniqueness with complete displacement data does not imply linearized injectivity from only a single displacement.

Ghomi, Howard, and Lai's later work proves a stronger nonlinear result permitting the common slab area to depend on direction, and develops height-density periodicity and a Newtonian-potential averaging identity. Its inspected full manuscript does not derive this radial-graph Legendre multiplier or characterize the one-offset infinitesimal kernel. The published 2017 geometric question establishes the motivation for fixed-width data but does not address local derivative kernels.

The computation relies on the standard Funk--Hecke identity, not a new harmonic-analysis theorem. The new result is the exact geometric **measurement-kernel classification**, its generic single-offset injectivity modulo translations, and the striking infinite-dimensional failure at the natural centered offset. It does not assert global recovery from a single offset.

## Limitations

The result concerns the derivative at the unit sphere, not a nonlinear inverse problem or a uniform stability estimate. The countable exceptional set is specified implicitly by polynomial roots; its topology and the size of nonzero harmonic multipliers are not classified. At some exceptional offsets beyond the centered one, additional harmonics may be invisible. The first eligible preprint's abstract was accessible, but its complete text was not available for inspection despite lawful public-source attempts; possible earlier formulations under different terminology remain a real originality risk.

## References

1. Mijia Lai, *The sphere is the only closed surface satisfying the fixed-width Archimedean property*, arXiv:2610.01550v1, first submitted 1 October 2026, https://arxiv.org/abs/2610.01550.
2. Mohammad Ghomi, Ralph Howard, and Mijia Lai, *A Converse to the Archimedes Sphere Theorem*, manuscript dated October 2026, https://ghomi.math.gatech.edu/Papers/archimedes.pdf.
3. Mohammad Ghomi, *Converse of the Archimedean property of the sphere*, MathOverflow Question 283109 (2017), https://mathoverflow.net/questions/283109.
4. F. Dai and Y. Xu, *Approximation Theory and Harmonic Analysis on Spheres and Balls*, Springer Monographs in Mathematics, Springer, 2013 (Funk--Hecke identity).
