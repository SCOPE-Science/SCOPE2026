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
# Verification notes

The embedded `verify.py` executes exact exhaustive enumeration over finite fields with orders \(2,3,4,5,7,9\). It represents \(\mathbb F_4\) by the irreducible polynomial \(x^2+x+1\) and \(\mathbb F_9\) by \(x^2+1\) over \(\mathbb F_3\). The checker independently forms products, determinants and traces and tests nilpotence by characteristic-polynomial coefficients; it does not classify a product merely from the derived census. It then checks each left-factor conditional count, every class multiplicity, the total nilpotent-product polynomial, the zero-product polynomial and the nonzero product factorization.

Observed exhaustive totals for nilpotent product, followed by zero products, are: \(q=2:(30,18)\), \(q=3:(165,69)\), \(q=4:(532,172)\), \(q=5:(1305,345)\), \(q=7:(5005,973)\), \(q=9:(13617,2097)\). Execution completed with `VERIFY_OK`.

The general proof instead uses: the \(q^2\) traceless nilpotent matrices, elementary conjugation to the two-by-two Jordan nilpotent block, trace-bilinear incidence, and the finite-field square map in characteristic two. Finite tests do not imply unbounded completeness. No independent mathematical audit has been performed.
