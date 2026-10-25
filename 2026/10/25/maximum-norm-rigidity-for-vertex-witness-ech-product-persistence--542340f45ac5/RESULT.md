# Maximum-norm rigidity for vertex-witness Čech product persistence

## Finding
Let \(\Phi\) be any normalized coordinatewise-monotone absolute norm on \(\mathbb R^2\). The following are equivalent:

1. \(\Phi(s,t)=\max\{|s|,|t|\}\) for every pair of real numbers.
2. For every pair of nonempty finite metric spaces, at every radius \(r\ge0\), the canonical coordinate-projection map from the *vertex-witness Čech complex* of the metric product to the product of the two individual Čech realizations is a homotopy equivalence.
3. For every such pair and every field, the entire product Čech persistence barcode is obtained by degree-wise pairwise intersections of the two factor barcodes.

Moreover, if \(c=\Phi(1,1)>1\), the two factors \(X=Y=\{0,1\}\) with unit distance already force failure: their four-point \(\Phi\)-metric product has an intrinsic vertex-witness Čech complex equal to the tetrahedral boundary \(S^2\) for every \(1\le r<c\), with a unique positive-degree bar \([1,c)\) in homological degree two; at \(r\ge c\) it is a full tetrahedron. Both factors become contractible at \(r=1\). Thus four product points exhibit an *exact higher-dimensional persistence obstruction* to universal factorization for every nonmaximum norm, and two points per factor are minimal for such a product obstruction.

## Assumptions and scope
A normalized absolute norm \(\Phi\) obeys \(\Phi(a,b)=\Phi(|a|,|b|)\), is nondecreasing separately in each nonnegative coordinate, and satisfies \(\Phi(1,0)=\Phi(0,1)=1\). For nonempty finite metric spaces \(X,Y\), define \(d_\Phi((x,y),(x',y'))=\Phi(d_X(x,x'),d_Y(y,y'))\). The intrinsic *vertex-witness* Čech complex \(C_r(X)\) has a nonempty finite set \(\sigma\) as a face precisely if there exists a witness \(z\in X\) satisfying \(d_X(z,v)\le r\) for every \(v\in\sigma\). Empty faces are understood. This is the nerve of vertex-centered closed balls intersected with the vertex set; no points in an ambient geodesic space are admitted as witnesses. We use ordinary (unreduced) homology for the barcode claim, with the standard convention that endpoints enter at their inclusive radius. Statement 2 concerns the canonical projection induced by the two coordinate maps; statement 3 concerns their induced natural persistence modules.

## Proof
Write \(c=\Phi(1,1)\). Normalization and coordinatewise monotonicity imply \(1\le c\) and, for \(a,b\ge0\),
\[\max(a,b)\le\Phi(a,b)\le c\max(a,b).\]
If \(c=1\), the inequalities force \(\Phi=\|\cdot\|_\infty\). Conversely, if \(\Phi\ne\|\cdot\|_\infty\), then \(c>1\).

Suppose \(c=1\). For any finite subset \(\sigma\subset X\times Y\), a product witness \((x,y)\) at radius \(r\) exists if and only if the projections of \(\sigma\) separately have witnesses in \(X\) and \(Y\). Therefore the product Čech complex is exactly the categorical simplicial product: its faces are finite subsets of rectangles \(\alpha\times\beta\), with \(\alpha\in C_r(X)\), \(\beta\in C_r(Y)\).

For a point \(z\) of its realization, write \(z_{xy}\ge0\) for its barycentric probabilities, and put \(a_x=\sum_y z_{xy}\), \(b_y=\sum_x z_{xy}\). The marginal map \(p(z)=(a,b)\) lies in \(|C_r(X)|\times|C_r(Y)|\); its section \(s(a,b)_{xy}=a_xb_y\) lies in the product simplicial complex because the entire rectangle of the marginal supports is a face. The formula
\[H_t(z)_{xy}=(1-t)z_{xy}+t a_xb_y\quad(0\le t\le1)\]
defines a strong deformation retraction onto \(s(|C_r(X)|\times|C_r(Y)|)\): every intermediate support stays in the same permitted rectangle, \(p\circ s\) is the identity, and \(H_t\) fixes the section pointwise. The formulas are independent of \(r\) and commute with radius inclusions, so this is a filtered strong deformation retraction. The field Künneth isomorphism gives the product persistence module as a direct sum of pointwise tensor products of the factor modules; interval modules tensor to the module of the intersection of their intervals. This proves 1 implies 2 and 3.

