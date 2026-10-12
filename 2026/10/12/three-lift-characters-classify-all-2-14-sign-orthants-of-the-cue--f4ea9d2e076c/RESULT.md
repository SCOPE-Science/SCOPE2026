# Three lift characters classify all \(2^{14}\) sign orthants of the Cueto--Markwig quartic
## Finding
For the fixed valuation vector and smooth Newton subdivision \(\Gamma\) of Cueto--Markwig Example 1.2, let the fifteen nonzero initial coefficient signs \(s_{ij}\in\{\pm1\}\) vary, modulo simultaneous global sign, so there are exactly \(2^{14}=16384\) projective sign orthants. Define \(A=[s_{00}s_{22}>0]\), \(B=[s_{21}s_{31}s_{30}s_{22}<0]\), and \(C=[s_{12}s_{13}s_{22}s_{03}<0]\). If \(k=A+B+C\), then the Viro patchwork of the real quartic near the tropical limit has exactly \(k+1\) connected components, while the Cueto--Markwig lift rules give respectively \(4,8,16,28\) real bitangents for \(k=0,1,2,3\). Each of the eight truth patterns of \(A,B,C\) occurs in exactly \(2048\) projective sign orthants. Consequently the exact orthant census is \(2048\) one-oval quartics with \(4\) real bitangents, \(6144\) quartics with two non-nested ovals and \(8\) real bitangents, \(6144\) three-oval quartics with \(16\) real bitangents, and \(2048\) four-oval quartics with \(28\) real bitangents. In particular, within this fixed tropical chamber, the \(4\)-real-bitangent case never has empty real locus or two nested ovals.

## Assumptions and scope
Let \(q(x,y)\) be a real Puiseux quartic whose coefficient valuations are exactly those of Example 1.2 of Cueto--Markwig, so its tropicalization is the smooth tropical quartic \(\Gamma\) from that example. Every coefficient has nonzero initial term. We vary only the signs \(s_{ij}\in\{\pm1\}\) of those fifteen initial terms. Multiplying every coefficient by \(-1\) leaves the projective curve unchanged, so we normalize \(s_{00}=+1\), leaving \(2^{14}\) sign orthants. The topology statement concerns the real curve near the tropical limit, where Viro patchworking applies, and the bitangent statement uses the generic lifting hypotheses of the cited source.

The three Boolean lift characters are
\[
A=[s_{00}s_{22}>0],\qquad
B=[s_{21}s_{31}s_{30}s_{22}<0],\qquad
C=[s_{12}s_{13}s_{22}s_{03}<0].
\]
These are exactly the three sign inequalities appearing in Table 1 of the source for this tropical quartic.

## Proof
The valuation vector has fifteen lattice points in the degree-four Newton triangle. Exact lower-hull calculation gives sixteen lower two-faces, each a unimodular triangle; their total normalized area is \(16\), so they form the whole smooth Newton subdivision.

For a sign assignment, extend the sign chart to the four reflected copies of the Newton triangle by the usual patchworking rule: at the reflected lattice point corresponding to \((i,j)\), the sign is multiplied by \(\epsilon_x^i\epsilon_y^j\), with \(\epsilon_x,\epsilon_y\in\{\pm1\}\). In each unimodular triangle the local real chart is the segment joining the midpoints of the two sign-changing edges. Gluing equal midpoint coordinates across reflected triangles and identifying antipodal points on the boundary \(|x|+|y|=4\) produces the projective Viro chart. Its connected components are the real ovals near the tropical limit.

The attached verifier performs this construction with exact rational midpoint coordinates for all \(2^{14}\) normalized sign assignments. It proves, exhaustively, that if \(k=A+B+C\), then the patchwork has exactly \(k+1\) components. It also checks that every one of the eight truth patterns of \((A,B,C)\) occurs exactly \(2048\) times.

For the bitangents, Cueto--Markwig Table 1 states that class \((3)\) is always real, class \((1)\) is real exactly when \(A\) holds, classes \((2)\) and \((4)\) exactly when \(B\) and \(C\) hold, and classes \((5),(6),(7)\) exactly under \(B\wedge C\), \(A\wedge C\), and \(A\wedge B\), respectively. Hence the number of real bitangent classes is
\[
1+A+B+C+AB+AC+BC,
\]
which equals \(1,2,4,7\) for \(k=0,1,2,3\). Their theorem gives exactly four real algebraic lifts per real class, yielding \(4,8,16,28\) real bitangents. Combining this with the patchwork component calculation gives the four topology/count strata and their exact orthant multiplicities.

For two components, the \(8\)-bitangent count forces the two non-nested-oval real quartic type; the two-nested-oval type has only \(4\) real bitangents. Thus the \(k=0\) chamber has one oval, and neither the empty nor the two-nested topology occurs among the \(4\)-bitangent orthants of this fixed tropicalization.

## Verification
Run `python verify.py`. The checker uses only the Python standard library. It reconstructs the lower regular triangulation from the valuation vector using exact rational arithmetic, verifies all sixteen triangles are unimodular and fill the Newton triangle, reproduces the four sample rows in Cueto--Markwig Table 2, and exhausts all \(16384\) projective sign orthants. The expected terminal line is:

`VERIFY_OK triangles=16 projective_sign_orthants=16384 patterns=8x2048 census=1oval:2048,2nonnested:6144,3ovals:6144,4ovals:2048 real_bitangents=4,8,16,28`

## Relationship to prior work
Cueto--Markwig prove the sign rules for real lifts and show that each tropical bitangent class has either zero or exactly four real lifts. For Example 1.2 they observe that three sign inequalities govern the real lift count and give one sample sign choice for each of the four possible totals \(4,8,16,28\). Their Table 2 is explicitly a table of sample sign choices; it does not state an exhaustive classification of all sign orthants or the orthant multiplicities.

The present finite classification combines those published lift characters with an exhaustive exact Viro-patchworking calculation for the fixed Example 1.2 subdivision. The new content is the identity “number of patchwork components \(=A+B+C+1\)” over every sign orthant, the \(2048,6144,6144,2048\) census, and the resulting exclusion of the empty and two-nested-oval \(4\)-bitangent types from this tropical chamber.

## Limitations
The classification is for the single fixed valuation vector/Newton subdivision of Example 1.2 and for real curves near the tropical limit. It does not classify sign chambers for other tropical quartics or for arbitrary changes of coefficient valuations. The topological certificate is combinatorial patchworking; it is not a direct numerical sampling of finite real coefficients. A later or unindexed computation could contain the same exhaustive orthant census under different terminology.

## References
1. M. A. Cueto and H. Markwig, *Combinatorics and real lifts of bitangents to tropical quartic curves*, arXiv:2004.10891, first public version 22 April 2020; Discrete & Computational Geometry 69 (2023), 597--658, DOI: 10.1007/s00454-022-00445-1.
2. O. Viro, patchworking theory as cited and used in the preceding source for the real topology near the tropical limit.
