# Gaussian-scale decoupling and residual anticorrelation in dihedral elephant walks

## Finding

Fix \(3/4<p<1\) and write \(q=2p-1\), so \(1/2<q<1\). Let the first generator be a fair choice between \(a\) and \(b\); thereafter select a past generator uniformly and repeat it with probability \(p\), or take the other generator with probability \(1-p\). Write \(Y_k=+1\) for \(a\) and \(Y_k=-1\) for \(b\), and set
\[
W_n=\sum_{k=1}^nY_k,\qquad S_n=\sum_{k=1}^n(-1)^{k-1}Y_k,\qquad
Z_n=q\sum_{k=1}^{n-1}(-1)^k\frac{W_k}{k},\quad Z_0=Z_1=0.
\]
The signed location on \(\mathbb Z_2*\mathbb Z_2\) is exactly \(S_n\). Define \(L_q=\lim_{n\to\infty}n^{-q}W_n\) and \(Z_\infty=\lim_{n\to\infty}Z_n\); both limits exist almost surely and in \(L^2\).

**Theorem (two-scale joint law and residual sign).** For every fixed \(T>0\),
\[
\left(\big(n^{-1/2}S_{\lfloor nt\rfloor},n^{-q}W_{\lfloor nt\rfloor}\big)_{0\le t\le T},\,Z_{\lfloor nT\rfloor}\right)
\Longrightarrow
\left(\big(B_t,t^qL_q\big)_{0\le t\le T},\,Z_\infty\right)
\]
in \(D([0,T],\mathbb R^2)\times\mathbb R\), with the usual Skorokhod \(J_1\) topology. Here \(B\) is standard Brownian motion **independent of the pair** \((L_q,Z_\infty)\). By contrast,
\[
\operatorname{Cov}(L_q,Z_\infty)<0,
\qquad \mathbb E L_q=0,
\qquad\operatorname{Var}(L_q)=\frac{2q}{(2q-1)\Gamma(1+2q)}.
\]
Thus the limiting Gaussian-scale location loses the dependence on the memory amplitudes even though those amplitudes remain strictly anticorrelated with one another.

## Assumptions and scope

The first label is symmetric, the two subsequent labels follow the common-global-history memory rule above, and \(p\) is fixed strictly between \(3/4\) and \(1\). The graph is the two-generator infinite dihedral Cayley graph with involutive generators, not a model that samples odd and even past steps separately. All limits concern \(n\to\infty\) and a fixed \(T>0\). The almost-sure limits \(L_q,Z_\infty\) live on the original probability space; \(B\) can be realized on an extension. The theorem asserts no independence between \(L_q\) and \(Z_\infty\); it proves the opposite sign of covariance.

## Proof

**1. Memory martingale and its scale.** Conditional on \(\mathcal F_n=\sigma(Y_1,\ldots,Y_n)\),
\[
\mathbb E[Y_{n+1}\mid\mathcal F_n]=q\frac{W_n}{n},\qquad
\mathbb E[W_{n+1}\mid\mathcal F_n]=\left(1+\frac qn\right)W_n.
\]
Set \(A_1=1\) and \(A_n=\prod_{j=1}^{n-1}(1+q/j)=\Gamma(n+q)/[\Gamma(n)\Gamma(1+q)]\). Then \(M_n=W_n/A_n\) is a martingale; its increments have second moments bounded by \(4/A_n^2\). Because \(q>1/2\), \(\sum_n A_n^{-2}<\infty\), so \(M_n\to M_\infty\) almost surely and in \(L^2\). Hence \(L_q=M_\infty/\Gamma(1+q)\). In fact, for each \(T>0\),
\[
\sup_{0\le t\le T}\left|n^{-q}W_{\lfloor nt\rfloor}-t^qL_q\right|\xrightarrow{\rm a.s.}0.
\]
To check the endpoint \(t=0\), use \(\sup_n|M_n|<\infty\) almost surely and \(A_k\le C k^q\). On \(t\ge\delta\), convergence is uniform by convergence of \(M_k\) and regular variation of \(A_k\); then send \(\delta\downarrow0\).

