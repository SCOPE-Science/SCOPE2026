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
# Verification and limits
The attached Python 3 checker uses SymPy for exact polynomial identities and its own elementary finite-field arithmetic for rational-point enumeration. Run from this directory with `python verify.py` after installing SymPy.

Checked algebraic identities: the four-factor degree-two pullback identity with \(h=m/2\) in odd characteristic; the two-factor identity using \(\omega^2+\omega+1=0\); arithmetic-genus consistency of the \(\lambda=0\), \(\lambda=-1/4\) and \(\lambda=-1/3\) stratifications for multiple parameter values.

All finite \(\lambda\in\mathbb F_q\) and projective \(\mathbb F_q\)-rational points were enumerated over \(q=3,4,5,7,8,11,13,16\). The exact singular-count pattern agrees with the classification, including characteristic two and three. The checker does not enumerate all geometric extension points or prove generic smoothness. The proof in `RESULT.md` is algebraic and covers all allowed \(q\), \(k\), and parameters.

No independent mathematical audit has been performed. No claims about the complete content of inaccessible later journal revisions are made.
