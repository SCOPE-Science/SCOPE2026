---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

I reconstructed the full all-d>=4 proof for S_d: F=x1^d+x1*x2^(d-1)+x3^d-x4^d. The partial derivatives have no common projective zero in characteristic zero, proving smoothness. A line parametrized by four binary linear forms has pair ranks (r1,r2); rank-zero is impossible and mixed 1/2 ranks would force a degree-d separable binary divisor to equal a dth power. If both ranks are two, the root configurations of u^d+uv^(d-1) (0 plus (d−1)-st roots of -1) and z^d-w^d (unit dth roots) would be projectively equivalent. For d−1>=3, three unit roots determine the generalized unit circle while 0 lies off it, contradicting Möbius preservation of generalized circles. Hence both ranks are one: exactly d² lines x1=a x2, x3=b x4 with a^d+a=b^d-1=0. Separability and normal bundle O(2−d) give finite reduced etale line scheme. Rational roots give four for even d and one for odd d. Row/column incidence and adjunction yield matrix eigenvalues d (1), 0 (2d−2), −d ((d−1)²). Hyperplane class belongs to their span and Hodge index makes pairing nondegenerate on that span; its rank is (d−1)²+1, hence 36 geometric lines, 4 rational, rank26 at d6. Independent small-degree integer Kronecker matrices d4,5,6 had ranks10,17,26; these are corroboration of the uniform proof.

## originality

PASS

PASS best of knowledge for the exact entire line Hilbert scheme and line-class lattice, distinguished from Cheltsov–Tschinkel's identical branch-surface equation and rational-curve density theorem. Poonen's related self-equality binary-form surface is not this mixed inequivalent pair; Page–Ryan–Smith supplies broad line bounds, not its exact Fano scheme. A specialized old classification of split or Delsarte-type surfaces could imply parts; flagged explicitly.

## value

PASS

The sextic is a specific arithmetically motivated branch surface used in potential-density research. Exhaustively determining every geometric and rational line, its incidence, and the rank-26 span of their Néron–Severi classes informs actual curve geometry and Picard constraints of the example; the theorem also classifies the full all-d>=4 family and gives an exact finite-etale scheme, not a numerical accident.

The dated certificate retains the supplied scientific assessment, sources and limitations.
