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

# Verification record

The proof is self-contained and covers every prime power \(q\ge2\) and \(n\ge1\). The separately packaged `verify_cyclic_borel.py` computes \(\deg m_A\) as the linear rank of the powers \(I,A,\ldots,A^{n-1}\), without using a conjugacy-orbit or centralizer formula. It enumerates every upper-triangular matrix and checks each diagonal word for eleven small field-dimension pairs over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), plus the identity between the Stirling and finite-power-sum formulas in additional field orders/dimensions. The executable script prints `VERIFY_OK_CYCLIC_BOREL` when its checks pass.

The final embedded script was extracted from the fully saved JSONL package and executed; its standard output ended in `VERIFY_OK_CYCLIC_BOREL`.

The prescribed-diagonal matrix count for \(q=2,n=4\) totals \(240\) across all words. The prescribed-diagonal count for \(q=3,n=4\) totals \(31752\). The tests substantiate arithmetic and normalizations, but finite enumeration is not an infinite proof, and the package has **not** received independent audit or external certification.
