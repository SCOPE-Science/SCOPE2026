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

The proof uses exact geometric sums and the four-dimensional Hermitian Pauli basis. Its nonstandard but elementary step is that the group reflection pairs eliminate cross-terms, and the remaining order-two case requires separate treatment because the second geometric sum no longer vanishes.

Run `python3 verify.py` in a directory containing the checker. In the checked environment the output was `VERIFY_OK spectra=588 optimal_orbits=196 n_range=3..29`. The checker builds the orbit projectors independently, applies symmetric Jacobi diagonalization, and compares against the displayed spectrum within a documented floating-point tolerance. Its scope is finite and does not replace the exact proof for all \(n\).

The focal article's first publicly available version is dated 2017-04-28, distinct from the later journal date. Full-text inspection of the focal article and the general projective-design antecedent is described in the accompanying literature comparison. A plausible subsequent article on phase retrievability of arbitrary finite-group irreducibles was not successfully accessed in full text; no inference about its detailed contents is made. Independent mathematical validation has not been performed.
