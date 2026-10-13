# Complete five-player reversal layer for Deegan–Packel versus Shapley–Shubik
## Finding
Let \(v\) be a proper simple voting game on a finite player set \(N\), and let \(\mathcal M(v)\) be its set of minimal winning coalitions.

The **Deegan–Packel index** is
\[
DP_i(v)=\frac{1}{|\mathcal M(v)|}\sum_{\substack{S\in\mathcal M(v)\\ i\in S}}\frac1{|S|}.
\]
It models power through equally likely minimal winning coalitions with equal division inside each such coalition.

The **Shapley–Shubik index** is
\[
SS_i(v)=\sum_{S\subseteq N\setminus\{i\}}
\frac{|S|!\,(|N|-|S|-1)!}{|N|!}
\bigl(v(S\cup\{i\})-v(S)\bigr).
\]
Equivalently, it is the probability that player \(i\) is pivotal in a uniformly random ordering of the players.

Compare the two vectors only by the weak ordering they induce on players.

Every proper simple game with at most \(4\) players gives the same weak player ranking under \(DP\) and \(SS\).

For \(5\) players there are exactly
\[
2645
\]
labeled proper simple games, and exactly
\[
460
\]
of them have different weak rankings. Thus the exact incidence is
\[
\frac{460}{2645}=\frac{92}{529}.
\]

The \(460\) divergent games form exactly \(9\) isomorphism classes under player relabeling. Every divergence is a **strict pairwise reversal**: there is no case in the first layer where one index merely refines a tie of the other.

More precisely:
\[
\begin{array}{c|c|c}
\text{number of reversed unordered player pairs} & \text{labeled games} & \text{isomorphism classes}\\ \hline
1 & 300 & 4\\
2 & 120 & 3\\
3 & 40 & 2.
\end{array}
\]

All \(9\) divergent classes are weighted voting games, and all \(460\) divergent labeled games are dummy-free. Among the \(2330\) dummy-free labeled proper five-player games, the divergence incidence is therefore
\[
\frac{460}{2330}=\frac{46}{233}.
\]

Using players \(A,B,C,D,E\), the nine canonical minimal-winning families, orbit sizes, and one integer weighted representation for each are:

| minimal winning coalitions | orbit | weighted representation |
|---|---:|---|
| `AB, AC, BCD, BCE` | \(30\) | `[7;4,3,3,1,1]` |
| `AB, ACD, BCD, ACE` | \(120\) | `[9;5,4,3,2,1]` |
| `AB, ACD, BCD, ACE, BCE` | \(30\) | `[6;3,3,2,1,1]` |
| `AB, ACD, BCD, ACE, BCE, ADE` | \(60\) | `[9;5,4,3,2,2]` |
| `AB, ACD, BCD, ACE, ADE` | \(60\) | `[7;4,3,2,2,1]` |
| `AB, ACD, ACE` | \(60\) | `[8;5,3,2,1,1]` |
| `AB, ACD, ACE, ADE` | \(20\) | `[6;4,2,1,1,1]` |
| `AB, ACD, ACE, ADE, BCDE` | \(20\) | `[5;3,2,1,1,1]` |
| `AB, ACD, ACE, BCDE` | \(60\) | `[7;4,3,2,1,1]` |

A clean witness is
\[
\mathcal M(v)=\{AB,ACD,ACE\},
\]
which is the weighted game `[8;5,3,2,1,1]`. Its two power vectors are
\[
DP(v)=\left(\frac7{18},\frac16,\frac29,\frac19,\frac19\right),
\]
\[
SS(v)=\left(\frac{37}{60},\frac15,\frac7{60},\frac1{30},\frac1{30}\right).
\]
Hence \(DP\) ranks
\[
A>C>B>D=E,
\]
while \(SS\) ranks
\[
A>B>C>D=E.
\]
Thus players \(B\) and \(C\) strictly reverse.

## Assumptions and scope
A simple game is a monotone \(0\)-\(1\) cooperative game with the empty coalition losing and the grand coalition winning. Properness means that no coalition and its complement are both winning.

Every simple game is represented uniquely by the antichain of its minimal winning coalitions. A dummy player is one that belongs to no minimal winning coalition.

The result compares weak player rankings, not numerical distances between the two indices. It classifies every proper simple game through five players; it makes no claim for six or more players.

## Proof
The verifier enumerates every nonempty antichain of nonempty coalitions on \(n\le5\) players and filters by properness. The exact labeled counts are
\[
1,\ 3,\ 11,\ 80,\ 2645,
\]
and the corresponding isomorphism-class counts under player relabeling are
\[
1,\ 2,\ 5,\ 14,\ 86.
\]

