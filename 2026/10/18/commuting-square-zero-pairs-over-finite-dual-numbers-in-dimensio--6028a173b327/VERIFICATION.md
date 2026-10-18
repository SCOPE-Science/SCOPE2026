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

# Reproducibility and verification limits

The included standalone `verify.py` uses the Python standard library and requires no external files. From the same directory, run `python3 verify.py`. Exact modular arithmetic and Gaussian elimination are used; no randomized tests or numerical tolerances are involved.

For the residue fields \(\mathbb F_2\) and \(\mathbb F_3\), the script enumerates every \(3\times3\) square-zero matrix, every ordered commuting pair of these matrices, and the rank of the actual \(27\)-equation \(18\)-unknown first-order lift system at every pair. For \(q=3\), it obtains \(105\) residue square-zero matrices, reduction-stratum populations \((1,208,208,1248)\), nullities \((18,10,9,8)\), and total lift count \(411984873\). For \(q=2\), a boundary check obtains \(22\) square-zero reductions and populations \((1,42,21,84)\) with nullities \((18,10,10,8)\). This latter characteristic-two case is not part of the accepted theorem. It checks the representative linear-system ranks over the additional odd prime fields \(\mathbb F_5\) and \(\mathbb F_7\), and outputs `VERIFY_OK`.

The arbitrary-odd-prime-power formula follows from the separately written proof in RESULT.md, not by extrapolation from these finitely many tests. No computational assertion of independent auditing, proof assistance, scheme reducedness or absolute literature uniqueness is made.
