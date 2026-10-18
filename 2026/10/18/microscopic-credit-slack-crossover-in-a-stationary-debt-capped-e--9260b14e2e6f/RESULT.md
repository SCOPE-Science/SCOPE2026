# Microscopic credit-slack crossover in a stationary debt-capped exchange model

## Finding

Let \(N\to\infty\) and suppose \(a_N\to\infty\), \(a_N=o(N)\), and integers \(K_N,L_N\) satisfy \(K_N/(a_NN)\to\kappa\in(0,\infty)\) and \(L_N/K_N\to r\in(0,\infty)\). The conserved-money exchange chain is defined below, with nonnegative and negative wealth transfer probabilities \(g_{+,N}\) and \(g_{-,N}\). Put \(q_N=g_{-,N}/g_{+,N}\ge1\), \(h_N=\log q_N\), and define unused credit \(S_N=L_N-\sum_i(-\xi_i)_+\) under its stationary distribution. Write
\[
c=\frac1{\kappa\sqrt{r(1+r)}}.
\]
The following three microscopic saturation laws hold, including convergence of the displayed scaled means:

1. If \(a_Nh_N\to\gamma\in[0,\infty)\), then
\[
S_N/a_N\ \Rightarrow\ \operatorname{Exp}(c+\gamma),
\qquad \mathbb E S_N/a_N\to(c+\gamma)^{-1}.
\]
2. If \(h_N\to0\) and \(a_Nh_N\to\infty\), then
\[
h_NS_N\ \Rightarrow\ \operatorname{Exp}(1),
\qquad h_N\mathbb ES_N\to1.
\]
3. If \(q_N\to q\in(1,\infty)\), then
\[
\Pr(S_N=s)\to(1-q^{-1})q^{-s}\quad(s=0,1,\ldots),
\qquad \mathbb ES_N\to\frac1{q-1}.
\]
In particular, exact rate balance yields order-\(a_N\) unused credit, while a fixed disadvantage for positive-wealth transfers yields order-one geometric slack. The critical bias \(h_N\asymp a_N^{-1}\) changes the exponential rate additively.

## Assumptions and scope

For each \(N\ge3\), take a connected undirected transfer network with symmetric positive transition weights along its edges. The state is \(\xi=(\xi_1,\ldots,\xi_N)\in\mathbb Z^N\) with \(\sum_i\xi_i=K_N\ge1\) and total debt \(B(\xi)=\sum_i(-\xi_i)_+\le L_N\). On a directed edge \((i,j)\), attempt to replace \(\xi_i\) by \(\xi_i-1\), \(\xi_j\) by \(\xi_j+1\), rejecting transfers violating \(B\le L_N\). An otherwise admissible transfer is executed with probability \(g_{+,N}\in(0,1]\) if \(\xi_i\ge1\), or \(g_{-,N}\in(0,1]\) if \(\xi_i\le0\). Assume \(q_N\ge1\). All limits concern the unique finite-state stationary law, not a transient process. The asymptotic restrictions \(a_N=o(N)\) and \(\kappa,r>0\) are part of the theorem; the claim does not cover unrestricted growth of \(a_N\), nonlinear transfer probabilities, negative-bias ratios, or multi-bank heterogeneity.

## Proof

**1. Exact debt partition.** Detailed balance gives the stationary weight proportional to \(\prod_iG(\xi_i)\), where \(G(k)=g_{+,N}^{-k}\) for \(k\ge0\) and \(G(-m)=g_{-,N}^{m}\) for \(m\ge1\), by the standard reversible stationary law. Thus, at fixed debt \(b\), the weight is the constant \(g_{+,N}^{-K_N}q_N^b\). If exactly \(j\) vertices have negative wealth, there are \(\binom Nj\) choices of these vertices, \(\binom{b-1}{j-1}\) strictly positive partitions of the debt, and \(\binom{K_N+b+N-j-1}{N-j-1}\) nonnegative allocations to the other vertices. Hence, writing \(K=K_N\), \(L=L_N\),
\[
C_N(K,b)=\sum_{j=1}^{\min(N-1,b)}\binom Nj\binom{b-1}{j-1}\binom{K+b+N-j-1}{N-j-1}\quad(b\ge1),
\]
with \(C_N(K,0)=\binom{K+N-1}{N-1}\). The exact finite law is
\[
\Pr(S_N=s)=\frac{q_N^{-s}C_N(K,L-s)}{\sum_{t=0}^L q_N^{-t}C_N(K,L-t)},\qquad 0\le s\le L.
\]

**2. Ratio of neighboring debt partitions.** Denote the \(j\)-th summand of \(C_N(K,b)\) by \(T_j(b)\). For \(2\le b\le L\), with a zero ratio when \(j=b\),
\[
\frac{T_j(b-1)}{T_j(b)}=
\frac{b-j}{b-1}\frac{K+b}{K+b+N-j-1},
\quad
\frac{T_{j+1}(b)}{T_j(b)}=
\frac{(N-j)(N-j-1)(b-j)}{(j+1)j(K+b+N-j-1)}.
\]
Fix \(M<\infty\) and restrict \(L-Ma_N\le b\le L\). The second ratio converges uniformly on compact subsets of \(0<j/N<1\) to
\[
R(x)=\frac r{1+r}\left(\frac{1-x}{x}\right)^2,
\]
which decreases strictly through one at \(\pi=\sqrt r/(\sqrt r+\sqrt{1+r})\). The finite summand ratios are strictly decreasing in \(j\), so, for every \(\delta>0\), ratios outside the band \(|j/N-\pi|\le\delta\) are bounded on the appropriate side of one by constants uniform in \(b\), and the resulting geometric tail comparison implies that the summand-weighted index \(J/N\) converges in probability to \(\pi\), uniformly in this band of \(b\). The first displayed ratio then yields, uniformly for \(L-Ma_N\le b\le L\),
\[
a_N\left(1-\frac{C_N(K,b-1)}{C_N(K,b)}\right)
\longrightarrow\frac\pi{r\kappa}+\frac{1-\pi}{(1+r)\kappa}=c.
\]
Taking logarithms and summing ratios proves, for every fixed \(x\ge0\),
\[
\frac{C_N(K,L-\lfloor xa_N\rfloor)}{C_N(K,L)}\to e^{-cx},
\]
uniformly over bounded \(x\)-intervals. Also, for integer \(s=o(a_N)\), the same ratio tends to one uniformly over such windows.

