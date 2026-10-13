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
# Verification

The proof in `RESULT.md` is unbounded. The attached computation is corroborative only.

`verify.py` constructs a smallest-prime-factor table through
\[
2{,}000{,}000.
\]
For every integer in that range with
\[
\Omega(n)=3,
\]
it computes
\[
\beta(n)=\sum_{p\mid n}p
\]
and tests the defining congruence
\[
2^n\equiv1\pmod{\beta(n)}
\]
using exact modular exponentiation.

The program asserts that the complete set of nonsquarefree hits in the range is
\[
\{12,52\},
\]
and independently asserts that the complete set of even hits in the layer is the same pair.

It also tests every prime
\[
q<100{,}000
\]
in the two nonsquarefree support-\(\{2,q\}\) branches \(4q\) and \(2q^2\), obtaining only \(4\cdot3=12\) and \(4\cdot13=52\).

These finite checks do not establish the universal theorem. The infinite conclusion rests on the complete factorization-shape, multiplicative-order, and valuation argument in `RESULT.md`.
