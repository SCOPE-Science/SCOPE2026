# Balanced alternating coverage beats independent sampling by half a logarithm

## Finding

Let \(n\ge 2\). On the complete bipartite graph \(K_{n,n}\), start a non-lazy simple random walk at any fixed vertex, and write \(C_n^{\mathrm{alt}}\) for the number of further steps before every vertex has been visited. On the same \(2n\)-vertex set, begin from the same fixed initial vertex, but subsequently sample each vertex independently and uniformly; let \(C_n^{\mathrm{iid}}\) be its number of further draws needed to cover the set.

**Theorem.** For every integer \(n\ge 2\) and every integer \(t\ge0\),
\[
\Pr\{C_n^{\mathrm{alt}}\le t\}\ge\Pr\{C_n^{\mathrm{iid}}\le t\}.
\]
Moreover,
\[
\boxed{\mathbb E C_n^{\mathrm{iid}}-\mathbb E C_n^{\mathrm{alt}}\sim\frac12\log n}\qquad(n\to\infty).
\]
The first statement is finite-sample stochastic domination; the second identifies the first divergent improvement beyond the common leading \(2n\log(2n)\) cover-time scale. For \(n=2\), the expectation difference equals exactly \(4/3\).

## Assumptions and scope

All transitions on \(K_{n,n}\) are uniform across the opposite side, with no holding. The initial vertex is fixed and is counted as visited without a transition. In the comparison process, each subsequent draw is independent and uniform over all \(2n\) vertices, including the initial vertex. All times are **additional** steps or draws following that initial observation. Logarithms are natural. The stochastic-order statement does not assert a pathwise coupling with strict improvement on every outcome.

Write \(T_n\) for the number of independent uniform draws from \(n\) types required to see all types, including the first draw; set \(F_n(k)=\Pr(T_n\le k)\) for integer \(k\ge0\), and \(p_n(k)=\Pr(T_n=k)\). Let \(H_j=\sum_{i=1}^{j}1/i\).

## Proof

**1. Independent side-collectors and stochastic dominance.** Since the walk alternates sides, the vertices observed on any one side after its initial observation are independent and uniform on that side, independently of the opposite-side observations. By symmetry, the time in side-observation counts to complete either side has law \(T_n\); the two counts are independent, even though the first observation on one side is fixed. If \(T,T'\) are these independent counts, then
\[
C_n^{\mathrm{alt}}=2\max(T,T')-2+\mathbf1_{\{T\le T'\}}.
\]
At time \(t\), exactly \(a=\lfloor t/2\rfloor+1\) observations have occurred on the starting side and \(b=\lceil t/2\rceil\) on the other, and \(a+b=t+1\). Hence
\[
\Pr(C_n^{\mathrm{alt}}\le t)=F_n(a)F_n(b).
\]
In the independent-uniform comparison, condition on \(B\sim\operatorname{Bin}(t,1/2)\), the number of subsequent draws from the starting side. Conditioning also on the chosen sides preserves uniform independence within each side. Therefore
\[
\Pr(C_n^{\mathrm{iid}}\le t)
=\mathbb E\bigl[F_n(B+1)F_n(t-B)\bigr].
\]
To compare these, recall that \(T_n\) is a sum of \(n\) independent geometric waiting times with respective success probabilities \(n/n,(n-1)/n,\ldots,1/n\). Each geometric mass sequence on positive integers is log-concave with no internal zeros. Convolution preserves discrete log-concavity (a direct consequence of the two-by-two minors of convolution Toeplitz matrices); cumulative summation is convolution with the log-concave sequence \(\mathbf1_{\{k\ge0\}}\). Thus \(F_n(k)\) is log-concave in integer \(k\ge0\). Consequently, for any nonnegative integers \(u,v\) with \(u+v=t+1\), the product \(F_n(u)F_n(v)\) is maximized when \(u,v\) differ by at most one. Apply this pointwise to \(u=B+1,v=t-B\), then take expectation.