Writing \(V_n=\mathbb E W_n^2\), conditional expansion gives \(V_1=1\) and \(V_{n+1}=(1+2q/n)V_n+1\). Solving this first-order recurrence gives
\[
V_n=\frac{1}{2q-1}\left[\frac{\Gamma(n+2q)}{\Gamma(n)\Gamma(2q)}-n\right].
\]
Consequently \(\mathbb E L_q^2=1/[(2q-1)\Gamma(2q)]\), equal to the variance asserted above; it is positive. Symmetry yields \(\mathbb E L_q=0\).

**2. The bounded memory correction.** Set \(\eta_{n+1}=Y_{n+1}-qW_n/n\). This is a bounded martingale difference. Pairing the alternating sum gives, for each \(m\ge1\),
\[
\frac{Z_{2m+1}}q=\sum_{j=1}^m\left(\frac{W_{2j}}{2j}-\frac{W_{2j-1}}{2j-1}\right)
=\sum_{j=1}^m\frac{\eta_{2j}}{2j}-(1-q)\sum_{j=1}^m\frac{W_{2j-1}}{2j(2j-1)}.
\]
The first sum converges almost surely and in \(L^2\) because it is a square-summable martingale transform. For the second, \(\|W_k\|_2=O(k^q)\) and \(q<1\), so the series is absolutely convergent in \(L^2\), and also almost surely by the absolute-sum estimate. Since \(W_k/k\to0\) almost surely and in \(L^2\), the intervening even-index values have the same limit. Hence \(Z_n\to Z_\infty\) almost surely and in \(L^2\). The random variable is centered by symmetry.

**3. A mixing functional central limit.** Put \(U_n=S_n-Z_n\). Its increments are \(\Delta U_1=Y_1\) and, for \(k\ge2\),
\[
\Delta U_k=(-1)^{k-1}\left(Y_k-q\frac{W_{k-1}}{k-1}\right).
\]
They are martingale differences bounded by \(2\). Their predictable quadratic variation obeys
\[
\langle U\rangle_n=n-q^2\sum_{k=1}^{n-1}\left(\frac{W_k}{k}\right)^2.
\]
As \(W_k/k=O(k^{q-1})\to0\) almost surely, Cesàro summation yields \(n^{-1}\langle U\rangle_{\lfloor nt\rfloor}\to t\), uniformly on \([0,T]\). The bounded jumps satisfy the conditional Lindeberg condition. The martingale functional central limit theorem therefore gives \(n^{-1/2}U_{\lfloor n\cdot\rfloor}\Rightarrow B\).

The stronger **mixing** statement follows without an additional independence assumption. Fix an integer \(m\) and any positive-probability history \(Y_1,\ldots,Y_m\). Under the probability law conditional on that history, the increments after \(m\) remain martingale differences with the same bounded jumps and unit limiting predictable quadratic variation. The finite prefix is \(o(\sqrt n)\), so the functional martingale CLT gives the **same** Brownian limit under each conditional law. Thus for bounded continuous \(f\) on path space and every bounded \(\mathcal F_m\)-measurable \(H\),
\[
\mathbb E\left[H f\left(n^{-1/2}U_{\lfloor n\cdot\rfloor}\right)\right]
\longrightarrow\mathbb EH\,\mathbb Ef(B).
\]
For arbitrary bounded \(H\) measurable with respect to \(\mathcal F_\infty=\sigma(\cup_m\mathcal F_m)\), approximate \(H\) in \(L^1\) by \(\mathbb E[H\mid\mathcal F_m]\) and then send \(m\to\infty\). Thus the Brownian functional limit is mixing relative to the entire original history. In particular it is independent of the pair \((L_q,Z_\infty)\). Because \(\sup_{k\le nT}|Z_k|<\infty\) almost surely (the correction converges), \(\sup_{t\le T}|S_{\lfloor nt\rfloor}-U_{\lfloor nt\rfloor}|/\sqrt n\to0\). Combining with the almost-sure functional memory limit and \(Z_{\lfloor nT\rfloor}\to Z_\infty\) establishes the joint convergence.

