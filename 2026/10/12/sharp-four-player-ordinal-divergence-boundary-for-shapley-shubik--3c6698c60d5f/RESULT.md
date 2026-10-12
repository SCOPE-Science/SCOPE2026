# Sharp four-player ordinal divergence boundary for Shapley–Shubik and the nucleolus
## Finding
A **proper simple voting game** is a monotone \(0\)-\(1\) cooperative game \(v\) with
\[
v(\varnothing)=0,\qquad v(N)=1,
\]
such that no coalition and its complement are both winning.

For such a game, the **Shapley–Shubik vector** is the Shapley value of \(v\). Its \(i\)-th coordinate is the probability that player \(i\) is pivotal in a uniformly random ordering of the players.

The **nucleolus** is the unique imputation that lexicographically minimizes the sorted coalition-excess vector
\[
e(S,x)=v(S)-\sum_{i\in S}x_i.
\]

Two allocations are said here to induce the same **weak player ranking** when every pair of players is ordered or tied in the same way.

Every proper simple game with at most three players gives the same weak player ranking under Shapley–Shubik and the nucleolus.

For four players there are exactly
\[
80
\]
labeled proper simple games, and exactly
\[
36
\]
of them have different weak rankings under the two solutions.

Those \(36\) games form exactly three isomorphism classes under player relabeling. Each class has orbit size
\[
12.
\]

Writing minimal winning coalitions with players \(A,B,C,D\), canonical representatives are:
\[
\mathcal W_1=\{AB,AC\},
\]
\[
\mathcal W_2=\{AB,AC,BCD\},
\]
and
\[
\mathcal W_3=\{AB,ACD\}.
\]

All three are weighted voting games. They admit the representations
\[
[3;2,1,1,0],
\qquad
[5;3,2,2,1],
\qquad
[5;3,2,1,1],
\]
respectively.

For \(\mathcal W_1\), the Shapley–Shubik vector is
\[
\left(\frac23,\frac16,\frac16,0\right),
\]
while the nucleolus is
\[
(1,0,0,0).
\]
Thus Shapley–Shubik ranks
\[
A>B=C>D,
\]
whereas the nucleolus ranks
\[
A>B=C=D.
\]

For \(\mathcal W_2\), the Shapley–Shubik vector is
\[
\left(\frac5{12},\frac14,\frac14,\frac1{12}\right),
\]
while the nucleolus is
\[
\left(\frac13,\frac13,\frac13,0\right).
\]
Thus Shapley–Shubik ranks
\[
A>B=C>D,
\]
whereas the nucleolus ranks
\[
A=B=C>D.
\]

For \(\mathcal W_3\), the Shapley–Shubik vector is
\[
\left(\frac7{12},\frac14,\frac1{12},\frac1{12}\right),
\]
while the nucleolus is
\[
(1,0,0,0).
\]
Thus Shapley–Shubik ranks
\[
A>B>C=D,
\]
whereas the nucleolus ranks
\[
A>B=C=D.
\]

The divergence is not caused only by dummy players. Among the \(50\) labeled proper four-player games with no dummy player, exactly
\[
24
\]
diverge. They are precisely the relabelings of \(\mathcal W_2\) and \(\mathcal W_3\).

Hence four players are the sharp first size at which Shapley–Shubik power ranking and nucleolus ranking can disagree in proper simple games.

## Assumptions and scope
A simple game is represented by its antichain of minimal winning coalitions. Properness means that no winning coalition has a winning complement.

The comparison is ordinal: only the weak ranking of players induced by each allocation is compared. Equality of the numerical allocations is not required.

The Shapley–Shubik index is the Shapley value specialized to a simple voting game. The nucleolus is computed on the imputation set, including individual-rationality constraints.

The classification covers every labeled proper simple game on one through four players. The result does not claim a count for five or more players, and it does not classify non-proper simple games.

## Proof
Every monotone simple game with \(v(\varnothing)=0\) and \(v(N)=1\) is uniquely represented by a nonempty antichain of nonempty coalitions: its minimal winning coalitions.

The verifier enumerates all such antichains for \(n\le4\) and filters by properness. The exact labeled counts are
\[
1,\ 3,\ 11,\ 80
\]
for one, two, three, and four players.

The corresponding numbers of isomorphism classes under player relabeling are
\[
1,\ 2,\ 5,\ 14.
\]

For each game, the Shapley–Shubik vector is computed exactly from pivotal coalitions:
\[
\phi_i(v)=
\sum_{S\subseteq N\setminus\{i\}}
\frac{|S|!\,(n-|S|-1)!}{n!}
\bigl(v(S\cup\{i\})-v(S)\bigr).
\]

The nucleolus is verified by exact rational least-core calculations together with structural certificates.

