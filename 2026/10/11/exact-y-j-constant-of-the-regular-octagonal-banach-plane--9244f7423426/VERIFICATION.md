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
The exact verifier represents each coefficient as \(a+b\sqrt2\) with rational \(a,b\). It enumerates active support facets for \(x\), \(y\), and \(x+y\), adds each possible fourth active support inequality to obtain every segment endpoint, solves the resulting linear systems exactly, rejects candidates violating any support inequality, and evaluates every support functional of \(x-y\).

The packaged replay must report `VERIFY_OK`, ninety-six feasible active systems, forty-eight distinct vertices, and maximum `2*sqrt(2)-1`. The explicit maximizing pair is checked independently inside the script. The verification proves only the displayed finite-dimensional polyhedral optimization; it does not certify any broader family of norms or any literature-novelty claim.
