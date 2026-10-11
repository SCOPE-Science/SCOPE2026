---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof reconstructs the full two-parameter triangle domain. With \(p=(B+C)/2\), \(\delta=(C-B)/2\), \(\gamma=\cos p\), and \(u=\cos\delta\), one has \(0<\gamma<u<1\) and the exact ratio \(Q=(y-z)/(c-b)=2(1-\gamma)\sqrt{(1+\gamma)/(1+u)}(u+\gamma+2\gamma^2)/(u-4\gamma^3+3\gamma)\). The denominator is positive because \(u>\gamma\) and \(\gamma-(4\gamma^3-3\gamma)=4\gamma(1-\gamma^2)>0\). For fixed \(\gamma\), the logarithmic derivative has numerator \(N_\gamma(u)\) with \(N_\gamma'(u)=-2u-4\gamma^3-6\gamma^2<0\); hence any interior stationary point is the sole sign change from positive to negative and is a maximum, so the minimum lies at an endpoint. The endpoint limits are \(1\) and \(f(2\gamma)\). The derivative of \(f\) has numerator \(x^3+4x^2+x-10\), strictly increasing on \(x>0\), so its unique root \(q\in(0,2)\) gives the global minimum \(\kappa=f(q)=0.856762017555545\ldots\). Taking \(\delta\downarrow0\) with \(2\cos p=q\) proves sharpness and also shows nonattainment away from the isosceles limit. A fresh independent numerical replay over the reduced domain found no violation and converged to the same constant; it is corroborative only.

## originality

PASS

Hajja's 2008 primary paper poses exactly the best-constant problem, reports numerical searches near \(0.856762\), derives the same isosceles-limit function and cubic, and explicitly conjectures the inequality with \(f(q)\). The audited result supplies the missing global two-parameter upper exclusion by proving that the ratio has no interior minimum. Current Resultary and targeted searches returned the assigned theorem but no independent proof of the 2008 conjecture. Later Steiner-Lehmus papers located in the search concern other variants; a 2019 same-theme article was not fully inspectable here, so that source remains a residual risk rather than a basis for a noncoverage claim.

## value

PASS

The theorem resolves an explicit published sharp-constant conjecture in a classical geometry problem and identifies the exact limiting shape. This is a natural global extremal question, not a parameter substitution or finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
