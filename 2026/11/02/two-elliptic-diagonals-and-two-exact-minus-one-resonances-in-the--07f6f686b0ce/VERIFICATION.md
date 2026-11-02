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

# Verification record

The standalone program `verify.py` was run with Python 3 and SymPy. It passed the exact geometry, curvature, positivity, return-matrix, polynomial, rational-root-bracket and parameter-range identities, plus 1,003 finite rational tests (999 interior \(u\) samples and four axial parameter cases).

Analytical boundaries: The factorization of \(2-K\), the positive curvature polynomial and the one-turning-point cubic derivative prove the global interval and exact exceptional root count; those facts are not inferred from sampling. The minus-one matrix identity is a Cayley–Hamilton equality, not merely a numerical double eigenvalue. The source already establishes the orbit-existence interval and the two axial traces, which are distinguished from the new diagonal calculation.

Limits: The result gives linear spectral type only. No nonlinear stability claim, KAM-island existence, higher-period classification, or proof of historical uniqueness is certified by these checks. Independent audit was not performed.
