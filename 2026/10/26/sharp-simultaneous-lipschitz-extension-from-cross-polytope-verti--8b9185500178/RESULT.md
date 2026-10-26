# Sharp simultaneous Lipschitz extension from cross-polytope vertices to all edge midpoints

## Finding
For every integer \(d\ge3\), let \(V_d=\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d\), and let \(M_d\) consist of all midpoints \((s e_i+t e_j)/2\), where \(i<j\) and \(s,t\in\{-1,1\}\). All metric distances below are ambient Euclidean distances. Let \(\Lambda_d\) be the least norm of a real-linear right inverse to restriction \(\operatorname{Lip}(V_d\cup M_d)/\mathbb R\to\operatorname{Lip}(V_d)/\mathbb R\). Then
\[
\Lambda_3=\frac{2\sqrt2-1}{\sqrt{3/2}+\sqrt2-1},\qquad
\Lambda_d=\frac{2(\sqrt2(d-1)+1)}{d(1+\sqrt2)+\sqrt2-2}\quad(d\ge4).
\]
The infima are attained by explicit positive, hyperoctahedral-equivariant linear extension operators. The constants increase strictly with dimension and tend to \(4-2\sqrt2\). The structural change between dimensions three and four is caused by the first occurrence of two edges with disjoint coordinate supports.

## Assumptions and scope
Functions are real-valued; no continuity beyond the Lipschitz condition is assumed. Linear extension means linearity on the quotient modulo constants and exact preservation of the given vertex values, modulo constants. The norm is the ratio of Lipschitz seminorms. An extension can be represented by probability weights at each new point because the optimizers below are positive; arbitrary competitors are allowed signed coefficients.

Put \(x=(s e_i+t e_j)/2\). The optimal extension is \((Ef)(x)=a_d(f(se_i)+f(te_j))+b_d(f(-se_i)+f(-te_j))+c_d\sum_{k\notin\{i,j\}}(f(e_k)+f(-e_k))\), with \((Ef)(v)=f(v)\) for \(v\in V_d\). In dimension three, put \(h=\sqrt{3/2}\) and
\[
c_3=\frac{\sqrt2-h}{2(h+\sqrt2-1)},\quad b_3=0,\quad a_3=\tfrac12-c_3.
\]
For \(d\ge4\), put
\[
b_d=c_d=\frac{\sqrt2-1}{2d(1+\sqrt2)+2(\sqrt2-2)},\quad a_d=\frac{1-(2d-2)c_d}{2}.
\]
These coefficients are nonnegative and satisfy \(2a_d+2b_d+2(d-2)c_d=1\).

## Proof
**1. Symmetry and the dual norm.** Average any linear extension over the signed-permutation group of the coordinates. This averaging fixes the original vertices, preserves constants, and cannot increase the operator norm. The stabilizer of one edge midpoint has exactly three orbits on original vertices: its two endpoints, their two antipodes, and the other \(2(d-2)\) vertices. Thus every equivariant extension has coefficients \((a,b,c)\in\mathbb R^3\) with \(2a+2b+2(d-2)c=1\). For a zero-mass signed measure \(\sigma\) on \(V_d\), write \(\|\sigma\|_{\mathrm{KR}}=\sup_{\operatorname{Lip}(f)\le1}|\sum_v\sigma(v)f(v)|\). The extension norm equals the maximum of \(\|\mu_x-\mu_y\|_{\mathrm{KR}}/\|x-y\|_2\) over all distinct original/new points, where \(\mu_x=\delta_x\) at original vertices and \(\mu_x\) is the signed coefficient row at new points. On \(V_d\), distances between nonantipodal distinct vertices equal \(\sqrt2\), and antipodal distances equal \(2\). For probability rows the KR norm is the minimum transport cost.

**2. Lower bound when \(d\ge4\).** For an incident vertex \(u\) and midpoint \(x\), the test function \(v\mapsto\|u-v\|_2\) yields the affine lower bound
\[
I=1+2\sqrt2\,b+2(d-2)c.
\]
For two midpoints supported on disjoint coordinate pairs, the coefficient-row difference has KR norm exactly \(2\sqrt2(|a-c|+|b-c|)\), since the positive and negative masses can be matched across disjoint coordinates at cost \(\sqrt2\) per unit, and no smaller nonzero source distance exists. Their Euclidean separation is \(1\). Using \(a=\tfrac12-b-(d-2)c\), this gives the two affine lower bounds
\[
D_1=\sqrt2[1-4b-2(d-2)c],\qquad D_2=\sqrt2(1-2dc).
\]
Hence every extension has norm at least \(\max\{I,D_1,D_2\}\). To show this maximum is at least the displayed \(\Lambda_d\), take a convex combination with weights
\[
\lambda_I=\frac{2}{3+(d-2)(\sqrt2-1)/d},\qquad
\lambda_1=\frac{\lambda_I}{2},\qquad
\lambda_2=\frac{(d-2)(\sqrt2-1)}{2d}\lambda_I.
\]
All weights are positive, sum to one, and cancel both coefficients of \(b\) and \(c\). The resulting constant equals the displayed \(\Lambda_d\) (equivalently, solve \(I=D_1=D_2\) at \(b=c=c_d\)). No sign or positivity restrictions are used in this lower bound.

