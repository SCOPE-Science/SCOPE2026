---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For 3<=m<=n and 0<=t<=m, any color shared between the bipartition parts must lie on one deleted pair; two different shared colors force m=n=t=3, giving exactly 6 isolated 3-colorings. All no-shared-colorings split into three n-cubes and three m-cubes meeting at the 6 pure corners; each deleted edge contributes six degree-two ears closing squares at the same junctions and no ear-ear edges. Removing an ear excursion reroutes through its junction with unchanged length. A circular coordinate of circumference 3(m+n), alternating 6 cube lengths, gives sharp eccentricity floor(3(m+n)/2), parity and odd-girth 3(m+n); square ears preserve these via first/last-step substitutions. I independently enumerated all proper colorings and one-vertex transitions at (m,n,t)=(3,3,0),(3,3,1),(3,3,2),(3,3,3),(3,4,0),(3,4,1),(3,4,3): verified order and edge formulas, all eccentricities in ordinary cases, and 60+6 isolated states at the exception. Both verify_direct.py and verify_constructive.py source were inspected. Finite samples do not replace general structural proof.

## originality

PASS

The substantive claimed result was compared at the level of mathematical objects, exact implications and limitations against same-family primary results, general theorems and Resultary; accepted as best-of-knowledge, with identified prior components and explicit residual risks, not an assertion of exhaustive historical priority.

## value

PASS

A complete named-color reconfiguration graph, metric, odd girth and a sharp exceptional six-cycle for an infinite family of crown-like matching deletions are meaningful exact invariants; multiple deleted edges could in principle introduce new interactions, and the theorem proves they do not except at one precise boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
