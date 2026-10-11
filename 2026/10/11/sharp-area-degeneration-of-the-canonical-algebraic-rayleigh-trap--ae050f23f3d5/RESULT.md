# Sharp area degeneration of the canonical algebraic Rayleigh trapping annulus

## Finding

The algebraic Poincaré–Bendixson annulus constructed by Grin and Schneider for the Rayleigh oscillator has an explicitly quantifiable geometric degeneration. Write \(A_{\mathrm{in}}(\lambda)\) and \(A_{\mathrm{out}}(\lambda)\) for the Euclidean areas enclosed by **their particular inner and outer algebraic ovals**, respectively. For \(\lambda>0\), the inner area has the sharp asymptotic expansion

\[
A_{\mathrm{in}}(\lambda)
=\frac32\lambda+
\frac{10\log\lambda+5+2\log(243/256)}{\lambda}
+o(\lambda^{-1}) \qquad(\lambda\to\infty).
\]

The outer area satisfies

\[
A_{\mathrm{out}}(\lambda)=C_{\mathrm{out}}\lambda+o(\lambda),\quad
C_{\mathrm{out}}=\frac23\int_0^{U_*}\sqrt{648+9u^4-u^6}\,du
=60.00037902855\ldots,
\]

where \(U_*\) is the unique positive root beyond \(\sqrt8\) of \(648+9U_*^4-U_*^6=0\), numerically \(U_*=3.59113593303\ldots\). In particular,

\[
\lim_{\lambda\to\infty}\frac{A_{\mathrm{in}}(\lambda)}{A_{\mathrm{out}}(\lambda)}
=\frac{3}{2C_{\mathrm{out}}}
=0.0249998420724\ldots .
\]

At the opposite end, the two limiting ovals are circles and
\[
\lim_{\lambda\downarrow0}A_{\mathrm{in}}(\lambda)=\frac{8\pi}{3},\quad
\lim_{\lambda\downarrow0}A_{\mathrm{out}}(\lambda)=8\pi,\quad
\lim_{\lambda\downarrow0}\frac{A_{\mathrm{in}}(\lambda)}{A_{\mathrm{out}}(\lambda)}=\frac13.
\]
The inner area also has the small-parameter expansion
\[
A_{\mathrm{in}}(\lambda)=\frac{8\pi}{3}+\frac{13\pi}{243}\lambda^2+o(\lambda^2).
\]
The exact area fraction quantifies the relative size of the two **certificate boundaries**, not the area enclosed by the actual limit cycle. No monotonicity of the area ratio is asserted.

## Assumptions and scope

The vector field is the cubic Rayleigh system
\[
\dot x=-y,\qquad \dot y=x+\lambda y-\frac{\lambda}{3}y^3,
\qquad\lambda>0.
\]
Following Grin and Schneider [1], define \(I_\lambda\) as the unique bounded oval of
\[
x^2+y^2-\frac83+\lambda x\left(y-\frac{y^3}{3}\right)=0,
\]
and \(O_\lambda\) as the image under the area-preserving map
\[
(x,y)=\left(-v+\lambda\left(\frac{u^3}{3}-u\right),u\right)
\]
of the outer oval in \((u,v)\) determined by
\[
 v^2+\lambda vu\left(2-\frac{u^2}{3}\right)
 +(1+\lambda^2)u^2-\frac7{12}\lambda^2u^4
 +\frac{\lambda^2}{18}u^6-8-3\lambda-18\lambda^2=0.
\]
The cited source proves that \(I_\lambda\) and \(O_\lambda\) bound a global trapping annulus containing the unique Rayleigh limit cycle; that fact and both defining ovals are **prior work**. The present claim concerns their enclosed Euclidean areas. All limits are taken through positive real values of \(\lambda\). The Euclidean area is the standard \(dx\,dy\) area, not an orbit-time measure.

Set \(c=8/3\), \(B=\sqrt3\), \(R=\sqrt c\), \(h(y)=y(1-y^2/3)\), and \(q(y)=4(c-y^2)\).

## Proof

**1. Exact inner area and its turning height.** Solving the inner defining quadratic for \(x\) shows that its horizontal chord at height \(y\) has length
\[
\sqrt{\Delta_\lambda(y)},\qquad
\Delta_\lambda(y)=\lambda^2h(y)^2+q(y).
\]
For \(0\le y\le R\), \(\Delta_\lambda(y)>0\) except for the endpoint at \(\lambda=0\). For \(R<y<B\), its derivative in \(t=y^2\) equals
\[
\frac{d}{dt}\left[\lambda^2t(1-t/3)^2+4(c-t)\right]
=\frac{\lambda^2}{3}(t-1)(t-3)-4<0.
\]
The discriminant is positive at \(R\) and negative at \(B\), so it has exactly one positive turning height \(Y_\lambda\in(R,B)\). The inner oval is the bounded branch, hence
\[
\boxed{\ A_{\mathrm{in}}(\lambda)
=2\int_0^{Y_\lambda}\sqrt{\lambda^2h(y)^2+q(y)}\,dy.\ }
\]
In particular, the upper limit is **not** the zero-parameter radius \(R\). This moving endpoint is essential to the sharp logarithmic term.

