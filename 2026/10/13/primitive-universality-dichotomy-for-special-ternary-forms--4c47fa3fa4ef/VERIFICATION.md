---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
Run `python3 verify.py`.

The checker implements the explicit constructions for the representative special parameters
\[
1,2,5,10,13,17,25,26,34,50
\]
and all integers
\[
-200\le m\le200.
\]
For every case predicted to be primitively representable, it searches the appropriate Bezout family and verifies a nonzero triple satisfying
\[
a^2+b^2-dc^2=m,
\qquad
\gcd(a,b,c)=1.
\]
For every even parameter and every tested integer congruent to \(4\pmod8\), it also exhaustively checks all nonzero triples in a bounded coordinate box and finds no primitive representation.

The finite replay is a regression check only. The infinite theorem is certified by the symbolic identities, common-divisor arguments, parameter-unboundedness argument, and complete modulo-\(8\) obstruction in `RESULT.md`.
