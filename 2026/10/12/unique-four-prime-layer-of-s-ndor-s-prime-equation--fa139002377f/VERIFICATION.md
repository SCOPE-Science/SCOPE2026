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
The proof was checked algebraically in the stated domain of distinct odd primes \(p<q<r<s\). The two normalized-product bounds are exact rational inequalities; they reduce the least two primes to \((3,5)\) or \((3,7)\). The latter branch is impossible modulo \(3\), while the former reduces to the complete integer factorization \((r-16)(s-16)=235\). The bundled verifier replays these reductions and checks the survivor.

The finite regression scan with the first three primes below \(500\) is auxiliary and is not used to prove the unbounded theorem. No claim is made about the variable-support conjecture for \(r\ge5\).
