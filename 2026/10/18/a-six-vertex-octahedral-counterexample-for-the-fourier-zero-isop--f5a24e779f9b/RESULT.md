# A six-vertex octahedral counterexample for the Fourier-zero isoperimetric problem

## Finding
Let
\[
P_a=\operatorname{conv}\{(\pm a,0,0),(0,\pm1,0),(0,0,\pm1)\}
=\{(x,y,z)\in\mathbb R^3:|x|/a+|y|+|z|\le1\},\qquad a>0.
\]
For a bounded positive-volume body \(K\), use the real-frequency Fourier transform
\(\widehat{\chi_K}(\xi)=\int_K e^{i\langle\xi,p\rangle}\,dp\) and let
\(\kappa(K)=\min\{\|\xi\|_2:\widehat{\chi_K}(\xi)=0,\ \xi\in\mathbb R^3\}\), whenever the real zero set is nonempty.

**Theorem.** For every \(a>0\), the Fourier transform of \(P_a\) is **strictly positive** at every \((u,v,w)\in\mathbb R^3\) satisfying \(v^2+w^2\le2\). Its real Fourier zero set is nonempty, and consequently
\[
\boxed{\ \kappa(P_a)>\sqrt2\qquad(a>0).\ }
\]
The equal-volume Euclidean ball \(B_a\) satisfies
\[
\kappa(B_a)=j_{3/2,1}\left(\frac\pi a\right)^{1/3},
\]
where \(j_{3/2,1}\) is the first positive root of \(\sin t-t\cos t\). Therefore \(\kappa(P_a)>\kappa(B_a)\) whenever
\[
a>\frac{\pi j_{3/2,1}^{3}}{2\sqrt2}.
\]
**In particular, the six-vertex integer-coordinate polytope \(P_{101}\) rigorously violates the proposed ball-maximal Fourier-zero inequality.** Six vertices are the minimum possible for any full-dimensional centrally symmetric three-dimensional polytope. Neither the zero-free cylinder width \(\sqrt2\) nor the parameter bound is asserted optimal for this family.

## Assumptions and scope
The body \(P_a\) is the full-dimensional, centrally symmetric octahedron specified above, with eight flat triangular facets and exactly six vertices. All frequencies are real and distances are Euclidean. Boundaries have zero Lebesgue measure, so open or closed polytope conventions give the same Fourier transform. The motivating source, first posted September 9, 2026, has primary MSC2020 class 52A40.

