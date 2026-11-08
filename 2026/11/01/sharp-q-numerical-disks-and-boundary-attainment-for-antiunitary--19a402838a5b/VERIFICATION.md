---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

With inner product linear in first variable, y=conjugate(q)x+sqrt(1-r²)z for r<1, z perpendicular to x. For fixed x and f=|<Ax,x>|, dim x-perp>=2 makes <Ax,z> fill the full disk of radius sqrt(1-f²). Thus the fiber max is F_r(f)=rf+sqrt(1-r²)sqrt(1-f²). A complex quadratic isotropic-vector argument yields f=0, and path-connectedness of unit sphere gives all 0<=f<s (including s if attained). Scalar Cauchy-Schwarz yields plateau at f=r for r<s and endpoint f=s otherwise, with exact boundary-attainment condition. Unitary scalar rotation of test pair makes the range circular, connected Stiefel domain plus a zero witness makes it a full disk; r=1 handled as sphere case. Infinite block antiunitaries with s_n increasing to nonattained s_infty exhibit genuinely open boundary. Independent 25 scalar-envelope comparisons confirm optimization but do not replace Hilbert geometry.

## originality

PASS

Best-of-knowledge: Gives a complete radius and topological boundary classification for a canonical operator class and constrained numerical range, including a nontrivial norm plateau and an infinite-dimensional nonattainment transition. These exact data are not fixed by the previously known qualitative disk shape and can matter in operator-range inclusion and extremal norm questions. Prior-art comparison is based on distinct theorem implications. See four structured checks and material source inspections; not exhaustive historical priority.

## value

PASS

Gives a complete radius and topological boundary classification for a canonical operator class and constrained numerical range, including a nontrivial norm plateau and an infinite-dimensional nonattainment transition. These exact data are not fixed by the previously known qualitative disk shape and can matter in operator-range inclusion and extremal norm questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
