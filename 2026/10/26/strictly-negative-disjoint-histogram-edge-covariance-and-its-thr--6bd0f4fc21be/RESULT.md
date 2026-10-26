# Strictly negative disjoint histogram-edge covariance and its three scaling phases

## Finding
Let \(m\geq4\), \(N\geq1\), and let \(X=(X_1,\ldots,X_m)\) have a multinomial distribution with \(N\) trials and a fixed probability vector \((p_1,\ldots,p_m)\). Assume \(p_1,p_2,p_3,p_4>0\); all other masses may vanish. Put
\[
u=p_1+p_2,\qquad v=p_3+p_4,\qquad a=\frac{|p_2-p_1|}{u},\qquad b=\frac{|p_4-p_3|}{v}.
\]
Define the absolute differences on two *disjoint* ordered edges by
\[
A_N=|X_2-X_1|,\qquad B_N=|X_4-X_3|.
\]
Then their covariance is **strictly negative at every positive sample size**:
\[
\operatorname{Cov}(A_N,B_N)<0 \quad (N\geq1).
\]
For fixed cell probabilities, the *exact leading asymptotics* display three distinct orders, depending on whether the two local contrasts are balanced:
\[
\operatorname{Cov}(A_N,B_N)=
\begin{cases}
-Nuvab+o(N),&a>0,\ b>0,\\[3pt]
-vb\sqrt{Nu/(2\pi)}+o(\sqrt N),&a=0,\ b>0,\\[3pt]
-ua\sqrt{Nv/(2\pi)}+o(\sqrt N),&a>0,\ b=0,\\[3pt]
-\sqrt{uv}/(2\pi)+o(1),&a=b=0.
\end{cases}
\]
All displayed coefficients are strictly negative. For the uniform law on \(m\) cells the last case gives \(-1/(\pi m)+o(1)\), in agreement with the previously published uniform-null result. Thus two nonoverlapping total-variation edges repel even when their individual cell probabilities are unequal; balancing one and then both edges changes the size of the dependence from order \(N\) to order \(\sqrt N\) and then to order one.

## Assumptions and scope
All limits keep \(m\) and the cell probabilities fixed while \(N\to\infty\). The four selected cells have strictly positive probabilities; the residual mass \(1-u-v\) may be zero. The statistic here is the **uncentered** absolute difference \(|X_{i+1}-X_i|\), not the reference-centered statistic \(|(X_{i+1}-Np_{i+1})-(X_i-Np_i)|\). The latter generally has different covariance behavior. The edge pairs do not share a cell, and no claim is made for adjacent overlapping edges.

## Proof
**1. Exact conditioning.** Put \(K=X_1+X_2\) and \(L=X_3+X_4\). Then \((K,L,N-K-L)\) has multinomial parameters \((N;u,v,1-u-v)\). Given \((K,L)\), the within-block splits are independent and
\[
X_2\mid K=k\sim\operatorname{Bin}\!\left(k,\frac{p_2}{u}\right),\quad
X_4\mid L=\ell\sim\operatorname{Bin}\!\left(\ell,\frac{p_4}{v}\right).
\]
For \(0<\theta<1\), define \(g_\theta(k)=\mathbb E|2\operatorname{Bin}(k,\theta)-k|\). Conditional independence yields the *identity*
\[
\operatorname{Cov}(A_N,B_N)
=\operatorname{Cov}\!\left(g_{p_2/u}(K),g_{p_4/v}(L)\right).
\]

**2. A monotone folded-walk lemma.** Let \(S_k\) be the sum of \(k\) independent signs with probability \(\theta\) for \(+1\), and put \(\delta=2\theta-1\). Define \(\operatorname{sgn}(0)=0\). Conditioning on the last sign and using the identity \(|s+1|+|s-1|=2|s|+2\mathbf1_{\{s=0\}}\), one obtains
\[
g_\theta(k+1)-g_\theta(k)
=\delta\,\mathbb E\operatorname{sgn}(S_k)+\mathbb P(S_k=0).
\]
The expectation \(\mathbb E\operatorname{sgn}(S_k)\) has the same weak sign as \(\delta\): couple the signs monotonically with unbiased signs when \(\delta\ge0\), and reflect the argument for \(\delta\le0\). Hence \(g_\theta\) is nondecreasing, and \(g_\theta(0)=0<g_\theta(k)\) for \(k\ge1\).

