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

# Verification and reproducibility

The self-contained file `verify_functional_derivations.py` creates all Leibniz constraints by multiplying basis vectors according to \(e_v^2=e_{f(v)}\) and \(e_v e_w=0\) for distinct vertices. A separate predicted-basis builder uses the claimed leaf-sibling blocks and modular-cycle assignments. Modular row reduction compares the dimension of the predicted basis with the entire equation-system nullspace, confirms independence and equation satisfaction, and tests sampled matrix commutators.

Execute `python3 verify_functional_derivations.py` with Python 3.8 or newer; no extra packages, network access, or cached inputs are needed. Successful termination prints `VERIFY_OK_FUNCTIONAL_DERIVATION_LIE` followed by trial and bracket-check counts.

The exhaustive range is all \(n^n\) functions on \(n\in\{1,2,3,4\}\) points for \(p\in\{2,3,5,7\}\), plus three selected functions on five points for each prime. Total configurations: \(4(1+4+27+256+3)=1164\). Matrix-equation ranks, the proposed basis, and nullity are compared for each configuration. Higher dimensions and arbitrary extension fields are not enumerated; the algebraic proof, not the finite tests, establishes the general theorem.

**Scientific limits:** This verifies a specified family of endofunction algebras, not weighted or multi-outgoing-edge evolution algebras. A finite checker cannot independently certify literature priority, field-universal truth, or a mathematical audit.