**2. Small damping.** As \(\lambda\downarrow0\), \(Y_\lambda\to R\) and the integrand tends to \(2\sqrt{c-y^2}\) on \([0,R]\), giving \(8\pi/3\). More precisely \(Y_\lambda-R=O(\lambda^2)\), and the added cap has area \(O(\lambda^3)\). On \([0,R]\), divide the difference of the two integrands by \(\lambda^2\), rationalize, and use the integrable bound proportional to \(h(y)^2/\sqrt{c-y^2}\); dominated convergence yields
\[
\lim_{\lambda\downarrow0}
\frac{A_{\mathrm{in}}(\lambda)-8\pi/3}{\lambda^2}
=\frac14\int_{-R}^{R}\frac{h(y)^2}{\sqrt{c-y^2}}\,dy
=\frac{13\pi}{243},
\]
where the last identity follows from \(y=R\sin\theta\) and elementary even trigonometric moments.

**3. Sharp large-damping inner area.** Put \(\epsilon=1/\lambda\), and denote \(Y_\lambda\) by \(Y_\epsilon\). Since \(h(y)>0\) for \(0<y<B\), \(Y_\epsilon\to B\) and \(\int_0^B h(y)\,dy=3/4\). Define
\[
J_\epsilon=
\int_0^{Y_\epsilon}\sqrt{h(y)^2+\epsilon^2q(y)}\,dy
-\int_0^B h(y)\,dy.
\]
Thus \(A_{\mathrm{in}}(\lambda)=3\lambda/2+2\lambda J_{1/\lambda}\).

For \(\delta=\sqrt\epsilon\), split \(J_\epsilon\) into the intervals \([0,\delta]\), \([\delta,B-\delta]\), and the signed remaining interval \([B-\delta,Y_\epsilon]\), subtracting \(\int_{B-\delta}^B h\) in the last one. At the lower endpoint, \(h(y)=y+O(y^3)\) and \(q(y)=q_0+O(y^2)\), where \(q_0=32/3\). Elementary integration of the model square root gives
\[
J_\epsilon^{(0)}=
\epsilon^2\left[
\frac83+\frac{16}{3}\log\frac{2\delta}{\epsilon\sqrt{32/3}}
\right]+o(\epsilon^2).
\]
At the upper endpoint put \(z=B-y\). Here \(h(B-z)=2z+O(z^2)\) and \(q(B-z)=-4/3+O(z)\). The turning value is \(z=\epsilon/\sqrt3+O(\epsilon^2)\); integrate the local model \(\sqrt{4z^2-4\epsilon^2/3}\) from its turning value to \(\delta\), subtracting \(\int_0^\delta 2z\,dz\). The result is
\[
J_\epsilon^{(B)}=
\epsilon^2\left[
-\frac16-\frac13\log\frac{4\delta}{\epsilon\sqrt{4/3}}
\right]+o(\epsilon^2).
\]
The replacement errors in these two models are \(o(\epsilon^2)\): away from a turning point, differentiate the square-root difference with respect to \(h,q\) and use the displayed \(O(y^3),O(y^2)\) or \(O(z^2),O(z)\) estimates; within an \(O(\epsilon)\) turning layer rescale the coordinate by \(\epsilon\), where the root displacement and the associated integrated error are of higher order. With \(\delta=\epsilon^{1/2}\), the middle-region Taylor remainder is \(O(\epsilon^4\delta^{-2})=O(\epsilon^3)\), while
\[
J_\epsilon^{(\mathrm{mid})}
=\epsilon^2\int_\delta^{B-\delta}\frac{q(y)}{2h(y)}\,dy+o(\epsilon^2).
\]
The antiderivative is explicit:
\[
\int\frac{q(y)}{2h(y)}\,dy=
\frac{16}{3}\log y+\frac13\log(3-y^2).
\]
Consequently,
\[
J_\epsilon^{(\mathrm{mid})}
=\epsilon^2\left[-5\log\delta+\frac52\log3+\frac13\log2\right]+o(\epsilon^2).
\]
The cutoff logarithms cancel exactly. Simplifying the finite constants gives
\[
J_\epsilon=
\epsilon^2\left[5\log(1/\epsilon)+\frac52+\log(243/256)\right]
+o(\epsilon^2).
\]
Substitution into the exact area identity proves the stated two-term logarithmic expansion. In particular, **both endpoints** contribute to the logarithmic coefficient: omitting the moving upper turning point would give an incorrect answer.

