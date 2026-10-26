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

# Reproduction and limits

Run `python3 verify.py` with Python 3 standard library only. It calculates exact integer-coefficient determinants of the seven-state and three-state cyclic-core matrices via Leibniz subset expansion; obtains arbitrary-length traces from Newton identities; independently builds the original sixteen-state twisted transfer and checks agreement through \(n=50\); and enumerates every labeled vertex set directly on \(M_{2n}\) for \(3\le n\le10\). The last line is `VERIFY_OK`. The packaged `verify_output.txt` is a record of that command, not itself a proof.

The unrestricted proof is the algebraic transfer/determinant argument and formal coefficient extraction in `RESULT.md`, not extrapolation from numerical experiments. The determinant expansion is a finite exact calculation with all inputs and verification algorithm present in the packaged code. No external validation or independent mathematical audit has been performed.
