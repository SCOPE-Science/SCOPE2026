---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For u_j equally spaced pentagon unit normals and target cone volumes (t,t,1,1,t), t>0, directly recomputed gamma_j=h_j(h_{j-1}+h_{j+1}-2q h_j)/(2s), q=(sqrt5-1)/4, s=sin(2pi/5). Positive gamma and h force all five edge lengths positive, hence a genuine convex pentagon. Reflection coordinates h=(a,b+x,d+y,d-y,b-x) split antisymmetric equations into a 2x2 linear system. Symmetric x=y=0 gives one branch with t(r) increasing 0->infinity. Nonsymmetric determinant zero forces rational algebraic A(B), y/x=-1/(B-sqrt5+1), Z(B)=(x/d)^2, H(B)=2s/d^2 and T(B)=t. Cubic roots beta0~2.057628, beta*~2.251826 delimit exactly the positivity interval (beta0,beta*), each B producing a reflected pair. Direct independent symbolic differentiation confirms T'(B)=positiveprefactor P6(B)/J0(B)^2; the SEVEN exact Bernstein coefficients of P6 on [2,2.3] are strictly negative, so T decreases infinity -> T(beta*)~3.085259816987. Thus exactly one solution t<=t*, three t>t*. Independent exact symbolic checks of factorization/discriminants/Bernstein negativity and direct cone-volume substitutions at three rational B values were successful. Fixed origin supports and no scaling/translation quotient; t=t* belongs to single-solution regime.

## originality

PASS

Baumbach–Chen–Henk (Oct 2026) exhibits EXACT same normals and t=4 data with three support solutions, so that particular example, equations, and general finite-fiber framework are NOT new. The full continuous 0<t<infinity sharp threshold and exact one/three branch classification requires explicit elimination and global sign proof not implied by one t=4 fiber or parity arguments. Strong plausible predecessor, however the complete source paper (and older Stancu articles) was not accessible; originality therefore best-of-knowledge and provisional, without claiming absence from unseen material.

## value

PASS

A specific three-solution example in the log-Minkowski cone-volume literature naturally asks whether the nonuniqueness is isolated or part of a sharp symmetry-breaking phase. The complete positive parameter range has an exact algebraic threshold and every nonsymmetric solution is classified via one monotone branch and reflection. Such sharp fiber geometry is structurally informative; it is not a routine restatement of the single published t=4 example. The scope is this one normalized reflection-invariant five-normal family, not the general discrete problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
