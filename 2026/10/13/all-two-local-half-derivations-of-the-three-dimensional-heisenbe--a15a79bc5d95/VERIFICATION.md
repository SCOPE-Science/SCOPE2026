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

# Reproduction and limits

With Python 3 standard library, execute `python3 verify.py` in the same directory. The script checks the six-parameter half-derivation matrices against the defining bracket identity on every basis pair at \(q=3,5\), giving \(729\) and \(15625\) distinct operators, respectively. It tests \(26460\) random-map interpolation conditions at \(q=3\) and \(78750\) at \(q=5\), exhausts every ordered pair for an explicit linear two-local non-half-derivation and a nonlinear example, rejects a map whose quotient output incorrectly depends on the central coordinate, and checks projective direction counts \(q+1\) and \(q^2+q+1\). Successful execution prints `VERIFY_OK`.

The code is finite testing of specific properties, not an exhaustive enumeration of nonlinear functions and not a proof for arbitrary fields. The algebraic necessity/sufficiency proof in RESULT.md supplies that part, while projective-line counting proves the exact full census without enumerating all maps. Only \(\operatorname{char}K\ne2\) is considered; no external independent audit has been performed.
