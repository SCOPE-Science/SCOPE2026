# Apex rigidity and sharp \(L^\infty\) norms of affine projection on solid Euclidean bipyramids

## Finding
For every integer \(d\ge1\), define the solid Euclidean bipyramid
\[
D_d=\{(x,t)\in\mathbb R^d\times\mathbb R:\ |t|+\|x\|_2\le1\}.
\]
Let \(\mu_d\) be normalized Lebesgue volume on \(D_d\), and let \(P_d\) be the \(L^2(\mu_d)\)-orthogonal projection onto the space of real affine functions, acting also on \(L^\infty(\mu_d)\). Its exact operator norm is
\[
\boxed{\|P_d\|_{L^\infty\to L^\infty}=1+\frac{d+3}{2}\left(1-\frac{2}{(d+2)(d+3)}\right)^{d+2}.}
\]
The sharp norm is attained by bounded measurable data and is witnessed at the two axial tips \((0,\pm1)\). For \(d\ge2\), these are the **only** points of \(D_d\) where the absolute projection-kernel row integral has its maximum. For \(d=1\), the four signed coordinate tips are symmetric maximizing points. The worst negative value produced by projecting input data in \([0,1]\) equals exactly half the excess of the displayed norm over \(1\), and it is attained.

The norm has the sharp dimension expansion
\[
\|P_d\|_{\infty\to\infty}=\frac{d+3}{2}+\frac1{d+3}+O(d^{-2})\qquad(d\to\infty).
\]

## Assumptions and scope
The domain has ambient dimension \(d+1\), Euclidean transverse sections, unit axial and equatorial radii, and normalized **volume** measure, not boundary surface measure. Projection is onto **all affine functions** on the full body, not pointwise nearest-point projection onto the convex body. Data are real and essentially bounded; sharp witnesses can be discontinuous. Output is affine and continuous, so its essential supremum equals its supremum over the body. No mesh assumptions are imposed.

## Proof
Write random \((X,T)\sim\mu_d\). By symmetry, \(\mathbb E X=0=\mathbb E T\), mixed second moments vanish, and \(\mathbb E X_iX_j=0\) for \(i\ne j\). The cross-section at height \(t\) is the Euclidean \(d\)-ball of radius \(1-|t|\). Hence \(|T|\) has density \((d+1)(1-u)^d\) for \(0<u<1\), giving
\[
\mathbb E T^2=\frac{2}{(d+2)(d+3)},\qquad
\mathbb E(1-|T|)^2=\frac{d+1}{d+3}.
\]
A uniform point of a Euclidean \(d\)-ball of radius \(r\) has coordinate variance \(r^2/(d+2)\); therefore
\[
\mathbb E X_i^2=\frac{d+1}{(d+2)(d+3)}.
\]
Put \(a_d=(d+2)(d+3)/(d+1)\) and \(c_d=(d+2)(d+3)/2\). The exact orthogonal projection formula, verified by integrating against the affine orthogonal basis, is
\[
(P_df)(x,t)=\mathbb E\big[(1+a_d x\cdot X+c_d tT)f(X,T)\big].
\]
Thus the row integral \(\Lambda(x,t)=\mathbb E|1+a_d x\cdot X+c_d tT|\) determines \(\|P_d\|=\max_{(x,t)\in D_d}\Lambda(x,t)\). It is convex in \((x,t)\), invariant under rotations of \(x\), and even in \(t\). Since \(D_d\) is the convex hull of the two tips \((0,\pm1)\) and its equatorial sphere \(\{(x,0):\|x\|_2=1\}\), the maximum is the larger of the tip value \(A_d=\mathbb E|1+c_dT|\) and the equatorial value \(B_d=\mathbb E|1+a_dX_1|\).

