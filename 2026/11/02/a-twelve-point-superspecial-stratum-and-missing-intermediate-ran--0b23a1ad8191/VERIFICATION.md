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

The accompanying `verify.py` is a standalone Python-standard-library exact arithmetic verifier. Running it with Python 3.10 or later prints the text embedded in `verification_output.txt`, ending in `VERIFY_OK`.

The verifier constructs the finite field \(\mathbb F_{17^2}\) via the irreducible polynomial \(z^2-3\), checks four explicit irreducible quadratic factors of the Legendre Hasse polynomial, enumerates its eight roots, checks the five quotient formulas on every one of the \(56\) ordered distinct Hasse-root pairs, computes the full label-permutation orbit, and directly enumerates all \(82,082\) smooth ordered parameter pairs over \(\mathbb F_{289}\). The exact results are \(44\) root pairs with exactly two supersingular quotients and \(12\) with all five; the full parameter distribution is \((N_0,N_1,N_2,N_5)=(71130,10500,440,12)\). No assertion of geometric exhaustiveness rests solely on a bounded field scan: the Hasse polynomial has degree eight and all eight roots are found, and symmetry reduces every possible pairwise intersection to these root pairs. The infinite-family point counts follow by geometric incidence and field-of-definition arguments.

This is reproducibility evidence and self-review only; no independent audit has been conducted. It does not verify related moduli questions outside the smooth marked parameter space.
