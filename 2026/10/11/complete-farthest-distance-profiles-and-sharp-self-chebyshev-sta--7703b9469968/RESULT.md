# Complete farthest-distance profiles and sharp self-Chebyshev stability for regular polygons
## Finding
Let \(n\ge5\) be an integer and let \(P_n\) be a regular convex Euclidean \(n\)-gon of circumradius \(R>0\), with boundary \(\Gamma_n\). Define
\[
\mu_n(x)=\max_{y\in\Gamma_n}\|x-y\|_2,\qquad
\delta_n=\min_{x\in\Gamma_n}\mu_n(x).
\]
The latter is the self Chebyshev radius, also called the relative Chebyshev radius of the boundary with respect to itself.

On each side of \(P_n\), let \(t\) be signed arc-length displacement from the side midpoint, measured along the straight side, with
\[
\alpha=\frac\pi n,\quad r=R\cos\alpha,\quad s=R\sin\alpha,\quad -s\le t\le s.
\]
Then **the entire farthest-boundary distance profile** on each side is
\[
\boxed{\mu_n(t)^2=\begin{cases}
(R+r)^2+t^2,&n\ \mathrm{odd},\\
4r^2+(s+|t|)^2,&n\ \mathrm{even}.
\end{cases}}
\tag{1}
\]
The self Chebyshev centers on the boundary are **exactly the \(n\) side midpoints**, and
\[
\boxed{\delta_n=\begin{cases}
R(1+\cos(\pi/n)),&n\ \mathrm{odd},\\
R\sqrt{1+3\cos^2(\pi/n)},&n\ \mathrm{even}.
\end{cases}}
\tag{2}
\]
More sharply, (1) gives the equality
\[
\boxed{\mu_n(t)^2-\delta_n^2=\begin{cases}
t^2,&n\ \mathrm{odd},\\
t^2+2R\sin(\pi/n)|t|,&n\ \mathrm{even}.
\end{cases}}
\tag{3}
\]
Thus the squared minimax function has a quadratic minimum on a side for odd \(n\) and a nonzero linear cusp for even \(n\). This is an exact, best-possible boundary-center stability law, not merely an inequality.

For odd \(n\), the unique farthest vertex from a side midpoint is the opposite vertex. For even \(n\), the two farthest vertices from a side midpoint are the opposite side's endpoints. Consequently the distinguished chords from every minimax center are fully classified.

The perimeter ratio satisfies
\[
\frac{\operatorname{per}(P_n)}{\delta_n}=
\begin{cases}
2n\tan\dfrac{\pi}{2n},&n\ \mathrm{odd},\\[5pt]
\dfrac{2n\sin(\pi/n)}{\sqrt{1+3\cos^2(\pi/n)}},&n\ \mathrm{even}.
\end{cases}
\tag{4}
\]
Along the respective parity subsequences, the expansion of (4) is
\[
\begin{aligned}
\frac{\operatorname{per}(P_n)}{\delta_n}
&=\pi+\frac{\pi^3}{12n^2}+\frac{\pi^5}{120n^4}+O(n^{-6}) &&(n\ \mathrm{odd}),\\
&=\pi+\frac{5\pi^3}{24n^2}+\frac{61\pi^5}{1920n^4}+O(n^{-6}) &&(n\ \mathrm{even}).
\end{aligned}
\tag{5}
\]
The lower bound by \(\pi\) for arbitrary convex curves is due to Falconer, not a new consequence asserted independently here.

## Assumptions and scope
The distance is ordinary ambient Euclidean distance between boundary points, **not shortest path distance along the boundary**. The covering disk's center must belong to the boundary, not the interior of the polygon. The parameter \(R\) is the distance from the polygon center to any vertex, not the side apothem.

The quantified new all-order result applies to \(n\ge5\). The displayed identities happen also to yield the known equilateral-triangle value at \(n=3\) and the known square value at \(n=4\); these special values are not claimed as new. No assertion is made about the optimal shape among all irregular \(n\)-gons.

