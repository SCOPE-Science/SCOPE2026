---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed exact convex program of conditional means x<=-u<z<v<=y under ax+cz+by=0 and weighted second moment ax²+cz²+by². KKT active sets yield m=au²+bv²+(au-bv)²/c in central regime, m=(cu-bv)²/a+bv²+cu² when b>u/(u+v), and m=au²+(au-cv)²/b+cv² when a>v/(u+v). These regimes cannot overlap for a+b<1. For a=0, b>0 or vice versa, strict middle-boundary mass conditions and the 1-group variance floor follow from Jensen. For c=0, the unique weighted two-tail minimum is max(au²/b,bv²/a). With a=b=0, (Z+u)(v-Z)>0 almost surely gives uv>1, and a 2-point law achieves variance one iff uv>1. For all abc>0, m<1 allows perturbation to strict means followed by tail variance inflation; m=1 is attainable precisely for a<v/(u+v), b<u/(u+v). Independently minimized 110 randomized strictly positive triples with scipy SLSQP; max absolute discrepancy from piecewise m was 4.69e-8. This is corroboration only, not a proof of universal equality or strict endpoints.

## originality

PASS

Best-knowledge novelty is the *closed piecewise feasible-set formula with attainment/open-endpoint constraints* for two ordered tail probabilities. The 2023 Ion-Klaassen-van den Heuvel article gives a sharp maximum for their sum, not the joint region. General moment SDP methods can encode this optimization, but the compared statements do not directly yield the explicit five-case formula without eliminating the moment variables. The Ogasawara multiple-Cantelli full text remains inaccessible after open preprint/OA attempts and authorized Oxford returned vpn_disconnected; its abstract concerns multiple variables.

## value

PASS

Separate Cantelli bounds do not answer whether a specified lower-tail risk and upper-tail risk can coexist for one mean-zero, variance-one law. The exact ordered-pair feasible region answers that natural inverse moment problem for all thresholds, including the genuinely important open-middle equality exclusions and zero-mass faces. The boundary cases are not a routine renaming of a single scalar bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
