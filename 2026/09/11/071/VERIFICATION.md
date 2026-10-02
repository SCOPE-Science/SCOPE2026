---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

An independent reconstruction of all normalized points and lines of PG(2,13) gives exactly 183 of each. Recomputing incidence for the 24 stated points gives secant histogram {1:99,2:43,3:25,4:11,5:2,6:1,7:1,9:1}, hence zero uncovered lines, zero 14-secants, maximum secant 9 and zero 11-secants. Every one of the 24 points has at least three tangent lines, proving minimality. Thus the explicit set is a minimal nontrivial non-Redei blocking set of size 24.

## originality

PASS

Meaningful searches found earlier PG(2,13) non-Redei examples at size 21 and a 2005 Danielsson thesis/seminar report of an unspecified minimal size-24 blocking set, but no source stating a size-24 non-Redei/no-11-secant example. Resultary likewise found only SCOPE071 for the exact non-Redei size-24 property, alongside a distinct SCOPE040 size-24 Redei example.

## value

PASS

Size 24 lies below the general Desarguesian interval beginning at 2q-1=25, and distinguishing a size-24 example as non-Redei is a natural secant-structure refinement in the small minimal-blocking-set spectrum. The explicit finite witness and full secant distribution give a reusable classification datum rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
