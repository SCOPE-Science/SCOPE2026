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

# Verification evidence

Run `python3 check_exponents.py` using the Python standard library. The program enumerates permutations of each degree \(d\in\{1,\ldots,6\}\), forms all \(r\)-th and \(s\)-th powers for every \(1\le r,s\le32\), and checks whether some two powers fail to commute. It compares this outcome with the exact divisibility criteria, independently of the subgroup normality/simplicity proof. The six completed lines and final success marker in `check_output.txt` were reproduced by executing the supplied code. Computation is finite and does not prove the all-degree formula; the essential group argument appears in `RESULT.md`.

No external audit or independent validation is reported.
