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

The accompanying `verify.py` computes exact unsigned Stirling rows from the recurrence \(\bigl[{n\atop k}\bigr]=\bigl[{n-1\atop k-1}\bigr]+(n-1)\bigl[{n-1\atop k}\bigr]\). It directly calculates the gcd filtration, identifies the prime-threshold active positions, and checks the deterministic inequality for every \(4\le n\le100\). For smaller indices it also tests minimality of individual active generators with exact residue shortest paths; no infinite minimality result is claimed or used. Run using `python3 verify.py`. The observed response was `VERIFY_OK`.

The infinite theorem is certified only by the written argument, not by the finite script: it uses the supplied exact gcd theorem, elementary prime-power congruence bounds, prime reciprocal asymptotics, and a CRT moment proof. The distributional limit is a self-review analytical assessment, not independently audited.
