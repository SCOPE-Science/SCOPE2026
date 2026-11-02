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

# Reproducibility and limits

Run `python verify_orbits.py` using Python 3 with its standard library only. The program enumerates nonzero vectors in \((\mathbb Z/(p-1)\mathbb Z)^2\), applies explicit integral matrices representing cyclic origin-fixing automorphisms of orders \(2\), \(4\), and \(6\), checks the predicted numbers and sizes of orbits, and then checks the complete distribution of automorphism orders. It also checks that the weighted orbit sizes recover the exact number of degree-two closed points. The ten sample parameters include \((p,m)=(5,6),(7,4),(11,6),(11,4),(17,2),(19,2),(23,6),(23,4),(29,6),(31,4)\).

For the maximal-elliptic starting examples it directly counts points over \(\mathbb F_{25}\), \(\mathbb F_{49}\), and two examples over \(\mathbb F_{121}\), representing the quadratic field as a polynomial quotient. Both `VERIFY_OK` and `FULL_VERIFY_OK` are printed when all assertions succeed. No external datasets, network calls, or computer-algebra libraries are needed.

These checks do not enumerate every prime and are not an exhaustive proof of the infinite statement. The mathematical proof instead uses the fact that maximal Frobenius is \([-p]\), an exact torsion-difference quotient, and the Burnside fixed-point calculation. The self-review checks the reasoning but is not independent validation.
