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

Both mechanisms are evaluated on precisely n students, n unit-capacity schools, complete strict truthful rankings, and ONE common strict student priority. Under that common priority, student-proposing deferred acceptance is serial dictatorship. Boston is immediate acceptance at each stated rank, irreversibly filling seats. At n=2 the first-choice tie can never produce an outcome difference. At n=3 a difference occurs iff students 1 and 2 rank the same school first and student 3 first ranks student 2's SECOND school (not the third school). For each label of shared first school there are 2 options for second student fallback, 2 for first student second choice and 2 for third student second choice: 3*2*2*2=24 of 6^3=216 truthful profiles, incidence 1/9. Direct independent simulation of every 2^2 and 6^3 preference profile reproduced 0 and 24 differences, four school-label orbits each size six, and the two 12-case rank vector patterns. In every difference second student prefers DA's assignment while third student prefers Boston's, establishing Pareto incomparability; no claim is made for arbitrary school priorities or unbalanced capacities. The source verifier implements each rule by independent constructions; this assessment uses an independent separately written simulation, not the packaged PASS log.

## originality

PASS

Best-of-knowledge PASS for the first COMMON-PRIORITY balanced 3-by-3 exact structural and 24/216 incidence classification; neither the founding mechanisms nor welfare comparisons imply this particular exhaustive statement without analysis. Full primary PDFs, relevant tables/examples, corpus aliases and adjacent SCOPE results were compared, not just titles. Novelty is not established by a failed search alone; unindexed course enumerations remain possible.

## value

PASS

This is the exact FIRST balanced unit-capacity preference domain (n=3) where two canonical assignment procedures diverge under uniform strict priority. The local priority conflict predicts each divergence, classifies all 216 profiles, and shows welfare incomparability for every divergent profile. It resolves a meaningful small-domain structural question rather than merely renaming the algorithms or choosing an arbitrary preference slice; it does not need a larger-market asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
