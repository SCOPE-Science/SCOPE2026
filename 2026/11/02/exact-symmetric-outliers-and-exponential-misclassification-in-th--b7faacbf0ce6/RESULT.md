# Exact symmetric outliers and exponential misclassification in three-class flip voting games

## Finding
For each integer \(m\geq5\), partition \(3m\) voters into three labeled classes \(A,B,C\), each of size \(m\). For a coalition \(S\), write \((a,b,c)\) for its numbers of members of the three classes, and declare it winning precisely when
\[
20a+15b+12c=59\quad\text{or}\quad20a+15b+12c\geq61.
\]
A weighted-majority surrogate assigns nonnegative voter weights and a real quota, and calls a coalition winning when its total weight is at least the quota. Let \(\delta_m\) be the minimum fraction of the \(2^{3m}\) coalitions whose status is misclassified, without restricting individual weights. Let \(\delta_m^{\mathrm{sym}}\) be the corresponding minimum subject to equal weights within each of the three classes.

Then the exact class-symmetric optimum is
\[
\boxed{\displaystyle\delta_m^{\mathrm{sym}}=
\frac{\min\{\binom m3,\binom m5\}}{2^{3m}}.}
\]
For \(5\leq m\leq7\), an optimal symmetric classifier sacrifices only coalitions with profile \((0,0,5)\); for \(m\geq9\), one sacrifices only profile \((3,0,0)\); both constructions are optimal at \(m=8\). Furthermore, for *unrestricted* weighted-majority surrogates,
\[
\boxed{\displaystyle 2^{-3m}\leq\delta_m\leq
\frac{\min\{\binom m3,\binom m5\}}{2^{3m}},\qquad
\delta_m=2^{-3m+O(\log m)}.}
\]
At the first case \(m=5\), the unrestricted optimum is **exactly** \(\delta_5=2^{-15}=1/32768\): just one coalition of the \(32768\) need be mislabeled.

## Assumptions and scope
The electorate is finite and its three classes each contain exactly \(m\geq5\) distinguishable voters. There are no constraints on coalition size. In both optimization problems, a classifier consists of a real quota and nonnegative real weights (all-zero weights are permitted), with the weak quota convention \(\text{winning}\Leftrightarrow\text{weight}\geq\text{quota}\). Error is counted **per labeled coalition** under the uniform distribution on all subsets, not per distinct class-count profile. The symmetric restriction concerns surrogate weights, not the original game, which is already class-anonymous. No assertion that \(\delta_m=\delta_m^{\mathrm{sym}}\) for \(m\geq6\) is made.

## Proof
**1. Four indispensable profiles.** If the class-symmetric weights are \((u,v,w)\), the profile \(P=(1,1,2)\) is winning, while the three profiles \(Q_1=(3,0,0)\), \(Q_2=(0,4,0)\) and \(Q_3=(0,0,5)\) are losing. Suppose a quota \(q\) correctly classifies all four. Since each \(Q_i\) is losing and weights are nonnegative, \(q>0\), and
\[
3u<q,\qquad4v<q,\qquad5w<q,\qquad u+v+2w\geq q.
\]
But the first three inequalities imply
\[
u+v+2w<\left(\tfrac13+\tfrac14+\tfrac25\right)q
=\tfrac{59}{60}q<q,
\]
a contradiction. Thus at least one of these four entire profiles must be misclassified by every symmetric surrogate. The four profile multiplicities are respectively
\[
m^2\binom m2,\quad\binom m3,\quad\binom m4,\quad\binom m5.
\]
For every \(m\geq5\), their minimum is \(\min\{\binom m3,\binom m5\}\). This establishes the lower bound for \(\delta_m^{\mathrm{sym}}\).

**2. Explicit surrogates with exactly one incorrect profile.** For the first surrogate take weights \((24,18,16)\) on \((A,B,C)\) and quota \(73\). For the second take weights \((30,20,16)\) and quota \(81\). We prove that the only misclassified profiles are \((0,0,5)\) and \((3,0,0)\), respectively, uniformly in \(m\).

Write \(H=20a+15b+12c\). For every profile with \(H\geq62\), the first surrogate's score is at least \(\frac65H\geq\frac{372}{5}>73\); the second's is at least \(\frac43H\geq\frac{248}{3}>81\). All such coalitions are correctly called winning.

For \(H\leq58\), we necessarily have \(0\leq a\leq2\), \(0\leq b\leq3\), and \(0\leq c\leq4\). For each fixed \((a,b)\), the largest allowable \(c\) is \(\lfloor(58-20a-15b)/12\rfloor\); pairs with negative numerator are omitted. Maximizing the two new scores over this complete short list gives, by fixed \(a=0,1,2\), respective upper bounds \((70,72,66)\) and \((76,78,80)\). Each is below its quota. All such coalitions are correctly called losing.

