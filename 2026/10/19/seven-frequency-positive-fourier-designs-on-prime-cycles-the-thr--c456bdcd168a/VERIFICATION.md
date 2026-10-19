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

# Reproduction

Execute `python3 verify.py` in a Python 3 environment. No external Python packages, network connections, downloaded tables, or other artifacts are required. This checker is part of the research package.

The complete run returned:

`VERIFY_OK exact rational pi/Taylor enclosures, interval Gaussian elimination, all 330 supports via 20 dihedral orbits`

The program constructs rigorous rational upper and lower bounds for \(\pi\) using Machin's identity and alternating arctangent series, then checks rigorous Taylor enclosures for all required sines and cosines. Each matrix entry is enclosed by directed integer fixed-point intervals; Gaussian elimination uses lower-rounded and upper-rounded exact integer/Fraction arithmetic. Every pivot interval is shown to avoid zero. For all twenty dihedral representatives, it certifies every feasible weight above \(1/25\), or provides an infeasible weight below \(-1/25\). The separate Burnside orbit-count identity appears in the proof, making exhaustiveness transparent.

The general prime-order lower bound uses the published Chebotarev theorem and existence uses Carathéodory. Finite enumeration does not certify results for other primes. Positivity depends on allowing individual adjustable weights; equal-weight requirements are outside the claim. No independent audit of either the analytic proof or the finite certificate has been performed.
