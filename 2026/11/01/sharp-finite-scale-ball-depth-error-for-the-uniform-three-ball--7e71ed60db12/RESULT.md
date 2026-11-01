# Sharp finite-scale ball-depth error for the uniform three-ball

## Finding

Let \(B=\{x\in\mathbb R^3:\|x\|_2\le1\}\) and let \(\mu\) be normalized Lebesgue measure on \(B\). For a real testing radius \(t\ge1\), define the ball-translate depth and Tukey halfspace depth by
\[
d_t(y)=1-\sup_{z:\,y\notin z+tB}\mu(z+tB),\qquad H(y)=\inf_{G\text{ closed halfspace},\,y\in G}\mu(G).
\]
The supremum is over translated *closed* radius-\(t\) balls that exclude \(y\); tangencies are handled as suprema of strictly excluding translates. If \(r=\|y\|_2\) lies in \([0,1]\), then
\[
H(y)=\frac{2-3r+r^3}{4},\qquad
\boxed{d_t(y)-H(y)=\frac{3(1-r^2)^2}{16(t-r)}.}
\]
At the sole indeterminate pair \((t,r)=(1,1)\), the right-hand side means its continuous value zero. For \(r\ge1\), both depths are zero. The discrepancy is nonnegative and strictly positive for \(r<1\).

Its sharp *global*, finite-scale uniform error and complete equality locus are
\[
\boxed{\sup_{y\in\mathbb R^3}|d_t(y)-H(y)|=\frac34 r_t(1-r_t^2),\qquad
r_t=\frac{2t-\sqrt{4t^2-3}}3=\frac1{2t+\sqrt{4t^2-3}}.}
\]
The maximizing points are **exactly** those on the sphere \(\|y\|_2=r_t\), where \(0<r_t<1\). In particular the largest error at \(t=1\) is \(2/9\), attained at radius \(1/3\). The optimal large-radius expansion is
\[
\sup_y|d_t(y)-H(y)|=\frac{3}{16t}+\frac{3}{128t^3}+O(t^{-5})
\quad (t\to\infty),
\]
so \(3/16\) is the exact sharp leading constant in this model, not merely an upper-bound constant.

## Assumptions and scope

All distances are Euclidean in \(\mathbb R^3\). The sampling measure is *volume-uniform* on the unit three-ball, not uniform on its surface. Testing sets are arbitrary translates of the closed ball of radius \(t\ge1\), with no restrictions on centers. The supremum is over the entire ambient space, including points outside the support. This is a finite-scale theorem for the specified measure and testing shape; it does not assert a universal constant for arbitrary measures, convex supports, dimensions, or other testing bodies.

## Proof

**1. Reduction of translate optimization to one lens.** Rotational symmetry allows \(y=re_1\) with \(0\le r\le1\). Every translate \(z+tB\) excluding \(y\) has \(\|z-y\|_2>t\), and hence \(\|z\|_2>t-r\) by the triangle inequality. Conversely, centers \(z=-(t-r+\varepsilon)e_1\), for arbitrarily small \(\varepsilon>0\), exclude \(y\) and approach the distance \(D=t-r\) from the origin. The overlap of two Euclidean balls is nonincreasing with their center separation (also verified explicitly below). Thus the translation-mass supremum is the normalized volume \(L(t,r)\) of the intersection of balls of radii \(1,t\) at center separation \(D=t-r\), and \(d_t(y)=1-L(t,r)\). This limiting argument correctly respects strict exclusion and treats tangency without assuming an unattained maximizing translate.

**2. Exact three-dimensional lens.** The radical plane of the unit ball centered at zero and the radius-\(t\) ball centered at \(-De_1\) has axial coordinate
\[
x_0=\frac{t^2-1-D^2}{2D}.
\]
For \(0\le r<1\), \(t\ge1\), we have \(-1\le x_0\le r\). The intersection's slice at axial coordinate \(x\) is governed by the smaller of the squared radii \(1-x^2\) and \(t^2-(x+D)^2\). Therefore its exact volume is
\[
V=\pi\!\int_{-1}^{x_0}(1-x^2)\,dx+\pi\!\int_{x_0}^{r}\bigl(t^2-(x+D)^2\bigr)\,dx.
\]
Dividing by \(\operatorname{vol}_3(B)=4\pi/3\), evaluating both elementary integrals, and substituting \(D=t-r\) yields
\[
L(t,r)=\frac{(1+r)^2\bigl(D^2+2D(t+1)-3(t-1)^2\bigr)}{16D},\quad D=t-r.
\]
Indeed the overlap volume's derivative with respect to center separation, for \(t-1<D<t+1\), is
\[
\frac{dV}{dD}=-\frac{\pi\bigl((t+1)^2-D^2\bigr)\bigl(D^2-(t-1)^2\bigr)}{4D^2}<0,
\]
justifying the reduction in Step 1 independently of any unproved rearrangement assertion. Boundary cases follow from continuity.

