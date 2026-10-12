# Complete six-player ordinal-divergence layer for Shapley–Shubik and Banzhaf power
## Finding
A **simple voting game** on player set \(N\) is a monotone map
\[
v:2^N\to\{0,1\}
\]
with \(v(\varnothing)=0\) and \(v(N)=1\). A coalition is winning when its value is \(1\).

The **Penrose–Banzhaf–Coleman score** of player \(i\) is the number of coalitions \(S\subseteq N\setminus\{i\}\) for which
\[
v(S)=0,\qquad v(S\cup\{i\})=1.
\]
Normalization by the total number of swings does not change its player ranking.

The **Shapley–Shubik index** of player \(i\) is
\[
\phi_i(v)=\sum_{S\subseteq N\setminus\{i\}}
\frac{|S|!\,(|N|-|S|-1)!}{|N|!}
\bigl(v(S\cup\{i\})-v(S)\bigr).
\]

Prior work establishes that the two induced player preorderings are not always ordinally equivalent once a simple game has six or more players. The new result is the complete first six-player layer.

There are exactly
\[
7{,}828{,}352
\]
labeled simple games on six players. Exactly
\[
2{,}540{,}340
\]
of them have different Shapley–Shubik and Banzhaf weak rankings. Thus the exact incidence is
\[
\frac{2{,}540{,}340}{7{,}828{,}352}
 =\frac{635085}{1957088}.
\]

The disagreement has a rigid direction. In every divergent six-player game, every strict Banzhaf comparison is preserved by Shapley–Shubik, while at least one Banzhaf tie is split by Shapley–Shubik. Equivalently,
\[
\text{the Shapley–Shubik weak order strictly refines the Banzhaf weak order.}
\]
There are no strict pairwise reversals and no cases in which Banzhaf strictly separates a pair that Shapley–Shubik ties.

Every divergent six-player game is dummy-free.

Among the
\[
1{,}422{,}563
\]
labeled proper six-player simple games, exactly
\[
573{,}960
\]
have different weak rankings, an incidence of
\[
\frac{573960}{1422563}.
\]

A compact proper witness has minimal winning coalitions
\[
\{ABC,\ ABDE,\ ADEF,\ BDEF\}.
\]
Its raw Banzhaf swing counts are
\[
(10,10,6,6,6,4),
\]
so its normalized Banzhaf vector is
\[
\left(\frac5{21},\frac5{21},\frac17,\frac17,\frac17,\frac2{21}\right).
\]
Its Shapley–Shubik vector is
\[
\left(\frac7{30},\frac7{30},\frac2{15},\frac3{20},\frac3{20},\frac1{10}\right).
\]
Hence Banzhaf gives
\[
A=B>C=D=E>F,
\]
whereas Shapley–Shubik gives
\[
A=B>D=E>C>F.
\]

The mechanism is visible in the swing-size spectra. Player \(C\) has swings by losing-coalition size
\[
(1,3,2)
\]
at sizes \(2,3,4\), while player \(D\) has
\[
(0,3,3).
\]
Both have six Banzhaf swings, but Shapley–Shubik weights swing sizes by the pivotal-order factor
\[
|S|!\,(5-|S|)!,
\]
so \(D\) receives more Shapley–Shubik power.

Players \(C\) and \(D\) are genuinely incomparable by the desirability relation in this witness: adding \(C\) to \(AB\) wins while adding \(D\) does not, whereas adding \(D\) to \(AEF\) wins while adding \(C\) does not.

## Assumptions and scope
Games are labeled, monotone, nontrivial simple games. The Banzhaf comparison may use either raw swing counts or the normalized Penrose–Banzhaf–Coleman index because normalization is common to all players within a game.

The result compares weak player rankings. A mismatch means that some pair is tied by one index and strictly ranked by the other, or strictly ordered in opposite directions. The census proves that only the first possibility occurs at six players, always with Shapley–Shubik splitting a Banzhaf tie.

A proper game has no winning coalition whose complement is also winning. A dummy has no swing coalition.

The enumeration is complete through six players. No numerical claim is made for seven or more players.

## Proof
Every simple game is uniquely determined by the antichain of its minimal winning coalitions. The verifier enumerates every nonempty antichain of the nonempty subsets of an \(n\)-player set for \(1\le n\le6\). It reconstructs the upward-closed winning set and computes both power vectors exactly.

The resulting labeled simple-game totals are
\[
1,\ 4,\ 18,\ 166,\ 7579,\ 7{,}828{,}352
\]
for \(n=1,\ldots,6\). These agree with the Dedekind-number identity \(M(n)-2\) for nontrivial monotone Boolean functions.

For every player, the Banzhaf score is the exact integer number of swing coalitions. The Shapley–Shubik comparison is also integral after multiplication by \(n!\): a swing coalition of size \(k\) contributes
\[
k!\,(n-k-1)!.
\]
Thus all pairwise comparisons are made without floating-point arithmetic.

For \(n\le5\), every game has identical weak rankings under the two indices. For \(n=6\), the verifier finds exactly \(2{,}540{,}340\) games with a mismatch.

