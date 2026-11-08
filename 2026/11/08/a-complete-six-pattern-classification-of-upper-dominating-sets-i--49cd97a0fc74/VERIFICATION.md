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
# Verification

Execute `python3 artifacts/verify.py` using Python 3 (standard library only). The script checks the private-neighbor local predicate against separate vertex-level enumeration, builds all \(625\) possible four-code states, establishes \(f_7=f_9\) and \(f_8=f_{10}\) across all reachable states, enumerates the finite optimal-prefix automaton, and checks that every accepted zero-excess endpoint lies in one of the six listed periodic templates (with the required even-length restriction). It also checks all size-\(n\) subsets independently for \(2\le n\le10\).

Expected terminal statements: `TROPICAL_PERIOD_2_CERTIFICATE_OK`, `INFINITE_OPTIMAL_LANGUAGE_INCLUSION_OK`, `DIRECT_ALL_SIZE_N_OK`, `TEMPLATE_LOCAL_PERIOD_BOUNDARIES_OK`, and `VERIFY_OK`. The finite closure plus deterministic recurrence is an infinite proof step; the direct small-graph census is additional corroboration. No external validation has been performed.
