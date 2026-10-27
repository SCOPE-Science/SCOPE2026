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

# Mathematical verification

The argument in `RESULT.md` proves the exact operator identities for all \(N\) in their stated domains. Finite checks serve only as falsification tests:

- `python3 check.py` runs an exact-integer Walsh-transform test for \(N=3,5,7,9\), requiring no third-party dependencies. It compares the **whole** integer matrix of \((DW)^3\) against \(2^{(3N-1)/2}(P_z+P_x)\) using each basis column.
- Independently, dense complex matrices for \(N=2\) to \(7\) satisfy their respective Pauli-power identities with maximum absolute entrywise error below \(3\cdot10^{-15}\).
- The theoretical parity argument fixes the original (not merely projective) operator order. The finite checker cannot prove a general statement by itself.

Full-text comparison of a related late-2024 follow-up was unavailable. An independent audit has not been performed.
