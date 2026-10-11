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

The analytic verification is the phase-character classification in the proof. For each positive difference \(h\), expand the squared correlation \(|C_h|^2\). After removing its constant diagonal terms, every Haar character has either three support points with exponent pattern \((-1,2,-1)\), or four support points with exponent pattern \((-1,1,1,-1)\). The first pattern is exactly one three-term progression and occurs once; the second is exactly one four-distinct equal-sum relation and occurs twice. Orthogonality on the phase torus then gives \(\operatorname{Var}(E_A)=2T(A)+8Q(A)\), hence \(\operatorname{Var}(X_A)=8T(A)+32Q(A)\).

`artifacts/verify.py` independently reconstructs those exponent vectors with integer arithmetic. It checks all \(255\) nonempty subsets of \(\{0,1,\ldots,7\}\) and verifies the formula exactly. It also checks consecutive supports of sizes \(2\) through \(20\) against the closed parity expressions obtained by direct simplification.

The finite replay is not used to infer the theorem for arbitrary finite supports. Its purpose is to detect sign, multiplicity, and normalization errors in the symbolic classification. The theorem does not address cyclic wraparound, non-Haar coefficient laws, or the full distribution beyond mean and variance.
