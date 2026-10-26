# Sharp linear Lipschitz extension at every edge midpoint of a Euclidean rectangle

## Finding
For every \(a,b>0\), write \(V=\{(-a,-b),(-a,b),(a,-b),(a,b)\}\) and
\[Y=V\cup\{(0,b),(0,-b),(a,0),(-a,0)\}.\]
All distances are inherited from the Euclidean plane. Equip the real functions on \(V\) and \(Y\) with Lipschitz seminorm. Every real-linear extension restricts to the identity on \(V\); its operator norm is measured on functions modulo constants. The unrestricted minimum is
\[
\boxed{\lambda(V,Y)=\frac{a+b+\sqrt{a^2+b^2}}{M+\sqrt{M^2+4m^2}},\quad m=\min\{a,b\},\ M=\max\{a,b\}.}
\]
The minimum is attained by a positive operator that simultaneously realizes the independent optimal one-point extension at each added point. Its Lipschitz modulus between any two added midpoints is at most one. With \(t=m/M\in(0,1]\), the value \(\lambda(t)\) has precisely one global maximum, at \(t_*=0.411594753826\ldots\), of size \(1.086156512046\ldots\). The maximizing rectangle is therefore not a square.

## Assumptions and scope
Real scalar functions and Euclidean chord distance are essential. A linear operator has finite Lipschitz seminorm precisely when it preserves constants: since it fixes the values at the original four vertices, the image of a constant input must be the same constant everywhere. Thus an extension value at an added point has affine coefficient sum one. No positivity, reflection symmetry, or equivariance is assumed in the minimization. Coordinates \(a,b\) are strictly positive; degenerating rectangles are outside the theorem.

Put \(c=\sqrt{a^2+b^2}\), \(D_a=\sqrt{a^2+4b^2}\), \(D_b=\sqrt{4a^2+b^2}\), and
\[
L_a=\frac{a+b+c}{a+D_a},\qquad L_b=\frac{a+b+c}{b+D_b},\qquad
\beta=\frac{a(L_a-1)}{2(b+c-a)},\qquad
\delta=\frac{b(L_b-1)}{2(a+c-b)}.
\]
The denominators are positive, and \(0<\beta,\delta<1/4\), as proved below. Let \(U\) be the uniform probability measure on the four vertices. Let \(T,B,R,L\) be the uniform probability measures on the respective top, bottom, right, and left edge's two vertices. Assign to the four added points the probability measures
\[
\mu_{(0,b)}=(1-4\beta)T+4\beta U,\quad
\mu_{(0,-b)}=(1-4\beta)B+4\beta U,
\]
\[
\mu_{(a,0)}=(1-4\delta)R+4\delta U,\quad
\mu_{(-a,0)}=(1-4\delta)L+4\delta U.
\]
Define \(Ef(y)=\int_V f\,d\mu_y\) at the added points and \(Ef(v)=f(v)\) at original vertices.

## Proof
**Step 1: unrestricted one-point lower bounds.** At the top midpoint \(z=(0,b)\), average any candidate operator over reflection in the vertical coordinate axis, which fixes \(z\) and preserves its operator norm. The resulting affine evaluation measure puts weight \(\alpha\) at each top vertex and \(1/2-\alpha\) at each bottom vertex, with \(\alpha\in\mathbb R\) unrestricted. Applying the one-Lipschitz vertex function \(f(v)=d(v,x)\) for a fixed top corner \(x\) gives the following lower bound on the normalized extension slope from \(x\) to \(z\):
\[
\frac{(b+c)-2(b+c-a)\alpha}{a}.
\]
The same distance-function witness at a bottom corner (whose distance from \(z\) is \(D_a\)) gives
\[
\frac{a+2(b+c-a)\alpha}{D_a}.
\]
Their slopes as functions of \(\alpha\) are strictly opposite; minimizing their maximum over *all signed* \(\alpha\) occurs at their intersection, with value exactly \(L_a=(a+b+c)/(a+D_a)\). Repeating after a quarter-turn of the geometric description, but without exchanging the numerical side lengths, yields the lower bound \(L_b=(a+b+c)/(b+D_b)\) at a right/left midpoint. Consequently every extension obeys
\[\|E\|\ge\max\{L_a,L_b\}.\]
Neither this step nor its witnesses presupposes positive interpolation coefficients.

**Step 2: positivity and the matching corner bounds.** The inequalities \(b+c>D_a\) and \(a+c>D_b\) follow by squaring and reducing to \(c>a\) and \(c>b\), respectively. Hence \(L_a,L_b>1\), so \(\beta,\delta>0\). The top-midpoint two witness slopes meet for a coefficient \(\alpha\in(1/4,1/2)\): at \(\alpha=1/4\) the near-corner slope is \((a+b+c)/(2a)\), strictly greater than the far-corner slope \((a+b+c)/(2D_a)\); at \(\alpha=1/2\), the near-corner slope is one and the far-corner slope is \((b+c)/D_a>1\). The unique intersection therefore has \(\beta=1/2-\alpha\in(0,1/4)\). The same argument gives \(\delta\in(0,1/4)\).

For positive probability measures on \(V\), the Lipschitz-free distance to an individual vertex mass is the expected Euclidean transport distance to that vertex. For the measures just constructed, reflection symmetry leaves only near-corner and far-corner cases at each midpoint, and their normalized transport costs are *both* exactly \(L_a\) for the top/bottom points and \(L_b\) for the right/left points. These formulas also follow by substituting \(\alpha=1/2-\beta\) into the two displayed slopes. Thus all old-to-new pairs cost at most \(\max\{L_a,L_b\}\) times their Euclidean separation.

