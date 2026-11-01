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

# Verification notes

The included `checks/return_map_verify.py` was executed from its actual package file path. It asserts the exact periodicity relation for five restitution values and six distinct flight lengths per value, with positive outgoing and negative incoming velocities. It obtains the restitution-\(0.8\) fold at \(r_*\approx0.6049417558076354\), reproduces the two \(r=0.8\) periods \(u_-\approx0.296942404795\) and \(u_+\approx5.352910578597\), and observes respective return-map multipliers above and below one. It tests the critical map coefficient \(\sqrt6/8\) and the large-impact limits through 30,000 collisions; at 30,000 iterations the dimensionless squared-speed quantity is about \(42.5492\), approaching \(128/3\approx42.6667\), while \(nT_n/\tau\) is about \(15.9790\), approaching \(16\).

Run `python checks/return_map_verify.py` from the extraction root to reproduce. The code is a finite numerical consistency check using Python's standard library. The proof of uniqueness, the no-other-periods statement, the exact cusp, and the infinite-impact asymptotics require the analytic arguments in `RESULT.md`. Inaccessible auxiliary publication material and independent validation remain outside the present evidence.
