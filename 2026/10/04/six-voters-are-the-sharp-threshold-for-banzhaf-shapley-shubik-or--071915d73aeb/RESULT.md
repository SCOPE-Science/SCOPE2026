# Six voters are the sharp threshold for Banzhaf–Shapley–Shubik ordinal divergence

## Finding

Among monotone simple voting games, the normalized Banzhaf–Coleman and Shapley–Shubik player preorderings are ordinally equivalent for every game with \(\lvert N\rvert\le 5\), and this cutoff is sharp: for the six-player game with minimal winning coalitions \(\{2,3,4,5\}\), \(\{1,5,6\}\), \(\{3,6\}\), and \(\{2,6\}\), players \(1\) and \(4\) tie under normalized Banzhaf at \(1/24\) but Shapley–Shubik ranks player \(4\) above player \(1\), with \(1/20>1/30\).

## Assumptions and scope

A simple voting game is a monotone map \(v:2^N\to\{0,1\}\) with \(v(\varnothing)=0\) and \(v(N)=1\). For player \(i\), a coalition \(S\subseteq N\setminus\{i\}\) is a swing when \(v(S)=0\) and \(v(S\cup\{i\})=1\). The normalized Banzhaf–Coleman index divides each player's number of swings by the total number of swings. The Shapley–Shubik index weights each swing at coalition size \(k\) by \(k!(n-k-1)!/n!\). Two indices are ordinally equivalent here when every pair of players has the same strict comparison or tie under both indices.

The lower-bound statement ranges over all monotone simple games on labeled player sets with \(1\le \lvert N\rvert\le 5\), not only weighted or complete games.

## Proof

Every monotone Boolean function on \(k\) variables is determined uniquely by its restrictions \(f_0\) and \(f_1\) at the last variable, where both restrictions are monotone functions on \(k-1\) variables and \(f_0\le f_1\) pointwise. Starting from the two constant functions on zero variables and recursively taking every ordered pair \((f_0,f_1)\) with \(f_0\le f_1\) therefore enumerates every monotone Boolean function exactly once.

The recursion gives respectively \(3,6,20,168,7581\) monotone Boolean functions on \(1,2,3,4,5\) variables. Imposing \(v(\varnothing)=0\) and \(v(N)=1\) leaves exactly \(1,4,18,166,7579\) simple games. For every one of these games, exact rational computation of all swing counts and all Shapley–Shubik weights gives the same sign for every pairwise index difference under the two indices. Hence the two induced weak player orders coincide for every simple game with at most five players.

For six players, let the minimal winning coalitions be
\[
\{2,3,4,5\},\qquad \{1,5,6\},\qquad \{3,6\},\qquad \{2,6\}.
\]
Upward closure defines a simple game. Its raw Banzhaf swing counts are
\[
(2,8,8,2,4,24),
\]
so its normalized Banzhaf vector is
\[
\left(\frac{1}{24},\frac{1}{6},\frac{1}{6},\frac{1}{24},\frac{1}{12},\frac{1}{2}\right).
\]
Its Shapley–Shubik vector is
\[
\left(\frac{1}{30},\frac{1}{6},\frac{1}{6},\frac{1}{20},\frac{1}{12},\frac{1}{2}\right).
\]
Thus players \(1\) and \(4\) tie under normalized Banzhaf but not under Shapley–Shubik. This proves sharpness of the five-player equivalence cutoff.

## Verification

The accompanying `verify.py` performs the monotone-function recursion, checks the known monotone-function counts, filters the simple games, computes both indices with exact `Fraction` arithmetic, checks all pairwise weak-order signs for all \(5768\) simple games with at most five players, and reconstructs the six-player witness from its minimal winning coalitions. A replay from the packaged file returned `VERIFY_OK`, together with the counts \(1,4,18,166,7579\) and the two exact witness vectors above.

## Relationship to prior work

Diffo Lambo and Moulen studied ordinal equivalence of Shapley–Shubik and Banzhaf–Coleman through the desirability relation and swap robustness. Friedman, McGrath and Parker showed that swap-preserving measures, including these two indices, are ordinally equivalent on swap-robust simple voting games and characterized achievable hierarchies in that structured class. Freixas and Pons and subsequent work broadened the hierarchy and class-level analysis, including complete, weakly linear and semicomplete settings. The present finding asks a different finite-threshold question over all simple games: how many labeled players are needed before the two canonical weak rankings can disagree.

The checked literature supplies the natural ordinal-equivalence framework and class-level sufficient conditions. No checked source stated the all-simple-game cutoff \(\lvert N\rvert=6\) or the witness above. The finite exhaustion is therefore used to establish the lower bound directly rather than infer it from weighted or complete-game classifications.

## Limitations

The result concerns only the ordinal player preorder, not equality of the numerical index vectors. The six-player witness separates the rankings by a tie-versus-strict comparison rather than by a strict reversal. The claim is finite and exact; it does not classify all six-player counterexamples. One highly relevant later article on Johnston, Banzhaf and Shapley indices could be checked at abstract level but its full text was not available without interactive publisher verification, leaving a residual literature-coverage risk.

## References

1. L. Diffo Lambo and J. Moulen, “Ordinal equivalence of power notions in voting games,” *Theory and Decision* 53 (2002), 313–325, DOI: 10.1023/A:1024158301610.
2. J. Friedman, L. McGrath and C. Parker, “Achievable Hierarchies In Voting Games,” *Theory and Decision* 61 (2006), 305–318, DOI: 10.1007/s11238-006-9003-5.
3. J. Freixas and M. Pons, “Hierarchies achievable in simple games,” *Theory and Decision*, DOI: 10.1007/s11238-008-9108-0.
4. J. Freixas, D. Marciniak and M. Pons, “On the ordinal equivalence of the Johnston, Banzhaf and Shapley power indices,” *European Journal of Operational Research* 216 (2012), 367–375, DOI: 10.1016/j.ejor.2011.07.028.
5. J. Freixas, “Ordinal equivalence of power indices,” Voting Power and Procedures Workshop presentation (2011), London School of Economics.