## Proof
**1. Diamond sections and a uniform curvature bound.** For real transverse frequencies \(v,w\), define
\[
\Phi_{v,w}(r)=\int_{|y|+|z|\le r}e^{i(vy+wz)}\,dy\,dz
=4\int_0^r\cos(vy)\int_0^{r-y}\cos(wz)\,dz\,dy,
\qquad 0\le r\le1.
\]
The equality follows by pairing all four reflected quadrants. It also makes \(\Phi_{v,w}\) real. Differentiation under the integral gives
\[
\begin{aligned}
\Phi_{v,w}'(r)&=4\int_0^r\cos(vy)\cos(w(r-y))\,dy,\\
\Phi_{v,w}''(r)&=4\cos(vr)-4w\int_0^r\cos(vy)\sin(w(r-y))\,dy.
\end{aligned}
\]
The elementary inequalities \(\cos s\ge1-s^2/2\) and \(|\sin s|\le|s|\), valid for all real \(s\), yield
\[
\Phi_{v,w}''(r)
\ge4\left(1-\frac{v^2r^2}{2}-\frac{w^2r^2}{2}\right).
\]
When \(v^2+w^2\le2\), this lower bound is \(4(1-r^2)>0\) for every \(0\le r<1\). Also \(\Phi_{v,w}(0)=\Phi'_{v,w}(0)=0\); hence \(\Phi_{v,w}(r)>0\) for \(0<r\le1\).

**2. Strict positivity at every axial frequency.** Put \(g(t)=\Phi_{v,w}(1-t)\) on \([0,1]\). The diamond-section formula and the change of variable \(t=|x|/a\) imply
\[
\widehat{\chi_{P_a}}(u,v,w)=2a\int_0^1g(t)\cos(aut)\,dt.
\]
For \(v^2+w^2\le2\), the preceding estimates give \(g''(t)>0\) on \(0<t\le1\), and \(g(1)=g'(1)=0\). If \(u\ne0\), two integrations by parts give the exact identity
\[
\int_0^1g(t)\cos(aut)\,dt
=\frac1{a^2u^2}\int_0^1g''(t)\bigl(1-\cos(aut)\bigr)\,dt>0.
\]
Indeed the integrand is nonnegative everywhere and positive on a set of positive measure. If \(u=0\), strict positivity follows directly from \(g(t)>0\) for \(0\le t<1\). This proves the stated zero-free transverse cylinder for every \(a>0\).

**3. Real zeros exist.** Directly integrate the axial coordinate first, to obtain
\[
\widehat{\chi_{P_a}}(0,s,s)
=2a\int_{|y|+|z|\le1}(1-|y|-|z|)e^{is(y+z)}\,dy\,dz.
\]
With \(p=y+z\), \(q=y-z\), the diamond becomes the square \(\max\{|p|,|q|\}\le1\), the Jacobian is \(1/2\), and integration in \(q\) gives
\[
\widehat{\chi_{P_a}}(0,s,s)
=a\int_{-1}^1(1-p^2)e^{isp}\,dp
=\frac{4a}{s^3}(\sin s-s\cos s),\qquad s\ne0.
\]
The function \(\sin s-s\cos s\) is positive at \(s=\pi\) and negative at \(s=3\pi/2\), so it has a zero in that interval. Thus the real zero set of \(\widehat{\chi_{P_a}}\) is nonempty. It is closed by continuity; its least Euclidean norm is attained by compactness of bounded sublevel balls. Every zero has \(v^2+w^2>2\), so that minimum exceeds \(\sqrt2\), proving \(\kappa(P_a)>\sqrt2\).

**4. Equal-volume comparison and an exact integer certificate.** Slicing the octahedron gives
\[
|P_a|=\int_{-a}^a2(1-|x|/a)^2\,dx=\frac{4a}{3}.
\]
The volume-radius relation \((4\pi/3)R^3=4a/3\) gives \(R=(a/\pi)^{1/3}\). The transform of the Euclidean ball vanishes first at \(j=j_{3/2,1}\), the first root of \(\sin j-j\cos j=0\); hence \(\kappa(B_a)=j(\pi/a)^{1/3}\). The displayed sufficient inequality follows by cubing \(\kappa(B_a)<\sqrt2\).

For \(a=101\), use the rational number \(x_0=44935/10000\). The exact Taylor expansion
\[
\sin x-x\cos x
=\sum_{k=1}^{\infty}(-1)^{k+1}\frac{2k\,x^{2k+1}}{(2k+1)!}
\]
has strictly decreasing term magnitudes from \(k=2\) onward at \(x=x_0\), since
\[
\frac{a_{k+1}}{a_k}
=\frac{k+1}{k}\frac{x_0^2}{(2k+3)(2k+2)}<1\qquad(k\ge2)
\]
for \(a_k=2k x_0^{2k+1}/(2k+1)!\). The ninth partial sum is therefore an upper bound, and exact rational arithmetic in `checks/exact_bounds.py` establishes
\[
\sin x_0-x_0\cos x_0
<\sum_{k=1}^{9}(-1)^{k+1}\frac{2k\,x_0^{2k+1}}{(2k+1)!}
<-\frac3{10000}<0.
\]
Because \(\frac{d}{dx}(\sin x-x\cos x)=x\sin x\), this function is positive on \((0,\pi]\), then strictly decreases until \(3\pi/2\). Thus \(j<x_0\). Combining the classical bound \(\pi<22/7\) with \(\sqrt2>24/17\) (verified by squaring) yields the **entirely rational** strict inequality
\[
\frac{\pi j^3}{2\sqrt2}
<\frac{(22/7)(44935/10000)^3}{2(24/17)}
=\frac{135733119870161}{1344000000000}<101.
\]
It follows that \(\kappa(P_{101})>\sqrt2>\kappa(B_{101})\).

**5. Minimal vertex count.** A centrally symmetric three-dimensional polytope's vertices form antipodal pairs about its center. At least three pairs are needed to span the ambient dimension, so every full-dimensional such polytope has at least six vertices. The vertices displayed for \(P_{101}\) are all exposed, proving sharpness of this combinatorial count.

## Verification
Run `python checks/exact_bounds.py` with the Python 3 standard library. It verifies, using only exact `fractions.Fraction` arithmetic, the negative ninth Taylor partial sum, the elementary squared bound for \(\sqrt2\), and the strict rational comparison with \(101\), then prints `OCTAHEDRAL_FOURIER_EXACT_CERTIFICATE_OK`. These are finite certificates for the specified rational inequalities, not substitutes for the analytic inequalities holding over continuous families of frequencies. The curvature inequality, two integrations by parts, explicit Fourier zero and compactness argument establish the uniform infinite-frequency assertion without discretization.

## Relationship to prior work
Gómez-Serrano, Levitin, Platt and Polterovich (2026, Section 2) disprove the previously proposed equal-volume-ball inequality in all dimensions at least three by using elongated convex bipyramids whose transverse sections are **Euclidean disks**, not finite-vertex polytopes. They also prove planar polygonal counterexamples. Benguria, Levitin and Parnovski (2009, Remark 4.11) earlier used a three-dimensional body of revolution with the same circular transverse geometry to demonstrate failure of a diameter-based bound. Neither inspected source states a six-vertex polyhedral witness.

Three relevant subsequent public comparisons—*A Pólya–Bessel zero-free strip for Fourier bipyramids* (2026), *A rationally certified width-two Fourier zero-free strip for three-dimensional bipyramids* (2026), and *Exact leading slope of Fourier-zero distance for elongated bipyramids* (2026)—also concern the circular-section family. Their Fourier-profile identities and bounds do not directly imply a sign condition for the two-parameter Fourier transform of the **diamond sections** in \(P_a\), nor do they constrain the number of vertices of a polyhedral counterexample. The present contribution is the minimal six-vertex, integral-coordinate polyhedral realization with a uniform analytic zero-free cylinder, not the general failure of ball maximality, which is known.

## Limitations
The \(\sqrt2\) zero-free transverse cylinder and the sufficient parameter bound for \(a=101\) are not established as optimal. This does not calculate \(\kappa(P_a)\) exactly or classify all six-vertex polyhedra violating the ball inequality. The six-vertex minimum applies to the class of centrally symmetric **polytopes**, not all convex bodies. The exact Taylor check is a same-document reproducibility calculation, not an independent scientific audit. Priority could be affected by unindexed work on Fourier zeros of anisotropic octahedra.

## References
1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517v1, first posted 2026-09-09, https://arxiv.org/html/2609.10517v1.
2. R. Benguria, M. Levitin, L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, Journal of Functional Analysis 257 (2009), 2088–2123; arXiv:0801.1617v3, https://arxiv.org/html/0801.1617v3.
3. *A Pólya–Bessel zero-free strip for Fourier bipyramids*, 2026, published mathematical note, identifier `72c1da0f9bb0`.
4. *A rationally certified width-two Fourier zero-free strip for three-dimensional bipyramids*, 2026, published mathematical note, identifier `7d5ef01cc46e`.
5. *Exact leading slope of Fourier-zero distance for elongated bipyramids*, 2026, published mathematical note, identifier `328d6e388fdc`.
