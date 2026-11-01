# Sharp area–perimeter profile of triangles contained in a square

## Finding

For every nondegenerate triangle \(T\subset Q=[0,1]^2\) with area \(A\in(0,1/2]\),
\[
P(T)\le M(A):=\sqrt2+2A+\sqrt{1+(1-2A)^2}.
\]
Equality holds exactly for the eight dihedral images, with repetitions removed, of
\[
\operatorname{conv}\{(0,0),(1,1),(0,2A)\}.
\]
For \(0<A<1/2\) these are eight different unordered triangles (four choices of boundary side for each square diagonal). At \(A=1/2\), they collapse to the four triangles formed by three of the square's four corners. The function \(M\) is strictly increasing and strictly convex; its limiting value as \(A\downarrow0\) is \(2\sqrt2\), the twice-diagonal perimeter of the degenerate limiting segment. This is the complete triangle-restricted fixed-area reverse-isoperimetric profile of a square.

## Assumptions and scope

All areas and perimeters use ordinary Euclidean normalization. The container is the **closed** unit square, the triangle is nondegenerate (three noncollinear points), and area is **exactly** \(A\). The result scales: for a square of side length \(L>0\), the perimeter maximum at area \(a\in(0,L^2/2]\) is \(L M(a/L^2)\). A convex subset with more than three vertices is not within the theorem.

## Proof

**1. Every maximizing triangle spans both coordinate directions.** The class of triples of points in \(Q\) with given unsigned area \(A>0\) is compact (orientation of a maximizing triangle can be fixed as positive), so a maximum exists. Let the vertices be \(v_i=(x_i,y_i)\). Keeping all \(y_i\) fixed, the doubled oriented area is a nonzero linear form in \((x_1,x_2,x_3)\):
\[
D=x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)=\pm2A.
\]
It is nonzero as a linear form because \(A>0\) forces the \(y_i\) not all equal. Suppose the horizontal span of a maximizing triple were strictly smaller than one. A common horizontal translation puts its three abscissas strictly inside \((0,1)\). The area constraint has a nontranslation infinitesimal direction in abscissa space because its kernel has dimension two and contains the one-dimensional translation subspace. There is therefore an open feasible interval of nontranslation perturbations with the same area and the same ordinates. On this interval the perimeter \(\sum_{i<j}\sqrt{(x_i-x_j)^2+(y_i-y_j)^2}\) is strictly convex: for every pair having distinct ordinates the associated summand is strictly convex in its abscissa difference, and the graph formed by such pairs is connected (since the three ordinates are not all equal). Thus a maximum cannot be interior. Contradiction. Interchanging coordinates proves that the vertical span is also one. Translate the triangle to make both coordinate spans precisely \([0,1]\).

**2. Two combinatorial cases.** Relabel by nondecreasing abscissa. The three abscissas are \(0,s,1\) with \(0\le s\le1\); the ordinates are a permutation of \(0,t,1\) with \(0\le t\le1\). Square symmetries and relabelling reduce the six permutations to two configurations.

**Case I: an opposite-corner diagonal is a triangle edge.** After a square symmetry, vertices are \((0,0),(1,1),(s,t)\). Their doubled area equals \(|s-t|=2A\). On each of the two possible line segments inside the unit square, the perimeter
\[
\sqrt2+\sqrt{s^2+t^2}+\sqrt{(1-s)^2+(1-t)^2}
\]
is strictly convex along the segment (the offset \(|s-t|=2A>0\) prevents either distance term from becoming affine). Hence it is maximal only at the segment endpoints, where the third vertex lies on a side of \(Q\). Taking, for example, \((s,t)=(0,2A)\), the perimeter is
\[
\sqrt2+2A+\sqrt{1+(1-2A)^2}=M(A).
\]
The other endpoints give precisely its square-symmetric images.

**Case II: no opposite-corner edge.** By square symmetries and vertex relabelling, write the vertices as \((0,0),(s,1),(1,t)\) with \(s,t\in[0,1]\). The doubled area is \(1-st\), so put \(q:=st=1-2A\), where \(0\le q<1\). The perimeter is
\[
F(s,t)=\sqrt{1+s^2}+\sqrt{1+t^2}+\sqrt{(1-s)^2+(1-t)^2}.
\]
Introduce \(p=s+t\) and \(c=1-q\). Every admissible pair gives \(p\in[2\sqrt q,1+q]\), and each \(p\) in that interval occurs. Direct algebra using \(st=q\) gives
\[
F(s,t)=F_q(p):=U(p)+V(p),\quad
U(p)=\sqrt{p^2+2c+2\sqrt{p^2+c^2}},\quad
V(p)=\sqrt{p^2-2p+2c}.
\]
If \(q\ge1/4\), then \(p\ge2\sqrt q\ge1\). Here \(U'(p)>0\), while \(V'(p)=(p-1)/V(p)\ge0\); thus \(F_q\) is strictly increasing, with its maximum at \(p=1+q\).

