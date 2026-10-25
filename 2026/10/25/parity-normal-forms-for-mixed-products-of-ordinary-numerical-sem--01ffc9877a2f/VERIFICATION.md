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

# Reproducible verification

Use Python 3 with no third-party packages:

`python3 verify.py`

The script computes the additive numerical semigroup directly from finite products of two factor generating sets (not from the asserted parity normal form), and independently checks membership, gaps, minimal generators and pseudo-Frobenius condition. It verifies every integer parameter from 2 through 160, where the m=2 case is an independent boundary consistency check. On the recorded execution it reported `VERIFY_OK m=2..160 exact DP multiplication, full normal form, Frobenius, genus, minimal generators, pseudo-Frobenius`.

Every finite computation has an explicit bound greater than the proved conductor and the positive generators used in pseudo-Frobenius testing. The numerical data cannot certify the theorem for unbounded m; the self-contained parity proof in `RESULT.md` supplies that argument. No independent mathematical audit or independent validation has been performed.
