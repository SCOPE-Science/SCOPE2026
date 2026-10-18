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

# Reproducibility and proof limits

Run `python verify.py` with Python 3.9 or newer; no third-party packages are required. Its exact rational row reduction verifies base hollow symmetric witnesses of rank \(n-2\), each having three independent infinitesimal normal restrictions to a two-dimensional kernel. It verifies the persistence of these properties after adjoining hyperbolic \(2\times2\) blocks in all sizes \(5\le n\le12\). The base witnesses and block-sum argument in `RESULT.md` show why these computations establish an infinite-family **existence statement**, rather than merely a finite experiment. The script also checks a five-dimensional full-support corank-one kernel and one zero-row corank-one witness for each dimension from five to twelve.

Expected terminal output is `VERIFY_OK`. The analytical proof of singular-support exhaustion applies the adjugate rank-one identity for all \(n\), independently of this program. Irreducibility is proved by a Gram-parametrization argument on irreducible isotropic cones, and generic local equations follow by explicit Schur complements. The finite script neither verifies every matrix nor independently certifies the full geometric theorem.

The bibliographic comparison includes full scientific statements for the most relevant published hollow quartic and squared-Grassmannian papers; a related 2026 work on maximum-likelihood Euler stratifications was available only in abstract and remains an access-related originality risk. No independent audit was performed.
