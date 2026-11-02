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

# Reproducibility and scope

Run `python3 verify_squarefree_variance.py` from the extracted package. The pure-Python implementation uses exact finite-field operations and direct polynomial greatest common divisors, rather than reproducing the Fourier proof. All 17 listed field/degree cases returned a matching rational variance, and all six ternary fibres were checked against the explicit tables. The extension-field test uses the irreducible polynomial \(X^2+1\) over \(\mathbb F_3\) to construct \(\mathbb F_9\).

These are finite checks only. They cannot prove the claimed identities for every odd prime power or arbitrarily large degree, which follow from the character and Gauss-sum proof in `RESULT.md`. No independent mathematical or priority audit has been performed.
