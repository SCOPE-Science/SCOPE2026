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

# Reproduction

Run `python3 verify.py` with the standard Python 3 interpreter. The verifier exhaustively enumerates unlabeled set partitions by restricted growth sequences for n=2,...,8 and compares exact rational covariances with both general counting identities. It also checks both positive extreme conditioned formulas and unconditional negativity through n=99, and checks normalized Bell log-concavity through n=99. Expected result: `PASS 621 exact assertions; exhaustive set partitions n=2..8; formulas/signs to n=99`.

The proof for all n depends on counting arguments, elementary binary-stratum enumeration and the published Bell inequality; finite checks do not certify those universal steps by themselves. No independent mathematical audit has been performed.
