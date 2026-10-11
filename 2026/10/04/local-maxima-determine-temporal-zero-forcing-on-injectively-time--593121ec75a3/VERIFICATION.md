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

With s seeds, exactly n-s one-shot edges must transmit, so exactly s-1 unused edges cut the path into s components and each component contains exactly one seed. A retained component is forceable from its unique seed iff its edge times strictly decrease toward the seed from the left and increase away to the right, i.e. iff the block has no strict interior local maximum. Therefore cuts are exactly hitting sets for peak neighborhoods {i-1,i,i+1}. Strict peaks cannot be adjacent; these neighborhoods overlap exactly for peak centers distance two, so each overlap chain of r peaks needs and admits ceil(r/2) cuts. Minimum interval stabbing equals maximum disjoint neighborhoods; their centers lie in 2,...,n-2 and must be at least three apart, giving floor((n-1)/3) extra cuts, achieved by the block timing (1,3,2),(4,6,5),.... The frozen verifier exhausts all timings through n=9 only as a stress test of this all-n proof.

## originality

PASS

Baste--Dreyer--Marcille--Rabie--Toullec-Streicher introduce the synchronous temporal zero-forcing process and advertise hardness/polynomial results, including temporal trees, but the accessible primary abstract does not state the exact one-shot injectively timed path formula. Resultary searches for the path/local-maximum law returned no covering published finding. A separate public project advertises alternating-path results under related temporal variants, but its complete manuscript was not available here; that source remains a named residual risk rather than being assumed noncovering.

## value

PASS

Paths with one-shot injective timings are the canonical minimal connected test family for temporal zero forcing. The theorem gives both an exact per-timing structural formula and the sharp worst timing, converting dynamics into a transparent local-maximum obstruction. This is a natural complete classification rather than a small computational census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
