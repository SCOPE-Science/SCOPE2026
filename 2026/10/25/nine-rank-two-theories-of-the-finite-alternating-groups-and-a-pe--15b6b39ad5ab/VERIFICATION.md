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

Execute `python3 check_alt.py` with Python 3 standard library only. The expected final marker is `VERIFY_OK`, and the supplied output file `check_alt.log` records the replayed run.

The program computes symbolic categories from all even cycle partitions for \(3\le n\le40\), and actual pairwise atomic-diagram extension sets of the full alternating groups for \(3\le n\le9\). It independently constructs all squares in each concrete group, checks the proposed square-root criterion on every conjugacy-partition shape, and checks the special extra-square-root criterion for order-three elements. It also compares the concrete pair signatures against their abstract category labels across degrees.

A partition enumeration to forty is not an infinite proof. The infinite result requires and is supplied by the group-theoretic permutation cycle-pairing lemma and the atomic-extension argument in `RESULT.md`. Explicit finite verification does not provide an independent mathematical audit or external certification.
