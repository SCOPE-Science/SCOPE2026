# Two chord moments reconstruct hollow Euclidean balls, with a sharp dimension-six ambiguity threshold

## Finding
For an integer \(d\ge2\), an outer radius \(R>0\), and an inner radius \(0<r<R\), let
\[
H_d(r,R)=\{x\in\mathbb R^d:r\le\|x\|_2\le R\}.
\]
Let \(X,Y\) be independent points uniform under normalized \(d\)-dimensional Lebesgue volume on this **solid annulus** (not on either boundary sphere), and put \(D=\|X-Y\|_2\), \(\mu_2=\mathbb E[D^2]\), \(\mu_4=\mathbb E[D^4]\), \(q=r/R\), and \(\kappa=\mu_4/\mu_2^2\). Define
\[
F_d(q)=\frac12+\frac1d+\frac{(d+2)^2}{2d(d+4)}
\frac{(1-q^d)(1-q^{d+4})}{(1-q^{d+2})^2}.
\]
Then \(\kappa=F_d(q)\) and \(F_d\) is **strictly decreasing** for every \(0<q<1\). Its exact image is
\[
\boxed{I_d=\left(1+\frac1d,\ 1+\frac1d+\frac{2}{d(d+4)}\right).}
\]
Consequently, if \(d\) is known, \(\mu_2>0\) and \(\kappa\in I_d\) are necessary and sufficient for such a shell, and the two moments recover its unique ordered radii via the unique solution \(q\in(0,1)\) of \(F_d(q)=\kappa\) and
\[
\boxed{R^2=\frac{\mu_2(d+2)(1-q^d)}{2d(1-q^{d+2})},\qquad r=qR.}
\]
One moment does not suffice, since varying \(q\) and rescaling \(R\) preserves \(\mu_2\).

There is also a sharp **dimension-identification transition** if \(d\) is not given. A shell in dimension \(d\in\{2,3,4,5\}\) is unambiguously identified by its two moments even among shells in arbitrary integer dimensions at least two. For every \(d\ge6\) there exist shells in dimensions \(d\) and \(d+1\) with exactly the same \((\mu_2,\mu_4)\). More precisely, consecutive dimension intervals overlap exactly when \(d\ge6\), in which case
\[
\boxed{I_d\cap I_{d+1}=\left(1+\frac1d,\ 1+\frac1{d+1}+\frac{2}{(d+1)(d+5)}\right)}
\]
and their overlap length is exactly \((d-5)/[d(d+1)(d+5)]\). At the borderline \(d=5\) the open intervals touch only in their unattainable endpoints. For a concrete collision between the first ambiguous dimensions, \(\kappa=146/125\) belongs to both \(I_6=(7/6,6/5)\) and \(I_7=(8/7,90/77)\). For each of \(d=6,7\), solve \(F_d(q_d)=146/125\) and choose \(R_d\) by the displayed reconstruction formula with \(\mu_2=1\); both resulting hollow balls then have exactly \((\mu_2,\mu_4)=(1,146/125)\), despite having different dimensions.

Finally the inverse problem has two different sharp degeneracy exponents. As \(q\downarrow0\) and \(q\uparrow1\), respectively,
\[
\boxed{F_d(0)-F_d(q)=\frac{(d+2)^2}{2d(d+4)}q^d+O(q^{d+2}),}
\]
\[
\boxed{F_d(q)-\left(1+\frac1d\right)=\frac{(1-q)^2}{6}+O((1-q)^3).}
\]
Here \(F_d(0)\) denotes the full-ball limit. Thus the optimal local inverse Hölder exponents for the *radius ratio* are \(1/d\) at a vanishing hole and \(1/2\) at the thin-shell limit. For each fixed \(d\ge2\) there is also a finite constant \(C_d\) such that
\[
|q_1-q_2|\le C_d|F_d(q_1)-F_d(q_2)|^{1/d}\quad(0<q_1,q_2<1),
\]
and its exponent cannot be increased uniformly.

