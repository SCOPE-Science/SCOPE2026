---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The two positive information-class balances force U=u and I=i. The population totals and R balance force q, s and R, and the remaining equation is p(1+M)=1+Z with M+Z=q, hence the stated strict feasibility interval and uniqueness. For stability, in independent M,Z,I,R coordinates write Q for the linearized perturbation of M+Z. An eigenvalue in the closed right half-plane with λ≠0 gives Q=dI/(λ+a), M=−(a−c)Q/λ, Z=Q−M and R=εγI/(λ+εt); if the infected perturbation I were zero, the whole eigenvector would vanish. The resulting scalar equation has the terms λ+εf+ε²fγ/(λ+εt)+εdB(a−c)/(aλ)+εd(cB−aA)/(a(λ+a)). If the last residue is negative, the maximum fractional loss of the positive constant f is [Ks/(1−Ki)]·[uz(m−z)/(q²(1+z)(1+m))]<1/8, using z(m−z)=z(q−2z)≤q²/8 and Ks<1−Ki. Thus the real part is strictly positive even on the imaginary axis. Zero is excluded directly: the M row forces Q=0, the Z row forces I=0, the R row forces R=0 and the infected row fixes M=Z=0. The normal rates follow from the two scalar population-total equations. This establishes exponential stability for fixed ε>0 without assuming a uniform rate as ε tends to zero or any global result. The supplied exact-rational verifier and notes were inspected, not executed; the algebraic obstruction, not the finite examples, is the replay path for the universal conclusion.

## originality

PASS

The precise universal local stability statement is distinct from the cited preprint's stable example and slow–fast framework. The exact iff interior feasibility interval also corrects a material difference in the inspected preprint's printed formula. The model and most equilibrium coordinates are not new.

## value

PASS

For a published coupled ODE with a coexistence example but no general quartic classification in the inspected source, excluding local instability throughout its entire feasible time-scale family resolves a concrete mathematical gap. The feedback positivity argument also explains why a time-scale sweep alone cannot change local stability. This has value independently of the concise feasibility correction, without claiming global convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
