# Complete minimal-boundary reinforcement census for three-candidate maximin
## Finding
For three-candidate maximin voting with complete strict anonymous ballots and unique winners, the first reinforcement boundary is completely finite and rigid.

There are no reinforcement-paradox pairs with fewer than \(15\) voters in total. At total size \(15\), there are exactly
\[
18
\]
unordered anonymous pairs \(\{P,Q\}\) for which \(P\) and \(Q\) have the same unique maximin winner but \(P+Q\) has a different unique maximin winner.

Every one of the \(18\) pairs has the electorate split
\[
5+10.
\]
Under simultaneous relabeling of the three candidates, the \(18\) pairs form exactly \(3\) classes, each of full orbit size \(6\).

The union profiles are just as rigid: all \(18\) pairs have different unions. Thus every minimal union profile admits exactly one paradox-producing partition into two nonempty electorates. The \(18\) unions themselves form exactly \(3\) candidate-relabeling classes, each of orbit size \(6\).

A structural feature holds uniformly across the entire boundary. In every minimal pair, the \(5\)-voter electorate has the shared maximin winner as a Condorcet winner; the \(10\)-voter electorate has no Condorcet winner; and the merged \(15\)-voter electorate has the new maximin winner as a Condorcet winner.

Writing the six ballot types in the order
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA,
\]
one set of canonical representatives for the three candidate-relabeling classes is
\[
(0,0,0,2,0,3)\quad\text{with}\quad(3,0,0,3,4,0),
\]
\[
(0,0,0,3,1,1)\quad\text{with}\quad(0,3,4,0,0,3),
\]
and
\[
(0,0,0,3,2,0)\quad\text{with}\quad(0,3,4,0,0,3).
\]

## Assumptions and scope
There are exactly three candidates. Every voter submits one strict linear order of the candidates, and voter identities inside an electorate are ignored.

For candidates \(x\) and \(y\), define the majority margin
\[
m(x,y)=\#\{i:x\succ_i y\}-\#\{i:y\succ_i x\}.
\]
The maximin score of candidate \(x\) is
\[
s(x)=\min_{y\ne x}m(x,y).
\]
A profile is admitted only when exactly one candidate has the largest maximin score.

An unordered pair \(\{P,Q\}\) is a reinforcement paradox when both \(P\) and \(Q\) are nonempty, both have the same unique maximin winner \(x\), and the merged profile \(P+Q\) has a different unique maximin winner \(y\).

The symmetry quotient simultaneously relabels the three candidate names in both subprofiles. The two electorates themselves are unordered.

## Proof
An anonymous three-candidate profile is a six-component vector of nonnegative integers, one coordinate for each strict ranking. For electorate size \(n\), there are
\[
\binom{n+5}{5}
\]
such profiles.

The verifier computes the three independent pairwise majority margins for every profile and then evaluates the maximin scores directly. It performs two exhaustive traversals.

The first route is pair-first. For every total size from \(2\) through \(15\), it enumerates every unordered split \(n_1+n_2\), every unique-winner anonymous profile of size \(n_1\), and every unique-winner anonymous profile of size \(n_2\) having the same winner. It then adds their majority-margin vectors and tests the union winner. The exact number of reinforcement pairs is zero for every total from \(2\) through \(14\) and is \(18\) at total \(15\). All \(18\) have split \(5+10\).

The second route is union-first. It independently enumerates every anonymous \(15\)-voter profile \(U\), every componentwise split \(P+Q=U\) with both parts nonempty, and all three maximin winners from scratch. After identifying unordered pairs only once, this route produces exactly the same set of \(18\) paradox pairs as the first route.

The candidate-symmetry computation applies all \(6\) permutations of the candidate names to both parts of a pair and chooses a canonical representative. This gives exactly \(3\) pair classes, each with orbit size \(6\). Applying the same action to the union profiles gives exactly \(3\) union classes. Since all \(18\) union profiles occur with multiplicity one among the \(18\) paradox pairs, each minimal union has exactly one paradox-producing partition.

Finally, the verifier computes Condorcet status independently from the maximin winner. On every one of the \(18\) pairs, the \(5\)-voter part has the shared winner as a Condorcet winner, the \(10\)-voter part is cyclic, and the union has the new winner as a Condorcet winner.

## Verification
The embedded `verify_maximin15_reinforcement.py` uses only Python's standard library and exact integer arithmetic.

Replay with:

`python3 verify_maximin15_reinforcement.py`

The first output line must be `VERIFY_OK`.

The verifier checks all anonymous profile pairs for every total electorate size through \(15\), then independently reconstructs the \(15\)-voter boundary from union profiles and all componentwise partitions. It requires exact equality of the pair sets returned by the two routes.

It also checks the \(5+10\) split, the \(3\) candidate-relabeling pair classes, the \(18\) distinct unions, the \(3\) union classes, the six possible ordered winner transitions, and the Condorcet-status structure stated above.

## Relationship to prior work
Courtin, Mbih, and Moyouwou study how frequently Condorcet procedures violate reinforcement under impartial-culture models. Their work places the rarity of maximin reinforcement failures in a probabilistic setting but does not provide the complete finite boundary census stated here.

Brandt, Matthäus, and Saile later compute minimal voting paradoxes for common rules. They explicitly treat the maximin reinforcement paradox as one of the difficult minimality cases and establish the minimal-instance framework under unique winners. The known minimal voter boundary is therefore not claimed as new here. What is added is the exhaustive classification of every three-candidate profile pair at that boundary.

Brandt, Dong, and Peters subsequently study reinforcement for three-candidate Condorcet extensions and show that some refinements of maximin have unusually strong small-electorate reinforcement behavior. Their work is rule-level and axiomatic; it does not state the \(18\)-pair boundary census for the ordinary maximin procedure.

## Limitations
The theorem is restricted to exactly three candidates, strict complete ballots, anonymous profiles, and unique maximin winners in both subelections and the union. Profiles requiring a tie-breaking convention are intentionally excluded.

The counts are for anonymous subelectorates. They do not count assignments of individually labeled voters to the two electorates.

The originality search located no published table with the \(18\)-pair, \(3\)-class, or unique-partition census. An unindexed thesis, supplementary data set, or unpublished enumeration program could nevertheless contain an equivalent boundary classification.

## References
1. S. Courtin, B. Mbih, and I. Moyouwou, “Are Condorcet procedures so bad according to the reinforcement axiom?”, THEMA Working Paper 2012-37; later *Social Choice and Welfare* 42 (2014), 927–940. DOI: 10.1007/s00355-013-0758-7.
2. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.
3. F. Brandt, C. Dong, and D. Peters, “Condorcet-Consistent Choice Among Three Candidates,” arXiv:2411.19857; later *Games and Economic Behavior* 153 (2025), 113–130. DOI: 10.1016/j.geb.2025.05.005.
