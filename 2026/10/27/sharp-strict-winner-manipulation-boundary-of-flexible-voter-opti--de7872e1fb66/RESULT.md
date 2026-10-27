# Sharp strict-winner manipulation boundary of flexible-voter-optimal approval voting

## Finding
For the FVR-optimal scoring rule \(R_{\mathrm{OPT}}\) of Halpern, Procaccia and Suksompong [1], strict-to-strict profitable dichotomous ballot manipulation is impossible for every electorate with at most three candidates. With exactly four candidates it is impossible with at most three voters but possible with four. Thus four candidates and four voters are jointly minimal among profiles whose sincere and manipulated elections each have a unique winner.

The positive example has candidate set \(\{A,B,C,D\}\). Three voters report \(\{A\},\{A\},\{A,B\}\). The fourth voter sincerely likes only \(B\), reports \(\{B\}\), and obtains unique winner \(A\). Reporting \(\{B,C,D\}\) instead gives unique winner \(B\), without reliance on tie-breaking.

## Assumptions and scope
There are \(m\geq1\) candidates and \(n\geq1\) voters. Each ballot is a subset of candidates. Let \(\sigma_m(k)=m/(m-k)\) for integers \(1\leq k<m\), and \(\sigma_m(0)=\sigma_m(m)=0\). Under \(R_{\mathrm{OPT}}\), a voter reporting a ballot of size \(k\) assigns \(\sigma_m(k)\) points to every candidate in that ballot and no points to other candidates. For a full ballot the convention of [1] ignores the voter; for an empty ballot there is no point contribution. Candidates maximizing their total score win, with arbitrary resolution of ties.

Fix a distinguished voter whose true liked set is \(S\); that voter's truthful ballot is \(S\), all other ballots are held fixed, and their dichotomous evaluation strictly prefers every member of \(S\) to every candidate outside \(S\). We call a deviation \(T\) *strict-to-strict profitable* if the sincere score vector has a **unique** winner outside \(S\) and the altered score vector has a **unique** winner in \(S\). This definition excludes outcomes involving score ties; it is deliberately weaker than full strategyproofness.

The statement refers only to this one-winner rule, complete reporting freedom, finite elections and strict winners. It is not a result for multiwinner FVR rules or arbitrary utility intensities within the liked set.

## Proof
**1. Score-gap obstruction.** Suppose sincere ballot \(S\) makes candidate \(b\notin S\) uniquely win, and deviation \(T\) makes \(a\in S\) uniquely win. Let \(P_c\) be the total score candidate \(c\) receives from the other voters. Set \(s=|S|\), \(t=|T|\), and \(u_k=\sigma_m(k)\).

Sincere unique victory of \(b\) implies
\[
P_b>P_a+u_s.
\]
If the misreport omits \(a\), then \(a\) has new score \(P_a\), while \(b\) has at least \(P_b\), so \(a\) cannot win. If the misreport includes \(b\) as well as \(a\), they gain the same nonnegative amount, so \(b\) stays ahead. Hence a successful report must include \(a\) and exclude \(b\), and the unique new victory of \(a\) necessitates
\[
u_s<P_b-P_a<u_t.\tag{1}
\]
This obstruction is valid for all voters, ballot sizes and score ties elsewhere in the profile.

**2. At most three candidates, any electorate.** For \(m=1\), a disliked winner and liked alternative cannot coexist. For \(m=2\), the possible weights are \(0\) and \(2\), so a deviation cannot have \(u_t>u_s\) whenever a truthful liked alternative is opposed by a disliked winner (the sincere ballot then is necessarily a singleton). For \(m=3\), a successful sincere profile must have a nonempty proper \(S\); the possible positive weights are \(u_1=3/2\) and \(u_2=3\). A strict interval in (1) can only arise when \(s=1\) and \(t=2\), where it would require \(3/2<P_b-P_a<3\). Every ballot cast by another voter contributes either \(0\), \(3/2\), or \(3\) to any candidate, so \(P_b-P_a\) is an integer multiple of \(3/2\). No such multiple lies strictly between \(3/2\) and \(3\). This proves the all-electorates impossibility.

