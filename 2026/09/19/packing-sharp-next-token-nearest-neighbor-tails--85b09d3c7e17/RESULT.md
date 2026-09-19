# Packing-sharp stability for high-dimensional next-token nearest-neighbor tails

## Result

Let \((\mathcal X,d)\) be a metric space, fix \(\delta>0\), and let \(X_1,\dots,X_{n+1}\) be a stationary stochastic process. Define the next-token nearest-neighbor tail probability
\[
\mathsf{NS}_d(\delta)
=
\mathbb P\!\left(\min_{i\in[n]}d(X_{n+1},X_i)>\delta\right).
\]
For a window length \(\tau\in\{1,\dots,n-1\}\), set
\[
\mathcal D_i=\{i,\dots,(i+\tau-1)\wedge n\},
\qquad
\mathcal I_i=[n]\setminus\mathcal D_i,
\]
and use the leave-a-window-out estimator
\[
\widehat{\mathsf{NS}}_d(\tau)
=
\frac1n\sum_{i=1}^n
\mathbf 1\!\left\{\min_{j\in\mathcal I_i}d(X_i,X_j)>\delta\right\}.
\]

Define the local strict packing number
\[
\kappa_{\mathcal X}(\delta)
=
\sup_{a\in\mathcal X}
\sup\left\{
|A|:
A\subseteq \overline B(a,\delta),\quad
d(x,y)>\delta\ \text{for all distinct }x,y\in A
\right\}.
\]
Assume \(\kappa_{\mathcal X}(\delta)<\infty\).

**Theorem.** The nearest-neighbor functional has the same out-of-sample deletion stability as in the one-dimensional argument,
\[
r_f(\tau,n)=\frac{\tau}{n},
\]
and its leave-a-window-out estimator satisfies the sharper replace-one bound
\[
\boxed{
\sup_{a,b\in\mathcal X}\sup_{k\in[n]}
\left|
\widehat{\mathsf{NS}}_d(X^{(k)}(a),\tau)
-
\widehat{\mathsf{NS}}_d(X^{(k)}(b),\tau)
\right|
\le
\frac{\kappa_{\mathcal X}(\delta)+1}{n}.
}
\]
Consequently, if the process has \(\beta\)-mixing coefficient \(\beta(\tau)\) and \(X^n\) is \((\gamma,s)\)-Martonizable in the sense of Nakul--Muthukumar--Pananjady, then
\[
\boxed{
\operatorname{MSE}\!\left(
\widehat{\mathsf{NS}}_d(\tau),\mathsf{NS}_d(\delta)
\right)
\le
64\left(\beta(\tau)+\frac{\tau}{n}\right)^2
+4\left(\frac{\tau}{n}\right)^2
+
\frac{2\gamma^2s\,\bigl(\kappa_{\mathcal X}(\delta)+1\bigr)^2}{n}.
}
\]

This extends the nearest-neighbor-tail guarantee from real-valued state spaces to every metric space with finite local strict packing number. It also sharpens the constant already in one dimension: for every \(\mathcal X\subseteq\mathbb R\), \(\kappa_{\mathcal X}(\delta)\le2\), so the bounded-differences constant can be taken as \(B_f=3\), improving the previously stated \(B_f=5\). The variance term in that corollary therefore improves from \(50\gamma^2s/n\) to \(18\gamma^2s/n\).

## Why the constant is \(\kappa+1\), not \(2\kappa+1\)

Fix a coordinate \(k\) and compare replacement values \(a,b\). For \(j\ne k\), a local indicator can change only when \(k\in\mathcal I_j\). Put
\[
M_j=
\min_{i\in\mathcal I_j\setminus\{k\}}d(X_j,X_i).
\]
Then, for \(c\in\{a,b\}\),
\[
\widehat{\mathsf{NS}}_{d,(j)}(X^{(k)}(c),\tau)
=
\mathbf1\{M_j>\delta,\ d(X_j,c)>\delta\}.
\]
Define the two exact change classes
\[
A=
\{j\ne k:k\in\mathcal I_j,\ M_j>\delta,\ d(X_j,a)\le\delta<d(X_j,b)\},
\]
\[
B=
\{j\ne k:k\in\mathcal I_j,\ M_j>\delta,\ d(X_j,b)\le\delta<d(X_j,a)\}.
\]
Indices in \(A\) contribute \(-1\) to the difference of the two unnormalized estimator sums, whereas indices in \(B\) contribute \(+1\). This sign cancellation is what is lost if one merely counts all changed indicators.

