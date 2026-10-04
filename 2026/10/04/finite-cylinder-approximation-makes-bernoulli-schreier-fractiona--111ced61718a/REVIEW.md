# Review

## Correctness

PASS. Bernshteyn proves \(\chi_B^*(G)=1/\alpha_\beta(G)\) for the Bernoulli free-part Schreier graph and proves that every value below \(\alpha_\beta(G)\) is exceeded by the measure of a clopen independent set. A clopen set in \(2^\Gamma\) has finite coordinate support. Taking the best independent cylinder on an increasing exhaustion therefore gives a monotone sequence of rational densities converging to \(\alpha_\beta(G)\). The finite independence test is decidable from group equality because cylinder intersection reduces to consistency of finitely many coordinate assignments. Reciprocals, capped initially by the finite-degree Borel coloring bound, give a computable decreasing rational sequence.

The claim is restricted to countably infinite effectively presented groups with decidable equality; no step assumes an effective rate of convergence.

## Originality

PASS. The closest source is Bernshteyn's 2022 paper itself: Theorem 1.1 supplies the reciprocal formula, while Lemma 2.2 and the following paragraph supply clopen approximation and finite-coordinate representation. Full-text inspection found no computability formulation. Searches for "right-c.e. Borel fractional chromatic number", "computable Borel fractional chromatic number", "finite cylinder approximation Bernoulli Schreier", and related terms found the Bernshteyn paper and background material but no statement that the invariant is a right-c.e. real. published-finding corpus searches likewise returned Schreier/Borel-coloring records but no matching finite-cylinder or right-c.e. result.

The new content is not the clopen approximation itself; it is the explicit monotone finite optimization formula under an effective group presentation and the resulting computability-theoretic classification.

## Value

PASS. Borel fractional chromatic number is an infinite definability-sensitive invariant, while the formula reduces it to a canonical sequence of finite rational optimization problems. The right-c.e. consequence gives a concrete effective upper-approximation mechanism without assuming amenability, residual finiteness, or a finite quotient model. This is a useful boundary statement: it isolates exactly what Bernoulli clopen approximation provides algorithmically and what remains open, namely lower approximation or full computability.

Same-model review: passed. Independent audit: not yet performed.
