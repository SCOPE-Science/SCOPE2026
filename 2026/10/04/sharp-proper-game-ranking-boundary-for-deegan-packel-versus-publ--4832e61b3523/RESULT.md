# Sharp proper-game ranking boundary for Deegan-Packel versus Public Good power
## Finding
Let \(v\) be a monotone simple voting game. A winning coalition is **minimal winning** if deleting any member makes it losing. The game is **proper** if no coalition and its complement are both winning.

For player \(i\), let \(\mathcal M_i(v)\) be the minimal winning coalitions containing \(i\), and let \(\mathcal M(v)\) be the full minimal-winning family.

The normalized Public Good index is proportional to
\[
PG_i(v)=|\mathcal M_i(v)|,
\]
while the normalized Deegan-Packel index is proportional to
\[
DP_i(v)=\sum_{S\in\mathcal M_i(v)}\frac1{|S|}.
\]
Normalization does not affect the weak player ordering.

For every proper simple game with at most \(3\) players, the two weak player orderings coincide.

This cutoff is sharp. There are exactly \(80\) labeled proper simple games on \(4\) players. Exactly \(30\) of them give different weak player orderings under the Public Good and Deegan-Packel indices. Up to relabeling, those \(30\) games form exactly three classes:

\[
\mathcal M_A=\bigl\{\{1,2\},\{1,3,4\}\bigr\},
\]
\[
\mathcal M_B=\bigl\{\{1,2\},\{1,3\},\{2,3,4\}\bigr\},
\]
and
\[
\mathcal M_C=\bigl\{\{1,2\},\{1,3,4\},\{2,3,4\}\bigr\}.
\]

Their labeled orbit sizes are respectively
\[
12,\qquad12,\qquad6.
\]

All three are weighted majority games:
\[
\mathcal M_A=[5;3,2,1,1],
\qquad
\mathcal M_B=[5;3,2,2,1],
\qquad
\mathcal M_C=[4;2,2,1,1].
\]
Thus four players are also the first possible size for an ordinal disagreement between these two indices inside proper weighted voting games.

The raw index vectors on the three canonical representatives are:
\[
PG(A)=(2,1,1,1),
\qquad
DP(A)=\left(\frac56,\frac12,\frac13,\frac13\right),
\]
\[
PG(B)=(2,2,2,1),
\qquad
DP(B)=\left(1,\frac56,\frac56,\frac13\right),
\]
and
\[
PG(C)=(2,2,2,2),
\qquad
DP(C)=\left(\frac56,\frac56,\frac23,\frac23\right).
\]
Hence each disagreement is visible directly as a different pattern of ties in the weak ordering.

Properness is essential to the boundary. If arbitrary simple games are allowed, divergence already occurs with three players. The unique three-player divergent isomorphism class has
\[
\mathcal M=\bigl\{\{1\},\{2,3\}\bigr\},
\]
with its three labeled relabelings. This game is improper because \(\{1\}\) and its complement \(\{2,3\}\) are both winning.

## Assumptions and scope
A simple game is monotone, has the empty coalition losing, and has the grand coalition winning. The result uses only properness; constant-sum, strongness, completeness, and weightedness are not assumed for the universal lower bound.

Two indices are called ordinally equivalent here when they induce the same weak preorder on players, including the same ties.

The census is complete for proper simple games through four players. The theorem does not classify larger games.

## Proof
Every monotone simple game is uniquely determined by its nonempty antichain of minimal winning coalitions.

For each \(n\le4\), the verifier constructs this antichain family in two independent ways:

1. recursively, by including or excluding coalitions while deleting comparable candidates;
2. by brute force over all families of nonempty coalitions and retaining exactly the antichains.

The two constructions agree exactly.

The labeled simple-game and proper-game counts are
\[
\begin{array}{c|rrrr}
n&1&2&3&4\\ \hline
\text{simple games}&1&4&18&166\\
\text{proper simple games}&1&3&11&80.
\end{array}
\]

