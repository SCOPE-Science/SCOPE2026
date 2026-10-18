# Sharp plateau and dimension cutoff for Hilbert distortion of long-edge even cycles

## Finding
For every odd integer \(m\ge5\) and every real \(1<t\le2\), let \(C_{m+1}(t)\) be the shortest-path metric on a cycle with \(m\) successive edges of length one and its closing edge of length \(t\). Let \(D_m(t)=d_{\mathrm{BM}}(\mathcal F(C_{m+1}(t)),\ell_2^m)\) be the **unrestricted real** Euclidean Banach--Mazur distance of its Lipschitz-free (transportation-cost) space. Set
\[
T_m=\frac{m}{\sqrt{1+(m-1)\sqrt{m+1}}},\qquad H_m=\frac{1+(m-1)\sqrt{m+1}}{m}.
\]
Then \(T_m>1\), and the exact distortion is
\[
\boxed{D_m(t)^2=\begin{cases}
\displaystyle \frac1{t^2}+\frac{(m-1)(m^2-1)}{m^2-t^2},&1<t\le\min\{2,T_m\},\\[5pt]
\displaystyle H_m^2,&T_m\le t\le2\quad\text{if }T_m\le2.
\end{cases}}
\]
The two branches agree at \(T_m\). The distortion strictly decreases up to \(T_m\), and has a nontrivial constant interval \([T_m,2]\) **exactly for** \(m\in\{5,7,9,11,13,15\}\) (cycle orders \(6,8,10,12,14,16\)). For odd \(m\ge17\), \(T_m>2\), and \(D_m(t)\) is strictly decreasing throughout \(1<t\le2\). At the equilateral limit \(t\downarrow1\), \(D_m(t)\to\sqrt m\). No claim for a four-cycle is new here.

## Assumptions and scope
All normed spaces, linear maps, and Banach--Mazur distances are over \(\mathbb R\). The weighted cycle has exactly \(m+1\) distinct vertices, with positive edge lengths \(1,\ldots,1,t\), and the induced shortest-path metric. Every edge is essential for the stated \(1<t\le2<m\). The Banach--Mazur distance is the infimum \(\inf_T\|T\|\|T^{-1}\|\) over **all** invertible real linear maps. The Lipschitz-free space has dimension \(m\). The theorem concerns only odd \(m\ge5\), equivalently even cycle orders at least six, and one exceptional longer edge at most two.

## Proof
**1. Exact dual ball.** Anchor a potential at one cycle vertex, and let \(x_i\) denote its successive increments on the \(m\) unit edges. The closing edge difference is \(-\sum_{i=1}^m x_i\). The edge inequalities are equivalent to global Lipschitzness for the weighted shortest-path metric, so the dual Lipschitz ball is linearly isometric to
\[
K_{m,t}=\{x\in\mathbb R^m:|x_i|\le1\ (1\le i\le m),\quad |\sum_i x_i|\le t\}.
\]
Finite-dimensional Banach--Mazur distance is invariant under duality and \(\ell_2^m\) is self-dual, so it suffices to optimize Euclidean ellipsoids for \(K_{m,t}\).

**2. Symmetry proves global optimality of a two-eigenvalue form.** If \(q\) is any positive definite quadratic form with norm \(\sqrt{q}\), its squared distortion is
\[
\frac{\max_{x\in K_{m,t}}q(x)}{\min_{x\in\partial K_{m,t}}q(x)}.
\]
Equivalently, \(a\|x\|_{K_{m,t}}^2\le q(x)\le b\|x\|_{K_{m,t}}^2\) for all \(x\). Average these inequalities over the entire coordinate-permutation group: the averaged positive definite form has the same bounds and therefore cannot have worse distortion. Every permutation-invariant positive definite quadratic, up to positive scale, equals
\[
q_r(x)=\sum_i x_i^2+\frac{r-1}{m}\left(\sum_i x_i\right)^2,\qquad r>0.
\]
It has eigenvalue \(1\) on the zero-sum hyperplane and \(r\) on the constant direction. Hence optimizing \(q_r\) is already optimizing over **every** Hilbertian position, not merely permutation-symmetric positions.

