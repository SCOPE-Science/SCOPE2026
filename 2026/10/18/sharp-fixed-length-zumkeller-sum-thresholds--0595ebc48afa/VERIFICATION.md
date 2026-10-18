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

# Exact reproducibility

Run `python3 verify.py` with Python's standard library. The script reconstructs each Zumkeller integer through \(4000\) by exact divisor-sum and subset-sum tests; verifies the published two-sum premise in the finite region \(40\le N\le4000\) (even \(N\)), checks that \(38\) has no two-term representation, confirms each small witness and the unique necessary odd-abundant candidate through \(971\), and verifies the exact \(k\)-summand thresholds for every \(3\le k\le30\) below \(4000\). `verification_output.txt` is the actual successful run output.

These finite checks cannot establish claims for unbounded \(N\) or \(k\). The proof in `RESULT.md` instead uses the known, inspected even two-summand theorem and explicit local divisor bounds, five base witnesses, a uniform nonrepresentability argument, and induction. The cited source supplies the infinite two-summand premise; the original claim does not rest solely on computation. No independent validation is claimed.
