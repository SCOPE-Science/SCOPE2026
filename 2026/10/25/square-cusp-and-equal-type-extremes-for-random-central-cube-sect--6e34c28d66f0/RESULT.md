# Square-cusp and equal-type extremes for random central cube-section perimeters

## Finding
Let \(C=[-1,1]^3\), let \(U\) have the uniform surface-area probability distribution on \(S^2\), and put \(K_U=C\cap U^\perp\). Write \(P(U)\) for the Euclidean perimeter and \(N(U)\) for the number of edges of \(K_U\) (almost surely four or six). The known sharp maximum is \(P_*=4(1+\sqrt2)\). As \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\{P(U)>P_*-\varepsilon\}
 =\frac{3\sqrt2}{8\pi}\varepsilon^2+O(\varepsilon^3).}
\]
More precisely, write \(a\ge b\ge c\) for the sorted absolute coordinates of \(U\), and, on the probability-one set \(b>0\), let \(r=(a-b)/b\) and \(q=c/b\). Conditional on \(P(U)>P_*-\varepsilon\),
\[
\boxed{\left(\frac{2\sqrt2\,r}{\varepsilon},
                 \frac{2\sqrt2\,q}{\varepsilon}\right)
 \Longrightarrow (V,W),\qquad V,W\ \text{independent uniform on }[0,1].}
\]
In the same joint convergence the indicator that the section is hexagonal tends to \(\boldsymbol1_{\{W>V\}}\). Consequently
\[
\boxed{\Pr\{N(U)=6\mid P(U)>P_*-\varepsilon\}\longrightarrow\tfrac12,
\quad\Pr\{N(U)=4\mid P(U)>P_*-\varepsilon\}\longrightarrow\tfrac12.}
\]
The normalized shortfall \((P_*-P(U))/\varepsilon\), under the same conditioning, converges to a \(\operatorname{Beta}(2,1)\) law. The 12 distinct oriented maximizing normals are conditionally equiprobable in the limit and independent of \((V,W)\).

## Assumptions and scope
The section plane passes through the cube center; the normal is Haar-uniform on the sphere (equivalently, a Haar-uniform unoriented plane). The cube is side length 2. Perimeter is ordinary Euclidean boundary length, including all faces of a generic section. The conditional limit is weak convergence as the positive deficit threshold tends to zero. The normal-coordinate tie sets and planes through cube vertices have spherical measure zero. No assertion is made for offset sections, oblique parallelepipeds, or non-Haar orientation measures.

## Proof
**1. Known sharp maximum and exact local face formulas.** The maximizers of central cube-section perimeter, up to signed permutations, are the normals \((1,1,0)/\sqrt2\), with value \(P_*=4(1+\sqrt2)\); see König--Koldobsky [2], which cites Pełczyński's earlier three-dimensional proof. The same work gives the following piecewise section formula after scaling from the half-unit cube to \(C\). It can also be derived by intersecting the cutting plane with each of the six cube faces. For arbitrary ordered nonnegative normal components \(a\ge b\ge c\), homogeneity allows \(b=1\) near the maximum and \(a=1+r\), \(c=q\). The section is a quadrilateral exactly when \(r\ge q\), and a hexagon exactly when \(r<q\). In these respective regimes, with \(H(x,y)=\sqrt{x^2+y^2}\),
\[
 P_Q(r,q)=\frac4{1+r}\bigl(H(1+r,1)+H(1+r,q)\bigr),\qquad r\ge q,
\]
\[
\begin{aligned}
 P_H(r,q)=2\biggl[&\frac{2+r-q}{1+r}H(1+r,1)
 +\frac{r+q}{(1+r)q}H(1+r,q)
 +\frac{q-r}{q}H(1,q)\biggr],\quad 0\le r<q.
\end{aligned}
\]
The apparent singular factors in the latter expression cancel on setting \(r=sq\) with \(s\in[0,1]\); indeed the second and third summands respectively become \((s+1)H(1+sq,q)/(1+sq)\) and \((1-s)H(1,q)\). The two formulas agree at \(r=q\). For generic normals all six faces intersect if and only if \(a<b+c\), the familiar triangle chamber; otherwise only four faces contribute. The sharp maximum theorem implies that, for any sufficiently small deficit, all contributing normals lie in arbitrarily small neighborhoods of the 12 maximizing normals.

**2. A uniform two-branch cusp.** Taylor expansion of \(P_Q(t,st)\) for \(s\in[0,1]\) and \(P_H(st,t)\) for \(s\in[0,1]\) gives, uniformly in \(s\),
\[
P_*-P_Q(t,st)=2\sqrt2\,t+O(t^2),\qquad
P_*-P_H(st,t)=2\sqrt2\,t+O(t^2).
\]
The bounded derivatives follow directly from the displayed smooth functions on a compact neighborhood of \((s,t)\in[0,1]\times\{0\}\). Therefore the two cases combine into the sharp square-cusp normal form
\[
\boxed{P_*-P(U)=2\sqrt2\max(r,q)+O((r+q)^2).}
\]
This identity is uniform as \(r,q\downarrow0\), including the quadrilateral--hexagon seam.

