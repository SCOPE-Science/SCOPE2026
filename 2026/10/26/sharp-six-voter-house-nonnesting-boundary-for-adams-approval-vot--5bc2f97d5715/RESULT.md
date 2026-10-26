# Sharp six-voter house-nonnesting boundary for Adams approval voting

## Finding

**Theorem (sharp tie-independent house-nonnesting boundary).** Consider any finite election with exactly three distinct candidates and any finite number of voters, each casting an arbitrary approval subset, including possibly the empty set. Apply the irresolute Adams approval voting (Adams-AV) rule separately at committee sizes one and two. Say the election is *strongly nonnested* if no Adams-AV-optimal singleton is contained in any Adams-AV-optimal pair. Then at least six voters are necessary. With exactly six voters there are precisely three strongly nonnested anonymous profiles for three labeled candidates, all one class under candidate relabeling. Up to names, the complete list at the minimum consists of two ballots approving \(\{A,B\}\), two approving \(\{A,C\}\), one approving only \(B\), and one approving only \(C\). The sole winning singleton is \(\{A\}\) and the sole winning pair is \(\{B,C\}\).

More strongly, if \(A\) is the unique winning singleton and \(\{B,C\}\) the unique winning pair, let \(u,v,w\) count respectively the single-candidate ballots \(\{A\},\{B\},\{C\}\), let \(p,q,r\) count ballots \(\{A,B\},\{A,C\},\{B,C\}\), let \(t\) count \(\{A,B,C\}\), and let \(e\) count empty ballots. Necessarily
\[
v\ge u+1,\quad w\ge u+1,\quad p\ge r+2,\quad q\ge r+2,
\qquad n\ge 6+3u+3r+t+e.
\]
Equality \(n=6\) uniquely determines the displayed profile, once \(A\) is fixed.

## Assumptions and scope

There are exactly three labeled candidates \(A,B,C\) and \(n\ge1\) unweighted voters with arbitrary subsets of those candidates as ballots. For a committee \(W\), let \(c(W)\) be its number of covered voters: those with at least one approval in \(W\). Adams-AV is the lexicographic composite Thiele rule with marginal weight sequences \((1,0,0,\ldots)\) and \((1,1,1/2,1/3,\ldots)\), exactly as in Baychkov et al., Definition 6. It first maximizes \(c(W)\); among the coverage-maximizing committees, it maximizes the second weighted score. At size one this is ordinary approval voting; at size two the secondary score is \(c(W)+d(W)\), where \(d(W)\) counts voters approving *both* committee members. All tied optimum committees are retained, not arbitrarily resolved.

A pair \(P\) extends singleton \(S\) when \(S\subseteq P\). Strong nonnesting is the failure of this containment for every optimum singleton and every optimum pair. This is a stronger, tie-breaking-independent notion than existence of a nonnested choice under some tie-breaker. No claim is made about more than three candidates, weighted voters, or larger changes in committee size.

## Proof

If strong nonnesting holds on three candidates, there is exactly one winning singleton and exactly one winning pair. Indeed, each two-candidate committee omits exactly one candidate, so two different optimal singletons could not both be excluded by any optimal pair, and two different optimal pairs could not both omit the one optimal singleton. Relabel so the singleton is \(\{A\}\) and the pair \(\{B,C\}\).

Use the seven nonempty ballot multiplicities and the empty-ballot multiplicity defined in the theorem. The singleton approval scores are
\[
s_A=u+p+q+t,\quad s_B=v+p+r+t,\quad s_C=w+q+r+t.
\]
Since \(\{A\}\) is the unique optimum singleton, its strict inequalities against \(B\) and \(C\) yield
\[
u+q>v+r,\qquad u+p>w+r. \tag{1}
\]
The pairwise coverage scores are
\[
c(\{B,C\})=n-e-u,\quad c(\{A,B\})=n-e-w,\quad c(\{A,C\})=n-e-v.
\]
Because Adams-AV maximizes coverage before any secondary comparison, optimality of \(\{B,C\}\) implies \(u\le w\) and \(u\le v\).