For any symmetric real random variable \(Z\), \(\mathbb E|1+Z|=\mathbb E\max(1,|Z|)\). For any \(v\ge4\) and nonnegative \(s\),
\[
\max(1,s)\le\frac12\left(\sqrt v+\frac{s^2}{\sqrt v}\right),
\]
because the right side is at least \(1\) and is at least \(s\) by the arithmetic-geometric mean inequality. Taking \(Z=a_dX_1\), whose second moment is \(a_d\ge4\), yields \(B_d\le\sqrt{a_d}\). Symmetry also yields \(A_d\ge c_d\mathbb E|T|=(d+3)/2\), with strict inequality since \(\mathbb P(|T|<1/c_d)>0\). For every \(d\ge3\),
\[
\left(\frac{d+3}{2}\right)^2\ge a_d
\quad\Longleftrightarrow\quad d^2\ge5,
\]
so \(A_d>B_d\). At \(d=2\), direct evaluation gives
\[
A_2=\frac{10561}{4000}>\sqrt{20/3}\ge B_2;
\]
the strict rational comparison follows from \(3\cdot10561^2-20\cdot4000^2=14604163>0\). When \(d=1\), \(D_1\) is a diamond symmetric under exchanging the two coordinates; thus \(A_1=B_1\). Therefore \(\|P_d\|=A_d\) in every dimension. For \(d\ge2\), any point with \(|t|<1\) is a convex combination with strictly positive equatorial weight, so its row norm is strictly below \(A_d\); only the axial tips maximize.

Finally, \(|T|\) has the above beta density, so
\[
A_d=1+\int_{1/c_d}^1(c_du-1)(d+1)(1-u)^d\,du
=1+\frac{c_d}{d+2}\left(1-\frac1{c_d}\right)^{d+2},
\]
which is the claimed exact formula. At the upper tip, \(f(X,T)=\operatorname{sgn}(1+c_dT)\) attains this \(L^\infty\) norm. Each projection-kernel row has signed integral \(1\). Its negative mass is therefore \((\Lambda-1)/2\); choosing \(f=\mathbf1_{\{1+c_dT<0\}}\) at the upper tip attains the maximal negative excursion for \(0\le f\le1\). A binomial/logarithmic expansion of the displayed exact formula yields the dimension asymptotic above.

## Verification
The self-contained script `check_bicone.py` uses exact rational arithmetic for the inverse covariance, \(d=2\) comparison, and all integer-dimensional algebraic inequalities through \(d=50\). It independently samples \(40,000\) normalized-volume points in each of seven dimensions \(d=1,2,3,4,5,8,12\) and compares the sampled apex and equatorial row integrals to the closed form. All checks passed. This is numerical corroboration of an analytic proof; finite checks are not a proof of all dimensions, all signals or uniqueness.

## Relationship to prior work
Orthogonal-projection stability in approximation theory motivates finding sharp cellwise norm constants. In particular, Gawlik and Lew (arXiv:1408.4104; subsequent DOI 10.1051/m2an/2014045) study **differences of finite-element projections on nearby meshes** using uniform stability and approximation estimates. Their Theorems 2.1, 2.2 and 2.4 do not calculate the single-domain endpoint norm on \(D_d\). Grigorieff and Sloan study discrete spline projections rather than solid bipyramid volume projectors. Earlier exact affine projection calculations for one-sided cones, simplices and cross-polytope face/surface measures use different domains or measures, and the associated constants do not specialize to the present full-volume bicone result. A fully exhaustive historical literature search is not claimed.

## Limitations
No exact \(L^p\) norm for intermediate \(p\), higher polynomial degree, arbitrary ellipsoidal/nonhomothetic sections, or nonuniform volume density is asserted. The result is a sharp endpoint operator norm, not an optimal norm among all projections onto affine functions. A prior implicit derivation using general convex-body projector kernels remains possible.

## References
- E. S. Gawlik and A. J. Lew, “Supercloseness of orthogonal projections onto nearby finite element spaces”, first public arXiv:1408.4104 (18 August 2014); ESAIM: M2AN **49** (2015), 559–576, DOI: 10.1051/m2an/2014045.
- R. D. Grigorieff and I. H. Sloan, “Stability of discrete orthogonal projections for continuous splines”, *Bulletin of the Australian Mathematical Society* **58** (1998), 307–332, DOI: 10.1017/S0004972700032263.
- M. Crouzeix and V. Thomée, “The stability in \(L^p\) and \(W^{1,p}\) of the \(L^2\)-projection onto finite element function spaces”, *Mathematics of Computation* **48** (1987), 521–532, DOI: 10.2307/2007825.
