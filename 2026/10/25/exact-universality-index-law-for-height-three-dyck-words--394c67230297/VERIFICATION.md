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

Run `python3 verify.py` with Python 3 (standard library only). The script checks the twelve-state transfer and the full polynomial identity through word length twenty. By the stated determinant degree bound, the resulting degree-twenty finite certificate proves the rational equality globally. It then separately enumerates every Dyck word of semilength at most ten and compares the full index histograms; up to eight it explicitly checks all subsequences of each predicted universe length and constructs a missing subsequence of the next length. The independent finite checks are not substituted for the algebraic proof.

The limiting density follows from the unique smallest-modulus simple pole of the resulting rational series, uniform under a complex neighborhood of the probability marker. The variance bound is analytic, not experimentally estimated.

No independent audit is asserted.
