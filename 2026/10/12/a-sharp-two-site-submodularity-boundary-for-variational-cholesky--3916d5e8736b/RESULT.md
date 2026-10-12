# A sharp two-site submodularity boundary for variational Cholesky pivoting

## Finding

The variational-free-energy (VFE) improvement associated with a Cholesky/Nyström pivot set is monotone but need not have diminishing returns. In the smallest nontrivial positive-definite kernel, the precise boundary is given below. This is a complete classification within the stated two-site family, not a claim about all kernels.

For \(0<r<1\) and \(a\ge 0\), define
\[
K_r=\begin{pmatrix}1&r\\r&1\end{pmatrix},\qquad y=a\begin{pmatrix}1\\-1\end{pmatrix}.
\]
With independent unit-variance observation noise, and subset gain \(G\) as below, put
\[
B(r)=r^2-\log(2+r^2)+\frac12\log(4-r^2),\qquad C(r)=\frac{3r(1-r)}{(2+r^2)(2-r)}.
\]
The exact two-element submodularity defect is
\[
\boxed{D(r,a)=G(\{1\})+G(\{2\})-G(\{1,2\})-G(\varnothing)=B(r)-C(r)a^2.}
\]
Both \(B(r)\) and \(C(r)\) are strictly positive. Hence **diminishing returns holds if and only if**
\[
\boxed{a^2\le \frac{(2+r^2)(2-r)}{3r(1-r)}\left[r^2-\log(2+r^2)+\frac12\log(4-r^2)\right].}
\]
The boundary is attained with equality. The strict reverse inequality gives increasing returns despite positive-definite matrices and positive individual gains.

The exact witness \(r=1/2\), \(a=1\) has
\[
\boxed{D(1/2,1)=\frac1{36}+\frac12\log\frac{20}{27}<0.}
\]
More strongly, for each fixed \(a>0\),
\[
D(r,a)=-\frac{3a^2}{4}r+\frac{3(1+a^2)}8r^2+O_a(r^3)<0
\]
for all sufficiently small \(r>0\), even though the spectral condition number of \(K_r\) tends to one. Finally, defining the two-element weak-submodularity ratio by \(\gamma(r,a)= [G(\{1\})+G(\{2\})]/G(\{1,2\})\), one has
\[
\boxed{\lim_{r\uparrow1}\lim_{a\to\infty}\gamma(r,a)=0.}
\]
Thus no uniformly positive two-element ratio exists over the family.

## Assumptions and scope

For each \(J\subseteq\{1,2\}\), let \(Q_\varnothing=0\), and if \(J\ne\varnothing\) let
\[
Q_J=K_{:,J}K_{J,J}^{-1}K_{J,:}.
\]
Every submatrix used in this expression is invertible because \(K_r\) is strictly positive definite. The VFE objective at a positive-semidefinite \(Q\preceq K_r\), at fixed noise variance one, is
\[
\mathcal L(Q)=-\frac12\left[\log\det(I_2+Q)+y^{\mathsf T}(I_2+Q)^{-1}y+\operatorname{tr}(K_r-Q)+2\log(2\pi)\right].
\]
Define \(G(J)=\mathcal L(Q_J)-\mathcal L(0)\). The order of selected pivots does not affect the exact Nyström matrix. The only possible nontrivial submodularity condition for two elements is \(G(\{1\})+G(\{2\})\ge G(\{1,2\})\) since \(G(\varnothing)=0\). All theorems apply for every real parameter in the stated ranges, with no probabilistic or floating-point assumptions.

## Proof

**Step 1, explicit subset values.** Directly,
\[
Q_{\{1\}}=\begin{pmatrix}1&r\\r&r^2\end{pmatrix},\quad
Q_{\{2\}}=\begin{pmatrix}r^2&r\\r&1\end{pmatrix},\quad Q_{\{1,2\}}=K_r.
\]
The rank-one determinant lemma gives \(\det(I_2+Q_{\{j\}})=2+r^2\), and the full determinant is \(\det(I_2+K_r)=4-r^2\). Using the Sherman–Morrison identity and the antisymmetric direction of \(y\), exact substitution gives
\[
\begin{aligned}
G(\{1\})=G(\{2\})&=\frac12\left[1+r^2-\log(2+r^2)+\frac{a^2(1-r)^2}{2+r^2}\right],\\
G(\{1,2\})&=1-\frac12\log(4-r^2)+\frac{a^2(1-r)}{2-r}.
\end{aligned}
\]
Subtracting the full-set gain from the sum of singleton gains yields \(D(r,a)=B(r)-C(r)a^2\), with the displayed rational coefficient \(C(r)>0\).