## Assumptions and scope
All inner and outer radii are strictly positive and distinct. The geometry is the concentric hollow **volume** of the two Euclidean balls; it is generally not convex. Pairwise distances use the ambient Euclidean metric, not an intrinsic shortest path that must avoid the hole. \(\mu_2,\mu_4\) are exact population moments of the distance between two independent points. Every dimension statement quantifies over the positive integers \(d\ge2\). The limits \(q=0\) (solid ball) and \(q=1\) (zero-volume boundary sphere) are used only to describe sharp endpoint behavior and are not additional members of the class.

## Proof
**1. Moments from radial symmetry.** Write \(S=\|X\|_2\) and \(u=\mathbb E[S^2]\), \(v=\mathbb E[S^4]\). Radial polar coordinates give, for every real \(j>-d\),
\[
\mathbb E[S^j]=\frac{d}{d+j}\frac{R^{d+j}-r^{d+j}}{R^d-r^d}.
\]
Since \(X,Y\) are independent, centered, and rotationally invariant, \(\mathbb E[X_iX_j]=(u/d)\delta_{ij}\). Expanding the powers of \(\|X-Y\|_2^2=\|X\|_2^2+\|Y\|_2^2-2X\cdot Y\) gives
\[
\mu_2=2u,\qquad \mu_4=2v+\left(2+\frac4d\right)u^2.
\]
Indeed the terms linear in \(X\cdot Y\) vanish, and \(\mathbb E[(X\cdot Y)^2]=u^2/d\). Therefore \(\kappa=(v/u^2)/2+1/2+1/d\). Substituting the radial moments proves the displayed formula for \(F_d(q)\) and the reconstruction formula for \(R\).

**2. Strict global monotonicity.** Let \(q=e^{-s}\), \(s>0\), and set
\[
A_d(s)=\frac{(1-e^{-ds})(1-e^{-(d+4)s})}{(1-e^{-(d+2)s})^2}
=\frac{\sinh(ds/2)\sinh((d+4)s/2)}{\sinh^2((d+2)s/2)}.
\]
For fixed \(s>0\), the function \(\phi_s(x)=x\coth(sx/2)\) is strictly convex for \(x>0\). Indeed the second derivative of \(h(y)=y\coth y\) is
\[
h''(y)=\frac{2(y\cosh y-\sinh y)}{\sinh^3y}>0\qquad(y>0),
\]
since the numerator starts at zero and has derivative \(y\sinh y>0\). Consequently,
\[
\frac{d}{ds}\log A_d(s)=\frac12[\phi_s(d)+\phi_s(d+4)-2\phi_s(d+2)]>0.
\]
Thus \(A_d(s)\) strictly increases with \(s\), so \(F_d(q)\) strictly decreases with \(q=e^{-s}\). Its limits at \(q=0\) and \(q=1\) are, respectively, \(1+1/d+2/[d(d+4)]\) and \(1+1/d\). Continuity and strict monotonicity prove both the exact interval and unique solvability. Given a feasible \(\mu_2\), the formula for \(R\) gives a positive finite radius and hence sufficiency.

**3. Dimension-six threshold.** Denote the lower and upper endpoints of \(I_d\) by \(L_d\) and \(U_d\). Both decrease strictly with integer \(d\). Hence the intersection of consecutive intervals, if nonempty, is exactly \((L_d,U_{d+1})\). The endpoints satisfy the exact identity
\[
U_{d+1}-L_d=\frac{d-5}{d(d+1)(d+5)}.
\]
The intervals are disjoint for \(d\le5\), including at the zero-gap case since both are open. Decreasing endpoints imply that the intervals of each \(d\le5\) are disjoint from every other dimension, not merely its neighbors. For every \(d\ge6\), choose any \(\kappa\) in the positive-length intersection. Strict invertibility gives unique ratios in each dimension; choosing the respective outer radii to make the same arbitrary \(\mu_2>0\) makes both \(\mu_2\) and \(\mu_4=\kappa\mu_2^2\) coincide. This proves the ambiguity and the exact overlap length.

