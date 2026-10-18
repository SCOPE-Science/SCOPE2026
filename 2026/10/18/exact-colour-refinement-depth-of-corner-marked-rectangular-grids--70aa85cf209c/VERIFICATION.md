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

Run `python3 verify_direct.py` and `python3 verify_algebra.py` using Python 3's standard library. Both run without input files or third-party packages.

The first constructs explicit undirected grid adjacency arrays, runs synchronous counting colour refinement until colour class counts cease to grow, and checks exactly \(R(m,n)=n+\lfloor m/2\rfloor-2\) iterations and the claimed corner-fixing automorphism orbits. It covers 345 pairs with \(2\le m\le16\) and \(m\le n\le31\).

The second does not construct any graph: it checks the path-boundary formal power series coefficients and their separation of reflection classes, the reversal-coefficient inequality outside four small cases, the root-geodesic binomial distinctness up to the proposed depth, and a sharpness witness. It covers 912 pairs with \(2\le m\le33\) and \(m\le n\le45\).

Expected terminal lines appear in `direct_output.txt` and `algebra_output.txt`. These are finite corroborating checks, not a machine proof of the universal result; the universal argument is given in `RESULT.md`. No independent scientific audit has been performed.