For every game, Deegan–Packel is computed twice. The first implementation applies the defining minimal-winning-coalition sum. The second explicitly forms the equal-split payoff vector of each minimal winning coalition and averages those vectors. The two exact rational vectors agree game by game.

Shapley–Shubik is also computed twice. The first implementation uses the exact swing formula with factorial weights. The second enumerates all \(|N|!\) player orders and counts pivotal players. These exact vectors agree game by game.

For every proper game through four players, the two weak rankings coincide. At five players exactly \(460\) labeled games diverge.

For each divergent game, every unordered player pair is compared under both vectors. The complete relation histogram is:
\[
300
\]
games with one strict reversal,
\[
120
\]
with two strict reversals, and
\[
40
\]
with three strict reversals. No tie-to-strict or strict-to-tie difference occurs. Hence every change at the first layer is a genuine reversal.

Canonicalization under all \(5!\) player permutations yields exactly nine divergent isomorphism classes. Their orbit sizes sum to
\[
30+120+30+60+60+60+20+20+60=460.
\]

For each canonical class the verifier independently searches nonnegative integer weights at most \(5\) and a positive quota. It finds the nine weighted representations displayed above and checks their truth tables exactly.

Finally, all coordinates of \(DP\) are positive in every divergent class, so no divergent game has a dummy player. The complete proper five-player domain contains \(2330\) dummy-free labeled games.

## Verification
The embedded `verify_dp_shapley_proper_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- every proper simple game on one through five players;
- exact labeled counts \(1,3,11,80,2645\);
- exact isomorphism-class counts \(1,2,5,14,86\);
- two independent exact computations of Deegan–Packel;
- two independent exact computations of Shapley–Shubik;
- no ordinal divergence through four players;
- exactly \(460\) divergent labeled five-player games;
- exactly \(9\) divergent isomorphism classes;
- the strict-reversal histogram \(300,120,40\);
- absence of tie-only differences;
- all nine displayed weighted representations;
- \(2330\) dummy-free proper five-player games and all \(460\) divergences inside that subdomain;
- the displayed witness and both exact power vectors.

Run:

`python3 verify_dp_shapley_proper_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Aziz treats Shapley–Shubik and Deegan–Packel as classical measures of influence on simple games and gives the exact standard formulas in a common framework. That work is computational-complexity focused rather than a finite ordinal census.

Freixas and Marciniak explicitly contrast the two indices structurally: Shapley–Shubik satisfies their egalitarian property, while Deegan–Packel does not. Their paper also records that Deegan–Packel need not preserve the desirability relation, whereas Shapley–Shubik is a regular semivalue and does preserve it.

A 2011 presentation on ordinal equivalence likewise emphasizes rankings as the relevant object and states that Deegan–Packel can contradict the desirability order, while regular semivalues such as Shapley–Shubik respect it. That presentation does not provide the complete proper five-player census, the nine symmetry classes, or the exact reversal histogram established here.

Targeted searches using both index names, ordinal-equivalence and desirability terminology, the five-player parameter, the exact count \(460\), and the nine canonical weighted representations did not locate an equivalent published classification.

## Limitations
The theorem is finite and stops at five players.

The novelty claim is the complete sharp proper-game layer and its exact quotient structure, not the general fact that Deegan–Packel can violate desirability or differ from Shapley–Shubik.

A 2011 presentation contains a five-player weighted example in a slide asserting a Deegan–Packel desirability reversal. The present result does not rely on that numerical slide example; all accepted vectors are recomputed from the standard definitions. The presentation does not contain the complete census claimed here.

An unindexed historical table, software test corpus, thesis appendix, or unpublished enumeration could contain the same finite classification.

## References
1. H. Aziz, “Complexity of comparison of influence of players in simple games,” arXiv:0809.0519, first submitted 2 September 2008.
2. J. Freixas and D. Marciniak, “Egalitarian property for power indices,” *Social Choice and Welfare* 40 (2013), 207–227; published online 21 September 2011. DOI: 10.1007/s00355-011-0593-7.
3. J. Freixas, “Ordinal equivalence of power indices,” presentation for the Voting Power in Practice Symposium, London School of Economics, March 2011.
4. J. Deegan Jr. and E. W. Packel, “A new index of power for simple \(n\)-person games,” *International Journal of Game Theory* 7 (1978), 113–123.
5. L. S. Shapley and M. Shubik, “A method for evaluating the distribution of power in a committee system,” *American Political Science Review* 48 (1954), 787–792.
