# A Minimax Rule for Bullet-Vote Positive Involvement

## Finding

Let \(X\) be a finite set of at least two alternatives and let \(P\) be a profile of strict weak orders. Define the pairwise margin by
\[
 m_P(x,y)=\#\{v:x\succ_v y\}-\#\{v:y\succ_v x\}.
\]
Let \(CL(P)=\{x\in X: m_P(y,x)>0\text{ for every }y\ne x\}\) be the set of Condorcet losers, and let
\[
 \mu_P(x)=\max_{y\ne x}m_P(y,x).
\]
Define \(F(P)=\operatorname*{argmin}_{x\in X\setminus CL(P)}\mu_P(x)\); for a singleton alternative set, define \(F(P)=X\). Then \(F\) is nonempty, satisfies the Condorcet-winner criterion and Condorcet-loser criterion, is resolvable by adding one voter, and is invariant under changes to the numerical margins that preserve the ordinal margin graph. Moreover, if a new voter ranks a current winner \(x\) uniquely first and ties all other alternatives below \(x\), then \(x\) remains a winner—in fact, it becomes the unique winner.

## Assumptions and scope

Profiles are finite and may contain indifference among alternatives below a uniquely top-ranked alternative. A *bullet vote for* \(x\) means exactly such a weak order: \(x\) is uniquely first and all alternatives in \(X\setminus\{x\}\) are tied. The participation guarantee concerns only bullet votes, not arbitrary rankings with \(x\) first. Pairwise margins may be positive, negative, or zero.

## Proof

**Nonemptiness and Condorcet losers.** At most one alternative can be a Condorcet loser: two such alternatives would each have to defeat the other. Hence \(X\setminus CL(P)\) is nonempty, and the argmin defining \(F(P)\) is nonempty. By construction, no Condorcet loser is selected.

**Condorcet winner.** If \(c\) is a Condorcet winner, then \(m_P(y,c)<0\) for every \(y\ne c\), so \(\mu_P(c)<0\). For each \(y\ne c\), \(m_P(c,y)>0\), whence \(\mu_P(y)\ge m_P(c,y)>0\). Thus \(c\) is the unique minimizer and \(F(P)=\{c\}\).

**Ordinal-margin invariance.** If \(x\) has at least one incoming majority edge, then \(\mu_P(x)\) is the largest positive margin among edges entering \(x\). Its comparisons with the corresponding scores of other losing alternatives are determined solely by the ordering (including ties) of positive margins. If \(x\) has no incoming edge but has a pairwise tie, then \(\mu_P(x)=0\). If \(x\) beats every other alternative, then \(\mu_P(x)=-\min_{y\ne x}m_P(x,y)<0\); there can be at most one such alternative, and its score is below every score of a candidate with a loss. These cases show that the ordering and ties among the scores \(\mu_P(x)\) are determined by the ordinal margin graph. The Condorcet-loser set is determined by its edge orientations as well. Therefore \(F(P)\) is unchanged whenever the ordinal margin graph is unchanged.

**Bullet-vote positive involvement and resolvability.** Suppose \(x\in F(P)\), and add one bullet voter for \(x\), obtaining \(P'\). For every \(y\ne x\), \(m_{P'}(x,y)=m_P(x,y)+1\), while margins between alternatives other than \(x\) are unchanged. Consequently,
\[
 \mu_{P'}(x)=\mu_P(x)-1,\qquad \mu_{P'}(y)\ge\mu_P(y)\quad(y\ne x).
\]
Since \(x\notin CL(P)\), some \(y\ne x\) satisfies \(m_P(x,y)\ge0\), so \(m_{P'}(x,y)>0\) and \(x\notin CL(P')\). A Condorcet loser in \(P\) remains a Condorcet loser in \(P'\), because its pairwise defeats are unchanged except that its defeat by \(x\) becomes larger. Thus the eligible set \(X\setminus CL(P')\) is a subset of \(X\setminus CL(P)\) and still contains \(x\). Every other eligible candidate has score at least its old score, which was at least \(\mu_P(x)\); meanwhile \(x\)'s score falls by one. Therefore \(x\) is the unique minimizer in \(P'\). This proves bullet-vote positive involvement. It also proves single-voter resolvability: whenever \(F(P)\) has multiple winners, choose any \(x\in F(P)\) and add a bullet voter for \(x\); the new winner set is exactly \(\{x\}\).

**Why the stronger participation axiom is not obtained.** In the four-alternative profiles denoted \(Q_3\) and \(Q_2\) in Holliday's 2024 paper, adding four voters ranking \(b\succ d\succ a\succ c\) changes the margin graph from \(Q_3\) to \(Q_2\). At \(Q_3\), \(d\) is a Condorcet loser and the remaining minimax scores are \(\mu(a)=17\), \(\mu(b)=15\), and \(\mu(c)=19\), so \(F(Q_3)=\{b\}\). At \(Q_2\), the scores are \(\mu(a)=21\), \(\mu(b)=11\), \(\mu(c)=23\), and \(\mu(d)=9\), so \(F(Q_2)=\{d\}\). Thus the rule does not satisfy full positive involvement: if it did, adding those four voters one at a time would preserve \(b\) throughout. This does not affect the bullet-vote guarantee proved above.

## Verification

The proof uses only pairwise-margin identities. The one-voter update changes every margin involving \(x\) by exactly one and leaves all other margins unchanged; the displayed score inequalities follow directly from taking maxima. The nonempty eligible set, Condorcet criteria, margin invariance, bullet-vote property, and resolvability are proved for every finite profile in the stated domain. The \(Q_3\)-to-\(Q_2\) comparison is read from the margin lists in the cited primary source and establishes the stated limitation on full positive involvement. No empirical inference or finite enumeration is used as a substitute for proof.

## Relationship to prior work

Holliday's 2024 impossibility theorem rules out the conjunction of full positive involvement, the Condorcet-winner and Condorcet-loser criteria, resolvability, and ordinal margin invariance. Its first footnote explicitly identifies bullet-vote positive involvement as a weaker alternative. The construction here shows that replacing full positive involvement by that weaker axiom changes the compatibility result: a Condorcet-safe minimax variant satisfies the other four properties. A 2026 follow-up proves a stronger impossibility result for full positive involvement without ordinal-margin invariance on domains with at least five candidates; that result still concerns the stronger axiom and does not imply impossibility for bullet votes.

## Limitations

The positive-involvement result is limited to added voters who tie all non-top alternatives; it does not extend to arbitrary strict rankings with the same top alternative. The rule is a simple axiom-compatible construction, not a claim that it is uniquely characterized or normatively optimal. The 2026 follow-up was checked at abstract level only, so a full-text comparison remains a residual literature risk; its stated theorem concerns full positive involvement.

## References

1. W. H. Holliday, “An impossibility theorem concerning positive involvement in voting,” arXiv:2401.05657 (first posted 11 January 2024); *Economics Letters* 236 (2024), article 111589, DOI 10.1016/j.econlet.2024.111589.
2. W. H. Holliday, “The incompatibility of the Condorcet winner and loser criteria with positive involvement and resolvability,” arXiv:2601.10506 (2026).
3. MaRDI record Q6498749, classification listing MSC 91B12 (voting theory) and 91B14 (social choice).
