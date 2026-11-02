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

# Reproduction and limits
Run `python verify.py` using Python 3 standard library only. The program constructs matrices of the incidence algebra with explicit multiplication and exhaustively enumerates commuting involutions. It tests two-element and three-element chains, both orientations of a three-point fork, two disjoint two-element chains over \(\mathbb F_3\), and the three-chain over \(\mathbb F_5\). It also evaluates both sides of the random-cluster expansion in 36 parameter cases. The expected terminal line is `VERIFY_OK`.

The finite checks independently recompute concrete instances but do not establish the universal theorem. Universality follows from the projector-and-conjugacy proof in RESULT.md, with the odd-characteristic hypothesis essential. The finite tests use prime fields; the proof covers all odd prime powers. The maximal-clique theorem is proved symbolically by the same conjugation construction and its free action; no exhaustive large-clique classification is claimed from the finite tests. The all-fields Tutte recovery is polynomial interpolation, not a finite experiment. Independent audit has not been performed.
