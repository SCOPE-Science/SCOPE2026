# An exact stability frontier for curvature-adaptive gradient tracking

## Finding

Consider the main AdGT update
\[
 x^{k+1}=W(x^k-D^k y^k),\qquad
 y^{k+1}=Wy^k+\nabla f(x^{k+1})-\nabla f(x^k),
\]
with two scalar quadratic objectives \(f_i(x)=\tfrac{h_i}{2}(x-c_i)^2\), \(h_i>0\), complete averaging \(W=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\), and the source's local-gradient stepsize update initialized at \(\alpha_i^0=q/h_i\), where \(q=1/(2\gamma)>0\). Assume the initial local smoothness estimates are defined. The adaptive steps remain exactly \(\alpha_i^k=q/h_i\). After the first averaging update, the common primal error \(e_k=x^k-x^*\), where \(x^*=(h_1c_1+h_2c_2)/(h_1+h_2)\), obeys
\[
 e_{k+1}=(1-q)e_k-q\xi e_{k-1},\qquad
 \xi=\frac{(h_1-h_2)^2}{4h_1h_2}\ge0,
\]
for all sufficiently large \(k\). The reduced recurrence is asymptotically stable exactly when
\[
 q<q_{\rm crit}(\xi):=
 \begin{cases}
 \dfrac{2}{1-\xi},&0\le\xi\le\tfrac13,\\[4pt]
 \dfrac{1}{\xi},&\xi\ge\tfrac13.
 \end{cases}
\]
Equivalently, the exact safety-factor condition is \(\gamma>(1-\xi)/4\) for \(0\le\xi\le\tfrac13\), and \(\gamma>\xi/2\) for \(\xi\ge\tfrac13\). At the boundary, the reduced recurrence has a unit-modulus root; above it, at least one root lies outside the unit disk.

## Assumptions and scope

The two-agent graph uses the symmetric doubly-stochastic matrix \(W=\tfrac12\mathbf1\mathbf1^\top\). Each local objective is a scalar strongly convex quadratic with curvature \(h_i>0\). The update uses \(D^k=\operatorname{diag}(\alpha_1^k,\alpha_2^k)\), the tracker is initialized by \(y_i^0=\nabla f_i(x_i^0)\), and the stepsize update is the local-gradient candidate \(\alpha_i^{k+1}=\min\{1/(2\gamma L_{f_i}^k),\sqrt{1+\theta_i^k}\alpha_i^k\}\), with \(\theta_i^0=0\). The source specifies that if a later primal difference is zero, the stepsize is held fixed. For a nonzero difference on a quadratic, \(L_{f_i}^k=h_i\). With \(q=1/(2\gamma)\) and \(\alpha_i^0=q/h_i\), both branches therefore keep \(\alpha_i^k=q/h_i\).

The claim is only about this exact scalar-quadratic, two-agent, complete-averaging specialization of AdGT. It does not assert an exact threshold for larger networks, nonlinear objectives, noisy updates, or the source's other candidate rules.

## Proof

