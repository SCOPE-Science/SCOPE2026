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

For d>=3 with N=d-1, signed-permutation symmetrization reduces an arbitrary real-linear right inverse to two real orbit weights a+b=1 at e_1. The 1-Lipschitz coordinate-deletion distance witness has exactly the same mean S_N=2E sqrt(Bin(N,1/2)) in both orbits and vanishes at a same-facet vertex distance sqrt(N), yielding a global lower bound S_N/sqrt(N) even for signed/asymmetric operators. The positive averaging map has exact KR ratios 1 for original vertex pairs, S_N/sqrt(N) for same-facet vertex-center pairs, U_N/sqrt(N+4) for opposite-facet pairs, 1 for opposite centers (flip matching), and 1 for different-axis centers (mass 1/2 at cost 2sqrt(2)). Off-facet U_N/sqrt(N+4)<=S_N/sqrt(N): for N>=4 use binomial variance plus Jensen with explicit positive rational difference (N-4)/(N(N+4))+1/(4N^2); N=2,3 hold by direct radical evaluation. Strict increase follows from strict conditional Jensen under random deletion; the sqrt2 limit and -1/(8N) term from binomial moments and exponentially small tails. Independent fresh computation checked 7152 vertex-center pairs, 88 center-center W1 minimizations with an independent linear program, and multiple moment bounds. Finite checks are corroborative; unlimited dimensions are proved analytically.

## originality

PASS

The closest published exact cube-center theorem has been read in full this run: its metric set adds exactly one cube center and supplies the same N=d-1 one-facet lower-bound constant, but does not assert compatible extensions to 2d separate facet centers. The new theorem supplies the needed off-facet vertex moment inequality and exact W1 couplings between all pairs of centers, proving simultaneous norm equality for arbitrary real-linear extensions. Bruè–Di Marino–Stra establishes random-projection linear extension and log-doubling bounds; Basso surveys general quantitative bounds. Neither full accessible mathematical text provides the exact all-facet compatible optimum. Search for literal and equivalent formulations did not find a stronger implication. The mathematical work is a best-of-knowledge priority claim, not historical certification.

## value

PASS

The Euclidean cube with all its codimension-one face centroids is a natural simultaneous finite-metric interpolation domain. The optimal one-point facet value was already known but in general separate optimal extensions can conflict across new points: showing full 2d-point compatibility requires nontrivial exact KR couplings and off-facet binomial domination. The theorem proves an unrestricted sharp operator constant, gives an explicit positive norm-attaining operator, and supplies a strict dimensional law and rate toward sqrt2. This addresses a motivated geometric gap, not mere reevaluation of the known one-center binomial mean. The result deliberately does not claim arbitrary polytope faces, Banach-valued extensions, or uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
