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

# Reproducible checks and limits

Run `python3 verify.py` alongside the other files. The script uses a direct matrix-unit computation of the adjoint operator rather than assuming the displayed polynomial description in its operator-level stage.

The exhaustive seven-coordinate algebraic-locus enumeration (with the remaining three coordinates free) gave finite-field counts \(288\) over \(\mathbb F_2\), \(2025\) over \(\mathbb F_3\), \(44032\) over \(\mathbb F_4\), and \(45625\) over \(\mathbb F_5\). All those seven-coordinate assignments agreed with the predicted component membership and characteristic-specific polynomial equations.

The independent operator-square check covered all \(1024\) binary ten-coordinate matrices, plus \(2048\) deterministic ten-coordinate matrices for each of \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). No counterexamples occurred. These finite checks corroborate rather than logically prove statements for all fields. The general proof is the full case analysis and irreducibility proof in RESULT.md. The scheme-theoretic radicality of the original quadratic equations is not asserted, and an independent mathematical audit has not been performed.