Write \(H=\operatorname{diag}(h_1,h_2)\) and \(D=qH^{-1}\). Since \(W\) maps every vector to its average repeated twice, \(x_1^k=x_2^k=x^k\) for every \(k\ge1\). The gradient-tracking invariant
\[
 \mathbf1^\top y^k=\mathbf1^\top\nabla f(x^k)
\]
holds initially and is preserved by the update because \(\mathbf1^\top W=\mathbf1^\top\). Consequently, for \(k\ge1\),
\[
 \bar y_k:=\frac{y_1^k+y_2^k}{2}
 =\frac{h_1+h_2}{2}e_k.
\]
Let \(d_k=(y_1^k-y_2^k)/2\). The tracker update gives
\[
 d_{k+1}=\frac{h_1-h_2}{2}(x^{k+1}-x^k),
\]
so for \(k\ge2\), \(d_k=(h_1-h_2)(e_k-e_{k-1})/2\). The primal update is
\[
 e_{k+1}=e_k-\frac q2\left(\frac{\bar y_k+d_k}{h_1}+\frac{\bar y_k-d_k}{h_2}\right).
\]
Substituting the formulas for \(\bar y_k\) and \(d_k\), and using
\[
 \frac{(h_1+h_2)^2}{4h_1h_2}=1+\xi,
\]
reduces the update to \(e_{k+1}=(1-q)e_k-q\xi e_{k-1}\). The characteristic polynomial is
\[
 p(r)=r^2+(q-1)r+q\xi.
\]
For a real monic quadratic \(r^2+ar+b\), the Jury/Schur conditions for both roots to lie strictly inside the unit disk are \(|b|<1\), \(1+a+b>0\), and \(1-a+b>0\). Here \(a=q-1\), \(b=q\xi\), and these conditions reduce to \(q\xi<1\) and \(2-q+q\xi>0\), because \(1+a+b=q(1+\xi)>0\). Thus the exact conditions are \(q\xi<1\) and \(q(1-\xi)<2\). Taking the tighter positive upper bound gives the displayed piecewise \(q_{\rm crit}\). At equality, either \(p(-1)=0\) or \(b=1\); beyond the active boundary the corresponding condition fails strictly, so the reduced recurrence is not asymptotically stable.

The full four-dimensional state matrix has an additional eigenvalue \(1\) corresponding to a constant consensus shift with zero tracker, which violates the tracking invariant unless that shift is zero. It is therefore excluded from the algorithm's invariant state subspace. The zero eigenvalue is a one-step disagreement transient. The two roots of \(p\) are exactly the remaining modes that determine asymptotic stability.

## Verification

The standalone script `verify.py` computes the exact symbolic characteristic polynomial of the four-dimensional linear update and checks
\[
 \det(rI-T)=(r-1)r\bigl(r^2+(q-1)r+q\xi\bigr).
\]
It also checks the two Jury identities symbolically and tests rational parameter points on both sides of each branch of the stability boundary. The script prints `VERIFY_OK` when all checks pass. The proof of the infinite-iteration stability criterion is the exact quadratic Schur test, not finite simulation.

## Relationship to prior work

The primary source, *AdGT: Decentralized Gradient Tracking with Adaptive Per-Agent Stepsizes* (arXiv:2504.15196), defines the local-gradient adaptive rule and proves linear convergence under a conservative sufficient stepsize bound depending on graph and objective constants. Its analyzed update does not state the exact necessary-and-sufficient boundary derived here for two scalar quadratics with reciprocal-curvature steps and complete averaging. The classical gradient-tracking analysis in Qu and Li, *Harnessing Smoothness to Accelerate Distributed Optimization*, uses a common fixed stepsize and a general-network sufficient bound; that statement does not imply the heterogeneous reciprocal-curvature recurrence or its sharp boundary. A nearby indexed result on exact graph-specific tuning for homogeneous distributed gradient tracking treats a common-step homogeneous quadratic setting, rather than this heterogeneous adaptive specialization.

## Limitations

The theorem is exact only for two scalar quadratic local objectives, the complete-averaging matrix, the source's main local-gradient stepsize update, and the specified initialization. It does not classify the stability of other weight matrices, more than two agents, multidimensional Hessians, time-varying stepsizes, or nonlinear objectives. The closest indexed homogeneous-stepsize record was available as a summary rather than a full-text source; it is materially different in its stated object, but the possibility of an unindexed related specialization remains a residual originality risk.

## References

1. D. Ghaderyan and S. Werner, “AdGT: Decentralized Gradient Tracking with Adaptive Per-Agent Stepsizes,” arXiv:2504.15196, first public version 2025-04-21; relevant version v5 updated 2026-09-14. https://arxiv.org/abs/2504.15196
2. G. Qu and N. Li, “Harnessing Smoothness to Accelerate Distributed Optimization,” arXiv:1605.07112; IEEE Transactions on Control of Network Systems 5(3), 1245–1260, 2018. https://arxiv.org/abs/1605.07112
3. Indexed comparison: “Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking,” record 2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6 (summary inspected).
