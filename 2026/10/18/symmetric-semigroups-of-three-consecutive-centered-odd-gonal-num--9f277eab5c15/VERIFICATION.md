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

The reproducibility artifact `verify.py` is standalone Python 3 code. Running `python3 verify.py` performs 198602 exact gcd/gluing checks with independently calculated pairwise gcds, followed by 624 separately implemented shortest-path computations of Apéry sets modulo the smallest generator. From each Apéry set it computes both the Frobenius number and genus, tests the symmetry equivalence, and compares the proposed Frobenius formulas on symmetric cases. The expected completion line begins `VERIFY_OK`.

These checks cover finite ranges only; they do not prove the infinite claim. The proof in `RESULT.md` uses exact congruences, sharp inequalities and the three-generator gluing characterization. No external mathematical audit was performed.
