# Rectangular-constant phase transition in planar Lorentz preduals
## Finding
For every \(0<w<1\), let \(X_w=(\mathbb R^2,N_w)\) be the real two-dimensional Lorentz-predual plane with
\[
N_w(u,v)=\max\left\{|u|,|v|,\frac{|u|+|v|}{1+w}\right\}.
\]
Its classical Joly rectangular constant
\[
\mu(X_w)=\sup_{\substack{x,y\in S_{X_w},\ x\perp_B y\\ t\ge0}}
\frac{1+t}{N_w(x+t y)}
\]
has the exact phase diagram
\[
\mu(X_w)=1+2\max\left\{w,\frac{1-w}{1+w}\right\}
=\begin{cases}
\dfrac{3-w}{1+w},&0<w\le\sqrt2-1,\\[2mm]
1+2w,&\sqrt2-1\le w<1.
\end{cases}
\]
Consequently the unique parameter minimizing \(\mu(X_w)\) is \(w=\sqrt2-1\), the Euclidean-regular octagonal member, and the minimum is \(2\sqrt2-1\). Complete normalized maximizing triples \((x,y,t)\) are as follows, up to a common signed-coordinate permutation. If \(0<w<\sqrt2-1\), the only type is
\[
x=(1,w),\quad y=\left(-\frac{1+w}{2},\frac{1+w}{2}\right),\quad t=\frac{2(1-w)}{1+w}.
\]
If \(\sqrt2-1<w<1\), the only type is
\[
x=(1,w),\quad y=(0,-1),\quad t=2w.
\]
At \(w=\sqrt2-1\) both displayed types maximize; these are the only two types under signed-coordinate permutations. Hence the maximizing mechanism switches from a slanted facet to an axial facet exactly at the regular-octagon threshold.

## Assumptions and scope
All vector spaces and scalar parameters are real. Birkhoff--James orthogonality means
\[
x\perp_B y\quad\Longleftrightarrow\quad N_w(x)\le N_w(x+s y)\ \text{for all }s\in\mathbb R.
\]
Write \(c=1+w\) and \(d=1-w\), so \(0<d<1<c<2\). The unit ball of \(N_w\) has eight vertices of the form \((\pm1,\pm w)\), \((\pm w,\pm1)\); its nontrivial edges are axial and diagonally slanted. We take the supremum over \(x,y\) of unit norm and \(t\ge0\), including all sign and coordinate symmetries. The theorem classifies ordered triples: no interchange of \(x,y\) is presumed to preserve Birkhoff--James orthogonality.

## Proof
A unit vector \(x\) lies in the interior of an axial edge, the interior of a slanted edge, or at a vertex. For a unit \(x\), the relation \(x\perp_B y\) is equivalent to the existence of a norm-one supporting functional \(\varphi\) at \(x\) with \(\varphi(y)=0\). This follows directly by applying the subgradient condition to the convex real function \(s\mapsto N_w(x+s y)\).

**Axial edges.** A common signed-coordinate permutation puts \(x=(1,s)\), \(-w<s<w\), and \(y=(0,1)\). Put \(t_0=w-s\). For \(0\le t\le t_0\), one has \(N_w(x+t y)\ge1\), so
\[
\frac{1+t}{N_w(x+t y)}\le1+t_0.
\]
For \(t\ge t_0\), the slanted supporting branch gives \(N_w(x+t y)\ge(1+s+t)/c\). The fractional function \(c(1+t)/(1+s+t)\) is monotone or constant, and its supremum on this half-line is at most \(\max\{1+t_0,c\}\). Therefore
\[
\sup_{t\ge0}\frac{1+t}{N_w(x+t y)}
\le\max\{1+w-s,c\}<1+2w.
\]
The last inequality is strict because \(s>-w\) and \(c=1+w<1+2w\).

