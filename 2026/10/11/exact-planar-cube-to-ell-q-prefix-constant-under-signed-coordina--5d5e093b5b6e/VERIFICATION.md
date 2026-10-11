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

The proof is universal and analytic. The following checks were performed on the final claim.

1. For \(v=(a,b)\), the change of variables \(m=(a+b)/2\), \(d=(a-b)/2\) satisfies \(|m|+|d|=\max\{|a|,|b|\}\).
2. The four pairs \((\alpha,\beta)\in\{-1,1\}^2\) yield exactly the allowed images \(\pm(a,b)\) and \(\pm(b,a)\).
3. Choosing each scalar sign against its current scalar partial sum gives \(|S+x|\le\max\{|S|,|x|\}\), so both transformed prefix coordinates remain in \([-1,1]\).
4. The map \((M,D)\mapsto\|(M+D,M-D)\|_q\) is convex for every \(1\le q\le\infty\). Its values at all four vertices of \([-1,1]^2\) are exactly \(2\), proving the upper bound on the whole square.
5. For \(v_1=(1,1)\) and \(v_2=(1,-1)\), every allowed second prefix is one of \((\pm2,0)\) or \((0,\pm2)\), proving the lower bound \(2\).
6. Substituting \(n=2,p=\infty\) into Theorem 9 of arXiv:2610.02127v1 gives \(R_{2,q}=2^{1/q}\), \(C_{2,\infty}=1\), and a second term \(2^{1/q}\), hence source bound \(2^{1+1/q}\) for finite \(q\); the \(q=\infty\) endpoint is \(2\).

No finite enumeration, numerical optimization, or timeout-based inference is used to establish the theorem. The originality review does not assert exhaustive global literature coverage; an unindexed historical formulation remains a stated residual risk.
