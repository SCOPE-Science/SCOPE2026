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

# Computation and limits

`VERIFY.py` builds the exact eight-neighbour toroidal transition matrix over \(\mathbb F_2\) directly, using one basis bit for each vertex. For every listed circumference pair, it computes all ranks through the first stabilized time by bitwise Gaussian elimination and compares each rank to
\[
16k\ell+8L\max(0,K-t)+2L\max(0,K/2-t)
\]
when \(K\geq2\), and to the separate \(K=1\) formula. It separately checks the nine zero/16 nonzero local eigenvalue frequencies using a two-bit implementation of \(\mathbb F_4\). Test pairs: \((5,5),(5,10),(10,10),(5,20),(10,20),(20,20),(10,40),(20,40),(40,40)\). The largest tested state space is dimension 1600 over \(\mathbb F_2\). Reproduce with `python3 VERIFY.py` in a directory containing the extracted code.

This finite verification neither covers all positive exponents nor certifies historical originality; the infinite-size proof is the Chinese-remainder and local-Jordan basis construction in `RESULT.md`. `VERIFIER_OUTPUT.txt` contains the actual stdout from the packaged program. No independent audit or certification is claimed.
