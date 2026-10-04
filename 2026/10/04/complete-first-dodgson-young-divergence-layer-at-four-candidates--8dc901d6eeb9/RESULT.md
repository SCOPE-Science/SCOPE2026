# Complete first Dodgson–Young divergence layer at four candidates and three voters
## Finding
Consider elections with complete strict rankings.

Under the standard **Dodgson rule**, the score of candidate \(x\) is the minimum number of adjacent swaps in the voters' rankings needed to make \(x\) a strong Condorcet winner.

Under the standard **Young rule**, the score of \(x\) is the minimum number of voters that must be deleted so that \(x\) becomes a weak Condorcet winner. Candidates with minimum score are the winners.

Prior work establishes that with exactly three candidates the Dodgson and Young winner correspondences agree on every profile. With four candidates and one voter, both rules trivially select that voter's top-ranked candidate.

With four candidates and three voters, however, the rules first separate. Among the
\[
24^3=13824
\]
labeled profiles, exactly
\[
1008
\]
have different winner sets. Hence the exact uniform-profile divergence probability is
\[
\frac{1008}{13824}=\frac{7}{96}.
\]

The separation is one-sided on the entire first layer:
\[
D(P)\subsetneq Y(P)
\]
for every divergent profile \(P\), where \(D(P)\) and \(Y(P)\) are the Dodgson and Young winner sets.

The complete winner-set-size census is
\[
\begin{array}{c|r}
(|D(P)|,|Y(P)|,\text{relation}) & \text{profiles}\\ \hline
(1,1,\text{equal}) & 12288\\
(3,3,\text{equal}) & 528\\
(2,3,\text{strict containment}) & 144\\
(2,4,\text{strict containment}) & 576\\
(3,4,\text{strict containment}) & 288.
\end{array}
\]

Thus every disagreement enlarges the winner set under Young; there are no profiles on this first layer where Young strictly refines Dodgson, where the sets overlap without containment, or where they are disjoint.

Up to relabeling the four candidates and relabeling the three voters, the \(1008\) divergent profiles form exactly seven isomorphism classes. Every class has the full orbit size
\[
4!\,3!=144.
\]

Using candidates \(A,B,C,D\), canonical representatives and score vectors are:

\[
\begin{array}{c|c|c|c}
\text{ballots} & \text{Dodgson scores} & \text{Young scores} & (D,Y)\\ \hline
ABC D,\ BCA D,\ DCAB & (1,1,1,3) & (1,1,1,1) & (\{A,B,C\},\{A,B,C,D\})\\
ABC D,\ BCDA,\ CDAB & (2,1,1,3) & (1,1,1,3) & (\{B,C\},\{A,B,C\})\\
ABC D,\ BCDA,\ DACB & (1,1,2,2) & (1,1,1,1) & (\{A,B\},\{A,B,C,D\})\\
ABC D,\ BCDA,\ DCAB & (2,1,1,2) & (1,1,1,1) & (\{B,C\},\{A,B,C,D\})\\
ABC D,\ BDAC,\ CDAB & (1,1,2,2) & (1,1,1,1) & (\{A,B\},\{A,B,C,D\})\\
ABC D,\ BDAC,\ DCAB & (1,1,3,1) & (1,1,1,1) & (\{A,B,D\},\{A,B,C,D\})\\
ABC D,\ BDCA,\ CDAB & (2,1,1,2) & (1,1,1,1) & (\{B,C\},\{A,B,C,D\}).
\end{array}
\]

Spaces in the first displayed ballot of each row are only typographical; for example \(ABC D\) means \(A\succ B\succ C\succ D\).

Consequently, four candidates are the smallest candidate set for which Dodgson and Young can differ, and three voters are the smallest odd electorate that realizes the separation at four candidates.

## Assumptions and scope
Preferences are complete and strict. Dodgson uses the strong Condorcet target and adjacent swaps, while Young uses the weak Condorcet target obtained by deleting voters; this is the standard distinction used in the computational-social-choice literature.

The census concerns exactly four labeled candidates and three labeled voters.

The lower candidate bound uses the published theorem that Dodgson and Young coincide for all three-candidate profiles. The one-voter lower bound at four candidates is immediate.

The result does not classify even electorates, StrongYoung, weak-Dodgson variants, incomplete ballots, ties, or elections with five or more candidates.

## Proof
There are
\[
4!=24
\]
strict rankings of four candidates and therefore
\[
24^3=13824
\]
labeled three-voter profiles.

For each candidate, the verifier computes the Dodgson score in two independent ways.

First, it uses a dynamic program over the candidate's pairwise majority deficits. Moving the candidate upward by one adjacent position changes exactly one pairwise margin by \(2\), so each ballot contributes a finite menu of exact gain vectors and costs.

