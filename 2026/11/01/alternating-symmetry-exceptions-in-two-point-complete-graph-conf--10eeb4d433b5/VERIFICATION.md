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

# Computational and mathematical verification

The standalone `verify.py` uses Python's standard library only. It reconstructs all zero-, one-, and two-cells of the unordered two-point discretized complex of each complete graph for \(2\le m\le6\), its barycentric flag chains, and every element of \(\mathfrak S_m\) and \(\mathfrak A_m\). It determines orbit cells without relying on the written orbit table, verifies incidence and the identity \(\partial^2=0\), computes exact rational boundary ranks, and carries out finite elementary free-face collapses. Its `orbit_certificate.json` contains the explicit incidence and collapse tables and is regenerated in the current directory by running the script.

The expected quotient cell counts are checked programmatically, as are the residual configurations: a one-vertex complex for all symmetric quotients and alternating quotients other than \(m=3,4\), and a pair of parallel edges for each of those two alternating exceptions. There are additional exact rational-coordinate sample checks of the analytic deformation for \(m=3,4,5\), all vertex permutations, and three deformation times; they test particle separation, fixing initial data, target membership at time one, and equivariance.

The uniform statement for \(m\ge6\) is **proved by the four-label stabilizer argument**, not inferred from the finite verifier. Analytic continuity of the deformation on the complement of collisions is demonstrated in RESULT.md; finite rational samples are corroboration, not a proof of infinite-point continuity. The group actions considered are ordinary vertex permutations on unit-length graph edges. Neither a homology classification of the original configuration spaces nor an independent external mathematical audit is claimed.

The recorded local run of `python3 verify.py` completed with `RATIONAL_SAMPLE_EQUIVARIANCE_OK` and `VERIFY_OK`. The text file `verification_output.txt` records that run. It may be reproduced by extracting all embedded files into one directory and executing that command.
