---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Tight-edge incidence rank plus bipartition parity make all surviving graph edges tight at each polar vertex. Every removed matched pair has graph distance three and a potential difference of magnitude either 1 or 3; if all are 1, extension to K_{p,q} forces the classical constant-one-part binary families of sizes 2^p and 2^q with two common functions. If a deleted pair x_i,y_i has a gap three, its endpoints can be set to 0,3; each remaining cross edge forces all other X heights 2 and Y heights 1 (p,q>=3), generating exactly two signed exceptional facets for that pair and excluding simultaneous other gaps. The group preserves the two parts or swaps them when p=q, permuting matched and unmatched members separately. In each binary family counts (j,l) are identified only with (k-j,s-k-l), and Burnside plus the shared constant and exceptional orbits gives the displayed formula and binomial orbit sizes. An independently written spanning-tree enumerator verified (p,q,k)=(3,3,0),(3,3,3),(3,4,2),(4,5,3),(5,5,5), with total facets 14,20,26,52,72 and exception counts 0,6,4,6,10; no finite bound was mistaken for universal proof.

## originality

PASS

The complete bipartite k=0 formula and its two constant-family normals belong to Higashitani–Jochemko–Michałek; the balanced fully deleted crown special case has known diameter-three gap patterns and some facet geometry. The asserted additional object is the all-(p,q,k) rectangular partial-deletion rigidity, exact per-edge additivity and full sign/automorphism orbit multiplicities, not those prior corner cases.

## value

PASS

Deleting a matching is a natural controlled structural perturbation of a complete-bipartite metric. The unexpected exact additivity of only two new facets per removed edge, coupled with all-parameter orbit-size classification, is a useful graph-polytope invariant, rather than a tiny isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
