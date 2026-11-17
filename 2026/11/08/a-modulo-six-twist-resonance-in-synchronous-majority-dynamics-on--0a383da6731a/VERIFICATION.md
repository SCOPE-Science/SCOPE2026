---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: For a flipping state, an agreeing rung forces both neighboring rungs to agree and alternate, giving exactly two states when n is even; a disagreeing rung forces all rungs to disagree, first-layer bits to contain no cyclic triple, and a twisted seam to impose complement closure. The explicit 4x4 no-triple transfer H commutes with complement J; its two eigenspace characteristic polynomials yield tr(H^n)=L_n+delta_n and tr(H^n J)=L_n-delta_n. Complement commutation gives exactly Q/2 primitive all-vertex-flipping orbits. Independently enumerated complete microscopic states at n=3,4,5,6 confirm Q pairs (6,2),(8,10),(10,12),(22,18); n>=3 follows from transfer, not enumeration.

## originality

PASS

PASS on the REPAIRED final claim only. A materially inspected November 1 result already proves the entire original fixed/periodic population and primitive-orbit twist sign law, so those were removed from the new claim and explicitly credited. That published proof does not resolve the all-vertex-flipping subpopulation: a total orbit count does not determine what fraction flips every coordinate. The separate complement-twisted no-triple trace proves the remaining Möbius/prism Q-sector. Ordinary cyclic no-triple words are credited to Agur–Fraenkel–Klein, so their known formula is not presented as new.

## value

PASS

PASS: The new Q-sector is a natural distinct dynamical classification of globally synchronized blinking oscillations on canonical cubic graph families; the bounded arithmetic response to a seam twist contrasts sharply with the previously known exponentially large change in the total two-cycle population, and the exact share decays like phi^{-n}. The answer is an all-n exact motivated invariant not determined by the known total census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
