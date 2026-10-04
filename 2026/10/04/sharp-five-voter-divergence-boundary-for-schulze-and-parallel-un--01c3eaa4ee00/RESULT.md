# Sharp five-voter divergence boundary for Schulze and parallel-universe Ranked Pairs
## Finding
Consider elections with complete strict ballots. Pairwise victory strength is measured by the majority margin.

Let \(S(P)\) be the winner set of the Schulze method, using strongest paths in the weighted majority graph.

Let \(RP(P)\) be the set-valued outcome of Tideman's Ranked Pairs method when every possible ordering of equally strong pairwise victories is allowed. Equivalently, \(RP(P)\) is the union of the top candidates over all admissible tie-breakings among equal-strength victories. This is the parallel-universe tie-breaking interpretation of the set-valued rule.

For every profile with exactly three candidates,
\[
S(P)=RP(P).
\]

With four candidates, the rules also agree on every one-voter and every three-voter profile. Five voters are the first odd electorate size at which they can differ.

There are
\[
24^5=7962624
\]
labeled profiles of five strict ballots over four candidates. Exactly
\[
51840
\]
profiles have different winner sets, so the exact uniform-profile divergence probability is
\[
\frac{51840}{7962624}=\frac{5}{768}.
\]

Every divergent profile has the same relation:
\[
RP(P)\subsetneq S(P),
\qquad
|RP(P)|=2,
\qquad
|S(P)|=3.
\]
There are no first-layer profiles with the opposite containment, nonnested overlap, or disjoint winner sets.

The complete labeled winner-set-size histogram is
\[
\begin{array}{c|r}
(|S(P)|,|RP(P)|,\text{relation}) & \text{profiles}\\ \hline
(1,1,\text{equal}) & 6858144\\
(2,2,\text{equal}) & 275760\\
(3,3,\text{equal}) & 591120\\
(4,4,\text{equal}) & 185760\\
(3,2,\text{strict containment}) & 51840.
\end{array}
\]

The entire divergent layer is supported on exactly two weighted-majority-graph types up to candidate relabeling. Writing the six upper-triangle majority margins in the order
\[
(AB,AC,AD,BC,BD,CD),
\]
canonical representatives are
\[
(-3,-3,1,-1,-1,-1)
\]
and
\[
(-3,-1,1,1,-1,-1).
\]

The first type occurs for exactly
\[
11520
\]
labeled ballot profiles. Its winner sets are
\[
S(P)=\{B,C,D\},
\qquad
RP(P)=\{C,D\}.
\]

The second type occurs for exactly
\[
40320
\]
labeled ballot profiles. Its winner sets are
\[
S(P)=\{B,C,D\},
\qquad
RP(P)=\{B,D\}.
\]

Each canonical type has \(24\) distinct candidate relabelings, so the divergent layer contains exactly \(48\) labeled weighted-majority margin matrices. At the anonymous ballot-profile level there are \(576\) divergent profiles: \(168\) of the first margin type and \(408\) of the second.

Thus the first Schulze–Ranked-Pairs separation at four candidates is unusually rigid: all disagreement is a two-versus-three winner refinement, and every divergent election has one of only two pairwise-margin geometries.

## Assumptions and scope
Ballots are complete and strict. The electorate size is odd, so no pairwise majority contest is tied.

Both methods use pairwise victory strength ordered by majority margin. For a fixed odd electorate size, ordering victories by winning votes gives the same order because winning votes equal \((n+m)/2\), where \(m\) is the majority margin; the increasing affine transformation also preserves minimum-edge path comparisons.

Ranked Pairs is treated as a correspondence rather than with one externally fixed tie-break. When equal-strength victories can be processed in multiple orders, every top candidate obtained from an admissible tie ordering is retained.

The theorem proves equality for every three-candidate profile, exhausts four-candidate electorates of sizes \(1\), \(3\), and \(5\), and identifies the first odd-electorate divergence at four candidates. It does not give a formula for larger electorates or for five or more candidates.

## Proof
First consider three candidates.

If the majority tournament is transitive, its Condorcet winner is the unique Schulze winner and the unique Ranked Pairs winner.

Otherwise the majority tournament is a three-cycle. Write its directed victories as
\[
A\to B,\qquad B\to C,\qquad C\to A
\]
with positive strengths
\[
x,\qquad y,\qquad z.
\]
Ranked Pairs locks the stronger victories first. In a three-cycle, the final edge that would close the directed cycle is omitted; therefore the possible Ranked Pairs winners are precisely the candidates exposed by omitting a minimum-strength edge, with all possibilities retained when minimum strengths tie.

For Schulze, the direct path from a candidate to its majority victim competes with the two-edge path in the opposite direction. For example, \(B\) defeats \(A\) in the Schulze comparison exactly when
\[
\min(y,z)>x.
\]
Thus a unique weakest cycle edge produces the same unique exposed candidate as Ranked Pairs, while ties among weakest edges produce exactly the same set of exposed candidates. Hence
\[
S(P)=RP(P)
\]
for every three-candidate profile.

Now fix four candidates. A complete strict ballot has \(4!=24\) possibilities. The verifier exhausts all one-voter and all
\[
24^3=13824
\]
three-voter profiles and finds no divergence.

