---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

Analytical verification consists of five independent proof steps: shortest-vector basis, construction of orthogonal index-two site superlattice, two-ball lower bound from cup product, covering-density extrema, and inversion-quotient equivalence. Their hypotheses, equalities and endpoint cases are explicit in `RESULT.md`.

Run `python3 checker.py` with the Python standard library. The packaged checker uses exact rational Gram products at \(\cos\theta\in\{-1/2,-2/5,-1/3,0,1/3,2/5,1/2\}\). It checks a finite window of integer lattice vectors, samples a rational grid of torus points, and checks the two farthest points. Expected output: `PASS: 5607 exact-rational vector/sample checks across 7 Gram shapes; max squared distance 1/4.` This diagnostic has been run successfully.

**Limits:** Finite tests do not prove the infinite-lattice minimum, global two-center lower bound, or universal covering radius. The proof of these statements is the reduced-basis argument, the Voronoi rectangle calculation, and the cohomological obstruction. There is no independent audit or outside formal certification.
