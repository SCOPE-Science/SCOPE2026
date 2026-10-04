# Exact square-root error budgeting for normal-mixture union confidence sequences
## Finding
For the normal-mixture boundary used in arm-wise anytime-valid inference,
\[
b(V;a)=\sqrt{(V+\eta^{{-2}})\log\!\left(\frac{{1+\eta^2V}}{{a^2}}\right)},
\]
consider \(m\ge 2\) arm-level boundaries combined by a union bound. Fix \(\eta>0\), a total error budget \(0<\alpha<e^{{-1/2}}\), and deterministic target clocks \(V_i\ge0\). Write
\[
s_i=\sqrt{{V_i+\eta^{{-2}}}},\qquad S=\sum_{{i=1}}^m s_i.
\]
Among all positive deterministic allocations \(a_i\) satisfying \(\sum_i a_i=\alpha\), the total half-width
\[
W(a_1,\ldots,a_m)=\sum_{{i=1}}^m b(V_i;a_i)
\]
has the unique minimizer
\[
a_i^*=\alpha\frac{{s_i}}{{S}}
=\alpha\frac{{\sqrt{{V_i+\eta^{{-2}}}}}}{{\sum_j\sqrt{{V_j+\eta^{{-2}}}}}},
\]
and the exact minimum is
\[
W^*=S\sqrt{{\log\!\left(\frac{{\eta^2S^2}}{{\alpha^2}}\right)}}.
\]
For two arms this says that the equal split \(a_0=a_1=\alpha/2\) is target-clock optimal if and only if \(V_0=V_1\). A larger target clock receives a strictly larger share of the error budget.

For the delayed-outcome construction of Lindon and Kallus, replacing \(\alpha/2,\alpha/2\) by any fixed positive split \(a_0,a_1\) with \(a_0+a_1=\alpha\) preserves the same asymptotic union-bound coverage argument. Consequently, a split selected before observing the experiment can be tuned to deterministic design targets. If \(V_i(t)=t v_i+o(t)\) with \(v_i>0\), the exact optimizer for the deterministic target clocks satisfies
\[
a_i^*(t)\longrightarrow \alpha\frac{{\sqrt{{v_i}}}}{{\sum_j\sqrt{{v_j}}}}.
\]
Let \(q_i=\sqrt{{v_i}}/\sum_j\sqrt{{v_j}}\) and let \(u_i=1/m\). Then the equal split has the second-order excess
\[
W_{{\mathrm{{eq}}}}(t)-W^*(t)
=\frac{{\sqrt t}}{{\sqrt{{\log t}}}}
\left(\sum_i\sqrt{{v_i}}\right)D(q\|u)
+o\!\left(\sqrt{{\frac{{t}}{{\log t}}}}\right),
\]
where \(D(q\|u)=\sum_i q_i\log(mq_i)=\log m-H(q)\). Thus the equal split loses nothing at this order only in the clock-balanced case.

## Assumptions and scope
The allocation theorem is deterministic: \(V_i\) are target clock values, not random plug-in estimates selected after looking at the experiment. The condition \(\alpha<e^{{-1/2}}\) ensures strict convexity throughout the feasible region; it includes conventional confidence levels such as \(\alpha=0.10,0.05,0.01\). The arm-level boundary parameter \(\eta\) is common across the terms.

In the delayed-outcome application, the coverage statement applies to an allocation fixed independently of the experiment, for example from a prespecified design target or external historical information. This finding does not justify choosing \(a_i\) after observing the random plug-in clocks \(\hat V_t(i)\), and it does not claim that a single fixed split is width-optimal at every calendar time when the clock ratio changes.

## Proof
Set \(z_i=a_i/s_i\) and define
\[
\phi(z)=\sqrt{{\log(\eta^2/z^2)}}.
\]
Because \(s_i\ge\eta^{{-1}}\) and \(a_i<\alpha<e^{{-1/2}}\), every feasible \(z_i\) satisfies \(z_i<\eta e^{{-1/2}}\). On this region, if \(L(z)=\log(\eta^2/z^2)\), then \(L(z)>1\) and
\[
\phi''(z)=\frac{{L(z)-1}}{{z^2L(z)^{{3/2}}}}>0.
\]
Moreover,
\[
b(V_i;a_i)=s_i\phi(z_i),
\qquad
\sum_i s_i z_i=\sum_i a_i=\alpha.
\]
Applying strict Jensen convexity with weights \(s_i/S\) gives
\[
\frac{{W}}{{S}}
=\sum_i\frac{{s_i}}{{S}}\phi(z_i)
\ge
\phi\!\left(\sum_i\frac{{s_i}}{{S}}z_i\right)
=\phi(\alpha/S).
\]
Equality holds if and only if every \(z_i\) is equal. Hence \(z_i=\alpha/S\), which gives \(a_i^*=\alpha s_i/S\) and the stated exact minimum. For \(m=2\), \(a_0^*=a_1^*\) holds exactly when \(s_0=s_1\), equivalently \(V_0=V_1\).