## Proof
Write \(\alpha=\pi/n\), \(r=R\cos\alpha\), and \(s=R\sin\alpha\), with \(R>0\). By the dihedral symmetry of the regular polygon it suffices to consider the side
\[
E=\{(r,t):-s\le t\le s\},
\]
whose endpoints are \(v_+=(r,s)\) and \(v_-=(r,-s)\). The polygon's vertices lie on the circumcircle and have polar angles
\[
(2k+1)\alpha,\qquad k=0,1,\ldots,n-1.
\tag{6}
\]

**Reduction of the maximization to vertices.** Along any nondegenerate side segment parameterized by \(z(\lambda)=(1-\lambda)a+\lambda b\), the squared distance \(\|x-z(\lambda)\|_2^2\) is strictly convex in \(\lambda\). Hence its maximum is attained at an endpoint. It follows that
\[
\mu_n(x)^2=\max_{0\le k<n}\|x-v_k\|_2^2
=\|x\|_2^2+R^2-2\min_k\langle x,v_k\rangle.
\tag{7}
\]

**Which vertex is farthest.** For \(x=(r,t)\in E\), let \(\theta=\arg x\), so \(-\alpha\le\theta\le\alpha\) because \(r>0\). Minimizing the dot product in (7) means choosing the vertex whose polar angle is nearest to \(\theta+\pi\) on the circle, since all vertices have the same radius.

If \(n\) is odd, \(\pi\) itself is a vertex angle in (6), and its two neighbors have angles \(\pi-2\alpha\) and \(\pi+2\alpha\). For every \(|\theta|\le\alpha\), the angle \(\pi\) is no farther from \(\pi+\theta\) than either neighbor (and therefore no farther than any other vertex). It is the unique closest one for \(|\theta|<\alpha\), with the adjacent vertex tying only at a side endpoint. Therefore the farthest vertex for the interior of the side is \((-R,0)\), giving
\[
\mu_n(r,t)^2=\|(r,t)-(-R,0)\|_2^2=(R+r)^2+t^2.
\tag{8}
\]

If \(n\) is even, the vertex angles immediately bracketing \(\pi\) in (6) are \(\pi-\alpha\) and \(\pi+\alpha\), with positions \((-r,s)\) and \((-r,-s)\). For \(-\alpha\le\theta\le\alpha\), the nearest vertex to \(\theta+\pi\) is the corresponding one of this pair. The vertex opposite the sign of \(t\) is farthest (both tie when \(t=0\)). Consequently,
\[
\mu_n(r,t)^2=\max\{(2r)^2+(t-s)^2,\ (2r)^2+(t+s)^2\}
=4r^2+(s+|t|)^2.
\tag{9}
\]
Equations (8)--(9) prove the full profile (1), including edge endpoints by continuity.

**Minima and rigidity.** Subtraction at \(t=0\) yields
\[
\mu_n(t)^2-\mu_n(0)^2=
\begin{cases}
t^2,&n\ \mathrm{odd},\\
t^2+2s|t|,&n\ \mathrm{even}.
\end{cases}
\]
This is strictly positive whenever \(t\ne0\). Thus on each side its midpoint is the **unique** minimizer, and the full boundary has exactly \(n\) such points. At the midpoint,
\[
\mu_n(0)=R+r\quad(n\ \mathrm{odd}),\qquad
\mu_n(0)=\sqrt{4r^2+s^2}\quad(n\ \mathrm{even}),
\]
which proves (2)--(3), the parity-dependent order of vanishing, and the farthest-vertex statements. The periodic polygon sides cover all boundary points, so there are no omitted minimizers.

**Perimeter ratios.** The polygon perimeter is \(2nR\sin\alpha\). Dividing by (2) and using
\[
\frac{\sin\alpha}{1+\cos\alpha}=\tan\frac\alpha2
\]
gives (4). Finally put \(x=1/n\) and Taylor-expand the two explicit analytic quotients around \(x=0\), obtaining (5). The expansions hold along the indicated integer subsequences.

