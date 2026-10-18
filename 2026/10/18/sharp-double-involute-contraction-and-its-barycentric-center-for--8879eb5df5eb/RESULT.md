# Sharp double-involute contraction and its barycentric center for symmetric hexagonal norms

## Finding
For the six-sided Minkowski geometry of Craizer and Martini, the double-involute operator on the central equidistant is an exact barycentric homothety. Its complete nonconstant spectrum has a **single** eigenvalue and its contraction factor is sharply bounded by \(1/4\), with equality exactly for affine-regular hexagonal norms.

Specifically, let \(U_1,\ldots,U_6\) be consecutive vertices of a strictly convex centrally symmetric hexagon, oriented counterclockwise and satisfying \(U_{i+3}=-U_i\), with indices modulo \(6\). Write \([v,w]=\det(v,w)\) and
\[
 a=[U_1,U_2],\qquad b=[U_2,U_3],\qquad c=[U_3,U_4],
\]
and define the positive quantities
\[
 x=b+c-a,\qquad y=c+a-b,\qquad z=a+b-c.
\]
Let \(P\) be any strictly convex hexagon with paired opposite edges parallel to those of \(U\), normalized so that
\[
 U_i=\frac{P_i-P_{i+3}}2,\qquad
 M_i=\frac{P_i+P_{i+3}}2,\qquad i=1,2,3.
\]
Here \(M_1,M_2,M_3\) are the three vertices of the (possibly degenerate) central equidistant of \(P\), in the normalization of the cited polygonal involute construction.

Set
\[
\rho=\frac{xyz}{4abc}
 =\frac{2xyz}{(x+y)(y+z)(z+x)},\qquad
Q=4abc-xyz=ax^2+by^2+cz^2,
\]
\[
(w_1,w_2,w_3)=\frac1Q(by^2,\;cz^2,\;ax^2),\qquad
O=w_1M_1+w_2M_2+w_3M_3.
\]
Then \(w_i>0\), \(w_1+w_2+w_3=1\), and **every** full two-involute step, relabeled back to the original index order, satisfies
\[
M_i^{(k)}=O+\rho^k(M_i^{(0)}-O)
 \quad(i=1,2,3;\ k=0,1,2,\ldots).
\]
Thus \(O\) is the central point of the involute iteration; if the initial central equidistant is nondegenerate, its distance from \(O\) contracts by exactly \(\rho\) on each double step in any norm.

The sharp range is
\[
0<\rho\le\frac14.
\]
Equality holds if and only if \(a=b=c\), equivalently \(U\) is an affine image of the regular hexagon. Every value of \(\rho\) in \((0,1/4]\) occurs for a strictly convex centrally symmetric hexagon. In the equality case, \(w_1=w_2=w_3=1/3\), and the central point is the ordinary centroid of the six vertices of \(P\): \(O=\sum_{i=1}^6P_i/6\).

## Assumptions and scope
All polygons here are planar and nondegenerate, and paired vertices are indexed consistently with the source's constant-width construction. The six-sided assumption means exactly three pairs of parallel opposite edge directions, not a regular Euclidean metric; \(U\) may have unequal side lengths. Scaling \(U\) does not change \(\rho\) or the weights. Convexity forces \(a,b,c>0\) and the three strict triangle inequalities for \(a,b,c\), equivalently \(x,y,z>0\). Conversely any positive \(a,b,c\) satisfying these inequalities is realized, up to common scale, by an admissible \(U\).

The double involute is the **specific** Minkowski polygonal involute defined in Craizer--Martini (2014), not one of the distinct polygonal perpendicular-bisector involutes. We use one *full* step to mean an involute from the central equidistant to the dual direction polygon followed by its involute back to \(U\)-directions; the relabeling is necessary for the displayed index correspondence.

## Proof
**1. Edge coefficients and the first involute.** Let \(d_i=U_{i+1}-U_i\) and let \(\alpha_i\) be the unique edge coefficients
\[
M_{i+1}-M_i=\alpha_id_i,\qquad
\alpha_{i+3}=-\alpha_i.
\]
Closing the triangle \(M_1M_2M_3\) shows, for a scalar \(s\) (possibly zero),
\[
(\alpha_1,\alpha_2,\alpha_3)=s(x,-y,z).
\]
One way to see this is to apply an invertible linear coordinate change taking \(U_1=(1,0)\), \(U_2=(0,1)\), \(U_3=(-b/a,c/a)\), multiply the resulting edge relation by \(a\), and eliminate its two coordinates. The source's involute formula is linear, so it is enough to calculate with \(s=1\); the zero case follows by linearity.