**3. Exact Haar area element.** Each of the 48 ordered sign chambers of the unit sphere is parametrized by
\[
\mathbf u(r,q)=\frac{(1+r,1,q)}{\sqrt{(1+r)^2+1+q^2}},\quad r\ge0,\quad 0\le q\le1.
\]
(The global range also requires \(q\le1\); this does not restrict the near-maximal neighborhood.) Direct evaluation of the scalar triple product gives
\[
\left\lVert\frac{\partial\mathbf u}{\partial r}\times
\frac{\partial\mathbf u}{\partial q}\right\rVert
 =\frac1{\bigl((1+r)^2+1+q^2\bigr)^{3/2}}
 =\frac1{2\sqrt2}+O(r+q).
\]
The Haar probability density in each chamber is this area element divided by \(4\pi\). The number 48 is \(3!\) permutations times \(2^3\) coordinate-sign choices, with almost-everywhere disjoint chambers; exactly four chambers meet at each of the 12 oriented maximizing normals.

**4. Integration and marked weak limit.** Let \(h=\varepsilon/(2\sqrt2)\). The square-cusp expansion, together with strict global maximization and compactness of the sphere, confines the event to \(r,q=O(h)\) and sandwiches it between \([0,h-Ch^2]^2\) and \([0,h+Ch^2]^2\) in every chamber for sufficiently small \(h\) and a fixed \(C>0\). As a result,
\[
\begin{aligned}
\Pr(P>P_*-\varepsilon)
 &=\frac{48}{4\pi}\left[\frac1{2\sqrt2}h^2+O(h^3)\right]\\
 &=\frac{3\sqrt2}{8\pi}\varepsilon^2+O(\varepsilon^3).
\end{aligned}
\]
For any bounded continuous function \(F\) on \([0,\infty)^2\), the same change of variables and dominated convergence yield
\[
\lim_{\varepsilon\downarrow0}
 \mathbb E\left[F(r/h,q/h)\mid P>P_*-\varepsilon\right]
 =\int_0^1\int_0^1F(v,w)\,dv\,dw.
\]
Since \(N=6\) exactly when \(q>r\), the marked six-sided law follows; the diagonal has zero limiting mass. The normalized shortfall converges to \(\max(V,W)\), which has cumulative distribution \(t^2\) for \(0\le t\le1\), i.e. \(\operatorname{Beta}(2,1)\). Symmetry gives the discrete maximizing-normal label uniform on 12 possibilities and independent of local coordinates. This completes the proof.

## Verification
The included Python program `verify_cube_section_perimeter.py` uses a geometric plane--cube-edge intersection and an independent planar convex-hull construction to verify the piecewise perimeter and polygon type against 650 random normal directions. It then checks the two uniform Taylor branches and the exact spherical Jacobian. Finally it draws 3,200,000 independent Gaussian directions, normalizes them implicitly, and tests the near-maximal tail and the balance of section types at three small deficits. Run `python3 verify_cube_section_perimeter.py` with Python 3 and NumPy. These finite computations test implementation and constants; the proof above establishes the infinite limiting statement.

## Relationship to prior work
Lonke [1] studies Haar-random cube sections and determines expected vertex counts. His analysis implies the unconditional probability of a hexagonal section but does not mark perimeter extremes. The exact cube hexagon probability, and a formula for all rectangular boxes, are also available in [3]. In contrast, the present conditional probabilities concern vanishing perimeter deficit, and the unconditional hexagon rate does not imply a half--half extreme-type split. König and Koldobsky [2] prove the global maximizing normal (already treated in three dimensions by Pełczyński) and give the exact deterministic, piecewise perimeter as a function of orientation; that known geometric formula underlies our calculation. The new assertions are the Haar upper-tail coefficient and the joint square-law including its sharp combinatorial split. These follow by analyzing a nonsmooth *two-variable* normal form at the maximizing set and then evaluating its spherical probability. They are not claimed as consequences of an unknown independent result, nor is the deterministic maximizing direction claimed new. The relevant published published-finding corpus findings on cube-section face counts [3] and projection-perimeter moments [4] have different marginal observables and do not state this conditional extreme-perimeter law.

## Limitations
The conditional law concerns central sections of one fixed Euclidean cube under Haar-uniform orientations. There is no claim of an exact finite-threshold perimeter distribution, an improved global perimeter maximum, a quantitative conditional convergence rate, or an extension to other dimensions. The proof makes essential use of known sharp global maximization; the first-order local expansion is nonsmooth across a polygon-type seam. Historical priority cannot be ruled out in literature not indexed or available to this review. Independent mathematical validation has not been performed.

## References
[1] Y. Lonke, *On random sections of the cube*, arXiv:math/9812123v1, first public version 1998-12-21, https://arxiv.org/abs/math/9812123.

[2] H. König and A. Koldobsky, *On the maximal perimeter of sections of the cube*, arXiv:1806.08659v1, 2018-06-22, subsequently *Advances in Mathematics* 346 (2019), 773–804, https://arxiv.org/abs/1806.08659.

[3] *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.

[4] *Haar-random planar projection perimeter moments of all orthotopes*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-haar-random-planar-projection-perimeter-moments-of-all-orthotope--5f6a2c7bb90c.
