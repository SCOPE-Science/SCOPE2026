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

The theorem is verified symbolically by an exhaustive factorization split on \(\Omega(n)\le2\): prime, prime square, or squarefree semiprime. The critical identities \(S(p)=p\), \(S(p^2)=2p\), and \(S(pq)=q\) are proved from prime divisibility of factorials. The only explicit small semiprime boundaries are larger prime factors \(3\) and \(5\); all larger cases are closed by the monotonicity of \(m!/(m^2(m-2)^2)\) for \(m\ge7\).

The bundled `verify.py` independently factors every integer through 200000, computes the Smarandache function from Legendre valuations, and uses exact capped factorial arithmetic. It reports `VERIFY_OK` and exactly the exceptions 2, 3, 6, 15 among 63214 tested integers with \(\Omega(n)\le2\). This finite replay is regression evidence only; it is not used as an infinite proof.

No claim is made for the full exceptional set when \(\Omega(n)\ge3\).
