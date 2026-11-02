# A sharp power-law welfare phase diagram and a cubic incentive obstruction for facility omission

## Finding

For each integer \(n\ge3\) and each real \(q\ge0\), consider the reciprocal-power omission rule for \(n\) agents and \(n-1\) facilities: with distinct reports, calculate each report's distance \(d_i\) to its closest *other* report, omit report \(i\) with probability proportional to \(d_i^{-q}\), and open facilities at every other report. The social cost is the sum of agents' nearest-facility distances. The following are exact worst-case approximation statements over **all metric spaces** and all distinct profiles, for each fixed \(n\).

* For \(0\le q<1\), the supremum of the approximation ratio is infinite.
* For \(q=1\), the supremum is \(n/2\), as previously established by Escoffier and collaborators.
* For every \(q>1\), the **attained** sharp ratio \(R_{n,q}>1\) is the unique real solution of

\[
2(R_{n,q}-1)R_{n,q}^{q-1}
=\frac{(n-2)(q-1)^{q-1}}{q^q}.
\]

Equality is attainable on the real line, for every \(n\ge3\) and \(q>1\), by the successive-gap pattern \(1,t,t,\ldots,t\), with \(t=qR_{n,q}/(q-1)\). For fixed \(n\), \(R_{n,q}\) is strictly decreasing for \(q>1\) and tends to one as \(q\) increases without bound. In particular, the known inverse-square case \(q=2\) reduces to \(R_{n,2}=(1+\sqrt{n/2})/2\), **which is prior work, not a new special-case claim**.

This improvement in approximation is not a general incentive guarantee. For **every \(q>3\)**, the reciprocal-power rule is **not strategyproof**, already with three agents on the real line, at truthful locations \((0,1,2)\). No claim is made here that powers between one and three are strategyproof, beyond the previously proved cases \(q=1\) and \(q=2\).

## Assumptions and scope

A metric space \((\Omega,d)\) contains \(n\ge3\) pairwise distinct reports \(x_1,\ldots,x_n\). Put \(d_i=\min_{j\ne i}d(x_i,x_j)>0\), \(d_*=\min_i d_i\), and \(p_i=d_i^{-q}/\sum_j d_j^{-q}\), with the convention \(d_i^0=1\). The mechanism opens the set of all reported positions except that of one randomly omitted agent. Utility uses actual, not necessarily reported, locations when considering manipulation. Facility locations in the optimum may lie anywhere in \(\Omega\), not merely at the reports. The approximation calculation applies to distinct truthful profiles; collocated reports would require an explicit implementation convention and are not claimed here.

The optimal \((n-1)\)-facility social cost is exactly \(d_*\): any \(n\) agents served by at most \(n-1\) facilities include two using the same facility, and the triangle inequality forces their sum of distances to be at least \(d_*\); omitting one endpoint of a closest pair and opening the other reports attains \(d_*\).

## Proof

**1. Exact expected-cost expression.** When \(i\) is omitted, precisely agent \(i\) is unserved at its own location and pays \(d_i\), while all other agents have zero cost. Hence

\[
\frac{\mathbb E[\operatorname{SC}]}{\operatorname{OPT}}
=\frac{\sum_i d_i^{1-q}}{d_*\sum_i d_i^{-q}}
=\frac{\sum_i y_i^{q-1}}{\sum_i y_i^q},\qquad y_i=d_*/d_i\in(0,1].
\]

Every closest pair contributes **two** entries equal to one. There may be more. For \(q=1\), the ratio is \(n/\sum_i y_i\le n/2\). For \(0\le q<1\), take three or more real-line reports with consecutive gaps \(1,t,\ldots,t\) and let \(t\to\infty\). Exactly two normalized nearest distances are one, while all others are \(1/t\). Then the displayed ratio is

\[
\frac{2+(n-2)t^{1-q}}{2+(n-2)t^{-q}},
\]

which tends to infinity for \(q<1\), and tends to \(n/2\) for \(q=1\).

**2. The sharp bound when \(q>1\).** For \(R>1\), define \(g_R(y)=y^{q-1}-Ry^q\) on \([0,1]\). Its derivative has the sign of \((q-1)-qRy\), so the unique maximizer is

\[
y_R=\frac{q-1}{qR}\in(0,1),\qquad \max_{0\le y\le1}g_R(y)=\frac{(q-1)^{q-1}}{q^qR^{q-1}}.
\]

For any profile, choose two indices with \(y_i=1\). Every remaining entry contributes no more than \(g_R(y_R)\). Therefore

\[
\sum_i(y_i^{q-1}-Ry_i^q)
\le2(1-R)+(n-2)\frac{(q-1)^{q-1}}{q^qR^{q-1}}.
\]

The right side vanishes at the stated root \(R=R_{n,q}\). There is exactly one such \(R>1\), because \(2(R-1)R^{q-1}\) is continuous and strictly increasing from zero to infinity. Hence \(\mathbb E[\operatorname{SC}]/\operatorname{OPT}\le R_{n,q}\).

