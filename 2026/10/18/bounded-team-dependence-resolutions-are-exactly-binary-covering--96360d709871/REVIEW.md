# Independent mathematical audit

## correctness

PASS

For r>=2, each truth set in an admissible flat disjunction excludes every conflicting pair (same predictor, opposite output), hence is a partial graph. Extending it to a total graph does not create a false-positive team. Every size-s partial graph, s=min(r,2^k), must extend to a selected total graph; this is exactly coverage of all s-column patterns. Conversely each valid smaller partial graph can extend to size s, and the rows are classically definable graph formulas. For r=1 the tautology works, while zero disjuncts cannot accept a singleton. Full strength needs every row. The exact strength-two formula is supported by Lawrence et al.; Stirling gives a maximum column count of order 2^N/sqrt(N) and the claimed inversion. At strength three on four columns, the eight required patterns and the even-parity extension prove optimality. The independent replay python3 /workspace/independent_checks.py (check 5) optimized directly over arbitrary flat truth sets for six (m,r) pairs, considering 318 teams in total, including both endpoints and the full k=2 profile. This is corroboration, not the general proof.

## originality

PASS

Pass is for the exact minimum-width correspondence under the bounded-team semantics, including why the singleton case differs. The covering-array optima and normal-form semantics are known ingredients, not independent originality claims.

## value

PASS

For a fundamental propositional dependence atom this gives an exact formula-size invariant restricted by the amount of information available to a team. The reduction transfers sharp array bounds and constructions at every strength without falsely claiming a closed form for unknown higher-strength optima; it separates the singleton, pairwise and saturated regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
