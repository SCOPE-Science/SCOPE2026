# Half-radius holes around every finite-cardinality stratum in Gromov–Hausdorff space

## Finding
Let \(\mathcal M\) be the metric space of isometry classes of nonempty compact metric spaces, with Gromov–Hausdorff distance \(d_{GH}\). For an integer \(n\ge1\), let \(\mathcal M_{\le n}\) consist of classes with at most \(n\) points. If \(X\in\mathcal M_{\le n}\), put \(\operatorname{sep}(X)=\min_{x\ne y}d_X(x,y)\) when \(X\) has at least two points and \(\operatorname{sep}(X)=\infty\) when \(X\) is a singleton. For every \(0<R<\operatorname{sep}(X)\), there is a finite metric space \(Y\) such that
\[
 d_{GH}(X,Y)=\operatorname{dist}_{GH}(Y,\mathcal M_{\le n})=R/2,
\]
and
\[
 B_{GH}(Y,R/2)\subset B_{GH}(X,R)\setminus\mathcal M_{\le n}.
\]
Thus every finite-cardinality stratum has explicit half-radius holes at every sufficiently small scale. In particular, each \(\mathcal M_{\le n}\) is closed and pointwise \(1/2\)-porous, and the set of all finite metric spaces is dense and meagre in \(\mathcal M\).

## Assumptions and scope
All metric spaces in \(\mathcal M\) are nonempty and compact, and spaces are identified up to isometry. A correspondence \(Q\subset X\times Z\) is a relation whose two coordinate projections are surjective; its distortion is
\[
 \operatorname{dis}(Q)=\sup\{|d_X(x,x')-d_Z(z,z')|:(x,z),(x',z')\in Q\},
\]
so \(d_{GH}(X,Z)=\tfrac12\inf_Q\operatorname{dis}(Q)\). Balls are open. The separation radius is positive for every finite space with at least two points, so the stated range of \(R\) always contains all sufficiently small positive radii. The result concerns the metric Gromov–Hausdorff structure, not merely the topology of \(\mathcal M\).

## Proof
First, \(\mathcal M_{\le n}\) is closed. If \(X_j\in\mathcal M_{\le n}\) converges to \(X\) and \(X\) had \(n+1\) distinct points, their minimum pairwise distance would be some \(\delta>0\). For large \(j\), choose a correspondence from \(X\) to \(X_j\) with distortion less than \(\delta\). The \(n+1\) chosen points must have distinct partners, since two points with the same partner would force distortion at least \(\delta\). This contradicts \(|X_j|\le n\).

Now fix \(X\in\mathcal M_{\le n}\), write \(m=|X|\), choose \(x_0\in X\), and take \(0<R<\operatorname{sep}(X)\). Add \(q=n+1-m\) new points \(p_1,\ldots,p_q\). Define a distance on \(Y=X\sqcup\{p_1,\ldots,p_q\}\) by retaining \(d_X\) on \(X\), setting \(d_Y(p_i,p_j)=R\) for \(i\ne j\), and setting
\[
 d_Y(p_i,x)=R+d_X(x_0,x)\qquad(x\in X).
\]
These formulas define a metric. For example, \(d_Y(p_i,x)\le d_Y(p_i,z)+d_X(z,x)\) follows from the triangle inequality in \(X\), while \(d_X(x,z)\le d_Y(x,p_i)+d_Y(p_i,z)\); the remaining triangles involving two new points follow from their mutual distance \(R\) and the fact that every new-to-old distance is at least \(R\). Since \(X\) is finite and \(R<\operatorname{sep}(X)\), the minimum separation of \(Y\) is exactly \(R\), and \(|Y|=n+1\).

Consider the correspondence
\[
 Q=\{(x,x):x\in X\}\cup\{(x_0,p_i):1\le i\le q\}.
\]
Every pairwise distance changes by at most \(R\), and the pair \((x_0,x_0),(x_0,p_i)\) realizes distortion \(R\). Hence \(\operatorname{dis}(Q)=R\) and \(d_{GH}(X,Y)\le R/2\).

For any compact metric space \(Z\) with at most \(n\) points, every correspondence between \(Y\) and \(Z\) must relate two distinct points of \(Y\) to one common point of \(Z\), by the pigeonhole principle. Those two points of \(Y\) are at distance at least \(R\), so every such correspondence has distortion at least \(R\). Therefore \(d_{GH}(Y,Z)\ge R/2\). Taking the infimum over \(Z\in\mathcal M_{\le n}\), and using \(X\in\mathcal M_{\le n}\), gives
\[
 d_{GH}(X,Y)=\operatorname{dist}_{GH}(Y,\mathcal M_{\le n})=R/2.
\]
The open ball \(B_{GH}(Y,R/2)\) is disjoint from \(\mathcal M_{\le n}\). If \(W\) lies in that ball, then
\[
 d_{GH}(X,W)\le d_{GH}(X,Y)+d_{GH}(Y,W)<R/2+R/2=R,
\]
so the ball is contained in \(B_{GH}(X,R)\setminus\mathcal M_{\le n}\). This proves the half-radius hole statement.

The holes imply that each closed set \(\mathcal M_{\le n}\) has empty interior. Finite metric spaces are dense in \(\mathcal M\), because a finite \(\varepsilon\)-net in any compact metric space, with its induced metric, lies within Hausdorff and hence Gromov–Hausdorff distance at most \(\varepsilon\). Finally, the set of all finite metric spaces is \(\bigcup_{n\ge1}\mathcal M_{\le n}\), a countable union of closed nowhere-dense sets, so it is meagre.

## Verification
The correspondence distortion and the cardinality lower bound are exact; no finite computation is needed. The strict hypothesis \(R<\operatorname{sep}(X)\) ensures that adding the new cluster does not reduce the minimum separation below \(R\). The theorem makes no assertion for radii at or above the separation radius of a nonsingleton center.

## Relationship to prior work
Recent work studies the global topology of the Gromov–Hausdorff space, including a Hilbert-space homeomorphism, while earlier work describes local neighborhoods around finite metric spaces in general position. The present claim is a metric-scale statement: it gives an explicit ball of radius \(R/2\) avoiding the entire at-most-\(n\)-point stratum, for every finite center and all radii below its separation. This estimate is not a consequence of a homeomorphism alone, since metric porosity is not a topological invariant.

## Limitations
The construction uses finiteness of the center and the strict separation-radius bound. It does not classify the full local geometry of the Gromov–Hausdorff space, nor does it claim porosity estimates for arbitrary subsets or for radii exceeding \(\operatorname{sep}(X)\).

## References
1. Y. Ishiki, “The topology of Gromov–Hausdorff space,” arXiv:2609.09639v1 (first public date 2026-09-09; abstract inspected, full text unavailable in the retrieval interface).
2. A. O. Ivanov and A. A. Tuzhilin, “Local Structure of Gromov–Hausdorff Space near Finite Metric Spaces in General Position,” arXiv:1611.04484v1 (2016; full HTML inspected).
3. R. Fukano, “Every Compact Metric Space Is Isometrically Embeddable into the Gromov-Hausdorff Space,” arXiv:2609.21469v1 (first public date 2026-09-18; abstract inspected).
