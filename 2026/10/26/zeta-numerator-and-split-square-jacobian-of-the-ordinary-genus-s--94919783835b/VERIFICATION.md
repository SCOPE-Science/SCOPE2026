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

# Exact verification and its scope

Run `python3 verify.py` with any recent standard Python interpreter. No external modules, data downloads, services or network access are needed. A successful run prints `VERIFY_OK` with the trace-frequency vectors, the six point counts, the thirteen Weil coefficients and the Jacobian order.

For \(\mathbb F_{27}\) and \(\mathbb F_{729}\) the verifier first proves irreducibility of the stated monic reduction polynomials using the finite-field Frobenius/GCD criterion. It then enumerates all field elements, computes the value of \(x+(x^3-x)^{-1}\) at every nonpole, and accumulates all three absolute-trace frequencies. Independently, it directly enumerates the image of \(y\mapsto y^3-y\) and checks that the same nonpole values are represented. It reproduces Newton coefficients, functional-equation coefficients, polynomial factors and the integer quadratic-factor obstruction for the surface polynomial.

The finite calculations establish the extension counts at degrees three and six; the remaining degrees up to six are derived mathematically from translation by one. The standard genus formula, Weil functional equation and Tate isogeny classification remain external mathematical inputs. No geometric simplicity, classification of twists or rational Jacobian group structure is asserted.
