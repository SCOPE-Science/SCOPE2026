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

Every side updates a color 0,1,2 via a deterministic map depending only on whether the opposite side contains an excited color 1. Consequently the ordered pair of nonempty color supports maps to another such pair in a finite 7x7 quotient independently of a,b. Enumerating the 49 transitions yields only closed support configurations: both-zero fixed, both-full supports with actual period three, and a two-support alternating class with actual period four; all other pairs have first-entry depth <=4. Within each closed class the vertex-level map is a permutation on colors, so macro periodicity and actual microperiod coincide after checking these classes. For side size a, the counts of assignments to exactly one/two/three named colors are 1, 2^a-2 and 3^a-3*2^a+3, respectively. Summing products over the 49 support cases gives the ten displayed polynomial formulas, their sum exactly 3^{a+b}, and cycles of lengths three and four counted by their periodic states. A completely separate enumeration of all 49 quotient types and symbolic formulas and all 810 labelled states for a,b in {(2,2),(3,3)} was completed; uniformity rests on exact support factorization, not sampling.

## originality

PASS

Qualified best-of-knowledge original contribution: A four-step relaxation law and complete orbit-depth census for bipartite excitable dynamics. Closest prior work and limits are compared by implication, not title; priority risk retained.

## value

PASS

On a canonical dense bipartite graph family, the full labelled basin census is a natural quantitative invariant of excitable dynamics. The 49-support reduction yields an all-size exact relaxation horizon, a classification by both first periodic-entry time and eventual period, and exact dynamical zeta functions. This complete parametric classification is useful independently of the well-known eventual activity criterion and is not arbitrary small-size experimentation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