**Step 3: simultaneous new-to-new bounds.** On finite \(V\), the Kantorovich–Rubinstein norm \(W_1\) of differences of probability measures is convex in each argument. For one horizontal-side midpoint and one vertical-side midpoint, its two mixing parameters \(4\beta,4\delta\) lie in \([0,1]\). Separate convexity bounds the transport distance by its maximum at the four endpoint pairs \((T,R),(T,U),(U,R),(U,U)\). Their exact \(W_1\)-distances are \(c,b,a,0\), respectively: pair the common corner first in the first case and transport the remaining half mass diagonally; in the second and third cases move half the mass between opposite sides. Since \(\max\{a,b,c\}=c\), which equals the Euclidean distance between adjacent edge midpoints, their extension slope is at most one. Reflections cover all four perpendicular side pairings.

For the opposite top and bottom midpoints, the difference of measures is \((1-4\beta)(T-B)\), so \(W_1=2b(1-4\beta)\le2b\). Likewise the right/left difference is \((1-4\delta)(R-L)\), giving \(W_1=2a(1-4\delta)\le2a\). Thus *all* added-to-added slopes are at most one. By the Lipschitz-free duality between vertex functions and signed probability measures, this proves \(\|E\|\le\max\{L_a,L_b\}\), matching Step 1.

**Step 4: which one-point bound controls?** If \(0<a\le b\), the triangle inequalities \(D_a\le a+2b\) and \(D_b\le2a+b\) give \(D_a+D_b\le3(a+b)\). Rationalizing yields
\[
D_a-D_b=\frac{3(b-a)(a+b)}{D_a+D_b}\ge b-a.
\]
Consequently \(a+D_a\ge b+D_b\), so \(L_b\ge L_a\); the inequality is strict for \(a<b\). Exchanging axes gives the claimed formula with \(m\) and \(M\).

**Step 5: unique worst aspect ratio.** By scale invariance normalize \(M=1\) and set \(t=m/M\in(0,1]\), \(c_t=\sqrt{1+t^2}\), \(D_t=\sqrt{1+4t^2}\). Then
\[
\lambda(t)=\frac{1+t+c_t}{1+D_t},\qquad
\lambda(t)-1=\frac{2t}{(c_t+t)(c_t+t+D_t)(1+D_t)}.
\]
For \(s=\log t\), the functions \(e^s\), \(\sqrt{1+e^{2s}}\), \(\sqrt{1+4e^{2s}}\), and the constant one are log-convex in \(s\). Positive sums of log-convex functions remain log-convex; hence each of the three denominator factors in the second expression is log-convex in \(s\). The last factor is strictly so. Therefore \(\log(\lambda(e^s)-1)\) is strictly concave in \(s\); its derivative is strictly decreasing. This derivative tends to one as \(s\to-\infty\), whereas it is negative at \(s=0\): indeed \(\lambda'(1)<0\) is equivalent to \(8>5+\sqrt5\). It crosses zero exactly once, proving the unique maximizing aspect ratio. Its defining equation is
\[
\left(1+\frac{t}{\sqrt{1+t^2}}\right)(1+\sqrt{1+4t^2})=
\frac{4t(1+t+\sqrt{1+t^2})}{\sqrt{1+4t^2}},
\]
and numerical root evaluation gives the approximations in the Finding. The square \(t=1\) is not maximally unstable.

## Verification
Run the attached standalone standard-library script `verify_rectangle.py` using `python verify_rectangle.py`. It enumerates every vertex of the three-dimensional Lipschitz dual polytope of the four rectangle corners (fixing the first corner's potential at zero), evaluates every one of the \(22\) nontrivial unordered target pairs across \(19\) aspect ratios, and compares its computed operator norm against the closed formula. It also checks that every midpoint-to-midpoint ratio is at most one. All \(418\) target pairs pass, including the aspect ratios near the unique peak and values on both sides of the square. These are finite numerical cross-checks only; Steps 1–5 prove the claims for all positive real \(a,b\).

## Relationship to prior work
Bruè, Di Marino and Stra provide general linear Lipschitz extension machinery by random projections on closed doubling sets, rather than this exact eight-point anisotropic Euclidean configuration. Basso develops finite Lipschitz-free projection constants and linear-programming methods, including a different four-point rectangle example in an \(\ell_\infty^2\) metric with two added points. Its statement does not imply this eight-point Euclidean formula. An existing sharp result for the Euclidean **square** with all four edge midpoints agrees with the specialization \(a=b\); that case is acknowledged and is not presented as new. The full non-square aspect-ratio formula, the simultaneous positivity compatibility and the unique non-square global maximizer are the new scope.

## Limitations
Only scalar real-linear extension operators and inherited planar Euclidean distances are treated. This does not classify all minimizers, extend the formula to arbitrary quadrilaterals, or imply the Banach-valued extension property. The cited literature comparison is best-knowledge rather than a proof that no earlier equivalent computation exists. The displayed decimal root and norm are numerical approximations; the uniqueness theorem is analytic. Independent mathematical audit has not been performed.

## References
1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533, first posted 2018-01-23, https://arxiv.org/abs/1801.07533.
2. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238, first posted 2021-04-29, https://arxiv.org/abs/2104.14238.
