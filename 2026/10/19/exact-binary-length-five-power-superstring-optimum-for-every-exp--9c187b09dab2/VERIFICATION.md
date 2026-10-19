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

# Reproduction and scientific limits

With Python 3 and the standard library, place `verify.py` and `CERTIFICATE.json` in the same directory and run `python3 verify.py`. The verifier builds all \(32\) binary roots and their cubes without external data, computes every directed suffix-prefix overlap, groups the roots into their eight rotation classes, and exhaustively enumerates at most \(5!=120\) orders inside each class.

The global integer subset/end-state dynamic program has \(4096\) states, with state counts by number of visited classes: \(32,224,672,1120,1120,672,224,32\). The minimum over final states is \(122\). The program checks its selected route against every mandatory cube, validates the separately embedded `CERTIFICATE.json` witness and reproduces host lengths \(40p+2\) at exponents \(3,4,5,8\).

As a separate finite cross-check of the block-restricted algorithm, for binary root lengths \(2,3,4\) and exponents \(2,3,4\) the verifier performs a second, unrestricted Hamiltonian-mask recurrence and confirms agreement with the block dynamic program. The exact mathematical argument excluding ungrouped paths for five-symbol roots at \(p\ge3\) is given in `RESULT.md`; the finite tests are not used to infer the all-exponent identity.

Expected final output line:

`VERIFY_OK power_exponent_formula_n5_p_ge3_exact_necklace_DP_and_switch_bound`

No formal proof assistant, third-party solver certificate, or independent scientific audit is asserted. The package verifies the explicit computation and construction, while the manuscript supplies the general transition-cost proof.
