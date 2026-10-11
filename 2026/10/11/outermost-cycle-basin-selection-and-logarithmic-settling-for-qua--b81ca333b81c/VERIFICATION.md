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

The mathematical proof in `RESULT.md` gives the complete infinite-domain argument. Its critical nonstandard steps are (a) \(g(n+1)-g(n)\in\{0,1\}\), (b) existence and contiguity of zeros of \(g(n)-n\), (c) no-overshoot endpoint capture, and (d) a uniform bounded additive error for all iterates of \(g\). Each step is proved from elementary floor inequalities with strict boundary conventions; no experiment is used to infer a universal result.

`CHECK.py` is standalone Python standard-library verification using rational arithmetic. Run `python CHECK.py` from the directory containing the extracted script. The script reports `CHECK_OK: 36 exact parameter cases and orbit/basin samples` and checks a representative exact example with nine fixed points of \(g\). These finite tests cannot prove the result for all real parameters, cannot establish the asymptotic for all initial integers, and do not certify independent originality.

Reproducibility requires only Python 3 with its standard library. Real-valued irrational parameters are handled in the symbolic mathematical proof rather than in the rational checker. Independent audit remains not performed.
