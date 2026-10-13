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

The companion script `verify_parity.py` uses Python 3 standard-library exact rationals. Running it gives `EXACT_CERTIFICATE_OK` and independently reconstructs the numerical ingredients used in the proof: 18,058 selected odd valuation vectors, 32,591 selected even vectors, both exact conditional masses, the rational bound obtained from \(\pi<22/7\), and a strict rational moment bound below \(1/70\) over the primes through \(1000\).

The unrestricted result additionally depends on proved, non-computational facts: convergence of the squarefree tail Euler product; the CRT density of prescribed valuations; convergence of the divisor-expanded \(100\)-th moment for the large-prime tail; and Markov's inequality. These deductions are given in RESULT.md. Finite verification is not a substitute for these infinite arguments. Exact limiting parity frequencies and the optimal gap are not computed.
