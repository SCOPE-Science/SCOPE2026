# Exact finite-electorate quality frontier for two-seat reciprocal representation

## Finding
Let \(n\ge 2\) voters approve subsets of \(m\ge2\) candidates, let every candidate be approved by at least one voter, and let each candidate \(c\) have quality \(h_c\in(0,1]\). For a committee \(W\) of exactly two candidates, write \(h(W)=\sum_{c\in W}h_c\). Let \(\mathrm{OPT}\) be the largest quality of any two-candidate committee. Under the reciprocal justified representation (reciprocal JR) and reciprocal extended justified representation (reciprocal EJR) axioms, respectively, define the best attainable fractions \(\mathrm{OPT}_{\mathrm{JR}}/\mathrm{OPT}\) and \(\mathrm{OPT}_{\mathrm{EJR}}/\mathrm{OPT}\).

For each **fixed** integer \(n\ge2\), the infimum of either fraction over all such elections (and all candidate counts \(m\ge2\)) is exactly
\[
\boxed{\frac{3n-2}{4(n-1)}=\frac34+\frac{1}{4(n-1)}.}
\]
Indeed, for every instance the maximal-quality reciprocal JR and reciprocal EJR committees have the **same quality**. A reciprocal JR committee realizing the guarantee can be obtained from any quality-optimal pair by replacing at most one candidate. Both exact bounds are attained already with three candidates and a two-block party-list approval profile.

## Assumptions and scope
There are \(n\ge2\) voters \(V\) and \(m\ge2\) candidates \(C\), each with a nonempty supporter set \(V[c]\subseteq V\) and quality \(0<h_c\le1\). Voter \(i\) approves \(A_i\subseteq C\), and an election chooses exactly \(k=2\) candidates. Define \(C_{\cap S}=\bigcap_{i\in S}A_i\) and \(C_{\cup S}=\bigcup_{i\in S}A_i\) for nonempty voter groups \(S\).

A group \(S\) can reciprocally afford a nonempty candidate set \(T\subseteq C_{\cap S}\) when
\[
|S|\ge \frac n2\sum_{c\in T}\frac1{h_c}.
\]
Reciprocal JR requires \(C_{\cup S}\cap W\neq\varnothing\) for all such \(S\). Reciprocal EJR requires \(\max_{i\in S}|A_i\cap W|\ge|T|\) for every such pair \((S,T)\). These definitions are those of Boehmer, Dong, Kreisel, and Utke (2026). The theorem is an existence and worst-case optimal-quality statement, not a statement that every reciprocal-JR committee enjoys the guarantee.

## Proof
**Lemma 1 (single-replacement JR).** Choose two highest-quality candidates \(a,b\), with \(\alpha=h_a\ge\beta=h_b\). If \(W_0=\{a,b\}\) satisfies reciprocal JR, retain it. Otherwise there is a group \(S\) with no approval of \(a\) or \(b\), and some candidate \(d\in C_{\cap S}\) such that
\[
|S|\ge\frac{n}{2h_d}.
\]
Since every candidate has at least one supporter, \(a\) has a supporter outside \(S\); therefore \(|S|\le n-1\). Thus
\[
\gamma:=h_d\ge\frac{n}{2|S|}\ge\tau_n:=\frac{n}{2(n-1)}.
\]
We claim \(W_1=\{a,d\}\) satisfies reciprocal JR. Were another group \(T\) to violate JR for \(W_1\), it would approve neither \(a\) nor \(d\) and could reciprocally afford some commonly approved candidate. Every voter in \(S\) approves \(d\), so \(S\cap T=\varnothing\). Both groups have size at least \(n/2\), because every quality is at most one. Hence \(|S|=|T|=n/2\), necessarily with \(T=V\setminus S\). But the supporter of \(a\) outside \(S\) then lies in \(T\), contradicting that \(T\) is unrepresented by \(\{a,d\}\). This proves the lemma, including the even-electorate boundary case.

**Lemma 2 (quality bound).** In the replacement case, \(\mathrm{OPT}=\alpha+\beta\), while
\[
\frac{h(W_1)}{\mathrm{OPT}}=\frac{\alpha+\gamma}{\alpha+\beta}\ge\frac{\alpha+\tau_n}{\alpha+\beta}\ge\frac{1+\tau_n}{2}.
\]
For the last inequality, multiply by the positive denominator and use the exact nonnegative identity
\[
2(\alpha+\tau_n)-(1+\tau_n)(\alpha+\beta)
=(1-\tau_n)(\alpha-\beta)+2\tau_n(1-\beta)\ge0,
\]
where \(\tau_n\le1\), \(\alpha\ge\beta\), and \(\beta\le1\). If no replacement was necessary, the fraction is one. Therefore reciprocal JR always permits fraction \((1+\tau_n)/2=(3n-2)/(4(n-1))\).

