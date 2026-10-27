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
# Reproduction and boundaries

Run `python nil_checker.py` from the directory containing `verify.py`. This constructs actual finite-field multiplication operator matrices and tests their powers through dimension \(n\), independently of the factor-based prediction. `nil_output.txt` is an exact record of the run. The 11 exhaustive configurations test 3,683 elements; a 12th configuration performs 100 direct comparisons at \((n,q)=(5,11)\). The test includes extension fields \(q=4,8,9\) and modular characteristics \(p\mid n\). Direct rank checks use `python verify.py`; see `checker_output.txt`.

The proof, not the finite tables, establishes the full parameter range. Factor permutations are computed from irreducible factors of the square-free part \(X^m-1\), and the characteristic radical fibers are accounted for by \(q^{n-m}\). No independent validation or external audit has been carried out.
