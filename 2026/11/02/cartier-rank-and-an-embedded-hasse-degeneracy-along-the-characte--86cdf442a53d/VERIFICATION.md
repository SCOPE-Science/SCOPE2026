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

# Reproduction and limitations

Install the dependency in `requirements.txt` and run `python VERIFY.py`. The program reconstructs the full polynomial coefficient matrix from the general characteristic-five Cartier expansion; it does not merely substitute a precomputed matrix. It checks the exact displayed nonzero entries, verifies the two-by-two determinant and nine decisive four-by-four minors, and enumerates all \(125\) coefficient triples \((u,a,b)\in\mathbb F_5^3\) at a fixed value of \(c\) to corroborate the rank stratification. Its output is:

`VERIFY_OK: polynomial Cartier coefficient matrix (15 entries), 4x4 minors, GF5 125 triples; rank counts 0:1 3:24 4:100`

The exhaustive finite-field enumeration alone does not prove a claim over an algebraic closure. The algebraic proof uses the polynomial matrix support, the exact determinant, and the ideal identity. The \(a\)-number equals the corank of the Cartier operator, not its stable iteration rank. The coefficient determinantal scheme depends on the stated entrywise fifth-power matrix convention; the geometric loci do not. No external independent audit has been performed.
