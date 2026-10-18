# Two sharp asymmetry thresholds for hyperbolic drums

## Finding
Let \(r>0\) and let a hyperbolic ball of radius \(r\) in \(\mathbb H^3\) be cut by two parallel totally geodesic planes, independently removing caps of angular depths \(\alpha_+,\alpha_-\in(0,\pi/2)\). Write \(S\) for the total boundary area and \(M\) for the total mean curvature, including the standard curvature-measure contribution at the circular ridges. A drum is **balanced** when \(\alpha_+=\alpha_-\).

There are two exact and distinct radii
\[
r_{\mathrm{shallow}}=\operatorname{arsinh}(1/2),\qquad
r_{\mathrm{deep}}=\operatorname{arsinh}\sqrt{\frac{\pi-2}{4-\pi}},\qquad
0<r_{\mathrm{shallow}}<r_{\mathrm{deep}}.
\]
For any fixed \(r\) strictly between these radii, balanced drums are strict *local minima* of \(M\) among unequal two-cap cuts of the **same parent ball and same total boundary area** when both cuts are sufficiently shallow, but strict *local maxima* for sufficiently deep cuts. Consequently, a small unequal displacement of the two cutting planes decreases \(M\) at fixed area in the deep-cut regime, whereas it increases \(M\) at fixed area in the shallow-cut regime. The assertions concern the one-dimensional antisymmetric cutting direction, not all convex-body perturbations.

More precisely, put \(s=\sinh r\), \(c=\cosh r\), and set
\[
\begin{aligned}
A_r(\alpha)&=2\pi\left[s^2\cos\alpha+\sqrt{1+s^2\sin^2\alpha}-1\right],\\
B_r(\alpha)&=2\pi s\left[2c\cos\alpha+\sin\alpha\arctan(c\tan\alpha)\right].
\end{aligned}
\]
The boundary area and total mean curvature of the unequal two-cap drum are exactly
\[
S=A_r(\alpha_+)+A_r(\alpha_-),\qquad
M=B_r(\alpha_+)+B_r(\alpha_-).
\]
The function \(A_r\) is strictly decreasing on \((0,\pi/2)\), so
\(m_r=B_r\circ A_r^{-1}\) is well-defined on
\((2\pi(c-1),\,2\pi s^2)\). Its second derivative has the *sharp endpoint laws*
\[
\boxed{\lim_{\alpha\downarrow0}\alpha^2m_r''(A_r(\alpha))
=\frac{4s^2-1}{5\pi s^3c},}
\]
\[
\boxed{\lim_{\alpha\uparrow\pi/2}m_r''(A_r(\alpha))
=\frac{4-\pi-2/c^2}{4\pi s^3}.}
\]
The first coefficient changes sign precisely at \(r_{\mathrm{shallow}}\), and the second precisely at \(r_{\mathrm{deep}}\). At either critical radius the displayed leading coefficient vanishes; no sign assertion at the critical radius itself is claimed.

## Assumptions and scope
Use the curvature \(-1\) metric on \(\mathbb H^3\). In the Beltrami--Klein model, let the parent ball be the Euclidean coordinate ball \(\|x\|\le\tanh r\). The two clipping planes are
\(x_3=\tanh r\cos\alpha_+\) and
\(x_3=-\tanh r\cos\alpha_-\), respectively, and the clipped body is their intersection with the parent ball. Assume \(r>0\) and both angles strictly inside \((0,\pi/2)\); the limiting ball and double disk are used only to evaluate the asymptotics. A balanced surface is varied at fixed parent radius and fixed **total** area by changing the two cuts independently. Total mean curvature uses \(H=\kappa_1+\kappa_2\) on smooth pieces and the usual convex curvature measure on edges, as in the cited source.

## Proof
**1. Exact additivity.** The spherical belt contributes \(2\pi s^2(\cos\alpha_++\cos\alpha_-)\) to the area and \(4\pi sc(\cos\alpha_++\cos\alpha_-)\) to the total mean curvature. The two totally geodesic disk faces contribute areas \(2\pi(\sqrt{1+s^2\sin^2\alpha_\pm}-1)\) separately and zero smooth mean curvature. The circular ridge from a cut of depth \(\alpha\) contributes \(2\pi s\sin\alpha\arctan(c\tan\alpha)\) to total mean curvature. Adding the independent north and south contributions proves the stated formulas for \(S,M\). For identical cuts they reduce exactly to Hong's formulas (4.1)--(4.2). There is no term coupling the planes, since the two ridge circles and the two disk faces are disjoint.

**2. Fixed-area direction.** Direct differentiation yields
\[
A'_r(\alpha)=2\pi s^2\sin\alpha
\left(\frac{\cos\alpha}{\sqrt{1+s^2\sin^2\alpha}}-1\right)<0
\qquad(0<\alpha<\pi/2).
\]
Let \(x=A_r(\alpha)\), and for sufficiently small real \(h\) define
\(\alpha_+(h)=A_r^{-1}(x+h)\) and
\(\alpha_-(h)=A_r^{-1}(x-h)\). The total area is exactly \(2x\), while Taylor's theorem gives
\[
M(h)-M(0)=m_r''(x)h^2+O_{r,\alpha}(h^4).
\]
Thus the sign of \(m_r''(x)\) determines strict local minimality or maximality within this balanced-area family.

