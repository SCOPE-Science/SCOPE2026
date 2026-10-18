# Rectangular lattice kissing distances and interior primitive extremizers

## Finding

Let \(a,b\ge1\) be integers. Among all pairs of disjoint, nonempty lattice polytopes (convex hulls of finitely many integer points) contained in the closed rectangle \(R_{a,b}=[0,a]\times[0,b]\), define their **kissing distance** \(\varepsilon(a,b)\) to be the smallest possible Euclidean separation. Put
\[
M(a,b)=\max_{\substack{0\le p\le a,\ 0\le q\le b\\\gcd(p,q)=1}}(p^2+q^2).
\]
Then for every such \(a,b\),
\[
\boxed{\varepsilon(a,b)=1/\sqrt{M(a,b)}.}
\]
There is always an optimal pair consisting of one integer point and one integer segment.

More precisely, a disjoint pair of lattice polytopes attains this bound if and only if **some exposed edge** of one of them has primitive direction \(v\in\mathbb Z^2\) with \(\|v\|^2=M(a,b)\), and **some integer vertex** \(z\) of the other lies on the immediately neighboring primitive lattice line (integer determinant distance one), with the perpendicular projection of \(z\) onto the supporting line belonging to that edge. The statement includes lower-dimensional polytopes; an edge of a lattice segment counts as an exposed edge.

The corner diagonal is a maximizing primitive direction exactly if \(\gcd(a,b)=1\). When \(\gcd(a,b)>1\), its norm is unattainable as a primitive direction. An infinite family exhibits a less obvious phenomenon: for every integer \(t\ge1\) with \(t\equiv1\pmod{21}\), put \(a=28t\), \(b=36t\). The **unique maximizing pair of absolute direction coordinates** is
\[
(p,q)=(28t-1,36t-1),
\]
strictly interior to the allowed coordinate rectangle, and hence
\[
\boxed{\varepsilon(28t,36t)=\frac1{\sqrt{(28t-1)^2+(36t-1)^2}}.}
\]
For \(t=1\), the maximizing primitive squared length is \(1954\), attained by the segment from \((0,0)\) to \((27,35)\) and the lattice point \((10,13)\).

## Assumptions and scope

The metric is the ordinary Euclidean norm in the given integer coordinates; anisotropic affine changes of coordinates are **not** isometries. A lattice polytope may be a point, segment, or two-dimensional polygon, but it must be nonempty and be the convex hull of integer points inside \(R_{a,b}\). The pair must have empty intersection. The minimum exists since there are finitely many lattice subsets of the rectangle. In the formula for \(M(a,b)\), the convention \(\gcd(0,1)=1\) is used; \((0,0)\) is excluded automatically. Since \(a,b\ge1\), the candidate \((1,1)\) guarantees \(M(a,b)\ge2\).

## Proof

**1. A universal geometric lower bound.** Let \(P,Q\) be a disjoint pair and choose closest points \(x\in P\), \(y\in Q\). The segment joining them is perpendicular to parallel separating supports at these points. In two dimensions there are only three relevant face configurations: two vertices, a vertex and an edge, or two parallel edges. If both are vertices, their integral distinct coordinates give distance at least \(1\), which exceeds \(1/\sqrt{M(a,b)}\).

Otherwise, choose an edge \(E\) of one polytope lying in the active separating support, and an integer vertex \(z\) of the other polytope on its opposite parallel supporting line. Write the primitive integer direction of \(E\) as \(v=(v_1,v_2)\). Because its endpoints lie in \(R_{a,b}\), \(|v_1|\le a\) and \(|v_2|\le b\). For any integer vertex \(u\) of \(E\), the supporting-line distance is
\[
\frac{|\det(v,z-u)|}{\|v\|}.
\]
The numerator is a **positive integer**: it cannot vanish since the two parallel supports are disjoint. Hence the distance between these supports, and therefore the distance between \(P,Q\), is at least \(1/\|v\|\ge1/\sqrt{M(a,b)}\). This argument applies equally to a point versus a segment and to parallel supporting segments. In particular, nonparallel edge interiors cannot be simultaneous closest faces.

**2. Every maximizing primitive vector has a geometric witness.** Let \((p,q)\) attain \(M(a,b)\). Both coordinates are positive: a vector along one coordinate axis is primitive only with nonzero coordinate one, but \((1,1)\) has larger squared norm. Thus \(\gcd(p,q)=1\), with \(p,q\ge1\). If \(p=1\), choose \((x,y)=(0,1)\). Otherwise, choose an integer \(x\in\{1,\ldots,p-1\}\) solving \(qx\equiv-1\pmod p\), and set \(y=(1+qx)/p\). This yields \(0\le x\le p\), \(0\le y\le q\), and \(py-qx=1\). The perpendicular projection of \((x,y)\) onto the segment from \((0,0)\) to \((p,q)\) lies in its **relative interior**, because the coordinates lie in that box, the point is not an endpoint, and the dot product is strictly between zero and \(p^2+q^2\). Consequently, the distance from this lattice point to that lattice segment equals \(1/\sqrt{p^2+q^2}\). Both sets lie in \(R_{a,b}\) and are disjoint. This matches Step 1.

