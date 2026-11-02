# Sharp heavy-item Nash-welfare frontier under two-agent temporal EF1

## Finding

**Theorem (sharp parameterized frontier).** Two agents share identical strictly positive additive valuations for a finite sequence of at least two indivisible goods. Write \(V=\sum_j w_j\), \(h=\max_j w_j\), and \(\delta=h/V\). Let \(P^*\) be the largest possible final two-bundle utility product over all complete allocations, without any fairness or arrival-order restriction. If \(\delta\in[1/2,1)\), then every final EF1 allocation \(A\) satisfies

\[
\frac{\operatorname{NSW}(A)}{\operatorname{NSW}^*}\geq \sqrt{\frac{1+\delta}{4\delta}},\qquad
\operatorname{NSW}(A)=\sqrt{v(A_1)v(A_2)},\quad \operatorname{NSW}^*=\sqrt{P^*}.
\]

For **each fixed** \(\delta\in[1/2,1)\), equality is attainable by a three-good instance and a prefix-wise EF1 allocation. Consequently the same expression is the exact worst-case guarantee of every irrevocable algorithm that is required to maintain EF1 after each prefix, even if it knows the complete future: a least-valued-bundle algorithm achieves the bound, and no deterministic or randomized policy has a stronger guarantee on the class of instances with this fixed \(\delta\).

**Universal corollary.** With no assumption on the largest-good fraction other than strict positivity and at least two goods, every final EF1 allocation, and hence every prefix-wise EF1 allocation, has \(\operatorname{NSW}(A)/\operatorname{NSW}^*>1/\sqrt2\). The factor \(1/\sqrt2\) is the sharp infimum, approached by three-good sequences. For two goods, prefix-wise EF1 gives an offline NSW optimum, so three is the smallest number of goods witnessing a strict loss.

## Assumptions and scope