**3. Shallow cuts.** Divide \(A_r\) and \(B_r\) by \(2\pi\), writing \(a(\alpha)\), \(b(\alpha)\). With \(s=\sinh r\), \(c=\cosh r\), the Taylor expansions through sixth order are
\[
\begin{aligned}
a(\alpha)&=s^2-\frac{s^2c^2}{8}\alpha^4
+\frac{s^2c^2(3s^2+1)}{48}\alpha^6+O_r(\alpha^8),\\
b(\alpha)&=2sc-\frac{sc(4s^2+1)}{12}\alpha^4
+\frac{sc(36s^4+22s^2+1)}{180}\alpha^6+O_r(\alpha^8).
\end{aligned}
\]
For \(a_4,a_6,b_4,b_6\) the corresponding coefficients, direct simplification gives the nontrivial identity
\[
b_6a_4-b_4a_6=-\frac{s^3(4s^2-1)c^5}{960}.
\]
Use
\[
m_r''(A_r(\alpha))
=\frac{B_r''(\alpha)A_r'(\alpha)-B_r'(\alpha)A_r''(\alpha)}{A_r'(\alpha)^3}.
\]
Substitution, remembering the \(2\pi\) factor, yields
\[
m_r''(A_r(\alpha))
=\frac{4s^2-1}{5\pi s^3c}\alpha^{-2}+O_r(1),
\]
which proves the first endpoint law and its strict signs whenever \(s\ne1/2\).

**4. Deep cuts.** Put \(u=\cos\alpha\downarrow0\). The same physical one-cap area and curvature take the regular forms
\[
\begin{aligned}
A_r(u)&=2\pi\left[s^2u+\sqrt{c^2-s^2u^2}-1\right],\\
B_r(u)&=2\pi s\left[2cu+\sqrt{1-u^2}
\left(\frac\pi2-\arctan\frac{u}{c\sqrt{1-u^2}}\right)\right].
\end{aligned}
\]
At \(u=0\), the derivatives are
\[
A'_r=2\pi s^2,\quad A''_r=-\frac{2\pi s^2}{c},\quad
B'_r=2\pi s\left(2c-\frac1c\right),\quad B''_r=-\pi^2s.
\]
The same inverse-function differentiation therefore gives
\[
m_r''(A_r(\alpha))
=\frac{4-\pi-2/c^2}{4\pi s^3}+O_r(\cos\alpha).
\]
The sign changes where \(c^2=2/(4-\pi)\), equivalently
\(s^2=(\pi-2)/(4-\pi)\), giving the second exact radius.

**5. Opposite signs in the intermediate band.** The two radii satisfy
\(r_{\mathrm{shallow}}<r_{\mathrm{deep}}\) since \(1/4<(\pi-2)/(4-\pi)\). If \(r\) is strictly between them, the shallow-limit coefficient is positive and the deep-limit coefficient is negative. By the endpoint expansions there are nonempty open angular intervals adjacent to \(0\) and \(\pi/2\) where the respective signs hold. Step 2 converts these signs into the asserted strict fixed-area local minimum and maximum. Continuity additionally ensures at least one intermediate angle where the second variation vanishes; uniqueness of such angles is **not** asserted.

## Verification
The standalone `checker.py` verifies the symbolic sixth-order coefficients, the cancellation identity, and the deep-cut derivative identity using SymPy. It separately differentiates the full original formulas with mpmath at high precision and checks the asymptotic predictions. It constructs two unequal cutting depths by numerically inverting the **exact area map** with opposite offsets and verifies that the total area is preserved and that the observed change in total mean curvature has the predicted sign. These checks are consistency tests; the analytical derivation in the preceding section proves the continuous claims.

## Relationship to prior work
Fang Hong, *On Santaló's Problem*, arXiv:2606.01771 (first made public June 1, 2026), proves existence of a family of centered two-plane truncated hyperbolic balls beating both the sphere and flat double-disk benchmark at some areas. Its section 4 gives formulas (4.1)--(4.2) for **equal** top and bottom angular cuts. The present result uses those geometric cap components but allows **independent cuts** and establishes an exact, sign-changing fixed-area antisymmetric second variation at two natural boundary geometries. It does **not** strengthen Hong's global counterexample or classify global Santaló minimizers.

Ghomi and Spruck's *Minkowski Inequality in Cartan--Hadamard Manifolds*, arXiv:2206.06554, gives global lower bounds for total mean curvature; those bounds do not determine the restricted two-cut second variation. See also Hong, *Sharp Minkowski Type Inequality in Cartan-Hadamard 3-Spaces*, arXiv:2603.19646, for general curvature inequalities rather than the explicit unequal-cut geometry.

## Limitations
This is a sharp **endpoint local** analysis in the two-parameter cutting family at a fixed parent radius. The finite-angle critical locus, its number of roots, global minimizers of this two-parameter family, and all unrestricted convex-body variations are not classified. At each threshold radius the leading coefficient vanishes, and higher-order behavior is left open. No assertion about unrestricted Santaló minimizers follows. The rigorous signs require fixed \(r\) strictly away from the displayed thresholds and cut angles sufficiently close to the relevant boundary.

## References
1. F. Hong, *On Santaló's Problem*, arXiv:2606.01771, first version June 1, 2026, especially section 4, equations (4.1)--(4.2). https://arxiv.org/html/2606.01771v4
2. M. Ghomi and J. Spruck, *Minkowski Inequality in Cartan--Hadamard Manifolds*, arXiv:2206.06554, 2022/2023. https://arxiv.org/abs/2206.06554
3. F. Hong, *Sharp Minkowski Type Inequality in Cartan--Hadamard 3-Spaces*, arXiv:2603.19646, 2026. https://arxiv.org/abs/2603.19646
