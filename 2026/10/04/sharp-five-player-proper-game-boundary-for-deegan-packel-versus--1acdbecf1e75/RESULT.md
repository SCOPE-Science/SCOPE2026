# Sharp five-player proper-game boundary for Deegan-Packel versus Shapley-Shubik ranking
## Finding
Let \(v\) be a monotone simple voting game. Write \(DP(v)\) for the Deegan-Packel power vector and \(SS(v)\) for the Shapley-Shubik power vector. We compare only the weak ordering of players, so multiplying an index by a common positive normalizing factor is immaterial.

For every proper simple game with at most \(4\) players, \(DP(v)\) and \(SS(v)\) induce exactly the same weak player ordering.

This cutoff is sharp. There are exactly \(2645\) labeled proper simple games on \(5\) players, and exactly
\[
460
\]
of them induce different weak orderings. In every one of those \(460\) games there is a pair of players whose order is strictly reversed by the two indices; none of the disagreements is merely a tie broken by one index.

Up to player relabeling, the \(460\) divergent games form exactly \(9\) classes. Using \(123\) for \(\{1,2,3\}\), their minimal-winning families, labeled orbit sizes, and weighted representations are:

\[
\begin{array}{c|c|c}
\text{minimal winning coalitions} & \text{orbit} & \text{weighted representation}\\ \hline
12,13,234,235 & 30 & [7;4,3,3,1,1]\\
12,134,234,135 & 120 & [9;5,4,3,2,1]\\
12,134,234,135,235 & 30 & [6;3,3,2,1,1]\\
12,134,234,135,235,145 & 60 & [9;5,4,3,2,2]\\
12,134,234,135,145 & 60 & [7;4,3,2,2,1]\\
12,134,135 & 60 & [8;5,3,2,1,1]\\
12,134,135,145 & 20 & [6;4,2,1,1,1]\\
12,134,135,145,2345 & 20 & [5;3,2,1,1,1]\\
12,134,135,2345 & 60 & [7;4,3,2,1,1]
\end{array}
\]

Hence five players are also the first possible size for a Deegan-Packel/Shapley-Shubik ranking reversal inside the proper weighted-majority subclass.

A concrete witness is
\[
[9;5,4,3,2,1],
\]
whose minimal winning coalitions are
\[
\{12,134,234,135\}.
\]
For this game, an unnormalized Deegan-Packel vector is
\[
\left(\frac76,\frac56,1,\frac23,\frac13\right),
\]
while the Shapley-Shubik vector is
\[
\left(\frac{11}{30},\frac{17}{60},\frac15,\frac{7}{60},\frac1{30}\right).
\]
Deegan-Packel ranks player \(3\) above player \(2\), whereas Shapley-Shubik ranks player \(2\) above player \(3\).

Properness changes the first possible market size. If arbitrary simple games are admitted, divergence occurs already for \(4\) players: exactly \(16\) labeled four-player simple games disagree, and every one of those \(16\) games is improper.

## Assumptions and scope
A simple game is monotone, has the empty coalition losing, and has the grand coalition winning. A game is proper when no winning coalition has a winning complement.

The Deegan-Packel index allocates equal total weight to every minimal winning coalition and then divides a coalition's weight equally among its members. Thus, up to a common normalization, player \(i\) receives
\[
\sum_{S\in\mathcal M_i(v)}\frac1{|S|}.
\]

The Shapley-Shubik index is the probability that a player is pivotal in a uniformly random ordering of all players.

Weak-order equality means that every pair of players has the same relation—above, below, or tied—under both indices.

The universal classification is complete through \(5\) players. No frequency statement for larger games is claimed.

## Proof
Every monotone simple game is uniquely determined by the antichain \(\mathcal M(v)\) of its minimal winning coalitions.

The verifier constructs all simple games through \(5\) players in two independent ways. The first recursively builds all nonempty antichains of nonempty coalitions. The second recursively builds all monotone Boolean truth tables by the Dedekind decomposition: a monotone function in one additional variable is a pair \((f_0,f_1)\) of monotone functions with \(f_0\le f_1\) pointwise. Converting each nonconstant truth table to its minimal winning coalitions yields exactly the same games.

