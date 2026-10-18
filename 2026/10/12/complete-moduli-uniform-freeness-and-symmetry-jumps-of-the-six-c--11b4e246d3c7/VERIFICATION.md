---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Bézout between six lines and the conic gives 3q+n=12 for conic quadruples q and conic nodes n; the only numerical cases are (4,0) and (3,3). If one quadruple point were off the conic four lines concur there and the two remaining lines meet in only one point, so cannot support three distinct triple-line conic quadruples. Thus q=4, n=0, each line meets two of four conic points, and all six are pairwise chords of a projective frame. Their standard coordinates yield L=xyz(x−y)(x−z)(y−z), Q=xy−lambda*xz+(lambda−1)yz, lambda≠0,1. Möbius permutation gives six anharmonic values with quotient j. For f=LQ, exact identities D(L)=3(x+y+z)L and D(Q)=(x+y+z)Q imply the quadratic Jacobian syzygy (2D−SE)f=0. Since any positive-dimensional projective stabilizer would fix/permutate the intrinsic four-point frame, no degree-one syzygy exists; mdr=2. Tjurina sum 3+4*9=39 meets du Plessis–Wall freeness equality (7^2−2(7−2))=39, free exponents (2,5). Four-point Möbius stabilizers yield generic V4, harmonic D4 and equianharmonic A4. Independent Sympy checked the universal polynomial identity, Tjurina identity, and j-orbits; classification for all complex lambda follows from geometry, not specialization.

## originality

PASS

Pokora 2023 exhibits one free harmonic configuration C(6,1;3,0,4); Janasz–Pokora 2026 prove numerical restrictions and restate that example. Neither inspected manuscript proves every complex realization of that weak-combinatorial stratum is the complete-quadrangle family or supplies universal freeness and the complete automorphism jump stratification. Complete quadrangles, cross-ratio and j-invariants are classical and not claimed as invented; their forced realization-wide appearance is the claim.

## value

PASS

The identified singularity stratum is a natural exact weak-combinatorial configuration. Proving every realization free and locating its coarse complex moduli and automorphism jump strata answers a motivating Terao-type realization question, substantially beyond a textbook cross-ratio restatement or one previously exhibited free curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
