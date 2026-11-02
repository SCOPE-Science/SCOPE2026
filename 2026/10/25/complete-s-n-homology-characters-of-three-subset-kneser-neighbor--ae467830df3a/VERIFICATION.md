---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For a face of the ordinary open-neighborhood complex, the union of its three-subset vertices omits at least three labels. An invariant face is a union of triple-orbits; alternating orientation contribution equals (-1)^{number of selected orbits+1}. Boolean Möbius inversion over the label cycles gives exact-support contribution (-1)^{cycle_count}(1-a-b+binom(a,2)). Removing supports missing <=2 labels yields Q(a,b), and degree n-6 concentration by Nilakantan–Singh converts the reduced Lefschetz trace to the claimed character. The character-binomial basis has zero signed/unsigned average when n>=6, giving both quotients rational acyclicity. Independently implemented a distinct orbit-mask dynamic program over all 48 cycle-type cases for n=6..8, agreeing exactly. Finite checks do not prove the all-n assertion.

## originality

PASS

Nilakantan and Singh establish the same open-neighborhood graph family and sphere-wedge ranks but not the full coordinate-permutation homology character. The actual trace polynomial and absence of both one-dimensional constituents refine those theorems. Published six-point two-subset KG(6,2) symmetry work concerns k=2, not k=3. Priority is qualified by possible unindexed equivariant formulations.

## value

PASS

The full rational S_n-module character is a natural symmetry invariant of a standard Kneser-neighborhood family, determines every conjugacy-class trace and two meaningful quotient homology consequences, and is not determined by the prior rank. No integral module or new nonequivariant homotopy is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