Define the dual vertices and first involute by the source's finite-sum formulas
\[
V_i=\frac{d_i}{[U_i,U_{i+1}]},\qquad
\beta_i=\frac12\sum_{j=i}^{i+2}\alpha_j[U_j,U_{j+1}],\qquad
N_i=M_i+\beta_iV_i.
\]
Substituting \(\alpha_1=x\), \(\alpha_2=-y\), \(\alpha_3=z\), and their opposite negatives, and using \(x=b+c-a\), \(y=c+a-b\), \(z=a+b-c\), gives
\[
(\beta_1,\beta_2,\beta_3)=\tfrac12(xz,-xy,yz).
\]
Consequently
\[
N_i=(1-t_i)M_i+t_iM_{i+1},\qquad
(t_1,t_2,t_3)=\left(\frac z{2a},\frac x{2b},\frac y{2c}\right).
\]
Both sides are three-periodic. The equality \(0<t_i<1\) follows from the strict triangle inequalities.

**2. The dual involute.** Directly from the definition of \(V\) and the three determinants,
\[
([V_1,V_2],[V_2,V_3],[V_3,V_4])
=\left(\frac z{ab},\frac x{bc},\frac y{ca}\right),\qquad
\frac{V_{i+1}-V_i}{[V_i,V_{i+1}]}=-U_{i+1}.
\]
The edge coefficients of \(N\) relative to the dual edges \(V_{i+1}-V_i\) are \(\beta_{i+1}\). Applying the same half-sum formula a second time yields a second involute \(Z_i\) satisfying
\[
Z_i=(1-r_i)N_i+r_iN_{i+1},\qquad
(r_1,r_2,r_3)=\left(\frac x{2c},\frac y{2a},\frac z{2b}\right).
\]
For clarity, the three second-involute half-sums are proportional to
\[
\left(-\frac{x^2yz}{4abc},\frac{xy^2z}{4abc},-\frac{xyz^2}{4abc}\right).
\]
Dividing each by the corresponding dual edge coefficient and determinant gives the displayed \(r_i\). By the source's duality identity, relabeling \(M'_{i+1}=Z_i\) returns the original edge indexing.