**3. Attainability and parameter monotonicity.** Set \(t=1/y_R=qR_{n,q}/(q-1)>1\) and consider real-line locations \(0,1,1+t,1+2t,\ldots,1+(n-2)t\). Their nearest-neighbor distances are \((1,1,t,\ldots,t)\), so every non-designated term attains the unique maximizer above. Equality holds. The construction also shows that any equality profile has exactly two minimal nearest distances and all remaining nearest distances equal to \(t d_*\), because \(g_R(1)<g_R(y_R)\) and the maximizer is unique.

For each fixed nonconstant nearest-distance vector, increasing \(q\) strictly reduces the weighted mean of those distances: differentiating \(\sum_i d_i^{1-q}/\sum_i d_i^{-q}\) gives \(-\operatorname{Cov}_{p(q)}(d_i,\log d_i)<0\). Apply this strict comparison to the sharp \(q_2\)-extremizer and compare it with the maximum at any \(1<q_1<q_2\); thus \(R_{n,q_2}<R_{n,q_1}\). Dividing the defining equation by its left-hand power shows the unique root tends to one as \(q\to\infty\), since for every fixed \(\epsilon>0\) the left side at \(R=1+\epsilon\) eventually exceeds the right side. (Equivalently, the right side divided by \(R^{q-1}\) tends to zero.)

**4. A truthful-cost deviation for every \(q>3\).** Three actual reports are \((0,1,2)\). The truthful expected cost of the agent at zero is \(1/3\). Let that agent instead report \(-\varepsilon\), while the other reports remain fixed. For \(\varepsilon>0\), the new nearest-neighbor distances are \((1+\varepsilon,1,1)\), so the probability of omitting the deviating report is

\[
P_q(\varepsilon)=\frac{1}{1+2(1+\varepsilon)^q}.
\]

If omitted, the agent's actual distance to the nearest facility is one; otherwise a facility at her misreported position is at distance \(\varepsilon\). Thus her exact new expected cost is

\[
C_q(\varepsilon)=\varepsilon+(1-\varepsilon)P_q(\varepsilon),\quad
C_q(0)=\frac13,\quad C'_q(0)=\frac{2(3-q)}9.
\]

For every \(q>3\), this one-sided derivative is negative, so sufficiently small positive \(\varepsilon\) strictly improves the deviator's cost. This proves failure of strategyproofness, without assuming or proving anything for the unresolved powers \(2<q\le3\).

## Verification

The included standalone `verify.py` runs deterministic floating-point checks of the sharp formula on 144 extremal line profiles (all combinations of population sizes 3 through 20 and eight exponents above one), 18,000 seeded random line profiles, and checks the \(q\le1\) boundary numerically. It additionally calculates with exact rational arithmetic that for \(q=4\), reporting \(-1/100\) in the three-agent witness changes cost from \(1/3\) to \(154668497/466849700<1/3\). Reproduction: run `python3 verify.py` beside this file. These are finite corroborations; the universal bounds and the continuum of profitable-exponent witnesses follow from the preceding analytical proof.

## Relationship to prior work

Escoffier et al. (2011) introduced the inverse-proportional (\(q=1\)) rule, proved strategyproofness, and its sharp \(n/2\) welfare ratio. Chan, Lin and Wang, in *Randomized Strategyproof Facility Location: Two Facilities and Beyond* (first public 2026-08-23), Section 4 and Theorem 3, independently introduced and **already proved** the strategyproof inverse-square (\(q=2\)) rule and its sharp \((1+\sqrt{n/2})/2\) welfare bound. These precise special cases are not claimed as new. The statement here is the full real-exponent welfare phase diagram together with a negative strategic boundary above exponent three. The cited preprint's full Section 4 and its appendix were checked for the parameterized theorem and local deviation obstruction; neither is stated there.

## Limitations

The optimality ratio is for exactly \(n-1\) facilities, distinct report positions and utilitarian distance costs, with a fixed real exponent \(q\ge0\). The construction does not assert truthful incentives for other exponents, nor approximate optimality over the class of all randomized strategyproof mechanisms. The deviation establishes non-strategyproofness only for \(q>3\). No independent mathematical audit has been conducted. Discovery of earlier equivalent power-law or incentive analyses in unindexed literature would affect novelty, not the proof.

## References

1. H. Chan, J. Lin, and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first posted 2026-08-23. https://arxiv.org/html/2608.22484v2 (Section 4, Theorem 3 and its proof).
2. B. Escoffier, L. Gourvès, N. K. Thang, F. Pascual, and O. Spanjaard, *Strategy-proof mechanisms for facility location games with many facilities*, Algorithmic Decision Theory (2011), Lecture Notes in Computer Science 6992, 67–81. Cited and contrasted in reference 1, Section 4.
