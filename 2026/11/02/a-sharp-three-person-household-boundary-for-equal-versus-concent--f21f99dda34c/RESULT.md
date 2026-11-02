# A sharp three-person household boundary for equal versus concentrated vaccination

## Finding

Consider two independent, equally sized households, each initially containing three vaccine-eligible people. Exactly two perfect prophylactic doses are available. Each unvaccinated person independently receives an external infectious introduction with probability \(q\). Conditional on these introductions, an epidemic follows a Reed–Frost process: every infectious person independently attempts transmission to each remaining susceptible in the same household, with probability \(p\), and is thereafter removed. There is no between-household transmission. Assume \(0<p<1\) and \(0<q<1\). The objective is to **minimize the expected total number of people ever infected**, including initial introductions.

Let \(B\) denote one dose in each household and \(C\) denote both doses in a single household. Write \(I_B\) and \(I_C\) for their expected total infections. The exact difference is

\[
I_B-I_C=pq(q-1)\left[2+6p-6p^2-q(9p-6p^2)\right].
\]

If \(p\le 2/3\), the balanced policy \(B\) is the unique optimum (up to household exchange). If \(p>2/3\), define

\[
q_c(p)=\frac{2+6p-6p^2}{9p-6p^2}.
\]

Then \(0<q_c(p)<1\); \(B\) is uniquely optimal for \(q<q_c(p)\), the policies tie at \(q=q_c(p)\), and the concentrated policy \(C\) is uniquely optimal for \(q>q_c(p)\), modulo exchange of household labels.

Three is the smallest household size for which this concentration advantage can occur with two doses. More generally, for **any** equal household size \(n\ge3\), let \(F_n(p,q)\) be the expected total infections in a household with \(n\) unvaccinated people, and set \(F_0=0\). For the two-dose comparison define

\[
D_n(p,q)=2F_{n-1}(p,q)-F_{n-2}(p,q)-F_n(p,q).
\]

For fixed \(n\ge3\) and \(0<p<1\), as \(q\uparrow1\),

\[
D_n(p,q)=p(1-p)^{n-3}(np-2)(1-q)+O((1-q)^2).
\]

Consequently, whenever \(np>2\), concentration strictly beats balancing for every \(q<1\) sufficiently close to one; whenever \(np<2\), balancing strictly beats concentration for every \(q<1\) sufficiently close to one. No sign at the boundary \(np=2\) is claimed by this asymptotic formula.

## Assumptions and scope

The infection mechanism is the finite **independent-directed-contact** Reed–Frost law, with pairwise transmission probability \(p\) not renormalized when household size changes. One may pregenerate a directed edge \(i\to j\) with probability \(p\) independently for every ordered pair of distinct unvaccinated people. The ultimately infected set is the set of vertices reachable along directed edges from initial Bernoulli-\(q\) seeds. Vaccinees are fully immune and removed from both the seeding and transmission graph. Households are independent and have the same parameters. All comparisons are of unconditional expected *cases* rather than reproduction numbers, probability of a major outbreak, or economic costs.

There are exactly two feasible dose-distribution types for household size at least two: \((1,1)\) and \((2,0)\), counting doses by household, up to exchanging household labels. Because individuals within a household are exchangeable, these exhaust all vaccination assignments relevant to the objective.

## Proof

Write \(r=1-q\) and \(x=1-p\). For any unvaccinated individual, let \(K\) be the size of the set of vertices, including that individual, from which a directed path leads to the individual (its incoming susceptibility/ancestor set). The individual escapes infection if and only if **all** \(K\) members were unseeded. Hence

\[
F_n(p,q)=n\left(1-\mathbb E[r^K]\right).
\]

For \(n=1\), \(F_1=q\). For \(n=2\), an individual's ancestor-set size is one with probability \(x\) and two with probability \(p\). Therefore

\[
F_2=2\left(1-xr-pr^2\right)=2\left(q+pq(1-q)\right).
\]

For \(n=3\), \(K=1\) precisely when both incoming direct edges are absent, with probability \(x^2\). The event \(K=2\) means exactly one other vertex reaches the tagged individual. For a prescribed such vertex, its edge to the tagged individual must be present and both edges from the remaining outsider into that two-vertex ancestor set must be absent, an event of probability \(px^2\). There are two choices of prescribed ancestor, hence \(\Pr(K=2)=2px^2\). The complementary probability is \(\Pr(K=3)=p^2(3-2p)\). Thus

\[
F_3=3\left[1-x^2r-2px^2r^2-p^2(3-2p)r^3\right].
\]

Substitute into \(I_B=2F_2\), \(I_C=F_1+F_3\) and collect powers to obtain the stated exact factorization of \(I_B-I_C\). Since \(pq(q-1)<0\), balancing is better exactly when

\[
2+6p-6p^2-q(9p-6p^2)>0.
\]

This affine expression strictly decreases with \(q\) because \(9p-6p^2>0\). Its value at \(q=0\) is positive and its value at \(q=1\) is \(2-3p\). It therefore has an interior zero exactly when \(p>2/3\), proving the complete two-policy classification and equality case.

