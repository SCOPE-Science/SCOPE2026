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

# Verification and exact boundaries

The standalone `verify.py` was run with Python 3 and SymPy against the actual local artifact. It returned `VERIFY_OK` for coprime exponent pairs \((2,3),(2,5),(2,7),(3,4),(3,5),(3,7),(4,5),(5,6),(5,7),(7,8)\). For each pair it enumerates parity-admissible labels, constructs the full degree-two diagonal/antidiagonal inclusion matrix and the degree-zero incidence matrix, and computes exact integer Smith normal forms. The degree-two blocks yield \(g\) invariant factors equal to \(2\); the degree-zero map has \(g\) invariant factors equal to \(1\) and one zero row.

The **all-parameter argument** is the uniform Mayer–Vietoris proof in RESULT.md, not finite extrapolation from those ten examples. Essential noncomputational inputs are the rigorously established geometric component decomposition and intersection graphs in Liriano's 2026 Lemmas 1–2, the antipodal map's integral degree \(-1\), the ordinary topology of the complex affine quadric and \(\mathrm{SL}_2(\mathbb C)\), and compatible semialgebraic triangulation for closed subvariety inclusions. These are stated explicitly in the proof and can be independently reconstructed.

The computation does not establish complete priority over inaccessible historical papers, determine cup products or unreduced representation schemes, or count independent external validations. No independent audit has been performed.
