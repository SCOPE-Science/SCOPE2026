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

# Computational and algebraic verification

The standalone `BCH_weight3_verify.py` enumerates norm-one subgroup elements in finite extensions, counts each distinct zero-sum triple exactly once, and checks both the closed multiplicity and regular coordinate incidence. It independently enumerates reducible members of the cubic family using finite-field arithmetic and verifies the order-three map. It runs using only Python 3 and is deterministic.

Reproduce using `python3 BCH_weight3_verify.py`; the complete expected output is embedded in `BCH_weight3_verify_output.txt`. Cases checked include \(s=1,2,3,4,5\), with the largest \(q=32\), \(n=1057\). Each checked case passes exact integer equalities; no numerical tolerances are involved.

The mathematical proof, rather than finite enumeration, covers every integer \(s\ge2\). It directly handles the primitive cube-root exception when \(s\) is even and shows the map's orbit fibers have exactly three elements away from the two fixed points. These computations and documents do not constitute independent mathematical validation.