**Slanted edges.** After the same symmetries, write \(x=(s,c-s)\), \(w<s<1\), and \(y=(-c/2,c/2)\). Here \(N_w(y)=1\). Define \(t_0=2(s-w)/c\). The slanted supporting functional gives \(N_w(x+t y)\ge1\) for all \(t\), while the second-coordinate functional gives \(N_w(x+t y)\ge c-s+ct/2\). Consequently
\[
\sup_{t\ge0}\frac{1+t}{N_w(x+t y)}
\le\max\left\{1+t_0,\frac2c\right\}<1+\frac{2d}{c}.
\]
Indeed, \(t_0<2d/c\), and \(2/c<1+2d/c\) because \(w<1\). Thus no point in the relative interior of any edge is maximizing for the final value.

**Vertices and the orthogonality cone.** Signed-coordinate permutations reduce every vertex to \(x=(1,w)\). Its norming functionals form the convex segment joining the coordinate functional \((u,v)\mapsto u\) and the slanted functional \((u,v)\mapsto(u+v)/c\). Therefore every unit vector \(y\) with \(x\perp_B y\) has the form \((-a,b)\) or \((a,-b)\), where
\[
0\le a\le c/2,\qquad
b=\begin{cases}1,&0\le a\le w,\\ c-a,&w\le a\le c/2.\end{cases}
\]
In particular \(b\ge a\) and \(b>w\).

First set \(y=(-a,b)\). For every \(t\ge0\),
\[
N_w(x+t y)\ge
\max\left\{1+\frac{b-a}{c}t,\ w+bt\right\}.
\]
The two affine lower bounds intersect exactly at
\[
t_+(a)=\frac{cd}{a+wb}.
\]
The ratio \((1+t)/(1+(b-a)t/c)\) strictly increases up to \(t_+(a)\), whereas \((1+t)/(w+bt)\) strictly decreases from \(t_+(a)\) onward. At this intersection the actual vector is
\[
x+t_+(a)y=\frac{wa+b}{a+wb}\,(w,1),
\]
so its norm equals both affine bounds. Hence the **exact** maximum over \(t\ge0\) for this \(y\) is
\[
R_+(a)=\frac{a+wb+1-w^2}{wa+b}.
\]
When \(a\le w\), this is \((a+w+1-w^2)/(1+wa)\), which is strictly increasing, with derivative \((1-w)^2(1+w)/(1+wa)^2\). When \(a\ge w\), it is \((c+da)/(c-da)\), also strictly increasing. Thus the unique maximum is at \(a=c/2\):
\[
\max_a R_+(a)=1+\frac{2d}{c},\qquad
x=(1,w),\quad y=(-c/2,c/2),\quad t=2d/c.
\]
For this pair the endpoint is \(x+t y=(w,1)\) and all displayed norms equal one.

Now set \(y=(a,-b)\). For all \(t\ge0\), the axial functional and the signed slanted functional give
\[
N_w(x+t y)\ge
\max\left\{1+at,\frac{d+(a+b)t}{c}\right\}.
\]
They intersect at
\[
t_-(a)=\frac{2w}{b-wa}.
\]
The ratio bounded by the first branch increases up to this point, and the ratio bounded by the second branch decreases afterward, since \(0\le a<1\) and \(a+b>d\). At the intersection,
\[
x+t_-(a)y
=\frac{b+wa}{b-wa}(1,-w),
\]
so both lower bounds equal the true norm. The exact maximum at fixed \(a\) is therefore
\[
R_-(a)=\frac{b-wa+2w}{b+wa}
=1+\frac{2w(1-a)}{b+wa}.
\]
For \(a\le w\) the derivative is \(-2w(1+w)/(1+wa)^2<0\), and for \(a\ge w\) it is \(-4w^2/(c-da)^2<0\). Therefore
\[
\max_a R_-(a)=1+2w,
\]
attained uniquely at \(a=0\), with \(y=(0,-1)\), \(t=2w\), and \(x+t y=(1,-w)\).

