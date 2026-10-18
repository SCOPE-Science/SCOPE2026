# Eleven exact tetrahedral volume levels in the regular dodecahedron

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(P\subset\mathbb R^3\) be the regular dodecahedron with twenty vertices
\[
V=\{(\pm1,\pm1,\pm1)\}\ \cup\
\{(0,\pm\varphi^{-1},\pm\varphi),
(\pm\varphi,0,\pm\varphi^{-1}),
(\pm\varphi^{-1},\pm\varphi,0)\},
\]
with independent choices of all displayed signs. For every unordered subset \(Q\subset V\) of four *distinct* vertices, write \(T_Q=\operatorname{conv}(Q)\), allowing zero-volume configurations. All \(\binom{20}{4}=4845\) resulting tetrahedral volumes belong to **exactly eleven levels**. Each level and its complete multiplicity appears below. Every volume is \((a+b\varphi)/6\); the table lists the pair \((a,b)\), its occurrence count through a fixed dodecahedron vertex, and its total occurrence count.

| \(a\) | \(b\) | Through fixed vertex | All unordered quadruples |
|---:|---:|---:|---:|
| 0 | 0 | 99 | 495 |
| 8 | -4 | 64 | 320 |
| -4 | 4 | 180 | 900 |
| 4 | 0 | 222 | 1110 |
| -8 | 8 | 24 | 120 |
| 0 | 4 | 180 | 900 |
| 8 | 0 | 80 | 400 |
| -4 | 8 | 30 | 150 |
| 4 | 4 | 64 | 320 |
| 0 | 8 | 24 | 120 |
| 16 | 0 | 2 | 10 |

The levels are ordered by increasing volume. In particular, precisely \(495\) vertex quadruples are coplanar. There are \(10\) maximum-volume vertex tetrahedra, of volume \(8/3\); the next lower vertex-supported volume is \(4\varphi/3\), attained \(120\) times. The strict **vertex-supported** relative gap is \(1-\varphi/2\). The count of ten regular maximizing tetrahedra is classical; the finding is the **complete eleven-level distribution and its multiplicities**, not the existence of the classical tetrahedron compound.

For a uniformly sampled four-element subset of vertices, the exact moments, including degeneracies, are
\[
\mathbb E\operatorname{Vol}(T_Q)=\frac{216+344\varphi}{969},
\qquad
\mathbb E[\operatorname{Vol}(T_Q)^2]=\frac{8000}{8721}.
\]

## Assumptions and scope

The vertex model is unscaled as written: its circumradius is \(\sqrt3\), not one. The classification is over distinct unordered four-element **vertex subsets** and includes degenerate quadruples. It is not a claim about all possible vertices of arbitrary tetrahedra contained in \(P\); in particular, the positive volume gap does not extend to freely placed tetrahedra. The classification is exact, not a numerical histogram.

## Proof

Set \(R=\mathbb Z[\varphi]\), using the reduction \(\varphi^2=\varphi+1\) and \(\varphi^{-1}=\varphi-1\). Every coordinate of every vertex belongs to \(R\). For distinct \(v_0,v_1,v_2,v_3\in V\), let
\[
\Delta(v_0,v_1,v_2,v_3)=
\det(v_1-v_0,v_2-v_0,v_3-v_0).
\]
The associated volume is \(|\Delta|/6\), including zero if the vertices are coplanar. Encode an element of \(R\) by its unique integer pair \((a,b)\), meaning \(a+b\varphi\). Integer-pair addition and multiplication are
\[
(a,b)+(c,d)=(a+c,b+d),\qquad
(a,b)(c,d)=(ac+bd,ad+bc+bd).
\]
These identities follow by substituting \(\varphi^2=\varphi+1\), so all subsequent calculations take place in an exact ordered quadratic field.

The regular dodecahedron is vertex-transitive. Fix \(v=(1,1,1)\); for each unordered triple of the remaining \(19\) vertices compute \(\left|\Delta(v,w_1,w_2,w_3)\right|\). The coefficient-pair histogram has exactly the eleven rows in the third column above and totals \(\binom{19}{3}=969\). This is a *complete finite calculation*: the supplied `verify.py` defines the coordinates with sign loops, enumerates every triple, and computes determinants using only integer pairs. Its `EXPECTED` dictionary and `spectrum.csv` give the complete coefficient-pair certificate. Exact sign comparisons use \(a+b\varphi=(2a+b+b\sqrt5)/2\) and integral square comparisons, without rounding.

