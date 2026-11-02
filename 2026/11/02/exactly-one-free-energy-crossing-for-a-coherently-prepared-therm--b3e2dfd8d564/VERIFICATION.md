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

# Verification of the free-energy crossing theorem

The proof uses the explicit thermal Davies Bloch solution, the exact identity for squared radii and the resolvent representation of the derivative of binary entropy. Every derivative sign and endpoint limit is analytic. The validity includes pure initial states by continuity for positive evolution time; it does not extend to the zero-temperature endpoint.

Run `python check.py` with `sympy`, `numpy`, `scipy` and `mpmath` installed. A successful run prints the total exact and numerical diagnostics and the high-precision root. The source runs standalone without remote services. It first checks the radius polynomial identities using exact symbolic simplification, then assembles the physical Lindblad superoperator as an independent four-dimensional linear operator and compares matrix relative entropies against the explicit formula. It checks the monotonicity shape on finite parameter grids and verifies a 40-digit root for a specified mixed state. All finite tests merely support the analytic argument and do not certify literature originality or proof completeness independently.

The numerical witness uses \(b=1/2\), \(R=4/5\), \(z=0\), \(\Gamma=1\), corresponding to positive rates \(\gamma_-=3/4\) and \(\gamma_+=1/4\). Its crossing is between \(p=0.4\) and \(p=0.5\) with \(p\approx0.4299317297264721\). The normalization monotonicity and strict endpoint signs imply uniqueness without numerical root extrapolation.

The comparison to published papers is limited to the named primary sources and mathematical-record searches. The distinct result has received self-review only; independent scientific audit is not yet performed.
