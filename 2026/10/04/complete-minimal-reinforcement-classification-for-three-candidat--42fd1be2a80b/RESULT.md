# Complete minimal reinforcement classification for three-candidate Black voting
## Finding
Black's rule elects the Condorcet winner when one exists and otherwise uses Borda count. Consider complete strict ballots over three candidates and only profiles for which Black's rule has a unique winner.

A reinforcement paradox pair is an unordered pair of nonempty anonymous electorates with the same unique Black winner separately but a different unique Black winner after the electorates are merged.

No such pair exists with fewer than \(9\) voters in total. At the sharp total of \(9\), there are exactly
\[
12
\]
unordered anonymous paradox pairs. Their electorate-size distribution is exactly
\[
6\text{ pairs of size }1+8,\qquad 6\text{ pairs of size }4+5.
\]

Modulo simultaneous relabeling of the three candidates, the \(12\) pairs form exactly two classes, both of orbit size \(6\). Writing ballot types in the order
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA,
\]
canonical representatives are
\[
(0,0,0,0,0,1)\quad\text{and}\quad(1,0,0,4,3,0),
\]
and
\[
(0,0,0,2,1,1)\quad\text{and}\quad(1,0,0,2,2,0).
\]
In both representatives the two subelections elect \(C\), while the union elects \(B\).

The two pair classes merge to the same union up to candidate relabeling. Across labeled candidates there are only \(6\) distinct union profiles, each admitting exactly two paradox-producing partitions: one \(1+8\) partition and one \(4+5\) partition. Thus the minimal boundary consists of one union orbit equipped with exactly two inequivalent reinforcement decompositions.

There is also a mechanism-level distinction between those decompositions. In the \(1+8\) class, the one-voter subelection elects \(C\) as a Condorcet winner, the eight-voter subelection elects \(C\) through Black's Borda fallback, and the union has \(B\) as Condorcet winner. In the \(4+5\) class, both subelections elect \(C\) through the Borda fallback, while the merged profile again creates \(B\) as Condorcet winner.

## Assumptions and scope
A profile is an anonymous six-component vector of nonnegative counts for the six strict rankings of three candidates. Black's rule is evaluated exactly as follows: if one candidate defeats each other candidate by strict pairwise majority, that candidate wins; otherwise Borda scores \(2,1,0\) are assigned and the unique Borda-score maximizer wins. Profiles with a tied Borda fallback are excluded so the result is independent of tie-breaking.

Reinforcement uses two nonempty electorates on the same candidate set. The two separate winners must coincide and the merged winner must be unique and different. The pair of electorates is unordered. Candidate relabeling acts simultaneously on both profiles.

## Proof
The finite domain is completely enumerable because a three-candidate anonymous profile of size \(n\) is a weak composition of \(n\) into six ballot types.

The first exhaustive route enumerates every anonymous profile for sizes \(1\) through \(9\), computes its unique Black winner when defined, and then considers every unordered pair of eligible profiles whose sizes sum to each total \(N\le9\). For each pair with a common separate winner, it recomputes Black's rule on the componentwise sum. The exact counts are zero for every total \(2\le N\le8\) and \(12\) for \(N=9\).

The second exhaustive route is organized in the reverse direction. It enumerates every anonymous nine-voter union profile and every componentwise decomposition of that union into two nonempty subprofiles. It independently computes the Black winner of both parts and of the union, retaining precisely the reinforcement failures. This route produces exactly the same set of \(12\) unordered pairs.

The pair set is then closed under all six candidate permutations. Canonicalization gives exactly two orbits, each of size \(6\). The orbit representatives are the two pairs displayed in the Finding. Counting their componentwise sums shows that all \(12\) pairs yield exactly six labeled unions and that each union occurs twice. Canonicalizing the unions gives a single candidate orbit.

Finally, the rule branch used at each profile is recorded. Exactly six pairs have branch pattern “Condorcet/Borda separately, Condorcet after merging,” and exactly six have “Borda/Borda separately, Condorcet after merging.” These are precisely the \(1+8\) and \(4+5\) classes, respectively.

## Verification
The embedded `verify_black9_reinforcement.py` uses exact integer arithmetic and the Python standard library. It performs the pair-first and union-first traversals independently and requires equality of the resulting pair sets.

It verifies the zero counts through total \(8\), the exact \(12\)-pair boundary at total \(9\), the \(6+6\) size split, the two candidate-relabeling pair classes, the six labeled union profiles, the single union orbit, the exactly-two-partitions-per-union fact, all six ordered winner transitions, and the rule-branch classification.

Replay command:

`python3 verify_black9_reinforcement.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Black's rule itself combines Condorcet selection with a Borda fallback. Felsenthal's survey of single-winner paradoxes records the vulnerability of standard procedures, including Black's rule, to reinforcement-type failures; the associated 2012 Springer volume provides an archival source for that literature.

Brandt, Matthäus, and Saile later compute minimal paradox sizes under a tie-independent unique-winner convention. Their Black-rule section defines the same Condorcet-then-Borda procedure and displays a three-candidate nine-voter reinforcement witness; their summary table proves that \(9\) voters are minimal for the three-candidate Black reinforcement paradox. The present result treats that minimal total as prior and refines it by exhaustively classifying all minimal pairs.

The inspected primary material does not state that there are exactly \(12\) minimal pairs, exactly two candidate-symmetry classes, exactly one union orbit, or exactly two paradox-producing decompositions of each minimal union.

## Limitations
The theorem is restricted to three candidates, anonymous complete strict ballots, unique Black winners, and the minimal total electorate size. It does not count individually labeled voters or tie-breaking-dependent failures.

The originality search cannot rule out an unpublished enumeration, thesis, software table, or supplementary file containing the same boundary census. The 2012 survey chapter was identified bibliographically and through indexed excerpts, but a lawful full-text copy was not available in the current search path; novelty comparison therefore relies primarily on the fully inspected 2022 minimal-paradoxes paper plus targeted exact-count searches.

## References
1. D. S. Felsenthal, “Review of Paradoxes Afflicting Procedures for Electing a Single Candidate,” in *Electoral Systems: Paradoxes, Assumptions, and Procedures*, Springer, 2012, pp. 19–91. DOI: 10.1007/978-3-642-20441-8_3.
2. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.
3. D. Black, *The Theory of Committees and Elections*, Cambridge University Press, 1958.
