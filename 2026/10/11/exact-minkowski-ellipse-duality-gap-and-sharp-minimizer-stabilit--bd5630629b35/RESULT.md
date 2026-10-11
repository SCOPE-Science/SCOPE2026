# Exact Minkowski-ellipse duality gap and sharp minimizer stability in the cube–crosspolytope pair
## Finding
For a real normed space \(X\) of dimension at least two, define the *pointwise Minkowski-ellipse chord mean*
\[
F_X(x)=\sup_{y\in S_X}\frac{\|x+y\|+\|x-y\|}{2},\quad x\in S_X,
\]
and the Baronti–Casini–Papini constants
\[
A_1(X)=\inf_{x\in S_X}F_X(x),\qquad A_2(X)=\sup_{x\in S_X}F_X(x).
\]
For every integer \(n\ge2\), the dual cube–crosspolytope pair has the **complete pointwise profiles**
\[
\boxed{F_{\ell_1^n}(x)=2-\min_{1\le i\le n}|x_i|,\qquad x\in S_{\ell_1^n},}
\tag{1}
\]
\[
\boxed{F_{\ell_\infty^n}(z)=1+\frac{a_1+a_2}{2}=\frac32+\frac{a_2}{2},\qquad z\in S_{\ell_\infty^n},}
\tag{2}
\]
where \(a_1\ge a_2\ge\cdots\ge a_n\) rearranges \((|z_i|)_{i=1}^n\), so \(a_1=1\).
Consequently,
\[
\boxed{A_1(\ell_1^n)=2-\frac1n,\quad A_1(\ell_\infty^n)=\frac32,\quad
A_1(\ell_1^n)-A_1((\ell_1^n)^*)=\frac12-\frac1n.}
\tag{3}
\]
The last quantity is strictly positive for \(n\ge3\), increases with dimension, and tends to \(1/2\). In contrast,
\[
A_2(\ell_1^n)=A_2(\ell_\infty^n)=2.
\tag{4}
\]

The minimizing vectors and their sharp stability are also explicit. Put
\[
U_n=\{x\in S_{\ell_1^n}:|x_i|=1/n\text{ for all }i\},\qquad
E_n=\{\pm e_i:1\le i\le n\}.
\]
With the respective excesses over the optimal values,
\[
\delta_1(x)=F_{\ell_1^n}(x)-(2-1/n),\qquad
\delta_\infty(z)=F_{\ell_\infty^n}(z)-3/2,
\]
one has
\[
\boxed{2\delta_1(x)\le\operatorname{dist}_{\ell_1}(x,U_n)\le2(n-1)\delta_1(x),}
\tag{5}
\]
\[
\boxed{\operatorname{dist}_{\ell_\infty}(z,E_n)=2\delta_\infty(z).}
\tag{6}
\]
Both factors in (5) are sharp for every \(\delta_1\in(0,1/n]\). The unique minimizing sets are \(U_n\) and \(E_n\), respectively.

## Assumptions and scope
All spaces are real, and \(n\) is an integer at least two. The norm on \(\ell_1^n\) is \(\|x\|_1=\sum_i|x_i|\); the norm on \(\ell_\infty^n\) is \(\|z\|_\infty=\max_i|z_i|\). The identification \((\ell_1^n)^*=\ell_\infty^n\) is the standard finite-dimensional isometric duality. The distance in (5) or (6) is taken in the norm of the indicated space.

## Proof
**Crosspolytope profile.** The scalar identity
\[
\frac{|u+v|+|u-v|}{2}=\max\{|u|,|v|\}
\tag{7}
\]
gives, for each \(x\in S_{\ell_1^n}\),
\[
\frac{\|x+y\|_1+\|x-y\|_1}{2}=\sum_{i=1}^n\max\{|x_i|,|y_i|\}.
\tag{8}
\]
This expression is convex as a function of \(y\). The \(\ell_1^n\) unit ball is the convex hull of the \(2n\) signed coordinate vectors. Therefore its maximum over the ball is attained at a signed vertex \(\pm e_j\). Since scaling a nonzero \(y\) up to the sphere cannot decrease the right side of (8), the maximum over the sphere equals that over the ball. At \(y=\pm e_j\), expression (8) becomes
\[
1+\sum_{i\ne j}|x_i|=2-|x_j|.
\]
Taking the largest such value proves (1). For nonnegative numbers with sum one, \(\min_i|x_i|\le1/n\), with equality exactly if all \(|x_i|=1/n\), proving the first value in (3) and its minimizer set.

**Cube profile.** Fix \(z\in S_{\ell_\infty^n}\) and let \(y\) vary in the cube \([-1,1]^n\). The chord mean is convex in \(y\); since the cube is the convex hull of its \(2^n\) sign vectors, the supremum is attained at one such vector \(\varepsilon=(\varepsilon_i)\). Every sign vector belongs to the unit sphere, so this also yields the sphere supremum. Put \(w_i=\varepsilon_i z_i\). Because \(|z_i|\le1\),
\[
\|z+\varepsilon\|_\infty=1+\max_i w_i,\qquad
\|z-\varepsilon\|_\infty=1-\min_i w_i.
\]
Hence the optimized mean is
\[
1+\frac12\max_{\varepsilon_i\in\{-1,1\}}\bigl(\max_i w_i-\min_j w_j\bigr).
\tag{9}
\]
For distinct indices \(i,j\), the spread is at most \(|z_i|+|z_j|\le a_1+a_2\). Choosing signs to make one largest-magnitude coordinate positive and one second-largest coordinate negative attains \(a_1+a_2\), including ties and zeros. This proves (2). Since \(a_1=1\), the minimum occurs exactly when \(a_2=0\), namely at \(E_n\), proving the second value in (3).

