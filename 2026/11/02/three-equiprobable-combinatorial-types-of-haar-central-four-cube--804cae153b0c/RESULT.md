# Three equiprobable combinatorial types of Haar central four-cube sections

## Finding
Let \(Q=[-1,1]^4\). Choose an unoriented central hyperplane \(H=U^\perp\) by the rotationally invariant (Haar) distribution on the Grassmannian of three-planes through the origin, and put \(P=Q\cap H\). With probability one \(P\) is a simple three-polytope. Its **complete facet-size distribution** is
\[
\begin{array}{c|c|c}
\text{facet sizes (with multiplicity)}&\text{face vector }(f_0,f_1,f_2)&\text{probability}\\
4,4,4,4,4,4&(8,12,6)&1/3\\
3,3,5,5,5,5,5,5&(12,18,8)&1/3\\
4,4,4,4,4,4,6,6&(12,18,8)&1/3
\end{array}
\]
These three facet inventories distinguish all generic combinatorial types. In particular, conditional on the already-known \((12,18,8)\) face vector, the two combinatorial types are equiprobable.

## Assumptions and scope
All points and geometric dimensions refer to Euclidean \(\mathbb R^4\); \(Q\) has sidelength two. The hyperplane passes through the cube center and its unit normal has uniform surface measure on \(S^3\), with antipodal normals identified. Inessential exceptional normals (zero coordinates or vanishing signed coordinate sums) form a finite union of proper great spheres and hence have probability zero. The term facet-size means the number of edges of a two-dimensional facet polygon. No assertion is made for noncentral affine sections or for exceptional directions.

By coordinate permutations and independent sign changes, almost every normal admits a unique representative with sorted strictly positive coordinates \(0<a<b<c<d\). Define the two chamber coordinates
\[
X=d-a-b-c,\qquad Y=d+a-b-c.
\]
Here \(X<Y\). The three facet profiles in the table occur, respectively, in the open chambers \(X>0\), \(X<0<Y\), and \(Y<0\).

## Proof
**1. Exact chamber classification.** The vertices of the four-cube are its sixteen sign vectors \(\epsilon\in\{-1,1\}^4\). For a generic normal, each vertex of its central section occurs at precisely one crossed four-cube edge. An edge varying coordinate \(i\) with the other three signs fixed is crossed exactly when
\[
\left|\sum_{j\ne i}\epsilon_j u_j\right|<|u_i|.
\]
For a positive strictly ordered normal, the sign of every signed coordinate sum is determined by the inequalities \(a<b<c<d\) except for the signs of \(X\) and \(Y\). Indeed, the only possibly vanishing one-versus-three split is \(d-a-b-c=X\), and the only possibly vanishing two-versus-two split is \(d+a-b-c=Y\). Therefore the pattern of edge crossings and its incidence with the eight possible coordinate facets \(\{x_i=\pm1\}\) is constant on each of the three connected open chambers.

For clarity, the exact edge-incidence enumeration can be done without a polytope library: fix \(i\), run over all eight sign assignments to the other three coordinates, retain the crossing if the displayed strict inequality holds, form its four section coordinates (the varying coordinate is the negative weighted sign sum divided by \(u_i\)), and count the resulting vertices lying on each of \(x_j=1\) and \(x_j=-1\). Representative integer normals, together with the directly obtained inventory of positive-area facets, are
\[
\begin{array}{c|c|c}
\text{chamber}&(a,b,c,d)&\text{facet sizes}\\
X>0&(1,2,3,7)&4^6\\
X<0<Y&(1,2,3,5)&3^2,5^6\\
Y<0&(6,8,10,11)&4^6,6^2.
\end{array}
\]
These representatives avoid every exceptional signed sum. The crossing test above, plus constancy within each chamber, proves both completeness and the claimed facet inventories. The corresponding vertex counts are eight, twelve, twelve.

**2. Exact measure of the dominant chamber.** Write the Haar normal as \(U=G/\|G\|\) where \(G_1,\ldots,G_4\) are independent standard real Gaussians. A prescribed four-cube edge directed along coordinate \(i\) is crossed exactly when
\[
|G_i|>\left|\sum_{j\ne i}\epsilon_jG_j\right|.
\]
The right side is the absolute value of a centered Gaussian of variance three, independent of \(G_i\). Hence, with \(C\) a standard Cauchy random variable, the crossing probability equals
\[
\Pr(|C|>\sqrt3)=1-\frac2\pi\arctan\sqrt3=\frac13.
\]
There are thirty-two cube edges, so the expected section vertex count equals \(32/3\). By Step 1, if \(p=\Pr(X>0)\), the vertex count takes values eight and twelve, and
\[
8p+12(1-p)=32/3,\qquad p=1/3.
\]
The already-published two-point face-vector law gives the same marginal, but does not separate the two twelve-vertex chambers.

