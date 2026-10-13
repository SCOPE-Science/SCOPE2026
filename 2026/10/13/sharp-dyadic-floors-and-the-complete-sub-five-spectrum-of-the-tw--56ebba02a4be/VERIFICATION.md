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

The infinite proof is symbolic. It depends on two published exact identities for the two-block odd partition function and on elementary divisor inequalities proved in `RESULT.md`.

The bundled `artifacts/verify.py` performs three finite consistency checks:

1. It evaluates the defining signed partition sum directly and compares it with the divisor-sum formula for every \(1\le n\le120\).
2. It computes the divisor-sum formula for every \(1\le n\le20000\) and verifies that the fibers \(a(n)=0,1,2,3,4\) are exactly the sets stated in the theorem.
3. It tests the sharp dyadic bounds for \(2\le k\le12\) and every odd \(3\le m<1000\), including the equality case \(m=3\).

These finite checks test normalization and arithmetic implementation only. They do not certify the universal quantifiers; those are established by the proof.
