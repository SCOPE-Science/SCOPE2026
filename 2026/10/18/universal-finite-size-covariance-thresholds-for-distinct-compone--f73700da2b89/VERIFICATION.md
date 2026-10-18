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

Run `python verify.py` with Python 3 and no dependencies outside the standard library. The observed output ends `VERIFY_OK 6982`; the script enumerates exact finite graph probability spaces and checks all ordered unequal component-size pairs for unrestricted, tree, and complete-graph component types, including cross-type pairs. Separate rational-factor checks cover the critical inequality and product identity through \(n=29\).

These computations test finitely many graphs and values of \(p\); they do not certify arbitrary size or probability. The proof for every \(n\ge3\) and \(0<p<1\) is the disjoint-subset mixed-moment identity, factorial cancellation and strict product argument in `RESULT.md`. The source comparison is based on the specified inspected sections and leaves open historical priority from inaccessible full text.