For two distinct indices \(j<j'\) in \(A\), the definition of the one-sided deletion window gives \(j\in\mathcal I_{j'}\setminus\{k\}\). Hence
\[
d(X_j,X_{j'})\ge M_{j'}>\delta.
\]
Also every \(X_j\) with \(j\in A\) belongs to \(\overline B(a,\delta)\). Thus \(\{X_j:j\in A\}\) is a strict \(\delta\)-packing of \(\overline B(a,\delta)\), so \(|A|\le\kappa_{\mathcal X}(\delta)\). Likewise \(|B|\le\kappa_{\mathcal X}(\delta)\).

The \(k\)-th local indicator itself changes by at most one. Therefore
\[
n\left|
\widehat{\mathsf{NS}}_d(X^{(k)}(a),\tau)
-
\widehat{\mathsf{NS}}_d(X^{(k)}(b),\tau)
\right|
\le
\bigl||B|-|A|\bigr|+1
\le
\kappa_{\mathcal X}(\delta)+1.
\]
This proves the bounded-differences claim.

The deletion-stability proof does not use an ordering or linear geometry of the state space: it uses only the inclusions among the retained and deleted index blocks and the dichotomy \(d(X_{n+1},X_j)\le\delta\) versus \(>\delta\). Replacing absolute distance by an arbitrary metric therefore leaves the argument unchanged and yields \(r_f(\tau,n)=\tau/n\). Substitution into the general mean-squared-error theorem of Nakul--Muthukumar--Pananjady gives the displayed risk bound.

## Euclidean form and an exact geometric stability constant

For \(\mathcal X=\mathbb R^d\), scaling removes \(\delta\). Define the strict kissing number
\[
\kappa_d^{>}
=
\max\left\{
|U|:
U\subset S^{d-1},\quad
\|u-v\|_2>1\ \text{for all distinct }u,v\in U
\right\}.
\]
Then
\[
\boxed{\kappa_{\mathbb R^d}(\delta)=\kappa_d^{>}.}
\]
Indeed, after translating and scaling, take a strict unit-separated set \(x_i=r_i u_i\) in the unit ball. If \(u_i\cdot u_j\ge1/2\) and, without loss of generality, \(r_i\ge r_j\), then
\[
\|x_i-x_j\|_2^2
\le
r_i^2+r_j^2-r_ir_j
=
r_i^2-r_j(r_i-r_j)
\le1,
\]
a contradiction. Hence the radial projections \(u_i\) form a strict kissing configuration. The converse is immediate by placing a strict kissing configuration on the unit sphere.

Moreover the uniform replace-one constant is **exact** in full Euclidean space:
\[
\boxed{B_f^{\star}(\mathbb R^d,\delta)=\kappa_d^{>}+1.}
\]
For the lower bound, take a maximum strict kissing configuration \(x_1,\dots,x_m\) on the sphere of radius \(\delta\) about a point \(a\), where \(m=\kappa_d^{>}\), and choose \(b\) farther than \(\delta\) from every \(x_i\). With \(\tau=1\), use a trajectory consisting of \(a\) together with the \(m\) points \(x_i\). Replacing \(a\) by \(b\) flips every one of the \(m+1\) local indicators from \(0\) to \(1\). Thus any uniform bounded-differences constant must be at least \(m+1\), matching the upper bound.

Two elementary estimates are
\[
2d\le\kappa_d^{>}\le3^d.
\]
The lower bound is given by the cross-polytope \(\{\pm e_1,\dots,\pm e_d\}\). For the upper bound, disjoint radius-\(1/2\) balls around a strict unit-separated set in the unit ball all lie inside the radius-\(3/2\) ball, and volume comparison gives at most \(3^d\) points. Hence the Euclidean risk bound is explicit even without knowing the exact strict kissing number:
\[
\operatorname{MSE}
\le
64\left(\beta(\tau)+\frac{\tau}{n}\right)^2
+4\left(\frac{\tau}{n}\right)^2
+
\frac{2\gamma^2s(3^d+1)^2}{n}.
\]
In particular, for fixed \(d\) the same parametric dependence on the effective sample size is retained. The exact stability constant also shows that dimension-free replace-one control is impossible for this estimator: already \(B_f^\star\ge2d+1\).

For reference, \(\kappa_1^{>}=2\), \(\kappa_2^{>}=5\), and \(\kappa_3^{>}=12\). Thus the exact Euclidean bounded-differences constants in dimensions \(1,2,3\) are \(3,6,13\), respectively.

## Doubling spaces

If \((\mathcal X,d)\) has doubling constant \(\lambda\), meaning every radius-\(r\) ball can be covered by at most \(\lambda\) radius-\(r/2\) balls, then
\[
\kappa_{\mathcal X}(\delta)\le\lambda.
\]
Indeed, each radius-\(\delta/2\) covering ball contains at most one point of a strict \(\delta\)-packing. Therefore
\[
B_f\le\lambda+1,
\]
and the variance term in the risk bound is at most
\[
\frac{2\gamma^2s(\lambda+1)^2}{n}.
\]
This gives the same extension for any fixed-doubling-dimension state space, not only Euclidean data.

## Relation to prior work and originality boundary

Nakul, Muthukumar and Pananjady (2026) introduced the leave-a-window-out framework, proved the general Marton-coupling MSE theorem used above, and treated nearest-neighbor tails only for \(\mathcal X\subset\mathbb R\). Their Corollary 3 uses \(B_f=5\), and their discussion explicitly asks whether the nearest-neighbor functional can be studied in high dimensions. Those ingredients are prior work and are not claimed here.

Dimension-dependent packing arguments are classical in nearest-neighbor theory; Clarkson's survey on nearest-neighbor search and metric dimensions, and the older statistical nearest-neighbor literature, are important prior art. The claim here is narrower: the signed-cancellation refinement giving \(B_f\le\kappa+1\), its exact Euclidean sharpness \(B_f^\star=\kappa_d^{>}+1\), the resulting improvement from \(5\) to \(3\) already on the real line, and the corresponding dependent-data MSE extension to finite-packing/doubling/high-dimensional metric spaces.

Searches for the source paper together with packing numbers, kissing numbers, high-dimensional nearest-neighbor tails, replace-one stability, and leave-a-window-out estimation did not locate these statements. To the best of our knowledge, the exact specialization above is not in the inspected literature. A residual originality risk remains because classical Stone-lemma and nearest-neighbor-graph arguments use closely related packing geometry and could imply the geometric sensitivity step under different language.

## Limitations

The result inherits stationarity, \(\beta\)-mixing, and Martonizability assumptions from the underlying next-token theorem. A finite local strict packing number is needed for a dimension-independent-in-\(n\) bounded-differences constant; spaces with infinite local packing are not covered by this argument. The lower bound concerns the replace-one sensitivity of this particular leave-a-window-out estimator, not the minimax statistical difficulty of estimating \(\mathsf{NS}_d(\delta)\) over all estimators. No claim is made that the exponential crude Euclidean upper bound \(3^d\) is sharp. Exact strict kissing numbers are unknown in many dimensions. The full nearest-neighbor chapters of older pattern-recognition monographs were not exhaustively checked, so equivalent geometric stability bounds remain a residual originality risk.

## References

1. M. Nakul, V. Muthukumar, A. Pananjady, *Next-token functional estimation*, arXiv:2609.19529 (2026).
2. D. Paulin, *Concentration inequalities for Markov chains by Marton couplings and spectral methods*, Electronic Journal of Probability 20 (2015), no. 79. DOI: 10.1214/EJP.v20-4039.
3. K. L. Clarkson, *Nearest-neighbor searching and metric space dimensions*, in *Nearest-Neighbor Methods for Learning and Vision: Theory and Practice*, MIT Press (2006), pp. 15--59.
4. L. Devroye, L. Györfi, G. Lugosi, *A Probabilistic Theory of Pattern Recognition*, Springer (1996), especially the chapters on nearest-neighbor rules and consistency. DOI: 10.1007/978-1-4612-0711-5.
