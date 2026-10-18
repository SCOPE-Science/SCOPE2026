# Sharp affine-plane section area and directional balancing of the regular cuboctahedron

## Finding
Let \(C\subset\mathbb R^3\) be the edge-\(\sqrt2\) regular cuboctahedron
\[
 C=\operatorname{conv}\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\}
 =[-1,1]^3\cap\{x:\|x\|_1\le2\}.
\]
For an affine plane \(H\), let \(A(H)\) be the two-dimensional Euclidean area of \(C\cap H\), taken as zero if the intersection has dimension less than two. Then
\[
 \boxed{A(H)\le 3\sqrt3.}
\]
Equality holds **if and only if** \(H\) is one of the four central planes \(\pm x_1\pm x_2\pm x_3=0\), with simultaneous reversal of signs identified. The exact range of areas among central planar sections is
\[
 \boxed{4\le A(u^\perp)\le3\sqrt3.}
\]
The minimum \(4\) occurs exactly when \(u\) points along a coordinate axis; the maximum occurs exactly when \(u\) points along a body diagonal.

More precisely, write \(a\ge b\ge c\ge0\) for the sorted absolute coordinates of a nonzero normal \(u\). If \(a>c\), the complete central-area formula is
\[
 \boxed{A(u^\perp)=\frac{2\sqrt{a^2+b^2+c^2}\,(2a^2+2ab-b^2-3c^2)}{(a+b)(a^2-c^2)}.}
\]
At \(a=b=c>0\), the value is the continuous limit \(3\sqrt3\). At fixed \(a,b\) with \(a\ge b>0\), the area strictly increases as \(c\) increases from \(0\) to \(b\), except for the endpoint interpreted by continuity.

Finally, all parallel sections in a maximizing orientation admit the exact profile
\[
 \boxed{A(\{x_1+x_2+x_3=h\})=\frac{\sqrt3}{8}(h^2-12|h|+24),\quad |h|\le2.}
\]
For \(|h|>2\) the intersection is empty. This profile is strictly decreasing with \(|h|\) on \([0,2]\).

## Assumptions and scope
All statements concern Euclidean areas and the fixed coordinate normalization above; its edge length is \(\sqrt2\). A central plane contains the origin. The normal is nonzero; replacing it by a scalar multiple or changing the signs and ordering of coordinates does not change the central area. Degenerate intersections of an affine plane have area zero. The central rational formula is evaluated only at \(a>c\); the body-diagonal case is supplied separately, without dividing by zero. The result is three-dimensional and does not cover different truncation depths or arbitrary Archimedean solids.

## Proof
**1. Reduction and the exact polygon.** The twelve displayed vertices are the midpoints of the twelve edges of the containing cube; the 24 cuboctahedral edges are exactly the vertex pairs at Euclidean distance \(\sqrt2\). Signed coordinate permutations reduce every central-plane normal to \(u=(a,b,c)\), \(a\ge b\ge c\ge0\), \(a>0\). First suppose \(a>b>c>0\). Every section vertex lies on an edge crossing \(u^\perp\). In cyclic order, the eight such edges have endpoint pairs

```text
( 1,-1, 0) -- ( 0,-1,-1)
( 1, 0,-1) -- ( 0,-1,-1)
( 0, 1,-1) -- (-1, 0,-1)
( 0, 1,-1) -- (-1, 1, 0)
( 0, 1, 1) -- (-1, 1, 0)
( 0, 1, 1) -- (-1, 0, 1)
( 1, 0, 1) -- ( 0,-1, 1)
( 1,-1, 0) -- ( 0,-1, 1)
```

The list follows directly by testing the 24 edges against the two open half-spaces. If \(v,w\) are endpoints with opposite normal signs, the unique crossing point is
\[
 p(v,w)=\frac{(u\cdot v)w-(u\cdot w)v}{u\cdot v-u\cdot w}.
\]
Substitute these eight points, in the displayed order, into the oriented polygon-area identity
\[
 A(u^\perp)=\frac1{2\|u\|_2}\sum_{j=1}^8 u\cdot(p_j\times p_{j+1}),\qquad p_9=p_1.
\]
Exact algebra gives
\[
 \sum_{j=1}^8u\cdot(p_j\times p_{j+1})
 =\frac{4(a^2+b^2+c^2)(2a^2+2ab-b^2-3c^2)}{(a+b)(a^2-c^2)}.
\]
Thus the asserted central-area formula holds in the open ordering chamber. A section area depends continuously on the normal, so the formula extends to all \(a>c\), including boundary directions; when \(a=b=c\) the section is a regular hexagon with side \(\sqrt2\) and area \(3\sqrt3\).