**3. Characterization of equality.** Suppose a pair realizes the minimum. Since \(M\ge2\), its distance is less than \(1\), so a vertex–vertex closest pair is impossible. Step 1 therefore supplies a supporting edge with primitive direction \(v\) and an integer vertex \(z\) on the opposite supporting line. Equality throughout its two bounds forces \(\|v\|^2=M(a,b)\) and \(|\det(v,z-u)|=1\). The closest points lie along the perpendicular connecting the supports; thus the projection of \(z\) lies on \(E\). Conversely, a disjoint pair having such an edge and vertex has distance at most their point-to-edge distance \(1/\sqrt M\), and Step 1 says it cannot be smaller. This proves the asserted if-and-only-if description.

**4. Coprime corner criterion.** The direction \((a,b)\) has the uniquely largest possible coordinatewise nonnegative norm \(\sqrt{a^2+b^2}\). It belongs to the primitive set exactly when \(\gcd(a,b)=1\). If it does not, every primitive vector has strictly smaller squared norm.

**5. Infinitely many interior maximizers.** Let \(t\equiv1\pmod{21}\), \(a=28t\), \(b=36t\), and \((p,q)=(a-1,b-1)\). The identity \(\gcd(28t-1,36t-1)=\gcd(28t-1,8t)=1\) follows because \(28t-1\) is coprime to \(t\) and odd. Thus \((p,q)\) is primitive.

Any primitive competitor strictly interior to both boundary sides, meaning \(u\le a-1\) and \(v\le b-1\), has squared norm at most \((a-1)^2+(b-1)^2\), with equality only at \((p,q)\). At the side \(u=a\), the three topmost values \(v=b,b-1,b-2\) are nonprimitive: the first shares \(4t\), the second shares \(7\) (since \(t\equiv1\pmod7\)), and the third shares \(2\) with \(a\). Thus a primitive vector on that side has \(v\le b-3\). Similarly, at \(v=b\), the three rightmost \(u=a,a-1,a-2\) share respectively \(4t\), \(3\) (since \(t\equiv1\pmod3\)), or \(2\) with \(b\), so a primitive vector on the top has \(u\le a-3\). Finally,
\[
(a-1)^2+(b-1)^2-[a^2+(b-3)^2]=88t-7>0,
\]
\[
(a-1)^2+(b-1)^2-[(a-3)^2+b^2]=40t-7>0.
\]
So no primitive boundary vector is competitive. The indicated interior direction is uniquely optimal, completing the proof.

## Verification

Run `python3 rectangular_kissing_check.py` using the Python standard library. It performs exact rational-arithmetic enumeration of all disjoint lattice point–segment configurations inside each \([0,a]\times[0,b]\) for \(1\le a,b\le5\), compares the minima to \(1/M(a,b)\) in squared-distance form, and reconstructs Bézout witnesses. It also checks the interior-extremizer family at \(t=1,22,43,64\). The enumerations are **sanity checks only**; Steps 1–5 prove the infinite parameter claims.

## Relationship to prior work

Deza, Onn, Pokutta, and Pournin introduce and bound Euclidean distances between disjoint lattice polytopes in **cubes** [1]. Deza, Liu, and Pournin subsequently determine the exact two-dimensional **square** value \(\varepsilon(k,k)=1/\sqrt{k^2+(k-1)^2}\) for \(k\ge2\) [2]. That formula is recovered here by maximizing primitive directions on a square, but it does not determine the anisotropic rectangular values or imply their arithmetic interior-optimum phenomenon: a nonuniform rescaling changes Euclidean distances. The later work on three-dimensional cubes and higher-dimensional bounds [3,4] addresses different parameters and dimensions.

## Limitations

The formula computes the geometric optimum by a finite arithmetic maximization rather than supplying a single closed expression in \(a,b\). The interior example is an infinite family, not a classification of all rectangles with interior winners. The result is about the integer lattice and Euclidean distance; it does not claim an analogue for arbitrary lattices, higher-dimensional boxes, or other norms. It does not establish that no unpublished or unindexed equivalent argument exists. All scientific checks described here are internal reproducibility checks, not independent certification.

## References

1. A. Deza, S. Onn, S. Pokutta, L. Pournin, *Kissing polytopes*, arXiv:2305.18597v1 (first submitted 2023-05-29), revised v2 2023-11-29; SIAM J. Discrete Math. 38 (2024), 2643–2664.
2. A. Deza, Z. Liu, L. Pournin, *Small kissing polytopes*, arXiv:2412.03479v1 (2024-12-04), Theorem 1.1 and Section 3; Vietnam J. Math. 53 (2025), 901–913.
3. A. Deza, Z. Liu, L. Pournin, *Kissing polytopes in dimension 3*, arXiv:2502.19554v1 (2025-02-26).
4. A. Deza, L. Pournin, *Flat simplices and kissing polytopes*, arXiv:2601.03183v1 (2026-01-06).
