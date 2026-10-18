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

The complete calculation can be replayed from `verify.py` using Python with SymPy and NetworkX. It constructs the sixteen four-spin states, applies the strict five-spin flip-energy criterion, recomputes all six characteristic polynomials symbolically, confirms maximal strongly connected recurrent component sizes and self-loop aperiodicity, and verifies the transfer trace by separately recomputing the Hamiltonian under every single-spin flip for all \(5\le N\le11\) at six representative rational coupling ratios.

The tests passed: 42 finite-state spin-configuration count comparisons, six independent symbolic characteristic-polynomial identities, and six recurrent-component checks. They are finite cross-checks, not the argument for all volumes: the exact transfer correspondence and primitive Perron–Frobenius argument in RESULT.md establish the infinite-size theorem. No independent audit has been performed.
