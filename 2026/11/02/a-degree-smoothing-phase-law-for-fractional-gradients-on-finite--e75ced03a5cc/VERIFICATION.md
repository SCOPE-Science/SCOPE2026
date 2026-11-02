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

The proof in RESULT.md applies to every integer \(m\ge2\), every real \(s>0\), and the stated fixed \(p\)-ranges. Numerical tests are corroboration only. Run `python proof_checks.py` after installing `requirements.txt`: the code reconstructs the operator from an independently formed Laplacian eigendecomposition, checks exact \(\ell^1\), \(\ell^2\), and \(\ell^\infty\) norms, tests critical non-Hilbert witnesses, and checks finite-grid approximations. Finite tests do not establish the limiting quantifiers; the analytical argument is in RESULT.md.

No independent mathematical audit has been performed. The older network-pseudoinverse source named in RESULT.md was not available in full for a complete statement-by-statement originality comparison.
