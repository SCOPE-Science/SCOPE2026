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

# Verification details

Run `python verify.py` with Python 3.10+ and NumPy. The program constructs the graph and matching complex, checks the complete cardinality distribution of \(708\) augmented faces, verifies the toggle matching and acyclicity of every reversed Hasse incidence, builds the exact signed algebraic Morse differential, and verifies its unit pivot and rank. It also determines the degree-two and degree-three dihedral characters by finite-field boundary-image coordinates for both primes \(101\) and \(103\), and verifies the Lefschetz trace identities for all twenty dihedral symmetries.

The integral homotopy conclusion uses the exact, primitive integer Morse differential together with the fact that a complex with one vertex, no one-cells and only two- and three-cells has attaching maps classified by the integral \(\pi_2\) lattice. The modular representation calculation is exact because integer trace bounds are at most eight, well below either prime's centered-lift threshold. No test addresses larger antiprism graphs, and the package does not assert independent external audit.