**3. Comparison with the halfspace cap.** A halfspace of smallest \(\mu\)-mass that contains \(re_1\) is the outward cap \(\{x:x_1\ge r\}\), by radial symmetry. Its mass is
\[
H(r)=\frac{\pi\int_r^1(1-x^2)\,dx}{4\pi/3}=\frac{2-3r+r^3}{4}.
\]
Putting \(d_t=1-L\) and simplifying the rational polynomial gives the *exact identity*
\[
1-L(t,r)-H(r)=\frac{3(1-r^2)^2}{16(t-r)}.
\]
This is an algebraic identity, not an asymptotic approximation. At \((t,r)=(1,1)\) both depth functions vanish. For \(r>1\), the translate with center zero when \(t=1\), or a translate containing the support but avoiding \(y\) for arbitrary \(t\ge1\), shows \(d_t(y)=0\), while a separating halfspace shows \(H(y)=0\). The boundary \(r=1\) follows by continuity of the supremum or the lens geometry.

**4. Exact maximizing radius.** On \(0<r<1\), differentiation gives
\[
\frac{d}{dr}\frac{3(1-r^2)^2}{16(t-r)}
=\frac{3(1-r^2)(3r^2-4tr+1)}{16(t-r)^2}.
\]
The polynomial \(3r^2-4tr+1\) has one zero in \((0,1)\), namely \(r_t\) in the finding; its other root is at least \(1\). The derivative is strictly positive before \(r_t\) and strictly negative after it. This holds also at \(t=1\), taking the limiting endpoint. Hence \(r_t\) is the unique maximizing radius. Since \(3r_t^2-4tr_t+1=0\) implies \(t-r_t=(1-r_t^2)/(4r_t)\), substituting this relation into the gap gives \(E_t=3r_t(1-r_t^2)/4\). At \(t=1\), \(r_t=1/3\) and \(E_t=2/9\). The rationalized root has expansion \(r_t=1/(4t)+3/(64t^3)+O(t^{-5})\), giving the displayed expansion of \(E_t\).

## Verification

The included standalone \(\texttt{verify.py}\) uses Python's exact rational arithmetic to independently integrate the two lens slices and compare them with the closed form, the halfspace depth, and the asserted difference, across 304 rational parameter pairs (plus positivity and radical-plane bounds). High-precision decimal checks cover the optimizer equation, maximum-gap identity, endpoint value, sampled radial inequalities, and asymptotic coefficients. Running \(\texttt{python verify.py}\) prints **1850 passed assertions**. The finite diagnostics are not offered as an infinite proof: the analytic argument above proves all quantified claims.

## Relationship to prior work

Molchanov and Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1 (first public October 19, 2026), define translate depth, prove monotone uniform convergence toward halfspace depth for smooth dilated testing bodies, and establish the generally sharp order \(O(t^{-1})\). This theorem evaluates the *entire pointwise error*, its *global finite-\(t\) optimizer*, and the *best three-dimensional model constant*, information not supplied by that rate statement. The prior general convergence and sharpness claims are not claimed as new.

Werner and Yalikun, *Ball-convex bodies and \(L_p\) relative surface areas*, arXiv:2512.19836v1 (December 22, 2025), study related ball-floating constructions and associated surface-area measures; their stated results do not furnish this exact depth error. The geometry of two intersecting balls and elementary formulas for spherical caps are classical; originality is not asserted for those ingredients in isolation.

## Limitations

The sharp \(3/16\) constant applies solely to a volume-uniform three-ball tested against translates of Euclidean balls. It does not improve the order or imply an optimal universal constant for all admissible distributions. The all-scale result is stated for \(t\ge1\), where the large testing ball contains the support up to translation. The simplicity of the three-dimensional polynomial cap formula is essential to the displayed elementary expression. Although primary literature and related indexed results were compared, equivalent unindexed treatments of the same special configuration cannot be ruled out without independent historical review. Independent proof audit has not been performed.

## References

1. Ilya Molchanov and Stanislav Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1, October 19, 2026, https://arxiv.org/abs/2610.26108.
2. Elisabeth M. Werner and Diliya Yalikun, *Ball-convex bodies and \(L_p\) relative surface areas*, arXiv:2512.19836v1, December 22, 2025, https://arxiv.org/abs/2512.19836.
