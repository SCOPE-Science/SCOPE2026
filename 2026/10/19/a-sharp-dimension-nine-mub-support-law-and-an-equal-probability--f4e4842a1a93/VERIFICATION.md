---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The trace pairing of F_9 is nondegenerate. Character orthogonality gives orthonormal finite bases; in the squared Gauss sum, summing over one coordinate after the difference substitution leaves only the zero difference for distinct quadratic coefficients, giving squared overlap 1/9. Diagonal traceless subspaces for the ten bases are pairwise orthogonal and have combined real dimension 80, so the squared norm of rho-I/9 is the sum of the squared probability deviations from 1/9. For pure states this gives sum p^2=2. Cauchy–Schwarz on all positive probabilities then gives 2 times total support >= (sum p)^2=100. For the unit five-coordinate witness, the unnormalized finite-basis sum is 1-zeta^A H(U)-zeta^(-A) H(V), with (U,V) running bijectively over F_3^2 and H=2 at zero, -1 otherwise. When A=0 exactly the four pairs with one zero give zero; when A is nonzero exactly the four pairs with neither zero give zero. All remaining sums have squared norm 9 and hence probability 1/5. The coordinate basis also has five equal nonzero probabilities, so equality holds. An independent integer character count reproduces both the overlap norms and all 81 witness norms.

## originality

PASS

The distinct contribution supported by the inspected evidence is exact saturation at dimension nine by the specified flat-on-five state, not the known moment identity or its universal Cauchy–Schwarz bound. Neither the closest complete-MUB support theorems nor the balanced-state constructions checked give this witness, an equivalent one, or an implication of the flat-on-five equality.

## value

PASS

The explicit exact witness closes the gap between a universal moment bound and actual attainment for a natural first odd composite square dimension; it supplies a balanced state in the congruence class excluded by the standard constructions. The small calculation is not the value: the sharp extremal statement and simple reproducible witness are.

The dated certificate retains the supplied scientific assessment, sources and limitations.