**2. An exact mean identity.** Exchangeability and the preceding pathwise count identity give
\[
\mathbb E C_n^{\mathrm{alt}}
=2\mathbb E\max(T,T')-\frac32+\frac12\Pr(T=T').
\]
The ordinary independent-uniform coupon collector satisfies \(\mathbb E C_n^{\mathrm{iid}}=2nH_{2n}-1\). Its difference from alternating coverage is therefore
\[
G_n:=\mathbb E C_n^{\mathrm{iid}}-\mathbb E C_n^{\mathrm{alt}}
=2\Delta_n+\frac12-\frac12\Pr(T=T'),
\quad\Delta_n=nH_{2n}-\mathbb E\max(T,T').
\]
The final coupon waiting time is an independent geometric variable of success probability \(1/n\); hence \(\sup_k p_n(k)\le1/n\) and \(0\le\Pr(T=T')\le1/n\). It remains to prove \(\Delta_n/\log n\to1/4\).

**3. Exact Poisson-clock comparison.** Let \(S_k=E_1+\cdots+E_k\), with independent mean-one exponential variables, and let \(S'_l\) be an independent such sum. The coupon marks of two independent unit-rate Poisson streams are independent uniform samples from their respective sets of \(n\) types. Their completion times \(S_T,S'_{T'}\) have the same joint distribution as the maxima of first arrivals of \(2n\) independent Poisson processes of individual rate \(1/n\). Thus
\[
\mathbb E\max(S_T,S'_{T'})=nH_{2n}.
\]
For \(k,l\ge1\) define the nonnegative Jensen gap
\[
h_{kl}=\mathbb E|S_k-S'_l|-|k-l|.
\]
Conditioning on the independent coupon counts and using the formula for the maximum of two numbers yields the *exact* identity
\[
\Delta_n=\frac12\sum_{k,l\ge n}p_n(k)p_n(l)h_{kl}.
\tag{1}
\]

**4. Localization estimates.** Put \(q_n=n\log n\) and \(s_n=\sqrt{2n\log n}\). Standard exponential moment calculations, included here for clarity, show that for \(\eta_{kl}=(S_k-k)-(S'_l-l)\),
\[
\mathbb E e^{z\eta_{kl}}
=e^{-(k-l)z}(1-z)^{-k}(1+z)^{-l},\qquad |z|<1.
\]
Chernoff's inequality therefore gives an absolute \(c>0\) such that
\[
\Pr(|\eta_{kl}|>v)\le2\exp\{-c\min(v^2/(k+l),v)\},\qquad v>0.
\]
As the centered signed difference has mean zero, splitting at the possible change of sign gives
\[
0\le h_{kl}\le4\int_{|k-l|}^{\infty}
\exp\{-c\min(v^2/(k+l),v)\}\,dv.
\tag{2}
\]
Splitting the sum over \(l\) into \(l<k/2\), \(k/2\le l\le2k\), and \(l>2k\), and summing the exponential envelopes from (2), gives for an absolute constant \(C\),
\[
\sum_{l\ge1}h_{kl}\le C(k+1).
\tag{3}
\]
Indeed, the middle range contributes at most \(C\sqrt{k}\sum_{j\in\mathbb Z}e^{-c'j^2/k}=O(k)\), and the two outside ranges have exponential tails. Since \(p_n(l)\le1/n\), equation (3) gives \(\sum_l p_n(l)h_{kl}\le C(k+1)/n\).

The coupon count has \(\mathbb ET_n=nH_n\) and \(\operatorname{Var}(T_n)=n^2\sum_{j=1}^n j^{-2}-nH_n=O(n^2)\). Thus the random variables \((T_n-q_n)/n\) have uniformly bounded second moments. It follows from (1), (3), and Cauchy--Schwarz/Markov bounds that terms with \(|k-q_n|>Kn\) or \(|l-q_n|>Kn\), divided by \(\log n\), have \(\limsup_{n\to\infty}\) bounded by \(C/K^2\). We can therefore fix large \(K\), first analyze \(k,l\) in this central window, then let \(K\to\infty\).

For central \(k\) and \(l\) at distance \(>A s_n\), the same Bernstein envelope (2), together with \(p_n(l)\le1/n\), bounds their contribution to \(\Delta_n/\log n\) by a function of \(A\) tending to zero as \(A\to\infty\), uniformly in \(n\). In particular, only pairs separated by \(O(s_n)\) contribute to the limit.

**5. Local limits and the leading constant.** Inclusion--exclusion gives
\[
p_n(k)=\sum_{j=1}^n(-1)^{j+1}\binom nj\frac jn\left(1-\frac jn\right)^{k-1}.
\]
Uniformly for \(y\) in any fixed bounded interval,
\[
n\,p_n(\lfloor n\log n+ny\rfloor)
\longrightarrow g(y):=e^{-y-e^{-y}}.
\tag{4}
\]
For each fixed \(j\), the summand multiplied by \(n\) tends to \((-1)^{j+1}j e^{-jy}/j!\), and a summable bound \(j e^{Kj}/j!\) on \(|y|\le K\) proves uniform convergence.

For central \(k,l\) with \((k-l)/s_n\to u\), the independent gamma-sum central limit theorem and uniform integrability (variance \(k+l\sim s_n^2\)) yield
\[
\frac{h_{kl}}{s_n}\longrightarrow
m(u):=\mathbb E|u+Z|-|u|,
\qquad Z\sim N(0,1),
\tag{5}
\]
uniformly for \(u\) in compact sets. The tail envelope (2) makes the corresponding Riemann integrals uniformly integrable. Since \(s_n/n\to0\), formulas (4)--(5) and the double Riemann sum in (1) give
\[
\frac{\Delta_n}{\log n}\longrightarrow
\left(\int_{-\infty}^{\infty}g(y)^2dy\right)
\left(\int_{-\infty}^{\infty}m(u)du\right).
\]
The first integral is \(1/4\), by \(z=e^{-y}\). Symmetry of \(Z\) gives \(m(u)=\mathbb E[(|Z|-|u|)_+]\), and integrating the triangular function in \(u\) gives \(\int m(u)du=\mathbb E Z^2=1\). Hence \(\Delta_n/\log n\to1/4\), so \(G_n/\log n\to1/2\), as claimed.

## Verification

Run the accompanying Python standard-library checker by executing `python3 check.py`. It verifies exact finite-sample stochastic domination at \(228-6=222\) parameter pairs, plus six exact rational expected-gap values, for \(2\le n\le7\) and \(0\le t\le8n\). It prints `PASS: 228 exact rational assertions` and the exact gaps for \(n=2,\ldots,7\). These tests are diagnostics only; the all-size stochastic ordering and logarithmic asymptotic are proved above. The checker has no network dependencies.

## Relationship to prior work

Doumas and Papanicolaou, *Sampling from a mixture of different groups of coupons* (arXiv:1709.04500, first posted 2017-09-13), analyze **independent** sampling from several coupon groups, including their cover-time maximum and Poisson embedding. Their asymptotic comparison in Section 4.2 assumes unequal group probabilities (their \(\lambda>1\)); it does not analyze a deterministic alternating schedule versus an independent random group choice, nor the logarithmic difference. Myers and Wilf (arXiv:math/0304229, 2003) calculate simultaneous-completion probabilities for two independently progressing collectors; this overlaps the intermediate tie probability but not the stochastic-cover comparison or its half-logarithmic mean difference. Rivera, Sauerwald and Sylvester (arXiv:2011.07893, first posted 2020-11-16) study cover times of multiple random walks on general graphs, but not this fixed-start single-walk versus independent-sampling comparison. Public related work on structured coupon collectors addresses independently sampled subsets or coupon distributions, not the present deterministic side balance.

These statements distinguish the result from inspected source material; they do not establish absolute historical priority. Generic de-Poissonization results for maxima are a residual priority risk and may offer an alternative derivation.

## Limitations

Both parts of \(K_{n,n}\) must have equal size and the walk must be non-lazy. The comparison samples with replacement, including the start vertex, after one fixed initial observation. This analysis does not give a constant-order remainder in the expectation gap, a uniform comparison on unbalanced bipartite graphs, or a direct extension to more general periodic schedules. No independent audit or exhaustive historical-priority certification has been completed.

## References

- A. V. Doumas and V. G. Papanicolaou, *Sampling from a mixture of different groups of coupons*, first posted 2017-09-13, https://arxiv.org/abs/1709.04500 .
- N. Rivera, T. Sauerwald and J. Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many*, first posted 2020-11-16, https://arxiv.org/abs/2011.07893 .
- A. N. Myers and H. S. Wilf, *Some new aspects of the coupon-collector's problem*, first posted 2003-04-16, https://arxiv.org/abs/math/0304229 .
- A. Falgas-Ravry, J. Larsson and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, https://arxiv.org/abs/1601.04455 .
