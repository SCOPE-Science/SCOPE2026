# Exact Estermann measure of every regular polygon
## Finding
For a planar convex body \(K\), define its Estermann measure by
\[
e(K)=\frac{\operatorname{area}(K)}{\inf\{\operatorname{area}(Q):K\subseteq Q,\ Q\text{ is a centrally symmetric convex body}\}}.
\]
Suppose that \(K\) is invariant under reflection in two distinct nonparallel lines \(L_1,L_2\) meeting at \(o\). Then the infimum in the denominator is attained by a body centered at \(o\), and the inclusion-minimal such body is
\[
Q_o=\operatorname{conv}(K\cup(2o-K)).
\]
Hence
\[
e(K)=\frac{\operatorname{area}(K)}{\operatorname{area}(Q_o)}.
\]

For the regular Euclidean \(n\)-gon \(P_n\), centered at \(o\), this gives the complete formula
\[
e(P_n)=
\begin{cases}
1,& n\text{ even},\\
\cos(\pi/n),& n\text{ odd}.
\end{cases}
\]
If \(n\) is odd, the minimizing centrally symmetric superset is the regular \(2n\)-gon with the same circumradius and vertex set consisting of the vertices of \(P_n\) together with their antipodes. Thus
\[
1-e(P_n)=\frac{\pi^2}{2n^2}+O(n^{-4})
\]
along odd \(n\).

## Assumptions and scope
A convex body means a compact convex subset of \(\mathbb R^2\) with nonempty interior. A centrally symmetric body \(Q\) has a center \(c\) such that \(Q=2c-Q\). Reflection axes are ordinary Euclidean reflection axes. The theorem is planar; no higher-dimensional analogue is asserted here.

Steiner symmetrization with respect to a line \(L\) is denoted by \(S_L\). Only four standard properties are used: it preserves area, maps convex bodies to convex bodies, is monotone under inclusion, and fixes every body already symmetric about \(L\). The proof below also verifies the additional point needed here: if a body is centrally symmetric, then its Steiner symmetral remains centrally symmetric and its center is the orthogonal projection of the old center to \(L\).

The Estermann measure is affine invariant, but the two-axis centering theorem is phrased in Euclidean coordinates because Steiner symmetrization is used in the proof.

## Proof
Translate coordinates so that \(o=0\). First consider one reflection axis \(L\). Rotate coordinates so that \(L\) is the \(x\)-axis. Let \(Q\) be centrally symmetric about \(c=(a,b)\). Write the vertical slice at abscissa \(x\) as an interval of length \(\lambda(x)\). Central symmetry of \(Q\) gives
\[
\lambda(2a-x)=\lambda(x).
\]
After Steiner symmetrization about \(L\), the slice becomes the interval centered at height \(0\) with length \(\lambda(x)\). Therefore the map
\[
(x,y)\longmapsto(2a-x,-y)
\]
preserves \(S_LQ\). Thus \(S_LQ\) is centrally symmetric about \((a,0)\), which is exactly the orthogonal projection of \(c\) onto \(L\).

Now assume \(K\) is symmetric about \(L\) and \(K\subseteq Q\). Every vertical slice of \(K\) is already centered on \(L\). Since the corresponding slice of \(Q\) contains it, the slice length of \(Q\) is at least that of \(K\). Centering the longer interval cannot lose the centered shorter interval. Hence
\[
K\subseteq S_LQ.
\]
So Steiner symmetrization about an axis of \(K\) preserves containment of \(K\), preserves area, and orthogonally projects the symmetry center of \(Q\) onto that axis.

Start from an arbitrary centrally symmetric convex superset \(Q_0\supseteq K\), with center \(c_0\). Alternately symmetrize about \(L_1\) and \(L_2\):
\[
Q_{j+1}=S_{L_1}Q_j,\quad Q_{j+2}=S_{L_2}Q_{j+1},
\]
repeating the pair. Every \(Q_j\) contains \(K\), has the same area as \(Q_0\), and is centrally symmetric. Its center is obtained from \(c_0\) by the corresponding alternating orthogonal projections onto \(L_1,L_2\). Because the two lines are distinct and nonparallel, the two-projection operator has norm strictly smaller than \(1\) on the relevant one-dimensional image. Hence the centers converge to \(0\).

Choose a Euclidean disk \(B\), centered at \(0\), containing \(Q_0\). Monotonicity of Steiner symmetrization and the identity \(S_{L_i}B=B\) imply \(Q_j\subseteq B\) for every \(j\). By Blaschke selection, a subsequence converges in the Hausdorff metric to a convex body \(Q_\infty\). Containment and area pass to the limit, so
\[
K\subseteq Q_\infty,
\qquad
\operatorname{area}(Q_\infty)=\operatorname{area}(Q_0).
\]
If \(x_j\in Q_j\) tends to \(x\in Q_\infty\), central symmetry gives \(2c_j-x_j\in Q_j\); since \(c_j\to0\), the limit contains \(-x\). Therefore \(Q_\infty=-Q_\infty\): it is centrally symmetric about \(0\).

