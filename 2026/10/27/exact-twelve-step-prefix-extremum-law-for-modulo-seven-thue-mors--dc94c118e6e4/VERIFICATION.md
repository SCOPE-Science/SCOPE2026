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

The included `verify.py` uses exact Python integers and no external dependencies. It reconstructs the seven-state triple of totals, prefix maxima and prefix minima by the binary block decomposition, checks all direct prefixes through level sixteen (131071 nonzero positions at the largest tested stage, plus shorter stages), verifies the full coordinatewise depth-seven/depth-nineteen certificate, and checks the stated affine relations at subsequent levels as a supplementary consistency test.

Observed output: `VERIFY_OK: 7-residue integer depth-7/19 certificate, direct 131071-prefix test, 107 further levels`.

The infinite result is certified mathematically by the displayed transition identity, its exact finite base certificate and a twelve-shift induction, not by a heuristic extrapolation of large experiments. Priority risks: the full primary Goldstein–Kelly–Speer (1992) article and Drmota–Skałba (1999/2000) article were not materially available. Independent mathematical audit remains unperformed.
