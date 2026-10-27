# Sharp stationary-barycenter envelope for Lipschitz Markov heat on weighted paths

## Finding

Fix an integer \(n\ge3\), strictly increasing positions \(x_0<\cdots<x_{n-1}\), and a probability vector \(\pi\) with \(\pi_i>0\). Let
\[
L_k=\sum_{j=0}^{k}\pi_j,\qquad R_k=\sum_{j=k+1}^{n-1}\pi_j,
\]
\[
a_k=\frac{\sum_{j=0}^{k}\pi_j x_j}{L_k},\qquad
b_k=\frac{\sum_{j=k+1}^{n-1}\pi_j x_j}{R_k},\qquad
C(\pi,x)=\max_{0\le k\le n-2}\frac{b_k-a_k}{x_{k+1}-x_k}.
\]
Let \(Q(c)\) be the reversible birth--death generator with positive edge conductances \(c_0,\dots,c_{n-2}\):
\[
Q(c)_{i,i+1}=c_i/\pi_i,\quad Q(c)_{i+1,i}=c_i/\pi_{i+1},\quad Q(c)_{i,i}=-\sum_{j\ne i}Q(c)_{i,j}.
\]
For \(H_t=e^{tQ(c)}\), acting on real functions modulo constants with seminorm
\[
\|f\|_{\mathrm{Lip}(x)}=\max_{0\le i\le n-2}\frac{|f(i+1)-f(i)|}{x_{i+1}-x_i},
\]
the exact sharp stationary-law-constrained envelope is
\[
\boxed{\sup_{c_i>0,\,t\ge0}\|H_t\|_{\mathrm{Lip}(x)\to\mathrm{Lip}(x)}=C(\pi,x).}
\]
The supremum is not attained with positive conductances at any finite time. For each cut \(k\) it is approached by holding the other conductances at \(1\), setting \(c_k=\varepsilon\), and taking \(t=\varepsilon^{-1/2}\) as \(\varepsilon\downarrow0\).

More generally, among **all** stochastically monotone Markov matrices \(K\) with invariant law \(\pi K=\pi\), the exact largest induced Lipschitz norm is \(C(\pi,x)\), attained by conditional averaging separately over the two sides of a maximizing cut. At every time, the single potential \(f(i)=x_i\) attains \(\|H_t\|\). When \(\pi\) is uniform and \(x_i=i\), the envelope equals \(n/2\).

## Assumptions and scope

The metric is \(d(i,j)=|x_i-x_j|\); in particular the metric edge lengths are \(x_{i+1}-x_i>0\) and need not agree with the conductances. A Markov matrix \(K\) is stochastically monotone when for every increasing real function \(f\), the function \(Kf\) is increasing. The operator seminorm is taken on real functions modulo constants; Markov matrices preserve constants. No normalization of the total conductance is imposed, because common conductance scaling may be absorbed into time. The invariant vector \(\pi\) is fixed while conductances vary.

## Proof

**1. Exact norming potential for an ordered kernel.** Write \(m_i=\sum_jK(i,j)x_j\) and \(\mu_i(j)=K(i,j)\). Stochastic monotonicity gives the first-order stochastic dominance \(\mu_i\preceq_{\mathrm{st}}\mu_{i+1}\). On an ordered finite real line, the transport identity is
\[
W_1(\mu_i,\mu_{i+1})=\sum_{h=0}^{n-2}(x_{h+1}-x_h)\left|\sum_{j\le h}(\mu_i(j)-\mu_{i+1}(j))\right|=m_{i+1}-m_i.
\]
For any real \(1\)-Lipschitz \(f\), duality (or summation by parts) bounds the adjacent difference \(|(Kf)(i+1)-(Kf)(i)|\) by this transport distance. The one potential \(f(j)=x_j\) attains all these differences simultaneously. Thus
\[
\|K\|_{\mathrm{Lip}(x)\to\mathrm{Lip}(x)}
=\max_i\frac{m_{i+1}-m_i}{x_{i+1}-x_i}.
\]

**2. Stationarity imposes a sharp barycenter bound.** Fix \(k\), set \(A=\{X_0>k\}\) and sample \(X_0\sim\pi\), \(X_1\mid X_0=i\sim K(i,\cdot)\). Let \(q=\mathbb P(A)=R_k\). By monotonicity of the row means,
\[
m_{k+1}-m_k\le\mathbb E[x_{X_1}\mid A]-\mathbb E[x_{X_1}\mid A^c].
\]
The law of \(X_1\) is \(\pi\). Since \(A\) has probability \(q=\sum_{j>k}\pi_j\), the elementary rearrangement inequality on a finite ordered support gives
\[
\mathbb E[x_{X_1}\mathbf1_A]\le\sum_{j>k}\pi_j x_j.
\]
Indeed, writing \(u_j=\mathbb P(A,X_1=j)\), one maximizes \(\sum_jx_ju_j\) over \(0\le u_j\le\pi_j\), \(\sum_ju_j=q\), by filling the largest \(x_j\) first. With \(\mu=\sum_j\pi_jx_j\), the difference of conditional expectations is
\[
\frac{\mathbb E[x_{X_1}\mathbf1_A]-q\mu}{q(1-q)}\le
\frac{\sum_{j>k}\pi_jx_j-q\mu}{q(1-q)}=b_k-a_k.
\]
Hence every monotone \(\pi\)-stationary \(K\) has norm at most \(C(\pi,x)\).

