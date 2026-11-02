# Finite-time graph collapse and complete periodic-orbit classification for an absolute-value plane map

## Finding
For the continuous piecewise-affine planar map
\[
F(x,y)=(|x|-y-3,\ x-|y|+1),
\]
all orbits are eventually periodic. There are exactly three periodic orbits: the fixed point \((-1,-1)\), and two primitive four-cycles
\[
\mathcal P_1=\{(-5,-1),(3,-5),(5,-1),(3,5)\},\qquad
\mathcal P_2=\{(1,-3),(1,-1),(-1,1),(-3,-1)\}.
\]
More precisely, define the finite graph
\[
C=\{(t,-1):-5\le t\le5\},\quad
D_+=\{(t,t+2):-2\le t\le3\},\quad
D_-=\{(t,-t-2):-2\le t\le3\},\quad G=C\cup D_+\cup D_-.
\]
Then \(F^{14}(\mathbb R^2)\subseteq G\), \(F(G)\subseteq G\), and every point of \(G\) reaches \(C\) after at most one further iteration. Every invariant Borel probability measure is precisely a convex combination of \(\delta_{(-1,-1)}\), the uniform measure on \(\mathcal P_1\), and the uniform measure on \(\mathcal P_2\). The second four-cycle expands in the direction of \(C\); in particular the eventual-periodicity entrance time is not uniformly bounded on the whole plane.

## Assumptions and scope
The phase space is the full real plane; iteration is deterministic, forward in integer time, and the absolute values have their usual continuous values on coordinate axes. No boundedness or quadrant restriction is imposed on initial conditions. \(F^n\) denotes the \(n\)-fold iterate, and a periodic orbit means a cycle of positive least period. The invariant probability assertion concerns ordinary Borel probability measures on \(\mathbb R^2\), without a finite-moment or compact-support assumption.

## Proof
**1. Five-step nilpotence of the homogeneous part.** Write \(F=H+c\) where \(c=(-3,1)\) and \(H(x,y)=(|x|-y,\ x-|y|)\). Direct signs show \(H^5\equiv(0,0)\): when both coordinates are nonnegative, the first image is \((t,t)\) with \(t=x-y\); positive \(t\) is killed at the next step, and negative \(t\) passes through \((-2t,2t)\), \((-4t,0)\), \((-4t,-4t)\), and zero. For two nonpositive coordinates, put \(s=-x-y\ge0\): the orbit reaches \((s,-s)\), then \((2s,0)\), then \((2s,2s)\), then zero. For \(x\ge0\ge y\), the first image is \((u,v)=(x-y,x+y)\) with \(u\ge0\); when \(v\ge0\) the next image is \((-2y,-2y)\), and when \(v<0\) the next two images are \((-2y,2x)\), \((-2(x+y),-2(x+y))\), followed by zero. Finally \(x\le0\le y\) maps in one step into a region with nonpositive second coordinate, already covered by the previous cases. These are exhaustive including axes.

The reverse triangle inequality gives \(\|H(v)-H(w)\|_\infty\le2\|v-w\|_\infty\). Comparing the perturbed and homogeneous iterates, and using \(\|c\|_\infty=3\), gives
\[
\|F^5(v)-H^5(v)\|_\infty\le3\sum_{j=0}^4 2^j=93.
\]
Consequently \(F^5(\mathbb R^2)\subseteq Q=[-93,93]^2\).

**2. Exact finite polyhedral cover.** The standalone rational certificate `verification/polyhedral_certificate.py` verifies the universal inclusion
\[
F^9(Q)\subseteq G.
\]
It performs exact rational convex-polygon propagation, splitting every current convex set at the two coordinate axes before applying the relevant affine branch. An affine image of a convex polygon is the convex hull of the branch images of its vertices, including when the image collapses to a segment or point. Half-plane clipping uses exact segment intersections, so the union of output pieces covers the full branch image and not just sampled points. The certificate produces \(18\) final convex sets, specifically \(5\) points and \(13\) segments. For every resulting segment it verifies that both endpoints lie on the **same one** of \(C,D_+,D_-\), and hence that the entire segment is contained in that graph edge. The exact intermediate piece counts are \(4,13,21,29,33,31,28,23,18\). All computations use integer or rational arithmetic and assert the final inclusion. Composing the two independently established inclusions proves \(F^{14}(\mathbb R^2)\subseteq G\).

**3. A one-dimensional return map.** For \(t\in[-5,5]\),
\[
F(t,-1)=(|t|-2,t),\qquad F^2(t,-1)=(g(t),-1),
\]
where
\[
g(t)=||t|-2|-t-3=\begin{cases}
-2t-5,&-5\le t\le-2,\\
-1,&-2\le t\le0,\\
-2t-1,&0\le t\le2,\\
-5,&2\le t\le5.
\end{cases}
\]
Here \(g([-5,5])=[-5,5]\). The image \(F(C)\) is exactly \(D_+\cup D_-\); since \(F^2(C)=C\), one also has \(F(D_+\cup D_-)=C\). This proves that \(G\) is forward invariant and all its points visit \(C\) in at most one step.

