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

# Executable and deductive verification

Run `python oct_mycielski_verifier.py` using Python 3 standard library. The program creates each graph from the explicit edge lists, compares two independent bipartiteness algorithms on all deletions of sizes zero through three for every odd graph parameter from three through twenty-five, compares all optimal deletion sets against the claimed patterns, and computes full exchange graphs with shortest paths for the five named parameters. The out-of-scope three-cycle is tested separately as a boundary. Success prints `VERIFY_OK`.

The universal result is established by the apex-deletion and forced-color proofs, the odd-cycle and independence obstructions, and the explicit exchange-distance count. The finite checks do not certify a theorem beyond their tested range or a claim of novelty. Publicly accessible literature and research records were consulted for comparison, without claiming that absence from them proves novelty. Independent audit has not been performed.
