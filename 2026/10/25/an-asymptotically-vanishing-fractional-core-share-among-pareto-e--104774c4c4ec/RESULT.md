# An asymptotically vanishing fractional-core share among Pareto-efficient approval committees

## Finding

**Theorem.** Fix integers \(k\ge3\) and \(r\ge1\). There are \(k+1\) voters and \(kr+1\) distinct candidates, consisting of a common candidate \(c\) and \(k\) pairwise-disjoint private groups \(P_1,\dots,P_k\) of \(r\) candidates each. For \(1\le i\le k\), voter \(i\) approves \(A_i=\{c\}\cup P_i\). The remaining (guardian) voter \(g\) approves \(A_g=\bigcup_{i=1}^k P_i\). Select exactly \(k\) candidates at Hare quota \(q=(k+1)/k\).

Every size-\(k\) committee is Pareto efficient. Its complete fairness classification is:

* **Ordinary core:** a committee is in the core if and only if either it contains \(c\), or, while omitting \(c\), it intersects at least \(k-1\) of the groups \(P_i\).
* **Fractional core+:** a committee is core+ if and only if it contains \(c\).

Consequently, writing \(A_{k,r}\) for the number of core+ committees and \(B_{k,r}\) for the number in the ordinary core but not core+,
\[
A_{k,r}=\binom{kr}{k-1},\qquad B_{k,r}=r^k+k(k-1)\binom r2 r^{k-2}.
\]
For fixed \(k\ge3\), as \(r\to\infty\),
\[
\frac{A_{k,r}}{A_{k,r}+B_{k,r}}\longrightarrow0,
\quad
\frac{B_{k,r}}{A_{k,r}+B_{k,r}}
=1-\frac{k^{k-1}}{(k-1)!\left(1+k(k-1)/2\right)}\frac1r+O_k(r^{-2}).
\]
In particular, the fractional axiom can retain an asymptotically vanishing share of **Pareto-efficient integral-core committees**.

## Assumptions and scope

All candidates are distinct and indivisible. A voter's utility for a candidate set \(T\) is \(u_i(T)=|A_i\cap T|\). The committee size is exactly \(k\); a blocking proposal may be smaller. A nonempty coalition \(S\) integrally blocks a committee \(W\) if some set \(T\) satisfies \(|S|\ge q|T|\) and \(u_i(T)>u_i(W)\) for each \(i\in S\). The ordinary core excludes such coalitions. The strengthened core+ is the fractional blocking relaxation of Becker, Greger, and Peters (2026), equivalently the payment-certificate characterization in their Theorem 3.3.

The latter criterion requires nonnegative payments \(p_{iw}\) supported on approved elected candidates and voter reserves \(\rho_i=1-\sum_{w\in A_i\cap W}p_{iw}\ge0\), with \(p_{iw}\le\rho_i\), with total payment to any elected candidate at most \(q\), and with strict reserve load \(\sum_{i:d\in A_i}\rho_i<q\) for each unelected candidate \(d\).

## Proof

**Pareto efficiency.** For a private-only committee, guardian utility is \(k\), its maximum, and the other \(k\) voters' utility sum is \(k\). Any alternative containing \(c\) lowers guardian utility; any alternative excluding \(c\) keeps the ordinary voters' utility sum unchanged. Hence no alternative Pareto-dominates this committee. For a committee containing \(c\), ordinary-voter aggregate utility is \(k+(k-1)=2k-1\), while every private-only committee gives their aggregate utility \(k\). Any alternative also containing \(c\) preserves the ordinary aggregate \(2k-1\); it cannot weakly improve all ordinary voters and strictly improve one. Thus these committees are also Pareto efficient.

**Ordinary core, committees containing \(c\).** Write \(s_i=|W\cap P_i|\), so \(\sum_i s_i=k-1\). For any coalition \(S\) of \(s\) ordinary voters, a proposal containing \(c\) that strictly benefits every member needs at least \(s_i+1\) private candidates from each member's group, hence more than \(s\) proposed candidates in total; a proposal without \(c\) needs at least \(s_i+2\) from each member's group and is still larger. Such a coalition cannot afford it, because \(|T|\le s/q<s\). If the coalition contains guardian \(g\), who currently receives \(k-1\) approved candidates, strictly improving the guardian requires a proposal with all \(k\) candidates private. Affording it requires all \(k+1\) voters to participate, but then strictly improving each ordinary voter would require at least \(s_i+2\) private candidates in their own group, totalling at least \(\sum_i(s_i+2)=3k-1>k\). No coalition blocks.

**Ordinary core, committees excluding \(c\).** Now \(\sum_i s_i=k\) and the guardian has maximal utility \(k\), so a blocker can only involve ordinary voters. A coalition of \(s\le k\) of them can afford at most \(s-1\) proposed candidates, since \(q=(k+1)/k\). Without \(c\), improving each requires at least \(s_i+1\) private candidates, already at least \(s\) in total. With \(c\), improving each requires at least \(s_i\) private candidates in addition to \(c\), so at least \(1+\sum_{i\in S}s_i\) candidates. If two groups are unrepresented, their two voters block by proposing \(\{c\}\), since \(2\ge q\). Conversely, with at most one unrepresented group, \(\sum_{i\in S}s_i\ge s-1\) for every coalition \(S\), so a proposal containing \(c\) needs at least \(s\) candidates and is unaffordable. This proves the stated iff.

