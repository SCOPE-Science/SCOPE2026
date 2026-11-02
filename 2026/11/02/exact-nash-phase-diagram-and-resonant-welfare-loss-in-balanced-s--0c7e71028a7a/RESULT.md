# Exact Nash phase diagram and resonant welfare loss in balanced signed coalition games

## Finding

Let \(m\ge1\), and let there be \(m\) labeled agents of each of two types. An agent values every agent of the other type at \(+1\) and every other agent of the same type at \(-q\), where \(q>0\). The utility of an agent is the sum of her valuations for other members of her coalition. A partition is Nash-stable when no agent can strictly improve by unilaterally joining another existing coalition or forming a singleton.

**Theorem (complete equilibrium and welfare spectrum).** Every Nash-stable partition consists entirely of *balanced* coalitions, each containing the same positive number of agents of each type. If their common per-type sizes are \(k_1,\dots,k_t\), with \(\sum_{i=1}^t k_i=m\), this condition is also sufficient precisely in the following regimes:

\[
\begin{array}{ll}
0<q<1: &(1-q)(\max_i k_i-\min_i k_i)\le q,\\
q=1: &\text{no further restriction},\\
q>1: &\max_i k_i\le q/(q-1).
\end{array}
\]

For an exact labeled equilibrium count, let \(\mathcal C_m(q)\) be the vectors \((c_1,\ldots,c_m)\) of nonnegative integers satisfying \(\sum_{j=1}^m jc_j=m\), with support \(J=\{j:c_j>0\}\), subject to the corresponding displayed regime (use \(\max J-\min J\) in the first, and \(\max J\) in the third). Then

\[
E_m(q)=(m!)^2\sum_{c\in\mathcal C_m(q)}\prod_{j=1}^m\frac{1}{c_j!(j!)^{2c_j}}.
\]

Write \(S_{\max}\) for maximum utilitarian welfare over all partitions, and \(S_{\min}^{\mathrm{NS}}\) for the minimum over Nash-stable partitions. The sharp values are

\[
\begin{array}{c|cc}
& S_{\max}&S_{\min}^{\mathrm{NS}}\\\hline
0<q<1&2m[q+(1-q)m]&2m\\
q=1&2m&2m\\
q>1&2m&2qm-2(q-1)(tK^2+r^2)
\end{array}
\]

where in the last row \(K=\lfloor q/(q-1)\rfloor\) and \(m=tK+r\), \(0\le r<K\). The price of stability is always \(1\). For \(q<1\), the price of anarchy is \(1+(1-q)(m-1)\); for \(q>1\), it is \(2m/S_{\min}^{\mathrm{NS}}\), with value \(+\infty\) if the denominator vanishes. The denominator vanishes exactly when \(q=k/(k-1)\) for an integer \(k\ge2\) dividing \(m\). For \(m\ge2\), *every* Nash equilibrium is efficient exactly when \(q=1\) or \(q>2\).

## Assumptions and scope

All \(2m\) agents are distinct, all partitions into nonempty coalitions are feasible, there are no size restrictions or vetoes, and strict unilateral improvement is the only admissibility requirement. Coalition labels do not matter. All social-welfare values are sums of individual utilities, with no normalization by coalition size. The preference matrix is symmetric, with each cross-type valuation exactly \(1\) and each within-type valuation exactly \(-q\); the parameter \(q\) is any real number strictly greater than zero. The theorem does not assert core stability or convergence-time bounds.

## Proof

For a coalition \(C\), denote the numbers of type-A and type-B agents by \(a_C,b_C\), and put \(d_C=a_C-b_C\). For an A-agent in \(C\), the current utility is \(b_C-q(a_C-1)\), and the utility after joining another coalition \(D\) is \(b_D-q a_D\). For a B-agent in \(D\), the corresponding current and prospective utilities are \(a_D-q(b_D-1)\) and \(a_C-q b_C\). Suppose \(d_C\ge1\) and \(d_D\le-1\). Both agents exist. If the A-agent moves from \(C\) to \(D\), let her gain be \(g_A\); if the B-agent moves from \(D\) to \(C\), let her gain be \(g_B\). Direct subtraction gives

\[
g_A+g_B=(q+1)(d_C-d_D)-2q\ge2>0.
\]

At least one of these two *individual* deviations is profitable. A Nash-stable partition therefore cannot contain coalitions of opposite nonzero imbalance signs. But \(\sum_C d_C=m-m=0\); if any coalition were unbalanced, positive and negative imbalances would both be present. Hence all coalitions are balanced. An empty-type coalition cannot be balanced unless it is empty, which is excluded.

In a balanced block with \(k\) agents of each type, each agent has utility

\[
u(k)=k-q(k-1)=q+(1-q)k.
\]

Joining a different balanced block of per-type size \(\ell\) gives utility \((1-q)\ell\); forming a singleton gives zero. For \(0<q<1\), all current utilities are positive, and no profitable cross-block move exists if and only if \((1-q)(\max k_i-\min k_i)\le q\). For \(q=1\), the current utility is \(1\) and both alternatives give \(0\). For \(q>1\), a cross-block move gives a negative utility, so Nash stability is equivalent to \(u(k)\ge0\) for every block, namely \(k\le q/(q-1)\). These implications are reversible, proving the equilibrium characterization.