**4. Sharp inverse exponents.** At \(q=0\), expand the rational expression: \((1-q^d)(1-q^{d+4})/(1-q^{d+2})^2=1-q^d+O(q^{d+2})\), valid for all \(d\ge2\). This yields the first asymptotic formula. For \(q=1-h\) with \(h\downarrow0\), the squared radius \(S^2/R^2\) lies in \([(1-h)^2,1]\). Its density is smooth and bounded relative to a uniform density as \(h\to0\); after linear rescaling of that interval it converges to the uniform law with moment error \(O(h)\). Hence
\[
\operatorname{Var}(S^2/R^2)=\frac{h^2}{3}+O(h^3),\quad
\mathbb E[S^2/R^2]=1+O(h).
\]
The identity \(v/u^2=1+\operatorname{Var}(S^2)/u^2\) yields the second asymptotic formula. Neither exponent can be enlarged, since its positive leading coefficient is exact.

For the global Hölder statement, write \(f=F_d\). The strictly positive function \(-f'(q)/[q^{d-1}(1-q)]\) extends continuously and positively to \([0,1]\), by the two endpoint expansions and smoothness of the rational formula on \((0,1)\). It therefore has a positive minimum. Splitting any interval \([a,b]\) at \(1/2\) and integrating \(q^{d-1}(1-q)\) on the resulting subintervals gives \(\int_a^b q^{d-1}(1-q)\,dq\ge c_d(b-a)^d\) for a positive \(c_d\) depending only on \(d\), since \(d\ge2\). Thus \(f(a)-f(b)\ge c'_d(b-a)^d\) for \(a<b\), proving the stated inverse bound; its exponent is optimal at \(q\downarrow0\).

## Verification
Run `python3 verify.py` with the standard Python library. The program executes 2,122 checks, including exact rational monotonic grids and endpoint identities for dimensions \(2\) through \(25\), exact dimension-overlap algebra through dimension \(59\), rational inversion checks, and independently generated Euclidean point-pair simulations in six dimensions/parameter choices (270,000 pairs total). Its deterministic output begins `VERIFY_OK 2122 exact_rational_and_independent_sample_checks`. The infinite-dimensional quantifiers, injectivity, and optimal exponents are proved analytically above, not by finite testing.

## Relationship to prior work
Tu and Fischbach (first publicly posted January 22, 2002) derive forward random-distance distributions in arbitrary dimensions for spherical regions with general radial densities, as well as full-ball distance moments and multilayer models. Their general formulas supply prior forward theory covering the present sampling model, but they do not state the specific two-moment injectivity, the dimension-six aliasing interval, or the two optimal degeneracy exponents. The forward identity is not claimed as a new general theory. Hong and Hong (2014) address moments of inertia of solid spheres and shells; these second-moment techniques do not themselves establish a fourth-distance-moment inverse classification. A published exact straight-segment visibility law for concentric shells studies a different two-point functional: whether the *connecting segment stays in the shell*, rather than its Euclidean length moments. Spherical-surface-cap and lune distance laws concern sampling on surfaces instead of in hollow volumes. In particular, the dimension-six interval-overlap theorem is not an immediate corollary of those other observation models.

## Limitations
The classification is conditional on equal-volume sampling from a perfectly concentric and homogeneous hollow region. Unknown nonuniform radial densities, displaced holes, anisotropic shells, noisy finite-sample moments, or unknown sampling procedures may produce nonidentifiability not addressed here. The result establishes mathematical injectivity and deterministic Hölder limits, not statistical estimation rates or independently certified historical priority. The original full text of Hong and Hong (2014) was not available for comparison; its accessible abstract addresses inertia rather than the inverse two-distance-moment threshold. Results not indexed by the consulted literature sources may still overlap historically.

## References
1. S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046v1, January 22, 2002, https://arxiv.org/abs/math-ph/0201046.
2. S.-I. Hong and S.-C. Hong, *Moments of inertia of spheres without integration in arbitrary dimensions*, European Journal of Physics **35** (2014), 025003, https://doi.org/10.1088/0143-0807/35/2/025003.
3. *Exact visibility laws for concentric spherical shells in odd dimensions*, publicly available research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-visibility-laws-for-concentric-spherical-shells-in-odd-dim--611519ee4958.
