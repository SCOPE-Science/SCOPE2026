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

The exact costs follow independently by solving the follower equations for the two class sums. With r=2-a, s=q-k+a and D=2q-rs, the inverse has diagonal blocks q^{-1}I_r + s/(qD) times the all-ones matrix, and (1/2)I_s + r/(2D) times the all-ones matrix, with off-diagonal entries 1/D. This includes empty classes by omission. The squared Frobenius norm gives the three formulas. J1-J2 has strictly increasing numerator on q>=k; its sign at q=k separates integer budgets 2,3 from k>=4. J0-J2 increases strictly from a nonpositive value and J0-J1 increases from a negative value; both tend to infinity. The printed derivative bound handles q>=3, but its text omits noninteger 2<k<3, k<=q<3 in the auxiliary real gamma assertion. To check the omitted range, the first two terms of F'_k are at least 1/(2q)+(q-2)/q^3>=1/6. If the last term is subtractive, its magnitude is at most 2(q^2+q-7)/(q+1)^3, which increases on [2,3] where this numerator is positive and is at most 5/32. Thus the claimed real uniqueness also holds. Ordering the crossings gives every minimizer and all admissible integer ties; K_{2,2} at k=2 ties counts 0 and 2. Subtracting (q-k)/4 gives the three stated limiting costs; the strict signs at fixed ratios on either side of alpha bracket gamma_k/k, and the explicit eta_k gives beta. An independent bounded replay constructed the raw follower matrices and checked the scaled inverse identity with integer entries and the resulting costs for 1,740 class cases (2<=k<=30, k<=q<=35). It reproduced the mixed examples and the k=11, q=22 tie. The packaged verify.py and verification.log give an alternate finite rational replay; the continuum proof, not those checks, covers unbounded sizes. No change to the claim is needed.

## originality

PASS

Credit the established second-order inverse-square criterion, exact inverse-first-power allocation on the same graph and the inverse-square near-balanced subfamily. The supported distinct result is exact inverse-square minimization, all ties, and the two limiting thresholds on the full unbounded two-hub family. No inspected statement implies those comparisons.

## value

PASS

The two-hub network is a natural asymmetric family with exactly three symmetry classes, and the inverse-square trace measures second-order coherence in the stated ideal model. Proving when a mixed placement is necessary, resolving the integer ties, and bounding the mixed phase by two distinct proportional scales answers a concrete optimization question not settled by a generic spectral formula. This is not a universal finite-gain or arbitrary-graph conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
