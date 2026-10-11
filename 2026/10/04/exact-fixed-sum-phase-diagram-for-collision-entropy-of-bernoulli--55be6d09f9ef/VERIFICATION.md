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

Conditioning on the difference of the two-coin sums gives the exact autocorrelation expression. Direct expansion yields derivative \(4Dr-2Ds+2G\) and second derivative \(4D\), while \(2D\) is the squared \(\ell_2\)-norm of the zero-extended second-difference sequence, hence positive for every nonzero finite-support probability mass function. The feasible product interval at fixed sum is exactly the stated interval, so strict convexity makes the projection formula necessary and sufficient. Specializing to the empty background gives \(D=3\), \(G=1\), and the two boundary equations produce the thresholds \(1/3\) and \(1-1/\sqrt3\). The inspected exact-rational verifier independently reconstructs convolutions, the energy identity, the quadratic completion, projection, and the two-coin phase partition; those finite checks corroborate the symbolic proof.

## originality

PASS

The Shannon Shepp--Olkin work and its Renyi/Tsallis extensions address joint concavity, while the recent sharp-threshold work shows failure of universal joint concavity above order one along two-coordinate fixed-sum perturbations. Neither inspected statement classifies the global fixed-sum order-two optimizer. The audited quadratic collision identity instead reduces the entire pair transfer to one scalar product and produces exact deterministic/unequal/balanced phases. No covering published finding appeared in the semantic search.

## value

PASS

The result resolves a natural sharp pair-transfer question exactly at the collision-entropy order where global Shepp--Olkin-type concavity fails. The background-dependent optimizer and explicit two-coin phase boundaries explain when balancing helps, hurts, or is only partially optimal, providing more structural information than a counterexample to concavity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
