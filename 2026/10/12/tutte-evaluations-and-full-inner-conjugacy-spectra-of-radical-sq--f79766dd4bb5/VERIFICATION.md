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

Run `python3 verify.py` in the extracted package. The program uses only the Python standard library. It directly constructs multiplication and inversion of units of the truncated quiver algebra (with an explicit multiplication table for the extension field of order four), conjugates each element by *every* unit, forms actual orbits, and independently compares the resulting size multiplicities with component-and-support predictions and the Tutte subset evaluations.

Cases cover five quivers over \(\mathbb F_2\) and \(\mathbb F_3\), and two additional quivers over \(\mathbb F_4\): one arrow, two parallel arrows, two-edge path, and directed versus transitive triangle. The triangle spectra over \(\mathbb F_3\) agree orientation-by-orientation with counts \(30\) for units and \(69\) for all elements. The last line must be `VERIFY_OK`.

The finite computations are exact within the enumerated finite cases, but they do not prove the infinite family. Generality follows from the explicit conjugation formula, the incidence kernel count, and the Tutte subset identity in the mathematical proof. No independently conducted audit has been performed.
