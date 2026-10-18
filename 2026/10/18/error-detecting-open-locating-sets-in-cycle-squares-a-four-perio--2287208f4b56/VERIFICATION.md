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

# Reproduction and verification

The self-contained Python 3 `verify.py` uses only standard-library packages; execute `python verify.py` from the directory holding the extracted files. A successful run ends with `VERIFY_OK` and may be checked against `verification_output.txt`.

The program directly tests the DET:OLD neighborhood criterion over all binary subsets for each \(3\le n\le16\). It separately checks the complement-independence equivalence for every binary subset in the range \(12\le n\le16\). A distinct state-transition counting procedure constructs the \(128\)-state polynomial transfer, checks all orders \(12\le n\le40\), confirms optimal values and minimum multiplicities, and compares full aggregate counts against exhaustive independence enumeration through order sixteen.

The finite checker cannot establish a theorem for arbitrarily large \(n\). The written proof supplies the infinite equivalence, transfer bijection, sharp gap bound, constructions and equality case analysis. No independent external audit or publication priority adjudication is claimed.
