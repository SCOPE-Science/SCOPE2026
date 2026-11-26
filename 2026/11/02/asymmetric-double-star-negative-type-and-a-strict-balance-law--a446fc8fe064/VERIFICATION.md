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

On the zero-sum space eliminate the second hub coefficient and write each leaf vector as its mean plus a zero-sum fluctuation. If A=2^p, the only remaining hub square is -2[u+AX/2-(A-2)Y/2]^2. Its complementary 2-by-2 form on the two leaf sums has diagonal U_m,U_n and off-diagonal -B after changing the sign. The fluctuations and hub variable are freely choosable in this decomposition. At p=1 the form is positive definite; at p_*<2 one diagonal vanishes and B>0 by strict concavity of log(3^p-1)-(2p-1)log 2 between its zeros at 1 and 2. Thus a root inside the interval is positive semidefinite of rank one. Li–Weston Theorem 5.4 excludes any higher negative type, hence also a second root in that interval, and gives strictness at every lower nonnegative exponent. The endpoint has one equality direction; equivalently the centered Euclidean Gram rank drops by one. For fixed S, at p_S=log_2(2+2/S) the diagonals are positive and B(p_S) is at most J(p_S-1)<2/S by B''<0 on p>=1 and J<2 log 2. The determinant is then positive, and all critical roots are above p_S. Beyond p_S the product-dependent term 2^(2p)(1+S(1-2^(p-1)))/(mn) strictly increases with mn. A larger product also lowers max(m,n), increasing p_*, so comparison at the smaller-product root stays inside the larger pair's positive-diagonal interval. For proportional growth the scaled equation is (1/rho-Lc)(1-Lc)=J^2 c^2/4; the left side strictly decreases until its first zero, giving the unique admissible root, whose rationalized form is the display. For fixed m the determinant instead forces U_n=O(n^-2) and gives 1/L. Independent bisection reproduced the two quoted examples to the displayed precision; this is diagnostic, not needed for proof.

## originality

PASS

Credit the balanced equation, equality dimension and balanced leading coefficient as material existing coverage. The supported distinction is the unequal-branch determinant classification, strict allocation order at fixed total leaf count and the full branching-ratio and fixed-branch laws. The strongest available exact comparisons concern either equal arms, the one-hub star, or a different hub separation.

## value

PASS

This is an exact threshold and extremal allocation law for a natural tree family, with the size, asymmetry, and critical equality dimension all controlled. The strict leaf-budget order is not a restatement of the balanced value, and the two growth regimes quantify distinct ways of approaching the tree exponent 1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
