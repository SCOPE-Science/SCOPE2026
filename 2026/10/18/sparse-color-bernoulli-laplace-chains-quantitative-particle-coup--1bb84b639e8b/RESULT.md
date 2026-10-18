# Sparse-color Bernoulli–Laplace chains: quantitative particle coupling and Gaussian cutoff profiles

## Finding

For a two-urn Bernoulli–Laplace chain with \(N\) balls, left capacity \(m\), \(r\) individually distinguishable red balls, and \(k\) exchanged positions from each urn at each step, write \(X_t\) for the number of red balls on the left. Put
\[
h=m/N,\qquad \rho=1-\frac{k}{m}-\frac{k}{N-m}.
\]
When \(X_0=x\), define the independent-binomial proxy
\[
Z_{x,t}\sim {\rm Bin}(x,h+(1-h)\rho^t)+{\rm Bin}(r-x,h-h\rho^t).
\]
Let \(\pi={\rm Hyp}(N,r,m)\), and assume \(1\leq r\leq\min(m,N-m)\), \(1\leq k\leq\min(m,N-m)\). For **every** integer \(t\geq0\),
\[
\left|d_{\rm TV}({\cal L}(X_t\mid X_0=x),\pi)-d_{\rm TV}({\cal L}(Z_{x,t}),{\rm Bin}(r,h))\right|
\leq \binom r2\left[t\left(\frac1{m-r+1}+\frac1{N-m-r+1}\right)+\frac1{N-r+1}\right].\tag{1}
\]

Consider any sequence \(N\to\infty\) with \(r=r_N\to\infty\), \(r_N^2\log(r_N)/N\to0\), \(m_N/N\to h_0\in(0,1)\), and \(k_N/N\to\gamma\in(0,\min(h_0,1-h_0))\). Require \(\rho_N\to\rho_0\), where \(0<|\rho_0|<1\). For integer times \(t_N\geq0\), put \(z_N=\sqrt{r_N}|\rho_N|^{t_N}\). If \(z_N\to z\in[0,\infty]\) and \(x_N/r_N\to u\in[0,1]\), then
\[
d_{\rm TV}({\cal L}(X_{t_N}\mid X_0=x_N),\pi_N)
\longrightarrow 2\Phi\!\left(\frac{|u-h_0|z}{2\sqrt{h_0(1-h_0)}}\right)-1.\tag{2}
\]
At \(z=+\infty\), interpret the limit as one when \(u\ne h_0\); the claim for \(u=h_0\) and \(z=+\infty\) is **not asserted**, since the product of the vanishing initial imbalance and \(z_N\) is then undetermined.

For all such \(z_N\to z\in[0,\infty]\), the worst-start distance has the unconditional limit
\[
\max_{0\leq x\leq r_N}d_{\rm TV}({\cal L}(X_{t_N}\mid X_0=x),\pi_N)
\longrightarrow 2\Phi\!\left(\frac{\max(h_0,1-h_0)z}{2\sqrt{h_0(1-h_0)}}\right)-1,\tag{3}
\]
where the right-hand side is one for \(z=+\infty\). Thus the worst-start chain exhibits total-variation cutoff at
\[
a_N=\frac{\log r_N}{2\log(1/|\rho_N|)}
\]
with a bounded (one-step-order) window. Formula (3) is lattice-aware: along integer-time subsequences it depends on the actual \(z_N\), so no continuous limiting profile is claimed after indiscriminate flooring of real times.

## Assumptions and scope

At each step, choose uniformly, independently, a subset of \(k\) out of \(m\) positions in the left urn and \(k\) out of \(N-m\) in the right urn; exchange the selected balls between urns. All \(r\) red balls are distinguished solely for the proof; all other balls are white. Conditional on the red count \(X_0=x\), the transition law of \(X_t\) is independent of the identities of the red balls. The stationary law is the hypergeometric distribution \(\pi(j)=\binom mj\binom{N-m}{r-j}/\binom Nr\). Total variation is one half the \(\ell^1\)-distance of mass functions. The normal distribution function \(\Phi\) is standard normal. When \(r=1\), the comparison error in (1) is zero.

