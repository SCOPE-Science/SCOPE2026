# Six voters are the sharp unique-committee split between bloc approval and satisfaction approval voting
## Finding
Consider an approval election with exactly three candidates
\[
\{A,B,C\},
\]
exactly two seats, and nonempty approval ballots.

Under bloc Approval Voting (AV), every approval contributes one point to the approved candidate, and the two highest-scoring candidates are elected.

Under Satisfaction Approval Voting (SAV), a voter approving \(r\) candidates contributes
\[
\frac1r
\]
to each approved candidate, and the two highest satisfaction-score candidates are elected.

Require both rules to have unique winning committees.

With at most \(5\) voters, AV and SAV cannot choose different committees.

The bound is sharp at \(6\) voters. Up to candidate relabeling, the unique anonymous conflict profile is
\[
3\times\{A,B\}+\{B\}+2\times\{C\}.
\]

AV candidate scores are
\[
(3,4,2),
\]
so AV uniquely elects
\[
\{A,B\}.
\]

SAV candidate scores are
\[
\left(\frac32,\frac52,2\right),
\]
so SAV uniquely elects
\[
\{B,C\}.
\]

There are exactly \(6\) candidate-labeled anonymous six-voter conflict profiles, all in this one candidate-relabeling orbit. Each has
\[
\frac{6!}{3!\,2!\,1!}=60
\]
voter labelings, so exactly
\[
360
\]
of the
\[
7^6=117649
\]
labeled six-voter nonempty-ballot profiles give distinct unique committees.

Exactly
\[
75051
\]
labeled six-voter profiles give both rules unique committees. Hence the conflict incidence conditional on both rules being decisive is
\[
\frac{360}{75051}=\frac{40}{8339}.
\]

## Assumptions and scope
There are exactly three candidates and exactly two seats.

Every voter submits a nonempty approval ballot, as in the formal SAV model of Brams and Kilgour.

AV is the fixed-size multiwinner approval rule that elects the two candidates with the largest ordinary approval counts.

SAV elects the two candidates with the largest individual satisfaction scores, where a ballot approving \(r\) candidates contributes \(1/r\) to each approved candidate.

Only profiles for which each rule has a unique winning committee are counted as decisive. Tied winner correspondences are not forced by an external tie-breaker.

Profiles are anonymous when voter identities are ignored but candidate labels are retained. The phrase “up to candidate relabeling” additionally quotients by permutations of \(A,B,C\).

## Proof
Suppose a conflict occurs. Since any two distinct two-member committees on three candidates share exactly one candidate, relabel candidates so that AV uniquely elects
\[
\{A,B\}
\]
and SAV uniquely elects
\[
\{B,C\}.
\]

Write
\[
a,b,c,ab,ac,bc,abc
\]
for the numbers of ballots approving exactly the corresponding nonempty subsets.

Because AV uniquely excludes \(C\),
\[
a-c+ab-bc>0.
\]
Because SAV uniquely excludes \(A\),
\[
c-a+\frac{bc-ab}{2}>0.
\]

Set
\[
d=c-a,\qquad e=ab-bc.
\]
The two strict inequalities become
\[
e-d\ge1
\]
and
\[
2d-e\ge1.
\]
Therefore
\[
d+1\le e\le2d-1,
\]
which forces
\[
d\ge2,\qquad e\ge3.
\]

Thus
\[
c\ge a+2,\qquad ab\ge bc+3.
\]
In particular at least five voters are already required among the \(C\)-only and \(AB\)-type excesses.

If there are exactly five voters, equality is forced:
\[
a=bc=b=ac=abc=0,\qquad c=2,\qquad ab=3.
\]
The profile is therefore
\[
3\times\{A,B\}+2\times\{C\}.
\]
Its SAV scores for \(A\) and \(B\) are both \(3/2\), so SAV does not have a unique winning committee. Hence no decisive conflict exists with at most five voters.

Now suppose there are exactly six voters. The inequalities above imply \(d=2\) and \(e=3\); otherwise the mandatory excess already uses at least seven voters. Hence
\[
2a+2bc+b+ac+abc=1.
\]
So
\[
a=bc=0
\]
and exactly one of
\[
b,\ ac,\ abc
\]
equals \(1\).

