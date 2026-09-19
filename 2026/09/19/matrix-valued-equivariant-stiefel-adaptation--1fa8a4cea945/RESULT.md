# Matrix-valued adaptive moments preserve Stiefel equivariance

## Result

Consider the embedded Stiefel manifold
\[
\operatorname{St}(d,r)=\{W\in\mathbb R^{d\times r}:W^\top W=I_r\},
\]
with the left ambient-coordinate action \(W\mapsto QW\), \(Q\in O(d)\). A recent Stiefel-attention construction (arXiv:2609.19363v1) argues that a single scalar second moment per frame is the unique form compatible with exact \(O(d)\)-equivariance, and its equivariance proof states that coordinatewise diagonal scaling can commute with every ambient rotation only when it is scalar.

Under the paper's stated \(O(d)\) criterion, that uniqueness claim is false for every \(r>1\). The full commutant of the left \(O(d)\) action is matrix-valued on the column index, and non-scalar adaptive covariance preconditioners remain exactly equivariant after Stiefel tangent projection and polar retraction. The same construction can in fact be made equivariant under both ambient \(O(d)\) rotations and right \(O(r)\) frame rotations.

This does **not** invalidate the source's scalar optimizer or its steepest-descent proposition. A scalar is special if one additionally requires the preconditioned direction to remain collinear with the embedded-metric Riemannian gradient for every gradient. The correction is that equivariance alone does not force scalar adaptation.

## 1. The exact commutant of ambient rotations

Let \(\mathcal L:\mathbb R^{d\times r}\to\mathbb R^{d\times r}\) be linear and suppose
\[
\mathcal L(QX)=Q\mathcal L(X)
\qquad\text{for every }Q\in O(d),\ X\in\mathbb R^{d\times r}.
\]
Then there is a unique \(B\in\mathbb R^{r\times r}\) such that
\[
\boxed{\mathcal L(X)=XB.}
\]
Conversely every right multiplication \(X\mapsto XB\) has this equivariance.

### Proof

Write \(X=[x_1,\ldots,x_r]\). The \(j\)-th output column of a linear map has the form
\[
(\mathcal L X)_j=\sum_{k=1}^r T_{jk}x_k
\]
for linear maps \(T_{jk}:\mathbb R^d\to\mathbb R^d\). Equivariance gives
\[
T_{jk}Q=QT_{jk}\qquad\forall Q\in O(d).
\]
The only real matrices commuting with every orthogonal matrix are scalar multiples of the identity, hence \(T_{jk}=b_{kj}I_d\). Therefore \((\mathcal L X)_j=\sum_k x_k b_{kj}\), i.e. \(\mathcal L(X)=XB\). The converse is immediate. \(\square\)

With the Frobenius inner product, \(\mathcal L\) is self-adjoint positive definite exactly when \(B\) is symmetric positive definite. Thus ambient \(O(d)\)-equivariance permits an \(r(r+1)/2\)-parameter family of positive anisotropic linear preconditioners, not one scalar.

There is an even sharper correction to the source's diagonal-scaling converse. If \(\mathcal L\) is diagonal in the standard entries as well as \(O(d)\)-equivariant, then \(B\) must be diagonal, but its \(r\) diagonal entries may differ. Hence
\[
\boxed{X\longmapsto X\operatorname{diag}(b_1,\ldots,b_r)}
\]
is coordinatewise, non-scalar for unequal \(b_j\), and still commutes with every ambient rotation. In vectorized form the left action is \(I_r\otimes Q\), whose diagonal commutant contains \(\operatorname{diag}(b_1I_d,\ldots,b_rI_d)\).

## 2. A two-column exact counterexample

Take \(d=4,r=2\),
\[
W=[e_1,e_2],\qquad
G=\begin{pmatrix}
0&0\\
0&0\\
1&0\\
0&2
\end{pmatrix}.
\]
Here \(W^\top G=0\), so \(G\) is already tangent. Its column covariance is
\[
C=G^\top G=\operatorname{diag}(1,4).
\]
The covariance-normalized direction is
\[
GC^{-1/2}=
\begin{pmatrix}
0&0\\
0&0\\
1&0\\
0&1
\end{pmatrix},
\]
which is not a scalar multiple of \(G\). Nevertheless, for every \(Q\in O(4)\),
\[
(QG)C^{-1/2}=Q(GC^{-1/2}),
\]
because \((QG)^\top(QG)=C\). Thus a genuinely anisotropic second moment already satisfies the source's ambient coordinate-freeness test exactly.

