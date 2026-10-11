---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The 32 evaluation columns collapse projectively to 16 types of multiplicity two. A 3-subcode can vanish on at most eight types because its annihilator has dimension seven and no nine-subset has rank at most seven. Exact enumeration finds 750 eight-subsets of rank seven and no rank≤7 nine-subset; each such eight-subset has a unique three-dimensional annihilator and hence gives one minimizer. The independently inspected verifier constructs all 1920 natural group actions and obtains orbit sizes 10,20,240,480; a fresh replay reproduced 750, zero bad nine-subsets and the same four orbit sizes.

## originality

PASS

Carvalho–López–San-José’s primary paper isolates the exact ternary torus example and reports d3=16 using a generalized-Hamming-weight package, while explicitly noting failure of the footprint lower bound. The full primary PDF page for the example was materially inspected. It does not count the minimizing subcodes or classify their symmetry orbits. Patanker–Singh’s exact third-weight regimes exclude the boundary m=5=2d+1, and earlier square-free evaluation-code work treats the first and second generalized weights. Resultary search found no covering minimizer census.

## value

PASS

The source itself highlights this boundary example because its footprint bound is nonsharp. Classifying every minimizer and its natural symmetry orbits turns a package-only scalar computation into an exact finite geometric description useful for understanding why the boundary behaves differently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
