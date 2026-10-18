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

# Finite verification and proof boundaries

Run `python3 verify_bouquet.py` with any recent Python 3 installation. The program requires only the standard library. On the reviewed inputs it prints `PASS: 4595 exact modular-rank/forcing checks across 50 bouquets`.

The checker builds each unit-edge Laplacian from the literal graph definition; forms the full Kalman block matrix with the proposed independent vertex inputs; computes its rank by exact arithmetic modulo the prime 1000000007; and checks the zero-forcing upper construction plus every smaller initial blue set in the tested cases. Full rank modulo a prime is a sound witness of rational full rank for these integer matrices. Failure of a modular rank test alone would not establish characteristic-zero uncontrollability; none was used to prove the universal statement.

The finite cases include all unordered length pairs from 3 through 10, all unordered triples of lengths from 3 through 5, and four further larger mixed-length configurations. The analytical sine-eigenvector obstruction, Chebyshev recurrence, hub identity, and zero-forcing proof in RESULT.md establish the infinite-range theorem independently. The finite checker does not certify any untested graph or resolve possible antecedents in the literature.