We have proved that every centrally symmetric superset of \(K\) can be replaced, without increasing area, by one centered at \(0\). Among centered centrally symmetric supersets, any such \(Q\) containing \(K\) also contains \(-K\), hence contains
\[
\operatorname{conv}(K\cup(-K)).
\]
This convex hull is itself centered and centrally symmetric, so it is the minimum-area admissible body. Translating back gives
\[
Q_o=\operatorname{conv}(K\cup(2o-K)).
\]

Apply the theorem to a regular \(n\)-gon \(P_n\), which has at least two reflection axes through its center \(o\). If \(n\) is even, then \(-P_n=P_n\), so \(e(P_n)=1\).

Let \(n\) be odd and let the circumradius be \(R\). The vertex angles of \(P_n\) are \(2\pi j/n\). The antipodal vertices have angles \(2\pi j/n+\pi\). Because \(n\) is odd, the two sets interlace and together form all angles \(k\pi/n\), so
\[
\operatorname{conv}(P_n\cup(-P_n))
\]
is the regular \(2n\)-gon with circumradius \(R\). Therefore
\[
\operatorname{area}(P_n)=\frac n2R^2\sin(2\pi/n),
\]
whereas the enclosing regular \(2n\)-gon has area
\[
nR^2\sin(\pi/n).
\]
Their ratio is
\[
\frac{\sin(2\pi/n)}{2\sin(\pi/n)}=\cos(\pi/n),
\]
which proves the formula. The asymptotic expansion follows from the Taylor series of \(\cos(\pi/n)\).

## Verification
The supplied `verify.py` independently reconstructs regular polygons by coordinates, forms the convex hull of the polygon together with its antipodal image, and compares the numerical area ratio with the theorem for every \(3\le n\le101\). It also verifies that the hull has \(n\) vertices for even \(n\) and \(2n\) vertices for odd \(n\). The script returns `VERIFY_OK`.

These finite checks test the parity, hull, and area bookkeeping only. The universal theorem is proved by the Steiner-symmetrization and compactness argument above, not by finite enumeration.

## Relationship to prior work
The Estermann measure is the classical outer, area-based measure of central symmetry: for a fixed candidate center \(c\), the smallest centrally symmetric convex superset is \(\operatorname{conv}(K\cup(2c-K))\). Classical work of Estermann and Grünbaum establishes the general framework and extremal lower bounds. A modern comprehensive treatment of measures of symmetry is G. Toth's 2015 monograph.

The closest neighboring exact regular-polygon formulas located concern different symmetry functionals, such as inner centrally symmetric subsets, Minkowski-type asymmetry, harmonic symmetrization, or Fraenkel asymmetry. Those functionals neither minimize the area of a centrally symmetric superset nor imply the centered-superset theorem proved here.

Targeted searches for the Estermann measure of regular polygons, for a two-reflection-axis centering principle, for Steiner-symmetrization proofs of the outer problem, and for the equivalent statement that the minimal centrally symmetric superset of a regular odd polygon is the antipodal regular \(2n\)-gon did not locate this theorem or formula in the inspected literature.

## Limitations
The structural centering theorem is proved only in the plane. The argument uses area-preserving Steiner symmetrization and alternating orthogonal projections of centers; no claim is made that the same proof yields a higher-dimensional statement for arbitrary arrangements of reflection hyperplanes.

The historical originality risk is nonzero. Estermann's 1928 paper and Grünbaum's 1963 survey are old and incompletely searchable in modern indexes, and the final regular-polygon computation is short once the centering lemma is known. The primary historical sources were therefore treated as a specific residual risk rather than assumed not to contain an equivalent observation.

## References
1. G. Toth, *Measures of Symmetry for Convex Sets and Stability*, Universitext, Springer, 2015, DOI: 10.1007/978-3-319-23733-6. The MaRDI bibliographic record reports first publication on 2015-10-08 and classifies the work under primary MSC 52A20.
2. T. Estermann, *Über den Grad der Asymmetrie einer konvexen Punktmenge*, Jahresbericht der Deutschen Mathematiker-Vereinigung 37 (1928), 122--124. Historical source for the outer area measure; no exact public day was assigned here.
3. B. Grünbaum, *Measures of symmetry for convex sets*, Proceedings of Symposia in Pure Mathematics 7 (1963), 233--270. Classical survey of symmetry measures.
