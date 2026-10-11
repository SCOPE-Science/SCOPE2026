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

The proof in `RESULT.md` is analytic: it reconstructs all vertices, evaluates the gauge, enumerates feasible illuminated vertex types using strict supporting-facet inequalities, proves each source cost exceeds its illuminated vertex count, and supplies near-boundary radial sources for the matching infimum. Every dimension \(d\ge3\) is handled without invoking numerical enumeration.

To replay supplementary computations in this directory, run `python3 verify.py`. The Python standard library suffices. It checks facet incidences, vertex membership, and radial illumination, then tests the per-source inequality on \(8452\) integer sources in dimensions \(3\) through \(6\) with exact arithmetic. Expected output begins `VERIFY_OK 8452`. These checks are finite diagnostics; they do not independently certify the universal theorem.

The source comparison uses complete lawful open-access papers by Kiss--de Wet (2012), Bezdek--Litvak (2011 preprint), and Bezdek--Khan (2016 preprint). An independent scientific audit has not been performed.