**The upper constant.** For all unit vectors \(u,v\) in any normed space, \(\|u\pm v\|\le2\), hence \(A_2\le2\). In \(\ell_1^n\), the choice \(u=e_1,v=e_2\) has both chords of norm two. In \(\ell_\infty^n\), the unit vectors \(u=(1,1,0,\ldots,0)\), \(v=(1,-1,0,\ldots,0)\) have both chords of norm two. This proves (4) and the strict contrast with (3).

**Sharp stability.** For \(x\in S_{\ell_1^n}\), write \(b=1/n\), \(c_i=|x_i|\), and \(m=\min_i c_i\). The nearest point of \(U_n\) has the same coordinate signs as \(x\) (an arbitrary sign if \(x_i=0\)), whence
\[
d_1=\operatorname{dist}_{\ell_1}(x,U_n)=\sum_i|c_i-b|.
\]
Because \(\sum_i(c_i-b)=0\), the total negative deviation equals the total positive deviation, and therefore
\[
d_1=2\sum_{c_i<b}(b-c_i).
\tag{10}
\]
The deficit is \(\delta_1=b-m\). At least one summand in (10) equals \(\delta_1\), while every summand is at most \(\delta_1\); there are at most \(n-1\) strictly negative deviations unless \(\delta_1=0\). This proves (5). To see *both bounds are sharp at every* \(\delta\in(0,b]\), set \(m=b-\delta\). The nonnegative modulus lists
\[
\left(m,\frac{1-m}{n-1},\ldots,\frac{1-m}{n-1}\right)
\quad\text{and}\quad
\left(1-(n-1)m,m,\ldots,m\right)
\tag{11}
\]
both sum to one, both have minimum \(m\), and give the lower and upper equality of (5), respectively. For \(n=2\) the two bounds coincide.

For \(z\in S_{\ell_\infty^n}\), pick a largest-magnitude coordinate, replace it by its sign and all others by zero. This yields an element of \(E_n\) at distance \(a_2\). Conversely, any signed coordinate vector cancels at most one coordinate, leaving some coordinate of \(z\) with magnitude at least \(a_2\). Thus \(\operatorname{dist}_\infty(z,E_n)=a_2=2\delta_\infty(z)\), proving (6).

## Verification
The bundled standalone Python checker uses exact rational arithmetic. It checks both pointwise formulas against a complete list of unit-ball vertices for numerous normalized rational vectors in dimensions \(2\) through \(6\), checks the exact duality gap, and checks both sharp stability inequalities and explicit equality families. A finite computation is not the continuum proof; the proof above uses the full convex-hull representations of the two balls and algebraic deviation identities.

## Relationship to prior work
Baronti, Casini and Papini introduced the pair \(A_1,A_2\) using sums of distances from boundary points to antipodal foci. Wolf's 2011 preprint proves an upper bound of \(3/2\) for \(A_1\) in **two-dimensional** normed planes and identifies the planar equality cases; it does not apply in dimensions \(n\ge3\). Mizuguchi's paper first published in April 2022 improves the general lower estimate for \(A_1\), discusses the planar case and two specific polygonal examples, and does not state the full profiles (1)--(2) or sharp stability laws (5)--(6).

A targeted search of published mathematical records for \(A_1(\ell_1^n)\), \(A_1(\ell_\infty^n)\), the exact \(2-1/n\) expression, pointwise antipodal chord means, cube–crosspolytope duality gaps and minimizer stability found no statement encompassing the two profiles and quantitative rigidity together. The original 2000 defining paper was available only through abstract/bibliographic material for this comparison; it is therefore retained as a genuine residual risk rather than treated as fully inspected. Results about von Neumann–Jordan, James, Daugavet or octahedrality constants concern different extremal expressions and do not imply these profiles.

## Limitations
The theorem concerns the finite-dimensional real cube–crosspolytope dual pair. It does not assert an optimal duality-gap bound over arbitrary Banach spaces, nor does it classify general Hanner polytopes or non-polyhedral norms.

The identities (7)--(9) use classical elementary convexity; the new mathematical assertion assessed here is the full paired pointwise classification with dimension-dependent dual gap and **optimal quantitative stability**. The inaccessible full text of the original 2000 defining paper remains an originality risk. Search failure is not proof of absolute novelty.

## References
1. M. Baronti, E. Casini and P. L. Papini, “Triangles inscribed in a semicircle, in Minkowski planes, and in normed spaces,” *Journal of Mathematical Analysis and Applications* **252** (2000), 124–146, doi:10.1006/jmaa.2000.6959.
2. R. Wolf, “A norm inequality related to affine regular hexagons,” arXiv:1106.6167v1, first posted 30 June 2011; *Beiträge zur Algebra und Geometrie* **53** (2012), 529–546, doi:10.1007/s13366-011-0075-1.
3. H. Mizuguchi, “A lower bound for the constant \(A_1(X)\) in normed linear spaces,” *Beiträge zur Algebra und Geometrie* **64** (2023), 535–543, doi:10.1007/s13366-022-00646-y. First publicly published online 22 April 2022; primary MSC 46B20.
