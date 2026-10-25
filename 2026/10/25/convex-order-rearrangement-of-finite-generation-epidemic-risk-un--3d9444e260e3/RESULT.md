# Convex-order rearrangement of finite-generation epidemic risk under temporary transmission controls

## Finding

**Theorem (finite-horizon transmission-order rearrangement).** Let \(h\ge2\) be an integer and let \(K\) be a nonnegative integer-valued random variable with \(0<m=\mathbb E K<\infty\) and \(\mathbb E K^2<\infty\). In a generation-based early-epidemic branching approximation, every infected individual has an independent copy of \(K\) potential transmissions; during generation \(j\), each potential transmission succeeds independently with probability \(p_j\in(0,1]\). All potential-contact counts and success indicators are independent across individuals and generations. Starting from one infected individual \(Z_0=1\), write \(Z_h(p_1,\ldots,p_h)\) for the number of **new infections in generation \(h\)**, not the cumulative outbreak size.

For any multiset of \(h\) permitted transmission levels, denote its nondecreasing and nonincreasing arrangements by \(p^\uparrow\) and \(p^\downarrow\). Every permutation \(\pi\) satisfies the *convex-order sandwich*

\[
Z_h(p^\downarrow)\ \le_{\mathrm{cx}}\ Z_h(p_{\pi(1)},\ldots,p_{\pi(h)})\ \le_{\mathrm{cx}}\ Z_h(p^\uparrow).
\]

Here \(X\le_{\mathrm{cx}}Y\) means \(\mathbb E\phi(X)\le\mathbb E\phi(Y)\) for every convex real function \(\phi\) for which the expectations exist. The common mean is

\[
\mathbb E Z_h=m^h\prod_{j=1}^h p_j.
\]

Consequently, **applying the lowest transmission levels earliest maximizes finite-horizon elimination probability and all convex terminal-risk functionals**, including variance and stop-loss expectations \(\mathbb E(Z_h-t)_+\); applying them latest minimizes these quantities. This is a *dispersion* comparison, not first-order stochastic dominance or a ranking of cumulative incidence. If \(\mathbb P(K\ge2)>0\), and the multiset has at least two different levels, the extreme arrangements have strictly different elimination probabilities and variances. Conversely, if \(\mathbb P(K\ge2)=0\), every ordering produces the same terminal distribution.

For an adjacent swap of \(0<p<q\le1\) in positions \(i,i+1\), write \(Z_h^{p,q}\) for the order with \(p\) first and \(Z_h^{q,p}\) for the reversed order, with every other level fixed. Put \(c_2=\mathbb E[K(K-1)]\). Then the **exact variance increment** is

\[
\operatorname{Var}(Z_h^{p,q})-\operatorname{Var}(Z_h^{q,p})
=\mathbb E[Z_{i-1}]\,m p q(q-p)c_2
 \prod_{j=i+2}^{h}(mp_j)^2\ge0.
\]

The empty product equals one. The inequality is strict if \(c_2>0\), since all transmission probabilities are positive.

## Assumptions and scope

The model is a *single-type, time-varying Galton–Watson early-epidemic approximation* on an effectively undepleted susceptible pool. Each generation shares the same potential-contact law \(K\), and temporary measures change only the edge-success probability \(p_j\) (for example short-lived contact restrictions or temporary protection). They do not alter the distribution of potential contacts, induce dependence between transmissions, or accumulate irrevocably as vaccinated fractions. The list of transmission levels is fixed; only its chronology is optimized. All comparisons concern **generation-\(h\) incidence**, not summed cases, duration, a finite susceptible network, or an unconstrained intervention budget.

Convex order and the elimination result hold under the stated finite-second-moment assumptions. The finite second moment is used to state variance; convex-order comparisons can be extended when only the first moment is finite by truncation, but that extension is not claimed here.

## Proof

**1. A two-stage offspring comparison.** Fix \(0<p\le q\le1\). Expose in advance a potential first-generation count \(K_0=k\) and independent potential second-generation counts \(K_1,\ldots,K_k\). For each potential child \(r\), its contribution to the second generation is distributed, conditional on \(K_r=\ell\), as

