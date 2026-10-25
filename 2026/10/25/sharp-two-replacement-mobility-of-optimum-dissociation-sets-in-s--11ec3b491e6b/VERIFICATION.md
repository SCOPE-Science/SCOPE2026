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

# Verification record

The accompanying `verify_rook.py` independently enumerates configurations from center assignments and tests two-replacement adjacency by direct common-subset hashing. The accompanying `verify_rook_independent.py` generates the states by an exact cover of the original row/column vertices by two-edge stars and builds adjacencies from explicit legal local transformations.

Each program is standalone Python 3 using only its standard library. Run `python verify_rook.py` and `python verify_rook_independent.py` in the extracted directory. The recorded outputs are included in corresponding `.out` files; replayed outputs must match as UTF-8 bytes.

For board sizes three and six, both programs give respectively nine and 8,100 optimal states, degrees four and 24, and a single two-replacement connected component. The independent script also brute-forces every subset on three- and four-by-four boards, checking maximum size four and five respectively. A finite check does not prove the infinite statement. The proof in `RESULT.md` is the basis for all quantified conclusions; no independent audit was performed.
