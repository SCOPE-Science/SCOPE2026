# Self-review

## Correctness
PASS. The classical Pluecker values are
\[
D=d(d-1),\qquad F=3d(d-2),\qquad B=\frac12d(d-2)(d-3)(d+3).
\]
After division by \(d\), the three pairwise gcds reduce to exact elementary computations. The dual-degree/flex pair leaves an extra factor \(3\) exactly for \(d\equiv1\pmod3\); the dual-degree/bitangent pair is controlled purely by the residue of an odd degree modulo \(4\); and the flex/bitangent pair factors through \(d-2\) with one additional factor \(3\) exactly when \(3\mid d\). The only possible extra factor in the first pair never divides the normalized bitangent count, so the normalized triple is primitive.

The embedded checker verifies all formulas through degree ten thousand. Those finite computations are regression evidence only.

## Originality
PASS. The closest inspected sources provide the classical Pluecker formulas, their conormal interpretation, and broader Newton-polygon generalizations. They do not state the triple common divisor or the complete pairwise gcd spectrum. Targeted searches using gcd, common-divisor, primitive-triple, divisibility, dual-degree, bitangent, and inflection formulations found no equivalent statement.

Residual risk: because the arithmetic proof is short once the classical formulas are known, an unindexed historical source could contain the same observation.

## Value
PASS. The three integers are the canonical dual-line enumerative invariants of a general smooth plane curve. The result gives a complete arithmetic interaction law for this classical package, showing that the curve degree is the exact universal common factor and describing every additional pairwise overlap.

Self-review: passed. Independent audit: not yet performed.
