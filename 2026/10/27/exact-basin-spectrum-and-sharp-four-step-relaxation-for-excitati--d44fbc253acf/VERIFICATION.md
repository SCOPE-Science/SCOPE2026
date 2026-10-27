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

# Verification of the basin-spectrum result

The proof-critical branch analysis is exhausted by `verify.py`: precisely 93 possible hub/initial-support combinations when every blade is nonrainbow, and precisely 27 hub-phase/ordered-wing-pair cases under the forced rotating hub. These finite tables establish the local dynamics for arbitrarily many blades because only the presence or absence of state 1 in the wing types affects the hub. Basin counts partition the total \(3^{2r+1}\) states exactly, including the three hub phases.

The standalone script further enumerates all \(3^{2r+1}\) full states for each \(r=1,2,3,4,5\). Each has the predicted number of cycles and per-cycle basins, exactly one fixed zero state, and the claimed sharp maximum preperiod. The file `verification_output.txt` is the recorded standard output of `python3 verify.py`. These finite graph checks alone are not used as an extrapolation to all \(r\); the proved local reductions supply the universal step.

No claim of externally performed audit, mechanized theorem certification or independent validation is made. Source inspection of the 1991 and 1993 historical full texts was incomplete; general established circulation criteria already imply the binary extinction partition but not the attractor-resolved census proved here.
