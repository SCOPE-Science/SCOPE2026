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

# Reproducibility and limitations

Run `python verify.py` with the Python standard library. The checker uses exact `Fraction` arithmetic and all \(2^m\) path words for the named tests, independently evaluates the site-departure moments and the proposed leading coefficient, and asserts equality. It has no stochastic seeds or numerical tolerances.

Checks: at \(r=1\), the selected three-atom law has \(a_1=\cdots=a_4=0\) and \(a_5=153/10^6\); at \(r=2\), the selected four-atom law has \(a_1=\cdots=a_8=0\) and \(a_9=554742/30517578125\); a symmetric two-atom example has \(a_7=0\). The exact script was executed successfully.

The general, all-integer moment order and speed asymptotic are established by the symbolic path argument in RESULT.md, not by finite enumeration. No independent audit or independent validation has been performed.
