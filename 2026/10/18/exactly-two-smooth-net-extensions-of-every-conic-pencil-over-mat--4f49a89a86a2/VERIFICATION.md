---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The requirement is that every F3-rational member of the pencil/net be geometrically smooth, not that every member after extension of the parameter space be smooth. The gradient matrix M(Q) is symmetric; Euler's identity in characteristic three identifies singular projective points with its nonzero kernel vectors. Rank does not change over the algebraic closure. The independent replay `python3 /workspace/conic_census.py` uses projective point sets, tests the kernel condition on the 13 projective coordinate points (sufficient by rank invariance), and constructs a pencil from every pair of distinct projective form points u,v as {u,v,[u+v],[u−v]}. It returned (364 projective forms, 234 smooth forms, 11011 total pencils, 1872 smooth pencils). For the displayed F,G, adjoining a projective form w outside the pencil gives the 13 points of the pencil, [w], and the eight [u±w] for u a normalized pencil point. Exhausting all w gave 40 distinct candidates, and exactly the two smooth extensions specified by H_1,H_2. Unlike the frozen generator-orbit scripts, the replay directly visits every ordered independent coordinate frame with normalized first column, exactly one representative per scalar coset (13·24·18=5616), acting by congruence. The orbit of the representative pencil equals the full enumerated set of 1872; the representative extensions have two disjoint 144-element orbits. Conjugating the two-extension result therefore covers all pencils; every smooth net contains at least one such pencil, so no net is missing. The number of pencils in a net is the number of hyperplanes in F3³, namely 13; degrees and incidence total follow. The packaged scripts and expected outputs were inspected, not executed.

## originality

PASS

The supported distinct result is the two smooth extensions of every F3 conic pencil and their partition into two different PGL net types, with an exact census and representatives. The comparable rank-one net classification excludes all-smooth nets, existence/classification of pencils alone is insufficient, and the strongest inspected Resultary incidence comparisons differ in field, degree or extension object. This is not a priority claim for odd-field pencil classification. A full prior all-smooth net orbit census, combined with pencil transitivity, would cover the essential incidence result by immediate double counting; that coverage was not established in the inspected evidence.

## value

PASS

The incidence asks a natural extension question for all-smooth linear systems, motivated by existence and the unique-extension conic case over F2. Over F3 uniform degree two is not a count guessed from isolated examples; the two extensions are genuinely inequivalent as nets and the census is exact. This supplies a reusable finite-geometric invariant and representative systems, without asserting that the incidence graph is classified beyond the stated orbits and degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
