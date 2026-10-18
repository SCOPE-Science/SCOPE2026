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
# Verification

Run `python3 stern_22_27_checker.py` with Python 3 and no extra packages.

The program checks the complete quotient of primitive residue pairs under unit scaling for each of the moduli \(22\), \(27\). It tests exactly \(36\) consecutive order-twelve residuals per modulus and compares twelve initial counts, which together establish the full rational series by the \(36\)-dimensional Cayley–Hamilton lemma in `RESULT.md`. An alternative direct-sum argument uses equality of the first \(72\) levels and a \(72\)-dimensional transfer matrix to conclude the equality at every depth. The checker verifies this initial equality directly. Raw Stern-array enumeration corroborates the first twelve levels.

Expected output includes four lines beginning `PASS:` and the common sequence starting with zeros through level six, then \(4,8,16,24,52\). Integer arithmetic is exact; no numerical precision assumption is required. There is no claim of independent audit or certification beyond these reproducible checks.
