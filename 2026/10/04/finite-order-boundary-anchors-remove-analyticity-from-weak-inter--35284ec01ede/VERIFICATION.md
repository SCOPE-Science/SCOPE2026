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

Full inspection of Li--Xia's proof isolates analyticity at exactly the places used by the package: Lemma 2.9 needs a finite Taylor leading term for bounded distortion, and Theorem A chooses minimal-order sink/source germs so that lower periodic jets vanish and Livšic normalization can remove them. Smooth finite-order anchors supply the same Taylor expansions. Periodic germs flat to all orders contribute zero to every finite jet and therefore do not obstruct the normalization. The density-of-Birkhoff-sums step then constructs the required finite-order comparison anchors, and positive iterates preserve finite order and weak boundary interconnection. No numerical extrapolation is used.

## originality

PASS

Li--Xia assume analytic central dynamics and explicitly say analyticity is used in the center to handle arbitrary finite-order parabolic degeneracy. Their complete proof shows where it enters but does not state the smooth finite-anchor weakening, and analyticity itself excludes nonidentity infinitely-flat germs. The audited theorem permits exactly those flat germs away from two anchors, a strictly larger smooth class not covered by the source theorem or the stronger robust-interconnection result.

## value

PASS

The result identifies the exact local role of a strong global regularity assumption in a new transitivity mechanism and enlarges the theorem to smooth systems with arbitrarily flat non-anchor periodic fibers. Removing analyticity while preserving weak boundary interconnection is a natural and substantive robustness-of-hypotheses question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
