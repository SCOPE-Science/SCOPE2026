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

The original covariance and correlation claims are correct, but the frozen proof's unqualified leaf variance is false at n=2: p_2=1 gives −11/9 rather than 0. The code already handles this seed separately and its leaf-variance recurrence comparison starts at n=3. The repaired proof uses Var(L_2)=Var(L_3)=0 and restricts the expression (n−1+4p_n−16p_n²)/9 to n≥3. For the final claim, the conditional probabilities of selecting the root, a leaf, and both give the claimed survival ratio and means, and cancellation in the mixed product gives the prior covariance increment. The two summands telescope: Δ(np_n)=(n−3)p_n/[2(n−1)] and Δ((2n−3)p_n²)=−(2n−3)p_n²/[4(n−1)²]. The resulting exact formula has c_2=0; the increment at n=2 is zero and all subsequent increments are positive. The degree factorial moment H=E[D(D+1)] has multiplicative increment factor 1+1/(n−1), giving H=2(n−1). For V=Var(L), the conditional leaf-selection probability gives Cov(L,J)=V/[2(n−1)], and the unconditional Bernoulli variance gives the inhomogeneity in the repaired recurrence. Direct substitution verifies the displayed solution and its n=3 base. Stirling gives p_n=(πn)^−1/2+O(n^−3/2); this yields the exact constant correction −8/(3π) and variance growth (2−4/π)n and n/9, hence √n Corr→√(2/(π−2)). Correlation is undefined only at the deterministic leaf-count seed sizes considered, and strict covariance establishes positive variances thereafter. A new exact integer (D,L)-state replay through n=8 checked the covariance and corrected variance, and isolates the seed discrepancy (e.g. at n=4 it gives covariance 1/16 and leaf variance 1/4). The original program was inspected, not executed or changed.

## originality

PASS

Pass for the repaired resummation and explicit finite-size constant, not for discovering the exact covariance, its sign, or its leading order. The October 13 record gives exactly the same covariance as a finite sum for every n, with identical process, observable pair, and survival probability. The repaired RESULT.md credits it and telescopes both summands, obtaining a form without an n-dependent sum and evaluating the previously unspecified constant term; the correlation normalization is reported as an interpretation, not needed as an independent novelty claim. The repaired scope also avoids treating PORT as a single model determined by name. No inspected earlier result states or directly supplies the summation-free form and constant, subject to bounded search limitations.

## value

PASS

Only the genuine remainder is credited. The leading square-root approximation leaves an order-one error that need not be small at finite tree sizes. The resummation evaluates that bias, leaving an error of order n^−1/2, and gives exact values without summing over intermediate sizes. This quantifies the finite-size dependence of two natural, differently scaled observables. The correlation consequence explains the scale without claiming a joint law. The prior covariance existence, sign and leading result are not part of this value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