Combining the edge bounds and the two vertex maxima yields
\[
\mu(X_w)=1+2\max\left\{w,\frac{1-w}{1+w}\right\}.
\]
The two quantities are equal exactly when \(w=\sqrt2-1\). The slanted branch \((3-w)/(1+w)\) strictly decreases with \(w\); the axial branch \(1+2w\) strictly increases. Hence this crossing is the unique minimum, with value \(2\sqrt2-1\). Strict monotonicity in the vertex parameters and strict bounds in the interiors of all edges give the complete maximizing-triple classification stated above.

## Verification
Every possible unit starting point is either a vertex or an edge-interior point. At a vertex every norming functional lies in the convex cone between the two adjacent edge functionals; the orthogonality cone above therefore exhausts the allowed unit directions. Each one-variable bound is sharp at its stated affine intersection, and derivative signs establish global extrema, not numerical approximations. Substituting the two explicit pairs into \(N_w\) gives denominator one and gives respectively the quotients \(1+2(1-w)/(1+w)\) and \(1+2w\).

Symbolic derivative checks verify the strict signs on both subintervals \(0\le a\le w\) and \(w\le a\le c/2\). Independent exploratory numerical optimization across the parameter range agreed with the exact formula, but it is not used as proof. The enhanced Euclidean dihedral symmetry at the regular octagon can identify the two displayed mechanisms under isometries larger than the signed-coordinate subgroup; the classification is stated for that subgroup only.

## Relationship to prior work
The two-dimensional Lorentz predual \(d_*(1,w)^2\) is a classical octagonal norm family. Kim (2013) studies the norm and extreme points of **symmetric bilinear forms** on that same family; its complete publicly reproduced text contains no rectangular-constant computation. Its occurrence of the threshold \(\sqrt2-1\) in an unrelated bilinear classification does not imply the present identity.

Paul, Ghosh, and Sain (arXiv, 2014; journal 2017) prove general attainment of the classical rectangular constant and their Theorem 3.6 allows reduction to a vertex starting point for every real two-dimensional polyhedral space. Their full paper does not compute the present Lorentz-predual family. The proof above independently controls all edge interiors in order to classify **all** maximizing triples, rather than only establishing that some vertex realizes the supremum.

Baronti, Casini, and Papini (first online 2021) give the classical definition, general results, a characterization involving **hexagonal** norms, and \(\ell_p\) estimates. Inspection of their complete ten-page open PDF reveals no octagonal/Lorentz-predual formula. The known Euclidean Banach--Mazur distance of this octagonal family and neighboring invariants are not formulas for the Birkhoff--James rectangular quotient. In particular, numerical agreement with an unrelated invariant at the regular-octagon parameter does not imply the present full profile or its extremizer transition.

## Limitations
The theorem concerns the real two-dimensional Lorentz predual and the classical rectangular constant, not the generalized rectangular constants with other exponents, higher-dimensional Lorentz preduals, or quantitative stability of nearly maximizing triples. The full 1977 article of del Río--Benítez on two-dimensional rectangular constants was not accessible through the checked routes; later fully inspected sources cite it for the Hilbert-space endpoint characterization, but its uninspected details remain a bibliographic residual risk. The family was already studied in a 2013 paper with month-level, not verified day-level, public dating; the metadata's exact first-public-date field refers to the earliest checked, verified day-level public source of the rectangular framework (the 2014 arXiv posting), not to the first historical use of the norm.

## References
1. S. G. Kim, “The unit ball of \(L_s({}^2d_*(1,w)^2)\),” *Kyungpook Mathematical Journal* 53 (2013), 295--306, DOI 10.5666/KMJ.2013.53.2.295.
2. K. Paul, P. Ghosh, and D. Sain, “On rectangular constant in normed linear spaces,” arXiv:1407.1353v1, submitted 2014-07-05; *Journal of Convex Analysis* 24 (2017), 917--925.
3. M. Baronti, E. Casini, and P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124--133, DOI 10.1017/S0004972721000253, first published online 2021-04-26.
4. M. del Río and C. Benítez, “The rectangular constant for two-dimensional spaces,” *Journal of Approximation Theory* 19 (1977), 15--21, DOI 10.1016/0021-9045(77)90025-9.
