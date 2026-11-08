# A joint envy-and-top-choice law for random serial dictatorship

## Finding

Let \(U_n\) count students whom nobody envies and let \(T_n\) count students who envy nobody (equivalently, who receive their globally first-ranked school) after random serial dictatorship (RSD). For **every** integer \(n\ge1\) under independent uniform strict rankings, the theorem below gives the **complete bivariate probability distribution** \(\Pr(U_n=u,T_n=t)\) by an exact finite recurrence. In particular,

\[
\operatorname{Cov}(U_n,T_n)=1-\frac{H_n}{n},\qquad H_n=\sum_{h=1}^{n}\frac1h.
\]

Writing \(B_n\) for the number of students satisfying both criteria, one also has

\[
\mathbb E B_n=1,\qquad
\mathbb E\bigl|\{\text{unenvied students}\}\cup\{\text{top-choice students}\}\bigr|
=H_n+\frac{n-1}{2}.
\]

These joint statements refine the previously established separate mean formulas \(\mathbb E U_n=H_n\) and \(\mathbb E T_n=(n+1)/2\). Neither separate expectation is asserted to be novel.

## Assumptions and scope

There are exactly \(n\) students and \(n\) unit-capacity schools. Each student independently draws a complete strict ordering of all schools uniformly from the \(n!\) possible orders. A uniform random priority order of students is then processed: the current student receives her highest-ranked unassigned school. By exchangeability of students it suffices to fix this priority order as \(1,\ldots,n\).

Student \(i\) envies student \(j\) if she strictly prefers \(j\)'s assigned school over her own. A student is *unenvied* if no other student envies her. A student *envies nobody* precisely when she receives her first choice among **all** schools, not merely among the currently available schools. This theorem is about the actual RSD outcome and makes no conclusion about the joint count under deferred acceptance.

Define \(S_j\) as the number of students among the first \(j\) assignees who have not been envied by any of these first \(j\) students, and \(T_j\) as the number of globally first-choice assignments among those first \(j\) assignees. Thus \((S_0,T_0)=(0,0)\), \((S_n,T_n)=(U_n,T_n)\). Before student \(j\) chooses, \(r=n-j+1\) schools remain available. All formulas are exact rationals; no approximation or asymptotic hypothesis is used.

For nonnegative integers \(s,k\) with \(0\le k\le s\), write the falling factorial \((s)_{\underline{k}}=s(s-1)\cdots(s-k+1)\), with \((s)_{\underline0}=1\).

## Proof

**1. An exact finite transition law.** Conditional on the full history before position \(j\), suppose \(S_{j-1}=s\). There are \(s\) assigned schools still unenvied, \(r\) available schools, and \(j-1-s\) already-envied assigned schools. An earlier student cannot envy the new choice, since earlier students already chose their best available school. The new student therefore creates one new unenvied assignee. She can make old unenvied assignees newly envied: let \(K\) be the number of the \(s\) still-unenvied schools ranked above her favorite of the \(r\) currently available schools.

In the projection of her random ranking onto these \(s+r\) relevant schools, all relative permutations are equiprobable. The event \(K=k\) says the first \(k\) relevant positions are occupied by distinct formerly unenvied schools and the next is occupied by an available school. Consequently

\[
\Pr(K=k\mid S_{j-1}=s)=p_{s,r}(k)
:=\frac{r(s)_{\underline{k}}}{(s+r)_{\underline{k+1}}},\qquad 0\le k\le s.
\]

It follows that \(S_j=s+1-K\). In particular \(\Pr(K=0)=r/(r+s)\). Let \(F_j\) indicate that student \(j\)'s assignment is her globally top-ranked school. There are \(r\) available schools among the \(n\) schools, independent of her fresh uniformly random preference. Hence \(\Pr(F_j=1\mid\text{history})=r/n\). The event \(F_j=1\) implies \(K=0\). Thus, conditional on the state \((s,t)\) and the current \(r\), the only transitions with positive probabilities are

\[
\begin{aligned}
(s,t)&\longrightarrow(s+1,t+1)&&\text{with probability }r/n,\\
(s,t)&\longrightarrow(s+1,t)&&\text{with probability }r/(r+s)-r/n,\\
(s,t)&\longrightarrow(s+1-k,t)&&\text{with probability }p_{s,r}(k),\quad 1\le k\le s.
\end{aligned}
\]

When two arrows lead to the same state their probabilities are added. The first two probabilities are nonnegative because \(r+s\le n\). Their sum and the remaining \(p_{s,r}(k)\) sum to one. Starting with \(\Pr(S_0=0,T_0=0)=1\), these transitions determine every \(\Pr(S_j=s,T_j=t)\) recursively and hence the claimed exact bivariate law. In the special case \(n=1\), the law assigns probability one to \((U_1,T_1)=(1,1)\).

**2. Conditional expectations and covariance.** For each of the \(s\) old unenvied assignees, the next student does not envy her if that old assignee's school ranks below her favorite among \(r\) remaining schools, an event of conditional probability \(r/(r+1)\). Therefore

\[
\mathbb E[S_j\mid S_{j-1}=s]=1+\frac{rs}{r+1}.
\]

