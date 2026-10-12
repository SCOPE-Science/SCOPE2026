# Sharp five-voter tie-independent divergence boundary for Nanson and Baldwin
## Finding
Fix four candidates and complete strict ballots.

Baldwin's rule repeatedly eliminates one candidate with minimum Borda score and recomputes the scores. If several candidates are tied for the minimum, define the **Baldwin winner set** to contain every candidate that can survive under at least one legal choice among tied minima. Thus Baldwin has a **tie-independent unique winner** exactly when this set is a singleton.

Nanson's rule, in the convention used by Narodytska, Walsh, and Xia, simultaneously eliminates every candidate whose Borda score is **strictly below** the average score of the surviving candidates. If all surviving candidates have the same score before a singleton is reached, no fixed tie-break is imposed here; the profile is treated as non-unique.

Among profiles for which both rules have tie-independent unique outcomes, the two rules agree for every electorate of size at most
\[
4.
\]

With five voters, exactly
\[
24480
\]
of the
\[
24^5=7962624
\]
labeled profiles have unique outcomes under both rules but different winners. The unconditional labeled-profile incidence is therefore
\[
\frac{24480}{7962624}=\frac{85}{27648}.
\]

There are
\[
7232544
\]
labeled five-voter profiles on which both rules have unique outcomes, so the conditional divergence incidence is
\[
\frac{24480}{7232544}=\frac{85}{25113}.
\]

At the anonymous level, five voters correspond to
\[
\binom{28}{23}=98280
\]
ballot-multiplicity vectors. Exactly
\[
384
\]
of these are tie-independent unique divergences, giving anonymous incidence
\[
\frac{384}{98280}=\frac{16}{4095}.
\]

Up to relabeling the four candidates, those \(384\) anonymous divergent profiles form exactly
\[
16
\]
isomorphism classes. Every class has orbit size \(24=4!\), so every divergent anonymous profile has trivial candidate-label stabilizer.

A compact witness uses candidates \(A,B,C,D\) and the ballot multiset
\[
2(B\succ D\succ C\succ A),\qquad
1(C\succ A\succ B\succ D),\qquad
2(D\succ C\succ A\succ B).
\]
Its first-round Borda scores are
\[
(A,B,C,D)=(4,7,9,10).
\]

For Baldwin, \(A\) is uniquely lowest and is eliminated. Recounting on \(\{B,C,D\}\) gives
\[
(B,C,D)=(5,4,6),
\]
so \(C\) is eliminated. The final two-candidate scores are
\[
(B,D)=(3,2),
\]
so Baldwin uniquely elects \(B\).

For Nanson, the first-round average is
\[
\frac{4+7+9+10}{4}=\frac{15}{2}.
\]
Thus \(A\) and \(B\) are simultaneously eliminated. On \(\{C,D\}\), the scores are
\[
(C,D)=(1,4),
\]
so Nanson uniquely elects \(D\).

Hence five voters are the sharp first electorate size at which these two closely related Borda-elimination rules can have different tie-independent unique winners with four candidates.

## Assumptions and scope
Ballots are complete and strict. Borda scores use \(3,2,1,0\) with four candidates and are recomputed after eliminations.

The Baldwin correspondence explicitly ranges over all possible choices among tied lowest-scoring candidates. A Baldwin outcome is called unique only if every such legal elimination path has the same winner.

Nanson uses strict-below-average elimination, matching the convention in the inspected primary source. Profiles on which no candidate is below average while more than one candidate remains are not assigned an artificial winner and are excluded from the unique-outcome comparison.

The theorem fixes four candidates and proves the exact voter threshold through five voters. It does not assert equivalence for all electorate sizes, nor does it compare other tie-breaking conventions.

## Proof
There are \(24\) possible strict ballots on four candidates. An anonymous profile with \(n\) voters is therefore a weak composition of \(n\) into \(24\) ballot multiplicities.

The verifier exhausts every such composition for
\[
n=1,2,3,4,5.
\]
The numbers of anonymous profiles are respectively
\[
24,
300,
2600,
17550,
98280.
\]

For each profile, the Baldwin winner set is computed recursively. At every stage all currently tied minimum-Borda candidates are branched over, so a singleton output is exactly tie-independent uniqueness.