For size two, concentration leaves a household with two unvaccinated people and the other with none, whereas balancing leaves one in each. The exact difference is

\[
D_2=2F_1-F_0-F_2=-2pq(1-q)<0.
\]

Thus at size two the balanced policy is always better, while at size three the strictly concentrated region just established is nonempty. This proves minimality.

For general \(n\), the tagged individual's incoming ancestor set has size one exactly when none of the \(n-1\) other members has a direct edge into the tagged individual, an event of probability \(x^{n-1}\). All other terms in \(\mathbb E[r^K]\) are of order \(r^2\). Since the household is finite, the expectation is a polynomial in \(r\) and this expansion is exact to first order:

\[
F_n=n-nx^{n-1}r+O(r^2).
\]

Subtract the corresponding formulas at sizes \(n-2,n-1,n\), where \(n\ge3\), to get

\[
\begin{aligned}
D_n&=r\left[-2(n-1)x^{n-2}+(n-2)x^{n-3}+nx^{n-1}\right]+O(r^2)\\
&=p x^{n-3}(np-2)r+O(r^2).
\end{aligned}
\]

Because \(p>0\), \(x>0\), and the coefficient is nonzero when \(np\ne2\), its sign fixes the optimal policy for sufficiently small positive \(r\). This completes the proof.

## Verification

Run `python checker.py` using Python 3 and SymPy. The checker verifies the central two-policy polynomial identity and boundary algebra, then independently enumerates every directed transmission graph and seed subset for three or fewer unvaccinated members at 49 exact-rational parameter pairs (147 expectations). It also verifies the symbolic leading-coefficient identity for 28 household sizes and two exact witnesses. The analytic proof above establishes the full continuum in \(p,q\); the finite enumerations are supplementary checks, **not** a substitute for that proof.

At \(p=9/10\), the sharp transition is \(q_c=127/162\). At \(q=1/2\), the balanced policy has \(I_B=29/10\), compared with \(I_C=3107/1000\), saving \(207/1000\) expected cases. At \(q=9/10\), the concentrated policy has \(I_C=486693/125000\), compared with \(I_B=981/250\), saving \(3807/125000\) expected cases.

## Relationship to prior work

Becker and Starczak (1997) and Ball, Lyne and collaborators (2002, 2004) study optimizing vaccination against epidemic thresholds in household-structured populations. The distinction between threshold minimization and unconditional *finite-household* expected case minimization matters: neither the household largest-susceptible-first heuristic nor a deterministic final-size limit determines the exact two-dose comparison under independent per-person introductions here.

Keeling and Shattock (available online March 7, 2012) analyze final-size vaccine allocation in large noninteracting communities. Their discussion explicitly contrasts that deterministic setting with stochastic household vaccination. The present result gives a distinct finite Reed–Frost statement: a complete sharp \((p,q)\) allocation boundary at the smallest household size where concentration can beat equal allocation, and a structural high-introduction sign law for all sizes.

The general susceptible-ancestor-set method is classical; no novelty is claimed for it or for the Reed–Frost construction itself.

## Limitations

There is no between-household transmission, vaccine failure, heterogeneous mixing, temporal importation following epidemic onset, stochastic vaccine supply, or fairness constraint. Independent Bernoulli seeding is imposed at the beginning, before within-household spread. The objective values expected infections, not severity, death, vaccination equity, resource cost, or reduction of the household reproduction number. The high-introduction statement is asymptotic for \(q\) near one; for \(n\ge4\) it does not classify the whole \((p,q)\)-plane. At \(np=2\) it makes no optimality assertion. The resulting recommendation is a mathematical comparison inside the stated idealized mechanism, not a public-health prescribing rule.

Historical priority may be affected by inaccessible detailed household-allocation literature; exact algebra and value do not establish independent priority.

## References

1. Becker, N. G., and Starczak, D. N. (1997), “Optimal vaccination strategies for a community of households,” *Mathematical Biosciences* **139**, 117–132. https://doi.org/10.1016/S0025-5564(96)00139-3
2. Ball, F. G., and Lyne, O. D. (2002), “Optimal vaccination policies for stochastic epidemics among a population of households,” *Mathematical Biosciences* **177–178**, 333–354. https://doi.org/10.1016/S0025-5564(01)00095-5
3. Ball, F. G., Britton, T., and Lyne, O. D. (2004), “Stochastic multitype epidemics in a community of households: estimation and form of optimal vaccination schemes,” *Mathematical Biosciences* **191**, 19–40. https://doi.org/10.1016/j.mbs.2004.05.001
4. Keeling, M. J., and Shattock, A. (2012), “Optimal but unequitable prophylactic distribution of vaccine,” *Epidemics* **4**, 78–85; first available online 2012-03-07. https://doi.org/10.1016/j.epidem.2012.03.001
5. Ball, F. G. (2018), “Susceptibility Sets and the Final Outcome of Collective Reed–Frost Epidemics,” *Methodology and Computing in Applied Probability*. https://doi.org/10.1007/s11009-018-9631-6