**3. Exhaust the exterior vertices.** Because \(m\) is odd and \(1<t\le2\), a cube vertex in \(K_{m,t}\) must have coordinate sum \(\pm1\). Every other vertex is the intersection of a strip plane \(\sum x_i=\pm t\) and a cube edge, fixing the other \(m-1\) signs with sum \(\pm2\); the free coordinate is \(\pm(t-2)\). Indeed, a vertex must activate \(m\) independent inequalities; when all cube coordinates are fixed one gets the first type, otherwise exactly one coordinate is free and the strip equality is active, and the even integer sum of the fixed signs must equal \(\pm2\) (the values zero and absolute values at least four violate \(1<t\le2\)). Conversely these are feasible vertices; endpoint coincidences do not affect maximization. A positive definite quadratic has its maximum on a vertex, yielding
\[
F_m(t,r)=\max\left\{m+\frac{r-1}{m},\quad m-1+(2-t)^2+\frac{(r-1)t^2}{m}\right\}.
\]

**4. Determine the interior boundary radius.** The ellipsoid \(\{q_r(x)\le R^2\}\) is inside \(K_{m,t}\) precisely when each of its supporting slab inequalities holds. The inverse matrix of \(q_r\) has eigenvalue \(1\) on the zero-sum subspace and \(1/r\) on the constant subspace, so
\[
\max_{q_r(x)\le1}|x_i|^2=\frac{m-1+1/r}{m},\qquad
\max_{q_r(x)\le1}|\sum_i x_i|^2=\frac mr.
\]
Consequently the squared distortion for \(q_r\) is *exactly*
\[
F_m(t,r)G_m(t,r),\qquad G_m(t,r)=\max\left\{\frac{m-1+1/r}{m},\frac{m}{t^2r}\right\}.
\]
No assumption about the contact positions or independent coordinate facets is needed.

**5. Globally minimize the scalar expression.** Let
\[
r_G=\frac{m^2/t^2-1}{m-1},\quad r_F=1+\frac{m(3-t)}{t+1},\quad r_0=\sqrt{m+1}.
\]
The two branches of \(G_m\) exchange at \(r_G\), and those of \(F_m\) exchange at \(r_F\). Elementary factorization gives
\[
r_F-r_G=\frac{m(t-1)\{m(1+2t-t^2)+2t^2\}}{t^2(m-1)(t+1)}>0,
\]
while \(r_F\ge1+m/3\ge\sqrt{m+1}=r_0\) (using \(m\ge5\)). For \(r\le r_G\), the product simplifies to \((m^2-1+r)/(t^2r)\), strictly decreasing in \(r\). Between \(r_G\) and \(r_F\), it is
\[
\frac{(m^2-1+r)(m-1+1/r)}{m^2},
\]
whose derivative has the sign of \(r^2-(m+1)\). Thus it decreases up to \(r_0\) and increases thereafter. Above \(r_F\), writing the second branch of \(F_m\) as \(a+(t^2/m)r\) with \(a=m-1+(2-t)^2-t^2/m\), differentiation shows the product has the sign of \(r^2-r_B^2\), where
\[
r_B^2=\frac{ma}{t^2(m-1)}\le m+1=r_0^2.
\]
The last inequality is equivalent to \((t-1)[(m-1)(t+1)+4]\ge0\). Thus the product is already increasing past \(r_F\). The **global** minimizer is therefore
\[
\boxed{r_*(t)=\max\{r_G,r_0\}.}
\]
The crossing \(r_G=r_0\) is exactly \(t=T_m\). Substituting \(r_G\) below this crossing gives
\[
F_m(t,r_G)G_m(t,r_G)=\frac1{t^2}+\frac{(m-1)(m^2-1)}{m^2-t^2},
\]
and substituting \(r_0\) above it gives \(H_m^2\). The derivative of the first formula is negative precisely for \(t<T_m\). At \(t=1\) it equals \(m\). Finally \(T_m\le2\) is equivalent, on this positive domain, to
\[
m^3-16m^2+8m+16\le0.
\]
For odd integers \(m\ge5\), direct evaluation through \(15\), positivity at \(17\), and strict positivity/increase thereafter show that this holds exactly for \(5\le m\le15\). This proves both the formula and the sharp dimension cutoff.

