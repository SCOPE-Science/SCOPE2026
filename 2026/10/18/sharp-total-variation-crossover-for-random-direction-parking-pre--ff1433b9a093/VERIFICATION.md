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

# Reproducible checks and analytical limits

Execute `python3 verify.py` in the extracted package root. Python 3 standard library is the only dependency. The verifier constructs the Abel--Cayley weights with exact rational arithmetic for \(2\le n\le24\), tests probability normalization and parameter-reflection symmetry, and independently enumerates every preference vector and its weighted parking branches for \(n=2,3,4\) at five rational direction parameters. It also checks convergence trends at \(n=200,1000,5000,20000\) for the critical-window parameters \(t=0,1/2,1,2\) and the endpoint fixed bias \(p=1\). The reported run passed 704 assertions.

The exact finite conditional identity is grounded in Theorem 3 of arXiv:2211.00536. The universal infinite-size theorem is proved analytically: Borel-progeny factorization, Stirling limits, absolute domination at both boundaries, compact-interior Riemann convergence, and explicit integration. A finite sample, however large, is not a certificate for the infinite theorem. Historical novelty and mathematical correctness have not been assessed by an independent reviewer.