\[
U_{\ell}=B_p\operatorname{Bin}(\ell,q)
\quad\text{in the order }(p,q),\qquad
V_{\ell}=B_q\operatorname{Bin}(\ell,p)
\quad\text{in the order }(q,p),
\]

where each Bernoulli variable, each binomial count, and each potential-contact count is independent within its respective model. Both contributions have conditional mean \(pq\ell\).

For any convex test function \(\phi\), let \(g_\ell(t)=\mathbb E\phi(\operatorname{Bin}(\ell,t))\). The Bernstein-polynomial identity gives

\[
g_\ell''(t)=\ell(\ell-1)\mathbb E[\phi(J+2)-2\phi(J+1)+\phi(J)],
\quad J\sim\operatorname{Bin}(\ell-2,t),
\]

for \(\ell\ge2\); for \(\ell<2\), \(g_\ell\) is affine. Thus \(g_\ell\) is convex on \([0,1]\), and its secant slope from zero is nondecreasing. Therefore

\[
\mathbb E\phi(U_\ell)-\mathbb E\phi(V_\ell)
=p[g_\ell(q)-g_\ell(0)]-q[g_\ell(p)-g_\ell(0)]\ge0.
\]

Together with equal conditional means, this proves \(V_\ell\le_{\mathrm{cx}}U_\ell\). Independent sums preserve convex order, so conditional on \(K_0,K_1,\ldots,K_{K_0}\), the total second-generation population after \((p,q)\) dominates that after \((q,p)\) in convex order, with equal means. Averaging over the potential counts preserves the same conclusion. Starting with any deterministic number of infected individuals is handled by another independent-sum argument.

**2. Convex-order preservation after the swap.** If an offspring variable \(Y\ge0\) is integer-valued and \(\phi\) is convex, then

\[
\psi(n)=\mathbb E\phi(Y_1+\cdots+Y_n),\qquad n\in\mathbb N_0,
\]

is convex on the nonnegative integers. Indeed, conditioning on \(S_n=Y_1+\cdots+Y_n\), its second difference is the expectation of

\[
\phi(S_n+Y+Y')-\phi(S_n+Y)-\phi(S_n+Y')+\phi(S_n)\ge0,
\]

