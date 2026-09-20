# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The argument was checked against the definitions and proof structure of Nakul--Muthukumar--Pananjady (2026). Their general theorem gives
\[
\operatorname{MSE}(\widehat\theta,\theta)
\le
2\left(4\|f\|_\infty(\beta(\tau)+\tau/n)+r_f(\tau,n)\right)^2
+
\frac{2\gamma^2B_f^2s}{n}.
\]
For nearest-neighbor tails their deletion-stability proof uses only index-block inclusions and threshold events of the form distance \(\le\delta\), so replacing absolute distance on \(\mathbb R\) by an arbitrary metric leaves the proof unchanged and gives \(r_f=\tau/n\).

The bounded-differences refinement is the key point. For a replacement \(a\to b\), every changed local indicator away from the replaced coordinate belongs to one of two disjoint classes: points within \(\delta\) of \(a\) but not \(b\), whose contributions change in one direction, and points within \(\delta\) of \(b\) but not \(a\), whose contributions change in the opposite direction. Each class is a strict \(\delta\)-packing inside one radius-\(\delta\) ball, by the same chronological argument used in the source paper. Hence each class has at most \(\kappa_{\mathcal X}(\delta)\) points, but the estimator difference contains the difference of their cardinalities, not their sum. Including the replaced coordinate gives \(B_f\le\kappa_{\mathcal X}(\delta)+1\).

The Euclidean identification with a strict kissing number was checked directly. Radial projection of a strict unit-separated subset of the unit ball preserves strict unit separation on the sphere: if two projected directions had inner product at least \(1/2\), the original two points would be at distance at most one. Conversely, any strict spherical code lies in the unit ball. The lower-bound construction takes a maximum strict kissing configuration around a center and replaces that center by a distant point at \(\tau=1\); all local indicators flip in the same direction. This attains \((\kappa_d^{>}+1)/n\), proving exactness of the Euclidean uniform bounded-differences constant.

The doubling-space corollary follows because a radius-\(\delta/2\) covering ball contains at most one point of a strict \(\delta\)-packing. The elementary Euclidean bounds \(2d\le\kappa_d^{>}\le3^d\) follow from the cross-polytope and a volume packing argument.

Substituting \(B_f=\kappa+1\), \(\|f\|_\infty=1\), and \(r_f=\tau/n\) into the source theorem gives the stated MSE bound. In one dimension \(\kappa\le2\), so \(B_f=3\) is valid and changes the source variance coefficient from \(2\cdot5^2=50\) to \(2\cdot3^2=18\).

## Originality

The originality claim is deliberately narrow. Nakul--Muthukumar--Pananjady (2026) provide the leave-a-window-out estimator, the general dependent-data MSE theorem, and the real-line nearest-neighbor result with \(B_f=5\). They explicitly identify extension of this nearest-neighbor functional to high dimensions as an open question.

Packing and dimension arguments are classical in nearest-neighbor theory. Clarkson (2006) surveys nearest-neighbor search through metric-space dimension, and Devroye--Györfi--Lugosi (1996) contains classical geometric arguments for nearest-neighbor rules. No novelty is claimed for packing numbers, doubling dimension, spherical codes, or Stone-type geometry themselves.

Searches targeted combinations of the source paper with high-dimensional nearest-neighbor tails, packing/kissing numbers, replace-one stability, bounded differences, and leave-a-window-out estimation. No inspected source stated the signed-cancellation bound \(B_f\le\kappa+1\), the exact Euclidean constant \(\kappa_d^{>}+1\), or the resulting improvement of the source's one-dimensional constant from 5 to 3.

The main residual originality risk is older nearest-neighbor stability literature. The full nearest-neighbor chapters of Devroye--Györfi--Lugosi (1996) were not exhaustively inspected, and classical nearest-neighbor-graph/Stone-lemma results may imply an equivalent packing sensitivity statement under different terminology. Clarkson's 2006 chapter was inspected at the bibliographic/summary level for its metric-dimension context rather than checked theorem by theorem for this estimator-specific statement. The originality conclusion is therefore only to the best of our knowledge.

## Value

The result answers the source paper's explicit high-dimensional question for all metric spaces with finite local packing and for all doubling spaces. It also detects a cancellation missed by the source proof, improving the existing real-line finite-sample constant before any high-dimensional generalization is made.

The Euclidean lower construction shows that the resulting dimension dependence is not merely an artifact of the proof: for the same estimator, the uniform replace-one constant is exactly the strict kissing number plus one, and in particular is at least \(2d+1\). Thus the result gives both a positive high-dimensional extension and a geometric obstruction to dimension-free stability for this estimator.

## Limitations

The statistical theorem inherits stationarity, beta-mixing, and Martonizability assumptions from the source framework. The lower bound is for the replace-one stability constant of this estimator, not a minimax lower bound over all estimators. Metric spaces with infinite local strict packing are not covered. The crude Euclidean bound \(3^d\) is not claimed sharp, and exact strict kissing numbers are unknown in many dimensions. Older nearest-neighbor literature remains a material residual originality risk. No independent validation is claimed.
