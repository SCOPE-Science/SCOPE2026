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

# Reproduction and limits

The companion `verify.py` is an executable, self-contained exact enumerator. It requires Python 3.10+ and SymPy 1.12+ and no external research data. Run `python verify.py`. It checks all \(9841\) projective coefficient vectors, \(3504\) rationally nonsingular sections, \(56\) factor-preserving orbits of these, and the four affine Jacobian ideals for one representative of each. The seven geometrically smooth orbits have lengths \(18,18,24,24,36,72,72\); factor exchange yields four orbits of lengths \(36,36,48,144\). Exact Cartier and iterated Frobenius ranks show \(48\) ordinary and \(216\) one-step-nonordinary sections. For seven representatives and four extension degrees each, independent point-counting agrees with the standard Hasse–Witt trace congruence.

Geometric smoothness is established via unit Gröbner ideals on all affine charts, not by scanning finite-field points. The Cartier formula and rank-to-invariants identification are standard mathematical inputs; no finite set of point counts proves them. Arithmetic over finite extensions is a consistency check. Dependence on the stated SymPy version, full projective coefficient normalization, and exact characteristic-three semantics are the main reproducibility limits. Bibliographic originality remains subject to unindexed publications. No independent audit or external validation is claimed.