For a specified multiset of per-type sizes with \(c_j\) coalitions of size \((j,j)\), distribute the \(m\) labeled A-agents and the \(m\) labeled B-agents among paired blocks, then divide by \(c_j!\) for each set of indistinguishable blocks of the same size. The resulting count is \((m!)^2/\prod_j c_j!(j!)^{2c_j}\). Summing over exactly the permitted vectors proves the displayed enumeration.

For an arbitrary partition, set \(s_C=a_C+b_C\). Its welfare contribution is

\[
2a_Cb_C-q[a_C(a_C-1)+b_C(b_C-1)]
=q s_C+\frac{1-q}{2}s_C^2-\frac{1+q}{2}d_C^2.
\]

If \(q<1\), summing this identity, using \(\sum_Cs_C=2m\), \(\sum_C s_C^2\le(2m)^2\), and \(\sum_Cd_C^2\ge0\), gives the stated universal upper bound, attained by the grand coalition. If \(q=1\), welfare is \(2m-\sum_Cd_C^2\), so every balanced partition attains the maximum. If \(q>1\), welfare is no greater than its value at \(q=1\), and therefore no greater than \(2m\); a perfect cross-type matching attains equality. Thus these are the unrestricted optima.

Within a balanced partition, welfare simplifies to

\[
S=2qm+2(1-q)\sum_{i=1}^t k_i^2.
\]

For \(q<1\), the minimum among equilibria is achieved by \(m\) balanced pairs, because \(\sum k_i^2\ge m\); the grand coalition is itself Nash-stable and maximizes welfare. For \(q=1\), all stable welfare values equal \(2m\). For \(q>1\), maximize \(\sum k_i^2\) subject to \(1\le k_i\le K\) and \(\sum k_i=m\). Exchanging one unit from a smaller positive part to a larger part whenever the latter has not reached \(K\) strictly increases the sum of squares. Hence a maximizer consists of \(t\) parts of size \(K\) and at most one remainder \(r\), yielding the final formula. A cross-type perfect matching remains stable and efficient for every \(q>0\), proving the price-of-stability claim.

Each stable balanced block contributes \(2k[q-(q-1)k]\) to welfare for \(q>1\), and each contribution is nonnegative. Their sum can vanish exactly when every block has \(k=q/(q-1)\), a positive integer at least \(2\), and consequently that integer divides \(m\). Finally, for \(m\ge2\), at \(0<q<1\) the pair matching has strictly smaller welfare than the grand coalition. At \(1<q\le2\), a balanced block with \(k=2\) and other pairs is stable but has strictly smaller welfare than the pair matching. At \(q>2\), \(K=1\), so all stable partitions consist only of pairs and are optimal. This proves every assertion.

## Verification

The standalone standard-library script `verify.py` independently generates all set partitions for equal type-population sizes \(m=1,2,3,4\) at 16 exact rational values of \(q\), and for \(m=5\) at four additional values. It compares direct agent-by-agent improvement testing to the closed Nash criterion; direct payoff summation to the quadratic welfare identity; and the exact equilibrium count and welfare extremes to the multiset formulas. All 533,660 complete partition/parameter comparisons passed, including 6,215 observed equilibrium incidences. It additionally evaluates exact integer-count formulas for sizes up to \(m=11\). Run `python verify.py` with Python 3.9 or later. Finite computation is supporting evidence only: the proof covers every positive real \(q\) and every positive integer \(m\).

## Relationship to prior work

The model is an explicitly symmetric and two-type instance of the additively separable hedonic games studied by Brandt, Bullinger and Tappe (2022), and of the symmetric games considered by Gairing and Savani (2015/2019). The general potential argument for symmetric games guarantees Nash equilibrium existence, but does not by itself give the balanced-block necessity, exact threshold for each coalition-size profile, labeled count or sharp inefficiency resonances established here. The dichotomous hedonic diversity games studied by Darmann (2023) instead evaluate fractions of types and dichotomous approval, so their results do not imply the present cardinal, total-count payoffs. The symmetric-game potential property is preexisting and is not claimed as new.

## Limitations

The equal population sizes and complete cross-type friendship with uniform within-type hostility are essential to the exact statement. Arbitrary graph edge deletion, unequal population counts, asymmetric valuations, size-normalized utilities, joint deviations, and veto-based stability are outside scope. No claim is made that a finite search establishes literature-wide novelty. Infinite price of anarchy uses the conventional positive-optimum/zero-equilibrium-welfare convention. Independent external validation has not been performed.

## References

1. F. Brandt, M. Bullinger and L. Tappe, *Single-Agent Dynamics in Additively Separable Hedonic Games*, Proceedings of AAAI 36 (2022), 4867–4874. DOI: 10.1609/aaai.v36i5.20415. Public article date: 2022-06-28. https://ojs.aaai.org/index.php/AAAI/article/view/20415
2. F. Brandt, M. Bullinger and L. Tappe, *Stability Based on Single-Agent Deviations in Additively Separable Hedonic Games*, expanded journal manuscript (2024), https://pub.dss.in.tum.de/brandt-research/ashg_unilateral_journal.pdf
3. M. Gairing and R. Savani, *Computing Stable Outcomes in Symmetric Additively Separable Hedonic Games*, arXiv:1509.05322 (2015); Mathematics of Operations Research 44 (2019), 1101–1121. https://arxiv.org/abs/1509.05322
4. A. Darmann, *Stability and Welfare in (Dichotomous) Hedonic Diversity Games*, Theory of Computing Systems 67 (2023), 1133–1155. https://doi.org/10.1007/s00224-023-10138-8
