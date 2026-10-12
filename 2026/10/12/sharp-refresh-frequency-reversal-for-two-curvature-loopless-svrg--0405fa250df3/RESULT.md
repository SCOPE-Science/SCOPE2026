# Sharp refresh-frequency reversal for two-curvature loopless SVRG

## Finding

Consider the original loopless stochastic variance-reduced gradient method on two equally weighted scalar strongly convex quadratic components of curvatures \(\mu(1-v)\) and \(\mu(1+v)\), with \(\mu>0\) and \(0<v<1\). At each iteration, choose the component independently and uniformly, take a constant gradient step \(\eta>0\), and independently reset the reference point to the **pre-step** iterate with probability \(p\in(0,1]\). Start from any nonzero common initial iterate and reference point.

Put \(h=\eta\mu\) and
\[
Q(h,p,v)=(p-1-2v^2)h^2+(2-3p)h+2p.
\]
The iterates converge geometrically in mean square to the minimizer exactly when
\[
0<h<h_*(p,v),\qquad
h_*(p,v)=\frac{2-3p+\sqrt{(2-3p)^2+8p(1+2v^2-p)}}{2(1+2v^2-p)}.
\]
At equality the expected squared iterate fails to approach zero, and above it diverges along a subsequence. The threshold is strictly below \(2\).

The dependence on the snapshot-refresh probability reverses sharply at a curvature-contrast ratio:
\[
\begin{array}{ll}
0<v^2<1/2 &: \quad h_*(p,v)\text{ strictly decreases with }p,\\
v^2=1/2 &: \quad h_*(p,v)=1\text{ for every }p,\\
1/2<v^2<1 &: \quad h_*(p,v)\text{ strictly increases with }p.
\end{array}
\]
Thus **refreshing the reference more often can destroy mean-square stability**, despite preserving the unbiased gradient estimator. For the exact rational choice \(v=1/2\), \(h=5/4\), refresh probability \(p=1/4\) gives geometric mean-square convergence, whereas \(p=1\) gives exponential mean-square growth.

## Assumptions and scope

Let \(f_{\pm}(x)=\mu(1\pm v)x^2/2\), \(f=(f_++f_-)/2=\mu x^2/2\), and \(x^*=0\). The sampling signs \(\sigma_k\) are independent and uniform on \(\{-1,+1\}\); the refresh indicators are independent Bernoulli variables of parameter \(p\), independent of the signs and of previous iterations. The precise algorithm is
\[
\begin{aligned}
g_k&=f'_{\sigma_k}(x_k)-f'_{\sigma_k}(w_k)+f'(w_k),\\
x_{k+1}&=x_k-\eta g_k,\\
w_{k+1}&=\begin{cases}x_k,&\text{with probability }p,\\w_k,&\text{otherwise.}\end{cases}
\end{aligned}
\]
The choice \(w_{k+1}=x_k\), rather than \(x_{k+1}\), is essential. The theorem concerns exact-arithmetic mean-square convergence of \(\mathbb E[x_k^2]\) from \(x_0=w_0\ne0\), and also supplies a strict second-moment contraction certificate for arbitrary square-integrable initial states in the stable region. No inter-iteration dependence, minibatches, noncommuting Hessians, or nonlinear objectives are included.

## Proof

**1. Exact stochastic moment map.** Set \(r=1-h\). Since
\[
g_k=\mu x_k+\mu v\sigma_k(x_k-w_k),
\]
the state \(z_k=(x_k,w_k)^\top\) is propagated by one of the two matrices
\[
B_{\sigma,1}=\begin{pmatrix}r-hv\sigma&hv\sigma\\1&0\end{pmatrix},\qquad
B_{\sigma,0}=\begin{pmatrix}r-hv\sigma&hv\sigma\\0&1\end{pmatrix}.
\]
Define the positive linear map on real symmetric \(2\)-by-\(2\) matrices
\[
\mathcal T(C)=\tfrac12\sum_{\sigma=\pm1}\left[pB_{\sigma,1}CB_{\sigma,1}^{\top}+(1-p)B_{\sigma,0}CB_{\sigma,0}^{\top}\right].
\]
Then \(C_k=\mathbb E[z_kz_k^\top]\) satisfies \(C_{k+1}=\mathcal T(C_k)\) exactly, and \(\mathcal T\) preserves the positive-semidefinite order.

