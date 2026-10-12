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

The mathematical proof is symbolic and uses one literature input: the uniform asymptotic formula for \(F(n,s)\) stated in Koussas Proposition 14 (following Maddux). The bundled checker does **not** try to reproduce that asymptotic enumeration.

`verify.py` uses exact Python integers and `fractions.Fraction` to check the deductions from the source formulas:

- \(Q(n,n-2k)-Q(n,n)=-k(n-1)\);
- \(P(n,n)=(n-1)!\) and \(P(n,n-2k)=(n-2k-1)!k!2^k\);
- the closed form for \(R_{n,k}\);
- \(R_{n,1}=(n-1)(n-2)/2^n\);
- the exact recurrence
  \[
  R_{n,k+1}/R_{n,k}=\frac{(n-2k-1)(n-2k-2)}{(k+1)2^n};
  \]
- for \(k\ge1\), the recurrence ratio is at most \(n^2/2^{n+1}\);
- the finite geometric-tail inequality
  \[
  \sum_{k\ge2}R_{n,k}
  \le R_{n,1}\frac{n^2/2^{n+1}}{1-n^2/2^{n+1}}
  \]
  whenever the denominator is positive.

The checker ranges over all valid \(k\) for \(5\le n\le250\), plus additional tail checks. These computations are sanity checks for the algebraic manipulations. The asymptotic transfer from \(R_{n,k}\) to actual relation-algebra counts depends on the cited uniform theorem and is justified in the written proof.

Independent audit has not been performed.