**3. Barycentric rank-one identity.** Let \(T\) be the row-stochastic \(3\times3\) matrix describing the passage from the ordered triple \((M_1,M_2,M_3)\) to its relabeled double-involute triple \((M'_1,M'_2,M'_3)\). The two interpolation formulas show that the two off-diagonal entries in each column are equal, and have values
\[
 T_{21}=T_{31}=\frac{y^2}{4ac},\quad
 T_{12}=T_{32}=\frac{z^2}{4ab},\quad
 T_{13}=T_{23}=\frac{x^2}{4bc}.
\]
Because every row sums to one, these identities determine the diagonal entries as well. The elementary identity
\[
ax^2+by^2+cz^2=4abc-xyz
\]
then implies the **exact matrix identity**
\[
T_{ij}=\rho\delta_{ij}+(1-\rho)w_j
\qquad(1\le i,j\le3).
\]
Indeed \((1-\rho)w_1=y^2/(4ac)\), and cyclically likewise for columns two and three. Thus \(M'_i=\rho M_i+(1-\rho)O\). Since \(\sum_iw_i=1\), the weighted center is fixed by this map. Induction proves the stated formula at every integer step. In linear-algebra terms, the spectrum of \(T\) is \(\{1,\rho,\rho\}\), while the action on the nonconstant two-dimensional shape space is multiplication by \(\rho\).

**4. Optimal contraction, rigidity, and range.** Since \(2a=y+z\), \(2b=z+x\), and \(2c=x+y\),
\[
\rho=\frac{2xyz}{(x+y)(y+z)(z+x)}\le\frac14
\]
by multiplying three two-variable arithmetic-geometric-mean inequalities. Equality requires \(x=y=z\), equivalent to \(a=b=c\). After affine normalization this is precisely \(U_3=U_2-U_1\), the centrally symmetric affine-regular hexagon. Conversely this configuration attains \(\rho=1/4\).

To see that every factor occurs, take \(x=y=1\) and \(0<z\le1\). These determine positive admissible \(a,b,c\) and give \(\rho=z/(1+z)^2\), strictly increasing from \(0\) to \(1/4\). Choose a nonconstant but sufficiently small central equidistant and add it to the vertices of \(U\) to obtain a strictly convex \(P\), realizing nontrivial contraction. At equality the weights are \(1/3\), so the formula for \(O\) reduces to the centroid of the six vertices of \(P\). This proves every assertion.

## Verification
The supplied standalone standard-library program `verify.py` checks the full matrix identity by exact rational arithmetic for six rationally parameterized norm hexagons, including the affine-regular extremizer and five asymmetric cases. For each case it explicitly constructs a strictly convex nonequicentral hexagon, computes both successive source involutes by their half-sum definitions, and verifies five full steps against the closed-form rate and center. These finite checks are consistency tests of signs and indexing; the all-parameter proof is the symbolic argument above.

For example, the admissible normalized norm vertices \(U_1=(1,0)\), \(U_2=(0,1)\), \(U_3=(-6/5,9/10)\) produce \(\rho=1001/4320\) and weights \((588,1521,1210)/3319\), exhibiting a genuinely nonuniform barycentric central point.

## Relationship to prior work
Craizer--Martini (first publicly available 2014) define the involutes, establish convergence to a shared central point and ask for a direct construction. They do not calculate the sharp global two-involute rate over all genuine symmetric hexagonal norms. The present result uses their involute and duality identities but determines the entire hexagonal shape spectrum, the exact barycentric center, and the sharp equality and range classification.

Craizer--Teixeira--da Silva (first publicly available 2012) introduce the area evolute and the parallel-diagonal transform of a polygon with paired opposite sides, a precursor to the later involute construction. Their paper treats the single transform, not the reiterated six-sided spectral contraction or its global extremal bound.

Craizer--Teixeira--Balestro (first publicly available 2017) study the general discrete double-evolute operator, its eigenmodes and regular-polygon examples. Their regular hexagon eigenvalues supply related spectral background, and their general operator description may be specialized to this setting, but it does not state the displayed determinant-triangle factor for arbitrary skew hexagons, its universal sharp upper bound, or the normalized involute's barycentric fixed point.

A subsequently published result entitled *A finite linear solve for the central point of a constant-width polygon* gives an exact linear-system solution for the general polygonal central point using a shape operator and translation cocycle. Thus neither finite computability of the center nor existence of a linear involute representation is claimed as new here. The distinct contribution is the **closed-form three-direction barycentric homothety and optimal contraction law**, including the equality classification for all six-sided norms. Its center formula is a specialized explicit expression compatible with the general linear solve.

Arnold--Fuchs--Izmestiev--Tabachnikov--Tsukerman (2015) study different discrete evolute/involute operators with different center constructions and so do not directly give this Minkowski six-sided involute spectrum.

## Limitations
The theorem applies only to strictly convex centrally symmetric six-sided direction polygons and their associated paired-edge hexagons. It does not assert any uniform \(1/4\) bound for polygons with more edge directions, nor extend unchanged to curves with smoothly varying directions. The boundary cases \(x=0\), \(y=0\), or \(z=0\) are excluded because the norm hexagon then ceases to be strictly convex. The result identifies no rate for the separate single-involute sequence unless the two-stage indexing is respected. The exact-rational tests do not certify the general proof independently. General spectral theory may conceal an implicit special-case derivation, and exhaustive equivalence to every unpublished or inaccessible formulation is not claimed.

## References
1. M. Craizer and H. Martini, *Involutes of Polygons of Constant Width in Minkowski Planes*, arXiv:1406.3205, first public version 2014-06-12, especially the finite-sum involute formulas and convergence theorem. Earlier versions use slightly different title and author listings.
2. M. Craizer, R. C. Teixeira and M. A. H. B. da Silva, *Polygons with Parallel Opposite Sides*, arXiv:1210.2442, first public 2012-10-08, especially Section 4 on the parallel-diagonal transform.
3. M. Craizer, R. Teixeira and V. Balestro, *Discrete Cycloids from Convex Symmetric Polygons*, arXiv:1702.00522 (2017); later *Discrete & Computational Geometry* 60 (2018), 859–884, especially the double-evolute spectral viewpoint and regular examples.
4. *A finite linear solve for the central point of a constant-width polygon*, publicly available mathematical result (2026), specifically the source-involute translation-cocycle formula and finite solve; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-finite-linear-solve-for-the-central-point-of-a-constant-width--ab4a4095bddf .
5. M. Arnold, D. Fuchs, I. Izmestiev, S. Tabachnikov and E. Tsukerman, *Iterating evolutes and involutes*, arXiv:1510.07742 (2015), for distinct polygonal evolute constructions.
