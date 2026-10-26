# Rank growth need not order dynamical low-rank covariance predictions

## Finding
Consider the dynamical low-rank approximation of a covariance Lyapunov equation with zero drift and positive-semidefinite process noise. Although each exact rank-constrained prediction remains positive semidefinite and below the untruncated exact covariance in Loewner order, increasing the approximation rank from one to two need not increase the predicted covariance in Loewner order. This failure occurs already in dimension three, for positive definite initial covariance and rank-one positive-semidefinite noise, at every sufficiently small positive time.

More precisely, let \(a>b>c>0\), \(\Sigma_0=\operatorname{diag}(a,b,c)\), and let \(Q=(q_{ij})\) be any real symmetric positive-semidefinite \(3\times3\) matrix with \(q_{12}q_{23}\ne0\). For ranks \(r=1,2\), initialize the rank-\(r\) solution at the leading spectral truncation of \(\Sigma_0\), and evolve by the **exact continuous-time tangent-projected Lyapunov equation**. Then there is \(\varepsilon>0\) such that \(Y_2(t)-Y_1(t)\) is indefinite whenever \(0<t<\varepsilon\).

An explicit example is \(\Sigma_0=\operatorname{diag}(3,2,1)\) and \(Q=\boldsymbol{1}\boldsymbol{1}^{\mathsf T}\), where \(\boldsymbol{1}=(1,1,1)^{\mathsf T}\). For \(z=(1,0,1/3)^{\mathsf T}\),
\[
 z^{\mathsf T}(Y_2(t)-Y_1(t))z=-\frac{t^2}{18}+O(t^3),
 \qquad e_2^{\mathsf T}(Y_2(t)-Y_1(t))e_2=2+O(t).
\]
Thus the difference has a negative and a positive quadratic form. No smaller ambient dimension allows this failure for ranks one and two under the assumptions below.

## Assumptions and scope
All matrices are real. The exact covariance solves the three-dimensional Lyapunov initial-value problem
\[
 \dot\Sigma(t)=Q,\qquad \Sigma(0)=\Sigma_0,\qquad \Sigma(t)=\Sigma_0+tQ.
\]
For each \(r\in\{1,2\}\), define \(Y_r(t)\) by
\[
 \dot Y_r=P_rQ+QP_r-P_rQP_r,\qquad
 P_r(t)=\operatorname{proj}_{\operatorname{ran}Y_r(t)},
 \qquad Y_r(0)=\operatorname{diag}(a,\ldots,\lambda_r,0,\ldots,0),
\]
where explicitly \(Y_1(0)=\operatorname{diag}(a,0,0)\) and \(Y_2(0)=\operatorname{diag}(a,b,0)\). The projector \(P_r\) is the standard Frobenius-orthogonal tangent-space projector at a symmetric rank-\(r\) matrix. Solutions are meant in exact arithmetic; no time-discretization or observation-update formula is asserted.

## Proof
**1. Existence, positivity, and comparison with the full covariance.** Write \(Y=USU^{\mathsf T}\), where \(U^{\mathsf T}U=I_r\) and \(S\) is positive definite. The tangent-projected equation has the local factor form
\[
 \dot U=(I-UU^{\mathsf T})QUS^{-1},\qquad \dot S=U^{\mathsf T}QU.
\]
Since \(Q\succeq0\), \(S(t)\succeq S(0)\succ0\) and the inverse in the factor equation stays bounded. A compact Stiefel factor together with bounded \(\dot S\) gives a global solution of fixed positive rank. Hence \(Y_r(t)\succeq0\). For each rank,
\[
 Q-\dot Y_r=(I-P_r)Q(I-P_r)\succeq0.
\]
Because \(\Sigma_0-Y_r(0)\succeq0\), integration gives
\[
 \Sigma(t)-Y_r(t)
 =\Sigma_0-Y_r(0)+\int_0^t(I-P_r(s))Q(I-P_r(s))\,ds\succeq0.
\]
This comparison is **between each truncation and the untruncated solution**; it does not compare distinct truncation ranks.

**2. Projector derivatives.** At time zero,
\[
 P_1(0)=\operatorname{diag}(1,0,0),\qquad
 P_2(0)=\operatorname{diag}(1,1,0).
\]
The factor equation yields the first derivatives
\[
 \dot P_1(0)=
 \begin{pmatrix}
 0&q_{12}/a&q_{13}/a\\
 q_{12}/a&0&0\\
 q_{13}/a&0&0
 \end{pmatrix},\qquad
 \dot P_2(0)=
 \begin{pmatrix}
 0&0&q_{13}/a\\
 0&0&q_{23}/b\\
 q_{13}/a&q_{23}/b&0
 \end{pmatrix}.
\]
For either rank, differentiation of the projected Lyapunov equation gives
\[
 \ddot Y=\dot P Q+Q\dot P-\dot P QP-PQ\dot P.
\]

