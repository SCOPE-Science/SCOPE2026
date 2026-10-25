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

The executable file `heawood_conf2_verify.py` requires Python 3.10+ and SymPy. Run it with `python heawood_conf2_verify.py`; its output must exactly equal the accompanying `heawood_conf2_verify_output.txt` and end in `VERIFY_OK`.

It enumerates the 14-vertex incidence graph and 168 Fano collineations; builds all cubical cells and the two signed integer boundaries; checks boundary composition; calculates Smith diagonal invariant factors, three finite-field boundary ranks and the sum-of-trajectories rank; computes signed cellular Lefschetz characters; and independently restricts every group element to a basis for the top homology kernel modulo 101.

The rank and Smith checks prove integral ordinary homology. The group-character calculation determines the rational representation by comparison with the classical character table. Mod-101 restrictions corroborate small integer traces but do not replace the integral Smith computation. The verifier checks only the specified finite complex and action, not originality, a full-group representation, or external validation.
