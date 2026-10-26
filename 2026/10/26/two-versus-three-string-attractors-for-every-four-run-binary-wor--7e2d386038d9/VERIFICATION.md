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

# Reproducible mathematical checks

Run `python3 standalone/verify.py` from the extracted finding directory. It uses only the Python 3 standard library and produces:

`VERIFY_OK exhaustive_parameter_quadruples=4096 generating_coefficients=19 parameters=1..8 lengths=4..22`

The verifier builds an occurrence mask for **every distinct nonempty factor** and independently tests all possible position pairs. For each of the \(4096\) four-run words with \(1\le a,b,c,d\le8\), it checks the proposed minimum against exhaustive two-position search, then independently checks that the stated optimal positions cover all factors. At each total length from \(4\) through \(22\), it enumerates all positive compositions into four parts and compares the count of three-attractor words against the coefficient computed from the stated rational generating function.

The verification is finite and does not establish the theorem for arbitrary parameters. The all-parameter proof relies on the unique middle transition, explicit characterization of the single-transition factor rectangles, optimal witnesses and necessary obstructions. No independent audit, external certification, or machine-verified infinite proof has been carried out.
