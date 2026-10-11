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

Run `python3 verify.py` with Python 3 and no additional packages. The checker uses exact fractions for Gaussian elimination of the Fourier-coefficient observation matrices, visits twenty abelian group presentations of orders four through eighteen, tests explicit null vectors for every even-order difference band, and reconstructs all rank-one Gram entries from deletion observations in twenty deterministic tests per odd-order presentation.

Expected terminal marker: `VERIFY_OK groups= 20`. The three order-eight ranks are asserted separately in the checker as \(44\), \(36\), and \(28\). The computation handles finitely many groups and does not establish the universal statement by exhaustion. Universal correctness rests on the stated Fourier-band decomposition and alternating-cycle proof. No experimental claim of complete bibliographic novelty or independent validation is made.