If \(0\le q<1/4\), then \(c>3/4\). Writing \(r=\sqrt{p^2+c^2}\), explicit differentiation yields
\[
U''(p)=\frac{N(p,c)}{U(p)^3},\quad
N(p,c)=2c+\frac{2c^2}{r}-\frac{p^2}{r^2}
+\frac{c^2p^2}{r^3}+\frac{2c^3}{r^3}+\frac{2c^2}{r^2}.
\]
All terms after \(-p^2/r^2\) are nonnegative, and \(p^2/r^2\le1\), so \(N(p,c)\ge2c-1>0\). Also \(V''(p)=(1-2q)/V(p)^3>0\). Therefore \(F_q\) is strictly convex, and any maximum occurs at an endpoint. At the endpoint \(p=1+q\), one of \(s,t\) equals one, giving
\[
F_q(1+q)=\sqrt2+(1-q)+\sqrt{1+q^2}=M(A).
\]
At the other endpoint \(p=2\sqrt q\), where \(s=t=\sqrt q\), we obtain
\[
F_q(2\sqrt q)=2\sqrt{1+q}+\sqrt2(1-\sqrt q).
\]
For \(0<q<1/4\), by \(\sqrt{1+q^2}\ge1\) and \(2\sqrt{1+q}\le2+q\),
\[
F_q(1+q)-F_q(2\sqrt q)
\ge\sqrt2\sqrt q-2q>0.
\]
At \(q=0\), the two endpoints tie, but both describe triangles formed by three square corners. In all cases the maximizers of Case II are exactly the corner-diagonal equality triangles already found in Case I. For \(0<q<1/4\) strictness excludes all other pairs; for \(q\ge1/4\), strict increase does the same. The borderline \(q=1/4\) is included in the latter case.

**3. Counting, derivatives, scaling.** A square has two diagonals; for each diagonal and \(0<A<1/2\), the third vertex can lie at the unique area-correct location on each of the four sides, giving eight distinct triangles. When \(A=1/2\) exactly four distinct three-corner triangles remain. Moreover,
\[
M'(A)=2-\frac{2(1-2A)}{\sqrt{1+(1-2A)^2}}>0,\qquad
M''(A)=\frac4{[1+(1-2A)^2]^{3/2}}>0.
\]
This proves the claimed profile, rigidity, and scaling law. \(\square\)

## Verification

Run the included standalone `verify.py` with Python 3.10 or later. It uses only the standard library and reports 151247 deterministic checks: 998 exact-area equality witnesses; 25000 rationally sampled nondegenerate and nearly degenerate triples (the exact arithmetic checks area); and 124750 checks of the Case II one-variable identity and bound. Random sampling is seeded and reproducible. The symbolic identity underlying \(U''\) was separately checked by algebraic reduction with \(r^2=p^2+c^2\); its displayed decomposition and the preceding convexity argument are the analytic verification, independent of finite tests.

## Relationship to prior work

Fattah–Ftouhi–Zuazua [1, §4.1, Proposition 13 and Remark 14] formulate the fixed-area perimeter maximization for convex subsets of prescribed containers as the \(p=1\) case of support-distance approximation, establish polygonal free-boundary structure, and discuss a conjectural triangular-container profile. Their statements neither specialize to nor imply the exact fixed-area **three-vertex square** profile or its equality count. Bogosel [2, Theorems 6 and 10] proves the exact disk-container classification and existence of polygonal maximizers for general polygonal containers, without a square-specific fixed-area triangle formula. The present theorem is restricted to triangles and does not determine the unrestricted square-container optimizer. Related square and triangle geometry records were also compared by the exact object/area/perimeter conditions, with no encompassing result identified.

## Limitations

The upper bound is sharp only within the class of triangles contained in a Euclidean square. It does not solve the fixed-area maximal-perimeter problem for arbitrary convex subsets of the square or for general rectangles. Historical priority of this exact triangle-restricted formula is provisional: the literature search may not uncover older equivalent elementary geometry arguments. Independent mathematical audit has not been performed.

## References

[1] Zakaria Fattah, Ilias Ftouhi, Enrique Zuazua, *Optimal \(L^p\)-approximation of convex sets by convex subsets*, arXiv:2501.00928, first publicly submitted 2025-01-01, §4.1 (https://arxiv.org/abs/2501.00928).

[2] Beniamin Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion constraint*, arXiv:2402.05648, first publicly submitted 2024-02-08, §§2–3 (https://arxiv.org/abs/2402.05648).