Induction on \(j\) with the initial condition \(\mathbb E S_0=0\) yields

\[
\mathbb E S_{j-1}=(r+1)(H_n-H_r),
\qquad H_0:=0,\quad r=n-j+1.
\]

Because \(F_j\) is independent of all history preceding position \(j\), and \(S_j=s+1\) whenever \(F_j=1\), its covariance with the new survival count is

\[
\operatorname{Cov}(S_j,F_j)
=\frac{r}{n(r+1)}\mathbb E S_{j-1}.
\]

Every one of the \(S_j\) survivors avoids envy from the subsequent fresh students with conditional probability \(1/r\), as the factors \((r-1)/r,(r-2)/(r-1),\ldots,1/2\) telescope. Each of the later new students contributes an expected number to \(U_n\) independent of the history through position \(j\). Thus

\[
\mathbb E[U_n\mid\text{full history through }j]
=\frac{S_j}{r}+H_{r-1}.
\]

Conditioning on the history through position \(j\) therefore implies

\[
\operatorname{Cov}(U_n,F_j)
=\frac1r\operatorname{Cov}(S_j,F_j)
=\frac{H_n-H_r}{n}.
\]

Since \(T_n=\sum_{j=1}^nF_j\), summing over the positions and using \(\sum_{r=1}^nH_r=(n+1)H_n-n\) proves

\[
\operatorname{Cov}(U_n,T_n)
=\frac1n\sum_{r=1}^n(H_n-H_r)
=1-\frac{H_n}{n}.
\]

The identity also holds at \(n=1\), when both counts are constant. As separate consequences of the same construction, \(\mathbb E U_n=H_n\) and \(\mathbb E T_n=(n+1)/2\). Indeed, the latter follows by summing \(\Pr(F_j=1)=r/n\).

**3. Exact intersection and union means.** Fix position \(j\), where \(r=n-j+1\). The probability that her globally first-ranked school is still available is \(r/n\). Conditional on this event and the history through position \(j\), she remains unenvied by every future student with probability \(1/r\), again by the telescoping survival product. Thus

\[
\Pr(F_j=1\text{ and position }j\text{ remains unenvied})=\frac1n.
\]

Summing over all positions gives \(\mathbb E B_n=1\). Inclusion–exclusion for the two random sets, together with the known separate means, yields their union mean \(H_n+(n-1)/2\). The set union consists of students satisfying at least one of the two stated envy criteria; it is **not** asserted to equal the set of Pareto-unimprovable students under RSD.

## Verification

The accompanying standalone `verify_joint.py` computes the bivariate recurrence exactly using Python's `fractions.Fraction`. An independent implementation enumerates all \((n!)^n\) strict preference profiles for \(n=1,2,3,4\) with fixed student priority and compares the **whole** joint probability table against the recurrence, not merely its first moments. It additionally counts the intersection directly in the exhaustive enumerations. For \(n=1,\ldots,7\), it independently verifies total mass, the two first moments, the exact covariance and the variance of the first-choice count. All checks passed at preparation. To reproduce: `python3 verify_joint.py` with Python 3 and no third-party dependencies. Exhaustive enumeration is limited to four students; the theorem for all \(n\) follows from the conditional-rank and telescoping arguments above, not from these computations.

## Relationship to prior work

Ortega, Ziegler, Arribillaga and Zhao's *The Distribution of Envy in Matching Markets* (online March 10, 2026), Section 3, establishes the separate RSD expectations \(H_n\) and \((n+1)/2\), motivating the joint question. Its results do not report this bivariate state law, covariance, intersection or union formula. The companion *Identifying and Quantifying (Un)Improvable Students* develops the envy digraph and the DA setting; it does not study this RSD bivariate law. The classical Myers–Wilf coupon calculation concerns singleton coupons and their collection time, which corresponds to the unenvied marginal, not simultaneously to the first-choice assignments in RSD. A separate existing full marginal law for the unenvied count is acknowledged and is not re-presented as a discovery. Having both marginal laws does not determine their dependence, covariance, overlap or union size.

## Limitations

The claim assumes independent uniformly random strict preferences, a square market, complete lists, unit capacities and serial dictatorship. It does **not** assert a bivariate result for deferred acceptance, deterministic heterogeneous preferences, school priorities, unequal markets, or correlated preference orders. The exact formulas describe two envy-based categories, not the full set of possible Pareto improvements. A self-review is not an independent audit; prior unindexed joint coupon-collection formulations may exist.

## References

- Ortega, J., Ziegler, G., Arribillaga, R. P., Zhao, G., *The Distribution of Envy in Matching Markets*, Economics Letters 263 (2026), 112936, https://doi.org/10.1016/j.econlet.2026.112936; open manuscript https://arxiv.org/html/2603.23385v1.
- Ortega, J., Ziegler, G., Arribillaga, R. P., Zhao, G., *Identifying and Quantifying (Un)Improvable Students*, 2024 preprint, https://arxiv.org/html/2407.19831v4.
- Myers, A., Wilf, H., *Some New Aspects of the Coupon Collector's Problem*, SIAM Review 48 (2006), 549–565; https://arxiv.org/abs/math/0304229.