Second, it directly enumerates every possible upward position of the candidate in each of the three ballots. Moving other candidates among themselves cannot improve the candidate's pairwise contests and would only add swaps, so this direct search is exhaustive for the minimum Dodgson score.

The two Dodgson implementations agree candidate by candidate on every profile.

For Young, the first implementation enumerates every nonempty voter subset and finds the largest subset on which the candidate is a weak Condorcet winner. The deletion score is three minus that maximum subset size.

The second implementation is specialized to three voters. It checks, in order, whether the candidate is already a strong Condorcet winner; whether some pair of voters makes the candidate a weak Condorcet winner; whether some single voter ranks the candidate first; and otherwise assigns deletion score \(3\). These two Young implementations also agree on every candidate of every profile.

The exhaustive relation histogram is exactly
\[
12288,\quad528,\quad144,\quad576,\quad288
\]
in the five rows displayed above. Thus
\[
144+576+288=1008
\]
profiles diverge, giving
\[
1008/13824=7/96.
\]

For every divergent profile, the complete winner sets satisfy
\[
D(P)\subsetneq Y(P).
\]

To quotient by symmetry, the verifier sorts the three ballots and applies every permutation of the four candidate labels. Each divergent profile is mapped to the lexicographically least representative in its orbit. Exactly seven representatives occur, and every orbit contains
\[
4!\,3!=144
\]
labeled profiles. Their seven canonical representatives and score vectors are exactly those displayed in the finding.

## Verification
The embedded `verify_dodgson_young_first_layer.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- all \(24\) four-candidate one-voter profiles;
- all \(13824\) four-candidate three-voter profiles;
- two independent Dodgson-score computations;
- two independent Young-score computations;
- exact equality counts \(12288\) and \(528\);
- exact divergent subtype counts \(144,576,288\);
- total divergence \(1008\) and probability \(7/96\);
- strict containment \(D(P)\subsetneq Y(P)\) on every divergent profile;
- exactly seven divergent isomorphism classes;
- orbit size \(144\) for every class;
- the seven canonical representatives and both score vectors.

Run:

`python3 verify_dodgson_young_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Dodgson and Young are classical Condorcet extensions built from different notions of distance to majority consensus. The standard computational treatment defines Dodgson score through adjacent exchanges leading to a strong Condorcet winner and Young score through voter deletion leading to a weak Condorcet winner.

Courtin, Mbih, and Moyouwou prove that with three alternatives, Dodgson, Young, maximin, and Kemeny always select the same winner, and explicitly note that the equivalence no longer holds once there are more than three alternatives.

Brandt, Dong, and Peters independently organize a broad family of three-candidate Condorcet extensions and again place Dodgson and Young in the same maximin-equivalence class.

The contribution here is the complete first layer after that three-candidate collapse: at four candidates, the first odd electorate size already suffices, exactly \(7/96\) of three-voter labeled profiles diverge, the separation is always the refinement \(D(P)\subsetneq Y(P)\), and the whole divergent layer consists of seven full symmetry orbits.

Targeted searches for the exact count \(1008\), the fraction \(7/96\), the three-voter/four-candidate boundary, and the seven-orbit classification did not locate an equivalent published result.

## Limitations
The theorem is a finite first-layer classification. It does not give a formula for larger electorates or candidate sets.

The result uses standard Young rather than StrongYoung. This distinction matters because two-voter subprofiles can have weak Condorcet winners without strong Condorcet winners.

The seven-orbit statement quotients only by voter and candidate relabeling; it does not identify profiles under ballot reversal or other transformations that are not symmetries of the two rules.

An unindexed exercise, code archive, thesis, or supplementary computation could contain the same first-layer census.

## References
1. I. Caragiannis, E. Hemaspaandra, and L. A. Hemaspaandra, “Dodgson's Rule and Young's Rule,” in *Handbook of Computational Social Choice*, Cambridge University Press, 2016, pp. 103–126. DOI: 10.1017/CBO9781107446984.006.
2. S. Courtin, B. Mbih, and I. Moyouwou, “Are Condorcet procedures so bad according to the reinforcement axiom?”, THEMA Working Paper 2012-37; later *Social Choice and Welfare* 42 (2014), 927–940. DOI: 10.1007/s00355-013-0758-7.
3. F. Brandt, C. Dong, and D. Peters, “Condorcet-Consistent Choice Among Three Candidates,” arXiv:2411.19857; later *Games and Economic Behavior* 153 (2025), 113–130. DOI: 10.1016/j.geb.2025.05.005.
4. I. Caragiannis, J. A. Covey, M. Feldman, C. M. Homan, C. Kaklamanis, N. Karanikolas, A. D. Procaccia, and J. S. Rosenschein, “On the approximability of Dodgson and Young elections,” *Artificial Intelligence* 187–188 (2012), 31–51. DOI: 10.1016/j.artint.2012.04.004.
