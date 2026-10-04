# Review

## Correctness

PASS. For an \(r\)-dimensional message subspace \(U\), exactly \(q^{m-r}-1\) nonzero simplex columns lie in \(U^\perp\), so every subcode has fixed simplex-block support
\[
q^m-q^{m-r}.
\]
The identity block contributes precisely the coordinate-support size \(s(U)\). Since \(s(U)\ge r\), with equality for coordinate \(r\)-spaces, the generalized weight is
\[
d_r=q^m-q^{m-r}+r.
\]
Inclusion-exclusion over coordinate hyperplanes gives the stated exact support multiplicities. Direct exhaustive subspace enumeration matches the formulas in four independent small instances.

## Originality

PASS. The primary article gives ordinary weight distributions and LCD optimality but no generalized Hamming weights. Classical simplex-code literature covers the base simplex block; it does not cover the identity-augmented LCD families or their coordinate-support correction. Exact and alias searches for the binary and ternary formulas and the complete support spectrum found no prior same-family statement.

## Value

PASS. These are newly published infinite LCD-optimal families, and the source already treats ordinary weight distributions as central structural data. The generalized Hamming hierarchy is the standard higher-dimensional refinement relevant to information leakage and secret-sharing behavior. The result supplies not only every generalized weight but the complete number of subcodes at each support size.

Same-model review: passed. Independent audit: not yet performed.
