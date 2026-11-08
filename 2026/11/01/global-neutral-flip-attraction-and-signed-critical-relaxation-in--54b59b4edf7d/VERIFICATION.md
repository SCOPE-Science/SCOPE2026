---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The exact logit identity logit(f(x))-logit(x)=-a(x-b) forces any two-cycle to have endpoints b±d and a=Q_b(d)=[L(b+d)-L(b-d)]/d. Since L‴(x)=2/x³+2/(1-x)³>0, Q_b increases strictly from 2/[b(1-b)] to infinity, proving the exact unique-cycle boundary. At and below a_c absence of a primitive 2-cycle invokes classical Coppel convergence; strict sign of f(x)-x toward b excludes boundary limits for interior trajectories. At critical a_c, the induced exact T_b(u)=u-2(expm1(u))/(1+b expm1(u)) has second-iterate jet u-gamma u³+delta u⁴+eta u⁵, gamma=4(1-3s)/3>0, delta=2(2b-1)(1-3s)/3, eta=(3-5s)/15. Independently expanded to order five at b=1/2,1/3,1/5 and confirmed these coefficients; the inverse-square increment is 2gamma-2delta u+(3gamma²-2eta)u²+O(u³). Summation gives n(x_n-b)²→s²/gamma, the parity-signed sqrt(m) correction and (b=1/2) 3/20 log(m) with bounded residual. Analytic iterates have countably many finite-time preimages of b; excluded from reciprocal-square formula. Near-birth expansion of Q_b gives d²/(a-a_c)→3s³/[2(1-3s)]. Exact global proof, not long-trajectory extrapolation, establishes all b and a.

## originality

PASS

Comparison across equivalence, broader coverage, exact results and claimed implication finds no decisive existing result that covers the final scoped theorem in accessible inspected material; precise covered ingredients and full-text access risks are explicitly recorded. This is a best-knowledge scientific judgment, not an attestation of independence or a guarantee of historical priority.

## value

PASS

Directly resolves the asymmetric neutral-equality case singled out as Conjecture 3.10 in the original game-theoretic dynamics paper, beyond later strictly attracting theorem, and quantifies the physically relevant decay time and asymmetric sign bias. The universal critical constant, signed sqrt correction, symmetry-specific logarithm and unique two-cycle birth are natural sharp transition data, not arbitrary coefficient calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