**Lemma 3 (EJR collapses to JR for quality optimization with two seats).** A group \(S\) can afford two commonly approved distinct candidates \(c,d\) only if
\[
|S|\ge\frac n2\left(\frac1{h_c}+\frac1{h_d}\right)\ge n.
\]
Equality throughout forces \(S=V\) and \(h_c=h_d=1\); both candidates are then approved by every voter. If such a pair exists, selecting it attains optimal quality two and satisfies reciprocal EJR, for groups entitled to one or two seats. Otherwise no group can afford two candidates. In that case every reciprocal-EJR demand has size one, and reciprocal EJR is **exactly reciprocal JR**. Consequently, the best feasible reciprocal-EJR and reciprocal-JR qualities are equal for every instance, and Lemma 2 applies to both.

**Sharpness.** For any \(n\ge2\), take precisely three candidates \(a,b,d\) with qualities
\[
h_a=h_b=1,\qquad h_d=\tau_n=\frac{n}{2(n-1)}.
\]
Exactly one voter approves \(\{a,b\}\), while the other \(n-1\) voters each approve only \(\{d\}\). The latter group \(S\) has size \(n-1\) and can reciprocally afford \(d\) with equality. Thus every reciprocal-JR or reciprocal-EJR committee contains \(d\). Its maximal attainable quality is \(1+\tau_n\); the unrestricted optimum \(\{a,b\}\) has quality two. Their ratio is exactly \((1+\tau_n)/2\), attaining the universal lower bound. For \(n=2\) this ratio equals one; the same construction remains valid.

## Verification
The full proof above is valid for arbitrary real qualities in \((0,1]\), arbitrary finite approval patterns, and every integer \(n\ge2\). It uses neither a numerical extrapolation nor an exhaustive-search hypothesis.

The standalone standard-library program `verify.py` separately evaluates reciprocal JR and EJR from voter-subset definitions using exact rational arithmetic; it enumerates every nonempty support pattern and selected rational quality tuple for three candidates with two or three voters, samples higher-electorate instances, and checks sharp three-candidate witnesses for two through eight voters. Invoke `python verify.py` from the directory containing this file and the program. On the checked package the program printed `CHECKS_OK 24407`.

## Relationship to prior work
Boehmer, Dong, Kreisel, and Utke, *Approval-Based Multiwinner Voting with Candidate Qualities* (arXiv:2609.08830, first made public September 8, 2026), introduced these reciprocal representation axioms. Their Theorem 5.5 and Appendix G establish the sharp **unrestricted** quality fraction \(3/4\) for several reciprocal proportionality axioms. Their Example G.1 provides a three-candidate family approaching \(3/4\) as electorate size increases. Fixing its electorate size yields the sharpness family above, but neither their global estimate nor the example establishes the **finite-\(n\) upper guarantee** or the **one-replacement structural lemma** proved here. The theorem also proves that, for exactly two seats, the optimal qualities obtainable with reciprocal JR and reciprocal EJR coincide. General reciprocal-EJR algorithms from proportional participatory budgeting are not needed for this two-seat construction.

## Limitations
The sharp formula assumes exactly two committee seats, qualities in \((0,1]\), and at least one supporter for each candidate. It does not assert the same formula for larger committees, unsupported candidates, reciprocal threshold-PJR+, or reciprocal value-EJR. It is an existence guarantee for optimally selected fair committees, not for arbitrary rule outputs. The related unrestricted \(3/4\) guarantee is already known; only the finite-electorate refinement, matching upper bound, and structural selection statement are claimed here. No independent scientific audit has been performed; overlap with otherwise unindexed literature cannot be ruled out.

## References
1. Niclas Boehmer, Chris Dong, Luca Kreisel, Markus Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830 (first submission September 8, 2026), Sections 2 and 5, Appendix F, Appendix G. https://arxiv.org/abs/2609.08830
2. Dominik Peters et al., *Proportional Participatory Budgeting with Additive Utilities* (2021), as cited in [1] for the underlying reciprocal-cost interpretation and EJR method.