**3. A negative direction at every sufficiently small positive time.** Put \(D(t)=Y_2(t)-Y_1(t)\). Direct substitution in the previous identities yields
\[
 D(0)=\operatorname{diag}(0,b,0),\qquad
 \dot D(0)=
 \begin{pmatrix}0&0&0\\0&q_{22}&q_{23}\\0&q_{23}&0\end{pmatrix},
\]
and the second-order coefficients
\[
 [t^2]D_{11}(t)=0,\qquad
 [t^2]D_{13}(t)=-\frac{q_{12}q_{23}}{2a},\qquad
 [t^2]D_{33}(t)=\frac{q_{23}^{2}}{b}.
\]
Here \([t^2]\) means the coefficient of \(t^2\) in the Taylor expansion. For the fixed vector
\[
 z=e_1+\frac{bq_{12}}{2aq_{23}}e_3
\]
the zeroth-order and first-order quadratic forms vanish, while the quadratic term is
\[
 z^{\mathsf T}D(t)z=-\frac{bq_{12}^{2}}{4a^{2}}t^2+O(t^3)<0
\]
for all sufficiently small \(t>0\). In contrast, \(e_2^{\mathsf T}D(t)e_2=b+O(t)>0\). Therefore \(D(t)\) is indefinite for every sufficiently small positive time, even though \(0\preceq Y_r(t)\preceq\Sigma(t)\) for each rank.

**4. Example and minimal dimension.** Taking \(a=3\), \(b=2\), \(c=1\), and \(Q=\boldsymbol{1}\boldsymbol{1}^{\mathsf T}\) gives \(z=e_1+e_3/3\) and the stated \(-t^2/18+O(t^3)\). In ambient dimension two, the rank-two tangent projector is the identity, so \(Y_2(t)=\Sigma(t)\), and the comparison in step 1 forces \(Y_2(t)\succeq Y_1(t)\). Consequently three dimensions are minimal.

## Verification
The accompanying standalone \(\texttt{verify_rank_order.py}\) recomputes all listed Taylor coefficients using symbolic matrix algebra and numerically integrates the two projected flows using independent ODE solves at several positive times. Execution with Python, NumPy, SciPy and SymPy gave **11 symbolic identities and 54 numerical assertions passed**. The negative quadratic coefficient and universal sufficiently-small-time conclusion follow analytically from the displayed identities; finite numerical tests do not substitute for that argument.

## Relationship to prior work
Schmidt, Hennig, Nick and Tronarp (2023) develop rank-reduced Kalman filtering in a dynamical-low-rank framework and derive tangent-projected covariance Lyapunov dynamics. Ceruti and Lubich (2020) provide a general dynamical-low-rank projection and integration framework. Their constructions are antecedents rather than new claims here. The present finding compares **two exact tangent-projected trajectories of different fixed ranks initialized by nested spectral truncations**, and shows a sharp obstruction to transferring a covariance-order intuition from the full Lyapunov solution to comparisons between these ranks. Neither discretization error nor low-rank observation updates are implicated by this theorem.

## Limitations
The result is for exact continuous projected flows with zero drift, positive-semidefinite constant process noise, diagonal simple-spectrum positive initial covariance, ranks one and two in dimension three, and sufficiently short times. It does not claim that the finite-step BUG integrator of Schmidt and coauthors has the same sign behavior, nor that larger-rank approximations are worse in Frobenius or spectral norms, nor that higher rank is generally undesirable. General drift and filtering observation updates are unanalysed. Some algebraic components are standard projection geometry; independent publication-priority verification remains outstanding.

## References
1. J. Schmidt, P. Hennig, J. Nick, and F. Tronarp, *The Rank-Reduced Kalman Filter: Approximate Dynamical-Low-Rank Filtering In High Dimensions*, arXiv:2306.07774 (first posted 2023-06-13). https://arxiv.org/abs/2306.07774
2. G. Ceruti and C. Lubich, *An unconventional robust integrator for dynamical low-rank approximation*, arXiv:2010.02022 (2020). https://arxiv.org/abs/2010.02022
3. F. Carrel, M. J. Gander, and B. Vandereycken, *Low-rank Parareal: a low-rank parallel-in-time integrator*, BIT Numerical Mathematics (2023). https://doi.org/10.1007/s10543-023-00984-4
