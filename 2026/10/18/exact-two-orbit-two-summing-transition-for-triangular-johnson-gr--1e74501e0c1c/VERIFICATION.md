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

# Reproducibility and checked limits

The analytical proof in `RESULT.md` establishes all infinite families. The following independent finite computations were run using the actual standalone scripts embedded here:

```
python verify_symbolic.py
python verify_johnson.py
```

The first command printed `PASS integer characteristic spectral comparisons 5`: exact integer matrices have the predicted spectral multiplicities for \(v=4,5,6,7,8\). The second printed `OK exact-formula vs actual weighted graph eigenspectra 89`, `OK full noninvariant design optimizations 15`, and `PASS`. The 89 configurations cover \(v=4,\ldots,12\), with amplitudes on both sides of the analytically derived support boundaries. The 15 unrestricted simplex optimizations cover \(v=4,5,6\), including the no-growth, mixed, and complementary regimes (where they exist), from randomized nonsymmetric starting weights. The code uses NumPy, SciPy, and SymPy, without external data.

Finite numerical comparisons are not proof of the formula for all dimensions or real amplitudes, and a numerical optimizer's success does not establish uniqueness. The full proof uses the free-lattice representation, finite-dimensional semidefinite duality, strict spectral concavity, exact Johnson/Kneser eigenvalue identities, and scalar endpoint inequalities. Symbolic checks verify the integer eigenspectrum but not bibliographic novelty. Independent scientific validation is not represented by these tests.
