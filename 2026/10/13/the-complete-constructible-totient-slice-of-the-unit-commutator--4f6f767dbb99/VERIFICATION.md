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

The proof in `RESULT.md` is unrestricted. The accompanying `verify.py` computes \(\varphi\) and \(\sigma\) independently from exact factorizations and performs three corroborative checks: a complete filter of \(2\le n\le300000\) satisfying \(\varphi(n)\) a power of \(2\); both dyadic rays \(2^a\) and \(3\cdot2^a\) for \(0\le a\le35\); and \(562\) distinct tested Fermat-support/power-of-two combinations with exact integer inputs not exceeding \(2^{41}\).

The expected eight hits in the finite \(300000\)-range and all ten large-ray hits are checked against direct evaluation of \(\varphi(\sigma(n))-\sigma(\varphi(n))\). The code also checks the primality of \(3,5,17,257,65537,641\) and the identity \(2^{32}+1=641\cdot6700417\).

These tests do not certify the infinitely many untested indices. The unrestricted classification comes from the Gauss–Wantzel factorization, Fermat-prime obstruction, exhaustive residual support cases, and Fermat-prefix lemma.
