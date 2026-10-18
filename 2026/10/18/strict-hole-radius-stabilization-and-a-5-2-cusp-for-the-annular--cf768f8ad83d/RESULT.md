# Strict hole-radius stabilization and a \(5/2\)-cusp for the annular affine projector

## Finding

For \(0\le r<1\), let \(A_r=\{x\in\mathbb R^2:r\le\|x\|_2\le1\}\), with normalized planar area probability measure \(\mu_r\). Let \(P_r:L^2(\mu_r)\to\operatorname{span}\{1,x_1,x_2\}\) be orthogonal projection, regarded also as a bounded operator on \(L^1(\mu_r)\) and \(L^\infty(\mu_r)\). For \(R\ge0\), \(b>0\), put
\[
H(R,b)=\begin{cases}
0,&R\le b,\\
\displaystyle\frac{2R^2+b^2}{3}\sqrt{R^2-b^2}-bR^2\arccos(b/R),&R>b.
\end{cases}
\]
Write \(b_r=(1+r^2)/4\). The common sharp endpoint norm is
\[
\boxed{\Lambda(r):=\|P_r\|_{1\to1}=\|P_r\|_{\infty\to\infty}
=1+\frac{2\bigl(H(1,b_r)-H(r,b_r)\bigr)}{\pi b_r(1-r^2)}.}
\]
The function \(\Lambda\) is continuous on \([0,1]\) after its natural boundary-circle extension, **strictly decreasing** on \([0,1]\), and real analytic on each of \((0,r_*)\) and \((r_*,1)\), where \(r_*=2-\sqrt3\). At the interior threshold it is exactly twice continuously differentiable, but is not three times continuously differentiable. More precisely, with the real-analytic function
\[
B(r)=1+\frac{2H(1,b_r)}{\pi b_r(1-r^2)}
\]
defined near \(r_*\),
\[
\boxed{\Lambda(r)=B(r)-D(r-r_*)_+^{5/2}+O((r-r_*)_+^{7/2}),\qquad
D=\frac{4\,3^{5/4}}{15\pi\sqrt{r_*}(1-r_*^2)}>0.}
\]
The two endpoint values are
\[
\Lambda(0)=\frac{11\sqrt{15}}{8\pi}+\frac2\pi\arcsin\frac14,
\qquad
\Lambda(1)=\lim_{r\uparrow1}\Lambda(r)=\frac13+\frac{2\sqrt3}{\pi}.
\]
The singularity is the precise first contact of the negative region of a norm-extremizing reproducing kernel with the moving inner circular boundary.

## Assumptions and scope

All radii are real. The disk at \(r=0\) is included; the degenerate circle at \(r=1\) is **only a limiting boundary-measure operator**, not the normalized area measure. The polynomial space consists of the three real affine coordinate functions, with complex scalar extension allowed. Endpoint operator norms use the **same** normalized area measure in domain and codomain. No assertion is made about higher polynomial degree, an off-center hole, nonconcentric lakes, or nonuniform weights.

## Proof

### Reproducing kernel and sharp endpoint reduction

Rotation symmetry gives \(\mathbb E_{\mu_r}x=0\) and \(\mathbb E_{\mu_r}x_ix_j=\delta_{ij}(1+r^2)/4\). Consequently the reproducing kernel is
\[
K_r(x,y)=1+\frac4{1+r^2}x\cdot y=1+\frac{x\cdot y}{b_r}.
\]
For an evaluation point \(x\), the Lebesgue function is \(L_r(x)=\int_{A_r}|K_r(x,y)|\,d\mu_r(y)\). By rotation symmetry it depends only on \(\|x\|_2\). Along each radial ray it is even and convex in the signed radial variable (an integral of absolute values of affine functions). It is therefore nondecreasing in nonnegative radius, so its supremum on the closed annulus is the value at any unit outer-boundary point. Continuity makes this boundary supremum equal the essential supremum on \(A_r\). Kernel symmetry and duality give equality of the \(L^1\) and \(L^\infty\) operator norms, and measurable kernel-sign inputs approximate the sharp value.

At \(x=(1,0)\), the kernel is negative precisely when \(y_1<-b_r\). Its mean is one. Thus
\[
\Lambda(r)=1+\frac2{\pi(1-r^2)b_r}\int_{A_r}(-b_r-y_1)_+\,dy.
\]
For a disk of radius \(R\), the integral of \((-b-y_1)_+\) is
\[
H(R,b)=2\int_b^R(z-b)\sqrt{R^2-z^2}\,dz
\]
when \(R>b\), and zero otherwise. An elementary antiderivative yields the displayed closed formula for \(H\). Subtract the inner disk from the outer disk to obtain the exact endpoint norm. The negative region touches the inner circle exactly when \(r=b_r\), whose only solution in \((0,1)\) is \(r_*=2-\sqrt3\).

### Strict monotonicity under growth of the hole

