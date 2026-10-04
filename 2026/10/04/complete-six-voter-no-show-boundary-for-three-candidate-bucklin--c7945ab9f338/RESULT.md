# Complete six-voter no-show boundary for three-candidate Bucklin voting
## Finding
For three-candidate Bucklin voting with complete strict anonymous ballots and tie-independent unique outcomes, no standard no-show paradox occurs with fewer than \(6\) voters.

At \(6\) voters there are exactly
\[
18
\]
labeled anonymous profiles that admit a profitable homogeneous abstention. Every bad profile admits exactly one such event, and the abstaining group consists of exactly one voter.

Modulo simultaneous relabeling of the three candidates, the \(18\) bad profiles form exactly \(3\) classes, each of orbit size \(6\). Normalize the abstaining voter's sincere ranking to
\[
A\succ B\succ C
\]
and order the six ballot types as
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA.
\]
Then the complete minimal boundary is the one-parameter family
\[
(1,t,0,3,2-t,0),\qquad t\in\{0,1,2\}.
\]
In every member of this family, \(C\) wins with all six voters, while after the single \(ABC\) voter abstains, \(B\) wins. Since that voter ranks \(B\) above \(C\), abstention is profitable.

There are
\[
\binom{11}{5}=462
\]
anonymous labeled-candidate profiles with six voters. Exactly \(417\) have a unique Bucklin outcome under the convention below. Therefore the minimal-boundary incidence is
\[
\frac{18}{462}=\frac{3}{77}
\]
among all anonymous profiles and
\[
\frac{18}{417}=\frac{6}{139}
\]
among unique-outcome profiles.

## Assumptions and scope
Every ballot is a strict linear order of exactly three candidates. Voters with the same ranking are anonymous.

Bucklin counting proceeds by rank depth. At depth one, a candidate supported by a strict majority is elected. If no candidate has a strict first-place majority, depth two counts every voter who ranks a candidate either first or second. Among candidates whose depth-two count is a strict majority, the candidate with the largest count is elected. For three candidates, a candidate's depth-two count is the total electorate size minus that candidate's last-place count.

Only profiles with a unique Bucklin winner are admitted. Thus no external tie-breaking convention enters the claim.

A homogeneous no-show event removes a nonempty group of voters all having the same sincere ranking. The event is profitable when every abstainer strictly prefers the post-abstention winner to the winner obtained when the group participates.

## Proof
An anonymous three-candidate profile is a weak composition of the electorate size into the six ballot types. Hence there are only \(462\) profiles at size six and fewer at every smaller size.

The verifier performs a complete profile-first enumeration for every electorate size from one through six. For each profile, it computes the unique Bucklin winner, then tests every ranking type present in the profile and every possible positive homogeneous abstention size. The post-abstention election is recomputed from scratch and compared using the abstainers' sincere ranking.

This exhaustive route finds no event at sizes one through five and exactly \(18\) events at size six. The \(18\) events occur in \(18\) distinct profiles, so each bad profile has exactly one profitable homogeneous abstention. Every such group has size one.

A second, independently organized enumeration starts from every possible post-abstention profile of size at most five, adds each possible homogeneous voter group, recomputes the participating election, and tests profitability. It produces exactly the same event set as the profile-first search.

The winner computation itself is also duplicated. One implementation follows literal Bucklin rank depths. The second uses the special three-candidate reduction: if no strict first-place majority exists, the depth-two winner is exactly the unique candidate with the fewest last-place votes. The two implementations agree on every full and post-abstention profile tested.

Canonicalizing each six-voter bad profile under all six candidate permutations gives three orbits, each of size six. Relabeling each event so that the abstainer has ranking \(A\succ B\succ C\) yields exactly
\[
(1,0,0,3,2,0),\quad
(1,1,0,3,1,0),\quad
(1,2,0,3,0,0),
\]
which is the stated family.

For any \(t\in\{0,1,2\}\), the first-place counts in \((1,t,0,3,2-t,0)\) are
\[
(1+t,3,2-t),
\]
so no candidate has more than three of six first places. The last-place counts are
\[
(3,2,1),
\]
independent of \(t\). Hence \(C\) has the unique largest depth-two count and wins. After removing the single \(ABC\) ballot, five voters remain and \(B\) has three first-place votes, a strict majority. Thus \(B\) wins, and the abstainer prefers \(B\) to \(C\).

## Verification
The embedded `verify_bucklin6_noshow.py` uses only the Python standard library and exact integer arithmetic.

Replay with:

`python3 verify_bucklin6_noshow.py`

The first output line must be `VERIFY_OK`.

The replay checks both exhaustive traversal directions, both independent Bucklin implementations, the zero count through five voters, the exact eighteen-event boundary at six voters, the one-voter abstention size, the three candidate-relabeling classes, the three normalized forms, and both incidence fractions.

## Relationship to prior work
Felsenthal and Nurmi study participation failures under Bucklin and eight other voting procedures. Their paper gives multi-candidate examples of two strong participation failures for Bucklin and explicitly describes Bucklin's rank-depth rule, but it does not present a complete three-candidate six-voter census.

Brandt, Matthäus, and Saile later compile minimal paradox instances for many common voting rules, including Bucklin, using optimization. Their compilation is expressly aimed at minimal numbers of voters and candidates. Accordingly, the six-voter minimality component is treated here as potentially covered by that broader minimal-instance literature rather than as the sole novelty claim. The refinement established here is the complete tie-independent boundary: exactly \(18\) bad profiles, three symmetry classes, one profitable event per bad profile, the closed normalized family \((1,t,0,3,2-t,0)\), and the two exact incidence fractions.

Targeted searches using the Bucklin, participation, and no-show terminology together with the six-voter boundary, the count \(18\), and the normalized profile vectors did not locate a published source stating this complete classification.

## Limitations
The theorem is restricted to exactly three candidates, complete strict rankings, anonymous voter types, and unique Bucklin outcomes. Tie-breaking variants can create additional cases.

The incidence fractions use the uniform counting measure on anonymous profiles, not a probabilistic model of independently sampled voters.

The literature search did not reveal an equivalent complete census, but an unindexed thesis, note, software table, or supplementary computation could contain the same finite classification.

## References
1. D. S. Felsenthal and H. Nurmi, “Two types of participation failure under nine voting methods in variable electorates,” *Public Choice* 168 (2016), 115–135. DOI: 10.1007/s11127-016-0352-5.
2. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.
3. D. S. Felsenthal and N. Tideman, “Varieties of failure of monotonicity and participation under five voting methods,” *Theory and Decision* 75 (2013), 59–77. DOI: 10.1007/s11238-012-9306-7.
