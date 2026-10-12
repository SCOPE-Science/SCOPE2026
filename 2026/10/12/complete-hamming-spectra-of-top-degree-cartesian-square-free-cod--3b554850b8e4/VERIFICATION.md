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

# Computation and proof verification

Run `python3 verify.py` in the directory containing the embedded source. The script reconstructs generator evaluations directly over each finite field and exhaustively runs through all coefficient vectors. It builds fields of cardinality \(4\) and \(8\) with polynomial-basis multiplication, not integer modular multiplication. For \(q\in\{2,3,4,5,7,8\}\), across 19 field/dimension pairs with \(2\le m\le6\), it checks the entire weight distribution, support-size uniformity, equality \(w_1=w_2\), strict later separation for \(q>2\), and coefficient-vector total \(q^m\). Successful execution ends with the exact marker `VERIFY_OK`.

The proof does not depend on the 19 tests: it uses field-additive-character orthogonality to count zero sums of nonzero terms and a disjoint coordinate-stratum decomposition. The tests do not exhaust infinitely many fields or dimensions. They independently catch index errors, missing zero coordinates, arithmetic normalization errors and unsupported prime-only assumptions.