Goods \(g_1,\ldots,g_m\), \(m\ge2\), have fixed values \(w_j\in\mathbb R_{>0}\) to **both** agents. One good arrives per step, must be assigned to exactly one agent immediately, and cannot later be reassigned. A partial or final allocation is EF1 if, for each ordered pair of agents, removing at most one good from the other agent's bundle eliminates the first agent's envy (an empty other's bundle creates no envy). A trajectory is *prefix-wise EF1* if this holds after every arrival. The offline benchmark \(P^*\) maximizes the product of final bundle sums without a prefix constraint. These assumptions also cover arbitrary real, not only integer, weights.

The parameterized sharpness statement concerns \(1/2\le\delta<1\). The universal corollary covers \(0<\delta<1\), which automatically follows from \(m\ge2\) and strictly positive goods. There is no assertion about heterogeneous agents, chores, goods with zero value, more than two agents, or multiperiod reassignment.

## Proof

**1. Heavy-item upper bound on the offline product.** Normalize only for convenience by retaining the total \(V>0\). Suppose \(h\ge V/2\). Every complete allocation puts a good valued \(h\) into one bundle with sum \(z\ge h\ge V/2\). The other bundle has sum \(V-z\). Since \(z(V-z)\) decreases for \(z\ge V/2\), every offline product is at most

\[
P^*\le h(V-h).
\]

The bound is attained by an allocation that puts the largest good alone in one bundle, if such an allocation is otherwise feasible.

**2. Lower bound on every EF1 product.** Write the final EF1 bundle totals in increasing order \(x\le y\), where \(x+y=V\). If the largest item \(h\) is held in the smaller bundle, then \(V/2\ge x\ge h\ge V/2\), so \(x=y=V/2\). The NSW ratio is then \(1\), larger than the required lower bound.

Otherwise the larger bundle contains \(h\). EF1 from the smaller agent toward the larger bundle implies

\[
x\ge y-h=V-x-h,\qquad\text{hence}\qquad x\ge\frac{V-h}{2}.
\]

Also \(x\le V/2\). On this range, the function \(x(V-x)\) is nondecreasing. Therefore

\[
xy=x(V-x)\ge \frac{V-h}{2}\frac{V+h}{2}=\frac{V^2-h^2}{4}.
\]

Dividing by the bound from Step 1, which is strictly positive because \(m\ge2\) and all item values are positive, yields

\[
\frac{xy}{P^*}\ge\frac{V^2-h^2}{4h(V-h)}
=\frac{V+h}{4h}=\frac{1+\delta}{4\delta}.
\]

Taking square roots proves the parameterized lower bound, including the boundary \(\delta=1/2\).

**3. Tightness simultaneously with temporal EF1.** For any prescribed \(1/2\le\delta<1\) choose \(V=1\), \(h=\delta\), and \(q=(1-\delta)/2>0\). Release precisely the three goods in order \((q,q,h)\). At the second prefix, EF1 forces the two \(q\)-goods into different agents' bundles: placing both in one bundle would leave a positive value after deleting either one, while the other agent has value zero. Whichever agent receives the last good, the final totals are \((q,q+h)\), a prefix-wise EF1 outcome: removing \(h\) from the richer bundle leaves \(q\).

The offline optimal partition separates the largest good from the two smaller goods, so

\[
P^*=h(2q)=h(1-h),\qquad xy=q(q+h),\qquad
\frac{xy}{P^*}=\frac{1+h}{4h}.
\]

This is equality for every allowed \(\delta\), for *every* prefix-wise EF1 decision path on the constructed three-good input. Randomization or advance knowledge cannot change its final product. Conversely, allocating each arriving good to a currently least-valued bundle preserves prefix-wise EF1: the newly receiving bundle was no larger before the step, so deleting the just-arrived good resolves any new envy toward it; other EF1 relations persist. Thus a feasible online policy exists and the minimax ratio is exactly the stated formula.

**4. Full-range universal guarantee and minimum obstruction.** If instead \(h<V/2\), let \(c\) be the largest good in the larger final bundle. The EF1 inequality implies \(x\ge(V-c)/2\ge(V-h)/2\). Hence

\[
xy\ge\frac{V^2-h^2}{4},\qquad P^*\le\frac{V^2}{4},\qquad
\frac{xy}{P^*}\ge1-\delta^2>\frac34.
\]

For \(\delta\ge1/2\), the sharp curve from Step 2 gives \((1+\delta)/(4\delta)>1/2\) because \(\delta<1\). Thus every finite admissible instance has NSW ratio strictly larger than \(1/\sqrt2\), while the sharp family above approaches it as \(\delta\uparrow1\). With exactly two positive goods, EF1 after the second arrival forces a split; that also maximizes final product, since the unsplit alternatives have zero product. This proves the universal sharp infimum and smallest strict-loss horizon.

## Verification

The standalone standard-library checker `verify.py` independently enumerates all allocations of sequences of length \(2\) through \(7\) with good values in \(\{1,2,3,4\}\), compares with the exact offline optimum, checks both universal and heavy-item inequalities for **all** EF1 final allocations, verifies every least-loaded-prefix update, and checks a three-item equality family. Execute with `python3 verify.py` from the extracted package. The actual run returned 21,840 instances, 1,040,454 final-EF1 allocations, 470 heavy-item tests, 254,528 prefix-wise EF1 allocations, and 199 sharp examples, without failure. This finite check is not a substitute for the proof of the real-parameter statement.

## Relationship to prior work

Barman, Krishnamurthy and Vaish (2018) give the population-uniform \(e^{-1/e}\) NSW lower bound for arbitrary EF1 allocations with identical additive valuations. Feng, Hu and Li (2026) revisit this same general EF1 gap. Yang et al. (2026) establish a small-item improvement and prefix-wise EF1 feasibility, and exhibit a separate five-good illustration of temporal efficiency loss; their small-item hypothesis applies when \(h/V\le1/2\), whereas the exact nontrivial portion of the present sharp heavy-item curve treats \(h/V>1/2\). Elkind et al. (2024/2025) establish temporal EF1 feasibility for generalized binary valuations and study existence and computational complexity, without providing this identical two-agent, largest-item-dependent Nash-welfare frontier. Thus the contribution is the **sharp, continuous heavy-item parameterization and forced three-good temporal welfare price**, not the feasibility of least-valued-bundle assignment or the previously known universal coarse bound. The endpoint \(\delta=1/2\) agrees with the earlier small-item inequality.

## Limitations

No claim of uniqueness of the minimizing allocation or of the extremal sequence is made. The bound is minimax sharp as a function of \(\delta\) only in the dominant-good regime \(\delta\ge1/2\); Step 4 is a valid, generally not asserted sharp, estimate for the smaller-good regime. A different order of the same three goods can permit better temporal welfare. The theorem compares against offline final NSW, not average welfare over prefixes. The proof has not undergone independent audit. Exhaustive finite experiments cannot eliminate equivalent unindexed prior literature.

## References

- S. Barman, S. K. Krishnamurthy, and R. Vaish, *Finding Fair and Efficient Allocations*, 2018; arXiv:1707.04731. https://arxiv.org/abs/1707.04731
- E. Elkind, A. Lam, M. Latifian, T. Y. Neoh, and N. Teh, *Temporal Fair Division of Indivisible Items*, arXiv:2410.14593 (first released 2024-10-18; AAMAS 2025). https://arxiv.org/abs/2410.14593
- Y. Feng, W. Hu, and S. Li, *New Convex Programming Technique for Nash Social Welfare and Scheduling*, ICALP 2026. https://doi.org/10.4230/LIPIcs.ICALP.2026.90
- Z.-S. Yang et al., *EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments*, first released 2026-09-03; arXiv:2609.03846. https://arxiv.org/abs/2609.03846