**2. An exact matrix supersolution/subsolution.** Restrict temporarily to \(0<h<2\), and write
\[
 d=p+(1-p)h,\qquad y=\frac{p(1-h)}{d},\qquad
 P=\begin{pmatrix}1&y\\y&1\end{pmatrix},\qquad
 E=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
Because \(|1-h|<1\) and \(d\ge p>0\), we have \(|y|<1\), hence \(P\) is positive definite. Directly averaging the four matrices gives
\[
\mathcal T(P)_{22}=1,\qquad
\mathcal T(P)_{12}=r[p+(1-p)y]=y,
\]
and, using \(1-y=h/d\),
\[
\mathcal T(P)_{11}=r^2+2h^2v^2(1-y)
=1-\frac{hQ(h,p,v)}{d}.
\]
Consequently,
\[
\boxed{\mathcal T(P)=P-\frac{hQ(h,p,v)}d E.}
\]
Moreover
\[
K:=E+\mathcal T(E)
=\begin{pmatrix}1+r^2+h^2v^2&pr\\pr&p\end{pmatrix},
\quad
\det K=p\left[1+h^2v^2+(1-p)r^2\right]>0.
\]
Since the leading diagonal entry of \(K\) is positive, \(K\) is positive definite. A second application of \(\mathcal T\) therefore yields the decisive identity
\[
\boxed{\mathcal T^2(P)=P-\frac{hQ(h,p,v)}d K.}
\]

**3. Sharp classification.** The polynomial \(Q\) is a strictly concave quadratic in \(h\), with \(Q(0,p,v)=2p>0\) and \(Q(2,p,v)=-8v^2<0\). It has exactly one positive root \(h_*\in(0,2)\), given by the formula in the finding. If \(0<h<h_*\), then \(\mathcal T^2(P)\prec P\). Since \(P\) and \(K\) are positive definite, there is \(\varepsilon>0\) such that \(0\preceq\mathcal T^2(P)\preceq(1-\varepsilon)P\). Any initial positive-semidefinite second-moment matrix is bounded above by a scalar multiple of \(P\). Iterating positivity proves geometric decay of both even and odd second moments, hence mean-square convergence.

If \(h_*<h<2\), then \(\mathcal T^2(P)\succeq(1+\varepsilon)P\) for some \(\varepsilon>0\). If \(h=h_*\), then \(\mathcal T(P)=P\). To transfer these conclusions from the auxiliary positive-definite \(P\) to the required initialization, scale \(x_0=w_0=1\) without loss of generality. The first iterate is \(x_1=r\) and \(w_1=1\). The next has
\[
x_2=r^2+h^2v\sigma_1,\qquad
w_2=\begin{cases}r,&\text{with probability }p,\\1,&\text{otherwise,}\end{cases}
\]
where the displayed random choices are independent. Thus \(C_2=\mathbb E[z_2z_2^\top]\) is positive definite: conditional on \(w_2\), \(x_2\) has strictly positive variance, and \(w_2\) is not identically zero. The sole exceptional case is \(p=h=1\), for which \(w_2=0\) but \(C_3=\operatorname{diag}(v^4,v^2)\succ0\). Accordingly, for some finite \(j\le3\) and \(c>0\), \(C_j\succeq cP\). Positivity of \(\mathcal T\) implies \(C_{j+2m}\succeq c(1+\varepsilon)^mP\) above the threshold, and \(C_{j+m}\succeq cP\) at the threshold. The first coordinate therefore grows geometrically along a subsequence or fails to decay, respectively. At \(h=2\) and \(0<p<1\), the same construction has \(y=-p/(2-p)\), so \(P\succ0\) and \(Q=-8v^2<0\): the geometric-growth comparison still applies. At the endpoint \(p=1,h=2\), \(P\) becomes positive semidefinite, but the exact identity remains true, and \(K\succ0\) still implies \(\mathcal T^2(P)\succeq(1+\varepsilon)P\) for some \(\varepsilon>0\). The already established \(C_2\succ0\) dominates a positive multiple of this nonzero \(P\), so the first moment component again grows on even subsequences. Finally, for \(h>2\), unbiasedness gives \(\mathbb E[x_k]=r^kx_0\), and hence \(\mathbb E[x_k^2]\ge r^{2k}x_0^2\) grows exponentially. This completes the claimed sharp divergence classification, including the endpoint \(h=2\).

**4. Refresh-probability phase reversal.** At the unique positive root, \(\partial_hQ<0\). Also
\[
\partial_pQ=(h-1)(h-2),\qquad Q(1,p,v)=1-2v^2.
\]
Implicit differentiation gives \(\operatorname{sign}(\partial_p h_*)=\operatorname{sign}[(h_*-1)(h_*-2)]\). If \(v^2<1/2\), the root exceeds \(1\) and the sign is negative; if \(v^2>1/2\), the root is below \(1\) and the sign is positive. When \(v^2=1/2\), the unique positive root is \(1\) for every \(p\). For the rational witness, direct substitution gives
\[
Q(5/4,1/4,1/2)=7/64>0,
\qquad Q(5/4,1,1/2)=-1/32<0.
\]
All claims follow.

## Verification

The standalone standard-library program `verify.py` exactly enumerates the sampled-sign and refresh branches using rational arithmetic. It independently reconstructs \(\mathcal T\), checks both displayed matrix identities, tests the positive-definiteness certificates and reachable covariance, checks the earlier fixed-probability specialization, and verifies the exact rational witness. Running `python3 verify.py` completed \(1{,}710\) distinct rational-parameter cases plus witness checks. The analytic matrix-order proof, not those finite tests, establishes the infinite-time theorem.

## Relationship to prior work

Kovalev, Horváth, and Richtárik introduced the original loopless SVRG update with an independently sampled refresh indicator and pre-step snapshot assignment; their convergence theorem provides a sufficient small-step bound, not this sharp threshold or the change in its dependence on refresh probability. Qian, Qu, and Richtárik developed arbitrary-sampling L-SVRG and an expected-smoothness Lyapunov analysis, again with sufficient step restrictions. Sebbouh and coauthors studied practical variance-reduced methods and a decreasing-step loopless variant; that variant changes the step after refresh and does not imply the constant-step frontier here.

The exact \(p=1/2\) specialization of the scalar two-component stability frontier has already been determined separately. It is **not** claimed as novel here. The substantive additional statement is the sharp all-\(p\) threshold together with its unexpected, strict curvature-dependent reversal and a fixed-step convergence-versus-divergence witness. Prior work guaranteeing convergence at sufficiently conservative step sizes does not imply that reversal.

## Limitations

The theorem concerns one scalar interpolation family with two distinct positive component curvatures, uniform independent component sampling, independent Bernoulli refresh, and the original pre-step reference assignment. The phase reversal applies to the *maximum mean-square stable step*, not necessarily to convergence rates at a common small step or to optimal computational cost per gradient evaluation. It does not establish the same phase diagram for vector-valued noncommuting quadratics, nonquadratic losses, nonuniform sample probabilities, or alternative post-step snapshot refresh. Search-based priority assessment cannot exclude a mathematically equivalent unpublished or unindexed derivation.

## References

1. D. Kovalev, S. Horváth, and P. Richtárik, “Don’t Jump Through Hoops and Remove Those Loops: SVRG and Katyusha are Better Without the Outer Loop,” arXiv:1901.08689v1, first publicly available 2019-01-24; algorithm and convergence analysis in Section 3. https://arxiv.org/abs/1901.08689
2. X. Qian, Z. Qu, and P. Richtárik, “L-SVRG and L-Katyusha with Arbitrary Sampling,” arXiv:1906.01481v1, 2019; Algorithm 1 and Theorem 3.1. https://arxiv.org/abs/1906.01481
3. O. Sebbouh, N. Gazagnadou, S. Jelassi, F. Bach, and R. M. Gower, “Towards closing the gap between the theory and practice of SVRG,” arXiv:1908.02725v1, 2019; Section 5 on the varying-step loopless variant. https://arxiv.org/abs/1908.02725
