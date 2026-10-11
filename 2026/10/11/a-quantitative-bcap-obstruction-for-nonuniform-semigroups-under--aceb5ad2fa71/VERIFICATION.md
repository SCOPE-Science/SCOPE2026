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

The proof was replayed from the semigroup and Calkin definitions.

1. Strong continuity makes \(L=\limsup_{t\downarrow0}\|T(t)\|\) finite and at least \(1\).
2. For every \(c>L\), a short-time bound \(\|T(t)\|\le c\) on \([0,\delta]\) and the semigroup law give a global estimate \(\|T(t)\|\le c e^{\omega t}\) with \(\omega=(\log c)/\delta\).
3. If the generator is unbounded, every right resolvent has dense proper range, so it is not Fredholm.
4. Atkinson's theorem plus uniform nilpotence of noninvertible Calkin elements makes \(J_\lambda^m\) compact.
5. Yosida convergence gives \(J_\lambda^m x\to x\) for every \(x\), while \(\|J_\lambda\|\le c\lambda/(\lambda-\omega)\to c\).
6. Hence, for every \(\eta>0\), a tail of the compact approximants has norm at most \((c+\eta)^m\). Strong convergence with a uniform tail bound is uniform on compact subsets.
7. Taking the infimum over approximation bounds and then letting \(\eta\downarrow0\) and \(c\downarrow L\) yields \(\beta_{\mathcal K}(X)\le L^m\).

The case \(\beta_{\mathcal K}(X)=\infty\) gives the qualitative Lotz conclusion by contradiction. The case \(\beta_{\mathcal K}(X)=1\) gives no positive jump beyond the trivial lower bound. No claim of equality, realization, or independent validation is made.
