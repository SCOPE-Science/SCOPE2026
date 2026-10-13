# Sharp four-player ordinal divergence layer for Deegan–Packel and the Public Good index
## Finding
Let \(v\) be a proper simple voting game with player set \(N\), and let \(\mathcal M(v)\) be its set of minimal winning coalitions.

The **Deegan–Packel index** of player \(i\) is
\[
DP_i(v)=\frac{1}{|\mathcal M(v)|}
\sum_{\substack{S\in\mathcal M(v)\\ i\in S}}\frac1{|S|}.
\]
It treats every minimal winning coalition as equally likely and splits that coalition's unit power equally among its members.

The **Public Good index** of player \(i\) is
\[
PG_i(v)=
\frac{|\{S\in\mathcal M(v):i\in S\}|}
{\sum_{j\in N}|\{S\in\mathcal M(v):j\in S\}|}.
\]
It depends only on how many minimal winning coalitions contain each player, not on their sizes.

Compare the two vectors only by the weak ordering they induce on players.

Every proper simple game with at most \(3\) players gives the same weak player ranking under \(DP\) and \(PG\).

For \(4\) players there are exactly
\[
80
\]
labeled proper simple games, and exactly
\[
30
\]
of them give different weak rankings.

Those \(30\) games form exactly three isomorphism classes under player relabeling, with labeled orbit sizes
\[
12,\qquad 12,\qquad 6.
\]

Using players \(A,B,C,D\), canonical minimal-winning families are
\[
\mathcal W_1=\{AB,ACD\},
\]
\[
\mathcal W_2=\{AB,AC,BCD\},
\]
and
\[
\mathcal W_3=\{AB,ACD,BCD\}.
\]

For \(\mathcal W_1\),
\[
DP=\left(\frac5{12},\frac14,\frac16,\frac16\right),
\qquad
PG=\left(\frac25,\frac15,\frac15,\frac15\right).
\]
Thus \(DP\) ranks
\[
A>B>C=D,
\]
while \(PG\) ranks
\[
A>B=C=D.
\]

For \(\mathcal W_2\),
\[
DP=\left(\frac13,\frac5{18},\frac5{18},\frac19\right),
\qquad
PG=\left(\frac27,\frac27,\frac27,\frac17\right).
\]
Thus \(DP\) ranks
\[
A>B=C>D,
\]
while \(PG\) ranks
\[
A=B=C>D.
\]

For \(\mathcal W_3\),
\[
DP=\left(\frac5{18},\frac5{18},\frac29,\frac29\right),
\qquad
PG=\left(\frac14,\frac14,\frac14,\frac14\right).
\]
Thus \(DP\) ranks
\[
A=B>C=D,
\]
while \(PG\) ties all four players.

All three first-layer divergent classes are weighted voting games. They admit the representations
`[5;3,2,1,1]`,
`[5;3,2,2,1]`,
and
`[4;2,2,1,1]`,
respectively.

Properness is a substantive part of the boundary. If properness is dropped, ordinal divergence already occurs on \(3\) players: exactly \(3\) labeled simple games diverge there, all in one isomorphism class.

Hence \(4\) players are the sharp first size at which these two classical minimal-winning-coalition power indices can rank players differently within the proper-simple-game domain.

## Assumptions and scope
A simple game is a monotone \(0\)-\(1\) game with the grand coalition winning. It is proper when no coalition and its complement are both winning.

Every simple game is represented uniquely by its antichain of minimal winning coalitions.

The comparison is ordinal: two power vectors count as equivalent when they induce the same weak ranking of players, even if their numerical coordinates differ.

The theorem covers every proper simple game on one through four labeled players. It does not classify five-player games or non-proper games beyond the stated three-player contrast.

## Proof
The verifier enumerates every nonempty antichain of nonempty subsets of \(N\), interprets it as the family of minimal winning coalitions, and filters by properness.

The exact numbers of labeled proper simple games are
\[
1,\ 3,\ 11,\ 80
\]
for one through four players. Their numbers of isomorphism classes are
\[
1,\ 2,\ 5,\ 14.
\]

