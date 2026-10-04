# Review

## Correctness
PASS. The claim is an exact finite calculation. The proof derives the moments of the minimum and maximum from the three-point parent law, obtains an exact rational expression for the covariance and common variance, and therefore the Pearson correlation. The explicit counterexample is checked by substitution: \(81/319-1/4=5/1276>0\). The included verifier independently enumerates all \(27\) ordered samples with rational arithmetic and confirms the formula at multiple rational parameter values. The proof does not extrapolate from numerical experiments.

## Originality
PASS. The lead source explicitly formulates the probability-vector extension and states that uniform probabilities are expected to maximize correlations of order statistics, with no proof available. The closest database result found concerns the same three-point support with only two iid draws and proves uniform optimality there; it does not imply the three-draw statement. Searches for the exact constants, the three-draw extreme pair, and aliases of the conjecture did not locate a matching published statement. The 2021 maximal-correlation paper is a residual risk because its full text was not exhaustively inspected here, but the later lead paper cites it before stating the conjecture as unresolved.

## Value
PASS. This is a direct exact counterexample to a natural published conjectural direction, in the first higher-sample setting beyond the two-draw case on the smallest nontrivial lattice. The example changes the qualitative conclusion from uniform optimality to strict non-optimality, with a rational witness and a local derivative certificate.

## Closest literature and limitations
The closest literature is Papadatos's 2022 preprint on the discrete Terrell problem and López-Blázquez--Salamanca-Miño's 2021 work on maximal correlation for discrete order statistics. The finding does not classify global maximizers over probability vectors, and the 2021 article remains a limited-access originality risk as described above.

Same-model review: passed. Independent audit: not yet performed.
