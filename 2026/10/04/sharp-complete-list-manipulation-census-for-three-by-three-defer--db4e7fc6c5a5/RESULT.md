# Sharp complete-list manipulation census for three-by-three deferred acceptance
## Finding
Consider men-proposing deferred acceptance with complete strict preference lists. Women may misreport only by permuting the full list of men; declaring a man unacceptable is not allowed.

With at most two men and two women, no woman can obtain a strictly better partner by a unilateral permutation misreport.

For \(3\times3\) markets, there are exactly
\[
6^6=46{,}656
\]
labeled truthful profiles. Exactly
\[
864
\]
of them admit at least one profitable unilateral permutation misreport by a woman. Hence the exact incidence under the uniform distribution on labeled profiles is
\[
\frac{864}{46{,}656}=\frac1{54}.
\]

The \(864\) manipulable profiles split as follows:
\[
648
\]
have exactly one manipulating woman and
\[
216
\]
have exactly two. No profile has three manipulating women.

There is also a sharp report-level statement. Across all manipulable profiles there are exactly \(1080\) manipulating woman-profile pairs, and every such woman has exactly one profitable complete-list report. Every profitable report produces a matching that is stable with respect to the original true preferences.

Finally, quotienting profiles by independent relabeling of the men and the women gives exactly \(24\) manipulable classes. Every one of these classes has the full orbit size
\[
|S_3\times S_3|=36.
\]

## Assumptions and scope
Each side contains the same number of agents. Every preference list is a strict total order of the entire opposite side. Men report truthfully and propose. A woman manipulates unilaterally when all other reports remain truthful and she replaces her true list by another permutation of the same men.

A manipulation is profitable only when the resulting partner is strictly preferred according to the woman's true preference order. The result does not allow truncation, blacklisting, ties, unmatched agents, coalitional deviations, or many-to-one capacities.

The symmetry quotient preserves the proposer and receiver roles: men may be relabeled arbitrarily and women may be relabeled arbitrarily, but the two sides are not exchanged.

## Proof
For market size \(n\), a labeled profile consists of \(2n\) strict rankings. The verifier exhausts all profiles for \(n=1,2,3\).

For \(n=1\) and \(n=2\), every woman's alternative complete-list report is tested directly and no profitable deviation occurs.

For \(n=3\), the verifier runs over all
\[
(3!)^{6}=46{,}656
\]
truthful profiles. At each profile it computes the truthful men-proposing deferred-acceptance outcome. Then, for each of the three women, it replaces only that woman's list by each of the other five permutations and recomputes the outcome. Profitability is evaluated against the woman's original true ranking. This is an exhaustive search over every unilateral complete-list deviation.

Two separately coded implementations of deferred acceptance are used throughout: one processes free proposers from a stack and the other processes simultaneous proposal rounds. Their outputs are asserted equal for every truthful profile and every tested deviation.

This gives exactly \(864\) manipulable truthful profiles. Counting the women with at least one profitable deviation gives \(648\) profiles with one manipulator and \(216\) with two. Counting profitable reports themselves gives exactly one profitable permutation for every manipulating woman.

For every manipulable truthful profile the verifier independently enumerates all \(3!=6\) perfect matchings and checks stability under the true preferences. Every matching induced by a profitable report appears in this true-stable set. The manipulable profiles refine by their number of true stable matchings as
\[
540\text{ profiles with two stable matchings and one manipulator},
\]
\[
216\text{ profiles with two stable matchings and two manipulators},
\]
and
\[
108\text{ profiles with three stable matchings and one manipulator}.
\]

For the quotient, every manipulable profile is transformed by all \(36\) elements of \(S_3\times S_3\) and reduced to a canonical representative. This produces \(24\) representatives, each occurring exactly \(36\) times. An independent Burnside computation over the same group again gives \(24\) orbits.

## Verification
Run

`python3 verify_da3_permutation_manipulation.py`

The verifier uses only exact finite operations and the Python standard library. Its first output line is `VERIFY_OK`.

It checks all \(46{,}656\) labeled \(3\times3\) profiles and all unilateral complete-list deviations. It also checks the \(n\le2\) boundary, two independent deferred-acceptance implementations, true stability of every profitable manipulated outcome, the manipulator-count distribution, canonical symmetry orbits, and an independent Burnside quotient.

The numerical claims are finite exhaustive theorems. No asymptotic or infinite conclusion is inferred from the computation.

## Relationship to prior work
Teo, Sethuraman, and Tan study exactly the complete-list permutation-manipulation model for a single woman. They derive an optimal cheating strategy and emphasize that forbidding rejection or truncation sharply limits women's strategic power. Their \(1999\) extended abstract reports simulation experiments at larger sizes rather than an exhaustive small-market census: for example, it samples \(1000\) random markets at size \(8\). It does not give the exact \(3\times3\) incidence, the manipulator multiplicities, or the role-preserving symmetry quotient.

Shen, Deng, and Tang later study permutation manipulations by arbitrary coalitions of women and characterize feasible stable outcomes using rotations and suitor graphs. Their general results do not state the finite \(3\times3\) counts proved here.

The fact that a profitable complete-list manipulation can exist is therefore prior work. The contribution here is the sharp boundary at size three, the exact \(864/46{,}656\) census, the \(648+216\) manipulator split, the uniqueness of the profitable report for every manipulating woman, the true-stability exhaustion of all profitable reports at this size, and the exact \(24\)-class quotient.

## Limitations
The classification is complete only through \(3\times3\). The fact that every profitable report induces a true-stable matching is asserted only for this finite boundary case; it is not extrapolated to larger markets.

The result concerns unilateral complete-list permutations. It does not apply to truncation, blacklists, coalitional manipulation, incomplete lists, or many-to-one matching.

Targeted searches and inspection of the closest primary literature found no equivalent small-market census, but an unindexed thesis, course note, code table, or supplementary computation could contain the same finite counts.

## References
1. C.-P. Teo, J. Sethuraman, and W.-P. Tan, “Gale-Shapley Stable Marriage Problem Revisited: Strategic Issues and Applications,” in *Integer Programming and Combinatorial Optimization*, LNCS 1610, 429–438, 1999. DOI: 10.1007/3-540-48777-8_32.
2. C.-P. Teo, J. Sethuraman, and W.-P. Tan, “Gale-Shapley Stable Marriage Problem Revisited: Strategic Issues and Applications,” *Management Science* 47(9), 1252–1267, 2001. DOI: 10.1287/mnsc.47.9.1252.9784.
3. W. Shen, Y. Deng, and P. Tang, “Coalitional Permutation Manipulations in the Gale-Shapley Algorithm,” arXiv:1502.07823, first submitted 27 February 2015.