Suppose \(c>1\) and choose \(X=Y\) with exactly two points at distance one. The four product points are the corners of a square; the distances from each corner to its two adjacent corners equal one, while the distance to its opposite corner is \(c\). If \(1\le r<c\), each ball includes exactly three corners, omitting the opposite corner. Each nonempty proper subset of the four corners therefore has a common witness, but all four corners do not. The complex is exactly the boundary of a three-simplex, giving \(\widetilde H_2\cong\mathbb Z\), while for \(r\ge c\) the four-corner set is a simplex. Below radius one all four corners are isolated. The unique degree-two barcode interval is consequently \([1,c)\), with no degree-one bars. However, the Čech complex of either two-point factor is a one-simplex for all \(r\ge1\), so their homological tensor products vanish in degree two throughout that range. Their topological product is contractible at \(r=1\), proving failures of 2 and 3. A factor with only one point yields the other factor exactly, so two points in each factor is a minimal size witness. Thus either universal property forces \(c=1\) and hence \(\Phi\) maximum.

## Verification
The accompanying executable `verify.py` independently enumerates all nonempty faces for four product norm models (maximum, taxicab, Euclidean, and a cut-square absolute norm). It verifies the face vectors \((4,0,0,0)\) below radius one, \((4,6,4,0)\) on the open obstruction stage for nonmaximum norms, and \((4,6,4,1)\) at the diagonal distance. These finite checks corroborate the four-point boundary description. They do not prove universal quantification over norms or finite metric spaces; that follows from the preceding inequalities, rectangular witness criterion, and explicit deformation retraction.

## Relationship to prior work
Matsushita (2025) connects closed neighborhood complexes to intrinsic vertex-witness Čech constructions. Gakhar–Perea (2019) establish general persistent Künneth formulas for categorical products of filtrations, including maximum-metric Vietoris–Rips products. The categorical product of abstract simplicial complexes and its realization are standard. Those results cover the positive product-persistence mechanism but do not state the **converse norm classification** or the exact four-point degree-two obstruction for vertex-witness Čech complexes established here. Ji–Souza–Garg (2025) treat graph box products under vertex/edge coloring filtrations, not the intrinsic vertex-witness Čech norm-rigidity question. No uniqueness claim is made from a failed search alone.

## Limitations
This result concerns finite metric spaces and vertex-centered witnesses, not Čech complexes with arbitrary ambient witnesses and not Vietoris–Rips complexes. It classifies normalized coordinatewise-monotone absolute norms in two arguments; nonmonotone functions and coordinate-dependent nonnorm metrics are not covered. The product homotopy theorem and categorical persistent Künneth formula are established background; the focus is the sharp necessity, minimal obstruction, and its exact degree-two barcode. An equivalent uninspected formulation may exist.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1 (first public 2025-11-16), https://arxiv.org/abs/2511.12608.
2. H. Gakhar and J. A. Perea, *Künneth Formulae in Persistent Homology*, arXiv:1910.05656v1 (2019), https://arxiv.org/abs/1910.05656.
3. C. Rüschoff, *Lecture notes: Simplicial sets*, section 1.3 (2017), https://ncatlab.org/nlab/files/Rueschoff_SimplicialSets.pdf.
4. M. Ji, A. H. Souza, V. Garg, *On topological descriptors for graph products*, NeurIPS 2025, https://proceedings.nips.cc/paper_files/paper/2025/hash/946731e787ad4fa68e1955d23f8bacfa-Abstract-Conference.html.