Since \(0<u<1\), \(K\) has positive probability at both \(0\) and \(N\). Conditional on \(K=k\), \(L\) has distribution \(\operatorname{Bin}(N-k,v/(1-u))\). The function
\[
h(k)=\mathbb E\left[g_{p_4/v}(L)\mid K=k\right]
\]
is nonincreasing in \(k\), by adding independent Bernoulli trials to couple binomials with different trial counts. It also satisfies \(h(0)>h(N)=0\). For an independent copy \(K'\),
\[
2\operatorname{Cov}(g_{p_2/u}(K),h(K))
=\mathbb E\left[(g_{p_2/u}(K)-g_{p_2/u}(K'))(h(K)-h(K'))\right]<0.
\]
The nonpositive integrand is strictly negative when \((K,K')=(N,0)\), an event of positive probability. By the tower property this covariance is \(\operatorname{Cov}(A_N,B_N)\). This proves strict negativity for every \(N\ge1\), including the four-cell case \(u+v=1\).

**3. Asymptotic folded-walk lemma.** For fixed \(0<\theta<1\), write \(d=|2\theta-1|\). If \(d>0\), a Chernoff bound on the wrong-sign event, together with \(|S_k|\le k\), gives
\[
g_\theta(k)=dk+O(k e^{-c_\theta k})
\]
for some \(c_\theta>0\). If \(d=0\), the central-binomial formula for the simple random walk and Stirling's formula give
\[
g_{1/2}(k)=\sqrt{2k/\pi}+O((k+1)^{-1/2}).
\]
Let \(K_N\sim\operatorname{Bin}(N,u)\), with fixed \(u\in(0,1)\). Chernoff concentration, the fourth central-moment bound \(\mathbb E(K_N-Nu)^4=O(N^2)\), and second-order Taylor expansion of the square root on \(|K_N-Nu|\le Nu/2\) show that
\[
g_{1/2}(K_N)=c_{u,N}+\frac{K_N-Nu}{\sqrt{2\pi Nu}}+R_{u,N},
\qquad \|R_{u,N}\|_{L^2}=O(N^{-1/2}),
\]
where \(c_{u,N}\) is a deterministic constant (for instance \(\sqrt{2Nu/\pi}\)). On the exponentially small complement, \(g_{1/2}(K_N)\le N\) handles the error. In the biased case,
\[
g_\theta(K_N)=dK_N+E_{u,N},\qquad\|E_{u,N}\|_{L^2}=O(e^{-cN})
\]
for some \(c>0\) (polynomial factors may be absorbed by reducing \(c\)). The analogous statements hold for \(L\sim\operatorname{Bin}(N,v)\).

**4. The three orders.** Since
\[
\operatorname{Cov}(K,L)=-Nuv,
\]
substituting the two expansions into the exact conditioning identity gives the four cases. For instance, if both pairs are balanced, the leading product of slopes is
\[
\frac{1}{\sqrt{2\pi Nu}}\frac{1}{\sqrt{2\pi Nv}}(-Nuv)
=-\frac{\sqrt{uv}}{2\pi}.
\]
The \(L^2\) remainder bounds and Cauchy–Schwarz make the covariance error \(o(1)\). With one balanced pair and one biased pair, the leading product is of order \(\sqrt N\), and the remainder is \(o(\sqrt N)\); with two biased pairs it is of order \(N\), and the error is \(o(N)\). All cases follow as stated. \(\square\)

## Verification
A standalone standard-library Python program, `verify_disjoint_covariance.py`, exactly evaluates the conditional folded-binomial means and multinomial pair totals using rational arithmetic. It ran successfully on six fixed rational probability vectors, for each \(N=1,\ldots,12\), yielding 72 strict negative covariance checks. The vectors cover all three asymptotic regimes and include the boundary \(u+v=1\). Additional direct numerical evaluations for \(u=1/4,v=1/2\) in the balanced-balanced regime at \(N=128,512,1024\) gave covariances \(-0.05665803\), \(-0.05636616\), and \(-0.05631791\), approaching the analytic constant \(-\sqrt{1/8}/(2\pi)\approx-0.05626977\). These finite checks do not replace the proof of the universal statement or the asymptotic limits.

## Relationship to prior work
Banić and Elezović (arXiv:2610.17046v1, October 12, 2026), Sections 2 and 4, derive the conditional edge representation and the asymptotic covariance \(-1/(\pi m)\) for **equal** probabilities \(1/m\). Their Part 1 (arXiv:2610.13366v1, October 9, 2026) computes uniform-null first moments. The present result identifies the full arbitrary-probability uncentered disjoint-edge sign, including strictly nonuniform within-pair probabilities, and all three regimes with their coefficients. Under uniform probabilities its balanced-balanced case reduces to the known result and is not claimed as new.

The known negative stochastic-order dependence of multinomial block totals (Block, Savits and Shaked, 1985) informs the monotone-conditioning proof; negative dependence of the totals by itself does not state the three asymptotic constants for these nonlinear folded differences. Banić and Elezović list a Part 4 on variance for general **reference-centered** total variation as *in preparation*. Its contents could not be inspected; there is no assertion that it will not cover some related formulas.

## Limitations
The three-phase result keeps all probabilities fixed as sample size grows; it does not characterize critical windows in which within-pair imbalance shrinks with \(N\). All four participating probabilities must be strictly positive. The uncentered and centered statistics are different except at balanced edges, so no conclusion is drawn about the full general-reference null statistic. Originality has been assessed against accessible literature and mathematical records; implicit equivalents in broader negative-dependence or Edgeworth theory remain possible. Independent external verification has not been performed.

## References
1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 2: variance under the uniform null*, arXiv:2610.17046v1 (submitted October 12, 2026), especially Sections 2.2, 4.1, 4.4 and 8. https://arxiv.org/html/2610.17046v1
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366v1 (submitted October 9, 2026), especially Sections 2.3 and 5. https://arxiv.org/html/2610.13366v1
3. H. W. Block, T. H. Savits and M. Shaked, *A concept of negative dependence using stochastic ordering*, Statistics & Probability Letters 3 (1985), 81–86. https://doi.org/10.1016/0167-7152(85)90029-X