**2. Directional balancing.** Divide \(a,b,c\) by \(a\) and put \(s=b/a\), \(t=c/a\), \(r=t^2\), so \(0\le r\le s^2\le1\). Let \(F(s,t)\) denote the central area. The formula from step 1 gives
\[
 \frac{F(s,\sqrt r)^2}{4}=W(s,r):=
 \frac{(1+s^2+r)(2+2s-s^2-3r)^2}{(1+s)^2(1-r)^2}.
\]
For \(r<1\), direct differentiation yields
\[
 \frac{\partial\log W}{\partial r}
 =\frac{N(s,r)}{(1+s^2+r)(1-r)(2+2s-s^2-3r)},
\]
where
\[
 N(s,r)=3r^2-(s^2-2s+7)r-2s^4+4s^3-5s^2+6s.
\]
All denominator factors are strictly positive in the stated open domain. Moreover,
\[
 \frac{\partial N}{\partial r}=6r-s^2+2s-7
 \le5s^2+2s-7\le0,
 \qquad N(s,s^2)=6s(1-s)^2\ge0.
\]
Hence \(N(s,r)\ge0\), with strict increase of \(F\) in \(r\) for \(s>0\) and \(r<s^2\). Therefore
\[
 F(s,t)\le F(s,s)=\frac{4(1+2s)\sqrt{1+2s^2}}{(1+s)^2}.
\]
The logarithmic derivative of the right-hand side is exactly
\[
 \frac{6s^2}{(1+s)(1+2s)(1+2s^2)},
\]
positive for \(s>0\). Its maximum for \(0\le s\le1\) is consequently \(3\sqrt3\) at \(s=1\). Equality in both comparisons forces \(s=t=1\), giving precisely the body-diagonal normals.

At the other endpoint, \(F(s,t)\ge F(s,0)\), while
\[
 F(s,0)=\frac{2\sqrt{1+s^2}(2+2s-s^2)}{1+s}\ge4.
\]
Indeed the squared inequality is equivalent to
\[
 (1+s^2)(2+2s-s^2)^2-4(1+s)^2
 =s^3\bigl(4(1-s^2)+s+s^3\bigr)\ge0.
\]
Equality holds only at \(s=t=0\), yielding precisely the coordinate-axis normals. Continuity covers the body-diagonal endpoint.

**3. Affine sections and strict equality.** For each fixed unit normal \(u\), Brunn's section theorem makes the square root of the parallel-section area a concave function of the offset on its interval of support. Central symmetry makes the function even, so \(A(\{u\cdot x=t\})\le A(u^\perp)\le3\sqrt3\).

If an affine plane attains \(3\sqrt3\), its normal must therefore be one of the body-diagonal directions found in step 2. Signed coordinate symmetries reduce the remaining comparison to \(x_1+x_2+x_3=h\). For \(0<h<2\), the six section vertices are the interpolations between the three \(x_1+x_2+x_3=2\) vertices and the six \(x_1+x_2+x_3=0\) vertices along the following edges:

```text
(1,0,1) -- (1,-1,0)
(1,1,0) -- (1,0,-1)
(1,1,0) -- (0,1,-1)
(0,1,1) -- (-1,1,0)
(0,1,1) -- (-1,0,1)
(1,0,1) -- (0,-1,1)
```

The same oriented-area computation now gives \(A=\sqrt3(h^2-12h+24)/8\). At \(h=0\) and \(h=2\), continuity gives respectively the regular hexagon and a triangular facet; central symmetry handles negative \(h\). The derivative is \(\sqrt3(2h-12)/8<0\) for \(0<h<2\). Therefore only \(h=0\) can realize the global upper bound, completing the affine equality classification.

## Verification
Two complementary checks accompany this result. `symbolic_section_check.py` reconstructs the crossing-edge polygons and verifies their area identities and all derivative factorizations by exact symbolic algebra (SymPy). `section_area_check.py` independently uses exact rational arithmetic and a monotone-chain planar convex hull to compare the central formula for 1,018 primitive integer normal triples with \(1\le a\le18\), and the diagonal offset formula for 81 rational offsets. They both executed successfully on the delivered source bytes. The analytic chamber and monotonicity arguments, not this finite sample, establish the continuum theorem.

## Relationship to prior work
Ball's classical cube-slicing theorem makes the cube's largest central planar section perpendicular to a face diagonal; for the edge-midpoint truncated cube studied here, the unique maximizing normal class changes to body diagonals. Matteo's 2014 classification identifies the cuboctahedron as a quasiregular, two-orbit polyhedron and records its truncation construction, rather than its section-area extrema. Feng and Yuan study acute surface triangulation counts, not plane-section areas. Meyer's cross-section-body theorem concerns the general geometry of maximal section functions; only its published abstract was accessible for comparison. Searches of relevant public research records located a study of the largest **inscribed tetrahedron** within the wider cube–octahedron intersection family, and unrelated section side-count laws, but did not identify the present planar-area bound or balancing formula. Absence from searches is not a proof of historical priority.

## Limitations
The area profile and equality classification apply to the single specified three-dimensional cuboctahedron, not to arbitrary cube–octahedron truncation parameters. The exact rational formula covers central planes; for noncentral planes only the global maximum and the explicit body-diagonal parallel-section profile are derived here. No claim is made about perimeter, general affine deformations, higher-dimensional root polytopes, or complete priority. A plausible general reference by Meyer could not be inspected in full; independent mathematical audit remains outstanding.

## References
1. M. Meyer, *Maximal hyperplane sections of convex bodies*, Mathematika **46** (1999), 131–136, DOI:10.1112/S0025579300007622 (general cross-section theory; full text inaccessible during comparison).
2. K. Matteo, *Two-orbit convex polytopes and tilings*, arXiv:1403.2125v1 (10 March 2014), especially Section 4 (cuboctahedral symmetry and truncation).
3. X. Feng and L. Yuan, *Acute Triangulations of the Cuboctahedral Surface*, arXiv:1209.4452v1 (20 September 2012) (surface triangulation, a different invariant).
4. K. Ball, *Cube Slicing in* \(\mathbb R^n\), Proceedings of the American Mathematical Society **97** (1986), 465–473, DOI:10.1090/S0002-9939-1986-0840631-0 (cube benchmark).
