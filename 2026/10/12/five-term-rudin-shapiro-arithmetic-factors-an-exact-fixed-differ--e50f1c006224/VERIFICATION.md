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
# Verification

Run `python3 verify.py` using Python 3.8 or newer. No external dependencies are used.

The verifier reconstructs the binary-addition and adjacent-one-parity transition algebra for five samples, starting from zero carries, zero previous-digit bits, and zero relative parities. It reaches 864 states, computes all possible terminal signatures after the prescribed difference digits have finished by a least fixed point, and projects away the starting-position digits by exact subset determinization. It finds 1302 determinized states, establishes an invariant partition into classes of sizes 2, 13, and 1287 according to whether the prescribed difference contains zero, one, or at least two ones, and checks both transitions and each state's output mask.

The respective terminal masks are `0x0001`, `0xff96`, and `0xffff`. Four signatures are omitted from the middle class; the mathematical argument that every relative signature admits either initial bit doubles these into the eight excluded five-bit words in `RESULT.md`. The final regression check enumerates a direct finite prefix for differences 1 through 128 and matches all predicted exceptional/full spectra. The infinite theorem depends on exhaustive finite-state transition closure, not the prefix check.