## Proof

**1. Without-replacement coupling.** Inspect the \(s\) marked red balls present in a given urn of size \(M\), and expose their membership in a uniformly random subset of size \(k\), one marked ball after another. After \(j\) exposures with \(a\) marked balls selected, the conditional next selection probability is \((k-a)/(M-j)\), while under independent selection it is \(k/M\). Since \(0\leq a\leq j\) and \(k\leq M\),
\[
\left|\frac{k-a}{M-j}-\frac{k}{M}\right|\leq\frac{j}{M-j}.
\]
Sequential maximal coupling therefore bounds the total-variation distance from \(s\) independent Bernoulli \((k/M)\) decisions by \(\sum_{j=0}^{s-1}j/(M-j)\leq\binom{s}{2}/(M-s+1)\). Applying it to both urns yields a uniform one-step error at most
\[
\epsilon=\binom r2\left(\frac1{m-r+1}+\frac1{N-m-r+1}\right)
\]
for the **vector** of the \(r\) labeled red-ball locations. Iterating the coupled vector chains for \(t\) steps gives error at most \(t\epsilon\), including every initial vector configuration with exactly \(x\) red balls on the left.

**2. The independent chain.** In the comparison process each labeled red ball independently moves from left to right with probability \(k/m\), and from right to left with probability \(k/(N-m)\). Its unique invariant probability of occupying the left urn is \(h\), and its second eigenvalue is \(\rho\). Consequently the left-occupation probability after \(t\) steps is \(h+(1-h)\rho^t\) for a ball starting left and \(h-h\rho^t\) for one starting right. Summation over the labels gives precisely \(Z_{x,t}\). This remains valid when \(\rho<0\).

**3. Stationary comparison.** Under the stationary red-ball configuration, the red labels occupy a uniform sample without replacement of \(r\) out of \(N\) slots. Applying the sequential coupling in part 1 with \(M=N,k=m,s=r\) gives
\[
d_{\rm TV}(\pi,{\rm Bin}(r,h))\leq\binom r2/(N-r+1).
\]
Contracting under the map from labeled locations to the left count and applying the reverse triangle inequality proves (1).

**4. Gaussian profile at finite \(z\).** The assumptions imply \(r^2\log r/N\to0\), \(\rho\to\rho_0\) bounded in absolute value away from zero and one, and \(m,N-m\asymp N\). If \(z_N\to z>0\), then \(t_N=(\log r_N)/(2\log(1/|\rho_N|))+O(1)\); thus (1) has error \(o(1)\). All \(r\) Bernoulli summands in \(Z_{x,t}\) have success probabilities \(h+O(r^{-1/2})\), uniformly in \(0\leq x\leq r\). Their means differ from the invariant binomial mean \(rh\) by exactly \((x-rh)\rho^t\), while both variances equal \(rh(1-h)+O(\sqrt r)\) uniformly. The classical lattice local central limit theorem for sums of independent Bernoulli variables whose parameters remain in a fixed interior subinterval of \((0,1)\), proved by characteristic-function inversion and Gaussian tail truncation, gives a total-variation comparison of these two mass functions with their unit-cell Gaussian approximations. The total-variation distance of normal laws with equal variance \(\sigma^2\) and mean displacement \(\Delta\) is exactly \(2\Phi(|\Delta|/(2\sigma))-1\). Uniformly in \(x\), the proxy distance therefore equals
\[
2\Phi\!\left(\frac{|x/r-h|\sqrt r|\rho|^t}{2\sqrt{h(1-h)}}\right)-1+o(1).
\]
The \(z=0\) case with \(t=O(\log r)\) follows by the same local limit comparison (all Bernoulli parameters are \(h+o(r^{-1/2})\)); if \(t\) is substantially later, comparison at any earlier cutoff time and contraction in total variation imply convergence to zero. This establishes (2) for finite \(z\), including \(z=0\).