Nanson is computed by deleting all strictly below-average candidates in parallel. If no deletion is possible before a singleton remains, the surviving set is returned as a non-unique outcome.

Two independently coded score engines are used. The first works directly on ballot multiplicities with precomputed Borda contributions for every surviving-candidate subset. The second expands the multiplicities to an explicit voter list and recomputes Borda scores from the restricted ballots at every round. Their Baldwin and Nanson outputs agree for every anonymous profile through five voters.

Anonymous profiles are weighted by their multinomial numbers of labeled voter orderings. This gives the exact labeled unique-outcome counts
\[
24,
144,
12288,
143424,
7232544
\]
for electorate sizes one through five.

No tie-independent unique divergence occurs for one through four voters. At five voters there are exactly \(384\) divergent anonymous profiles, with total multinomial weight \(24480\).

For an additional symmetry check, every divergent anonymous profile is relabeled by all \(24\) candidate permutations and mapped to its lexicographically least ballot-multiplicity vector. Exactly \(16\) canonical vectors occur, each with \(24\) profiles in its orbit.

Candidate-label symmetry also forces uniformity over ordered winner pairs: each of the \(12\) ordered pairs of distinct Baldwin and Nanson winners occurs in exactly
\[
2040
\]
labeled divergent profiles.

The displayed witness is replayed directly and all of its elimination scores are asserted exactly.

## Verification
The embedded `verify_nanson_baldwin_first_unique_divergence.py` uses only the Python standard library and exact integer or rational arithmetic.

It verifies:
- every anonymous four-candidate profile with one through five voters;
- an independent explicit-ballot replay of both rules for every enumerated anonymous profile;
- zero tie-independent unique divergences for electorate sizes one through four;
- exactly \(384\) anonymous and \(24480\) labeled divergences at five voters;
- exact incidences \(85/27648\), \(85/25113\), and \(16/4095\);
- exactly \(16\) candidate-relabeling classes, all with orbit size \(24\);
- exactly \(2040\) labeled divergences for each ordered pair of distinct winners;
- the displayed witness and every intermediate Borda score.

Run:

`python3 verify_nanson_baldwin_first_unique_divergence.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Narodytska, Walsh, and Xia give a modern primary treatment of Nanson's and Baldwin's rules. They define Borda scores, define Nanson by eliminating all candidates strictly below the average Borda score, and define Baldwin by eliminating a lowest-Borda candidate, with an external tie-breaking mechanism when several candidates are tied. They emphasize that the two rules are closely related but have different formal properties.

Their work studies manipulation complexity, including the fact that weighted Nanson manipulation is polynomial with at most three candidates and becomes NP-complete with four candidates. It does not state a voter-count threshold at which the two voting rules themselves first select different tie-independent unique winners.

The later Artificial Intelligence article expands the manipulation analysis of Borda, Nanson, and Baldwin, again focusing on strategic computation rather than exact small-profile agreement between the two elimination rules.

The contribution here is the complete first tie-independent disagreement layer at four candidates: equality through four voters, exact labeled and anonymous counts at five voters, and the full candidate-relabeling quotient.

Targeted searches using both rule names, four-candidate and five-voter parameters, tie-independent/unique-winner language, the exact counts \(24480\) and \(384\), and isomorphism-class terminology did not locate an equivalent theorem or table.

## Limitations
The classification is specific to complete strict ballots on four candidates.

It deliberately avoids conclusions that depend on an arbitrary fixed tie-breaking order. Profiles with non-unique Baldwin winner sets or unresolved equal-score Nanson states are outside the accepted comparison.

The exact finite search cannot rule out an unindexed teaching computation, software test corpus, thesis appendix, or unpublished enumeration containing the same census.

## References
1. N. Narodytska, T. Walsh, and L. Xia, “Manipulation of Nanson's and Baldwin's Rules,” arXiv:1106.5312, first submitted 27 June 2011; later *Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelligence* (2011), 713–718. DOI: 10.1609/aaai.v25i1.7872.
2. J. Davies, G. Katsirelos, N. Narodytska, T. Walsh, and L. Xia, “Complexity of and algorithms for the manipulation of Borda, Nanson's and Baldwin's voting rules,” *Artificial Intelligence* 217 (2014), 20–42. DOI: 10.1016/j.artint.2014.07.005.