Both inequalities must actually be strict. If \(u=w\), then \(\{A,B\}\) and \(\{B,C\}\) tie in primary coverage. Since \(\{B,C\}\) remains an optimum, its secondary score must be at least that of \(\{A,B\}\). Their respective double-approval counts are \(r+t\) and \(p+t\), so \(r\ge p\). This contradicts \(u+p>w+r\) from (1), which becomes \(p>r\). The same comparison of \(\{A,C\}\) with \(\{B,C\}\) shows that \(u=v\) would force \(r\ge q\), contradicting \(u+q>v+r\). Therefore
\[
v\ge u+1,\qquad w\ge u+1.
\]
Substituting into (1) and using integrality gives
\[
q\ge v+r-u+1\ge r+2,
\qquad p\ge w+r-u+1\ge r+2.
\]
Summing the eight ballot multiplicities yields the universal structural bound
\[
\begin{aligned}
n&=e+u+v+w+p+q+r+t\\
 &\ge e+u+(u+1)+(u+1)+(r+2)+(r+2)+r+t\\
 &=6+3u+3r+t+e\ge6.
\end{aligned}
\]
When \(n=6\), all nonnegative surplus terms must vanish, forcing \(e=u=r=t=0\), \(v=w=1\), and \(p=q=2\). There is exactly one such profile after choosing the omitted candidate \(A\). Conversely, this profile has approval scores \((4,3,3)\), so its unique best singleton is \(\{A\}\). The pair \(\{B,C\}\) covers all six voters, whereas each pair containing \(A\) covers five. Thus \(\{B,C\}\) is uniquely optimal even before the tie-break stage. Relabeling gives exactly three labeled anonymous profiles. This proves all claims.

## Verification

The standalone dependency-free script `verify.py` exhausts every anonymous profile on three candidates with one through six voters, **including empty ballots**. It enumerates all eight approval subsets as ballot types, computes exact singleton approval counts, and computes the lexicographic pairs \((c(W),c(W)+d(W))\). It tests whether every optimal singleton is absent from every optimal pair. The respective numbers of profiles for voter counts one through six are \(8,36,120,330,792,1716\), totaling \(3002\). Exactly three profiles fail strong nesting, all at six voters, and they match the three relabelings of the proof's witness. Running `python verify.py` prints all counts and an assertion-checked PASS message. The finite enumeration corroborates the minimum and classification; the inequalities above, rather than computation, prove the bound for arbitrary electorate size.

## Relationship to prior work

Baychkov, Lackner, Maly, Nardi, and Peters (2026) introduce and formally define Adams-AV as a composite Thiele rule, show that it extends Adams' apportionment method, and study justified upper quota. Its definition and primary coverage stage are used here; those properties are not new. Chamberlin–Courant (CC) coverage optimization and classical nonmonotonicity of optimization-based Thiele committee selection provide context. In particular, because the displayed six-voter witness already has *strictly greater coverage* for \(\{B,C\}\), it also exhibits nonnesting for CC. The distinctive additional analysis is the sharp cutoff and equality rigidity for the full lexicographic Adams-AV rule, including proof that its second-stage tie-break does not admit any smaller strong counterexample. We found no exact prior statement establishing this minimum and classification in the accessible sources searched; that observation is not a claim of exhaustive historical priority.

## Limitations

The theorem concerns precisely three candidates and committee sizes one and two. It does not assert the minimal voter count over elections with four or more candidates, nor universal house-monotonicity beyond the stated scope. The six-voter example shows failure of guaranteed nesting, not incompatibility with the rule's upper-quota guarantee. The equality enumeration refers to **anonymous** approval profiles; ballot permutations are not separately counted. Historical-priority uncertainty remains because a published minimal-example statement could use a different characterization of lexicographic CC refinement. Independent scientific audit has not been performed.

## References

1. A. Baychkov, M. Lackner, J. Maly, O. Nardi, and J. Peters, *Beyond Lower Quota: Avoiding Overrepresentation in Multi-Winner Voting*, arXiv:2606.19968v1 (public June 18, 2026), Definition 6, Sections 2–3 and Appendix B. https://arxiv.org/abs/2606.19968 ; open full text: https://www-live.dfki.de/fileadmin/user_upload/import/17523_2606.19968v1.pdf .
2. M. Lackner and P. Skowron, *Multi-Winner Voting with Approval Preferences*, Springer (2023), background on approval-based Thiele and CC rules. This work is background, not cited for a minimality result.
3. The historical nonnested committee example and CC/PAV comparison in *Committee monotonicity — add a seat, keep the winner*, STAR Voting Education & Test-Case Library, https://masiarek.github.io/star-voting-library/04_Approval/03_Criteria/committee_monotonicity.html . This provides a different example, not the exact classification above.
