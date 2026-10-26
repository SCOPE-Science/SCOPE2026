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
# Verification and scope

Run `python verify.py` with a standard Python 3 interpreter. Expected success begins `VERIFY_OK cases=77 nonprimitive_solutions=616 exact_integer_conditions=PASS`.

The checker constructs all \(77\) explicit pairs with \(3\le a\le13\) and even \(2\le L\le14\), verifies least-residue-class selection using exact rational inequalities, enumerates all ordinary nonnegative representations at the witness value, and confirms that no coefficient pair is coprime. All calculations use arbitrary-precision integers and exact fractions.

**Logical limit:** Checking these finite instances does not prove the theorem for every \(a\) and every even \(L\). The general obstruction follows from congruence, divisibility, and the explicit progression bound in `RESULT.md`; no external certification or independent audit is claimed.