**4. Strict residual anticorrelation.** For each \(k\), martingale projection gives
\[
\mathbb E[L_qW_k]
=\frac{1}{\Gamma(1+q)}\mathbb E[M_\infty W_k]
=\frac{V_k}{A_k\Gamma(1+q)}.
\]
Taking the \(L^2\)-limit of the finite covariance identity therefore yields
\[
\operatorname{Cov}(L_q,Z_\infty)
=\frac{q}{\Gamma(1+q)}\sum_{k=1}^\infty(-1)^k b_k,
\qquad b_k=\frac{V_k}{kA_k}.
\]
This convergent alternating series has a definite strict sign. Define \(H_k=(1-q+q/k)V_k-k\). The variance recurrence implies \(H_1=0\) and
\[
H_{k+1}=
\frac{(1-q+q/(k+1))(1+2q/k)}{1-q+q/k}\,H_k
+\frac{kq(1-q)}{k(1-q)+q}.
\]
Thus \(H_k>0\) for \(k\ge2\). Direct subtraction gives
\[
b_{k+1}-b_k=-\frac{H_k}{k(k+1)A_k(1+q/k)}.
\]
Therefore \(b_1=b_2=1\) and \(b_{k+1}<b_k\) for all \(k\ge2\). Moreover \(b_k=O(k^{q-1})\to0\). Pairing terms \(-b_{2j-1}+b_{2j}\) shows that the first pair vanishes and every following pair is strictly negative; their convergent sum is negative. Since \(q>0\), the covariance is strictly negative.

## Verification

The standalone standard-library script `elephant_joint_checker.py` checks all \(2^n\) sign histories for every \(1\le n\le10\), separately at \(q=3/5,2/3,4/5,9/10\). It uses exact rational transition probabilities and confirms the pathwise martingale decomposition, all three joint second-moment recursions, memory-martingale projection against the correction, and finite monotonicity of the covariance-series terms. Run `python elephant_joint_checker.py`. The observed check count is 28712. Exact enumeration does not establish the infinite-process convergence or global covariance sign; these follow from the proof above.

## Relationship to prior work

Mukherjee and Talukdar (2026), arXiv:2604.04922v1, identify the signed-location representation, the bounded correction and its \(L^2\) limit (Theorem 2.1), and the **marginal** Brownian functional limit (Corollary 2.1). Bercu (2017), arXiv:1707.04130v1, gives the classical elephant-walk superdiffusive limit and its moment properties. The present theorem instead determines the **joint** weak law under incompatible diffusive/superdiffusive scales, proves independence of the Brownian factor from both history-dependent memory limits, and establishes an exact strict negative sign for the dependence *within* those limits.

Shibata (2025), arXiv:2511.10347v1, studies generalized periodic-lattice elephant walks. Its bipartite type uses separate odd/even memory urns, rather than the common global history used here; its statements do not supply this joint Gaussian/non-Gaussian factorization or the displayed covariance sign. The standard martingale functional CLT is the main general tool, but it does not by itself identify the interacting memory limits or their residual covariance.

## Limitations

The theorem requires a fixed parameter strictly in the superdiffusive interval \(3/4<p<1\), a fair first generator, and global-history binary memory. At \(p=1\) the Gaussian limit degenerates; the critical endpoint \(p=3/4\) requires another normalization. No convergence rate, explicit joint density of \((L_q,Z_\infty)\), or analogous classification for other groups is claimed. Standard conditional martingale-limit results are used; no external formal certification or independent scientific audit is asserted. Priority cannot be guaranteed against unindexed equivalent formulations.

## References

1. S. S. Mukherjee and H. Talukdar, *Elephant random walk on the infinite dihedral group* (2026), arXiv:2604.04922v1, first posted 2026-04-06. https://arxiv.org/html/2604.04922v1
2. B. Bercu, *A martingale approach for the elephant random walk* (2017), arXiv:1707.04130v1. https://arxiv.org/html/1707.04130v1
3. S. Shibata, *Functional limit theorems for elephant random walks on general periodic structures* (2025), arXiv:2511.10347v1. https://arxiv.org/html/2511.10347v1