## Verification
The standalone program `verify.py` verifies the symbolic \(1/n\) series in (5), the published equilateral-triangle and square calibration values, and the exact center-stability algebra. It also independently evaluates the maximum squared distance from each of a dense collection of side points to **every** polygon vertex for \(3\le n\le121\), together with \(n=201,301\). It reported `VERIFY_OK` after 401,880 vertex-distance comparisons; the largest absolute discrepancy was below \(1.34\times10^{-15}\) in width-one coordinates.

The finite computations are regression tests and **not** an exhaustive proof for unbounded \(n\). Equations (6)--(9), the angle-ordering argument, and the strict defect (3) establish the universally quantified statement.

## Relationship to prior work
Walter's 2016 preprint introduced and studied this relative-Chebyshev invariant for convex curves. Its Sections 4--5 give a finite algorithm for an arbitrary polygon, and its Section 6 treats triangles and quadrilaterals. Its equilateral-triangle benchmark and square calculation are prior results. The algorithm does not state an all-order regular-polygon closed form or a parity-dependent stability profile.

Balestro, Martini, Nikonorov, and Nikonorova (2021) give a full classification of the self Chebyshev radius of arbitrary triangles (their Theorem 2), alongside general upper perimeter bounds. Their regular \(2(n-1)\)-gon construction produces a different half-disk polygon as a perimeter maximizer, not the boundary-self-radius profile of a regular \(n\)-gon. The all-order profile is not in that materially inspected paper.

Nikitenko and Nikonorov (2023 preprint) determine the sharp **quadrilateral** perimeter-to-self-radius constant and, in Section 9, motivate a still-open direction: regular odd \(n\)-gons are conjectured to minimize perimeter among convex \(n\)-gons at a fixed boundary self Chebyshev radius. Our exact odd-order ratio in (4) is the natural candidate value for that conjecture, but **does not prove the global conjecture**. Their article also credits Falconer's 1977 general inequality \(L\ge\pi\delta\), which is not claimed as new.

The even constant in (2) numerically coincides with an exact regular-even-polygon **maximum-piece-diameter bisection** invariant reported separately. That result optimizes over cuts and two-piece diameters, not over centers of one covering disk constrained to the polygon boundary. No general equivalence of those optimization problems has been established here; in particular, we do not claim the even numerical value as an independently new invariant. The present contribution is the complete farthest-distance profile, sharp parity-dependent boundary-center stability, exact center/chord classification, and all-order odd-family benchmark.

## Limitations
No global optimizer among irregular convex polygons is determined; the regular-odd extremality conjecture remains open beyond the established triangle case. No extension to geodesic boundary distance, higher dimensions, or non-Euclidean norms is claimed.

The trigonometric benchmark is elementary once the farthest vertex is rigorously classified. An unindexed earlier regular-polygon calculation could already state it; this is the principal historical originality risk. The even numerical constant matches a related published bisection value; its existence does not itself certify equivalence of the two underlying variational problems. Only the named full-profile and stability statements are asserted as the contribution.

## References
1. R. Walter, *On a Minimax Problem for Ovals*, arXiv:1606.06717v1 (21 June 2016), subsequently Minimax Theory and its Applications 2 (2017), 285--318.
2. V. Balestro, H. Martini, Yu. G. Nikonorov, and Yu. V. Nikonorova, *Extremal Problems for Convex Curves with a Given Self Chebyshev Radius*, Results in Mathematics 76 (2021), article 87, DOI:10.1007/s00025-021-01394-6.
3. E. V. Nikitenko and Yu. G. Nikonorov, *The Extreme Polygons for the Self Chebyshev Radius of the Boundary*, arXiv:2301.03218v1 (9 January 2023), later Studia Scientiarum Mathematicarum Hungarica 60 (2023), 193--236, DOI:10.1556/012.2023.04297.
4. K. J. Falconer, *A Characterisation of Plane Curves of Constant Width*, Journal of the London Mathematical Society, 1977. Cited in reference 3 for the established general perimeter/self-radius inequality.
