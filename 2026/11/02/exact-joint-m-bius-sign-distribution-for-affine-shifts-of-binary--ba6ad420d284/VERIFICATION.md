---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Translation by the quadratic coefficient a gives B=b+a^2, C=c+ab and C'=C+ua+v; for u nonzero, (B,C,C') uniquely gives back (a,b,c). The repeated-root condition for a depressed cubic is exactly C=0, since its derivative is Y^2+B and its value at sqrt(B) is C. Verified the Berlekamp/Pellet polynomial specialization against Carmon's formulas. Also independently derived the signed sums by counting roots: for B=0, the cube map permutes the nonzero elements for odd m (one root per nonzero fiber), while for even m every nonzero fiber has zero or three roots. Thus S(0)=epsilon(q-1), epsilon=(-1)^(m+1). For B nonzero let A1,A3 count nonzero fibers of x^3+Bx with one and three roots. The zero fiber has two roots, so A1+3A3=q-2. Two different inputs with sum t!=0 collide exactly when z^2+z=1+B/t^2 with z=x/t. If the right-hand side has trace zero this gives two solutions, representing one unordered pair. As t varies, B/t^2 runs over the nonzero field, so the number of pairs is q/2-1_{Tr(1)=0}=1+3A3. It follows that S(B)=2A1-(q-1)=-epsilon. The total signed sum over B is zero. In the product sum S(B)S(B+u), two distinct exceptional B each contribute -(q-1), and the other q-2 each contribute 1, giving -q. At each B, one C gives zero sign, and (q-1+sS(B))/2 gives the other sign counts; multiplying and summing over B yields q[(q-1)^2-st]/4 for nonzero s,t, q(q-1)/2 for exactly one zero and q for two zeros. At q=2 the table has same-sign entries zero, opposite-sign entries one each, one-zero entries one each, and the double-zero count two. This is an independent symbolic proof for every m, not an extrapolation. Frozen verify.py and VERIFICATION.md were inspected but not executed; their recorded finite field checks are not needed for the quantifier.

## originality

PASS

The distinct claim is the sign-resolved joint law and exact negative correlation for nonconstant affine shifts, not the cubic Berlekamp formula, the unsigned squarefree total, or the affine normalization. No equivalent/stronger result covering that exact nonconstant-shift law was identified in the passages compared. The closely related indexed exact result is for constant shifts, and the cited general correlation estimates do not determine the finite numbers. This is a bounded scientific comparison, not a priority claim.

## value

PASS

Monic cubics are a natural low-degree test of finite-field sign correlations. The exact joint probabilities distinguish equal from opposite signs and pin down the finite negative correction -q in a regime usually addressed by cancellation bounds. The coefficient separation applies to every nonconstant affine shift and every binary field size, including the smallest boundary, not to selected shifts or a few enumerated fields. It provides a substantive sign-resolved benchmark beyond an unsigned squarefree count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
