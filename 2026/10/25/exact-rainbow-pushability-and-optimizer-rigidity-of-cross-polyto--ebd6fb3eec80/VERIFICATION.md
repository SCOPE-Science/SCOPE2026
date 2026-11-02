---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every facet sign sigma the membership probability of row i is q_iσ=(1+sum_j σ_j(a_ij^+−a_ij^-))/2. Because collective expectation sum is zero, sum_i q_iσ=r/2, so AM–GM bounds each independent joint facet probability by 2^(-r). Summing 2^d facet probabilities yields min(1,2^(d-r)). For r<=d distinct fair signed coordinate axes always lie on some common facet. For r>=d, one fair law dedicated to each of the d axes plus arbitrary individually antipodally symmetric additional laws attains 2^(d-r). Equality in the summed facet bounds forces q_iσ=1/2 for every i and all sign σ, whence all individual law signs are balanced for each axis. Conditional on independent axes J_i with K distinct chosen axes, compatible signs have probability 2^(K-r). Thus probability=E 2^(K-r), sharp iff K=d almost surely. An axis appears in every positive-probability independent tuple iff at least one row is entirely supported on it; this proves exact optimizer characterization for r>=d. The r=d case forces a permutation of fair axis laws. Independent rational enumeration for 2<=d<=4 and r<=d+2 confirms constructions and nonoptimizer examples; the analytical finite-axis independence argument proves all dimensions.

## originality

PASS

The general centrally symmetric facet-depth bound min(1,f_{d-1}(P)/2^r) is already known; this statement specializes it for a cross-polytope. Originality lies in the matching lower bound, full equality/rigidity characterization, and exact cross-polytope family. Crucially, the same paper computes exact cube pushability, but duality does not preserve the vertex-sampling common-facet probability.

## value

PASS

The exact optimum and complete optimizer geometry answer a natural exact-value extension raised by the defining source on colorful-pushability. It provides a genuine sharpness example for the broad facet-depth theorem and shows how independent axis occupancy controls equality; the result is not just a renamed cube formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
