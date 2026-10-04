# Complete minimal reinforcement-pair census for three-candidate instant runoff
## Finding
Consider three-candidate instant-runoff voting (IRV, equivalently the three-candidate Hare rule) with complete strict ballots. Only elections with a uniquely determined IRV winner are admitted: a profile is excluded if the lowest first-choice score is tied at the elimination step or if the final two-candidate contest is tied.

A reinforcement-paradox pair is an unordered pair of nonempty anonymous subelectorates whose separate IRV winners are the same candidate, while their union has a different unique IRV winner.

No such pair exists with fewer than \(13\) voters in total. At the sharp total of \(13\), there are exactly
\[
288
\]
unordered anonymous reinforcement-paradox pairs. Every one has the electorate-size split
\[
5+8.
\]
Under simultaneous relabeling of the three candidates, the \(288\) pairs form exactly \(48\) classes, and every class has the full orbit size \(6\).

The \(288\) pairs produce \(126\) distinct anonymous union profiles. These \(126\) unions form exactly \(21\) candidate-relabeling classes, again all with orbit size \(6\). The number of paradox-producing partitions of an individual union has the exact distribution
\[
36\text{ unions with }1,\qquad
36\text{ with }2,\qquad
36\text{ with }3,\qquad
18\text{ with }4.
\]
The weighted sum
\[
36+2\cdot36+3\cdot36+4\cdot18=288
\]
recovers the pair count.

A representative pair uses ballot types \(ABC,ACB,BAC,BCA,CAB,CBA\) in that order. Let
\[
P=(0,0,0,2,0,3),\qquad
Q=(3,0,0,2,0,3).
\]
In \(P\), candidate \(A\) is eliminated from first-choice scores \(0,2,3\), and \(C\) beats \(B\) by \(3\) to \(2\). In \(Q\), \(B\) is eliminated from scores \(3,2,3\), its two ballots transfer to \(C\), and \(C\) beats \(A\) by \(5\) to \(3\). Their union is
\[
P+Q=(3,0,0,4,0,6),
\]
where \(A\) is eliminated from scores \(3,4,6\), its three ballots transfer to \(B\), and \(B\) beats \(C\) by \(7\) to \(6\).

## Assumptions and scope
A ballot is a strict linear order of the three candidates, and an anonymous profile is a six-component vector of nonnegative ballot-type counts. IRV first elects a candidate having an absolute majority of first choices; otherwise it eliminates the unique candidate with the fewest first choices, transfers those ballots to their next remaining choice, and elects the unique majority winner of the resulting two-candidate contest.

The reinforcement condition studied here is Young consistency for a single-valued rule: if two disjoint electorates separately choose the same candidate, their union should choose that candidate as well. The theorem counts violations at the first possible total electorate size.

Pairs of subelectorates are unordered. Candidate names are fixed for the labeled count and are simultaneously relabeled on both subelectorates for the quotient. Voters within an electorate are anonymous.

## Proof
There are six strict ballot types. For a fixed electorate size \(n\), every anonymous profile is therefore a weak composition of \(n\) into six parts.

The first exhaustive route enumerates every such profile for each size \(1\le n\le13\), evaluates IRV exactly, and retains only profiles having a unique winner. For each total \(N\), every unordered split \(n_1+n_2=N\) and every pair of unique-winner profiles of those sizes with the same winner are examined. Their componentwise sum is evaluated independently as a union election. A pair is counted exactly when the union has a unique winner different from the shared subelection winner.

This gives zero pairs for every \(2\le N\le12\) and \(288\) pairs for \(N=13\). Inspection of the exhaustive list shows that all \(288\) have sizes \(5\) and \(8\).

For the second exhaustive route, every anonymous \(13\)-voter union profile is enumerated directly. For each union vector \(u\), every componentwise subprofile \(p\) with \(0\le p_i\le u_i\) is generated, with \(q=u-p\). Empty parts are discarded and the smaller electorate is used to count each unordered decomposition once. The IRV winners of \(p\), \(q\), and \(u\) are then recomputed. This independent union-first search produces exactly the same set of \(288\) pairs.

Simultaneous application of all six candidate permutations to both members of each pair gives \(48\) canonical representatives, each with orbit size \(6\). Canonicalizing the \(126\) distinct unions in the same way gives \(21\) classes, again each with orbit size \(6\). Counting how many of the \(288\) pairs share each union gives the partition-multiplicity distribution \(36,36,36,18\) for multiplicities \(1,2,3,4\), respectively.

## Verification
The embedded `verify_irv13_reinforcement_pairs.py` uses only exact integer arithmetic and the Python standard library.

It contains two independent exhaustive traversals: a profile-pair enumeration over all total electorate sizes through \(13\), and a union-first enumeration over all \(13\)-voter profiles and all of their componentwise two-part decompositions. The two routes are required to produce exactly the same \(288\)-pair set.

The verifier also checks the \(5+8\) size split, the \(48\) candidate-relabeling pair classes, the \(126\) distinct unions, the \(21\) union classes, the partition-multiplicity histogram, all six winner-transition types, and the displayed witness.

Replay with:

`python3 verify_irv13_reinforcement_pairs.py`

The first line must be `VERIFY_OK`.

## Relationship to prior work
Courtin, Mbih, Moyouwou, and Senné study Young reinforcement for sequential positional rules. In the three-candidate formulation, the Hare rule is the sequential positional rule with first-step plurality scoring. Their Proposition 1 supplies reinforcement violations at \(13\) voters and for all sufficiently large electorates, and their small-electorate discussion uses computer enumeration. Their printed results do not provide the complete tie-independent census of all minimal unordered subelectorate pairs or the number of paradox-producing partitions per union.

Brandt, Matthäus, and Saile study minimal voting paradoxes under an explicitly tie-independent convention. For instant runoff, their minimality table gives three candidates and \(13\) voters for reinforcement, together with a concrete minimal example. Thus the sharp total \(13\) is prior work and is independently reproduced here rather than claimed as new.

McCune and Wilson give necessary and sufficient conditions for whether a fixed three-candidate IRV election admits some partition witnessing the reinforcement paradox. Their analysis is existential at the union-profile level. They explicitly identify the structure and similarity of paradox-producing partitions as a direction worth further exploration. The present result refines that existential question at the minimal boundary by counting all paradox-producing pairs, all distinct unions, and the exact partition multiplicity of each union.

## Limitations
The census is restricted to three candidates and to the minimal total electorate size \(13\). It deliberately excludes elimination ties and final ties, so it does not depend on a tie-breaking convention.

The result counts anonymous ballot-type profiles and unordered electorate pairs. It does not count assignments of individually labeled voters to the two constituencies.

The primary literature and targeted searches did not reveal the \(288\)-pair, \(48\)-class, \(126\)-union, or partition-multiplicity census. An unpublished enumeration program, thesis, note, or supplementary data set could nevertheless contain an equivalent table.

## References
1. S. Courtin, B. Mbih, I. Moyouwou, and T. Senné, “The reinforcement axiom under sequential positional rules,” *Social Choice and Welfare* 35 (2010), 473–500. DOI: 10.1007/s00355-010-0449-6. Published online 13 March 2010.
2. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.
3. D. McCune and J. Wilson, “Instant Runoff Voting and the Reinforcement Paradox,” arXiv:2502.05185, first submitted 23 January 2025; subsequently *Mathematical Social Sciences* 143 (2026), article 102563. DOI: 10.1016/j.mathsocsci.2026.102563.
