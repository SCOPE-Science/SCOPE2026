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

# Executable verification

Run `python3 verify.py` alongside the package's `spectrum.csv`. The program requires only the Python standard library and checks all incoming/outgoing matchings, independent Eulerian tours, every 32-position window at half-lengths 1 through 16, all 71 histogram cells, both symmetry-orbit extremizers, and the rational moments. It also verifies the exact occurrence/distinct-factor difference for orders 1 through 5. The unrestricted difference identity has a symbolic proof in `RESULT.md`; finite checks are not used to extrapolate it.

The finite proof is complete because both generators enumerate every admissible 32-edge tour or all 65536 local matchings, not a random sample. The calculation can be rerun from the embedded source. No external or independent audit has been performed.
