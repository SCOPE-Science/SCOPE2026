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

# Direct verification and limitations

The complete incidence checker enumerates 21 points, 21 lines, 54264 six-subsets and 2520 valid four-arcs; it checks unique completion, every pairwise intersection, every common-neighbor count and the all-pairs distance profile. The independent projective-orbit checker generates 168 distinct hyperovals from a canonical conic-plus-nucleus and projective-linear generators, then independently recomputes the exchange graph and the exact common-neighbor table. Run `python3 direct_incidence.py` and `python3 projective_orbit.py` with Python 3 and no third-party libraries. Both were actually executed successfully before recording these results. The finite exhaustive proof does not generalize to other projective planes. No independent audit is claimed.
