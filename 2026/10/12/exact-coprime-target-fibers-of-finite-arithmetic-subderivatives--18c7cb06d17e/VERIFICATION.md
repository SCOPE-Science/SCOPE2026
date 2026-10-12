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

The proof is symbolic and has no finite cutoff. Its critical steps are:

1. For an \(S\)-coprime target, any exponent \(\nu_p(n)\ge2\) with \(p\in S\) would force \(p\mid D_S(n)\), so all active \(S\)-exponents equal one.
2. Writing the active subset as \(T\) and \(n=mP_T\) gives the exact identity \(D_S(n)=mH(T)\).
3. Divisibility \(H(T)\mid y\) is both necessary and sufficient because \(H(T)\mid y\) together with \(\gcd(y,P_S)=1\) makes \(m=y/H(T)\) coprime to \(P_S\).
4. Distinct subsets have distinct intersections with \(S\), hence yield distinct preimages.
5. Singleton subsets prove the universal lower bound and exact minimum; the admissible-subset least common multiple proves the exact maximum.

The included `verify.py` recomputes \(D_S\) directly from valuations and compares predicted and actual fibers for 135 coprime targets across four finite prime sets. For exhaustive checks it uses the rigorous bound \(n\le y\max(S)\), since any positive value satisfies \(D_S(n)\ge n/\max(S)\). It also verifies
\[
D_{\{2,3,5\}}^{-1}(217)=\{210,310,434,651,1085\}.
\]
The computation is regression evidence only. No finite experiment is used to justify the general theorem.
