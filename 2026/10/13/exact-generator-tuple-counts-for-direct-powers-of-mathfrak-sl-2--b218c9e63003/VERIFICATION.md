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

# Verification scope

Run `python verify.py` using Python 3 without external dependencies. This constructs finite-field multiplication for \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), computes linear spans and iterated Lie brackets directly from \(2\times2\) traceless matrices, and checks the proposed counts.

Exact enumerations yield one-factor generating-pair counts \(24,432,2880,12000\) for field orders \(2,3,4,5\), respectively; full projective-plane counts are \(7,13,21,31\), with \(3,4,5,6\) Lie-closed planes, respectively. One-factor generating-triple counts are \(336\) and \(16848\) for field orders \(2,3\). For odd characteristic the generating-pair automorphism orbits have sizes \(24\) (\(q=3\)) and \(120\) (\(q=5\)); the two-factor counts are \(176256\) and \(142560000\), respectively. The even-characteristic quotient-rank census gives \(5160960\) tuples when \((q,k,r)=(2,2,4)\), zero for \((2,2,2)\) and \((2,2,3)\), and \(2880\) for \((4,1,2)\). The program prints `VERIFY_OK` on completion.

The checks are finite, and do not independently establish the formula for arbitrary prime powers or arbitrary powers and tuple lengths. Those unrestricted claims require the matrix trace/conic argument, Lie Goursat classification, and full-rank quotient argument in RESULT.md. The automorphism-group order is also justified mathematically, not just sampled. No independent external audit or formal proof certificate is asserted.
