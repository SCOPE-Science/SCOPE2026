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

# Reproduction and proof limits

Run `python verify.py` using NumPy and SciPy to repeat the directly constructed normalized evaluation/derivative determinant comparisons, root-of-unity Fourier-block singular-spectrum checks, nonuniform-angular determinant checks, and numerical radial optimization. It reports 45 passing tests, with maximum direct-algebra discrepancy below \(2.2\times10^{-14}\), and evaluates \(4^n\mathcal D_H/\mathcal D_V\) for finite values of \(n\) up to 160. Representative computed values are \(2.762824908\) at \(n=2\), \(2.731849736\) at \(n=10\), \(2.721115559\) at \(n=80\), and \(2.719698057\) at \(n=160\), consistent with the proved limit \(e\).

The proof of universal angular optimality uses Hadamard equality and Newton identities, and the proof of radial optimality uses strict exponential-family mean monotonicity. The exponential limit is established analytically by Poisson-tail and second-order log-determinant estimates; numerical tests do **not** establish any infinite limit. All quantities use the finite Fock-space normalization, not the untruncated kernel normalization. Independent audit is not performed.
