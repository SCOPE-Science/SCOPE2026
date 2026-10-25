# Exact curvature phase transition for exponential generalized-parabolic starlikeness

## Finding

Let \(\mathcal S_e^*\) be the normalized starlike class characterized by \(zf'(z)/f(z)\prec e^z\). For \(\alpha>0\), put
\[
\mathcal P_\alpha=\{u+iv\in\mathbb C:v^2<4\alpha(u-1/2)\},
\]
and let \(R_\alpha\) be the largest \(R\in(0,1]\) such that every \(f\in\mathcal S_e^*\), rescaled as \(f(Rz)/R\), satisfies \(Rzf'(Rz)/f(Rz)\in\mathcal P_\alpha\) for all \(|z|<1\). Define
\[
L=\log2,\qquad \alpha_*={\log2\over4(1-\log2)}=0.5647228383\ldots.
\]
Then
\[
\boxed{R_\alpha=\log2\ \Longleftrightarrow\ \alpha\ge\alpha_*,\qquad R_\alpha<\log2\ \ (0<\alpha<\alpha_*).}
\]
Thus the sharp exponential generalized-parabolic radius has an exact curvature phase transition: above the threshold the first obstruction is the negative-real-axis contact \(e^{-L}=1/2\), while below the threshold an off-axis contact necessarily occurs earlier. No exact formula for \(R_\alpha\) below the threshold is asserted.

## Assumptions and scope

Here \(\mathcal S_e^*\) consists of normalized analytic functions \(f(0)=0,f'(0)=1\) whose logarithmic derivative is subordinate to \(e^z\) on the unit disk. Since \(e^{\mathbb D}\) lies in the right half-plane, this implies starlikeness and univalence. The target is the \(\beta=1/2\) slice of the generalized parabolic domains \(\mathcal{ST}_p(\alpha,\beta)\), namely the strict inequality \((\Im w)^2<4\alpha(\Re w-1/2)\).

A subordination \(zf'/f=e^{\omega(z)}\) with \(\omega(0)=0\), \(|\omega(z)|<1\), implies \(|\omega(Rz)|\le R|z|\). Conversely the canonical function
\[
f_e(z)=z\exp\!\left(\int_0^z{e^t-1\over t}\,dt\right)
\]
has \(zf_e'(z)/f_e(z)=e^z\), so testing the disk \(e^{R\mathbb D}\) yields the exact universal radius.

## Proof

**Sharp upper obstruction.** For any \(R>L\), the point \(z=-L/R\) belongs to the open unit disk and \(e^{Rz}=1/2\notin\mathcal P_\alpha\). Thus \(R_\alpha\le L\) for every \(\alpha>0\).

**Necessity of the threshold.** On the radius-\(L\) circle consider \(z_y=-\sqrt{L^2-y^2}+iy\). For
\[
F_\alpha(x,y)=4\alpha(e^x\cos y-1/2)-e^{2x}\sin^2y,
\]
a direct Taylor expansion at \(y=0\) gives
\[
F_\alpha(\Re z_y,y)
=\left({\alpha(1-L)\over L}-{1\over4}\right)y^2+O(y^4).
\]
For \(\alpha<\alpha_*\), this is negative for all sufficiently small nonzero \(y\). By continuity, points strictly inside \(|z|<L\) also violate the target inequality, so the sharp radius is strictly below \(L\).

**Sufficiency at the threshold.** It remains to prove \(F_{\alpha_*}(x,y)>0\) for \(x^2+y^2<L^2\). First establish nonnegativity on the closed disk. Write \(q=e^x\), \(U=y^2\) and \(0\le U\le Y=L^2-x^2\). The alternating Taylor bounds valid for \(|y|\le L<0.7\) are
\[
\cos y\ge1-U/2+U^2/24-U^3/720,\quad
\sin^2y\le U-U^2/3+2U^3/45.
\]
They imply
\[
F_{\alpha_*}(x,y)\ge H(U,x)
=4\alpha_*(q-1/2)-(2\alpha_*q+q^2)U
 +(\alpha_*q/6+q^2/3)U^2
 -(\alpha_*q/180+2q^2/45)U^3.
\]
For \(0\le U\le L^2<0.482\),
\[
\partial_U H\le\alpha_*q(-2+U/3)+q^2(-1+2U/3)<0.
\]
Consequently \(H(U,x)\ge H(Y,x)\). Set \(t=x+L\in[0,2L]\), \(Y=t(2L-t)\), so that \(q=e^t/2\). Then
\[
H(Y,x)=\alpha_*\big[(2-Y+Y^2/12-Y^3/360)e^t-2\big]
 -(Y/4-Y^2/12+Y^3/90)e^{2t}.
\]
Both polynomial prefactors of the exponentials are nonnegative on the indicated interval, and the first is strictly positive. Introduce rational Taylor polynomials
\[
E_1(t)=\sum_{j=0}^{10}{t^j\over j!},\quad
E_2(t)=\sum_{j=0}^{12}{(2t)^j\over j!}+21{(2t)^{13}\over13!}.
\]
Since \(0\le 2t<3\) and \(e^3<21\), Taylor's theorem gives \(E_1(t)\le e^t\) and \(e^{2t}\le E_2(t)\). Thus
\[
H(Y,x)\ge P(t,L)=\alpha_*[(2-Y+Y^2/12-Y^3/360)E_1(t)-2]
 -(Y/4-Y^2/12+Y^3/90)E_2(t).
\]
An exact rational-polynomial certificate verifies that \(Q(t,L)=(1-L)P(t,L)/t^2\) is a polynomial of degree \(17\) in \(t\), and for all \(693/1000\le L\le694/1000\), \(0\le t\le1388/1000\), its constant coefficient is greater than \(0.0468\), while the total possible negative contribution of all other coefficients is less than \(0.00023\). Hence \(Q(t,L)>0.04657\) whenever \(t\ge0\). The provided exact-rational checker constructs \(Q\), verifies coefficient-interval enclosures and the elementary bound \(693/1000<\log2<694/1000\), without numerical optimization. Thus \(P(t,L)>0\) for \(t>0\); at \(t=0\) the disk condition forces \(x=-L,y=0\) and equality \(F_{\alpha_*}=0\). Therefore \(e^{L\mathbb D}\subset\mathcal P_{\alpha_*}\), proving \(R_{\alpha_*}=L\).

**Monotonicity in curvature.** The established inequality at \(\alpha_*\) entails \(e^x\cos y-1/2\ge0\) on the closed \(L\)-disk (strict except at the leftmost point). Consequently \(F_\alpha\ge F_{\alpha_*}\ge0\) for all \(\alpha\ge\alpha_*\), with strict containment on \(|z|<L\). Together with the universal upper obstruction this proves the theorem.

## Verification

Run `python artifacts/check_certificate.py` with Python 3 and SymPy. It uses exact rational arithmetic to establish the logarithm enclosure, the polynomial identity, the signs of interval-enclosed coefficients and the final strict positivity margin. The checker does not replace the analytic Taylor, monotonicity and sharpness steps described above. The proof is an infinite-disk inclusion theorem, not a conclusion inferred from finite sampling.

## Relationship to prior work

Lecko, Madhumitha and Ravichandran (published October 5, 2026) introduce the two-parameter generalized-parabolic target and investigate sharp radii for Janowski starlike and several ratio-defined classes. Their inspected results do not cover the exponential class or the exact curvature plateau asserted here. The recent *Geometric Function Atlas* frames directed class-radius questions, without this target pair. A published October 2026 result, *Exact uniform-convexity phase boundary for exponentially convex functions*, proves the sharp classical parabolic radius \(0.6905440336\ldots\) at the **single** parameter \(\alpha=1/2\), including its off-axis obstruction. The present statement neither reclaims that case nor follows from its fixed-parameter optimization: it identifies and proves the exact transition to the real-axis-controlled regime for all larger curvature parameters.

## Limitations

The statement fixes the parabola's horizontal intercept \(\beta=1/2\) and proves an exact **plateau threshold** rather than the complete function \(R_\alpha\) below it. The certificate uses a deliberately coarse rational Taylor enclosure; its numerical margins are proof devices, not optimized bounds. Independent review and priority verification remain outstanding. Although direct literature and recorded-result comparisons found no stronger encompassing theorem, equivalent statements under another parameterization cannot be ruled out exhaustively.

## References

1. A. Lecko, S. Madhumitha and V. Ravichandran, *Radius of generalized parabolic starlikeness*, Boletín de la Sociedad Matemática Mexicana 32 (2026), article 131; DOI 10.1007/s40590-026-00962-6, publicly published 2026-10-05.
2. *Geometric Function Atlas: Using What We Know About Radius Problems to Solve New Ones*, arXiv:2608.15697, first submitted 2026-08-16.
3. *Exact uniform-convexity phase boundary for exponentially convex functions*, published-finding corpus, publicly available 2026-10-04, `2026/10/4/SCOPE-exact-uniform-convexity-phase-boundary-for-exponentially-convex--8b684117a07f`.
4. W. C. Ma and D. Minda, *Uniformly convex functions*, Annales Polonici Mathematici 57 (1992), 165–175; F. Rønning, *Uniformly convex functions and a corresponding class of starlike functions*, Proceedings of the AMS 118 (1993), 189–196.