by monotonicity of increments of a convex function and \(Y,Y'\ge0\). Therefore a common later branching transition preserves convex order. The earlier generations have identical laws in the two arrangements. Combining this fact with Step 1 proves that swapping an adjacent \(p<q\) into chronological order \((p,q)\) increases the final population in convex order. Repeated adjacent swaps give the claimed extreme ordering for all \(h\).

**3. Mean and exact variance gap.** Let \(v=\operatorname{Var}(K)\). A thinned offspring variable has mean \(mp\) and variance

\[
V(p)=mp+p^2(v-m).
\]

From a single ancestor the two-stage variances are \((mq)^2V(p)+(mp)V(q)\) and \((mp)^2V(q)+(mq)V(p)\). Subtraction yields

\[
\Delta V_2=mpq(q-p)(m^2+v-m)=mpq(q-p)c_2.
\]

If the incoming population has mean \(a\), conditioning on that count multiplies the variance difference by \(a\), because the two orderings have equal conditional means \(m^2pq\) per ancestor. Every common subsequent generation with offspring mean \(mp_j\) multiplies an existing variance difference by \((mp_j)^2\), since the two models continue to have the same mean. This proves the displayed exact formula. The mean expression follows by multiplying mean reproduction factors \(mp_j\).

**4. Sharp strictness and nonbranching boundary.** Write \(G(s)=\mathbb E s^K\) and \(F_p(s)=G(1-p+ps)\), the one-generation probability-generating function. Put \(z=1-s>0\), and \(H(t)=(1-G(1-t))/t\). Since \(G\) is convex, \(H\) is nonincreasing for \(t>0\) and strictly decreasing if \(\mathbb P(K\ge2)>0\). For \(0<p<q\), the arguments of the outer \(G\) in \(F_p(F_q(s))\) and \(F_q(F_p(s))\) differ by

\[
pqz\bigl[H(pz)-H(qz)\bigr]>0.
\]

The function \(G\) is strictly increasing on \((0,1]\) when \(m>0\), hence \(F_p(F_q(s))>F_q(F_p(s))\) for \(0\le s<1\). Composition with the positive-transmission prefix and suffix retains strict inequality when evaluated at the extinction argument \(s=0\): the suffix composition gives an argument strictly below one, and the prefix is strictly increasing. Thus each genuine inversion changes terminal elimination probability strictly; the variance formula shows strict variance change as well.

When \(c_2=0\), necessarily \(K\in\{0,1\}\) almost surely; then \(G\) is affine and all \(F_p\) commute, so the entire terminal law is permutation-invariant. This proves necessity and sufficiency of genuine branching for chronology dependence.

## Verification

For a concrete binary potential-contact law \(K\equiv2\), take \(p=1/4\), \(q=3/4\), and horizon \(h=2\). Both orders have mean \(3/4\), but

\[
\mathbb P(Z_2^{p,q}=0)=\frac{2401}{4096},\qquad
\mathbb P(Z_2^{q,p}=0)=\frac{1849}{4096},\qquad
\operatorname{Var}(Z_2^{p,q})-\operatorname{Var}(Z_2^{q,p})=\frac38.
\]

These fractions follow by direct composition of \(F_p(s)=(1-p+ps)^2\) and \(F_q\). The standalone `verify.py` script uses only Python's standard library and exact `Fraction` arithmetic. Run `python verify.py` from the extracted package directory. It checks 1,680 exact-rational assertions: offspring and population normalization, equality of means across all orderings of three levels, integer stop-loss inequalities for six finite-support potential-contact laws, exact adjacent-swap variance identities, strict elimination where branching is possible, the nonbranching boundary, and the displayed benchmark. Since the distributions in these tests have finite integer support, the stop-loss checks are exhaustive for the listed cases; they do not prove the universal theorem.

## Relationship to prior work

Boudreau, Allen, Roberts, Allard, and Hébert-Dufresne (first public preprint 2023-02-07) develop generation-dependent epidemic probability-generating functions to compare temporal intervention forecasts and cumulative incidence. Their full available text gives the recursion and numerical policy comparisons but not a convex-order permutation theorem for the final generation with fixed multiset of transmissibility levels. The present theorem specializes to a fixed potential-contact law with successive independent thinning, and provides an exact order rule and variance swap identity.

Bertacchi, Rodriguez, and Zucca (2016) and Kersting (2017 preprint; 2020 journal) study general branching processes in varying environments, especially eventual survival and asymptotic behavior. Their stated survival criteria and limit theorems do not compare all permutations of a finite thinned-offspring schedule in convex order. Standard branching-process PGF composition alone gives exact distributions, but does not state the inequality or its sharp equality boundary. The result is compatible with general convex-order theory; possible equivalent reorderings in broader stochastic-order literature remain a priority risk.

## Limitations

The generation-dependent control is transient and can be permuted; irreversible vaccine rollout proportions cannot generally be reordered arbitrarily. The result compares terminal generation size and elimination by a fixed generation, **not cumulative infections**, instantaneous disease prevalence in calendar time, infection-timing distributions, finite-network depletion, targeted interventions changing the potential-offspring law, or feedback policies. Convex order does not give a fixed sign for every tail exceedance probability. Neither comparative costs nor feasibility of intervention timing are modeled. Strictness requires positive transmission in each generation, at least two distinct levels, and positive chance of at least two potential secondary cases. The literature comparison was extensive but not a proof of publication priority.

## References

1. M. C. Boudreau, A. J. Allen, N. J. Roberts, A. Allard, L. Hébert-Dufresne, *Temporal and probabilistic comparisons of epidemic interventions*, arXiv:2302.03210 (first version 2023-02-07), https://arxiv.org/abs/2302.03210.
2. D. Bertacchi, P. M. Rodriguez, F. Zucca, *Galton-Watson processes in varying environment and accessibility percolation*, arXiv:1611.03286 (first version 2016-11-10), https://arxiv.org/abs/1611.03286.
3. G. Kersting, *A unifying approach to branching processes in a varying environment*, arXiv:1703.01960 (first version 2017-03-06), *Journal of Applied Probability* 57 (2020), 196–220, https://doi.org/10.1017/jpr.2019.84.
