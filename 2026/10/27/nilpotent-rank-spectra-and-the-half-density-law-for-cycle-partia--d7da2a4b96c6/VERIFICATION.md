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
# Reproducibility checks

Run `python3 verify.py` with Python 3.8 or later (standard library only). The program constructs each of the \(2n\) dihedral permutations at sizes \(3\le n\le10\), enumerates every restriction, deduplicates partial maps, independently walks partial orbits to detect directed cycles, and checks the rank polynomial coefficient by coefficient. It also verifies the overall cardinality formula and the highest nilpotent rank count \(n\varphi(n)\).

The checked nilpotent totals for \(n=3,4,5,6,7,8,9,10\) are respectively \(13,41,141,307,897,1889,4393,9651\). The exact expected final line is `VERIFY_OK cycle partial-isometry nilpotent rank polynomial`.

These computations are exhaustive only for the stated finite range. The proof in `RESULT.md` supplies unrestricted parameter reasoning. Independent mathematical audit: not performed.
