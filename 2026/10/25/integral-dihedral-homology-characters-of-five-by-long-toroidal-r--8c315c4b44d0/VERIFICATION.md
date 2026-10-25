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

# Reproduction and verification

Use Python 3 and the two supplied scripts in the same directory. Execute:

`python3 verify_rips_c5_symmetry.py`

The verifier builds complete inclusive metric flag complexes independently. It checks the ten-vertex block's full face list and 48 explicit elementary collapse pairs; it tests the exact dihedral signed-Lefschetz formula for each of 20 block automorphisms. It then checks full-complex geometric collapses for circumferences 7, 8, 9 and 10 (140, 160, 180 and 200 global elementary pairs), and computes signed face traces independently for all 140, 160 and 180 product actions at circumferences 7, 8 and 9, respectively. All 480 global traces match the theorem.

The theorem for unbounded circumference uses the separately stated uniform spanning-edge link classification and the natural integral Mayer–Vietoris block decomposition. Exhaustive tests at finite sizes are evidence for implementation correctness, not a substitute for this proof.

There has been no independent audit. The provenance of the mathematical claims is restricted to the cited sources and the included reproducibility files.
