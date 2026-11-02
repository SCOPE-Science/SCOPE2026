# Scientific review

## Correctness

**PASS.** The column recurrence is equivalent to all binary closed-neighborhood parity equations including the boundary conditions. The stated matrix Fibonacci identities and rank lists determine the exact admissible seed spaces. Every allowed seed yields a unique codeword. Reflection around the forced zero column proves repeated blocks have exactly scaled weights and subcode-support unions, covering all lengths. Exact finite-base seed and span tables prove all coefficients and generalized weights. Direct brute force and exhaustive span generation in `verify.py` agree with the tables. Finite calculations are not substituted for the length-uniform argument.

## Originality

**PASS, with historical-priority qualification.** The recurrence, nullity count and reflection mechanism are already known and specifically credited; likewise square-board primeness itself is not offered as new. The final theorem concerns refined weight and entire subcode-support distributions for an infinite family rather than the pre-existing existence, code-size or zero-row criteria. The accessible primary materials inspected for the 2026 source, the 2005 parity-domination survey/article, and the classical Lights Out exposition do not state the six closed weight formulas or the four-row support-spectrum table. The original 2002 paper could not be inspected in full, and equivalent coding-theoretic formulations might already cover the result.

## Mathematical value

**PASS.** Exact size distributions of valid even-neighborhood configurations are natural statistical and coding invariants not recoverable from code dimension alone. The width-four strip is the first low-width transition from constant-weight to a two-weight family, with explicit positive multiplicities and an exact higher-support hierarchy for every repeated block length. The classification has a structural reflection proof and covers infinitely many labelled rectangles, not an isolated small search.

## Closest literature and limitations

Goldwasser–Klostermeyer–Ware (2002), *Fibonacci Polynomials and Parity Domination in Grid Graphs*, supplies foundational recurrence and existence methods; complete full text was inaccessible. Goldwasser–Klostermeyer (2005), *Parity Dominating Sets in Grid Graphs*, Theorem 3 states the total count \(2^d\), rather than cardinality and subcode-support counts. Klostermeyer (arXiv:2610.31475v1, 2026-10-22) studies prime nullspace matrices and presents zero-row reflection; its primeness results are acknowledged. A published Lights Out exposition supplies classical square-board nullspace examples. All conclusions here are restricted to binary closed neighborhoods of ordinary path products of width at most four; orbit counting and positive parity domination are not covered.

Self-review: passed. Independent audit: not yet performed.
