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

# Reproducibility and exact-check limits

Execute the embedded standalone Python 3 script `verify.py`. It reconstructs the power-residue histogram modulo \(2^r\) without using the theorem's group argument, calculates the circular self-convolution for all residues, and compares it to the claimed closed recursion. It tests exponents \(4,6,8,10,12,14,20\) and \(1\le r\le10\) and also uses direct ordered-pair enumeration for smaller cases. The test checks total mass and all listed fibers, including singular even-even cases.

The proof for unrestricted \(k,r\) rests on the exact structure of the dyadic unit group and a parity case decomposition. Finite checks alone cannot certify an infinite theorem. No independent scientific verification has been performed.