**Fractional core+ for committees containing \(c\).** Assign payment \(1/k\) from each ordinary voter to \(c\); assign payment \(1/k\) from the guardian to each of the \(k-1\) elected private candidates; use no other payments. Ordinary reserves are \(\rho_i=1-1/k\); guardian reserve is \(\rho_g=1/k\). Every positive payment is at most its voter's reserve (using \(k\ge3\)). The common winner receives total payment \(1\le q\), and each private winner receives \(1/k\le q\). Any unelected private candidate is approved by precisely its ordinary voter and the guardian, so its reserve load is \((1-1/k)+1/k=1<q\). The payment criterion proves core+.

**Exclusion of \(c\) rules out core+.** Let \(W\) contain only private candidates. In any proposed core+ payment certificate, each ordinary voter \(i\) approves exactly \(s_i\) elected candidates. The condition \(p_{iw}\le\rho_i\) implies \(1=\rho_i+\sum_{w\in A_i\cap W}p_{iw}\le(s_i+1)\rho_i\); hence \(\rho_i\ge1/(s_i+1)\). By Cauchy--Schwarz and \(\sum_i(s_i+1)=2k\), the common losing candidate has supporter reserve load
\[
\sum_{i=1}^{k}\rho_i\ge\sum_{i=1}^k\frac1{s_i+1}\ge\frac{k^2}{2k}=\frac k2>\frac{k+1}{k}=q\qquad(k\ge3).
\]
This contradicts the strict reserve inequality in the characterization of core+. Therefore a committee must contain \(c\) to qualify.

**Counting.** With \(c\), choose the remaining \(k-1\) winners freely from \(kr\) private candidates, giving \(\binom{kr}{k-1}\). Without \(c\), a core committee has either one selected private from each group (\(r^k\) possibilities), or exactly one missing group and exactly one other group contributing two winners: choose the missing group in \(k\) ways, the doubled group in \(k-1\) ways, its pair in \(\binom r2\) ways, and one private from each of the remaining \(k-2\) groups in \(r^{k-2}\) ways. These cases are disjoint and exhaustive. Finally \(\binom{kr}{k-1}=\frac{k^{k-1}}{(k-1)!}r^{k-1}+O_k(r^{k-2})\) and \(B_{k,r}=(1+k(k-1)/2)r^k+O_k(r^{k-1})\); division gives the asserted limit and correction.

## Verification

The accompanying `verify_guardian_core_gap.py` enumerates **all** size-\(k\) committees in six small finite instances. It independently tests every affordable integral proposal by exact integer comparisons; tests Pareto efficiency against all alternative committees; and uses a separate linear program with strict positive slack for fractional core+ payment certificates. The six cases are \((k,r)=(3,1),(3,2),(3,3),(4,1),(4,2),(5,1)\). All \(296\) tested committees agree with the theorem, including \((3,3)\), where \(117\) committees are core-stable and \(36\) are core+. Exact derivations, not finite experiments, prove the unbounded parameter statement. Run `python verify_guardian_core_gap.py` with NumPy and SciPy installed.

## Relationship to prior work

Becker, Greger, and Peters (2026) introduce fractional core+ and prove a general nonemptiness and payment-certificate theorem; we use their exact payment equivalence, but their principal results do not count ordinary-core and core+ outcomes in this family. Gölz and Yaghoubizade (2026) connect the same payment notion to frugal Lindahl priceability and analyze its implications to proportional approval voting. Berker et al. (2025) demonstrate that ordinary core stability does not imply Lindahl priceability, including small explicit examples. Thus neither qualitative nonimplication nor the general existence of core+ is claimed as new here. Prior constructions with one private candidate per ordinary voter give related Pareto-efficient separations, but do not imply the full \(r\)-parameter classification or the asymptotic density in this theorem.

## Limitations

The instance is intentionally structured: one universal alternative, equal numbers of private alternatives, and one guardian voter. The asymptotic ratio is over **labeled size-\(k\) committees of this fixed election instance**, not over randomized approval profiles or an arbitrary distribution of elections. Voter count and seat count are held fixed while the candidate number grows. Related clone-based examples might contain equivalent ideas under other terminology; the theorem makes no global minimum-size or universal upper/lower-bound claim. Independent scientific validation has not been performed.

## References

1. R. E. Berker, E. Tewolde, V. Conitzer, M. Guo, M. Heule and L. Xia (2025), *On the Edge of Core (Non-)Emptiness: An Automated Reasoning Approach to Approval-Based Multi-Winner Voting*, arXiv:2512.16895, first public 2025-12-18. https://arxiv.org/abs/2512.16895
2. P. Gölz and H. Yaghoubizade (2026), *Approval-Based Apportionment: Like Portioning, Approximately like Committee Voting*, arXiv:2608.27605, first public 2026-08-27. https://arxiv.org/abs/2608.27605
3. P. Becker, M. Greger and D. Peters (2026), *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912, first public 2026-09-10, especially Definition 3.1 and Theorem 3.3. https://arxiv.org/abs/2609.11912