**Step 2, strict positivity of the threshold numerator.** Set \(t=r^2\in(0,1)\) and \(f(t)=t-\log(2+t)+\frac12\log(4-t)\). Then \(f(0)=0\) and
\[
f'(t)=1-\frac1{2+t}-\frac1{2(4-t)}>1-\frac12-\frac16=\frac13>0.
\]
Thus \(B(r)=f(r^2)>0\); solving the exact inequality \(D\ge0\) yields the stated necessary and sufficient threshold. At \(r=1/2\), elementary substitution gives the displayed strict negative witness, because \(20/27<e^{-1/18}\) (or directly using the alternating series for \(\log(1-x)\)).

**Step 3, arbitrarily weak kernel correlations.** Taylor expansion at \(r=0\) gives \(B(r)=3r^2/8+O(r^4)\) and \(C(r)=3r/4-3r^2/8+O(r^3)\). For any fixed \(a>0\), the negative first-order term dominates. Since the eigenvalues of \(K_r\) are \(1\pm r\), its condition number tends to one. The model has no singularity in this limit.

**Step 4, vanishing uniform weak-submodularity ratio.** Using the values in Step 1, the leading coefficients of \(a^2\) give, for each fixed \(r\in(0,1)\),
\[
\lim_{a\to\infty}\gamma(r,a)
=\frac{(1-r)(2-r)}{2+r^2}.
\]
This is positive for every fixed \(r<1\) but tends to zero as \(r\uparrow1\). Moreover, the limiting ratio of the after-first marginal gain to the before-first gain is
\[
\lim_{a\to\infty}\frac{G(\{1,2\})-G(\{1\})}{G(\{2\})}
=\frac{2(2+r^2)}{(1-r)(2-r)}-1,
\]
which diverges as \(r\uparrow1\). These statements require an ordered limit, not a single fixed data amplitude.

**Step 5, monotonicity without submodularity.** Every legal Nyström enlargement has \(0\preceq Q_J\preceq Q_{J'}\preceq K_r\). The directional derivative of \(\mathcal L(Q)\) along a positive-semidefinite increment \(H\) is
\[
\frac12\operatorname{tr}\!\left(\left[I_2-(I_2+Q)^{-1}+(I_2+Q)^{-1}yy^{\mathsf T}(I_2+Q)^{-1}\right]H\right)\ge0.
\]
The bracket is positive semidefinite for \(Q\succeq0\); therefore \(G\) is monotone and all strictly nonempty marginal gains in this nondegenerate family are positive. Monotonicity does not imply diminishing returns.

## Verification

The standalone standard-library program `verify.py` reconstructs the Nyström matrices and computes all three VFE gains using exact rational matrix entries for \(2170\) parameter-and-data configurations. It independently checks the symbolic defect, monotonicity, a strict witness, and ten asymptotic-scale cases; it returns `VERIFY_OK`. No finite enumeration is offered as a proof of the real-parameter assertions. Steps 1–5 are the complete analytic proof.

## Relationship to prior work

Titsias (2009) introduced the collapsed variational bound and greedy inducing-variable selection. Cao, Brubaker, Fleet and Hertzmann (2013) derived exact gains and algorithms for sparse GP inducing-point optimization. Schaub and Zaspel (2026, first publicly posted June 1) derived and implemented a data-aware VFE pivot rule for Cholesky, explicitly crediting the earlier Cao formula and proving per-step VFE monotonicity. Those definitions, closed-form gains, and monotonicity are prior art. The present claim is the **exact, data-amplitude-dependent two-pivot diminishing-returns phase boundary**, its weak-correlation obstruction, and vanishing uniform weak-submodularity ratio; these statements are not the general gain formula, and no greedy approximation theorem is claimed. Classical mutual-information submodularity under conditional-independence hypotheses uses a different set function; it cannot be transferred by identifying the objectives merely by name.

## Limitations

The classification uses a normalized real two-site kernel, positive off-diagonal correlation, antipodal observations, fixed unit noise variance, and exact Nyström/Cholesky selection. It proves neither an approximation ratio for an actual greedy algorithm nor a general dimension-independent obstruction for every kernel or data configuration. The negative example does not rule out special structure or restricted observational regimes where VFE submodularity holds. A previously unindexed equivalent calculation could exist.

## References

1. M. K. Titsias, *Variational Learning of Inducing Variables in Sparse Gaussian Processes*, AISTATS 2009, PMLR 5, pp. 567–574, https://proceedings.mlr.press/v5/titsias09a.html .
2. Y. Cao, M. Brubaker, D. Fleet and A. Hertzmann, *Efficient Optimization for Sparse Gaussian Process Regression*, arXiv:1310.6007, https://arxiv.org/abs/1310.6007 .
3. L. Schaub and P. Zaspel, *Variational Free Energy Pivot Selection for Pivoted Cholesky*, arXiv:2606.01821v1, first posted 2026-06-01, https://arxiv.org/abs/2606.01821 .
4. A. Krause, A. Singh and C. Guestrin, *Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies*, JMLR 9 (2008), pp. 235–284, https://www.jmlr.org/papers/v9/krause08a.html .