Direct enumeration of the remaining attainable integer values yields exactly one profile at \(H=59\), namely \((1,1,2)\), and exactly three at \(H=60\), namely \((3,0,0),(0,4,0),(0,0,5)\); no profile has \(H=61\). The score of the \(H=59\) profile is \(74\) for the first classifier and \(82\) for the second, so it is correctly called winning. The scores at the three \(H=60\) profiles are \((72,72,80)\) under the first classifier and \((90,80,80)\) under the second. Thus the first errs **only** at profile \((0,0,5)\), and the second errs **only** at profile \((3,0,0)\). Their exact numbers of labeled errors are \(\binom m5\) and \(\binom m3\). Together with Step 1, this proves the exact symmetric minimum and the switch at \(m=8\).

**3. Unrestricted lower bound and exponential rate.** If an unrestricted weighted-majority surrogate were perfect, average its weights over permutations within each class. Because every coalition of a given profile has the same true status, the average score of every winning profile remains at least \(q\), and the average score of every losing profile remains strictly below \(q\). The averaged weights are nonnegative and constant on each class. They would classify \(P,Q_1,Q_2,Q_3\) perfectly, contradicting Step 1. Therefore the game is not weighted at any \(m\geq5\), even without a symmetry restriction. Every surrogate makes at least one labeled error, so \(\delta_m\geq2^{-3m}\), while Step 2 gives \(\delta_m\leq\delta_m^{\mathrm{sym}}\). Since \(\min\{\binom m3,\binom m5\}=\binom m3\sim m^3/6\) for \(m\geq9\), the claimed exponential order follows. For \(m=5\), the first surrogate makes exactly one error, proving equality for unrestricted \(\delta_5\).

## Verification
The standalone standard-library script `verify.py` checks the complete finite exceptional-weight table, both all-size score-ratio certificates, both one-profile error claims, the binomial-count identity for \(5\leq m\leq44\), and independently exhausts all \(2^{15}=32768\) labeled coalitions for \(m=5\). Its verified output is:

`VERIFY_OK low_profiles=120 parameter_sizes=40 exhaustive_m5=32768 errors_m5=1`

The infinite statements follow from the analytical proof, not the finite exhaustive checks. The formula for \(\delta_m^{\mathrm{sym}}\) is exact for every integer \(m\geq5\). The unrestricted inequality is exact only at \(m=5\); the unrestricted multiplicative prefactor is not determined for larger \(m\).

## Relationship to prior work
Einy and Haimanko (2026, arXiv:2610.08968, Definition 17 and Proposition 18) introduced precisely these three-class flip games to show the sharp \(\varepsilon^*=1/(47m)\) excess-weight convergence rate for \(C\)-complete games. Their Definition 26 and Section 6 study the minimal coalition-misclassification fraction generally, proving an \(O(m^{-1/2})\) upper bound in the bounded-class setting. The result proved here instead resolves the exact **class-symmetric** misclassification minimum for their concrete three-class family, identifies the optimal exceptional profile as a function of class size, and proves an exponential decay rate for the unrestricted error. The worst-case excess-weight and coalition-count losses therefore follow very different scales within the same natural examples.

Albareda-Sambola, Molinero and Roura (2025) introduced optimization-based measures including an outlier count and report a census through six players; no result about this subsequently introduced \(3m\)-voter family is established by that earlier census. Classical linear-threshold representability is the background rather than a claim of priority. No source inspected supplies the precise binomial symmetric minimum or the stated exponential classification for this family.

## Limitations
The exact formula concerns weighted surrogates which treat equivalent voters equally. Permitting unequal weights may improve the optimum for \(m\geq6\), and no exact general expression for unrestricted \(\delta_m\) is proved. The exponential bound is specific to the published flip family and does not improve the general bound for arbitrary \(C\)-complete games. Published source and database searches are not an exhaustive guarantee of priority; equivalent unindexed outlier calculations remain possible. The related 2025 outlier-study article was available only through bibliographic information and abstract in the inspected access routes.

## References
1. Ezra Einy and Ori Haimanko, *Large player classes and approximately weighted voting*, arXiv:2610.08968, first submitted 2026-10-06, revised version 2026-10-12. https://arxiv.org/abs/2610.08968 ; https://arxiv.org/html/2610.08968
2. Maria Albareda-Sambola, Xavier Molinero and Salvador Roura, *Weightedness measures from inequality systems*, International Journal of Approximate Reasoning 182 (2025), 109418. https://doi.org/10.1016/j.ijar.2025.109418
