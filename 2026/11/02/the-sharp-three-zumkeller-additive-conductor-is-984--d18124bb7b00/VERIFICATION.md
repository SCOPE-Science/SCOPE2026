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

Execute `python3 verify_three_zumkeller.py` with Python 3 and no external dependencies. Its checks reconstruct every displayed finite Zumkeller divisor partition, all \(18\) residue covering starts, the two intermediate odd exceptions, all \(19\) odd deficiencies from \(947\) to \(983\), and the failed two-summand decomposition of \(38\). It verifies constructive representations for each integer \(984\le n\le50000\) and independently reconstructs the exact Zumkeller predicate by divisor subset sums through \(1200\).

The modular covering and multiplicative partition arguments in the proof establish the infinite quantifier. The finite script is a reproducibility cross-check, not an infinite proof. The exact odd boundary uses the published least-odd-Zumkeller fact and independently checks every larger odd candidate at most \(983\). Independent validation has not been performed.
