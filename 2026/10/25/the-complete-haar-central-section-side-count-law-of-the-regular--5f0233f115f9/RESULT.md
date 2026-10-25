# The complete Haar central-section side-count law of the regular truncated cube

## Finding
Let \(K\) be the regular truncated cube described below, and let \(N\) be the number of sides of \(K\cap U^\perp\) for uniform \(U\in S^2\). Its exact distribution has four positive masses, supported on \(\{4,6,8,10\}\). Put \(a=\sqrt2-1\). For a plane point \(P=(p_x,p_y)\), set \(w_P=(1,p_x,p_y)\). Define the elementary spherical triangle area
\[
\Omega(P,Q,R)=2\arctan\!\frac{|\det(w_P,w_Q,w_R)|}{\|w_P\|\|w_Q\|\|w_R\|+(w_P\cdot w_Q)\|w_R\|+(w_Q\cdot w_R)\|w_P\|+(w_R\cdot w_P)\|w_Q\|}.
\]
Here every triangle used has positive denominator, and \(\Omega\) is nonnegative. Define the following eight planar points:
\[
O=(0,0),\quad J=(a,0),\quad B=(a/2,a/2),\quad H=(1,0),
\]
\[
T=(2a,a),\quad E=(1/\sqrt2,1/\sqrt2),\quad F=(1,1-a),\quad G=(1,1).
\]
Then the **complete exact law** is
\[
\begin{aligned}
\Pr(N=4)&=\frac{12}{\pi}\Omega(O,J,B),\\
\Pr(N=6)&=\frac{12}{\pi}[\Omega(J,B,E)+\Omega(J,E,T)+\Omega(E,G,F)],\\
\Pr(N=8)&=\frac{12}{\pi}[\Omega(H,J,T)+\Omega(T,E,F)],\\
\Pr(N=10)&=\frac{12}{\pi}\Omega(H,T,F).
\end{aligned}
\]
The numerical values, respectively, are \(0.1510526932733458\ldots\), \(0.5002272882524017\ldots\), \(0.2813973562961121\ldots\), \(0.0673226621781402\ldots\). These are exact evaluations, not simulation-derived estimates. In particular, decagonal sections occur with positive probability.

## Assumptions and scope
The solid is the three-dimensional Archimedean truncated cube
\[
K=[-1,1]^3\cap\{x:|x_1|+|x_2|+|x_3|\le 2+a\},\qquad a=\sqrt2-1.
\]
Its vertices are all \(24\) signed permutations of \((1,1,a)\); it has six octagonal facets, eight triangular facets, and thirty-six edges. The plane passes through the center, and its unoriented normal is Haar-uniform. Degenerate directions are a finite union of great circles and have probability zero. Polygon sides and vertices agree in count. Distances are in the displayed coordinate normalization.

## Proof
**Facet incidence.** For every nondegenerate central section, its vertices are transverse intersections with the original edges of \(K\), and its sides are transverse intersections with original facets. Both counts agree. Write the absolute values of a generic normal in decreasing order \(p>q>r>0\), normalize to \(p=1\), and put \(x=q/p\), \(y=r/p\). The fundamental spherical chamber maps gnomonically onto \(\mathcal D=\{0<y<x<1\}\). There are forty-eight such congruent signed/permuted chambers on \(S^2\).

Each of the four octagonal facets with coordinate \(x_i=\pm1\) corresponding to the two smaller absolute normal components is cut by the plane. The remaining antipodal pair is cut precisely if \(p<q+ar\). Indeed, within a coordinate octagon, the maximum of a linear functional with coefficients \(q,r\) is \(q+ar\) (after arranging \(q\ge r\)). The octagonal facets therefore contribute \(4+2\mathbf1_{1<x+ay}\).

For a triangular facet with corner-sign pattern \(s=(s_1,s_2,s_3)\), its three vertices have signed dot products \(\sum_i s_i u_i-(1-a)s_j u_j\) for \(j=1,2,3\). An antipodal pair contributes two cut facets if these three values straddle zero. For the ordered positive components, the corner with all signs equal never contributes, the pair with its negative sign on the smallest component never contributes, the pair with negative sign on the largest component contributes exactly when \(a<x+y\) and \(y<1-ax\), and the pair with negative sign on the middle component contributes exactly when \(y<x-a\). Thus, off boundary lines,
\[
N(x,y)=4+2\mathbf1_{1<x+ay}+2\mathbf1_{\{a<x+y,\ y<1-ax\}}+2\mathbf1_{y<x-a}.
\]
All of these inequalities follow directly by taking the minimum and maximum of the displayed three facet-vertex dot products; no sampling hypothesis enters.