If a proper simple game has veto players, every core allocation gives zero to non-veto players. Symmetry among veto players then determines the nucleolus whenever they form one automorphism orbit.

For \(\mathcal W_1\) and \(\mathcal W_3\), player \(A\) is the unique veto player. The core is therefore the singleton
\[
(1,0,0,0),
\]
which is necessarily the nucleolus.

For \(\mathcal W_2=\{AB,AC,BCD\}\), let
\[
x_A+x_B+x_C+x_D=1.
\]
The sum of the excesses of its three minimal winning coalitions is
\[
e(AB,x)+e(AC,x)+e(BCD,x)=1+x_D.
\]
Consequently the largest coalition excess is at least \(1/3\).

At
\[
x=\left(\frac13,\frac13,\frac13,0\right),
\]
all three displayed excesses equal \(1/3\), and every coalition excess is at most \(1/3\). Thus the least-core value is exactly \(1/3\). Equality in the lower bound forces
\[
x_D=0
\]
and forces all three minimal-winning excesses to equal \(1/3\), which uniquely determines the displayed allocation. The least core is therefore a singleton, hence this point is the nucleolus.

For every remaining four-player isomorphism class, the verifier computes the exact rational least core. Whenever the first least core is a singleton, it is the nucleolus immediately. In the only class whose first least core is not a singleton, the two extreme points are interchanged by an automorphism and the unique symmetry-fixed point is the nucleolus. These values agree in weak ranking with the Shapley–Shubik vector.

After expanding the \(14\) canonical classes by orbit size, exactly \(36\) of the \(80\) labeled proper games diverge. Canonicalization shows that the divergent games are exactly three orbits, each of size \(12\).

Finally, a player is a dummy exactly when its Shapley–Shubik coordinate is zero. Filtering them out leaves \(50\) labeled proper four-player games, of which \(24\) diverge; these are exactly the two nondummy divergent orbits.

## Verification
The embedded `verify_shapley_nucleolus_proper_simple_games.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- every proper simple game on one through four players;
- exact labeled counts \(1,3,11,80\);
- exact isomorphism-class counts \(1,2,5,14\);
- exact Shapley–Shubik vectors from pivotal coalitions;
- exact nucleoli from core or rational least-core certificates;
- agreement of weak rankings for every game through three players;
- exactly \(36\) divergent labeled four-player games;
- exactly three divergent isomorphism classes, each of orbit size \(12\);
- the three displayed canonical minimal-winning families;
- the three displayed Shapley–Shubik vectors and nucleoli;
- \(50\) proper four-player games without dummies;
- exactly \(24\) nondummy divergences, in two isomorphism classes.

Run:

`python3 verify_shapley_nucleolus_proper_simple_games.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The Shapley–Shubik index and the nucleolus are classical cooperative-game solution concepts with different interpretations: the first measures pivotal voting power, while the second lexicographically stabilizes coalition excesses.

Elkind, Goldberg, Goldberg, and Wooldridge study weighted threshold games as models of voting power and payoff division and explicitly analyze the core, least core, and nucleolus.

Elkind and Pasechnik give a later full treatment of computing the nucleolus of weighted voting games, emphasizing political decision-making as a principal application.

Tauman and Zapechelnyuk directly compare the Shapley value and nucleolus in four-player cooperative games and show that the concepts can behave differently. Their model is not a \(0\)-\(1\) proper simple voting game and does not provide the finite classification proved here.

The new claim is the sharp ordinal boundary and complete first layer for proper simple games: no divergence through three players, exactly \(36\) labeled divergences at four players, exactly three isomorphism classes, and a \(24\)-game nondummy sublayer.

Targeted searches using the two solution names, proper/simple/weighted voting terminology, four-player ranking language, the three canonical weighted representations, and exact census language did not locate an equivalent classification.

## Limitations
The result compares weak player rankings, not Euclidean distance or another numerical discrepancy between power allocations.

The classification stops at four players. It makes no asymptotic claim.

All three first-layer divergent classes happen to be weighted voting games, but the theorem does not classify all weighted games beyond four players.

An unindexed power-index table, software test corpus, thesis appendix, or historical enumeration could contain the same finite census.

## References
1. E. Elkind, L. A. Goldberg, P. W. Goldberg, and M. Wooldridge, “Computational Complexity of Weighted Threshold Games,” *Proceedings of the Twenty-Second AAAI Conference on Artificial Intelligence* (2007), 718–723.
2. E. Elkind and D. V. Pasechnik, “Computing the nucleolus of weighted voting games,” arXiv:0808.0298, first submitted 3 August 2008.
3. Y. Tauman and A. Zapechelnyuk, “On (non-) monotonicity of cooperative solutions,” *International Journal of Game Theory* 39 (2010), 171–175. DOI: 10.1007/s00182-009-0196-z.