For each game, \(DP\) is computed independently in two equivalent implementations. One applies the defining sum directly. The other constructs the equal-split payoff vector of every minimal winning coalition and averages those coalition vectors.

Likewise, \(PG\) is computed in two ways. One uses the defining normalized participation count. The other explicitly forms the complete player-minimal-coalition incidence multiset and normalizes its frequencies.

Both pairs of implementations agree game by game, and both indices sum exactly to \(1\).

No proper game on one, two, or three players gives different weak rankings.

At four players exactly \(30\) games diverge. Canonicalization under all
\[
4!=24
\]
player permutations gives exactly three canonical antichains:
\[
\{AB,ACD\},\qquad
\{AB,AC,BCD\},\qquad
\{AB,ACD,BCD\}.
\]
Their orbit sizes are \(12,12,6\), whose sum is \(30\).

Direct substitution into the two index formulas yields the three displayed vector pairs.

Finally, the verifier searches exact integer weighted representations and obtains
`[5;3,2,1,1]`,
`[5;3,2,2,1]`,
and
`[4;2,2,1,1]`.

Repeating the enumeration without the properness filter gives exactly three divergent labeled simple games on \(3\) players; they form one isomorphism class and none is proper.

## Verification
The embedded `verify_dp_public_good_proper_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- all proper simple games on one through four players;
- exact labeled counts \(1,3,11,80\);
- exact isomorphism-class counts \(1,2,5,14\);
- two independent computations of the Deegan–Packel index;
- two independent computations of the Public Good index;
- no ordinal divergence through three players in the proper domain;
- exactly \(30\) divergent labeled four-player proper games;
- exactly three divergent isomorphism classes with orbit sizes \(12,12,6\);
- the three displayed canonical minimal-winning families;
- the three displayed index-vector pairs;
- the three displayed weighted representations;
- exactly three non-proper three-player divergences, all in one isomorphism class.

Run:

`python3 verify_dp_public_good_proper_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Deegan and Packel introduced an index based on minimal winning coalitions being equally likely and their power being divided equally among coalition members. Holler introduced the Public Good index, in which a player's power is proportional to the number of minimal winning coalitions containing that player.

Alonso-Meijide, Álvarez-Mozos, and Fiestras-Janeiro treat both indices in a common minimal-winning-coalition framework. Their open working paper explicitly emphasizes the conceptual distinction relevant here: Deegan–Packel is sensitive to minimal-winning-coalition sizes, whereas Public Good is not.

That distinction makes ordinal divergence mathematically natural, but it does not determine the smallest proper game where it occurs or the complete first layer.

The contribution here is the sharp proper-game boundary and complete four-player quotient: no divergence through three players, exactly \(30\) labeled divergences at four players, exactly three symmetry classes, and weighted representatives for all three.

Targeted semantic-repository and web searches using both index names, Public Good/Holler aliases, proper/simple/weighted voting terminology, four-player ranking language, exact counts, and the three weighted representatives did not locate an equivalent classification.

## Limitations
The theorem compares weak rankings rather than numerical distances between the two power vectors.

The result is restricted to proper simple games through four players.

Without properness, divergence occurs already at three players; that contrast is included only to delimit the theorem's scope.

An unindexed historical power-index table, software package test set, thesis appendix, or teaching enumeration could contain the same finite census.

## References
1. J. Deegan Jr. and E. W. Packel, “A new index of power for simple \(n\)-person games,” *International Journal of Game Theory* 7 (1978), 113–123.
2. M. J. Holler, “Forming coalitions and measuring voting power,” *Political Studies* 30 (1982), 262–271.
3. J. M. Alonso-Meijide, M. Álvarez-Mozos, and M. G. Fiestras-Janeiro, “Power Indices and Minimal Winning Coalitions in Simple Games with Externalities,” UB Economics Working Paper E15/328, 2015; public working-paper version dated 4 September 2015.
