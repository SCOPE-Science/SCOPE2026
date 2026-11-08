---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed all six unordered effective bond states with three p-probability tree edges and three g-probability nonlocal edges. Conditional on occupied edge set E, uniform seed size-j probability equals (1/4)sum_components |C| 1{|C|=j}. The distinct star-minus-path coefficient table has six nonzero (k,l) entries at (0,2),(2,0),(1,1),(0,3),(2,1),(1,2). Their weighted sum is (1-p)(p-g)^2*(1,-4(1-g),3,-4g), divided by four. Multiplying by j,j^2,j^3 yields K(1-4g)/2, 3K(1-4g), K(25/2-56g). When 0<g,r<1, K=(1-g)^3(1-r)r^2>0; g=1/4 gives moment alias and third-moment gap -3K/2. Independent separate 64-configuration and 512-opportunity enumerations with exact rational parameters were read; independent_checks.py reconstructs the table and representative endpoints. Four sites are first with nonisomorphic local trees.

## originality

PASS

The finite exact four-site law and universal 1/4 mean crossover are not supplied by the inspected standard two-level-mixing epidemic or percolation framework theorems. General finite graph reliability techniques offer computational derivations, not an identified earlier assertion of the full comparison or simultaneous moment alias.

## value

PASS

This is the minimal population order allowing two nonisomorphic connected spanning trees. It produces an exact parameter-independent ranking reversal, and a nontrivial moment-information alias while the full outbreak probabilities stay distinct. Mean outbreak risk and complete infection probability disagree in a natural mixed-contact model; the exact finite benchmark has independent mathematical usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
