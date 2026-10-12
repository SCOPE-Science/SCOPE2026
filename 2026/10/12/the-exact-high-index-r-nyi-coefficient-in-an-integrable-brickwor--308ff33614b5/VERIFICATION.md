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

# Reproducibility and proof limits

The package includes `verify.py` and `requirements.txt`. Run `python -m pip install -r requirements.txt` and then `python verify.py`. The program independently propagates basis configurations through the circuit, constructs output coefficient matrices for both the operator and domain-wall states at times 1, 2, 3, and 4, and checks the count-projector block singular values, including their precise ranks and flat weights. It tests both Schatten inequalities used by the proof for four real Rényi indices. The expected successful terminator is `VERIFY_OK 94 flat count-sector spectra; diagonal pinching and Minkowski moments`.

Analytic proof responsibilities: (i) use the source's all-time flat block-spectrum lemma; (ii) prove the fixed-difference direct-sum identity; (iii) establish the \(O(t^{-1/2})\) central binomial bounds; (iv) prove summability of the exponential rank-penalty kernel for each fixed \(\alpha>1\); (v) apply Schatten triangle and diagonal count-phase pinching; (vi) use a \(\Theta(\sqrt t)\)-width lower binomial window. These are all included in RESULT.md. The numerical routine tests the finite-time premises, not infinitely many times or originality.

The upstream preliminary PDF of September 4 was not accessible for direct content comparison; the later full arXiv text, including relevant supplementary sections, was inspected. No independent audit or independent validation is claimed.
