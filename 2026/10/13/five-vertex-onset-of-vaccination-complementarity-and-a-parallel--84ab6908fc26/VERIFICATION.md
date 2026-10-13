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

# Exact verification and proof boundary

The package includes a standalone Python 3 verifier in `CHECK/verify.py`. Execute `python CHECK/verify.py` using only the standard library. The program enumerates all simple undirected labeled graphs on two to five vertices and all legal two-site mixed differences, validating the general deterministic attachment formula in 83,506 cases and validating the nonnegative bound up to four vertices. It enumerates the 32 independent-edge configurations of the five-cycle, expands their Bernstein weights exactly into ordinary polynomial coefficients \((0,0,2,6,10,-20)\), and checks the exact rational witness \(p=19/20\).

Expected output:

`VERIFY_OK structural_and_small_graph_cases=83506 C5_coefficients=[0, 0, 2, 6, 10, -20] C5_gap_at_19_over_20=-61009/160000`

These finite checks do not certify the all-order forest theorem or arbitrary-edge-probability statement. Those follow from the displayed unique-path identity and pointwise deterministic sign proof in `RESULT.md`. The cubic's root classification follows from its derivative and endpoint signs. No independent external audit has been conducted.
