# Sharp five-voter unique-winner disagreement between STV and Coombs runoff
## Finding
Consider elections with exactly three candidates and complete strict ballots.

Use the runoff-scoring definitions in which single transferable vote (STV) repeatedly eliminates a candidate with the smallest plurality score, while Coombs repeatedly eliminates a candidate with the smallest veto score, equivalently the candidate with the most last-place votes. When an elimination tie occurs, use parallel-universes tie-breaking: the winner set is the union of the winners obtainable over all tied elimination choices.

No electorate with fewer than \(5\) voters has singleton STV and Coombs winner sets containing different candidates.

At \(5\) voters, exactly
\[
180
\]
of the
\[
6^5=7776
\]
labeled profiles have different unique winners. Thus the exact unconditional impartial-culture incidence is
\[
\frac{180}{7776}=\frac5{216}.
\]

Exactly
\[
6516
\]
labeled five-voter profiles have unique winners under both rules, so conditional on both winner sets being singletons, the disagreement incidence is
\[
\frac{180}{6516}=\frac5{181}.
\]

At the anonymous-profile level there are
\[
\binom{10}{5}=252
\]
five-voter ballot-multiplicity profiles. Exactly \(6\) disagree, giving incidence
\[
\frac6{252}=\frac1{42}.
\]
Those six profiles form one orbit under candidate relabeling.

A canonical representative is
\[
1(A\succ C\succ B)+2(B\succ A\succ C)+2(C\succ A\succ B).
\]
Its first-place counts are
\[
(A,B,C)=(1,2,2),
\]
and its last-place counts are
\[
(A,B,C)=(0,3,2).
\]
Therefore STV eliminates \(A\), after which \(C\) beats \(B\) by \(3\) votes to \(2\). Coombs eliminates \(B\), after which \(A\) beats \(C\) by \(3\) votes to \(2\).

The complete pairwise comparison is
\[
A\succ_M B,
\qquad
A\succ_M C,
\qquad
C\succ_M B,
\]
with each majority margin equal to one vote. Hence \(A\) is the Condorcet winner, Coombs elects \(A\), and STV elects \(C\).

Every one of the six anonymous minimal disagreement profiles is a candidate relabeling of this profile. Consequently every minimal unique-winner disagreement has the same structural form: Coombs elects the Condorcet winner, while STV eliminates that Condorcet winner in the first round.

## Assumptions and scope
Candidates are labeled \(A,B,C\). Every voter submits one strict complete ranking, so there are exactly \(6\) ballot types.

The winner correspondence uses parallel-universes tie-breaking for elimination ties. A profile is counted only when both resulting winner sets are singletons and the singleton candidates differ.

The Coombs convention used is the veto-based runoff-scoring rule. Some expositions stop Coombs immediately when a candidate has a majority of current first-place votes. The six minimal disagreement profiles all have first-place counts \((1,2,2)\) up to relabeling, so no majority exists before the first elimination; therefore the stated first-disagreement layer is unchanged by adding that majority shortcut.

The theorem is exhaustive only for electorate sizes through \(5\) with exactly three candidates.

## Proof
There are six strict rankings of three candidates. For each electorate size \(n\), an anonymous profile is a weak composition of \(n\) into six ballot-type multiplicities.

For every anonymous profile, both rules are evaluated as set-valued runoff rules under parallel-universes tie-breaking. Every tied first-round loser is explored, and the two surviving candidates are compared by their exact pairwise majority.

The computation is performed in two independent forms for each rule.

First, a generic recursive runoff engine recomputes the relevant plurality or veto scores on the surviving candidate set at every stage and explores all lowest-score eliminations.

Second, a closed three-candidate implementation identifies every first-round loser directly from first-place counts for STV or last-place counts for Coombs, and then computes the pairwise winner among the two survivors.

The two implementations agree on every anonymous profile for electorate sizes \(1\) through \(5\).