**4. Full recurrent classification.** Every visit of the return coordinate \(t\) to \([-2,0]\) produces \(-1\), a fixed point of \(g\). Every visit to \([2,5]\) produces \(-5\), which alternates with \(5\). Thus an orbit never entering either constant branch must alternate between \(A=[-5,-2]\) and \(B=[0,2]\). In the alternating region \(g^2(t)=4t+9=4(t+3)-3\) for \(t\in A\); an indefinitely alternating forward orbit is bounded in \(A\) at every even return and therefore must have \(t=-3\). Then \(g(-3)=1\) and \(g(1)=-3\). There are no other nontrivial recurrent return orbits. The return fixed \(-1\), the two-cycle \(-5,5\), and the two-cycle \(-3,1\) lift under \(F\) to the stated equilibrium and four-cycles. In the last pair \(g^2\) expands deviations from \(-3\) by a factor of four; starting arbitrarily close but not equal to \(-3\) gives arbitrarily long transients, so there is no uniform entrance time for eventual periodicity.

**5. Invariant probability simplex.** Every point has finite preperiod followed by one of the three cycles, as proved. For any invariant Borel probability, Poincaré recurrence ensures almost every sampled point is recurrent (the plane is a second-countable metric space). Therefore the measure is supported on these three periodic orbits, with uniform weights along each cycle by invariance. Conversely all their convex combinations are invariant.

## Verification
Run `python verification/polyhedral_certificate.py` with standard Python 3; it requires no external packages. On the delivered version the checker reports the exact nine counts \(4,13,21,29,33,31,28,23,18\) and ends with `CERTIFICATE PASS`. It represents convex vertices as pairs of `fractions.Fraction` and clips all four closed quadrants, including boundary cases. The proof of the code's propagation invariant is given in Step 2; the checker is not a probabilistic search or floating-point experiment. In addition, the homogeneous nilpotence and scalar return analysis are direct exhaustive sign computations written above; neither requires a computational conjecture. A formal proof assistant or independent audit was not used.

## Relationship to prior work
Youtuam, Thipar, Thakthuang and Tikjha (2024) analyze second-quadrant initial conditions for this same planar map and identify the fixed point and two primitive four-cycles. Their results are credited here: the new question is complete **global** behavior from arbitrary real initial conditions, including quadrant-crossing trajectories and all invariant Borel probability measures. Earlier work on the parameter family with additive constant \(b\ge4\), and other analyses limited to specific axes or quadrants, do not imply the full-plane result for the present \(b=3\) case. The proof's new ingredient is the five-step homogeneous collapse and a finite rational covering certificate yielding a global graph reduction. The existence of related previous partial classifications does not establish publication priority: some potentially relevant work may remain unidentified.

## Limitations
This is a fixed-parameter, two-dimensional theorem and does not classify nearby parameters or higher-dimensional variants. The finite cover is justified by its exact rational algorithm and the stated propagation-invariant proof, but has not been audited by an independent mathematical reviewer. The \(14\)-iterate graph-cover bound is **not claimed optimal**; it is distinct from the unbounded final settling time. The coefficient 93 is a crude uniform enclosure, not a minimal trapping-square radius. The complete prior-art comparison is bounded by accessible material and indexed search results.

## References
1. K. Youtuam, B. Thipar, N. Thakthuang, W. Tikjha, “Stable Attractors on a Certain Two-dimensional Piecewise Linear Map,” *Journal of Computational Analysis and Applications* **32** (2024), 222–235. Public article page (2024-01-28): https://eudoxuspress.com/index.php/pub/article/view/54 ; full text: https://eudoxuspress.com/index.php/pub/article/download/54/45/88 .
2. B. Aiewcharoen, R. Boonklurb, N. Konglawan, “Global and Local Behavior of the System of Piecewise Linear Difference Equations \(x_{n+1}=|x_n|-y_n-b\), \(y_{n+1}=x_n-|y_n|+1\), where \(b\ge4\),” *Mathematics* **9** (2021), 1390. https://www.mdpi.com/2227-7390/9/12/1390 .
3. S. Krisuk, K. Soprom, J. Pantain, W. Tikjha, “Equilibrium Solution on a Two-dimensional Piecewise Linear Map,” *KKU Science Journal* **50** (2022 issue, public article 2023), 223–230. https://ph01.tci-thaijo.org/index.php/KKUSciJ/article/view/251510 .
