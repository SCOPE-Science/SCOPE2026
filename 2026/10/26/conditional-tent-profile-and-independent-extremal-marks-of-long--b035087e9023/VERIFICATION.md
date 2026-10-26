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

# Reproducibility and verification

Run the standalone Python 3 standard-library script `gap_shape_verifier.py` in the same directory. Its deterministic output for this package is recorded in `gap_shape_verifier_output.txt`.

The script derives the exact marked weights by independent uniform-minimum moment formulas and checks all \(100\) normalization identities for \(n=1,\ldots,100\) against the primary literature's gap probability. It checks \(5{,}050\) symmetry and strict-positivity cases. It also computes the exact conditional apex mean, variance and left boundary uniformized first-arrival mean at \(n=5,10,20,50,100,200\); the values approach the theorem's predicted limits \(1/4\) for \(\operatorname{Var}(K_n)/n\) and \(2\) for \(n\mathbb{E}[U_0\mid E_n]\).

Proof obligations not discharged by this finite checker are the asymptotic independence of the conditional boundary/peak marks, the tilt's uniform integrability, the tightness of the uniform profile, and convergence to the Gumbel law. These are established analytically in `RESULT.md` by order-statistic identities, exact tilt expectations, binomial large-deviation bounds and weak-convergence calculations. The finite exact checks do not certify any infinite limiting claim or claim independent validation.