The numbers of anonymous profiles with different unique winners are
\[
0,\ 0,\ 0,\ 0,\ 6
\]
for \(n=1,2,3,4,5\).

Weighting each anonymous profile by its multinomial number of voter labelings gives labeled disagreement counts
\[
0,\ 0,\ 0,\ 0,\ 180.
\]
A separate direct enumeration of all labeled profiles independently reproduces these labeled counts.

For \(n=5\), canonicalizing the six anonymous disagreement profiles under all \(3!=6\) candidate relabelings gives one canonical multiplicity vector. In the ranking order
`ABC, ACB, BAC, BCA, CAB, CBA`, it is
`(0,1,2,0,2,0)`.

Its candidate-relabeling orbit has size \(6\), so all minimal disagreements are symmetry copies of the displayed representative.

The pairwise tally of the representative is \(A\) over \(B\) by \(3\) to \(2\), \(A\) over \(C\) by \(3\) to \(2\), and \(C\) over \(B\) by \(3\) to \(2\). This proves the Condorcet statement. Relabeling preserves it for the other five anonymous profiles.

## Verification
The embedded `verify_stv_coombs_first_unique_disagreement.py` uses only the Python standard library and exact integer/rational arithmetic.

It checks:
- every anonymous profile for one through five voters;
- every labeled profile for one through five voters;
- two independent implementations of STV under parallel-universes tie-breaking;
- two independent implementations of Coombs under parallel-universes tie-breaking;
- the exact unique-winner disagreement counts \(0,0,0,0,180\) for labeled profiles;
- exactly \(6516\) labeled five-voter profiles with singleton winner sets under both rules;
- exact incidences \(5/216\), \(5/181\), and \(1/42\);
- one candidate-relabeling orbit of six anonymous disagreement profiles;
- the canonical profile, first-place counts, last-place counts, and all three pairwise tallies;
- that Coombs selects the Condorcet winner in every minimal disagreement.

Run:

`python3 verify_stv_coombs_first_unique_disagreement.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Freeman, Brill, and Conitzer formalize runoff scoring rules, identify STV as the plurality-based runoff rule and Coombs as the veto-based runoff rule, and use parallel-universes tie-breaking for elimination ties. Their work concerns axiomatic characterization rather than a smallest-electorate disagreement census.

Miller directly compares the Alternative Vote, also called Hare or instant-runoff voting, with Coombs in the three-candidate setting. He emphasizes that the two rules differ only in the first elimination criterion: fewest first preferences for the Alternative Vote versus most last preferences for Coombs. His analysis studies plurality, anti-plurality, Condorcet status, simulated English-election data, and Condorcet efficiency; it does not state the exact five-voter first unique-winner disagreement layer above.

Targeted searches using STV, instant-runoff, Alternative Vote, Hare, Coombs, three-candidate, five-voter, exact-profile-count, Condorcet-winner, and the count \(180\) did not locate an equivalent exhaustive classification.

## Limitations
The result concerns exactly three candidates and electorates through five voters.

The count is for complete strict ballots. Truncated ballots, weak orders, or alternative tie-breaking conventions define different domains.

The theorem isolates different unique winners. The two set-valued correspondences can be studied under weaker notions of disagreement involving non-singleton outcomes, but those are not classified here.

Failed bibliographic search is not a proof of uniqueness. An unindexed historical enumeration, software test corpus, thesis appendix, or teaching note could contain the same finite census.

## References
1. R. Freeman, M. Brill, and V. Conitzer, “On the Axiomatic Characterization of Runoff Voting Rules,” *Proceedings of the Twenty-Eighth AAAI Conference on Artificial Intelligence*, 2014, 675–680. DOI: 10.1609/aaai.v28i1.8827.
2. N. R. Miller, “The Alternative Vote and Coombs Rule versus First-Past-the-Post: a social choice analysis of simulated data based on English elections, 1992–2010,” *Public Choice* 158 (2014), 399–425.
