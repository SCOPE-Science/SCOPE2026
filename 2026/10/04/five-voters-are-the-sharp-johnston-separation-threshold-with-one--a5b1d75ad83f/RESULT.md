# Five voters are the sharp Johnston separation threshold, with one sparsest witness class

## Finding

For monotone simple voting games, five players are necessary and sufficient for the Johnston index to induce a different weak player ordering from both normalized Banzhaf–Coleman and Shapley–Shubik. Exhaustively, no such divergence occurs for \(1\le |N|\le4\); among the \(208\) isomorphism classes on five players, exactly \(34\) diverge. The sparsest divergent games have exactly three minimal winning coalitions and form one isomorphism class, represented by
\[
\mathcal{M}=\{\{2,3,4\},\{2,3,5\},\{1,4,5\}\}.
\]

## Assumptions and scope

A simple voting game is a monotone map \(v:2^N\to\{0,1\}\) with \(v(\varnothing)=0\) and \(v(N)=1\). A player is critical in a winning coalition \(W\) when removing that player makes \(W\) losing. The normalized Banzhaf–Coleman index normalizes each player's number of critical winning coalitions. The Shapley–Shubik index weights a swing whose losing predecessor has size \(k\) by \(k!(n-k-1)!/n!\). The Johnston score gives each critical member of a winning coalition \(W\) the share \(1/d(W)\), where \(d(W)\) is the number of critical members of \(W\), and the Johnston index normalizes these scores.

Two indices have the same weak player ordering when every player pair has the same strict comparison or tie under both. The claim ranges over all labeled monotone simple games for the lower bound and over isomorphism classes under player relabeling for the five-player census.

## Proof

Every monotone Boolean function on \(k\) variables is uniquely determined by its two restrictions at the last variable, \(f_0\) and \(f_1\), with \(f_0\le f_1\) pointwise. Recursively generating every ordered pair \((f_0,f_1)\) with this relation enumerates every monotone Boolean function exactly once. After imposing \(v(\varnothing)=0\) and \(v(N)=1\), the numbers of labeled simple games for \(n=1,2,3,4,5\) are
\[
1,\ 4,\ 18,\ 166,\ 7579.
\]

For every game with \(n\le4\), exact rational computation of all three indices gives identical signs for every pairwise difference. Thus no Johnston/Banzhaf or Johnston/Shapley–Shubik ordinal divergence is possible with fewer than five players.

For \(n=5\), canonicalizing each minimal-winning-coalition antichain under all \(5!\) player permutations gives \(208\) isomorphism classes. Exactly \(34\) classes have a Johnston weak order different from the Banzhaf weak order; the same \(34\) classes are exactly those where Johnston differs from Shapley–Shubik. In labeled form these classes account for \(1870\) of the \(7579\) simple games.

Among the divergent games, the minimum possible number of minimal winning coalitions is three. There are \(30\) labeled divergent games with three minimal winning coalitions, and canonicalization puts all \(30\) into one isomorphism class. A representative has
\[
\mathcal{M}=\{\{2,3,4\},\{2,3,5\},\{1,4,5\}\}.
\]
For this game the normalized Banzhaf–Coleman vector is
\[
\left(\frac{3}{23},\frac{5}{23},\frac{5}{23},\frac{5}{23},\frac{5}{23}\right),
\]
the Shapley–Shubik vector is
\[
\left(\frac{2}{15},\frac{13}{60},\frac{13}{60},\frac{13}{60},\frac{13}{60}\right),
\]
and the normalized Johnston vector is
\[
\left(\frac{1}{8},\frac{11}{48},\frac{11}{48},\frac{5}{24},\frac{5}{24}\right).
\]
Hence Banzhaf–Coleman and Shapley–Shubik tie players \(2,3,4,5\), whereas Johnston ranks players \(2,3\) strictly above players \(4,5\). This proves the sharp five-player separation and the unique sparsest witness class.

## Verification

The accompanying `verify_johnston_cutoff.py` independently reconstructs the monotone-function recursion, checks the labeled simple-game counts, computes the three indices using exact `Fraction` arithmetic, compares every player pair, canonicalizes five-player games under all player permutations, and verifies the witness vectors. A replay returned `VERIFY_OK`, with \(208\) five-player isomorphism classes, \(34\) divergent classes, \(1870\) divergent labeled games, and one sparsest divergent isomorphism class.

## Relationship to prior work

Freixas, Marciniak and Pons studied ordinal equivalence of exactly the Johnston, Banzhaf and Shapley–Shubik indices and proved equivalence on semicomplete simple games, a class containing complete games. Diffo Lambo and Moulen earlier characterized Banzhaf/Shapley–Shubik ordinal agreement with the desirability relation on swap-robust games. Freixas and Marciniak give the standard simple-game formulas and further comparisons involving Johnston and Banzhaf. The checked literature therefore makes the three-index ordinal-equivalence question structurally natural, but the inspected material did not state the unrestricted small-player cutoff, the \(34\)-class five-player census, or the unique three-minimal-winning-coalition witness class.

As an independent enumeration check, the standard count of \(210\) permutation classes of antichains on a five-set includes the two constant monotone functions; removing those two boundary-violating cases gives the \(208\) simple-game classes recovered here.

## Limitations

The result is a complete finite classification only at the first separation order \(n=5\). It does not classify larger-player divergence or quantify distances between index values. The full text of the most directly relevant 2012 ordinal-equivalence paper could not be inspected because institutional retrieval stopped at interactive human verification; its abstract and bibliographic material were checked, so an unobserved example or finite-table remark in the inaccessible body remains a residual originality risk.

## References

- J. Freixas, D. Marciniak, M. Pons, “On the ordinal equivalence of the Johnston, Banzhaf and Shapley power indices,” *European Journal of Operational Research* 216 (2012), 367–375. DOI: 10.1016/j.ejor.2011.07.028.
- J. Freixas, D. Marciniak, “Egalitarian property for power indices,” *Social Choice and Welfare* 40 (2013), 207–227. DOI: 10.1007/s00355-011-0593-7; published online 21 September 2011.
- L. Diffo Lambo, J. Moulen, “Ordinal equivalence of power notions in voting games,” *Theory and Decision* 53 (2002), 313–325. DOI: 10.1023/A:1024158301610.
