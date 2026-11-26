---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Re-audited the full corrected RESULT.md with geometric smoothness defined by the simultaneous vanishing of the equation and all partials. The brief blocking-size double-count excludes blocking sets of size ≤5 containing no full line; a smooth cubic has no full line by Bézout. All four rational fibers have points by Hasse and their rational point sets partition the 13 points when there is no rational base point, so two blocking fibers are impossible. An independent exact replay computed 29524 scalar classes, verified injective cubic point evaluation, recovered exactly 936 smooth blocking equations in the model's PGL orbit, and enumerated distinct pencils through it directly as sets of the three complementary scalar-normalized forms. The replay used a separate geometric-smoothness criterion: reject a rational line component, an empty rational point set or a rational singularity. A geometrically integral singular cubic has exactly one singular point by its genus defect, hence a rational one. A geometrically reducible cubic with no rational line must be three conjugate lines; any rational point common to its support then lies on all conjugates and is singular. Thus the alternative test is exact, and no finite extension cutoff is needed. The result is 312 pencils with profile frequencies 24, 132, 42, 114 as stated; the example belongs to the 132 class. Transitivity transfers this to each of the 936 blocking equations. Uniqueness gives 936·312=292032 without multiple counting. The repaired statement, proof and retained Gröbner verifier consistently use C=0 along with the partials; no verification-file edit is required.

## originality

PASS

For the repaired finding credit only the exact pencil incidence census and complementary-fiber profile frequencies. The numerical upper bound on blocking fibers is a routine corollary of earlier facts; the identical single-cubic classification is present in a separate same-day indexed result. Neither provides the count or profiles of pencils through a specified cubic, and the separately indexed base-point census does not mark blocking members. Their date supplies no ordering.

## value

PASS

The census is a motivated refinement of blocking-versus-nonblocking behavior in pencils, not an arbitrary coefficient slice: it simultaneously controls all four fibers over the first odd prime field, with no rational base points. The exact incidence count and its four complementary profiles tell which rational fiber configurations are realized around the exceptional blocking class and their frequencies. They can be used in finite-field pencil constructions and in comparing counts with and without incidence restrictions. The value is in this independently useful distribution, not in recomputing one cubic orbit or the simple upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
