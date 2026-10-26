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

# Reproducibility and boundaries

Execute `python3 verify.py` from this directory. It uses only the Python 3 standard library and prints `VERIFY_OK` if all assertions pass. It directly generates **all** partitions of the labeled underlying set of the rectangular band \(R_{2,m}\) for \(1\le m\le5\). Through \(m=4\), it checks Schur closure by direct multiplication of every pair of primitive block sums, and independently checks the derived row/column-profile test. At \(m=5\), it uses the profile test to avoid repeated coefficient multiplication. In every case it compares the separate balanced and separated counts to the Bell-weight formulas and constructs explicit automorphism-subgroup generators whose orbits must be exactly the partition blocks.

Expected outputs are the lines `m=1 ... =2`, `m=2 ... =5`, `m=3 ... =13`, `m=4 ... =48`, `m=5 ... =184`, followed by `VERIFY_OK`. No external input, network request, symbolic-algebra package, or precomputed certificate is needed.

Finite enumeration independently tests many consequences of the theorem but does not prove statements for all \(m\). The infinite proof is the profile-criterion and normal-form argument in RESULT.md. The database and literature comparison is limited to retrieved, identified records and their explicitly inspected material; a negative search cannot certify novelty over all mathematical literature.