**4. Exact outer area and its large-damping limit.** The change of coordinates defining \(O_\lambda\) has Jacobian determinant \(1\), so it preserves Euclidean area. Regard the defining outer polynomial as a quadratic in \(v\). Its discriminant is
\[
D_\lambda(u)=\frac{\lambda^2(648+9u^4-u^6)+108\lambda+288-36u^2}{9}.
\]
Writing \(t=u^2\), the numerator is positive for \(0\le t\le8\); for \(t>8\) its derivative is \(\lambda^2(18t-3t^2)-36<0\). Thus it has a unique zero \(t=U_\lambda^2>8\), and horizontal chord integration in \((u,v)\) gives
\[
\boxed{\ A_{\mathrm{out}}(\lambda)
=\int_{-U_\lambda}^{U_\lambda}\sqrt{D_\lambda(u)}\,du.\ }
\]
At \(\lambda=0\) this is the disk \(u^2+v^2\le8\), so its limiting area is \(8\pi\). As \(\lambda\to\infty\), \(U_\lambda\to U_*\), the unique positive zero beyond \(\sqrt8\) of \(g(u)=648+9u^4-u^6\). After dividing by \(\lambda\), bounded-support dominated convergence (or a fixed-interval substitution \(u=U_\lambda\sin\theta\)) yields
\[
\lim_{\lambda\to\infty}\frac{A_{\mathrm{out}}(\lambda)}{\lambda}
=\frac13\int_{-U_*}^{U_*}\sqrt{g(u)}\,du
=C_{\mathrm{out}}>0.
\]
Dividing the inner and outer leading terms proves the limiting area fraction.

## Verification

The accompanying standalone standard-library script `verify.py` reconstructs both area quadratures from their defining polynomial discriminants, locates the moving turning heights by bisection, and evaluates integrals using composite Simpson quadrature. Executing `python3 verify.py` produces `CHECK_OK`. It checks the zero-parameter circle areas, the small-damping coefficient, the large-damping renormalized constant, and the leading outer area and ratio; its numerical comparisons are finite illustrations, not an infinite-limit proof. In particular, at the moderate test value \(\lambda=300\), the renormalized inner constant is approximately \(4.8951958\), versus the proved limit \(5+2\log(243/256)\approx4.8957680\).

## Relationship to prior work

Grin and Schneider [1] constructed and proved the two specified algebraic boundaries, showed they form a Poincaré–Bendixson annulus for every \(\lambda>0\), and established their dynamical crossing properties. Their earlier van der Pol work [2] supplies the predecessor outer oval. Those results are not new here. The present statement evaluates the Euclidean **areas of the already-defined boundaries**, their sharp singular expansion, and the asymptotic annulus area fraction; the two-endpoint logarithmic correction is not supplied by the original boundary construction. Li, Grin, and Kuzmich [3] subsequently constructed improved boundaries, a separate reason that quantitative comparison of bounding-region geometry is natural. The abstract of [3] was available, but its full text could not be inspected; priority comparison with any unpublished or inaccessible area calculation remains incomplete.

## Limitations

These are properties of the **specific 2023 algebraic certificate ovals**, not of all trapping annuli and not of the Rayleigh limit cycle itself. The limiting fraction measures relative *enclosed areas*, not Hausdorff distance, period, amplitude error, or the actual occupied area of the invariant orbit. No claim is made about the best possible trapping annulus, the monotonicity of the area fraction at intermediate damping, or the behavior of the improved 2024 construction. The numerical value of \(C_{\mathrm{out}}\) is approximate; the integral definition is exact. Independent verification of publication priority remains desirable, particularly for the inaccessible full text of [3].

## References

[1] A. Grin and K. R. Schneider, “Global algebraic Poincaré–Bendixson annulus for the Rayleigh equation,” *Electronic Journal of Qualitative Theory of Differential Equations* (2023), no. 35, 1–12, DOI: 10.14232/ejqtde.2023.1.35. Public PDF: https://real.mtak.hu/185166/1/p10296.pdf. First public appearance stated in PDF: 2023-08-16.

[2] A. Grin and K. R. Schneider, “Global algebraic Poincaré–Bendixson annulus for the van der Pol equation,” WIAS Preprint 2864 (2021), DOI: 10.20347/WIAS.PREPRINT.2864, https://www.wias-berlin.de/preprint/2864/wias_preprints_2864.pdf.

[3] Y. Li, A. A. Grin, and A. V. Kuzmich, “Specified global Poincaré–Bendixson annulus with the limit cycle of the Rayleigh system,” *Differential Equations* 60 (2024), 736–746, DOI: 10.31857/S0374064124060023. Abstract: https://journals.rcsi.science/0374-0641/article/view/265610.
