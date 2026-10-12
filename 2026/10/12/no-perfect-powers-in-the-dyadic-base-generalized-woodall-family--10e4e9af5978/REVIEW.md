# Review

## Correctness
PASS. The proof exhausts even and odd exponents. Even exponents contradict the residue \(7\pmod8\) once \(an\ge3\), and the three remaining \((a,n)\) pairs are checked exactly. For odd \(k\ge3\), the odd cofactor
\[
T=(y^k+1)/(y+1)
\]
must divide \(n\), so \(T\le n\); the bound \(T>3y^{k-1}/4\) then gives \(y^k<(4n/3)^{3/2}\), whereas \(n2^{an}-1>(4n/3)^{3/2}\) for \(n\ge3\). The cases \(n=1,2\) are already impossible from \(T\mid n\) and \(T>1\).

## Originality
PASS. The closest complete archival Woodall paper inspected studies pseudoprimality and contains no perfect-power statement. The Woodall primality-testing literature concerns primality certification, not perfect-power values. Generalized Woodall search material defines \(nb^n-1\) but does not supply the dyadic-base theorem. Formula-level and alias searches for perfect powers, squares, cubes, and generalized Woodall values found no equivalent statement.

The closest prior result in the same local collection concerns perfect powers in the companion Cullen sequence; it does not imply this theorem because the sign is reversed, Cullen has actual square values, and the present theorem is uniform in a second dyadic-base parameter.

Residual risk remains because the argument is short and could have appeared in unindexed recreational literature.

## Value
PASS. Perfect-power structure is a natural arithmetic invariant of a classical generalized prime-search family. The theorem closes an infinite two-parameter subfamily at once and identifies why dyadic bases are structurally special: the odd cofactor of \(y^k+1\) cannot hide in the base. This is stronger than a one-base or bounded computation.

Self-review: passed. Independent audit: not yet performed.