## 3. A matrix-valued adaptive moment that is equivariant on both sides

For the embedded metric, let
\[
\Pi_W(Z)=Z-W\operatorname{sym}(W^\top Z)
\]
be the orthogonal tangent projector. Let \(M_t\) be a tangent first-moment state and let the second-moment state be
\[
C_t=\beta C_{t-1}+(1-\beta)\,\xi_t^\top\xi_t\in\mathbb S_+^r.
\]
For \(\varepsilon\ge0\), define
\[
D_t=(C_t+\varepsilon^2I)^{-1/2},\qquad
\eta_t=\Pi_{W_t}(M_tD_t).
\]
A scalar Frobenius-norm trust cap may then be applied to \(\eta_t\), followed by polar retraction.

### Ambient equivariance

Under \(W\mapsto QW\), \(\xi\mapsto Q\xi\), \(M\mapsto QM\),
\[
\xi^\top\xi\mapsto \xi^\top Q^\top Q\xi=\xi^\top\xi,
\]
so \(C_t\) and \(D_t\) are unchanged. Since
\[
\Pi_{QW}(QZ)=Q\Pi_W(Z),
\]
we obtain
\[
\boxed{\eta_t(QW,Q\xi,QM)=Q\eta_t(W,\xi,M).}
\]
The Frobenius trust factor is invariant under \(Q\), and polar retraction satisfies \(\operatorname{polar}(QA)=Q\operatorname{polar}(A)\). Therefore the complete update is exactly \(O(d)\)-equivariant.

### Right-frame covariance and bi-equivariance

Let \(O\in O(r)\) act on a frame by \(W\mapsto WO\), and transform the optimizer state covariantly:
\[
\xi\mapsto\xi O,\qquad M\mapsto MO,\qquad C\mapsto O^\top C O.
\]
Matrix functional calculus gives
\[
D(O^\top C O)=O^\top D(C)O,
\]
and the Stiefel projector obeys
\[
\Pi_{WO}(ZO)=\Pi_W(Z)O.
\]
Hence
\[
\boxed{\eta(WO,\xi O,MO,O^\top C O)=\eta(W,\xi,M,C)O.}
\]
For simultaneous left and right rotations,
\[
\eta(QWO,Q\xi O,QMO,O^\top C O)=Q\eta(W,\xi,M,C)O.
\]
Finally,
\[
\operatorname{polar}(QAO)=Q\operatorname{polar}(A)O,
\]
so the entire trust-capped polar step is \(O(d)\times O(r)\)-equivariant whenever the internal state is transformed accordingly. For attention, the same right \(O(r)\) may be applied jointly to the query and key frames and their optimizer states.

When \(\varepsilon=0\), \(C_t\succ0\), and the entire gradient history is scaled by \(c>0\), a first-moment state scales as \(M_t\mapsto cM_t\) while \(C_t\mapsto c^2C_t\). Therefore
\[
(cM_t)(c^2C_t)^{-1/2}=M_tC_t^{-1/2},
\]
so the matrix-valued rule has the same degree-zero gradient-scale homogeneity as a scalar Adam normalization. A fixed \(\varepsilon>0\) introduces a settling scale, just as in the scalar rule.

The trust-region conditioning bound used in arXiv:2609.19363 depends only on \(\|\eta_t\|_F\). Consequently it is unchanged by whether \(\eta_t\) was produced by scalar or matrix-valued adaptation.

## 4. What scalar adaptation is actually unique for

There is a correct narrower uniqueness statement. If a fixed linear preconditioner \(\mathcal L\) is required to preserve the embedded-metric steepest-descent direction for **every** nonzero gradient, so that
\[
\mathcal L(X)\in\operatorname{span}\{X\}\qquad\forall X\ne0,
\]
then linearity forces \(\mathcal L=\lambda I\). Thus a scalar rescaling is the only fixed linear preconditioner that simultaneously leaves every Euclidean/Frobenius steepest direction unchanged.

Matrix-valued adaptation instead changes the metric/direction while remaining coordinate-equivariant. Hence the four properties emphasized by the source should be separated:

