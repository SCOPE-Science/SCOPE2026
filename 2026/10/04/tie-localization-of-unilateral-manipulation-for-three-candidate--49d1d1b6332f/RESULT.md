# Tie-localization of unilateral manipulation for three-candidate Kemeny voting
## Finding
Consider Kemeny-Young voting with exactly three candidates, complete strict ballots, and an odd number of voters. For a profile \(P\), let \(W(P)\) be the set of candidates that appear first in at least one Kemeny-optimal ranking.

Suppose truthful voting gives a singleton winner set
\[
W(P)=\{a\}.
\]
If one voter changes only her own ballot, producing \(P'\), then it is impossible to have
\[
W(P')=\{b\}
\]
for a candidate \(b\) that the voter sincerely prefers to \(a\).

Thus a one-voter profitable manipulation cannot jump directly from one unambiguous Kemeny winner to another unambiguous, sincerely preferred winner. Any profitable manipulation of a resolute implementation on an odd electorate must touch an underlying Kemeny tie at the truthful profile or at the manipulated profile.

This is not ordinary strategyproofness. Tie handling can still create strategic opportunities. The statement isolates where those opportunities must live.

## Assumptions and scope
There are exactly three candidates and an odd number of voters. Every ballot is a complete strict ranking.

A Kemeny-optimal ranking minimizes the sum of Kendall-tau distances to the ballots, equivalently maximizes total agreement with the three pairwise majority margins. The Kemeny winner correspondence \(W(P)\) consists of all candidates topping at least one optimal ranking. The theorem makes no arbitrary tie-breaking assumption.

A unilateral manipulation replaces one sincere ballot by another strict ranking. It is profitable in the singleton-to-singleton sense if the new singleton winner is strictly higher than the old singleton winner in that voter's sincere order.

The odd-electorate assumption ensures that every pairwise majority margin is a nonzero odd integer. The theorem does not claim that ties are impossible at the Kemeny level: equal positive margins in a majority cycle can still create several optimal rankings.

## Proof
Write the third candidate as \(c\), and let pairwise majority margins be positive in the indicated direction.

For three candidates with no pairwise majority ties, the Kemeny rule has a simple form. If the majority tournament is transitive, the Condorcet winner is the unique Kemeny winner. If the majority tournament is the cycle
\[
a\succ_M b,\qquad b\succ_M c,\qquad c\succ_M a
\]
with positive margins \(p,q,r\), then an optimal ranking breaks exactly one majority edge, and it is optimal to break an edge of minimum margin. Hence \(a\) is the unique Kemeny winner exactly when
\[
r<\min\{p,q\}.
\]
Cyclic relabelings give the corresponding statements for \(b\) and \(c\).

Because the electorate is odd, all three pairwise margins are odd. Therefore, whenever two positive margins satisfy \(r<p\),
\[
r+2\le p.
\]
Changing one ballot changes any one pairwise margin by only \(0\) or \(2\) in absolute value.

Fix a voter who sincerely prefers \(b\) to the truthful singleton winner \(a\). We show that no false ballot can make \(b\) the new singleton winner.

First suppose \(a\) is the Condorcet winner. The sincere ballot already ranks \(b\) over \(a\), so a false report cannot improve \(b\)'s pairwise margin against \(a\); the margin favoring \(a\) over \(b\) can only stay fixed or increase. Therefore \(b\) cannot become a Condorcet winner.

The only remaining possibility would be a new majority cycle
\[
a\succ_M b,\qquad b\succ_M c,\qquad c\succ_M a
\]
in which the edge \(a\succ_M b\) is the unique weakest edge, because that is the condition for \(b\) to be the unique Kemeny winner. To create \(c\succ_M a\) from the truthful relation \(a\succ_M c\), the manipulator must reverse her own comparison of \(a\) and \(c\). An odd positive margin can cross zero after a change of \(2\) only from \(1\) to \(-1\). Thus the new edge \(c\succ_M a\) has margin \(1\). The unchanged-or-increased edge \(a\succ_M b\) has positive odd margin at least \(1\), so it cannot be strictly weaker than the new \(c\succ_M a\) edge. Hence \(b\) cannot be the unique Kemeny winner.

Now suppose the truthful majority tournament is cyclic and \(a\) is its unique Kemeny winner. There are two positions for the preferred target \(b\).

In the first orientation,
\[
a\succ_M b,\qquad b\succ_M c,\qquad c\succ_M a,
\]
let the margins be \(p,q,r\). Since \(a\) is the unique Kemeny winner,
\[
r<\min\{p,q\}.
\]
The sincere voter already ranks \(b\) over \(a\), so a false report cannot reduce the majority margin \(p\) favoring \(a\) over \(b\). For \(b\) to become the unique cyclic Kemeny winner, \(p\) would have to become the unique weakest edge. The only helpful change to the currently weaker edge \(c\succ_M a\) can raise its margin by at most \(2\). But odd parity gives
\[
r+2\le p,
\]
so after the report that edge still has margin at most \(p\). Thus \(p\) cannot become uniquely weakest. Nor can \(b\) become Condorcet winner, because the voter cannot improve \(b\)'s already-sincere comparison against \(a\).

In the second orientation,
\[
b\succ_M a,\qquad a\succ_M c,\qquad c\succ_M b.
\]
Let \(r\) be the margin of \(b\succ_M a\) and \(q\) the margin of \(c\succ_M b\). Since \(a\) is the unique Kemeny winner, the incoming edge \(b\succ_M a\) is uniquely weakest, so
\[
r<q.
\]
For \(b\) to become the unique Kemeny winner, the edge \(c\succ_M b\) would have to become the unique weakest edge or reverse so that \(b\) becomes Condorcet winner. If the sincere ballot already ranks \(b\) over \(c\), a false report cannot help \(b\) on that pairwise contest. If instead it ranks \(c\) over \(b\), switching that comparison reduces \(q\) by at most \(2\). Odd parity gives
\[
q-2\ge r,
\]
so \(c\succ_M b\) cannot become strictly weaker than \(b\succ_M a\), and it cannot reverse sign either. Hence \(b\) again cannot become the unique Kemeny winner.

These cases exhaust the position of every sincerely preferred target \(b\), proving the claim.

## Verification
The embedded `verify_kemeny_singleton_strategy.py` independently implements Kemeny winners in two ways.

The first implementation uses the three pairwise margins. If
\[
u=M_{AB},\qquad v=M_{BC},\qquad w=M_{CA},
\]
the best Kemeny agreement scores among rankings topped by \(A,B,C\) are respectively
\[
u-w+|v|,\qquad v-u+|w|,\qquad w-v+|u|.
\]
The second implementation directly computes the total Kendall distance of all six rankings.

The replay exhausts every anonymous strict profile for each odd electorate size
\[
1,3,5,\ldots,17,
\]
checks agreement of the two implementations, checks the transitive/cyclic majority-margin characterization used in the proof, and tests every present voter type against every false strict report. Across these finite stress tests there are many singleton-to-singleton outcome changes but zero profitable ones.

The replay is a check of the finite cases and of the formulas used in the proof; the theorem for arbitrary odd electorates is established by the margin argument above, not by extrapolation from finite enumeration.

Run:

`python3 verify_kemeny_singleton_strategy.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Wang, Sturm, Cuff, and Kulkarni analyze strategic voting geometrically for three-candidate Condorcet methods. Their 2012 Allerton paper identifies strategic and non-strategic Kemeny boundaries. The longer Wang-Cuff-Kulkarni manuscript proves that, with three candidates, strategic voting is possible at a Kemeny boundary exactly when the two adjacent winning rankings have Kendall distance \(2\); it also explicitly models randomized tie handling.

That boundary classification is the closest prior result. It does not state the parity-sensitive singleton-to-singleton theorem proved here. The present result cuts across the strategic-boundary picture: with an odd electorate, a single false ballot can move pairwise margins by \(2\), while distinct positive margins are separated by at least \(2\). This prevents a strategically favorable crossing all the way from one singleton winner region to another; strategic opportunities must terminate or originate on an underlying tie.

Brandt, Matthäus, and Saile later note that with exactly three candidates, Kemeny's method agrees with maximin, Young's rule, and several other Condorcet extensions in the relevant strict setting. Their compilation studies other voting paradoxes under a unique-winner restriction, not this unilateral misreport localization result.

## Limitations
The theorem is restricted to three candidates and odd electorates. It does not claim strategyproofness under arbitrary tie resolution, and it does not cover four or more candidates.

The proof concerns one voter changing one ballot. Coalitional manipulation can change a pairwise margin by more than \(2\) and is outside scope.

The Wang-Cuff-Kulkarni strategic-boundary table is close prior art. Although it does not state the singleton-to-singleton consequence and the targeted searches did not locate that formulation, an equivalent corollary may have appeared elsewhere or may be derivable from an uninspected treatment of their boundary table.

## References
1. T. Wang, J. Sturm, P. Cuff, and S. R. Kulkarni, “Condorcet voting methods avoid the paradoxes of voting theory,” *50th Annual Allerton Conference on Communication, Control, and Computing*, pp. 201–203, 2012. DOI: 10.1109/Allerton.2012.6483218. Conference dates: 1–5 October 2012.
2. T. Wang, P. Cuff, and S. R. Kulkarni, “Condorcet Methods are Less Susceptible to Strategic Voting,” manuscript, 2013.
3. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Politics, Philosophy & Economics* 21 (2022). DOI: 10.1177/09516298221122104.
