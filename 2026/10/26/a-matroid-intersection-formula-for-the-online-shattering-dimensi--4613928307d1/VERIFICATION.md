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

Static coordinate shattering iff F is independent in M and its dual: all-ones and all-zeros give necessity; given basis B0 disjoint F and independent subpattern I, augmentation extends I inside B0∪I to a full basis, realizing exactly I. Edmonds matroid intersection theorem gives ν(M)=m-R+min_A φ(A), φ=2r(A)-|A|. For e neither loop nor coloop, applying dual rank to M\e and M/e separately gives ν_del=m-R-1+min_{A:e∉A}φ(A) and ν_contr=m-R-1+min_{A:e∈A}φ(A). Their minimum is exactly ν(M)-1, since domains partition 2^E. Induction on the first query bounds Littlestone depth by ν; fixed VC-shattered F gives lower bound, hence equality including all edge cases. Graphic dual independence equivalent to G\F connected. Independent direct version-space recursion matched VC and Ldim for uniform and partition matroids of size up to seven; no extrapolation from finite tests is used.

## originality

PASS

Matroid intersection min-max and general Ldim branching are classical; the proposed connection is that all basis-incidence concept classes, even nonrepresentable, have equality of static and adaptive shattering, and a stronger exactly-one-decrement minor dichotomy. Compared general learning and matroid-basis enumeration works do not state this in inspected passages. Priority risk remains for unindexed general theorem about greedoids or matroid concept classes.

## value

PASS

A natural rich class of concepts where adaptivity unexpectedly cannot increase shattering complexity, with an exact primal/dual rank minimization and polynomial oracle algorithm for optimum online mistake bound. Graphic specialization yields a meaningful forest-with-connected-complement invariant rather than a one-off example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
