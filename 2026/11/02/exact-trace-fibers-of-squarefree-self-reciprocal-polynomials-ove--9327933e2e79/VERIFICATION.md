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

Execute `python3 verify.py` using Python 3's standard library only. The verifier checks prescribed-coefficient counts by enumerating all monic degree-\(n\) polynomials \(g\) and testing squarefreeness with formal derivatives and polynomial Euclidean gcd. It independently transforms every such \(g\) to its degree-\(2n\) reciprocal polynomial for \(n\le3\) and compares squarefreeness directly, including ramification at \(\pm2\).

A successful run printed:

`VERIFY_OK cases=25 fibers=215 polynomials=32915 direct_transform_checks=19150`

The fields tested were the prime fields of orders 3, 5, 7, and 11 and the quadratic extension fields of orders 9 and 25. All permitted coefficient values were checked in 25 field-degree cases. The check does not establish the universal theorem; the proof uses character orthogonality and unique factorization for arbitrary odd prime powers and degrees. The predicted formula and the independent direct polynomial computations agree on the entire enumerated domain.

Independent audit status: not performed.
