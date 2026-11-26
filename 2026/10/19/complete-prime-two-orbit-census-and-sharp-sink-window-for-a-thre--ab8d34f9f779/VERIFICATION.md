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

The frozen result is mathematically correct, including the boundaries: on a primitive two-cycle the other coordinates are forced by its two successive y-values, and normalized scalar equations give U²+UV+V²=B−1 and, off the symmetric branch, U²−UV+V²=B+1. This excludes B≤1, gives the symmetric pair for B>1, and gives two asymmetric pairs only for B>2; at B=2 the candidate asymmetry collapses. The symmetric polynomial follows from the trace, principal minors and determinant of the full return, or squaring the conjugate-one-step spectrum. For d=B−1 strict cubic Schur conditions give 4d²<1 and the sign of −(4d²−2d+1)(4d²+2d−1), with the other two conditions positive on 0<d<1/2. At the cutoff the stated real factor and nonreal unit pair follow; no nonlinear endpoint attraction was established. In the repaired claim the affine normalization G(X,U,Z)=(U²,UZ,X−B) gives the return derivative directly; UV=−1 and U²+V²=B reduce its trace, principal-minor sum and determinant to 1, 2(B²−2), 4. The resulting P_B is strictly increasing for real λ and changes sign between 0 and 1. Its nonreal pair has modulus 2/√ρ>2 by the product of roots. The invertible return therefore has the stated local stable and unstable dimensions. Independently computed exact states and characteristic polynomials at B=3 corroborate this result. The new companion verifier was executed successfully, including both signs at B=3 and a symbolic check under V=−1/U; the frozen script was not executed.

## originality

PASS

PASS applies to the repaired claim only. The frozen headline census and symmetric cutoff directly duplicate an earlier catalogue result on the identical real map; those assertions, together with the already proven asymmetric nonsink conclusion, are excluded from the repaired claim of advance. The surviving asymmetric characteristic polynomial and the real/complex multiplicity and modulus information distinguish a definite hyperbolic saddle type from that earlier determinant obstruction. The near-equivalent and stronger claims checked below do not give that asymmetric classification.

## value

PASS

The repaired claim gives the local phase-space type of both known asymmetric cycles throughout their entire existence region. An expanding multiplier guaranteed by a determinant does not distinguish a repeller from a saddle or real expansion from a two-dimensional oscillatory instability. The exact polynomial, uniform modulus gap and stable dimension give useful information for local invariant-manifold or bifurcation studies of the original map. This judgment does not add value credit for the already-known census, symmetric sink window or asymmetric nonsink obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
