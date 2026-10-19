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

# Verification record

The proof is algebraic and exact. Under \(a,c>0\), \(b>a\), the projective first integral, inverse-ratio quadrature, beta substitution, convergence at infinity, beta-tail expansion, and origin/explosion endpoint limits are established in RESULT.md. No claim of exhaustive numerical verification or external certification is made.

Execute `python3 verify.py` using only Python standard-library modules. The program checks 51 independent finite diagnostics on five rate triples, including rational differentiated identities, an incomplete-beta numerical quadrature comparison with a separate Simpson integral, small-distance finite-part diagnostics, and the coefficient at rates \((1,2,1)\). Its expected success line is `VERIFIED 51 finite rational/analytic/numerical diagnostics`.

Finite numerical experiments do not establish assertions quantified over all real positive rates or all initial conditions. Those statements depend on the exact proof, not the script. Bibliographic priority outside inspected sources remains unverified; the independent audit is not performed.
