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

The general proof is contained in `RESULT.md`. It uses exact finite character-group and root-of-unity arguments, with no numerical premise.

Run the companion `verify.py` using Python 3 with the standard library. It independently builds the doubling cycles and all real-compatible Fourier solutions for cyclic orders \(1,3,5,7,9,11,13\), performs inverse transforms, checks reality and the original bilinear idempotent equation, builds each real right-multiplication matrix, and compares its characteristic polynomial to the symbolic product formula. It separately enumerates all \(512\) real idempotents for the noncyclic group \((\mathbb Z/3\mathbb Z)^2\).

The check returned `VERIFY_OK`. Cyclic real totals were \(2,8,12,16,80,68,132\) respectively, with complex totals \(2^m\) for order \(m\). The noncyclic nine-element case returned \(512\) real solutions. Finite numerical checks use explicit tolerance bounds and cannot certify the arbitrary-group theorem or literature originality. Independent external audit has not been performed.
