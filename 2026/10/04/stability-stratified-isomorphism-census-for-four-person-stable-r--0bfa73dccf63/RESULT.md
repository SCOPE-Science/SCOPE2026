# Stability-stratified isomorphism census for four-person stable roommates
## Finding
Consider strict stable-roommates instances on four agents, where each agent linearly ranks the other three agents and profiles are identified under simultaneous relabeling of the agents. There are 60 relabeling classes in total, and their exact stability refinement is
\[
2\text{ classes with no stable matching},\qquad
51\text{ classes with exactly one},\qquad
7\text{ classes with exactly two}.
\]
No profile admits all three perfect matchings stably.

The orbit-size refinement under the natural \(S_4\)-action is exact:
\[
\begin{array}{c|ccc}
\text{stable matchings} & \text{orbit size }6 & \text{orbit size }12 & \text{orbit size }24\\
\hline
0 & 0 & 0 & 2\\
1 & 3 & 6 & 42\\
2 & 1 & 0 & 6
\end{array}
\]
Thus the corresponding labeled-profile counts are \(48\), \(1098\), and \(150\), summing to \(6^4=1296\).

The two unsolvable isomorphism classes have representatives
\[
\begin{array}{c|ccc}
1&2&3&4\\
2&3&1&4\\
3&1&2&4\\
4&1&2&3
\end{array}
\qquad\text{and}\qquad
\begin{array}{c|ccc}
1&2&3&4\\
2&3&1&4\\
3&1&2&4\\
4&1&3&2.
\end{array}
\]
They are the two possible orientation types of the classical four-person cyclic obstruction after quotienting by relabeling.

## Assumptions and scope
A stable matching is a partition into two pairs with no blocking pair: two agents not paired together block if each strictly prefers the other to the assigned partner. Preferences are complete and strict. Isomorphism means one common permutation of the four agent labels applied both to the owners of preference lists and to every name appearing inside those lists.

The statement concerns the complete four-agent universe only. The known total of 60 unlabeled profiles is not claimed as new; the claim is the refinement by number of stable matchings and by orbit size, together with the resulting complete two-class description of the unsolvable stratum.

## Proof
There are exactly \(6^4=1296\) labeled profiles, because each of four agents has \(3!=6\) strict orders of the other agents. There are exactly three perfect matchings. For every profile, test each of the three matchings against all unmatched pairs; this gives its stable-matching count in \(\{0,1,2,3\}\).

For the first exhaustive route, apply all 24 label permutations and replace each profile by the lexicographically least relabeling. This partitions the 1296 profiles into 60 canonical representatives. Counting representatives by the stable-matching count gives \(2,51,7,0\) for counts \(0,1,2,3\), respectively. Computing stabilizers of these representatives gives the orbit-size table in the finding.

A second exhaustive route uses Burnside's lemma without canonicalizing any profile. Stratifying fixed profiles by the number of stable matchings, the fixed counts per group element are
\[
\begin{array}{c|rrrr}
\text{cycle type in }S_4&0&1&2&3\\
\hline
1^4&48&1098&150&0\\
2\,1^2&0&0&0&0\\
2^2&0&34&2&0\\
3\,1&0&0&0&0\\
4&0&4&2&0.
\end{array}
\]
There are respectively \(1,6,3,8,6\) group elements of these cycle types. Averaging fixed counts over the group gives
\[
\frac{48}{24}=2,
\]
\[
\frac{1098+3\cdot34+6\cdot4}{24}=51,
\]
and
\[
\frac{150+3\cdot2+6\cdot2}{24}=7.
\]
The zero count for three stable matchings is obtained independently in both enumerations.

Finally, the two zero-stable canonical representatives are exactly the two displayed cyclic profiles. The classical four-person obstruction fixes the first three lists as a directed three-cycle with agent 4 last, while agent 4 may rank the first three agents arbitrarily. The six choices for agent 4 split into two orbits under rotation of that directed three-cycle, producing precisely the two displayed orientation classes. Their full relabeling orbits each have size 24, accounting for all 48 labeled unsolvable profiles.

## Verification
The embedded `verify_roommates4_orbits.py` performs two independent exact calculations. One constructs canonical representatives under all 24 relabelings; the other applies stability-stratified Burnside counting. Stability itself is checked in two equivalent implementations, one using rank maps and one using preference prefixes. The script also verifies the orbit-size distribution, the two unsolvable canonical representatives, and the labeled solvability probability \(1248/1296=26/27\).

Replay with:

`python3 verify_roommates4_orbits.py`

The required leading output is `VERIFY_OK`.

## Relationship to prior work
Irving's 1985 paper presents the strict stable-roommates problem and records Gale and Shapley's size-four unsolvable obstruction in the form where agents 1, 2, and 3 make a directed preference cycle and agent 4's order is arbitrary. Mertens's 2015 analysis gives the exact random-instance solvability probability \(p_4=26/27\), hence exactly 48 unsolvable labeled profiles among the 1296 four-agent profiles, and develops exact small-instance probability formulas.

A later OEIS entry, A356584, gives 60 as the number of four-agent profiles up to relabeling and derives the total orbit count by Burnside's lemma. That total is therefore treated as prior coverage, not as a new result here. The checked sources and targeted searches did not locate the stability-stratified decomposition \(2+51+7\), its orbit-size refinement, or an explicit statement that the 48 unsolvable labeled profiles collapse to exactly the two orientation classes above.

## Limitations
This is a finite complete classification at the smallest nontrivial even size. It does not provide a formula for the stability-stratified orbit counts at six or more agents. Search failure is not a proof that the refinement has never appeared in an unindexed thesis, course note, software table, or supplementary data set.

## References
1. S. Mertens, “Small random instances of the stable roommates problem,” arXiv:1502.06635, first submitted 2015-02-23; *Journal of Statistical Mechanics: Theory and Experiment* (2015), P06034.
2. R. W. Irving, “An Efficient Algorithm for the ‘Stable Roommates’ Problem,” *Journal of Algorithms* 6 (1985), 577–595. DOI: 10.1016/0196-6774(85)90033-1.
3. OEIS Foundation Inc., A356584, “Number of instances of the stable roommates problem of cardinality n,” entry giving relabeling-orbit counts including 60 at cardinality four.
