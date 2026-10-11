---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The normalized Gibbs state has tangent \(-h/d\) at the maximally mixed state, with h the centered Hamiltonian. Applying the entropy Hessian \(S(I/n+\varepsilon X)=\log n-(n\varepsilon^2/2)\operatorname{Tr}(X^2)+O(\varepsilon^3)\) to the joint state and both marginals yields the difference of three squared Hilbert--Schmidt norms. Orthogonally decomposing h into A-only, B-only, and interaction components leaves exactly \(\operatorname{Tr}(H_{\mathrm{int}}^2)/d\). Vanishing interaction is equivalent to a commuting local-plus-scalar decomposition and hence exact Gibbs factorization. Pauli orthogonality gives the crossing-string form. For disjoint Ising bonds the state factorizes over bonds and the exact one-bond mutual information is \(x\tanh x-\log\cosh x\), giving the claimed sharpness. The inspected verifier independently checks the projection algebra, a noncommuting two-qubit numerical Hessian, the Pauli form, and the Ising formula.

## originality

PASS

The recent exact-area-law source explicitly notes that perturbation suggests an \(O(\beta^2)\) leading term but does not extract a basis-free Hessian coefficient; its proof is nonperturbative and designed to control higher orders. Older high-temperature mutual-information papers inspected through the source trail are model-specific. A targeted Resultary search for the interaction-projection Hessian returned no implication-equivalent published finding. Because the entropy Hessian itself is standard, best-of-knowledge originality is assigned specifically to the universal Gibbs interaction-projection formula together with the Pauli crossing interpretation and sharp boundary witness, with the standard-information-geometry residual risk recorded.

## value

PASS

The exact coefficient answers a natural question left behind by a current nonperturbative area-law result: which Hamiltonian components contribute at the first nonzero high-temperature order. It cleanly removes all bulk-only directions, gives a directly computable Pauli formula, and supplies an exact family saturating both quadratic temperature dependence and linear boundary scaling. This is a motivated structural refinement rather than an arbitrary Taylor coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
