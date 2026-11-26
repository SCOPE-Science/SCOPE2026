---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope of verification

Execute `python3 check.py` with SymPy installed. The script constructs the incidence matrices and projections over exact rationals, obtains the two Green functions, compares the absolute row sums, and tests the strict Möbius-versus-prism inequality at each size from three through twelve. It also checks ancillary single-graph identities outside the comparative finding.

The all-size inequality and the two parity-dependent gap asymptotics are proved in `RESULT.md`, not inferred from the finite check.
