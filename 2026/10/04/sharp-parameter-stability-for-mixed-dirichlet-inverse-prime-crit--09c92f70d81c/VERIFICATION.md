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

The universal proof was checked case by case against the exact local formulas in arXiv:2609.33278v2. In particular:

- primes satisfy \(H_k(p)=0\) and \(\mu(p)+1=0\), so the parameter disappears exactly;
- even-parity squarefree composites have \(H_k(n)\ge4\), hence remain positive after adding \(2t\) whenever \(t>-2\);
- odd-parity squarefree composites have \(\mu(n)+1=0\) and the source's exact difference-of-products bound makes \(H_k(n)<0\);
- prime-cube divisibility gives \(P_{k,t}(n)=J_k(n)+2+t>1\);
- cube-free nonsquarefree integers satisfy the new exact bound
\[
\frac{\sigma_k(a)}{J_k(a)}<\frac{\zeta(k)^2}{\zeta(2k)}\le\frac52<3\le J_k(b),
\]
which forces the relevant integer bracket to be at least \(1\), hence \(P_{k,t}(n)>4\);
- at \(t=-2\), \(P_{k,-2}(1)=0\), proving sharpness of the connected interval containing the two source criteria.

`verify.py` independently replays the arithmetic functions by trial division and exact rational arithmetic. It checks \(2\le k\le6\), \(1\le n\le5000\), several rational values of \(t\) in \((-2,\infty)\), the boundary \(t=-2\), and the positivity of all tested cube-free nonsquarefree cases. The finite replay is corroboration only and is not used to justify the universal quantifiers.

Scientific limit: no assertion is made for \(k=1\) or for all disconnected parameter values below \(-2\).
