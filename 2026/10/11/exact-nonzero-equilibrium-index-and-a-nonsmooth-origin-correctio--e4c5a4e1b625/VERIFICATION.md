---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

From x3'=0 get x3=−x1; x1'=0 yields x1(x2−a−1)=0. If x1=0 then E0=(0,1/b,0); otherwise x2=a+1 and r²+r=1−b(a+1)=c, giving ±r iff c>0. At E± calculate Jσ=[[1,σr,1],[-σ(2r+1),−b,0],[-1,0,−1]], determinant χ(λ)=λ³+bλ²+α λ+α with α=r(2r+1)>0. Region c>0 forces 0<b<1; Routh column [1,b,α(b−1)/b,α] has signs +,+,−,+, exactly two positive-real-part roots and one negative, none on imaginary axis. Independent SymPy determinant and high-precision benchmark roots corroborate algebra. At E0 one-sided derivatives ∂x1(−|x1|)=−1,+1 differ, disproving a classical Jacobian there. Do not extend hyperbolic-index theorem to E0 or claim global dynamics.

## originality

PASS

Original part is exact existence/characteristic-cubic and fixed two-dimensional unstable index for entire positive-parameter region, plus a concrete correction of the source's mathematically undefined Jacobian at the central equilibrium. Model and special equilibria were published earlier.

## value

PASS

Identifies a substantive local stability error in a published named finance flow and supplies complete exact equilibrium-index classification for its full natural positive-parameter regime. More than cheap eigenvalue recomputation: fixes nondifferentiability and uniform stability type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
