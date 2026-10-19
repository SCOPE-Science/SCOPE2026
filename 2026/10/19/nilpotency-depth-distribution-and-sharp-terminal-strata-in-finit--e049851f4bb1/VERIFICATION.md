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

# Reproducibility of the finite-field nilpotency census

Run `python3 verify_nilpotency.py` with an ordinary Python 3 interpreter. The script requires no third-party modules. It constructs the multiplication on each rectangular Munn algebra coordinatewise, using arithmetic in prime fields and the explicit quotient \(\mathbb F_2[t]/(t^2+t+1)\) for \(\mathbb F_4\). It independently evaluates the Jordan-partition formula, using exact Gaussian coefficients and centralizer orders. Exhaustive literal-product enumeration gives exact depth bins. All cumulative values and terminal-index multiplicities must match.

The actual execution checked 18 parameter quadruples, including the full \(3\)-by-\(3\) rank-two sandwich algebra over \(\mathbb F_3\), with depth histogram \((1,314,1008,864)\), and an \(\mathbb F_4\) rank-one case with histogram \((1,27,36)\). The execution concluded with the exact marker `VERIFY_OK_MUNN_NILPOTENCY_DEPTHS` and no assertion failures.

**Boundaries:** Exhaustive finite experiments are not a proof for arbitrary rank, rectangular dimensions or finite-field size. Those cases are covered by the proof in `RESULT.md`. The checker tests ordinary nilpotency of algebra elements and does not assert reducedness of the scheme cut out by a single power equation. No independent audit has been performed.
