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
# Verification and scope

Run `python3 reflection_gap_verify.py` using a standard Python 3 installation. The script independently generates numerical semigroups from the known generators, enumerates semigroup membership, and checks the predicted gaps and isolated gaps for genus 1 through 100; then independently checks the arithmetic tail formula and exact means for genus 2 through 1200. All tests passed: 4,668 complete parameter pairs, 1,199 finite genus profiles, and 467,488 tail-level checks.

These computations are finite corroboration only. The proof for every genus depends on the published characterization of reflective semigroups, elementary neighbor arguments, floor-count identities, and standard divisor bounds. No external or independent mathematical audit has been performed.
