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

# Reproduction of exact arithmetic checks

Run `python verify.py` in the same folder. The program uses only the Python standard library. For every \(1\le r\le12\), it calculates the pushforward CSM classes of the two apolar projective bundles using Chern classes and the projective bundle pushforward, subtracts from \(c(T\mathbb P^{2r})\), and checks the binomial-product prediction coefficient by coefficient. It additionally checks the top and bottom coefficients and the Euler characteristic of the secant variety. The observed terminal marker is `VERIFY_OK`.

The inputs are exact binomial coefficients and integer alternating sums, with no floating-point arithmetic. The finite verification is not an infinite-rank proof. The general proof is in RESULT.md, especially the secant-fiber argument, adjunction calculation, formal diagonal residue, and constant-term evaluation. The geometry assumes the standard binary-apolarity theorem and MacPherson proper functoriality in characteristic zero, cited there. Independent audit and independent validation have not been performed.