For every proper game, the verifier computes the raw Public Good count vector
\[
\bigl(|\mathcal M_i(v)|\bigr)_i
\]
and the raw Deegan-Packel vector
\[
\left(\sum_{S\in\mathcal M_i(v)}\frac1{|S|}\right)_i
\]
using exact rational arithmetic, then compares every pairwise player relation.

There are no disagreements for \(n=1,2,3\). For \(n=4\), exactly \(30\) of the \(80\) proper games disagree.

Canonicalization under all \(4!\) player relabelings gives exactly three isomorphism classes, with orbit sizes
\[
12,\quad12,\quad6.
\]
The three canonical minimal-winning families are exactly the families \(\mathcal M_A,\mathcal M_B,\mathcal M_C\) displayed above.

Finally, direct enumeration of weighted coalitions verifies the representations
\[
[5;3,2,1,1],\qquad[5;3,2,2,1],\qquad[4;2,2,1,1].
\]
This proves the same sharp four-player boundary in the proper weighted subclass.

For comparison, dropping properness gives exactly three labeled divergent games already at \(n=3\), all relabelings of
\[
\bigl\{\{1\},\{2,3\}\bigr\}.
\]

## Verification
The embedded `verify_dp_pgi_proper_boundary.py` uses only the Python standard library and exact rational arithmetic.

It checks:
- two independent generators for every nonempty antichain through \(n=4\);
- the exact simple/proper counts \(1,4,18,166\) and \(1,3,11,80\);
- zero proper ordinal disagreements through \(n=3\);
- exactly \(30\) proper four-player disagreements;
- exactly three four-player isomorphism classes with orbit sizes \(12,12,6\);
- the exact raw Public Good and Deegan-Packel vectors of all three classes;
- direct weighted representations of all three classes;
- the three labeled improper three-player disagreements.

Run:

`python3 verify_dp_pgi_proper_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Deegan and Packel introduced the index that weights each minimal winning coalition equally and divides its contribution equally among its members. Holler introduced the Public Good index, whose raw form counts each player's memberships in minimal winning coalitions.

Freixas and Kurz directly compare the Public Good and Deegan-Packel indices. Their open preprint states the two raw formulas, observes that both can violate local monotonicity, and gives the three-player weighted game
\[
\mathcal M=\bigl\{\{1\},\{2,3\}\bigr\}
\]
as an example where the normalized Public Good and Deegan-Packel values differ. That example is precisely the unique three-player divergent isomorphism class found by the verifier, but it is improper.

The same paper proves that on uniform complete simple games, where all minimal winning coalitions have one size, the two indices induce the same ranking because their raw vectors differ only by a common scalar. This explains one large coincidence subclass but does not settle the proper-game boundary, since proper games may have minimal winning coalitions of different sizes.

Targeted literature and exact-count searches did not locate the statement that properness postpones the first ordinal disagreement to four players, nor the complete \(30\)-game, three-isomorphism-class census.

## Limitations
The result is about weak player rankings, not equality of normalized numerical index values.

The four-player census covers proper simple games, and the three witnesses show the sharp boundary already inside proper weighted majority games. No claim is made that every larger proper game must exhibit disagreement.

The oldest foundational papers are bibliographically dated to the late 1970s and early 1980s, but the day-resolved public-source date recorded for this package is the first submission date of the inspected open preprint by Freixas and Kurz. An unindexed historical note, thesis, or table could contain the same small-game classification.

## References
1. J. Deegan Jr. and E. W. Packel, “A New Index of Power for Simple \(n\)-Person Games,” *International Journal of Game Theory* 7 (1978), 113–123. DOI: 10.1007/BF01753239.
2. M. J. Holler, “Forming Coalitions and Measuring Voting Power,” *Political Studies* 30 (1982), 262–271.
3. M. J. Holler and E. W. Packel, “Power, Luck and the Right Index,” *Journal of Economics* 43 (1983), 21–29.
4. J. Freixas and S. Kurz, “The cost of getting local monotonicity,” arXiv:1411.0944, first submitted 4 November 2014.
