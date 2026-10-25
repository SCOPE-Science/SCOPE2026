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

# Reproducible verification and limits

The standalone file `verify.py` uses only Python's standard `fractions` module. Execute `python verify.py 8 8`; the expected final line is `PASS: 49 parameter pairs, 1470 exact tree-edge dual-norm identities, plus dual witnesses and phase thresholds`. Every coefficient and reported norm is represented as an exact rational number; the script computes the total absolute descendant masses on the actual leaf-to-root tree edges for the proposed extension. It additionally checks the explicit Lipschitz witness, the strict positivity of the symmetric mixture parameter, the closed formula and the \(\Lambda_{m,k}>2\) phase equivalence. The sample values are \(\Lambda_{2,2}=10/7\), \(\Lambda_{2,3}=8/5\), \(\Lambda_{3,2}=12/7\), \(\Lambda_{3,3}=28/15\), \(\Lambda_{4,3}=2\).

The infinite-family proof is the analytical group-averaging, signed tree-transport, affine minimax and attainment argument in `RESULT.md`. The script deliberately does not purport to test all parameter values, quantify bibliographic uniqueness, or supply external validation. Independent mathematical audit has not yet been performed.