Every quadruple is incident to exactly four of its vertices. Vertex-transitivity makes the fixed-vertex histogram independent of the chosen vertex, so if a determinant level has \(h\) incidences through one vertex, its global multiplicity is \(20h/4=5h\). This proves all eleven global multiplicities and exhausts \(\binom{20}{4}=4845\) unordered vertex quadruples. Since \(3/2<\varphi<5/3\), the eleven displayed values are distinct and in the stated order.

For an independent exact consistency argument, let \(X\) be the \(20\)-by-\(4\) matrix with rows \((1,v)\) for \(v\in V\). Central symmetry and coordinate symmetries give \(X^{\mathsf T}X=20I_4\), using \(\|v\|^2=3\). By Cauchy–Binet,
\[
\sum_{\lvert Q\rvert=4}\Delta(Q)^2=\det(X^{\mathsf T}X)=20^4=160000.
\]
The table independently gives this exact sum and the stated second moment after division by \(36\binom{20}{4}\). Summing the eleven volumes weighted by multiplicities gives the first moment. The ten regular tetrahedra in the classical two compounds have circumradius \(\sqrt3\) and volume \(8/3\); since the highest table level is also \(8/3\) and has multiplicity ten, the table identifies precisely those classical regular configurations as the vertex-supported maxima. The attached checker additionally computes all \(4845\) squared determinants independently as Gram determinants of the three edge vectors and tests equality case by case.

## Verification

Execute `python3 verify.py` from the extracted package directory; no nonstandard Python packages are required; the included `spectrum.csv` must be next to `verify.py`. The program enumerates all \(4845\) unordered quadruples, verifies the separate \(969\)-triple fixed-vertex count, checks the exact Gram identity for each quadruple, verifies the complete distribution against `spectrum.csv` and the internal expected table, and checks the Cauchy–Binet moment. All computations use integer pairs; floating point is absent from the proof and certificate.

## Relationship to prior work

Horváth's 2014 preprint on the Fejes-Tóth icosahedron inequality investigates volume extremals for sphere-inscribed polyhedra, supplying an older geometric extremal context, but not the distribution of tetrahedral volumes selected from the twenty dodecahedron vertices. Classical sources on the regular dodecahedron's compound of ten regular tetrahedra establish the top row's geometric configuration. Makai and Tarnai (2018) provide a complete account of colourings by five regular tetrahedra and explicitly identify the ten regular tetrahedra; their paper does not state the eleven-level nonregular determinant spectrum or its multiplicities. A publicly indexed separate result gives a five-level tetrahedral spectrum for the *regular icosahedron* (twelve vertices); it concerns a different vertex set and does not imply the present dodecahedral counts.

## Limitations

The claim is a finite vertex-configuration classification, not a classification of freely inscribed tetrahedra or a new universal convex-geometry inequality. It is computed from the exact conventional coordinate model and proved by exhaustive finite calculation with an independently checked Gram calculation and Cauchy–Binet identity. The maximum-volume regular tetrahedron compound itself is established classical geometry and is not claimed as original. Priority relative to unindexed tables or older computational catalogues of dodecahedral tetrahedra cannot be ruled out by the documented searches. Independent mathematical review has not been performed.

## References

1. Ákos G. Horváth, *On the icosahedron inequality of László Fejes-Tóth*, arXiv:1411.5819 (first arXiv version 2014-11-21), https://arxiv.org/abs/1411.5819.
2. Endre Makai, Jr. and Tibor Tarnai, *A colouring problem for the dodecahedral graph*, arXiv:1812.08453 (first arXiv version 2018-12-20), https://ar5iv.labs.arxiv.org/html/1812.08453.
3. Eric W. Weisstein, *Tetrahedron 10-Compound*, MathWorld, https://mathworld.wolfram.com/Tetrahedron10-Compound.html (classical compound and older references; no date inferred for its earliest publication).
4. Public research record, *Complete tetrahedron-volume spectrum and continuous maximum families in the regular icosahedron* (2026-10-11); inspected indexed summary, not full text. The regular icosahedron has twelve vertices, unlike the dodecahedron's twenty.
