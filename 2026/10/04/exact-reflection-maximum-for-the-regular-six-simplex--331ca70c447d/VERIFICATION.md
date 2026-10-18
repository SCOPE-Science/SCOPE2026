---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a regular six-simplex, every support meets a vertex; normalize edges to 1 and contact at 0. Its Gram inverse 2I-(2/7)J gives A^2=[2(Q-1/7)]^-1 in normalized nonnegative vertex heights. The reflected-hull volume follows integration over upper projected facets, leading to R=2[Q_I-(8/7)t+(m+1)/7]/(Q-1/7). For m in {1,...,5}, conditional Cauchy equalization of complementary heights and fractional derivative sign of Q_I reduces to F_m(t); m=0 gives R<=12 and m=6 impossible. Independently differentiated each F_m and checked all admissible radical maxima, showing m=1 gives R=6+2sqrt(511)/7. The unique m=1 ratio is (29-sqrt511)/11; 7 possible contact vertices times 6 small-height vertices gives exactly 42 supports. Separately independently constructed seven reflected vertices and verified six-dimensional ConvexHull ratio 12.458659745975591 vs exact 12.45865974597561. Finite/float hull is not the universal proof.

## originality

PASS

Best-of-knowledge statement-level prior comparison: the exact final claim goes beyond inspected narrower qualitative, lower-bound, upper-bound or Poisson-restricted results. This is not a claim of exhaustive historical priority; see four comparisons and source-specific risks.

## value

PASS

First full global solution for dimension six of the corrected Horváth supporting-hyperplane reflection problem, including rigorous upper bound over all facet chambers and complete 42-support equality orbit. The matching two-upper-facet numerical witness was already known; the global optimization and equality classification are the valued novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
