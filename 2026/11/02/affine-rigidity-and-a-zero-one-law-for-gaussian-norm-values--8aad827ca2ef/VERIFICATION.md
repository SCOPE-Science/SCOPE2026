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

# Reproducible checks and boundaries

The companion standard-library program `verify_affine_norms.py` enumerates all ordered residues modulo each squared prime for fourteen parameter combinations at primes 3, 7, 11 and 19. Its checks include the exact count `q*(q*q-1)` and the exact intersection of the two valuation-one conditions at `a=b=1` on all 194481 pairs modulo 441. The source records `VERIFY_OK local_q_cases= 14 CRT_exact_pairs= 194481 direct_affine_witnesses=6`; the individual witness and zero-intercept checks are ancillary, not part of the positive-shift density claim.

The finite tests check only the specified parameters. The proof in `RESULT.md` establishes the general local count and the lattice-box limit; it makes no assertion about primitive sums, density among distinct values, or quantitative rates.
