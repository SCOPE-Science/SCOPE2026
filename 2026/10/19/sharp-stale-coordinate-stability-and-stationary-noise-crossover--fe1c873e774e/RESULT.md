# Sharp stale-coordinate stability and stationary-noise crossover in randomized two-variable relaxation

## Finding

For the normalized two-variable SPD system specified below, update one uniformly selected coordinate at each step, reading its current value and reading the other coordinate one global update late. The noiseless iteration converges in mean square from every deterministic initial history if and only if
\[
0<\beta<\beta_{\mathrm{crit}}(r)=\frac{4}{1+\sqrt{1+4r^2}}.
\]
In this interval, centered scalar update noise of variance \(\sigma^2>0\), independent across updates and independent of the entire coordinate-selection sequence, yields a limiting mean squared error in each coordinate of
\[
V_{\mathrm{stale}}=\frac{\sigma^2(2-\beta r^2)}{\beta(1-r^2)(4-2\beta-\beta^2r^2)}.
\]
With the same update rule and noise law but a current remote read, it is
\[
V_{\mathrm{fresh}}=\frac{\sigma^2}{\beta(2-\beta)(1-r^2)}.
\]
In the common stability interval the exact difference is
\[
V_{\mathrm{stale}}-V_{\mathrm{fresh}}=
\frac{2\sigma^2 r^2(\beta-1)}{(2-\beta)(1-r^2)(4-2\beta-\beta^2r^2)}.
\]
Thus stale reads reduce the stationary noise floor for \(0<\beta<1\), leave it unchanged at \(\beta=1\), and increase it for \(1<\beta<\beta_{\mathrm{crit}}(r)\). This comparison does not concern convergence speed.

## Assumptions and scope

Let \(0<r<1\), \(A=\begin{pmatrix}1&r\\r&1\end{pmatrix}\), and \(\beta>0\). Start from any fixed finite deterministic error history \((e_{-1},e_0)\) with \(e_k\in\mathbb R^2\). The coordinate choices \((I_k)_{k\ge0}\) are independent and fair on \(\{1,2\}\). The scalar noises \((\xi_k)_{k\ge0}\) are mutually independent and are independent of the entire sequence \((I_k)_{k\ge0}\); \(\mathbb E\xi_k=0\) and \(\mathbb E\xi_k^2=\sigma^2\) at each step. No Gaussian assumption is made.

For \(I_k=1\), set
\[
e_{k+1,1}=(1-\beta)e_{k,1}-\beta r e_{k-1,2}+\xi_k,\qquad e_{k+1,2}=e_{k,2}.
\]
For \(I_k=2\), interchange the coordinate labels. The fresh comparator replaces the delayed remote value by its current value. Mean-square stability refers to \(\mathbb E\|e_k\|^2\to0\) when \(\sigma^2=0\), for every deterministic history. The noise-floor claims concern \(\sigma^2>0\).

The independence from the selection sequence matters. For example, take \(\beta=1\), \(r=1/2\), and noises equal to \(+\sigma\) on selection of coordinate 1 and \(-\sigma\) on selection of coordinate 2. These noises are mutually independent and marginally centered, but dependent on the selections. The history \(e_{-1}=e_0=(2\sigma,-2\sigma)^\top\) stays fixed for either rule: its residual is \((\sigma,-\sigma)^\top\), exactly canceled by the selected noise. The squared error in either coordinate is then \(4\sigma^2\), not the \(4\sigma^2/3\) predicted by the independent-noise formulas.

## Proof