**3. Four candidates, up to three voters.** The exact checker `verify_opt_fvr.py` iterates, for each \(n\in\{1,2,3\}\), all ordered \(n-1\) opponent ballots, all \(16\) truthful ballots and all \(16\) deviating ballots. The number of ordered instances is exactly \(16^{n+1}\): respectively \(256\), \(4096\) and \(65536\). All scores use exact rational arithmetic. The checker computes the unique maximum at each endpoint and tests whether a sincere loser becomes a deviating liked unique winner. The three exhaustive counts are respectively \(0\), \(0\), \(0\). Because every allowed profile and deviation for these finite \(m,n\) is present, this is exhaustive finite proof, not sampling.

**4. Four-candidate/four-voter witness.** Name candidates \(A,B,C,D\). Two opponent singleton ballots \(\{A\}\) each add \(4/3\) to \(A\), and one opponent two-element ballot \(\{A,B\}\) adds \(2\) to both. The manipulator's sincere ballot \(\{B\}\) adds \(4/3\) to \(B\). The sincere score vector, in order \(A,B,C,D\), is
\[
\left(\frac{14}{3},\frac{10}{3},0,0\right),
\]
whose unique maximizer is the disliked \(A\). With report \(\{B,C,D\}\), each approved name instead gains \(4\); the new scores are
\[
\left(\frac{14}{3},6,4,4\right).
\]
The only maximizing name is the liked \(B\), completing both sharpness statements.

## Verification
Run `python3 verify_opt_fvr.py` under Python 3.8 or newer. It uses the standard library's `fractions.Fraction` and `itertools.product`, requires no external data or packages, asserts all six endpoint score checks for the explicit witness, and exhausts all \(69888\) ballot/report tuples for \(m=4\) and \(1\leq n\leq3\). The expected exact output is in `verify_output.txt`. The script's exhaustive search supplements the analytic all-electorate proof for \(m\leq3\); it is not used to justify claims about unrestricted electorate sizes with \(m=4\).

## Relationship to prior work
Halpern, Procaccia and Suksompong [1, Sections 2.5–2.6, Theorems 2.5–2.7] introduce precisely this score function, establish its optimal flexible-voter-representation guarantee and essential uniqueness within their scoring-rule class. Their stated results concern representation guarantees, not the sharp joint candidate/electorate boundary for strict-to-strict ballot manipulation proved here. Their equivalent disapproval-point formulation is covered because minimizing disapproval points orders candidates exactly as maximizing the approval scores.

Endriss [2] studies manipulation when voters can have multiple sincere ballots, including the ordinary approval-rule setting; the present statement fixes the distinguished voter's sincere ballot to the true liked set and concerns a ballot-size-dependent scoring weight absent from ordinary approval voting. Alcalde-Unzu and Vorsatz [3] study *size approval voting* with a different ballot-size weighting design. The cited abstract was accessible but its full text was not verified, so related historical priority remains a residual risk. None of these comparisons is claimed to establish literature-wide novelty solely from failed searches.

## Limitations
This is a threshold for **unique sincere winner to unique manipulated winner**. It does not establish ordinary (tie-sensitive) strategyproofness with at most three candidates. Indeed, with three candidates \(A,B,C\), another voter reporting \(\{B\}\) and a distinguished voter sincerely liking \(\{A\}\) yield a tie between \(A\) and \(B\); a deviation to \(\{A,C\}\) changes the score profile and can help under a suitable tie convention. Ties may also occur at the manipulated endpoint and lie outside our definition. The four-voter example involves padding with two disapproved candidates; it demonstrates a concrete strategic defect of this rule but does not quantify the prevalence of manipulable profiles or generalize the sharp electorate threshold to more than four candidates. Exact finite enumeration supports only the explicitly enumerated sizes.

## References
[1] Daniel Halpern, Ariel D. Procaccia and Warut Suksompong, *The Proportional Veto Principle for Approval Ballots*, arXiv:2505.01395v1 (first public 2025-05-02), Section 2.5, Section 2.6, Appendix A, https://arxiv.org/html/2505.01395v1.

[2] Ulle Endriss, *Vote Manipulation in the Presence of Multiple Sincere Ballots* (2007), Sections 1–3, on multiple sincere ballots and manipulation under standard voting rules.

[3] Jorge Alcalde-Unzu and Marc Vorsatz, *Size Approval Voting*, abstract/catalogue and open manuscript landing page; full text not independently obtained.
