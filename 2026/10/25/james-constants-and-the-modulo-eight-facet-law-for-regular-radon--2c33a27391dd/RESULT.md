# James constants and the modulo-eight facet law for regular Radon polygonal planes

## Finding

For each integer \(N\ge6\) with \(N\equiv2\pmod4\), give \(\mathbb R^2\) the norm whose unit ball is the Euclidean regular \(N\)-gon with circumradius \(1\), denoted \(X_N\). Its **classical James constant**
\[
J(X_N)=\max_{\|x\|_N=\|y\|_N=1}\min\{\|x+y\|_N,\|x-y\|_N\}
\]
has the exact two-branch formula
\[
\boxed{J(X_N)=\frac{\sqrt2}{\cos(\pi/N)}
\begin{cases}
\cos^3(\pi/(2N))-\sin^3(\pi/(2N)),&N\equiv2\pmod8,\\
\cos^3(\pi/(2N))+\sin^3(\pi/(2N)),&N\equiv6\pmod8.
\end{cases}}
\]
At least one maximizing ordered pair is a vertex and its Euclidean-perpendicular unit edge-midpoint direction, up to the dihedral symmetries and signs. The formula gives \(J(X_6)=3/2\) and \(J(X_{10})=(3\sqrt5-1)/4\), consistent with previously available special cases. Along the two residue classes,
\[
J(X_N)=\sqrt2\left(1+\frac{\pi^2}{8N^2}
+\sigma_N\frac{\pi^3}{8N^3}+O(N^{-4})\right),
\qquad \sigma_N=\begin{cases}-1,&N\equiv2\pmod8,\\+1,&N\equiv6\pmod8.\end{cases}
\]
Thus the leading Euclidean-limit defect is quadratic, but the next term records the polygon's residue class modulo eight.

## Assumptions and scope

All vector spaces are two-dimensional and real; \(N\) ranges over all integers \(N\ge6\), \(N\equiv2\pmod4\). Let \(\alpha=\pi/N\), \(c=\cos\alpha\), and \(v_j=(\cos(2\pi j/N),\sin(2\pi j/N))\). The unit ball is \(P_N=\operatorname{conv}\{v_0,\ldots,v_{N-1}\}\). Its Minkowski functional is
\[
\|(a,b)\|_N=\frac1c\max_{0\le j<N}
\bigl(a\cos((2j+1)\alpha)+b\sin((2j+1)\alpha)\bigr).
\]
This is a norm because \(N\) is even and \(0\) is interior to \(P_N\). Here isosceles orthogonality means \(\|x+y\|_N=\|x-y\|_N\). The only external structural input is the vertex-reduction theorem for planar polyhedral James constants, stated and cited below; the exact polygon calculations are proved here.

## Proof

**1. Reduction to one vertex.** Theorem 2.13 and Remark 2.14 of Sain--Ghosh--Paul [1] show that for any real two-dimensional polyhedral Banach space the classical James constant is attained by a vertex \(v\) and a unit vector \(w\) isosceles-orthogonal to \(v\), with \(J=\|v+w\|=\|v-w\|\). The theorem's proof bounds the local James constant on each polygonal boundary segment by relevant vertex values using monotonicity of its isosceles-orthogonal direction; it does not require strict convexity. Their Lemma 1.3 (attributed to Gao--Lau) gives uniqueness of that partner up to sign in a normed plane. The dihedral isometry group of \(P_N\) acts transitively on its vertices, so it suffices to calculate this value at \(v_0=(1,0)\).

**2. The perpendicular unit partner.** Since \(N\equiv2\pmod4\), two adjacent polygon vertices are reflected across the vertical axis and have second coordinate \(c\). Thus \(w=(0,c)\) lies on a horizontal top facet of the unit sphere; in particular \(\|w\|_N=1\). Reflection about the horizontal axis is a norm isometry fixing \(v_0\) and exchanging \(w\) with \(-w\). Hence \(v_0\) is isosceles-orthogonal to \(w\). The uniqueness statement in step 1 gives
\[
J(X_N)=\|(1,c)\|_N=\frac1c\max_j
\bigl(\cos\theta_j+c\sin\theta_j\bigr),\qquad
\theta_j=(2j+1)\alpha.
\]