The labeled simple-game counts are
\[
1,\ 4,\ 18,\ 166,\ 7579
\]
for \(1,2,3,4,5\) players. Direct complement testing leaves
\[
1,\ 3,\ 11,\ 80,\ 2645
\]
proper games.

For every proper game, the verifier computes the Deegan-Packel vector exactly from its minimal winning coalitions. It computes Shapley-Shubik twice: once from the standard pivotal-coalition factorial formula and once by enumerating every player permutation and counting pivotal players. The two Shapley-Shubik calculations agree in every case.

The weak orders agree for every proper game through \(4\) players. For \(5\) players, exactly \(460\) proper games disagree. Each of those \(460\) contains a strict pairwise reversal.

Canonicalizing each divergent game under all \(5!\) player relabelings gives exactly \(9\) isomorphism classes, with orbit-size multiset
\[
\{120,60,60,60,60,30,30,20,20\}.
\]
The nine weighted representations displayed above are checked by reconstructing all winning coalitions from the quota and weights and recomputing the minimal-winning family exactly.

Finally, the same comparison over all \(166\) labeled four-player simple games finds exactly \(16\) unrestricted disagreements, and direct properness testing shows that all \(16\) are improper.

## Verification
The embedded `verify_dp_ss_proper_boundary.py` uses only the Python standard library and exact rational arithmetic.

It checks:
- two independent enumerations of every simple game through \(5\) players;
- the exact simple-game counts \(1,4,18,166,7579\);
- the exact proper-game counts \(1,3,11,80,2645\);
- two independent Shapley-Shubik computations on every proper game;
- zero proper ranking disagreements through \(4\) players;
- exactly \(460\) divergent proper five-player games, each with a strict reversal;
- exactly \(9\) five-player isomorphism classes and their orbit sizes;
- all nine explicit weighted representations;
- exactly \(16\) unrestricted four-player disagreements, all improper;
- the exact index vectors of the displayed weighted witness.

Run:

`python3 verify_dp_ss_proper_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Deegan and Packel introduced their minimal-winning-coalition index as an alternative model of voting power to the Shapley-Shubik index. Aziz treats both as classical power indices for simple games, states the standard Shapley-Shubik formula, gives the Deegan-Packel formula, and studies the computational complexity of evaluating and comparing influence in different representations of simple games.

Freixas and Marciniak show that the two indices can behave differently under structural transformations: Shapley-Shubik satisfies their egalitarian property, whereas Deegan-Packel admits counterexamples.

Khmelnitskaya and Chessa make the relationship especially explicit. They prove that the classical Deegan-Packel index of a simple game equals the Shapley value of an auxiliary game obtained by averaging the unanimity games generated by the original minimal winning coalitions. This explains a close formal affinity with Shapley-Shubik, but it does not force the two indices to rank players identically in the original simple game.

The result here identifies the first proper-game size where that affinity can break at the ordinal level and classifies the whole first divergent stratum. Targeted searches for this proper five-player boundary, the count \(460\), the nine-class decomposition, the displayed coalition families, and the weighted representatives did not locate an equivalent published statement.

## Limitations
The finding concerns weak player rankings, not equality of normalized numerical power values.

Properness is the only structural restriction in the lower-bound statement. The nine first divergent classes happen all to be weighted, but the result does not classify all proper weighted games on five players.

The classification is finite and exact through five players; it gives no asymptotic frequency or larger-player characterization.

An unindexed historical enumeration, thesis, teaching note, or software table could contain the same small-game boundary even though the targeted literature and exact-number searches did not reveal one.

## References
1. H. Aziz, “Complexity of comparison of influence of players in simple games,” arXiv:0809.0519, first submitted 2 September 2008.
2. J. Deegan Jr. and E. W. Packel, “A New Index of Power for Simple \(n\)-Person Games,” *International Journal of Game Theory* 7 (1978), 113–123. DOI: 10.1007/BF01753239.
3. J. Freixas and D. Marciniak, “Egalitarian property for power indices,” *Social Choice and Welfare* 40 (2013), 207–227. Published online 21 September 2011. DOI: 10.1007/s00355-011-0593-7.
4. A. Khmelnitskaya and M. Chessa, “Weighted and Restricted Deegan-Packel Power Indices,” 2020 working paper, University of Twente; SSRN DOI: 10.2139/ssrn.3713983.
