---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

PASS: For each site E_i(X)=|φ_i><φ_i|_i⊗tr_i X is CPTP, idempotent and pairwise commuting. Conditional on selected sites V, T^m=∑_V p(V)E_V; on full V, E_V=R. Hence T^m=(1-p_m)R+p_m N_m, giving diamond upper bound 2p_m even with an arbitrary reference. An input tensor product of local states orthogonal to φ_i leaves at least one orthogonal factor for every incomplete V, so its output is block-orthogonal to |Φ>, saturating 2p_m; ancillas cannot help. Inclusion–exclusion yields exact weighted tail for m=0 as well (0^0=1); binomial factorial domination yields limit 1−exp(−e^(−c)) at m=n log n+cn and epsilon quantile. The fair-bit classical hypercube TV upper bound by Walsh chi-square and lower bound by magnetization variance establish (1/2+o(1))nlogn in same update normalization. Independently computed 36 exact rational mask distributions, all matching weighted inclusion-exclusion, for n=1,2,3 and m=0..8; the structural diamond proof, not masks, handles all reference ancillas and dimensions.

## originality

PASS

PASS: Temme–Wocjan arXiv:2504.02651v1 Section 3 Eq56 gives the quantized grand-coupling Kraus construction, Section 5.2 the fair-bit hypercube and one-sided coupon tail, Section 6 asks about its general stationary-mass prefactor. Those prior statements do not provide this exact diamond norm, saturating no-ancilla witness for all positive weights/local pure product targets, or the sharp Gumbel diamond profile. The classical coupon collector and hypercube TV cutoff are explicitly prior, not novelty claimed. Possible implicit derivability from standard commuting channel decompositions is retained as originality risk.

## value

PASS

PASS: Exact diamond distance, not merely trace-distance upper bound, is a strong operational guarantee for a natural quantum-state preparation protocol against entangled reference inputs. It gives all-time weighted formula, sharp uniform cutoff location and profile, a provable ancilla-free optimum and concrete contrast with classical mixing. Scope deliberately excludes noncommuting/interacting/mixed-state channels, so makes no spurious claim to solve the original broad open question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
