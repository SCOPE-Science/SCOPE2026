---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the cyclic perfect two-dimensional evolution algebra e1^2=e2, e2^2=e1, e1e2=0 over any field, expanding weight-lambda Rota-Baxter identity gives exactly six polynomial equations in a,b,c,d (column convention). These imply (a+d+lambda)b=(a+d+lambda)c=0 and b,c either both zero or both nonzero. Diagonal nonzero solutions give t=a/d with (t-1)(t^2-t+1)=0; t=1 yields -lambda I and the other roots require (t+1)d=-lambda. Off-diagonal solutions satisfy trace a+d+lambda=0 and b=(a-d)u^2,c=-(a-d)u with u^3=1, and the same t relation. For nonzero weight the count is exactly 2 or 10 according to primitive cubic roots, including char2/char3. For zero weight only char3 permits nonzero solutions, on two distinct k-linear lines with intersection {0}; over finite fields char3 count 2q-1. This covers all field characteristics, not just finite enumerations. Independent direct enumeration of four matrix entries over F2,F3,F5,F7 for weights 0,1 gave counts (1,2),(5,2),(1,2),(1,10), matching classification. Symbolic proof supplies unrestricted quantifiers.

## originality

PASS

Ladra–Murodov 2019 classify the complex-field two-dimensional cyclic evolution algebra case in Section 3/Theorem 3.3. The complex specialization is covered and explicitly not novel. Their complex calculations cannot imply the two 1-dimensional zero-weight branches in characteristic three; the all-field cyclotomic descent and finite-field counts are the assessed original remainder. Later 2026 nilpotent maximal-nilindex work treats a different non-perfect algebra family. Unindexed positive-characteristic literature remains possible.

## value

PASS

A complete all-field classification of operators for a canonical minimal perfect evolution algebra is a natural exact arithmetic-algebra invariant; the characteristic-three appearance of infinitely many weight-zero operators and the finite-field 2-versus-10 jump exhibit genuine field-characteristic changes not visible over C.

The dated certificate retains the supplied scientific assessment, sources and limitations.