**3. Which facet maximizes?** The vector \((1,c)\) has Euclidean direction \(r=\arctan c\), with \(r<\pi/4\). Write \(u=\alpha/2\), \(t=\tan u\). The identity
\[
 c-\tan(\pi/4-u)=\frac{2t(1-t)}{(1+t^2)(1+t)}>0
\]
holds because \(0<t\le\tan(\pi/12)<1\). Thus \(\pi/4-u<r<\pi/4\). Maximizing \(\cos\theta+c\sin\theta\) over equally spaced facet normals is the same as minimizing the circular angular distance to \(r\). If \(N\equiv2\pmod8\), the two neighboring normals straddling \(r\) are \(\pi/4+u\) and \(\pi/4-3u\), whose midpoint is \(\pi/4-u\); the first is strictly closer. If \(N\equiv6\pmod8\), the neighboring normals are \(\pi/4-u\) and \(\pi/4+3u\), and the first is strictly closer since \(r<\pi/4\). The chosen normal is therefore \(\theta_*=\pi/4+u\) in the first class and \(\theta_*=\pi/4-u\) in the second.

**4. Evaluation and asymptotics.** Substituting \(c=\cos(2u)\) and using elementary trigonometric identities yields
\[
\cos(\pi/4+u)+c\sin(\pi/4+u)=\sqrt2(\cos^3u-\sin^3u),
\]
\[
\cos(\pi/4-u)+c\sin(\pi/4-u)=\sqrt2(\cos^3u+\sin^3u).
\]
Dividing by \(c\) proves the exact formulas for every permitted \(N\). The Taylor expansions \(\cos^3u=1-3u^2/2+O(u^4)\), \(\sin^3u=u^3+O(u^5)\), and \(1/\cos(2u)=1+2u^2+O(u^4)\) give the claimed class-dependent expansion. This is an exact infinite-family argument; no extrapolation from the checker is used.

## Verification

Run `python3 james_polygon_check.py` using Python's standard library. It checks both norm and formula on fourteen polygon orders \(N=6,10,\dots,98\), tests isosceles-orthogonal vertex witnesses and \(448\) sampled local-James values, and reproduces the previously known exact hexagon and decagon special values. The checker provides numerical corroboration only; completeness for every \(N\) comes from steps 1--4.

## Relationship to prior work

Sain, Ghosh, and Paul [1, Theorem 2.13 and Remark 2.14] establish vertex attainment for two-dimensional polyhedral James constants; this general theorem is a **premise, not a new claim**. Mandal, Sain, and Paul [2] show that regular polygons with \(N\equiv2\pmod4\) are Radon unit circles; their verified abstract concerns Radon classification, not exact James constants. Mizuguchi [3] establishes significant sharp results on the classical James constant in Radon planes; published subsequent citations include the bound \(J\le3/2\) and hexagonal equality characterization. Its full text could not be examined, so possible direct coverage of the all-order regular-polygon formula remains an explicit bibliographic risk. Separate publicly indexed calculations already include the regular decagon's value \((3\sqrt5-1)/4\), and this special case is **not** claimed as new. Work on \(4m\)-gonal James constants and on Birkhoff-restricted Massera--Schäffer constants addresses different polygon families or different constants. The asserted addition is the exact classical James constant throughout both infinite \(4m+2\)-gonal residue classes and its cubic-order arithmetic splitting.

## Limitations

The result is restricted to real normed planes with Euclidean-regular \((4m+2)\)-gonal unit balls. It does not determine the complete set of all maximizing pairs; only explicit maximizing vertex pairs are provided. It does not compute generalized James parameters, Birkhoff-restricted constants, or results for nonregular Radon polygons. Exact formulas for individual small polygons may have appeared in earlier work, and the inaccessible full text of [3] leaves unresolved bibliographic risk; novelty is not established by an absence of search hits alone.

## References

1. D. Sain, S. Ghosh, K. Paul, *On isosceles orthogonality and some geometric constants in a normed space*, arXiv:2407.14475v1, first public 19 July 2024, especially Lemma 1.3, Theorem 2.13 and Remark 2.14. https://arxiv.org/pdf/2407.14475
2. K. Mandal, D. Sain, K. Paul, *A complete characterization of Radon planes whose unit spheres are regular polygons*, arXiv:1809.04760, first public 13 September 2018. https://arxiv.org/abs/1809.04760
3. H. Mizuguchi, *The James constant in Radon planes*, Aequationes Mathematicae 94 (2020), 201--217, doi:10.1007/s00010-020-00698-2.
