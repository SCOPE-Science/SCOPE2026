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

Exact standalone program: `verify.py` with dependency `sympy==1.14.0` (`requirements.txt`). Invoke `python verify.py` in the directory containing those files. `verification_output.txt` contains the complete expected standard output from an actual successful run.

The computation enumerates \(\mathbb P^2(\mathbb F_9)\), the Hermitian quartic, all explicit inverse-image components of its 28 tangents, and the 56-by-56 intersection matrix. It constructs seven pairwise disjoint exceptional classes and an integer Picard basis. Its Frobenius matrix preserves the intersection form and anticanonical class, has square the identity, and is exactly a product of four orthogonal square-\(-2\) root reflections. Smith normal form of \(M-I\) has four unit entries and four zero entries. Checks over \(\mathbb F_3\) and \(\mathbb F_9\) give 10 and 154 points.

The program checks finite identities; completeness over the algebraic closure requires the standard general 56-curve theorem, and the extension-field zeta formula uses the established cohomology of a geometrically rational surface. Historic priority beyond inspected sources is not machine-verifiable. No independent audit has been performed.
