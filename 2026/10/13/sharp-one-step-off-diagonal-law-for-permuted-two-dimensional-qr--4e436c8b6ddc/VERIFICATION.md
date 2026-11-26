---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With r=||Ae1||, the columns of Q are (a,b)/r and (-b,a)/r under the positive-R-diagonal convention, and A(-b,a)=(0,det A). Their inner product through A yields b⁺/b=det A/r², with the swapped denominator d²+b². Since both diagonals are positive, comparing column norms compares a and d. Their squared norms sum to μ²+L², so the larger is at least half this sum; a 45-degree eigenbasis realizes equality and leaves b nonzero. For larger-eigenvalue weight w on e1 the fixed-order ratio is κ/[1+(κ²−1)w]; this grows above one exactly for 0<w<1/(κ+1) in the assumed non-diagonal domain, equals one at the boundary, and tends to its unattained supremum κ as w decreases to zero. The boxed bound is an upper bound on the multiplier, which is the precise reading of the later informal contraction wording. The supplied rational checker was inspected, not run; its witnesses do not establish the universal assertions.

## originality

PASS

Credit the classical QR identities and existing diagonal/column-norm permutation heuristics. The supported distinct claim is the exact sharp best-versus-fixed one-step off-diagonal comparison for 2×2 SPD inputs, not the algorithms, the power-iteration viewpoint, or the elementary column calculation in isolation. The closest bounded mathematical comparisons did not establish that sharp comparison or a stronger bound implying it.

## value

PASS

The existing ordering heuristic and the standard off-diagonal measure motivate the optimization without selecting an arbitrary example. The exact worst-case multiplier and equality orientation quantify a guarantee for the heuristic on every two-dimensional SPD input, while the adverse orientation and nearly κ-fold transient show precisely what the heuristic prevents. This is useful as a sharp diagnostic for the elementary QR case, not a claim of better general eigensolver complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
