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
Run `python3 verify.py`.

The checker constructs Jordan totients directly from prime factorizations and enumerates every powerful integer
\[
n\le20000.
\]
For each parameter triple
\[
3\le s\le6,\qquad
1\le b\le3,\qquad
1\le a<sb,
\]
it verifies that the values
\[
n^aJ_s(n)^b
\]
are pairwise distinct on that finite powerful set.

It also verifies the published identity
\[
J_3(28268)=J_3(28710)
\]
from recent work on bare Jordan-totient noninjectivity and checks that both sides contain exponent-one primes.

The finite replay is not the proof of injectivity. The theorem for all powerful positive integers and the support-exponent obstruction are proved symbolically in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
