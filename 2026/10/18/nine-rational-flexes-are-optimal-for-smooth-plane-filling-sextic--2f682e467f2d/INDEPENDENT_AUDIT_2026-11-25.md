# Independent mathematical audit

## correctness

PASS

Rebuilt the full 13-point evaluation kernel over F3 (rank 13, nullity 15), enumerated all 3^15 vectors and tested the exact quadratic coefficient in the tangent direction after excluding rational singular points. The counts at 1,3,5,7,9,11 flexes are 213408,1044576,1095120,527904,202176,39312, with none at any other count. Scalar normalization and generator closure partitioned the 11-flex stratum into four orbits and the 9-flex stratum into twenty. Direct tangent-line restrictions confirmed the representative counts, and exact Jacobian ideals on all three charts gave no smooth orbit at 11 and three smooth orbits at 9, each of size 5616. Thus 16848 projective equations, 33696 nonzero scalar equations, and trivial PGL3 stabilizers. The three encoded witnesses lie in distinct smooth orbits and the displayed equation matches the first. A smooth plane sextic has no line component and its tangent contains three other rational points, giving contact at most three by Bézout. Replay: python3 /workspace/branches/audit_sextics.py (NumPy, SymPy).

## originality

PASS

The exact all-sextic rational-flex bound and extremal census are distinct from the inspected family-specific flex results and degree-five classification. This is a best-of-knowledge statement, not a priority award.

## value

PASS

For the first field and degree specified, sharp rational tangent contact separates geometric smoothness from rational nonsingularity: the apparent eleven-flex maximizers all disappear. The natural extremal locus is resolved into three free embedded classes, with representatives suitable for future comparison, not just an example or a coefficient slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
