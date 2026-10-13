# A universal short-time obstruction makes a decreasing-past-extropy characterization vacuous
## Finding
For any nonnegative absolutely continuous random variable \(Z\) whose past extropy is finite and well-defined for every \(t>0\),
\[
\bar J(Z;t)=-\frac12\int_0^t\left(\frac{f_Z(x)}{F_Z(t)}\right)^2\,dx
\]
satisfies the universal bound
\[
\bar J(Z;t)\le -\frac1{2t}.
\]
Therefore
\[
\bar J(Z;t)\longrightarrow-\infty\qquad(t\downarrow0),
\]
and \(t\mapsto\bar J(Z;t)\) cannot be nonincreasing on all of \((0,\infty)\).

Theorem 2.9 of Alrewely, Kayid, Alarfaj, and Balakrishnan assumes that the past extropies of two linear consecutive \(r\)-out-of-\(n\):F system lifetimes are well-defined and decreasing on \((0,\infty)\). Under the paper's convention that “decreasing” means nonincreasing, the universal bound above makes this premise impossible. Hence the characterization theorem has an empty admissible hypothesis class and is vacuous as stated.

## Assumptions and scope
Let \(Z\) have density \(f_Z\) and cdf \(F_Z\). For every \(t>0\), assume \(F_Z(t)>0\) and
\[
\int_0^t\left(\frac{f_Z(x)}{F_Z(t)}\right)^2\,dx<\infty.
\]
These are exactly the conditions needed for finite past extropy at every positive inspection time. No smoothness, stochastic-order, aging, or consecutive-system assumption is required for the obstruction.

The conclusion applies in particular to any absolutely continuous consecutive-system lifetime \(T_{r\mid n:F}\) whenever its past extropy is well-defined for all \(t>0\).

## Proof
For fixed \(t>0\), the conditional density
\[
g_t(x)=\frac{f_Z(x)}{F_Z(t)},\qquad 0<x<t,
\]
integrates to one. Cauchy–Schwarz on the interval \((0,t)\) gives
\[
1=\left(\int_0^t g_t(x)\,dx\right)^2
\le t\int_0^t g_t(x)^2\,dx.
\]
Thus
\[
\int_0^t g_t(x)^2\,dx\ge\frac1t,
\]
and multiplication by \(-1/2\) reverses the inequality:
\[
\bar J(Z;t)=-\frac12\int_0^t g_t(x)^2\,dx
\le -\frac1{2t}.
\]
As \(t\downarrow0\), the right-hand side tends to \(-\infty\), so \(\bar J(Z;t)\to-\infty\).

Now fix any \(t_0>0\). If \(\bar J(Z;\cdot)\) were nonincreasing on \((0,\infty)\), then for every \(0<s<t_0\),
\[
\bar J(Z;s)\ge\bar J(Z;t_0).
\]
But the short-time divergence gives \(\bar J(Z;s)<\bar J(Z;t_0)\) for all sufficiently small \(s\), a contradiction.

The 2026 source explicitly states Theorem 2.9 with past extropies “well-defined and decreasing on \((0,\infty)\),” after declaring that increasing and decreasing are used in the non-strict sense. Therefore its monotonicity premise cannot hold for any finite past-extropy law in the stated domain.

## Verification
The proof is symbolic and requires no numerical or finite experiment. The critical checks are:

1. \(g_t\) is a probability density on an interval of length \(t\).
2. Cauchy–Schwarz yields the sharp \(L^2\) lower bound \(\int_0^t g_t^2\ge1/t\).
3. The negative sign in the extropy definition gives \(\bar J(Z;t)\le-1/(2t)\).
4. The source's theorem assumes finite, globally nonincreasing past extropy on all positive times, which contradicts the forced limit \(-\infty\) at the left endpoint.

The argument remains valid for every absolutely continuous system lifetime, independent of the specific consecutive-system cdf formula.

## Relationship to prior work
Alrewely, Kayid, Alarfaj, and Balakrishnan (2026) develop past extropy for linear consecutive \(r\)-out-of-\(n\):F systems. Their Theorem 2.9 is a distributional characterization requiring the relevant past-extropy functions to be well-defined and decreasing on \((0,\infty)\). Their paper also records the opposite, increasing behavior under a decreasing reversed-failure-rate condition.

Earlier work by Kayid and Alshehri (2023) likewise studies past extropy of coherent systems and proves increasing behavior for decreasing reversed-hazard-rate models. Toomaj, Hashempour, and Balakrishnan (2023) study dynamic extropy and related aging properties. These sources establish the surrounding monotonicity framework, but the inspected material does not state the universal short-time obstruction above or identify the 2026 characterization hypothesis as empty.

Focused database and literature searches for the exact theorem, dynamic-past-extropy lower bounds, Cauchy–Schwarz formulations, and corrigenda did not locate a covering statement.

## Limitations
The finding invalidates the global decreasing premise used by Theorem 2.9; it does not assert that every local characterization on an interval bounded away from zero is impossible. Nor does it provide a replacement characterization for the increasing case, where the quadratic relation between reversed hazard and past extropy can have two positive branches.

The originality assessment cannot exclude an unindexed note, corrigendum, or equivalent observation stated under different terminology.

## References
1. F. Alrewely, M. Kayid, B. Alarfaj, and N. Balakrishnan, “Past extropy for linear consecutive r-out-of-n: F systems and its properties, bounds, and estimation,” AIMS Mathematics 11 (2026), 10342–10371. DOI: 10.3934/math.2026427.
2. M. Kayid and M. A. Alshehri, “System Level Extropy of the Past Life of a Coherent System,” Journal of Mathematics (2023), Article 9912509. DOI: 10.1155/2023/9912509.
3. A. Toomaj, M. Hashempour, and N. Balakrishnan, “Extropy: Characterizations and dynamic versions,” Journal of Applied Probability 60 (2023), 1333–1351. DOI: 10.1017/jpr.2023.7.