For five voters, the first verifier exhausts all
\[
24^5=7962624
\]
labeled profiles. It computes Schulze winners by a Floyd–Warshall strongest-path calculation. For Ranked Pairs, it groups majority victories by equal strength, enumerates every ordering inside each tied strength group, locks an edge exactly when doing so does not create a directed cycle, and takes the union of all resulting source candidates.

The complete histogram is exactly
\[
6858144,\quad275760,\quad591120,\quad185760,\quad51840
\]
in the five rows displayed above.

A second implementation provides an independent replay from anonymous profiles. It enumerates all
\[
\binom{28}{23}=98280
\]
multisets of five ballots. Schulze path strength is recomputed by direct enumeration of simple directed paths rather than Floyd–Warshall. Ranked Pairs is recomputed using Tideman's ranking-elimination formulation: within each equal-strength group, all pair orderings are considered, inconsistent linear rankings are eliminated, and all surviving top candidates are retained.

Exactly \(576\) anonymous profiles diverge. Weighting each anonymous profile by its multinomial number of labeled ballot sequences gives exactly
\[
51840.
\]

Canonicalizing the weighted majority margins under all \(24\) candidate permutations leaves exactly the two margin types displayed in the finding. The first accounts for \(11520\) labeled profiles and the second for \(40320\), completing the first-layer classification.

## Verification
The embedded `verify_schulze_rankedpairs_full.c` performs the full labeled census with exact integer operations.

It verifies:
- all four-candidate one-voter profiles;
- all \(13824\) four-candidate three-voter profiles;
- all \(7962624\) four-candidate five-voter profiles;
- no divergence for one or three voters;
- exactly \(51840\) five-voter divergences;
- exact probability \(5/768\);
- the complete winner-set-size histogram;
- strict containment \(RP(P)\subsetneq S(P)\) on every divergence;
- exactly two candidate-relabeling margin types with labeled counts \(11520\) and \(40320\).

Compile and run:

`cc -O3 -std=c11 verify_schulze_rankedpairs_full.c -o verify_schulze_rankedpairs_full`

`./verify_schulze_rankedpairs_full`

The first output line must be `VERIFY_OK`.

The embedded `verify_schulze_rankedpairs_anonymous.py` independently enumerates every anonymous five-voter profile and reimplements both rules by different algorithms.

Run:

`python3 verify_schulze_rankedpairs_anonymous.py`

The first output line must be `VERIFY_OK`.

It confirms \(98280\) anonymous profiles, \(576\) divergences, the multinomially weighted total \(51840\), the two margin types, their anonymous counts \(168\) and \(408\), and the \(48\) exact labeled margin matrices.

## Relationship to prior work
Tideman introduced Ranked Pairs and explicitly treated ties in pair ordering by considering every possible way to break the tied pair rankings and retaining all candidates that can win under some such ordering. This is the set-valued interpretation used here.

Schulze's method compares candidates by the strengths of their strongest paths in the pairwise majority graph. The published formulation gives an algorithmic strongest-path computation and a winner condition based on pairwise path strengths.

Parkes and Xia directly compare Schulze and Ranked Pairs, including parallel-universe tie-breaking for Ranked Pairs, and give examples where the two methods select different winners. Their work establishes that the methods are genuinely distinct, but it does not locate the smallest odd electorate at four candidates or enumerate the complete first divergent layer.

The contribution here is therefore not the existence of Schulze–Ranked-Pairs disagreement. It is the sharp four-candidate voter threshold and complete first-layer census: five voters are necessary and sufficient among odd electorates, the exact incidence is \(5/768\), every disagreement is the containment \(RP(P)\subsetneq S(P)\), and only two candidate-relabeling weighted-majority-graph types occur.

Targeted searches for the exact count \(51840\), the fraction \(5/768\), the four-candidate five-voter boundary, and the two-margin-type classification did not locate an equivalent published statement.

## Limitations
The census is exact only for complete strict ballots with four candidates and odd electorates through five voters.

The set-valued Ranked Pairs convention matters. A single fixed external tie-break can select one member of the correspondence and therefore answers a different question.

The result classifies the first divergent layer by weighted majority margins, not by ballot-profile isomorphism under all possible preference-domain symmetries.

The older Ranked Pairs literature predates the day-resolved public-source date stored for this package, but the checked publisher metadata for that paper supplies only a publication month rather than a public day. No day has been fabricated.

An unindexed teaching computation, election-software test suite, thesis appendix, or unpublished enumeration could contain the same finite census.

## References
1. T. N. Tideman, “Independence of Clones as a Criterion for Voting Rules,” *Social Choice and Welfare* 4 (1987), 185–206. DOI: 10.1007/BF00433944.
2. M. Schulze, “A new monotonic, clone-independent, reversal symmetric, and Condorcet-consistent single-winner election method,” *Social Choice and Welfare* 36 (2011), 267–303. Published online 11 July 2010. DOI: 10.1007/s00355-010-0475-4.
3. D. C. Parkes and L. Xia, “A Complexity-of-Strategic-Behavior Comparison between Schulze's Rule and Ranked Pairs,” *Proceedings of AAAI 2012*, pp. 1429–1435.
