# Self-review

## Correctness

PASS. The auxiliary optimization is reconstructed from first principles. For fixed \(x\), minimizing the objective over the simplex of \(y\) is equivalent to putting all \(y\)-mass on a maximal coordinate of \(x\). For fixed maximum \(M\), convexity forces the remaining \(x\)-coordinates equal, reducing the problem to a one-variable strictly convex quadratic on \([a/n,a]\). Its stationary point and endpoint transition at \(b=2a\) give the stated exact minimum. The six-eigenvalue witness satisfies every displayed ordering and Eq. (9)/(10) constraint used in the source relaxation, and exact arithmetic gives the Eq. (12) value \(-7N^2/24\).

## Originality

PASS. The closest source is Rana--Parashar itself, which states the incorrect equal-coordinate minimizer and derives the \(N(2-5N)/16\) bound. Later work by Bag--Dey--Osaka supplies additional physical counterexample families and bounds for squared negativity minus geometric discord, but the searched material does not state this correction or imply the exact auxiliary minimum. Targeted semantic-database searches for the source, the Lagrange step, the \(2/5\) threshold, and exact aliases returned no equivalent mathematical statement. Previously recorded scientific findings were compared at claim-and-implication level; the closest relevant item concerns field-reflection symmetry of geometric discord in a thermal spin model, not this relaxation.

Residual bibliographic risk remains that an obscure correction or lecture note contains the same elementary minimization. No such source was located.

## Value

PASS. The result removes a quantitative threshold from a published argument in a central quantum-correlation example and replaces the erroneous optimization with its exact global solution. The all-\(N\) witness shows that this is not a tiny numerical adjustment: the displayed relaxation loses the claimed threshold completely. The scope is appropriately limited so that the source's genuine physical counterexamples remain intact.

Self-review: passed. Independent audit: not yet performed.