**Augmented second moments.** Put \(z_k=(e_{k,1},e_{k,2},e_{k-1,1},e_{k-1,2})^\top\). The update is \(z_{k+1}=T_{I_k}z_k+\xi_k v_{I_k}\), where
\[
T_1=\begin{pmatrix}1-\beta&0&0&-\beta r\\0&1&0&0\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
T_2=\begin{pmatrix}1&0&0&0\\0&1-\beta&-\beta r&0\\1&0&0&0\\0&1&0&0\end{pmatrix},
\]
and \(v_1,v_2\) are the first two standard unit vectors in \(\mathbb R^4\). The independence hypotheses make \(I_k\) independent of \(z_k\) and give a centered noise with variance \(\sigma^2\) even conditional on \((z_k,I_k)\). Hence \(X_k=\mathbb E[z_k z_k^\top]\) satisfies
\[
X_{k+1}=\mathcal L(X_k)+Q,\qquad
\mathcal L(X)=\tfrac12(T_1XT_1^\top+T_2XT_2^\top),\qquad
Q=\tfrac{\sigma^2}{2}\operatorname{diag}(1,1,0,0).
\]

**Stationary balance.** The map and forcing are invariant under simultaneous exchange of the two coordinate labels at both times. At stationarity the current and previous diagonal blocks coincide, so any swap-invariant stationary matrix has the form
\[
X=\begin{pmatrix}a&b&c&d\\b&a&d&c\\c&d&a&b\\d&c&b&a\end{pmatrix}.
\]
Entrywise balance gives
\[
\begin{aligned}
a&=\tfrac12[1+(1-\beta)^2+\beta^2r^2]a-\beta r(1-\beta)d+\tfrac12\sigma^2,\\
b&=(1-\beta)b-\beta rc,\\
c&=(1-\beta/2)a-\beta rd/2,\\
d&=(1-\beta/2)b-\beta rc/2.
\end{aligned}
\]
Thus \(b=d=-rc\). The two remaining equations are
\[
\beta[2-\beta(1+r^2)]a-2\beta r^2(1-\beta)c=\sigma^2,\qquad
-(2-\beta)a+(2-\beta r^2)c=0.
\]
Their determinant is \(D=\beta(1-r^2)(4-2\beta-\beta^2r^2)\). With \(u=2-\beta r^2\), \(v=2-\beta\), and \(D\ne0\), the unique swap-invariant stationary matrix is
\[
X_*=\frac{\sigma^2}{D}
\begin{pmatrix}
u&-rv&v&-rv\\-rv&u&-rv&v\\v&-rv&u&-rv\\-rv&v&-rv&u
\end{pmatrix}.
\]
At the positive root \(\beta=\beta_{\mathrm{crit}}<2\), elimination of \(c\) instead gives \(0=\sigma^2u\); this is impossible for \(\sigma^2>0\) because \(u>0\).

**Exact stability.** The eigenvalues of \(DX_*/\sigma^2\), obtained by taking symmetric and antisymmetric combinations across times and coordinate labels, are
\[
\beta(1-r^2),\quad \beta(1-r^2),\quad
(1-r)[4-\beta(1-r)],\quad (1+r)[4-\beta(1+r)].
\]
Within the claimed interval, \(D>0\) and all four eigenvalues are positive. Choose \(\sigma^2>0\) to use \(X_*\succ0\) as a comparison matrix even in the homogeneous problem. Then \(X_*-\mathcal L^2(X_*)=Q+\mathcal L(Q)\succ0\). Indeed the positive semidefinite first term forces a vector in the kernel of the sum to have zero current block, and the lower diagonal block of \(\mathcal L(Q)\) is \(\sigma^2 I_2/2\), forcing the previous block to vanish as well. Hence \(\mathcal L^2(X_*)\preceq\gamma X_*\) for some \(0\le\gamma<1\). Positivity of \(\mathcal L\) and domination of any symmetric matrix between two scalar multiples of \(\pm X_*\) give geometric decay of homogeneous second moments and convergence of forced second moments to \(X_*\).