**3. An orthogonal involution of the nondominant cone.** Consider the Euclidean reflection in the hyperplane \(Y=0\), whose normal is \((1,-1,-1,1)\). In ordered coordinates this reflection is
\[
T(a,b,c,d)=(a,b,c,d)-\frac{Y}{2}(1,-1,-1,1).
\]
It is orthogonal, involutive, and satisfies \(Y(Tu)=-Y(u)\). In expanded form
\[
Tu=\frac12(a+b+c-d,\ a+b-c+d,\ a-b+c+d,\ -a+b+c+d).
\]
Suppose \(0<a<b<c<d\) and \(X<0\). The first new coordinate is \(-X/2>0\), while consecutive differences of transformed coordinates are \(d-c\), \(c-b\), and \(b-a\), respectively. Thus the reflected coordinates remain positive and strictly increasing. Moreover \(X(Tu)=-2a<0\), so the entire nondominant cone is preserved. The map interchanges \(X<0<Y\) and \(Y<0\), since it negates \(Y\), and it is its own inverse.

The distribution of the sorted absolute Gaussian coordinates has density proportional to \(\exp(-\|u\|^2/2)\) on this ordered cone. Orthogonality of \(T\) preserves its norm, Jacobian, and therefore Gaussian measure; equivalently, it preserves the induced angular Haar measure. Consequently the two nondominant chambers have equal probability. Their total probability is \(2/3\) by Step 2, and so each has probability exactly \(1/3\). This proves the complete claim.

## Verification
The included `verify.py` uses only the Python standard library and exact rational arithmetic to independently enumerate crossed edges and all facet sizes for generic increasing integer-coordinate normals (1,501 normal vectors checked, excluding the exact signed-sum boundaries). It verifies all three representative inventories and checks that the reflection is involutive, norm-preserving, order-preserving and swaps the two nondominant chamber labels. A deterministic 75,000-trial Gaussian experiment corroborates the three Haar probabilities; these trials are not the proof of equiprobability. Running `python3 verify.py` from the extracted package must print `ALL_FOURCUBE_THREE_TYPE_CHECKS_PASSED`.

## Relationship to prior work
Ambrus, *Critical central sections of the cube* (first public version 2021-07-30), analyzes volume-critical normals, including dimension four, not the full probability law of facet inventories. Egan's earlier visual classification already lists exactly the three generic inventories, without giving Haar probabilities; this classification is not claimed as new. Brandenburg and Meroni, *Combinatorics of slices of cubes* (first posted 2025-10-10), give certified enumeration of three generic central combinatorial types of the four-cube, again not their angular probabilities. The published *Exact two-point face-vector law for random central sections of the four-cube* proves probabilities \(1/3\) and \(2/3\) for the two face vectors; it cannot distinguish the two different inventories having the same face vector. The contribution here is the additional, exact **conditional split** and the non-obvious reflection explaining its equality. An exact classification of types or an exact vertex-count expectation alone does not imply this conditional probability statement.

## Limitations
The conclusion is for the symmetric four-cube and Haar-random *central* hyperplanes only. The reflection is not a global symmetry of all normal directions; it preserves only the nondominant ordered cone. It does not imply equal probabilities for anisotropically sampled normals, rectangular four-dimensional orthotopes, affine sections, or sections in other dimensions. Historical priority is provisional: an unindexed stereological treatment might contain the same conditional distribution. No independent mathematical audit is claimed.

## References
1. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778, initial posting 2021-07-30, https://arxiv.org/abs/2107.14778.
2. M.-C. Brandenburg and C. Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265, initial posting 2025-10-10, https://arxiv.org/abs/2510.09265.
3. G. Egan, *Slice*, 2002-03-11, https://www.gregegan.net/APPLETS/27/27.html (known three possible facet inventories).
4. *Exact two-point face-vector law for random central sections of the four-cube*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-two-point-face-vector-law-for-random-central-sections-of-t--88770003c8ac.
