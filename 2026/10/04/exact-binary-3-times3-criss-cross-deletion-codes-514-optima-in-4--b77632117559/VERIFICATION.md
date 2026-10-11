---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Independent enumeration of all 512 binary 3×3 arrays reconstructed every 2×2 one-row/one-column deletion ball. Exact set packing over the 16 possible outputs gives maximum 4. Separate four-clique enumeration gives 514 labeled optima; the verified 16 channel symmetries partition them into 46 classes with orbit sizes 2:1, 4:4, 8:20, 16:21.

## originality

PASS

The same-object primary paper defines criss-cross deletion balls and gives general large-n coding bounds, but it does not determine the binary 3×3 maximum or enumerate optimum orbits. The multiple-error follow-up is broader asymptotically but not a small-case classification. Exact searches found no inspected source with the 514/46 census.

## value

PASS

This is the natural smallest square case whose surviving output is still two-dimensional. The complete optimum and symmetry classification provides a reproducible benchmark for the criss-cross synchronization channel and reveals substantial nonuniqueness of extremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
