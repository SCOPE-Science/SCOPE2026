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

# Reproducibility and limitations

Use Python 3 standard library: `python3 verify.py`. The checked script reconstructs exact three-by-three edge heat matrices using rational \(r\) and directly verifies \(T\boldsymbol1=\boldsymbol1\), the nontrivial trace identity, \(\det T=r^3\), the exact discriminant factorization, and the antisymmetry identity at 24 rational nodes. Numeric tests also compare the exceptional-point location and rate to 11 off-optimum parameters. The stated stdout is `VERIFY_OK rational_sweeps=24 phase_boundaries=3 rate_tests=11`.

The proof is algebraic. Finite checks do not establish an inequality for all \(t>0\), the global minimizer, publication priority, finite-iterate mixing behavior, or independent scientific verification. The review covers correctness, originality and value only for the exact uniform three-edge, per-sweep claim. No independent audit has been performed.