**5. Large \(z\), endpoints, and cutoff.** If \(z_N\to\infty\), the time is no later than the cutoff by a diverging number of steps. When \(x_N/r_N\to u\ne h_0\), the proxy mean differs from \(rh\) by \(|x-rh||\rho|^t\gg\sqrt r\), whereas its variance and the invariant binomial variance are at most \(r/4\). Chebyshev's inequality on a midpoint-separating event yields proxy distance \(1-o(1)\). Since \(t_N=O(\log r_N)\), (1) transfers this conclusion to the actual chain. A subsequence argument over \(u\in[0,1]\), with the uniform estimate for finite \(z\), shows that the worst-start distance is attained asymptotically by \(x=0\) or \(x=r\) and proves (3). Monotonicity of worst-start distance under the Markov semigroup, together with its values at times a fixed number of steps before/after \(a_N\), establishes cutoff and a bounded window. No claim about a globally convergent continuously shifted profile on integer times is required.

## Verification

Run `python3 verify.py` using only Python's standard library. It enumerates the exact hypergeometric transition kernel in rational arithmetic, propagates finite-state laws, forms the independent-binomial proxy, and checks (1), including its stationary component. The provided check covers 1,680 valid parameter/time configurations. The numerical checks are not a substitute for the infinite-sequence argument; the latter is the proof above.

## Relationship to prior work

Griffin et al. (arXiv:2308.08676v1), Assumption 1.1 and Theorem 1.4, study simultaneous macroscopic swaps with positive limiting red density \(r/N\to\eta>0\), and give mixing-time bounds centered at a multiple of \(\log N\). Their hypotheses exclude the sparse-red regime treated here. Alameda et al. (arXiv:2203.08647) treat positive-fraction swaps with balanced red and white populations. Olesker-Taylor and Schmid (arXiv:2409.07900v1) derive a profile for a different, *single-pair-per-step* Bernoulli–Laplace chain. None of the compared theorems immediately implies the stated uniform finite-time approximation (1) or the \(\log r\)-centered profile (3). Coupling without-replacement samples to Bernoulli variables is classical; the claim of distinctiveness concerns its specified simultaneous-swap quantitative application and resulting sparse-color cutoff, not priority for the elementary coupling method.

## Limitations

The asymptotic result assumes \(r^2\log r=o(N)\), fixed interior urn fraction, and a noncritical limiting single-particle eigenvalue \(0<|\rho_0|<1\). It does not cover denser minorities, vanishing swap fractions, the critical zero-eigenvalue regime, or the parameter-dependent case \(u=h_0,z=\infty\). These statements concern total-variation mixing of the red **count**, not the full labeled-ball permutation chain. The explicit error in (1) can be larger than one for some finite parameters and is then valid but uninformative. Historical priority has not been independently certified.

## References

1. Griffin, T., Hall, B., Hebner, J., Herzog, D., Selyuzhitsky, D., Wong, K., and Wright, J. *Cutoff in the Bernoulli-Laplace Model With Unequal Colors and Urn Sizes*. arXiv:2308.08676v1 (first public 2023-08-16). Sections 1, 3, and 5.
2. Alameda, J. S., Bang, C., Brennan, Z., Herzog, D. P., Kritschgau, J., and Sprangel, E. *Cutoff in the Bernoulli–Laplace model with \(O(n)\) swaps*. arXiv:2203.08647 (first public March 2022). Theorem 1.2.
3. Olesker-Taylor, S. and Schmid, D. *Limit Profile for the Bernoulli–Laplace Urn*. arXiv:2409.07900v1 (first public 2024-09-12). Theorem A, Sections 1–5.