- ambient \(O(d)\)-equivariance does **not** force a scalar moment;
- gradient-scale homogeneity does **not** force a scalar moment;
- the source's Frobenius trust-cap conditioning argument does **not** force a scalar moment;
- preserving the embedded-metric steepest direction for every gradient does force scalar directional rescaling.

This distinction leaves the source's scalar method mathematically valid while removing the claimed uniqueness based on equivariance.

## 5. Prior literature narrows the algorithmic novelty further

The non-scalar construction above is not claimed as a new adaptive-manifold paradigm. Kasai, Jawanpuria, and Mishra (ICML 2019) already introduced RASA for matrix manifolds, explicitly maintaining left and right covariance matrices
\[
L_t=\beta L_{t-1}+(1-\beta)G_tG_t^\top/r,\qquad
R_t=\beta R_{t-1}+(1-\beta)G_t^\top G_t/n,
\]
preconditioning as \(L_t^{-1/4}G_tR_t^{-1/4}\), projecting the result to the tangent space, and allowing either the row or column adaptation to be switched off. Their practical diagonal approximation is coordinate-dependent, but their full covariance framework already contains matrix-valued adaptive Stiefel preconditioning as prior art.

There is also direct prior art for adaptive Stiefel optimization of transformer query/key matrices. Kong, Wang, and Tao (ICLR 2023; arXiv:2205.14173) derive an Adam-Stiefel optimizer with elementwise second moments and apply Stiefel constraints specifically to the \(W_i^Q\) and \(W_i^K\) matrices of Vision Transformer attention. Their experiments compare Stiefel Adam, projected Stiefel Adam, and Stiefel SGD on those constrained attention matrices. Therefore the statement in arXiv:2609.19363v1 that the closest prior application to \(W_Q,W_K\) used fixed-step Riemannian SGD is not supported by this earlier work.

These prior results do not supply the 2026 paper's particular scalar, trust-capped, embedded-metric update, and they do not negate its empirical results. They do show that (i) non-scalar adaptive matrix-manifold preconditioning predates it and (ii) adaptive Stiefel optimization of transformer query/key projections predates it.

## Verification

A standalone NumPy artifact checks an exact two-column non-scalar example and a random \(O(d)\times O(r)\) covariance-preconditioned polar step. In the recorded run, the left-equivariance error is \(3.20\times10^{-16}\), the columnwise-diagonal commutant error is exactly zero at displayed precision, the bi-equivariant tangent-direction error is \(1.96\times10^{-15}\), and the bi-equivariant polar-step error is \(8.05\times10^{-16}\).

## Limitations

The commutant theorem is elementary representation theory and is not claimed new in isolation. Full matrix adaptive moments also have clear prior art in RASA. The contribution here is the source-specific correction: under the exact \(O(d)\)-equivariance criterion stated in arXiv:2609.19363v1, scalar second moments are not unique, and the paper's diagonal-commutant converse misses the column multiplicity of the \(O(d)\) representation. The stronger bi-equivariant covariance construction makes the surviving degrees of freedom explicit.

An anisotropic matrix preconditioner is generally **not** steepest descent in the source's fixed embedded metric; it is better viewed as steepest descent in a different/adaptive metric. No convergence-rate or transformer-accuracy improvement is claimed for the matrix-valued rule. Full covariance costs \(O(r^2)\) state and matrix-function work, though \(r\) is the head width rather than the ambient embedding dimension. The literature correction is based on the accessible versions cited below; contemporaneous revisions of the very recent 2026 preprint may change its claims.

## References

1. R. D. Guerrero, *Stiefel Attention: When the Geometry of Transformer Projection Matrices Dominates Optimizer Choice—and When It Does Not*, arXiv:2609.19363v1, 2026. https://arxiv.org/abs/2609.19363
2. H. Kasai, P. Jawanpuria, B. Mishra, *Riemannian adaptive stochastic gradient algorithms on matrix manifolds*, ICML 2019, PMLR 97:3262–3271. https://proceedings.mlr.press/v97/kasai19a.html
3. L. Kong, Y. Wang, M. Tao, *Momentum Stiefel Optimizer, with Applications to Suitably-Orthogonal Attention, and Optimal Transport*, ICLR 2023, arXiv:2205.14173. https://arxiv.org/abs/2205.14173