**Complete chamber partition.** The four threshold lines \(x+ay=1\), \(x+y=a\), \(y=1-ax\), \(y=x-a\), together with the boundary of \(\mathcal D\), partition its closure into exactly six nonoverlapping polygons. Their vertices, in cyclic order, and their values of \(N\) are:

| Side count | Euclidean chamber polygon |
|---|---|
| \(4\) | \(O,J,B\) |
| \(6\) | \(J,B,E,T\) |
| \(6\) | \(E,G,F\) |
| \(8\) | \(H,J,T\) |
| \(8\) | \(T,E,F\) |
| \(10\) | \(H,T,F\) |

Substitution of the eight coordinates into the four line equations checks every listed edge. Their interiors are disjoint and they triangulate \(\overline{\mathcal D}\), using \(a^2+2a=1\) and \(E_x=E_y=1/(1+a)\). Testing the count formula in any one interior point of each convex tile gives the indicated integer throughout that tile. These six cases exhaust the triangle, establishing the support and classification.

**Haar areas.** Gnomonic coordinates of \(U=(1,x,y)/\sqrt{1+x^2+y^2}\) have Jacobian \((1+x^2+y^2)^{-3/2}\,dx\,dy\). The \(48\) congruent chambers produce factor \(48/(4\pi)=12/\pi\). The standard spherical triangle identity shown in the Finding paragraph evaluates the integral over each tile, splitting quadrilateral \(J,B,E,T\) across \(J,E\). This proves the four exact probability formulas. Their sum equals one because the six tiles partition \(\mathcal D\).

**Independent mean identity.** Every original edge has length \(2a\), and all vertices lie on the sphere of radius \(\sqrt{2+a^2}\). An edge subtends central angle \(\delta=2\arcsin(a/\sqrt{2+a^2})\). A uniform central plane cuts an edge with probability \(\delta/\pi\). Summing over thirty-six edges gives
\[
\mathbb E N=\frac{72}{\pi}\arcsin\!\frac{a}{\sqrt{2+a^2}}=6.529979974758095\ldots,
\]
which also equals the expectation from the full exact law.

## Verification
Run `python verify.py` with Python 3, NumPy, and SciPy. It independently reconstructs twenty-four vertices, thirty-six edges and fourteen facets; compares facet and edge intersection counts with the closed directional classification; evaluates each spherical triangle both by the explicit solid-angle identity and numerical gnomonic quadrature; verifies the exact edge-crossing mean; and samples 450,000 independent Gaussian normals. The program is corroborative; the full classification and exact formulas are proved above. A fixed random seed is used for reproducibility.

## Relationship to prior work
Lonke (1998) gives a general expectation formula for Haar sections of a cube, not a four-atom law for this truncated cube. Related section results for other three-dimensional solids likewise do not imply the decagon and octagon probabilities here. For the larger cube–octahedron intersection family \(K_c\), the quadrilateral probability has already been computed for \(2<c<3\), and its specialization to \(c=2+a\) is precisely the quadrilateral entry above. Accordingly, that entry is a consistency check, **not an independent novelty claim**. The new content is the complete six-tile incidence classification and the separate positive octagon and decagon masses, which do not follow from that quadrilateral formula and the mean alone.

## Limitations
The result assumes a fixed regular truncated cube, central planes, and rotationally invariant sampling. It does not describe offset planes, nonregular truncation depths, perimeter or area distributions. Published mathematical priority outside the inspected literature is not proven; independently checking all historical sources would require a separate bibliographic review. Decimal evaluations do not replace the exact elementary expressions.

## References
1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123v1, first posted 21 December 1998, https://arxiv.org/abs/math/9812123.
2. *Truncated cube*, geometric description and Cartesian coordinates, https://en.wikipedia.org/wiki/Truncated_cube (accessed October 2026).
