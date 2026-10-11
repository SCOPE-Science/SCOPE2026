# Exact Minkowski asymmetry and unique critical point of parallel-opposite hexagons

## Finding

Let \(P\subset\mathbb R^2\) be a strictly convex hexagon (six nonzero edges and no collinear consecutive edges) with corresponding opposite sides parallel. Its Minkowski asymmetry is
\[
s(P)=\inf_{o\in\mathbb R^2}\inf\{\lambda\ge1: -(P-o)\subseteq\lambda(P-o)\}.
\]
There is a natural affine-normalized four-parameter presentation: up to an invertible affine transformation and cyclic labeling, the six successive edge vectors are
\[
(a,0),\quad(0,b),\quad(-c,c),\quad(-(a+t),0),\quad(0,-(b-t)),\quad(c+t,-(c+t)),
\]
where \(a,b,c>0\) and \(a+t,b-t,c+t>0\). Put \(S=a+b+c\) and \(T=S+t\). Then
\[
\boxed{s(P)=\max\left\{\frac{T}{S},\frac{S}{T}\right\}.}
\]
In these coordinates the **Minkowski critical point is unique**. Writing \(\lambda=s(P)\), its coordinates \(o=(o_x,o_y)\) satisfy
\[
(1+\lambda)o=\begin{cases}
\bigl(\lambda a-(c+t),\ \lambda(b+c)\bigr),&t\ge0,\\
\bigl(a-\lambda(c+t),\ b+c\bigr),&t\le0.
\end{cases}
\]
The two formulas coincide when \(t=0\). Moreover, \(s(P)=1\) exactly for centrally symmetric hexagons, and the exact range over strictly convex parallel-opposite hexagons is \([1,2)\).

## Assumptions and scope

Opposite sides means edges three positions apart in the cyclic six-edge sequence. Strict convexity excludes zero edges and supplementary adjacent directions. The expression is not a Euclidean perimeter ratio: the positive coefficients are measured in an **affinely normalized** triple of directions. Let the first three ray generators \(d_1,d_2,d_3\) be chosen uniquely up to common positive scale so that \(d_2=d_1+d_3\). Such a choice exists because the second ray lies in the positive cone spanned by the first and third. Sending \(d_1\) to \((1,0)\) and \(d_2\) to \((0,1)\) sends \(d_3\) to \((-1,1)\). Closure forces the opposite edge coefficients to be \(a+t,b-t,c+t\). This proves the normal form for every hexagon in the stated class.

The displayed ratio is invariant under changing the common scale of \(d_1,d_2,d_3\), translating, and applying nonsingular affine maps; hence it computes the intrinsic asymmetry despite the coordinate choice. No restriction to equiangular, equal-length or centrally symmetric examples is made.

## Proof

