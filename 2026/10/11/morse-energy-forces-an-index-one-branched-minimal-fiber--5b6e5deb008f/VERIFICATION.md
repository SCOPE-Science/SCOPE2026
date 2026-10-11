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

The accepted statement is proved symbolically; no numerical or exhaustive computation is needed.

The following source facts were checked directly in the open primary text: \(d\mathcal E_X=0\) exactly when the Hopf differential \(\Phi_X\) vanishes; \(\mathcal E\) is invariant under pullback by the pseudo-Anosov monodromy; the descended energy on \(\mathcal T(S)/\langle f\rangle\) is proper; and \(\mathcal E(X)=A_0\) exactly for least-area maps, which are conformal embeddings onto least-area fibers. The source also records proper discontinuity of the pseudo-Anosov orbit.

The topological step was independently reconstructed: contractibility of \(\mathcal T(S)\) makes the cyclic quotient a \(K(\mathbb Z,1)\), hence its first homology over any field is nonzero. For a proper Morse exhaustion, the weak Morse inequality therefore forces at least one index-one critical point. Lifting through the covering preserves criticality and Morse index.

The index-one point cannot attain \(A_0\), because a negative Hessian direction would locally decrease the function below a global minimum. Its Hopf differential vanishes, so the associated nonconstant harmonic map is a branched minimal immersion.

Limit: the verification does not establish the Morse hypothesis for any particular mapping torus, and it does not infer embeddedness or an energy-gap estimate for the forced index-one immersion.
