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

# Reproducibility
Run `python3 verify_picard.py` using a standard Python 3 installation. The standalone verifier requires no third-party dependencies and checks all marked quartic models over \(\mathbb F_2\) and \(\mathbb F_4\), including the discriminant condition and semilinear Cartier stable rank. It checks every admissible quotient identity over \(\mathbb F_{2^m}\) for \(1\le m\le4\) and counts points on three example curves over four finite fields. The full output is in `verification_output.txt` and ends with `VERIFY_OK`.

The infinite-field conclusion rests on the differential calculation and the tame cyclic cover genus argument. The elliptic quotient decomposition rests on an exact polynomial identity and the finite-group character splitting for odd \(\ell\). The finite enumerations are illustrative tests, not substitutes for these proofs. Historical priority is qualified by the lack of the full 1991 article.
