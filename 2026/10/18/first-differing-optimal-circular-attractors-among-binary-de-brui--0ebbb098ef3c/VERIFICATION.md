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

Run `python3 verify.py` with Python 3.8 or later; no third-party modules are used. Its input is two fixed 64-digit hexadecimal cycle descriptions. It verifies all 256 distinct cyclic eight-windows for each, checks the 32- and 33-position covering witnesses, and checks eight seven-bit lower-bound obstruction factors with their two occurrence starts. For orders one, two and four it enumerates every canonical balanced binary candidate: 16 order-four de Bruijn necklaces among 495 candidates.

The analytical lower bound \(\gamma_{\mathrm{circ}}\ge\lceil 2^k/k\rceil\), together with the rigidity of equality when \(k\mid 2^k\), is proved in `RESULT.md`. The finite checker does not rely on a heuristic search for minimum attractors or extrapolate beyond the stated orders. The captured output is in `verification_output.txt` and should be reproduced exactly by the command above.

Independent scientific auditing and external verification have not been performed. The claim does not classify order-eight cycles generally or address the linear-unfolding conjecture.