Conversely, if mean-square stability holds for every deterministic history then \(\mathcal L^k(zz^\top)\to0\) for every \(z\in\mathbb R^4\): both time blocks tend to zero in second moment. Rank-one symmetric matrices span the symmetric-matrix space, so \(\mathcal L\) has spectral radius less than one there. For any \(\sigma^2>0\) this would give a positive semidefinite stationary matrix \(\sum_{j\ge0}\mathcal L^j(Q)\); averaging under the label swap keeps it stationary and positive semidefinite. At the threshold there is no swap-invariant stationary solution, as shown above. Beyond it, the two temporally antisymmetric eigenvalues of the unique swap-invariant solution equal \(\sigma^2/(4-2\beta-\beta^2r^2)<0\), also impossible. This proves necessity, and the stationary diagonal of \(X_*\) gives \(V_{\mathrm{stale}}\).

**Fresh reads.** The selected noiseless step is \(e\mapsto e-\beta(Ae)_i e_i^{\mathrm{unit}}\). Since \(A_{ii}=1\), it decreases \(e^\top A e\) by \(\beta(2-\beta)[(Ae)_i]^2\). The expected decrease bounds a positive multiple of \(e^\top A e\) for \(0<\beta<2\), since \(A\) is SPD. The corresponding second-moment map is therefore stable. The stationary second-moment matrix is swap-invariant with diagonal \(a\) and off-diagonal \(b\). The off-diagonal balance gives \(b=-ra\); the diagonal balance reduces to \(\beta(2-\beta)(1-r^2)a=\sigma^2\). This gives the stated \(V_{\mathrm{fresh}}\). Subtraction and positivity of the common denominator prove the crossover; \(V_{\mathrm{stale}}\) diverges as \(\beta\) approaches \(\beta_{\mathrm{crit}}\) from below.

## Verification

The included standard-library script `artifacts/verify_asynchronous.py` checks finite rational instances of the two Lyapunov identities, covariance eigenvalue identities, two-update forcing positivity and the formula for the variance difference. It checks algebra for the stated covariance operator; it does not establish the noise assumptions or the general frontier. The universal argument is the balance and positive-cone proof above.

## Relationship to prior work and limitations

Carson and Ma give a sufficient convergence-rate condition for a general asynchronous model with locally current and remotely delayed reads. The exact delay-distribution law in Resultary record `9ae0040f2dac` already includes the noiseless \(\beta=1\), fixed-one-step-delay overlap through its exact overwrites; it does not address variable relaxation or the noise comparison. Earlier work of Beidas and Papavassilopoulos, Verkama, and Moga and Dubois treats random delays or relaxation; a complete historical full-text comparison is not established here. The distinct claims concern the exact stability interval for this constant-relaxation model and the stationary crossover under independent update noise.

The calculation is for two normalized SPD variables with fair independent single-coordinate selection and a one-step delay on only the remote read. It does not cover correlated selection and noise, arbitrary delay distributions, simultaneous updates, higher dimensions, or guarantees on transient convergence speed or cost.

## References

1. E. Carson and Y. Ma, *Asynchronous Jacobi and randomized Gauss–Seidel methods in shared and distributed memory: A unified convergence-rate analysis*, arXiv:2609.15605v1, §4.1. https://arxiv.org/html/2609.15605v1
2. *Exact delay-distribution law for two-coordinate randomized Gauss-Seidel*, Resultary `9ae0040f2dac`. https://github.com/Resultary/2026/blob/main/2026/9/20/SCOPE-exact-stochastic-delay-law-randomized-gauss-seidel--9ae0040f2dac/RESULT.md
3. B. F. Beidas and G. P. Papavassilopoulos, *Convergence analysis of asynchronous linear iterations with stochastic delays*, Parallel Computing 19 (1993), 281–302. https://doi.org/10.1016/0167-8191(93)90038-M
4. M. Verkama, *Random Relaxation of Fixed-Point Iteration*, SIAM J. Sci. Comput. 17 (1996), 906–912. https://doi.org/10.1137/0917058
5. A. C. Moga and M. Dubois, *Performance of Asynchronous Linear Iterations with Random Delays*, USC technical report CENG 95-06 (1995). https://ceng.usc.edu/techreports/1995/Dubois%20CENG%2095-06.pdf