**3. Attainment when \(d\ge4\).** Write \(q=a_d-c_d>0\), \(c=c_d\), and \(S=2+2(d-1)\sqrt2\). A midpoint row is the uniform background mass \(c\) at every original vertex plus extra mass \(q\) at the two endpoints; \(2q+2dc=1\). Algebra gives
\[
2\sqrt2\,q=\Lambda_d,\qquad cS=\frac{\sqrt2-1}{2}\Lambda_d.
\]
For a pair consisting of a vertex and a midpoint, the three symmetry types (incident, antipodal to an endpoint, or outside both coordinate axes) have norm ratios, respectively,
\[
\Lambda_d,\qquad \frac{2}{\sqrt5}\Lambda_d,\qquad
\frac{1+\sqrt2}{\sqrt6}\Lambda_d.
\]
The latter two factors are strictly less than one. For pairs of different midpoints, there are five types: one sign reversal on the same coordinate pair; two reversals on that pair; one shared coordinate with the same sign; one shared coordinate with opposite sign; disjoint coordinate pairs. Their exact KR/distance ratios are
\[
2q,\quad2q,\quad2q,\quad\frac4{\sqrt3}q,\quad2\sqrt2\,q.
\]
These follow from transporting the two positive extra atoms to the two negative extra atoms along original-vertex distances \(\sqrt2\) or \(2\); in the shared-signed-coordinate cases the common atoms cancel. Every ratio is at most \(\Lambda_d\), and the incident and disjoint cases attain it. Original-vertex pairs have ratio one. Thus the lower bound is attained.

**4. Dimension three.** There are no disjoint coordinate-pair edges. Set \(h=\sqrt{3/2}\). For a midpoint and an incident vertex, the 1-Lipschitz test function taking value zero on that vertex and its antipode and \(\sqrt2\) at all other original vertices yields the lower bound \(1+2c\). For a midpoint and an original vertex on the third coordinate axis, the distance-to-that-vertex test gives \([\sqrt2-2(\sqrt2-1)c]/h\). Thus every extension, even with signed coefficients, has norm at least
\[
\max\left\{1+2c,\frac{\sqrt2-2(\sqrt2-1)c}{h}\right\}
\ge\frac{2\sqrt2-1}{h+\sqrt2-1}.
\]
The two affine functions meet at \(c=c_3\). For the prescribed positive row \((a_3,0,c_3)\), the incident-vertex and outside-vertex ratios both equal this lower bound. An antipodal-to-endpoint vertex has ratio \([(2+\sqrt2)a_3+2\sqrt2c_3]/\sqrt{5/2}\). The four nontrivial midpoint-pair types have ratios at most \(2a_3\) or \(4a_3/\sqrt3\). Direct substitution shows all three displayed competing quantities are strictly smaller than \(\Lambda_3\); for example \(0.442<a_3<0.443\), \(0.057<c_3<0.058\), and \(1.115<\Lambda_3<1.116\) are certified by squaring rational bounds on the radicals. This proves attainment.

**5. Strict increase and comparison with barycentric interpolation.** The expression for \(d\ge4\) is strictly increasing because its real-parameter derivative has numerator proportional to \(3-2\sqrt2>0\); direct substitution shows \(\Lambda_3<\Lambda_4\). Its limit is \(2\sqrt2/(1+\sqrt2)=4-2\sqrt2\). Ordinary arithmetic midpoint interpolation has norm \(2/\sqrt3\) at \(d=3\), and \(\sqrt2\) for all \(d\ge4\), strictly larger than these optima.

## Verification
A standalone checker, `verify_crosspolytope.py`, constructs the original/new Euclidean point sets and the specified coefficient rows. It independently solves a finite linear program in the values of each original-vertex Lipschitz function, for **every** pair of points for dimensions three through six, rather than relying on the symmetry-type norm formulas. The observed test counts are 153, 496, 1225 and 2556 pairs respectively; all matched the exact predicted optimum to tolerance \(2\times10^{-8}\). The checker requires Python 3, NumPy and SciPy and executes with `python verify_crosspolytope.py`. These finite checks corroborate but do not substitute for the all-dimension proof.

## Relationship to prior work
Ambrosio and Puglisi (arXiv:1609.01450, 2016) establish a connection between linear Lipschitz extension operators and random projections in the Kantorovich–Rubinstein/Lipschitz-free setting. Bruè, Di Marino and Stra (arXiv:1801.07533, first posted 2018-01-23) construct linear extension operators for doubling subsets via regular random projections. Both supply a general framework, but the relevant examined full-text statements concern existence and broad bounds, not the precise cross-polytope vertex-to-all-edge-midpoints constant. Related published research on simplex midpoints and on a single added center concerns different source metrics and destination configurations. The novelty claim here is exclusively the sharp dimension-dependent constants and their explicit globally optimal simultaneous extension kernels, not the general transport duality or symmetry-averaging methodology.

## Limitations
This result concerns real-linear scalar Lipschitz extensions from precisely the Euclidean cross-polytope vertices to the union with all edge midpoints. It does not resolve extensions to all boundary points, arbitrary polytope vertices, general Banach-valued targets, or uniqueness of optimizers. Bibliographic noncoverage cannot rule out independently discovered equivalent results. No independent mathematical audit has been performed.

## References
1. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (first version, 2016-09-06), https://arxiv.org/pdf/1609.01450.
2. E. Bruè, S. Di Marino and F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533 (first version, 2018-01-23), https://cvgmt.sns.it/media/doc/paper/3749/extproj.pdf.
