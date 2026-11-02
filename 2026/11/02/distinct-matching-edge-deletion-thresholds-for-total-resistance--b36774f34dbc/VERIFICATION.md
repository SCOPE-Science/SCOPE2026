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

# Reproducible verification

`python3 verify.py` (Python 3 standard library, no network and no dependencies) prints `VERIFICATION_OK 1131 checks` when successful.

The checker performs exact rational Gauss–Jordan inverses of \(L+J/(2m)\) and Kirchhoff cofactor determinants for \(2\le m\le6\), comparing both against the pair-symmetric and pair-antisymmetric spectral formulas at rational weights including deleted matching weights. It checks algebraic threshold-gap and derivative identities exactly, performs finite one-dimensional objective comparisons and asymptotic tests, and checks strict inequalities on randomly generated unequal positive weight vectors. All tests are executable from the file included beside this document.

The general proof is independent of enumeration: every integer \(m\ge2\) is covered by strict matrix convexity, graph automorphisms, the exact two-eigenspace decomposition and elementary derivative signs. The finite computations do not establish originality, do not establish an infinite result by enumeration and do not constitute independent validation.
