# Sharp five-player tie-refinement boundary for Johnston and Banzhaf power rankings
## Finding
Let \(v\) be a proper simple voting game. For a player \(i\), let \(c_i\) be the number of winning coalitions in which \(i\) is critical.

The normalized Penrose–Banzhaf–Coleman vector is obtained by normalizing the critical-coalition counts:
\[
B_i(v)=\frac{c_i}{\sum_j c_j}.
\]

For a winning coalition \(S\), let
\[
\chi(S)=|\{i\in S:v(S)=1,\ v(S\setminus\{i\})=0\}|
\]
be its number of critical members. The raw Johnston score gives each critical member of \(S\) the share \(1/\chi(S)\); normalizing the raw scores gives the vector \(J(v)\). Normalization does not affect its weak ranking.

Every proper simple game with at most \(4\) players has the same weak player ranking under \(B\) and \(J\).

For \(5\) players there are exactly
\[
2645
\]
labeled proper simple games. Exactly
\[
480
\]
have different weak rankings, so the exact incidence is
\[
\frac{480}{2645}=\frac{96}{529}.
\]

The \(480\) divergent games form exactly \(9\) isomorphism classes under player relabeling. Seven classes have orbit size \(60\), and two have orbit size \(30\).

Moreover, every first-layer disagreement is a **tie refinement**:
- whenever \(B_i>B_j\), one also has \(J_i>J_j\);
- whenever the two rankings differ, the changed pair satisfies \(B_i=B_j\) but \(J_i\ne J_j\).

Thus there is no strict pairwise reversal at the first divergence layer. Exactly \(420\) divergent games refine \(2\) unordered player comparisons, while \(60\) refine \(4\).

Using players \(A,B,C,D,E\), canonical minimal-winning families for the nine classes are:
\[
\begin{aligned}
&\{AB,ACD,ACE,BDE\},\\
&\{ABC,ABD,ACD,ABE,ACE,BDE\},\\
&\{ABC,ABD,ACD,ABE,ACE,BDE,CDE\},\\
&\{ABC,ABD,ACD,ABE,BCE,CDE\},\\
&\{ABC,ABD,ACD,ABE,CDE\},\\
&\{ABC,ABD,ACD,BCE\},\\
&\{ABC,ABD,ACD,BCE,BDE\},\\
&\{ABC,ABD,ACE,BDE\},\\
&\{ABC,ABD,CDE\}.
\end{aligned}
\]

Their orbit sizes, normalized Banzhaf vectors, and normalized Johnston vectors are:

| minimal winning coalitions | orbit | \(B\) | \(J\) |
|---|---:|---|---|
| \(\{AB,ACD,ACE,BDE\}\) | \(60\) | \((9/25,7/25,3/25,3/25,3/25)\) | \((31/72,11/36,7/72,1/12,1/12)\) |
| \(\{ABC,ABD,ACD,ABE,ACE,BDE\}\) | \(60\) | \((4/13,3/13,2/13,2/13,2/13)\) | \((25/66,8/33,3/22,4/33,4/33)\) |
| \(\{ABC,ABD,ACD,ABE,ACE,BDE,CDE\}\) | \(30\) | \((7/27,5/27,5/27,5/27,5/27)\) | \((11/36,7/36,7/36,11/72,11/72)\) |
| \(\{ABC,ABD,ACD,ABE,BCE,CDE\}\) | \(60\) | \((3/13,3/13,3/13,2/13,2/13)\) | \((17/66,17/66,7/33,3/22,3/22)\) |
| \(\{ABC,ABD,ACD,ABE,CDE\}\) | \(60\) | \((7/25,1/5,1/5,1/5,3/25)\) | \((1/3,1/5,11/60,11/60,1/10)\) |
| \(\{ABC,ABD,ACD,BCE\}\) | \(60\) | \((1/4,1/4,1/4,1/6,1/12)\) | \((8/27,13/54,13/54,4/27,2/27)\) |
| \(\{ABC,ABD,ACD,BCE,BDE\}\) | \(60\) | \((1/5,7/25,1/5,1/5,3/25)\) | \((7/30,17/60,11/60,11/60,7/60)\) |
| \(\{ABC,ABD,ACE,BDE\}\) | \(60\) | \((1/4,1/4,1/6,1/6,1/6)\) | \((7/27,7/27,1/6,1/6,4/27)\) |
| \(\{ABC,ABD,CDE\}\) | \(30\) | \((5/23,5/23,5/23,5/23,3/23)\) | \((11/48,11/48,5/24,5/24,1/8)\) |

Consequently, five players are the sharp first size at which Johnston and Banzhaf can rank players differently within the proper-simple-game domain.

## Assumptions and scope
A simple game is a monotone \(0\)-\(1\) game with the grand coalition winning and the empty coalition losing. It is proper when no coalition and its complement are both winning.