Put \(s=r^2\), let \(U\) be uniform on \([0,1]\), and let \(\Theta\) be uniform on \([0,2\pi]\), independently. Area sampling has radius \(\sqrt{s+(1-s)U}\). Set
\[
c_s(u)=\frac{4\sqrt{s+(1-s)u}}{1+s},\qquad
G(c)=\begin{cases}0,&0\le c\le1,\\
\sqrt{c^2-1}-\arccos(1/c),&c>1.
\end{cases}
\]
Angular integration gives \(\mathbb E_{\Theta}|1+c\cos\Theta|=1+(2/\pi)G(c)\). Hence
\[
\Lambda(\sqrt s)=1+\frac2\pi\int_0^1G(c_s(u))\,du.
\]
The derivative \(G'(c)=0\) for \(c\le1\), and \(G'(c)=\sqrt{1-c^{-2}}\) for \(c>1\). It is nonnegative and nondecreasing in \(c\). For \(0<s<1\),
\[
\partial_sc_s(u)=\frac{2\bigl(1-s-(3-s)u\bigr)}{(1+s)^2\sqrt{s+(1-s)u}}.
\]
This derivative is positive below \(u_s=(1-s)/(3-s)\) and negative above it. Since \(c_s(u)\) is increasing in \(u\), the weight \(w_s(u)=G'(c_s(u))\) is nondecreasing. Thus
\[
\int_0^1w_s(u)\partial_sc_s(u)\,du
\le w_s(u_s)\int_0^1\partial_sc_s(u)\,du.
\]
Moreover \(c_s(u_s)=4/\sqrt{(1+s)(3-s)}\ge2\), so \(w_s(u_s)>0\), whereas
\[
\int_0^1c_s(u)\,du=\frac83\frac{1+r+r^2}{(1+r)(1+r^2)},
\quad
\frac{d}{dr}\frac{1+r+r^2}{(1+r)(1+r^2)}
=-\frac{r^2(r^2+2r+3)}{(1+r)^2(1+r^2)^2}<0
\]
for \(0<r<1\). Differentiating the angular integral is justified by boundedness of \(G'\) and integrability of \(\partial_sc_s\) for positive \(s\). It follows that \(\Lambda\) is strictly decreasing for \(0<r<1\); continuity at zero gives strict decrease on the closed interval including the limiting circle.

### Sharp regularity at tangency

For \(r\le r_*\), \(H(r,b_r)=0\), so \(\Lambda(r)=B(r)\). For \(r>r_*\), write \(\delta=r-b_r>0\). The cap integral gives, uniformly as \(\delta\downarrow0\),
\[
H(r,b_r)=2\int_0^\delta t\sqrt{(\delta-t)(2b_r+\delta+t)}\,dt
=\frac{8\sqrt{2b_r}}{15}\delta^{5/2}+O(\delta^{7/2}).
\]
Since \(\delta=(\sqrt3/2)(r-r_*)+O((r-r_*)^2)\) and \(b_{r_*}=r_*\), substituting into the norm expression gives the stated \(D\), with a \(7/2\)-order remainder. Upon setting \(t=\delta v\), the cap integral becomes \(\delta^{5/2}\) times a function analytic in \(\delta\) near zero; hence this expansion may be differentiated term by term on the right. Differentiation shows
\[
\Lambda'''(r)=B'''(r)-\frac{15D}{8}(r-r_*)^{-1/2}+O((r-r_*)^{1/2}),
\qquad r\downarrow r_*.
\]
The left branch is analytic. The singular term therefore proves \(\Lambda\in C^2\) locally at \(r_*\), but \(\Lambda\notin C^3\) there.

### Endpoints

For \(r=0\), substitute \(b_0=1/4\) into the cap formula and use \(\arccos(1/4)=\pi/2-\arcsin(1/4)\). For \(r\uparrow1\), radius converges to one in the radial sampling representation while \(c_s(u)\to2\). Angular integration gives \(\mathbb E|1+2\cos\Theta|=1/3+2\sqrt3/\pi\). Both limits are exact.

## Verification

The included `checker.py` (standard Python only) independently evaluates the cap integral by quadrature, compares the closed endpoint norm to a two-dimensional angular/radial midpoint integral, checks interior evaluation bounds at representative radii, samples strict monotonicity, and checks the positive \(5/2\)-cusp coefficient. Run `python3 checker.py`; its test assertions are finite consistency checks, not substitutes for the universal proof. The exact integration and monotonicity argument above do not depend on numerical experiments.

## Relationship to prior work

Saff, Stahl, Stylianopoulos and Totik [1] treat area-orthogonal polynomials on domains with holes, chiefly asymptotic comparisons and image reconstruction, without a sharp degree-one endpoint norm or a radius-dependent boundary-contact regularity theorem. Hangelbroek, Narcowich, Sun and Ward [2] establish general stability results for kernel least-squares projectors on manifolds, not the concentric area-annulus endpoint formula. Classical disk and circle endpoint evaluations are recovered here and are not claimed as new in isolation. The asserted contribution is their interpolation by a sharp strictly monotone annular stability profile, together with the exact nonanalytic tangency transition at the intrinsic radius \(2-\sqrt3\).

## Limitations

The result is an explicit theorem for **concentric** circular holes and affine degree one only; it does not imply analogous monotonicity or regularity for arbitrary holes, higher-degree polynomial projectors, or other spatial dimensions. The comparative literature search is not a historical uniqueness proof; a differently formulated earlier result may exist. No independent verification of mathematical priority is claimed.

## References

[1] E. B. Saff, H. Stahl, N. Stylianopoulos and V. Totik, *Orthogonal polynomials for area-type measures and image recovery*, arXiv:1403.6456, first publicly posted 2014-03-25, https://arxiv.org/abs/1403.6456 .

[2] T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424, first publicly posted 2010-05-13, https://arxiv.org/abs/1005.2424 .