If \(ac=1\), then the AV scores of \(B\) and \(C\) tie, so AV is not unique.

If \(abc=1\), then the SAV scores of \(A\) and \(B\) tie, so SAV is not unique.

The only surviving case is
\[
b=1,
\]
giving
\[
3\times\{A,B\}+\{B\}+2\times\{C\}.
\]
Direct score computation gives the unique committees claimed above.

Candidate relabeling produces six distinct anonymous labeled profiles because the representative has no nontrivial candidate symmetry. Each anonymous profile has multinomial voter multiplicity \(60\), yielding \(360\) labeled profiles.

## Verification
The embedded `verify_av_sav_six_voter_boundary.py` uses only the Python standard library and exact rational arithmetic.

It independently performs two exhaustive computations.

First, it enumerates every labeled profile of nonempty approval ballots through six voters. The numbers of labeled profiles for which both AV and SAV have unique committees are
\[
3,\ 27,\ 201,\ 1467,\ 10398,\ 75051
\]
for one through six voters, while the numbers with distinct unique committees are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 360.
\]

Second, it enumerates the \(924\) anonymous six-voter profiles, viewed as weak compositions into the seven nonempty ballot types. Exactly six are conflicts. Their candidate-relabeling canonicalization gives one orbit, represented by count vector
\[
(0,1,2,3,0,0,0)
\]
in the ballot-type order
\[
A,B,C,AB,AC,BC,ABC.
\]

The verifier also checks the direct proof inequalities on every oriented conflict candidate and confirms that the six-voter representative is forced.

Run:

`python3 verify_av_sav_six_voter_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Brams and Kilgour introduced Satisfaction Approval Voting as a multiwinner approval rule designed to split each voter’s unit weight equally among all approved candidates. They explicitly compare SAV with ordinary multiwinner AV and prove that the two rules can produce different, even disjoint, winning sets.

Their paper studies the exact three-candidate, two-winner setting in a decision-theoretic section. It also gives a three-candidate example with \(17\) voters in which AV elects one pair and SAV another:
\[
5\times AB+5\times AC+4\times B+3\times C.
\]
The paper does not state a minimum-electorate theorem for distinct unique AV and SAV committees.

Aziz and collaborators later formalized AV and SAV together in a common approval-based committee framework. Their full text defines AV as maximizing total approvals and SAV as maximizing
\[
\sum_i\frac{|W\cap A_i|}{|A_i|},
\]
and studies winner determination and strategic complexity rather than the smallest profile where the two unique committees disagree.

The present finding isolates the exact onset of the disagreement already motivated by that literature: in the smallest competitive candidate/seat geometry, six voters are necessary and sufficient, and the entire first layer is one profile type up to candidate relabeling.

Targeted searches using AV/SAV aliases, three-candidate/two-seat language, six-voter language, unique-committee language, and minimal-electorate language did not locate this exact cutoff or one-orbit classification.

## Limitations
The theorem fixes exactly three candidates and two seats.

Every ballot is required to be nonempty. Empty ballots would contribute nothing to either rule and therefore only add inactive voters.

The result concerns unique committees. Smaller profiles may exhibit ties or set-valued differences without producing two distinct unique committees.

The exact census stops at the first conflict order. No formula is claimed for larger electorates.

An unindexed teaching example, software test corpus, or chapter exercise could contain the same six-voter profile.

## References
1. S. J. Brams and D. M. Kilgour, “Satisfaction approval voting,” MPRA Paper 22709, posted 17 May 2010; later published as a chapter in *Voting Power and Procedures*.
2. H. Aziz, S. Gaspers, J. Gudmundsson, S. Mackenzie, N. Mattei, and T. Walsh, “Computational Aspects of Multi-Winner Approval Voting,” arXiv:1407.3247, first submitted 11 July 2014.
3. S. J. Brams and D. M. Kilgour, “Satisfaction Approval Voting,” in *Mathematical and Computational Modeling*, 2015, DOI: 10.1002/9781118853887.ch11.
