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
# Reproducibility and limits

Run `python3 verify.py` using standard Python 3; no third-party dependencies. The verifier builds the quadratic presentation directly, computes row bases of the exact quadratic-relation space over characteristic two, and compares literal squares of all degree-one vectors to the proposed graph/partition criterion for \((n,q)=(2,2),(3,2),(3,4),(4,2),(4,4),(5,2),(6,2)\). Independent set-partition exhaustive subspace-inclusion checks cover \(2\le n\le6\). The successful output ends `VERIFY_OK_FK_CHARACTERISTIC_TWO`.

These are finite parameter checks and **not** proofs for larger dimensions or all characteristic-two fields. The proof in `RESULT.md` uses independent degree-two relation classes and all-triple closure; it is uniform. The underlying zero locus is treated in the **reduced** sense, and no claim about a nonreduced quadratic equation scheme is made. The literature comparison is selective; independent mathematical audit and absolute priority validation have not been performed.
