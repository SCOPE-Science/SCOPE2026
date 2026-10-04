# TITLE_PLACEHOLDER
## Finding
Among five-player weighted simple voting games, exactly \(17\) of the \(117\) isomorphism classes violate local monotonicity for the Deegan–Packel index. Here local monotonicity is understood in the standard dominance/desirability sense: if player \(i\) is at least as desirable as player \(j\), the index should not assign \(i\) less power than \(j\).

Every violating class has at least \(3\) minimal winning coalitions. The violating classes with exactly \(3\) minimal winning coalitions form one isomorphism class. A representative is the weighted game \([8;5,3,2,1,1]\), whose minimal winning coalitions are
\[
\{1,2\},\qquad \{1,3,4\},\qquad \{1,3,5\}.
\]
Player \(2\) strictly dominates player \(3\): for example, adjoining player \(2\) to coalition \(\{1\}\) reaches the quota, whereas adjoining player \(3\) does not. Nevertheless the normalized Deegan–Packel vector is
\[
\left(\frac{{7}}{{18}},\frac{{1}}{{6}},\frac{{2}}{{9}},\frac{{1}}{{9}},\frac{{1}}{{9}}\right),
\]
so the index ranks player \(3\) above the strictly more desirable player \(2\).

## Assumptions and scope
A simple game is a monotone Boolean decision rule on a five-player set with the empty coalition losing and the grand coalition winning. Two games are isomorphic when a permutation of the five players carries the set of minimal winning coalitions of one game to that of the other. A game is weighted when some nonnegative weights and positive quota realize its winning coalitions.

For players \(i\) and \(j\), player \(i\) is at least as desirable as \(j\) when every coalition containing neither player that becomes winning after adding \(j\) also becomes winning after adding \(i\). The Deegan–Packel raw score is
\[
DP_i^r(v)=\sum_{{S\in\mathcal{{M}}_i(v)}}\frac{{1}}{{|S|}},
\]
and normalization divides all raw scores by the number \(|\mathcal{{M}}(v)|\) of minimal winning coalitions, so normalization does not change player ordering.

The result is an exact finite classification for five-player weighted games only. It does not assert a formula for larger numbers of players, nor does it change the previously known fact that Deegan–Packel local monotonicity first can fail at five players.

## Proof
The proof is exhaustive and finite. The accompanying verifier uses two generation routes.

First, it generates all monotone Boolean functions on five variables recursively. Removing the two constant functions leaves exactly \(7579\) labeled simple games. It computes the desirability relation directly from the truth table and retains the \(3285\) labeled complete games. Canonicalizing the minimal-winning-coalition antichain under all \(5!\) player permutations yields exactly \(117\) isomorphism classes.

Second, independently of the monotone-function generator, the verifier enumerates every nonincreasing integer weight vector with entries from \(0\) through \(5\), together with every positive quota up to the total weight. The resulting canonical weighted classes are exactly the same \(117\) classes from the first route. Thus every complete five-player class found in the first route has an explicit weighted representation, while every weighted game is complete; these \(117\) classes are therefore precisely the five-player weighted games.

For each of the \(3285\) labeled complete games, the verifier reconstructs its minimal winning coalitions, computes exact rational Deegan–Packel scores, and checks every ordered dominance pair. There are \(695\) labeled games with a strict local-monotonicity violation. Canonicalization gives exactly \(17\) violating isomorphism classes.

Among those \(695\) labeled violations, the minimum number of minimal winning coalitions is \(3\). Exactly \(60\) labeled games attain this minimum, and all \(60\) canonicalize to the same isomorphism class. Its canonical minimal-winning antichain is \(\{\{1,2\},\{1,3,4\},\{1,3,5\}\}\), and the verifier checks directly that \([8;5,3,2,1,1]\) realizes it.

For that representative, the raw Deegan–Packel scores are
\[
\left(\frac{{7}}{{6}},\frac{{1}}{{2}},\frac{{2}}{{3}},\frac{{1}}{{3}},\frac{{1}}{{3}}\right).
\]
Dividing by the three minimal winning coalitions gives the normalized vector displayed above, proving the claimed reversal between players \(2\) and \(3\).

## Verification
Run `python verify_deegan_packel_census.py dp_census.json`. The archived census is accepted only if the exact regenerated object matches byte-for-byte at the JSON value level. The verifier reports `VERIFY_OK` and checks the counts \(7579\), \(3285\), \(117\), \(695\), and \(17\), the minimum support size \(3\), the single sparsest isomorphism class, the explicit weighted representation, the dominance witness, and the exact rational Deegan–Packel vector.

The second weighted-generation route is a constructive cross-check of weightedness: it supplies an integer weighted representation with maximum individual weight at most \(5\) for every one of the \(117\) complete classes found by the first route. No floating-point arithmetic or optimization solver is used in the verifier.

## Relationship to prior work
Deegan and Packel introduced the index based on equal division within minimal winning coalitions. Freixas and Kurz later studied the cost of restoring local monotonicity. Their 2014 preprint defines dominance and local monotonicity in the same framework used here and gives, for the pair formed by the raw Johnston and raw Deegan–Packel indices, zero cost through four players and positive cost at five players, with an explicit five-player weighted example. Thus the five-player onset of Deegan–Packel nonmonotonicity is prior work rather than part of the new claim.

Freixas also tabulated \(117\) complete and \(117\) weighted isomorphism classes for five voters. That total agrees with the independent census here, but the inspected table does not classify which classes violate Deegan–Packel local monotonicity. The contribution here is the exact \(17/117\) violation census and the structural statement that the sparsest violations require three minimal winning coalitions and form a unique isomorphism class.

## Limitations
The originality comparison is literature-based rather than a formal proof that no unindexed source contains the same finite census. Searches and inspections found the known five-player cutoff and total weighted-game count but no source stating the exact \(17\)-class violation count or the unique three-minimal-winner class. An unindexed thesis, software table, or supplementary dataset could therefore reduce the originality of the classification without affecting its correctness.

The result concerns the standard Deegan–Packel index and player desirability. It does not classify other minimal-winning-coalition indices, alternative notions of monotonicity, or games with more than five players.

## References
1. J. Deegan Jr. and E. W. Packel, “A new index of power for simple n-person games,” *International Journal of Game Theory* 7 (1978), 113–123. DOI: 10.1007/BF01753239.
2. J. Freixas and S. Kurz, “The cost of getting local monotonicity,” arXiv:1411.0944, first submitted 4 November 2014; later *European Journal of Operational Research* 251 (2016), 275–285. DOI: 10.1016/j.ejor.2015.11.030.
3. J. Freixas, “Bounds for Owen’s multilinear extension,” *Journal of Applied Probability* 44 (2007), 852–864. DOI: 10.1239/jap/1197908809. Table 1 gives the five-player totals of \(117\) complete and \(117\) weighted isomorphism classes.