## Verification
The standalone Python 3 standard-library checker `verify_long_even_cycles.py` independently enumerates every feasible vertex type of the clipped cube, including strip/cube-edge intersections, using exact rational arithmetic. It tests ninety exact rational vertex-shell/ellipsoid cases in dimensions five, seven, and nine. Separately it numerically minimizes the complete piecewise convex-body distortion expression in forty-five dimension/parameter configurations through dimension twenty-one, and checks the endpoint and dimension cutoff. It prints `PASS: 90 exact rational vertex-shell/ellipsoid comparisons`, `PASS: 45 independent golden-section minimizations`, and `PASS: dimension cutoff m<=15 and known four-cycle boundary`. The enumeration and numerical tests are finite corroboration; the general theorem is established by the analytic proof.

## Relationship to prior work
Ostrovska and Ostrovskii established the cycle-space quotient model for weighted finite-graph transportation spaces, which supplies the standard edge-coordinate starting point but not the optimal Hilbert distortion. Alexander, Fradelizi, García-Lirola, and Zvavitch studied finite Lipschitz-free ball geometry, decomposition, and Mahler volume products. Two particularly close subsequently published results determine: (i) the complete Euclidean distortion on the **four-vertex** cycle with one arbitrary edge, including an earlier four-cycle plateau; and (ii) the complete Euclidean distortion of one-edge-weighted cycles with the exceptional edge **no longer than one**. Another result covers exactly the equilateral cycle endpoints. The present statement excludes the already-treated four-cycle, uses \(m\ge5\) and \(t>1\), and determines a new all-dimensional plateau-cutoff law for precisely the unaddressed long-edge domain. Neither the four-cycle-only theorem nor the short-edge theorem implies the new cutoff in cycle order sixteen.

## Limitations
The result is restricted to real Lipschitz-free spaces, even cycles of order at least six, a single exceptional longer edge, and the interval \(1<t\le2\). It does not determine multi-weight or complex-scalar distortions, uniqueness among all nonsymmetric optimal Hilbertian forms, or the region \(2<t<m\). Although the proof is valid for every real parameter in scope, the independent computer checks are finite. Equivalent calculations in inaccessible or unindexed classical ellipsoid literature remain a bibliographic risk. There has been no independent scientific audit.

## References
1. S. Ostrovska and M. I. Ostrovskii, "On relations between transportation cost spaces and \(\ell_1\)," arXiv:1910.03625v1, submitted 8 October 2019; Journal of Mathematical Analysis and Applications 491 (2020), 124338. https://arxiv.org/abs/1910.03625
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, "Geometry and volume product of finite dimensional Lipschitz-free spaces," arXiv:1911.10642v1, submitted 24 November 2019. https://arxiv.org/abs/1911.10642
3. "Exact Euclidean distortion of a one-defect four-cycle transportation space," publicly available mathematical record (2026); full theorem and proof, domain \(n=4\), \(0<t\le3\).
4. "Opposite parity laws for exact Hilbert distortion of one-edge weighted cycles," publicly available mathematical record (2026); full theorem and proof, domain \(0<t\le1\).
5. "Scalar-field parity in Euclidean distortion of cycle transportation spaces," publicly available mathematical record (2026); equilateral cycle Hilbert distortion law.
