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

Run `python3 artifacts/verify.py` using only the Python standard library. The code builds the simplicial complex from its graph-domination definition, builds the signed chain action of vertex permutations, and forms averaged cyclic-invariant boundary maps for each of the eleven conjugacy types of \(\mathfrak S_6\). It checks \(\partial^2=0\), performs sparse rank reductions modulo the two primes \(2147483647\) and \(1000000007\), and reproduces the full character, Frobenius-alternant Specht decomposition, and independent signed Lefschetz checks. The exact output from a successful execution is included as `artifacts/verification_output.json` with status `D63_SYMMETRY_VERIFY_OK`.

The prior integral homotopy classification implies all reduced integral homology is free in degrees four and five. Since neither prime divides any relevant cyclic-group order, the averaging idempotent splits a free module after localization and its rank is unchanged by reduction modulo either prime. Thus the modular homology-invariants computed by the program are exactly the rational invariants used to reconstruct the character. The checker independently verifies the complex's face counts, its modular Betti dimensions, and all required boundary relations, but does not reprove the prior global sphere-wedge theorem. The claimed irreducible representation is over \(\mathbb Q\), not an integral-lattice or characteristic-dividing-group-order assertion. Independent mathematical audit of this result has not been performed.