**3. Uniform domination and the zero-debt endpoint.** The two factors in the first summand ratio are \(1-(j-1)/(b-1)\) and \(1-(N-j-1)/(K+b+N-j-1)\). Therefore \(1-z\le e^{-z}\) gives, for \(b\ge2\),
\[
\frac{C_N(K,b-1)}{C_N(K,b)}
\le\exp\left(-\frac{N-2}{K+L+N}\right)=e^{-d_N},\quad a_Nd_N\to\frac1{(1+r)\kappa}>0.
\]
At \(b=1\), the exact formula gives \(C_N(K,1)/C_N(K,0)=N(N-1)/(K+1)\to\infty\), using \(a_N=o(N)\). Thus for every \(s\in\{0,\ldots,L\}\),
\[
0\le \frac{C_N(K,L-s)}{C_N(K,L)}\le e^{-d_N(s-1)_+}.
\]
This controls all tails rather than relying on local convergence alone.

**4. Scaling limits and moments.** For \(a_Nh_N\to\gamma\ge0\), combine the local ratio with \(q_N^{-\lfloor xa_N\rfloor}\to e^{-\gamma x}\). The last domination bound permits Riemann summation and convergence of the first moment; the normalizer divided by \(a_N\) tends to \((c+\gamma)^{-1}\), yielding the first assertion. If \(h_N\downarrow0\) and \(a_Nh_N\to\infty\), relevant \(s\) satisfy \(s=O(1/h_N)=o(a_N)\), where the partition ratio tends to one. Comparison with the geometric weights \(e^{-h_Ns}\) and the same domination gives the second assertion, including its mean. Finally, if \(q_N\to q>1\), each fixed-\(s\) partition ratio tends to one and \(q_N^{-s}\) supplies a uniform summable geometric bound (also after multiplying by \(s\)); dominated convergence proves the third assertion.

## Verification

The accompanying standard-library script `debt_slack_verify.py` checks the partition count by exhaustive enumeration of small integer configurations, tests strict growth of the partition count in finite cases, checks neighboring partition ratios and their global bounds, and evaluates local and finite-window limits using log-gamma summation. The completed script produced `PASS: 131 independent exact and numerical assertions`. These finite checks are diagnostic only. The proof of the infinite asymptotic statements is the ratio concentration and uniform tail argument above.

## Relationship to prior work

Sakagawa, *Convergence of stationary distributions for a class of zero-range processes and its application to a wealth distribution model with debt* (arXiv:2610.00901v1, submitted October 1, 2026), proves the general reversible product formula (Proposition 1.1), a two-dimensional local limit theorem (Theorem 2.3), and a coarse saturation estimate (Lemma 2.4) for fixed transfer laws. We use the product formula, not claim it anew. The macroscopic limiting wealth marginal of Theorem 1.4 does not determine the microscopic bank-slack law. Theorem 2.3 can assist a partition-ratio analysis in the fixed-law case, and consequently represents meaningful nearby coverage; it does not state or assume a triangular family of transfer biases \(a_N\log(g_{-,N}/g_{+,N})\to\gamma\), nor give the three-scale slack crossover. The proof here is a direct combinatorial derivation under that new scaling.

Lanchier and Reed studied the uniform rate bank/debt model (arXiv:1812.10359), Cao and Motsch developed a mean-field exchange model (arXiv:2208.11003), and Cao and Reed examined bias and a two-phase mean-field equilibrium (arXiv:2311.07851). These predecessors do not appear to provide this triangular-array stationary credit-slack classification; there remains a priority risk from broader combinatorial conditioned-allocation or ensemble-equivalence results.

## Limitations

The theorem is restricted to piecewise constant transfer probabilities, symmetric connected transfer weights, \(a_N=o(N)\), \(q_N\ge1\), and the specified positive density limits. Its three cases do not cover all possible oscillating bias sequences, and no mixing time or nonequilibrium process limit is claimed. The finite-state numerical checks do not prove the limiting laws. The novelty assessment remains provisional pending independent examination, especially of partition-function consequences of previously known local limit theorems.

## References

- H. Sakagawa, *Convergence of stationary distributions for a class of zero-range processes and its application to a wealth distribution model with debt*, arXiv:2610.00901v1 (2026), https://arxiv.org/html/2610.00901v1.
- N. Lanchier and S. Reed, *Rigorous results for the distribution of money on connected graphs (models with debts)*, arXiv:1812.10359 (2018), https://arxiv.org/abs/1812.10359.
- F. Cao and S. Motsch, *Uncovering a two-phase dynamics from a dollar exchange model with bank and debt*, arXiv:2208.11003 (2022), https://arxiv.org/abs/2208.11003.
- F. Cao and S. Reed, *A biased dollar exchange model involving bank and debt with discontinuous equilibrium*, arXiv:2311.07851 (2023), https://arxiv.org/abs/2311.07851.
