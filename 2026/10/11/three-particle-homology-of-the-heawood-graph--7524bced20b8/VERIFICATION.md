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

The included verifier reconstructs the 14-vertex, 21-edge Fano-incidence model of the Heawood graph and the weight-three full-vertex reduced Świątkowski complex. It verifies the chain dimensions, checks the integer identity \(\partial^2=0\), and recomputes sparse boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\).

For the integral degree-three statement, `artifacts/d3_kernel.json` supplies a concrete integer cycle. The verifier checks that its support has 881 basis elements, every nonzero coefficient is \(1\) or \(-1\), the coefficient gcd is \(1\), and its boundary is exactly zero. Together with rank \(2911\) for \(\partial_3\) modulo \(3\), this proves that the integral kernel has rank one and that the supplied primitive cycle generates it.

The verification does not compute Smith normal forms of the lower differentials and therefore does not claim the integral structures of \(H_1\) or \(H_2\). It also does not address particle numbers other than \(3\).
