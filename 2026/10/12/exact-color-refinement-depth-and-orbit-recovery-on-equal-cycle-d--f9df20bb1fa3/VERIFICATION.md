---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The two attachment vertices are same-colored by the end-interchanging graph automorphism, and all other degree-two vertices lie on threads of lengths m or p between degree-three endpoints in the universal cover. At round r, each thread position has color determined by unordered clipped distances from its endpoints; induction extends one visible edge per round, with degree-three endpoint color as anchor. Same-thread partitions stabilize at floor(L/2). Unequal thread lengths first separate positions near an endpoint at round min(m,p), while equal threads remain identified forever. If p!=m, position up to reflection and thread type exactly describes automorphism orbits; if p=m, connector internal vertices are cut vertices while cycle internal vertices are not, proving orbit mismatch. Independently reimplemented 1-WL and constructed graphs for all 210 pairs 3<=m<=12, 0<=k<=20 and reproduced the depth formula, including 10 resonances. Infinite claim relies on clipped-distance induction, not these samples.

## originality

PASS

Best-of-knowledge original exact stabilized partition and resonance classification for canonical equal-cycle dumbbells. Krebs–Verbitsky establish the general truncated universal-cover interpretation of refinement, while Liu–Lu and Wang et al. study spectral structure of dumbbells, not exact 1-WL depth. Generic covering results do not directly yield the piecewise formula and strict orbit-recovery dichotomy for this family.

## value

PASS

The exceptional equality of cycle and connector lengths yields a clean qualitative phase change where 1-WL fails to recover orbit classes, along with sharp iteration depth for every family parameter. Exact depth and the cutvertex-orbit obstruction are natural graph isomorphism/color-refinement invariants and cannot be replaced by a finite-instance observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