Translate so that the successive vertices of \(P\) are
\[
(0,0),\ (a,0),\ (a,b),\ (a-c,b+c),\ (-c-t,b+c),\ (-c-t,c+t).
\]
Since the six edge directions occur in cyclic order, the positivity conditions give a strictly convex hexagon. Its outward facet normals can be represented, including positive scalings, by \((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\). Their support values, in that order, are
\[
a,\quad c+t,\quad b+c,\quad0,\quad a+b,\quad0.
\]

For a fixed \(\lambda\ge1\), put \(z=(1+\lambda)o\). The inclusion \(-(P-o)\subseteq\lambda(P-o)\) is equivalent, via support functions, to the six linear inequalities
\[
\begin{aligned}
a-\lambda(c+t)&\le z_x\le\lambda a-(c+t),\\
b+c&\le z_y\le\lambda(b+c),\\
a+b&\le z_x+z_y\le\lambda(a+b).
\end{aligned}
\]
The sum of the lower coordinate endpoints must not exceed the upper diagonal endpoint, which simplifies to \(\lambda(S+t)\ge S\). Likewise, the sum of the upper coordinate endpoints must not lie below the lower diagonal endpoint, giving \(\lambda S\ge S+t\). These conditions are **also sufficient**: for \(\lambda\ge1\) the individual coordinate intervals and the diagonal interval are nonempty, and the sum of the two coordinate intervals intersects the diagonal interval exactly when the two displayed inequalities hold. Thus the least admissible \(\lambda\) is their maximum ratio.

For \(t\ge0\), at the optimum \(\lambda S=S+t\), the sum of the two upper coordinate endpoints equals the lower diagonal endpoint \(a+b\). Consequently both coordinates are forced to their upper endpoints, giving the first formula for \(o\). For \(t\le0\), the equality \(\lambda(S+t)=S\) forces both coordinates to their lower endpoints, giving the second formula. This proves **existence and uniqueness of the critical point for every admissible parameter choice**, including \(t=0\).

Since \(S,T>0\), equality \(s(P)=1\) is equivalent to \(t=0\). Precisely then opposite edge vectors agree after reversing orientation, which is equivalent to central symmetry. The general planar bound \(s(P)\le2\) is strict here by the formula: if \(t\ge0\), then \(T=S+t<S+b<2S\), using \(t<b\); if \(t<0\), then \(T=S+t>S-\min\{a,c\}>0\), but more precisely \(S+2t=(a+t)+(c+t)+b>0\), whence \(T>S/2\). Conversely, to realize any prescribed \(r\in(1,2)\), choose sufficiently small \(\varepsilon>0\), set \(a=c=\varepsilon\), \(b=1\), and \(t=(r-1)(1+2\varepsilon)\). These parameters satisfy the positivity conditions for sufficiently small \(\varepsilon\) and give \(s(P)=r\). Take \(t=0\) for \(r=1\). Therefore the exact range is \([1,2)\).

## Verification

The standalone file `verify.py` runs with Python 3.9 or newer and only the standard library (`python verify.py`). It constructs six vertices independently from edge displacements, verifies facet supports and strict convexity, and checks the claimed optimal inclusion in 3,424 rational configurations. In 375 rational configurations it independently minimizes the defining three-variable linear program by enumerating all possible active triples of facet inequalities, recovering the formula without substituting it into the optimization. Rational realizations of an array of target asymmetry ratios are checked as well. The run returned `VERIFY_OK 3424 exact cases; 375 independent rational LP solves and range witnesses`.

These finite checks corroborate, but do not replace, the preceding proof for all positive real parameters.

## Relationship to prior work

Craizer, Teixeira and da Silva introduced polygons with parallel opposite sides and their affine equidistants and central symmetry sets. Konicer, Murawski, Rogala, Wieczorek and Zwierzyński (first preprint publicly dated 21 June 2026) establish reconstruction, isoperimetric inequalities and caustic-area bounds for this geometric class. Their full available manuscript, especially Sections 2–4 and Theorems 4.4 and 4.7, does not present this containment-based exact Minkowski asymmetry formula or uniqueness of its optimizing center; those area-based bounds do not imply the two scalar inequalities above. Grünbaum's 1964 paper treats a different affine asymmetry functional based on a three-line area partition. The separate 2026 affine-reflection-transform preprint studies an area-energy asymmetry functional, not evidently the minimal homothetic containment factor here. Classical general algorithms for linear optimization of a polygon's asymmetry are compatible with the present proof, but the universal one-ratio simplification and center rigidity for the full parallel-opposite hexagon class are the claimed specific contribution.

## Limitations

The result is restricted to strictly convex six-edge polygons with parallel opposite sides, not all even polygons or higher dimensions. The affine-normalized coefficients are not actual side lengths. The proof does not assert novelty against inaccessible or unindexed literature. A related affine-reflection-transform preprint could be assessed only from its abstract and may contain additional relevant comparisons; its explicitly described invariant is distinct. The listed exact-rational tests do not establish universal correctness without the analytic proof.

## References

1. M. Craizer, R. C. Teixeira and M. A. H. B. da Silva, *Polygons with Parallel Opposite Sides*, Discrete & Computational Geometry **50** (2013), 474–490, arXiv:1210.2442.
2. I. Konicer, B. Murawski, B. Rogala, T. Wieczorek and M. Zwierzyński, *Convex Polygons with Parallel Opposite Sides: Convergence, Reconstruction, and Isoperimetric Inequalities*, arXiv:2606.22612v1 (public preprint 21 June 2026).
3. B. Grünbaum, *A Measure of Asymmetry for Plane Convex Sets*, Journal of the London Mathematical Society **39** (1964), 95–102, DOI:10.1112/jlms/s1-39.1.95 (a different area-partition functional).
4. P. Giblin, S. Janeczko and M. Zwierzyński, *Invariants of an Affine Reflection Transform*, arXiv:2609.27931 (related but differently defined area-energy asymmetry).
