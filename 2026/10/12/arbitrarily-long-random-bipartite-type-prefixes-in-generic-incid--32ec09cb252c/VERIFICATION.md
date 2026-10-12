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

The bundled `verify.py` uses only Python's standard library and exact integer arithmetic.

It performs three independent finite checks. First, it evaluates the closed injective formula and its Stirling transform through arity seven. Second, it directly enumerates side colorings, cross-incidence subsets, and canonical equality partitions through arity five, without using those closed formulas for the enumeration. Third, for all \(2\le m,n\le6\) and every \(r<\min(m,n)\), it checks every enumerated injective incidence signature and confirms that no \(K_{m,n}\) can occur.

Recorded output:

`a_0..7 = [1, 2, 6, 26, 162, 1442, 18306, 330626]`

`b_0..7 = [1, 2, 8, 46, 362, 3804, 52994, 981838]`

`exact assertions = 2523`

`VERIFY_OK`

The finite replay supports the enumeration and threshold bookkeeping. The universal theorem is proved structurally from the published algebraic-closure and type-classification results.