For validity, the arm-level result holds at any fixed level \(a_i\). The probability that at least one arm-level confidence process fails is at most \(\sum_i a_i=\alpha\), so the same union-bound construction remains valid for a deterministic unequal split. This is exactly the argument used by Lindon and Kallus for the special choice \(a_0=a_1=\alpha/2\).

For deterministic target rates \(V_i(t)=t v_i+o(t)\),
\[
s_i(t)=\sqrt t\,\sqrt{{v_i}}+o(\sqrt t),
\]
so the exact formula immediately yields the square-root-rate allocation limit. To compare with the equal split, write \(q_i(t)=s_i(t)/S(t)\) and
\[
L_t=\log\!\left(\frac{{\eta^2S(t)^2}}{{\alpha^2}}\right).
\]
At the equal split, the \(i\)-th logarithm is \(L_t+2\log(mq_i(t))\). Since \(L_t=\log t+O(1)\), the expansion \(\sqrt{{L_t+c}}=\sqrt{{L_t}}+c/(2\sqrt{{L_t}})+O(L_t^{{-3/2}})\), summed over the finitely many arms, gives
\[
W_{{\mathrm{{eq}}}}-W^*
=\frac{{S(t)}}{{\sqrt{{L_t}}}}\sum_iq_i(t)\log(mq_i(t))
+o\!\left(\frac{{\sqrt t}}{{\sqrt{{\log t}}}}\right).
\]
Taking limits yields the stated Kullback--Leibler divergence coefficient.

## Verification
The standalone script `verify_error_budget.py` checks the exact closed form on multiple clock configurations, verifies positivity of the second derivative over representative feasible grids, confirms that the proposed allocation equalizes \(a_i/s_i\), and compares the closed-form optimum against dense numerical searches. It also verifies the entropy identity \(D(q\|u)=\log m-H(q)\). The script returns `VERIFY_OK`.

## Relationship to prior work
Lindon and Kallus derive the arm-wise normal-mixture boundary and combine two arm-level confidence sequences with the equal split \(\alpha/2,\alpha/2\). Their Theorem 4.9 states that construction, while Proposition 4.12 explicitly studies how imbalance between the two variance clocks changes the width comparison with a variance-upper-bound benchmark. The inspected full text does not optimize the allocation of \(\alpha\) across arms.

The normal-mixture boundary itself comes from the confidence-sequence literature, including Howard, Ramdas, McAuliffe, and Sekhon. Generic Bonferroni reasoning permits fixed unequal error allocations whenever their sum is controlled, but that general fact does not specify the boundary-shape-dependent optimizer above, its exact minimum, or the clock-rate entropy penalty.

Targeted searches of the published-finding index and the accessible literature for square-root clock allocation, unequal normal-mixture error splitting, and the exact minimized width did not surface an equivalent statement. The closest indexed findings concern heterogeneous randomized-experiment concentration and variance clocks, but they do not optimize union-bound significance allocation for this normal-mixture boundary.

## Limitations
The exact optimizer depends on the target clocks. In the design-based delayed-outcome setting, the oracle clocks depend on fixed potential outcomes and are not generally known to the analyst; the observable plug-in clocks are random. Post-hoc substitution of random plug-in clocks into the allocation formula is therefore outside the validity claim unless a separate argument is supplied. The result also keeps the mixture parameter \(\eta\) fixed and does not jointly optimize \(\eta\), assignment probabilities, or augmentation choices.

The originality assessment is limited to the inspected sources and indexed searches. The optimization is a strict-convexity problem, so an equivalent mathematical resource-allocation lemma may exist under different terminology even if no statistically formulated antecedent was found.

## References
1. M. Lindon and N. Kallus, “Design-Based Anytime-Valid Inference for Randomized Experiments with Delayed Outcomes and Staggered Entry,” arXiv:2603.25971v2; Proceedings of Machine Learning Research 306, 75193–75210 (2026).
2. S. R. Howard, A. Ramdas, J. McAuliffe, and J. Sekhon, “Time-uniform, nonparametric, nonasymptotic confidence sequences,” The Annals of Statistics 49(2), 1055–1080 (2021), DOI: 10.1214/20-AOS1991.
