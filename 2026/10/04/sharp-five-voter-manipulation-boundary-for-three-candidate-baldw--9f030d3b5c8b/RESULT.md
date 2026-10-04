# Sharp five-voter manipulation boundary for three-candidate Baldwin voting
## Finding
For three-candidate Baldwin voting with complete strict anonymous ballots and tie-independent unique outcomes, no voter can profit from a unilateral false report when the electorate has fewer than \(5\) voters.

At exactly \(5\) voters, there are exactly
\[
6
\]
manipulable anonymous labeled-candidate profiles among the
\[
\binom{10}{5}=252
\]
anonymous profiles. All six form a single orbit under candidate relabeling.

These six anonymous profiles expand to exactly
\[
180
\]
labeled voter profiles among the \(6^5=7776\) possible ordered profiles, so the unconditional profile incidence is
\[
\frac{180}{7776}=\frac5{216}.
\]
Among the \(6636\) labeled profiles with a unique Baldwin outcome, the incidence is
\[
\frac{180}{6636}=\frac{15}{553}.
\]

Every bad anonymous profile has exactly one vulnerable sincere ranking type, and that type occurs exactly twice. Either one of the two voters of that type can manipulate, and each has exactly one profitable false report. Hence there are exactly
\[
360
\]
vulnerable distinguished voter-profile pairs. Their incidence is \(1/108\) among all labeled voter-profile pairs and \(6/553\) when conditioning on a unique truthful Baldwin outcome.

Normalize the manipulator's sincere order to
\[
A\succ B\succ C
\]
and list the six ballot types as
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA.
\]
Then the entire minimal boundary has the single normal form
\[
(2,0,0,1,2,0).
\]
A vulnerable \(ABC\) voter has the unique profitable report
\[
B\succ C\succ A.
\]
Truthfully, the Baldwin winner is \(C\); after this one voter reports \(BCA\), the winner is \(B\), which the voter sincerely prefers to \(C\).

## Assumptions and scope
There are exactly three candidates and every ballot is a strict linear order. Baldwin's rule repeatedly recomputes Borda scores among the candidates still alive and eliminates the unique lowest-scoring candidate until one remains.

The theorem is tie-independent. A profile or reported profile is used only when every Baldwin elimination round has a unique lowest Borda score and the resulting winner is therefore uniquely determined without an external tie-breaker.

A unilateral manipulation means that one voter changes only her own ballot, all other ballots remain fixed, and the new unique winner is strictly preferred to the truthful unique winner according to that voter's sincere ranking.

The profile counts distinguish candidate names. The anonymous counts ignore voter identities; the labeled counts retain them.

## Proof
There are six strict rankings of three candidates. An anonymous \(n\)-voter profile is therefore a weak composition of \(n\) into six parts.

The verifier performs a complete anonymous census for every \(1\le n\le5\). For each profile it computes the truthful Baldwin winner. For every sincere ranking type present, it removes one voter of that type, inserts each of the five possible false rankings in turn, recomputes Baldwin from scratch, and tests whether the new winner is strictly better in the sincere order.

Two independent winner implementations are required to agree. The iterative implementation literally recomputes Borda scores after each elimination. The closed three-candidate implementation computes the first-round Borda scores, requires a unique Borda loser, and then resolves the surviving pair by their head-to-head majority. They agree on every truthful and deviating profile used in the exhaustive search.

The anonymous search gives zero manipulable profiles for electorates of sizes \(1,2,3,4\), and exactly six at size \(5\). Each of the six has one vulnerable ranking type, that type has multiplicity two, and exactly one false report is profitable.

A second exhaustive route enumerates all \(6^5=7776\) ordered five-voter profiles directly. It independently checks every distinguished voter and every false report. After forgetting voter labels, its bad-profile support is exactly the same six anonymous profiles; the multiplicities match their multinomial coefficients. This route gives exactly \(180\) bad labeled profiles and \(360\) vulnerable distinguished voter-profile pairs.

Candidate relabeling maps all six anonymous profiles to one orbit. Fixing the manipulator's sincere ranking as \(A\succ B\succ C\) reduces every event to
\[
(2,0,0,1,2,0),
\]
with false report \(BCA\).

For this representative, truthful first-round Borda scores are
\[
(s_A,s_B,s_C)=(6,4,5).
\]
Thus \(B\) is eliminated. Recomputing Borda on \(\{A,C\}\) gives scores \((2,3)\), so \(C\) wins.

After one \(ABC\) voter reports \(BCA\), the profile becomes
\[
(1,0,0,2,2,0).
\]
The first-round Borda scores become
\[
(4,5,6),
\]
so \(A\) is eliminated. Recomputing on \(\{B,C\}\) gives \((3,2)\), so \(B\) wins. Since the manipulator's sincere order is \(A\succ B\succ C\), the deviation is strictly profitable.

## Verification
The embedded `verify_baldwin5_manipulation.py` uses only Python's standard library and exact integer arithmetic.

It verifies the full anonymous search through five voters, agreement of two Baldwin implementations, the direct labeled-profile replay, the six-profile candidate-relabeling orbit, the unique normalized manipulation, the exact profile frequencies, and the direct Borda-score mechanism of the representative.

Replay with:

`python3 verify_baldwin5_manipulation.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Narodytska, Walsh, and Xia study manipulation of Nanson's and Baldwin's rules and prove that unweighted Baldwin manipulation is computationally hard even with one manipulator. Their theorem is a complexity result over unrestricted candidate sets and uses explicit tie-breaking; it does not identify the smallest tie-independent three-candidate electorate or its exact profile frequency.

A later three-candidate study by Heilmaier gives the same five-voter profile type \((2\,ABC,1\,BCA,2\,CAB)\) as a minimal example where Black's rule and Baldwin's rule choose different winners. That source computes Baldwin's truthful winner \(C\), but it does not analyze unilateral manipulation; its strategyproofness discussion explicitly says that strategyproofness is not pursued further. The false-report step \(ABC\to BCA\), the four-voter lower bound, the exact six-profile orbit, and the prevalence calculations are not stated there.

The accepted contribution is therefore not the general manipulability of Baldwin's rule, nor the existence of the five-voter truthful profile. It is the sharp tie-independent three-candidate strategyproofness boundary and its complete finite classification.

## Limitations
The theorem is restricted to exactly three candidates, strict complete ballots, one unilateral manipulator, and tie-independent unique outcomes. Fixed tie-breaking can create additional manipulable profiles and may change smaller-electorate behavior.

The frequencies use impartial culture on labeled strict ballots only as exact finite counting measures; they are not empirical estimates for real electorates.

An unindexed note, thesis, or software census could contain the same complete boundary even though the targeted searches did not locate one.

## References
1. N. Narodytska, T. Walsh, and L. Xia, “Manipulation of Nanson's and Baldwin's Rules,” arXiv:1106.5312, first submitted 27 June 2011; later *Proceedings of the AAAI Conference on Artificial Intelligence* 25(1), 713–718, 2011. DOI: 10.1609/aaai.v25i1.7872.
2. S. Heilmaier, *Optimal Voting Rules for Few Candidates*, Master's thesis, Technische Universität München, 2020.
