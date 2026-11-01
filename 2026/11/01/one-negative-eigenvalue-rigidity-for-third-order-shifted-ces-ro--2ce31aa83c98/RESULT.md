# One-negative-eigenvalue rigidity for third-order shifted Cesàro self-commutators

## Finding
For each real \(-1<\alpha<0\), the compact self-adjoint operator
\[
S_{\alpha}=M_{\alpha,3}^{*}M_{\alpha,3}-M_{\alpha,3}M_{\alpha,3}^{*}
\]
has exactly one strictly negative eigenvalue, counted with multiplicity. For \(\alpha\ge0\), this operator is nonnegative. Thus the negative spectral index is exactly one throughout the nonhyponormal regime at order three, the first order with two nominally negative terms in the published finite-rank defect.

## Assumptions and scope
On complex \(\ell^{2}(\mathbb N_{0})\), define the bounded third-order generalized Cesàro matrix
\[
(M_{\alpha,3})_{nj}=\begin{cases}
\dfrac{3(n-j+1)(n-j+2)}{(n+\alpha+1)(n+\alpha+2)(n+\alpha+3)},&0\le j\le n,\\
0,&j>n,
\end{cases}
\qquad \alpha>-1.
\]
The negative index of a self-adjoint operator is the total multiplicity of its strictly negative spectrum. Here the self-commutator is compact, as shown below. No claim is made about the magnitude of its negative eigenvalue or higher orders.

## Proof
Put \(t=n+\alpha\) and
\[
D(t)=(t+4)(t+5)(t+6),\quad H(t)=(t+1)(t+2)(t+3),\quad r_n=1-H(t)/D(t),\quad R=\operatorname{diag}(r_n).
\]
Every \(r_n>0\). The bounded operator \(B\) and third-order specialization of Ma's defect identity [1, Theorem 2.3] give
\[
BM_{\alpha,3}=M_{\alpha,3}^{*},\quad
S_{\alpha}=M_{\alpha,3}^{*}QM_{\alpha,3},\quad
Q=R+\sum_{j=0}^{2}\lambda_jv_jv_j^{*},
\]
where \(v_j(n)=p_j(n;\alpha)/D(n+\alpha)\), and
\[
\begin{aligned}
p_0(n;\alpha)&=(t+1)(t+2)+4(1-\alpha)(t+1)+\tfrac{10}{3}(1-\alpha)(2-\alpha),\\
p_1(n;\alpha)&=t+1+\tfrac54(2-\alpha),\\
p_2(n;\alpha)&=1,\\
\lambda_0&=9\alpha,\quad \lambda_1=48\alpha(\alpha^2-1),\quad
\lambda_2=5\alpha(\alpha^2-1)(\alpha^2-4).
\end{aligned}
\]
For \(-1<\alpha<0\), the signs are \(\lambda_0<0\), \(\lambda_1>0\), \(\lambda_2<0\). Although two terms are negative, the last one is uniformly absorbed by \(R\): for \(t=n+\alpha\ge n-1\),
\[
D(t)\ge(n+3)(n+4)(n+5),\qquad
D(t)-H(t)=9t^2+63t+114\ge60.
\]
The second polynomial increases for \(t\ge-1\). Consequently the weighted quadratic-form norm of \(v_2\) satisfies
\[
\sum_{n=0}^{\infty}\frac{|v_2(n)|^2}{r_n}
=\sum_{n=0}^{\infty}\frac1{D(n+\alpha)[D(n+\alpha)-H(n+\alpha)]}
\le\frac1{60}\sum_{n=0}^{\infty}\frac1{(n+3)(n+4)(n+5)}
=\frac1{1440}.
\]
The telescoping sum is \(1/24\), and \(|\lambda_2|=5|\alpha|(1-\alpha^2)(4-\alpha^2)\le20\). By weighted Cauchy–Schwarz, for every \(x\in\ell^2\),
\[
|\lambda_2|\,|\langle v_2,x\rangle|^2\le\frac1{72}\langle Rx,x\rangle.
\]
Thus
\[
\langle Qx,x\rangle\ge\frac{71}{72}\langle Rx,x\rangle+\lambda_0|\langle v_0,x\rangle|^2.
\]
On the codimension-one subspace orthogonal to \(v_0\) this is nonnegative. Hence the negative index of \(Q\), and therefore of \(S_{\alpha}=M^*QM\), is at most one.

For existence of a negative direction, write \(u_N=\sum_{n=0}^{N}e_n\). From the displayed explicit formulas, as \(n\to\infty\),
\[
r_n=9/n+O(n^{-2}),\quad v_0(n)=1/n+O(n^{-2}),\quad
v_1(n)=O(n^{-2}),\quad v_2(n)=O(n^{-3}).
\]
It follows directly that
\[
\langle Qu_N,u_N\rangle
=9\alpha(\log N)^2+O(\log N)<0
\]
for sufficiently large \(N\), because \(\alpha<0\). The range of \(M_{\alpha,3}\) is dense: Ma's finite-support right inverse satisfies \(M_{\alpha,3}L e_j=e_j\) for each \(j\) [1, equation (2.2)]. Density therefore transfers a strictly negative quadratic-form direction from \(Q\) to \(S_{\alpha}\). Its negative index is at least one, hence exactly one.

Finally \(r_n\to0\) and each \(v_jv_j^*\) has rank one; therefore \(Q\) and \(S_{\alpha}\) are compact. A negative direction of a compact self-adjoint operator yields a negative eigenvalue, and the index-one bound makes its multiplicity one. Nonnegativity for \(\alpha\ge0\) is Ma's independently established theorem [1, Theorem 1.1].

## Verification
The auxiliary standalone script `verify.py` checks all 49 entries of a seven-column finite Gram defect against the exact rational specialization at \(\alpha=-1/2\); it also checks a finite negative direction and a finite weighted domination bound. These tests confirm algebraic normalization, not the infinite-dimensional spectral assertion. The proof uses the infinite telescoping estimate and the diverging logarithmic negative witness, not finite truncation.

## Relationship to prior work
Ma [1] determines the hyponormality threshold and supplies the all-orders defect decomposition, but does not determine the exact number of negative eigenvalues below the threshold. Rhaly [2] studies third-order supraposinormality and hyponormality. The present result classifies the negative **inertia**, not merely existence of a negative direction. Previous results determining the trace or sharp weighted lower coefficient of generalized Cesàro self-commutators likewise do not specify this index. This theorem is deliberately restricted to order three, the first case where two negative signed rank-one components must be reconciled.

## Limitations
The finite-rank defect identity and range-density lemma are sourced from [1] and verified in a finite rational instance; their full infinite proof belongs to that reference. The prior third-order supraposinormality article [2] was accessible by abstract, not by full text; earlier implicit coverage remains a publication-priority risk. The result does not quantify the unique eigenvalue, its asymptotics as the shift tends to zero, or the negative inertia at orders four and above. Independent mathematical validation has not been performed.

## References
[1] Yicen Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1, first submitted 2026-09-18, especially Theorems 1.1 and 2.3 and equations (2.2), (2.13), (2.18).

[2] H. C. Rhaly Jr., *The generalized Cesàro matrices of order three are supraposinormal on* \(\ell^2\), arXiv:1903.07896, 2019 (abstract inspected; full text unavailable during this review).