Every such game is represented uniquely by its antichain of minimal winning coalitions.

The comparison is ordinal: only the weak player ranking is compared. Numerical equality of the two power vectors is not required.

The finding concerns proper simple games on at most five labeled players. It does not classify six-player games or non-proper five-player games.

## Proof
The verifier enumerates every nonempty antichain of nonempty coalitions for \(n\le5\), interprets it as the minimal-winning family of a simple game, and filters for properness.

The numbers of proper labeled games for \(n=1,2,3,4,5\) are
\[
1,\ 3,\ 11,\ 80,\ 2645,
\]
and their numbers of isomorphism classes under all player permutations are
\[
1,\ 2,\ 5,\ 14,\ 86.
\]

Banzhaf power is computed in two exact ways. One counts losing coalitions that become winning when player \(i\) joins. The other counts winning coalitions that become losing when player \(i\) leaves. The swing counts agree game by game.

Johnston power is also computed in two exact ways. One loops over winning coalitions and divides one unit equally among all critical players in that coalition. The other loops player by player and independently recomputes the number of critical players in every coalition containing that player. The raw and normalized scores agree game by game.

All arithmetic is exact rational arithmetic.

No proper game through \(4\) players gives different weak rankings. At \(5\) players exactly \(480\) games diverge.

For every divergent game, every strict Banzhaf comparison has the same sign under Johnston. Hence the only changes are Banzhaf ties split by Johnston. The verifier records \(420\) games with exactly \(2\) changed unordered pairs and \(60\) with exactly \(4\).

Finally, canonicalization under all
\[
5!=120
\]
player permutations gives exactly the nine displayed minimal-winning families, with orbit sizes summing to \(480\).

## Verification
The embedded `verify_johnston_banzhaf_proper_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It checks:
- all simple games through five players via minimal-winning antichains;
- the standard small simple-game counts \(1,4,18,166,7579\);
- proper-game counts \(1,3,11,80,2645\);
- proper-game isomorphism counts \(1,2,5,14,86\);
- two independent Banzhaf swing computations;
- two independent Johnston computations;
- exact normalization of both vectors;
- no weak-ranking divergence through four players;
- exactly \(480\) divergent proper five-player games;
- exact incidence \(96/529\);
- exactly nine divergent player-relabeling classes;
- orbit sizes seven times \(60\) and twice \(30\);
- absence of every strict pairwise rank reversal;
- the \(420/60\) split by number of refined unordered player pairs;
- every displayed canonical family and power vector.

Run:

`python3 verify_johnston_banzhaf_proper_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Johnston's index and the Penrose–Banzhaf–Coleman index are classical measures of voting power based on criticality, but they distribute credit for critical coalitions differently.

Freixas, Marciniak, and Pons study ordinal equivalence of Johnston, Banzhaf, and Shapley–Shubik power. Their public presentation gives the raw Banzhaf and Johnston formulas used here and proves that the three indices rank players identically throughout the semicomplete class, which contains complete games. Their later journal article states the same semicomplete ordinal-equivalence theorem.

That theorem implies that every divergent game in the present finite census lies outside the semicomplete class. It does not determine the smallest proper game outside that protection on which Johnston and Banzhaf actually disagree, nor the size and symmetry structure of the first divergent layer.

The contribution here is exactly that first-layer classification: complete agreement through four proper players, \(480\) divergent labeled games at five players, nine isomorphism classes, and the stronger fact that every first disagreement is only a Johnston refinement of a Banzhaf tie.

Targeted searches by index names, ordinal-equivalence terminology, five-player/proper-simple-game parameters, exact counts, the fraction \(96/529\), and isomorphism language did not locate an equivalent published census.

## Limitations
The theorem is finite and ordinal. It makes no statement about numerical distance between the two indices or the behavior for six or more players.

The full text of the 2012 journal article was restricted in the inspected source. A public 2011 presentation by the same lead author and on the same ordinal-equivalence program was inspected in full, including the formulas and semicomplete equivalence theorem.

Johnston's original work predates the day-resolved source used for metadata, but the inspected original article record gives only month and year rather than a public day. No day was invented.

An unindexed historical enumeration, thesis appendix, or software test corpus could contain the same five-player census.

## References
1. J. Freixas, “Ordinal equivalence of power indices,” presentation at the Voting Power in Practice Symposium, London School of Economics, 20–22 March 2011.
2. J. Freixas, D. Marciniak, and M. Pons, “On the ordinal equivalence of the Johnston, Banzhaf and Shapley power indices,” *European Journal of Operational Research* 216(2) (2012), 367–375. DOI: 10.1016/j.ejor.2011.07.028.
3. R. J. Johnston, “On the Measurement of Power: Some Reactions to Laver,” *Environment and Planning A* 10(8) (1978), 907–914. DOI: 10.1068/a100907.
