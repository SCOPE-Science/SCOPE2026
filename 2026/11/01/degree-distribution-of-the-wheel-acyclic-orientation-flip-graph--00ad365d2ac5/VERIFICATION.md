---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The explicit orientation parametrization partitions cases by constant versus mixed hub-spoke direction. Mixed runs have forced unflippable boundary edges and every within-run rim edge is individually reversible; source/sink counts of oriented paths have P_l(z)=sum_s C(l,2s-1)z^s and B(x,z)=zx/(1-2x+(1-z)x^2). Cyclic run compositions contribute (2m/k)z^(m-k)[x^m]B^k, and uniform spokes require the one-wrong-way-edge correction. Extracting the coefficient at z^m yields the Lucas identity via logarithms. Independently enumerated every directed-edge orientation and legal flip for m=3..6, matching all four claimed histograms. The unrestricted result relies on the run proof, not the finite check.

## originality

PASS

The wheel-local vertex degree enumerator and its Lucas simplicial-vertex specialization are finer than the already-known acyclic orientation count, edge count and global graphical-zonotope face vector. Comparison of identical AO(W) objects in the full original Gray-code paper and the general f-vector theorem found no covering local-degree statement. Best-of-knowledge priority, not a novelty certificate.

## value

PASS

Complete local degree distribution for a standard natural orientation graph and its graphical zonotope (number of simplicial vertices), with an exact Lucas law and sharp maximum multiplicity, is a structurally useful invariant strictly finer than known total counts; not just an arbitrary fixed-size instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