Every mismatching player pair is classified into one of three possible types: strict reversal, a Banzhaf tie split by Shapley–Shubik, or a Shapley–Shubik tie split by Banzhaf. Across all six-player simple games, the counts of games exhibiting these types are respectively
\[
0,\quad 2{,}540{,}340,\quad 0.
\]
Therefore every divergent game is a strict Shapley–Shubik refinement of a Banzhaf tie.

Properness is checked independently in two equivalent finite ways: no winning coalition may have a winning complement, and no two minimal winning coalitions may be disjoint. The two tests agree for every enumerated game. They give \(1{,}422{,}563\) proper six-player games and \(573{,}960\) proper divergences.

A player is a dummy exactly when its Banzhaf swing count is zero. Every divergent game has all six swing counts positive, proving the dummy-free statement directly.

For the displayed witness, direct swing enumeration gives raw Banzhaf counts
\[
(10,10,6,6,6,4).
\]
The exact Shapley–Shubik numerators over denominator \(6!=720\) are
\[
(168,168,96,108,108,72),
\]
which reduce to the displayed vector.

## Verification
The embedded `verify_ss_banzhaf_six_player_layer.c` is a standalone exact verifier using only the C standard library and integer arithmetic.

Compile and run:

`gcc -O3 -std=c11 verify_ss_banzhaf_six_player_layer.c -o verify_ss_banzhaf && ./verify_ss_banzhaf`

A successful run contains `VERIFY_OK` and confirms:
- all labeled simple-game totals through six players;
- zero ordinal divergence through five players;
- exactly \(2{,}540{,}340\) six-player divergences;
- zero strict reversals;
- every divergence is a Shapley–Shubik split of a Banzhaf tie;
- exactly \(1{,}422{,}563\) proper six-player games and \(573{,}960\) proper divergences;
- every divergent game is dummy-free;
- the displayed witness, its swing-size spectra, Banzhaf counts, and exact Shapley–Shubik numerators.

## Relationship to prior work
Tomiyama's 1987 work introduced this ordinal-equivalence problem for the Shapley–Shubik and Banzhaf–Coleman indices. The available bibliographic and abstract records state that weighted majority games are ordinally equivalent and that ordinal equivalence can fail for nonweighted simple games with six or more players. That qualitative six-player boundary is prior and is not claimed here.

Diffo Lambo and Moulen later characterized swap-robust simple games as precisely the games in which both power preorderings coincide with the desirability preorder. Weighted majority games are swap robust, so this extends the weighted-game equivalence.

Friedman, McGrath, and Parker show that swap-preserving power measures, including Banzhaf and Shapley–Shubik, are ordinally equivalent on swap-robust games and characterize the hierarchies achievable there.

Carreras and Freixas extend ordinal-equivalence results to regular semivalues on a larger weakly linear class. Freixas, Marciniak, and Pons further establish ordinal equivalence of Johnston, Shapley–Shubik, and Penrose–Banzhaf–Coleman on semicomplete simple games.

The contribution here is different: it classifies the entire first six-player simple-game layer, including incomplete games. The exact count \(2{,}540{,}340\), the universal no-reversal/refinement phenomenon, the dummy-free statement, and the proper subcount \(573{,}960\) were not located in the inspected literature or exact-number searches.

## Limitations
The theorem is finite and stops at six players. The universal refinement phenomenon may fail at larger sizes; no extrapolation is claimed.

Tomiyama's 1987 article is historically earlier than the day-resolved source date stored in the metadata. Its original full text was not retrievable through the open sources or institutional retrieval attempted here. Available abstract-level evidence decisively establishes the prior six-or-more existence statement, but an unindexed table in that article or another historical source remains a residual originality risk for exact finite counts.

The metadata date is therefore the earliest day-resolved public source verified in the inspected literature, rather than an invented day for the 1987 paper.

## References
1. Y. Tomiyama, “Simple Game, Voting Representation and Ordinal Power Equivalence,” *Policy and Information* 11(1) (1987), 67–75.
2. L. Diffo Lambo and J. Moulen, “Ordinal equivalence of power notions in voting games,” *Theory and Decision* 53 (2002), 313–325. DOI: 10.1023/A:1024158301610.
3. J. Friedman, L. McGrath, and C. Parker, “Achievable Hierarchies In Voting Games,” *Theory and Decision* 61 (2006), 305–318. DOI: 10.1007/s11238-006-9003-5.
4. F. Carreras and J. Freixas, “On ordinal equivalence of power measures given by regular semivalues,” *Mathematical Social Sciences* 55 (2008), 221–234. DOI: 10.1016/j.mathsocsci.2007.08.004.
5. J. Freixas, D. Marciniak, and M. Pons, “On the ordinal equivalence of the Johnston, Banzhaf and Shapley power indices,” *European Journal of Operational Research* 216 (2012), 367–375. DOI: 10.1016/j.ejor.2011.07.028.
6. J. Freixas and D. Marciniak, “Egalitarian property for power indices,” *Social Choice and Welfare* 40 (2013), 207–227. DOI: 10.1007/s00355-011-0593-7.
