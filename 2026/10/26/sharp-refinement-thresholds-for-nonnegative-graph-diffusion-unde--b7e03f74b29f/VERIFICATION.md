---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The binomial series of f_r gives its signed coefficient (-1)^k a_k. When d(u,v)=d, all lower powers vanish off diagonal because each multiplication can traverse at most one edge; at order d there are no diagonal stays and every weighted geodesic contributes with the same sign (-1)^d. Thus the leading contribution is a_d W_d h^d with W_d>0. Geodesic subpaths realize every positive distance up to the diameter; finiteness gives a common small interval when the leading signs are positive. The signs through k=5 prove the r=3,...,17 and r=18 thresholds and also handle r=2 for diameters ≤2 or ≥4. For diameter three at r=2, I checked that the frozen 13-vertex construction has diameter three and endpoint L³=-1, L⁴=2 (16 length-four paths less the degree sum 14), whereas on the four-vertex path these powers are -1,-6. With a₃=0 and a₄=-3/8 the leading terms have opposite signs. The diagonal starts at one and each resolvent preserves the all-ones vector. The result is local for each fixed graph, not a timestep uniform in graph and weights. Independent exact replay passed: python3 /workspace/checks/richardson_coefficients.py. The supplied checker was inspected, not executed.

## originality

PASS

The earlier scalar barrier and extrapolation literature do not give these entrywise diameter cutoffs or the degenerate r=2 examples. The strongest archive overlap, the November 22 all-refinement geodesic record, directly covers much of the same mathematics but is later-dated than this October 26 record. The latter's r=2 diameter-three split is not established by the later first-negative-coefficient criterion. The pass is a best-of-knowledge comparison against established earlier coverage, not an independent dating certification.

## value

PASS

The proof ties positivity of an accelerated diffusion step to an intrinsic graph invariant and pins down two sharp refinement requirements uniformly over edge weights. The 13-vertex witness and positive path demonstrate why the first zero coefficient is a genuine structural boundary, not just a failed sign test. These are useful method-selection facts even without a uniform timestep estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