**3. Exact attainment in the larger Markov class.** For any \(k\), define \(K^{(k)}\) by assigning to every row \(i\le k\) the law \(\pi\) conditioned on \(\{0,\ldots,k\}\), and to every row \(i>k\) the law \(\pi\) conditioned on \(\{k+1,\ldots,n-1\}\). It is stationary, stochastically monotone and idempotent. Its row mean jumps from \(a_k\) to \(b_k\) only across edge \(k\), so its norm equals \((b_k-a_k)/(x_{k+1}-x_k)\). Choosing a maximizing cut establishes the Markov-kernel equality.

**4. Positivity and nonattainment for birth--death heat.** The generator has \(\pi Q(c)=0\). For the edge differences \(g_i=f(i+1)-f(i)\), the induced differential system has off-diagonal entries \(c_{i-1}/\pi_i\) and \(c_{i+1}/\pi_{i+1}\), all nonnegative, hence its matrix exponential preserves nonnegative differences. Thus \(H_t\) is stochastically monotone. For positive conductances and \(t>0\), every entry of \(H_t\) is strictly positive. Consequently the rearrangement step above is strictly suboptimal at each nontrivial cut: \(u_j>0\) also for \(j\le k\), whereas the maximizing allocation has \(u_j=0\) there. Therefore \(\|H_t\|<C(\pi,x)\) at all positive finite times. At \(t=0\), the norm equals \(1<C(\pi,x)\), since already \(b_0>x_1\) for \(n\ge3\).

**5. Singular sharpness.** Fix \(k\), take \(c_j=1\) for \(j\ne k\), \(c_k=\varepsilon\), and \(t_\varepsilon=\varepsilon^{-1/2}\). Let \(Q_0\) be the generator with the cut conductance deleted. The stochastic semigroups have supremum matrix norm \(1\), so the Duhamel identity gives
\[
\|e^{t_\varepsilon Q(c)}-e^{t_\varepsilon Q_0}\|_{\infty\to\infty}
\le t_\varepsilon\|Q(c)-Q_0\|_{\infty\to\infty}=O_{\pi}(\sqrt\varepsilon).
\]
Both blocks of \(Q_0\) are finite irreducible birth--death generators; therefore \(e^{t_\varepsilon Q_0}\to K^{(k)}\) as \(t_\varepsilon\to\infty\). The Lipschitz norm is continuous in finite matrix entries, so the original heat norm approaches the cut value. Maximize over \(k\) to conclude.

**6. Uniform-law and boundary consequences.** If \(\pi_i=1/n\) and \(x_i=i\), conditional means across any cut are \(a_k=k/2\) and \(b_k=(k+n)/2\), giving \(C=n/2\). Order preservation is essential: for uniform \(\pi\) on four equally spaced states, the stationary permutation with rows mapping \((0,1,2,3)\mapsto(0,3,1,2)\) has Lipschitz norm \(3\), whereas \(C=2\).

## Verification

Run `python check_stationary_barycentric.py` with Python, NumPy and SciPy. The checker uses exact rational arithmetic for \(1{,}105\) two-block cases, tests the uniform-law formula in dimensions \(3\) through \(29\), and tests the nonmonotone permutation boundary. It independently computes the one-dimensional transport formula and the mean-difference formula for \(720\) numerical birth--death semigroup instances. It also checks \(42\) slow-cut singular sequences. All executed tests passed. These finite tests are diagnostic, not substitutes for the preceding universal proof.

## Relationship to prior work

Ollivier's transport curvature framework and Veysseire's continuous-time contraction theorem describe Markov transport and curvature-controlled semigroup norms. Huillet's study discusses stochastic monotonicity and Siegmund duality for birth--death chains. Pflug and Schachermayer study Wasserstein ergodicity coefficients while optimizing metric-dependent coefficients for a given chain. These are relevant frameworks, but the results inspected do not state the sharp optimization over **all positive conductances with prescribed equilibrium weights and arbitrary path metric**, nor the stronger universal stationary-barycenter bound for order-preserving Markov kernels. The earlier three-state unit-edge special case is not claimed as new.

## Limitations

The stationary-mass formula concerns finite totally ordered spaces with the induced line metric and order-preserving kernels. An arbitrary nonmonotone stationary chain need not satisfy the bound. For the heat-semigroup equality, the generator must be an irreducible reversible nearest-neighbor path generator and conductances are optimized without positive lower bounds. The bound is a supremum, not attained at fixed positive conductances and finite time. No exact time profile for an arbitrary fixed conductance vector or infinite-state extension is asserted. An equivalent formulation in older unindexed literature, especially the not-fully-accessible Pflug--Schachermayer article, cannot be excluded.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first posted 2007-01-30.
2. L. Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420, first posted 2012-02-02.
3. T. E. Huillet, *Fluctuations Analysis of Finite Discrete Birth and Death Chains with Emphasis on Moran Models with Mutations*, International Scholarly Research Notices 2013, 939308, doi:10.1155/2013/939308.
4. G. Ch. Pflug and W. Schachermayer, *Coefficients of ergodicity for stochastically monotone Markov chains*, Journal of Applied Probability 29 (1992), 850--860, doi:10.2307/3214717 (abstract inspected; full text not accessible).
