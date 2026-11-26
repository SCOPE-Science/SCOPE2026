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

Reconstructed the process on an uninterrupted exact Gram–Schmidt run. At inspection i, conditional on the full past, the squared residual U_i and the squared in-span projection V_i have a fixed product chi-square law, with n-i+1 and i-1 degrees of freedom. Consequently the pairs are independent across i. The running total S_i is their cumulative sum; S_i-U_i is independent of U_i with (i-1)(n+1) degrees of freedom. This proves the beta marginal, not a conditional hazard. At i=1 the test never passes for epsilon<1. For the timing let i0=(1-epsilon^2)n, h_n=sqrt(n log n), and fix 0<eta<1-epsilon^2. The chi-square law S_i~chi-square(in) gives max over i>=eta n of |S_i/i-n| <= A sqrt(log n) with probability tending to one for a sufficiently large constant A. For i<=eta n the residual means exceed epsilon^2 n by a fixed fraction of n, and union bounds using chi-square deviations of order n for U_i and S_i/i exclude stops there with probability tending to one, including the smallest i. For i<=i0-c h_n with i>=eta n, an upper threshold u=epsilon^2(n+A sqrt(log n)) suffices. The chi-square lower-tail Chernoff bound is exp(-I(k,u)), where I=(k log(k/u)-k+u)/2 at k>u. Its derivative in k is log(k/u)/2, increasing and of order sqrt(log n/n) at the smallest k=epsilon^2 n+c h_n+O(1). Thus the early tail sum is bounded by a geometric series, O(sqrt(n/log n)) exp(-I(k,u)), and I(k,u)=(c^2/(4epsilon^2)+o(1))log n. This tends to zero when c>sqrt(2)epsilon. For 0<c<sqrt(2)epsilon the sqrt(n)-long window just before i0-c h_n has one-look probabilities at threshold epsilon^2(n-A sqrt(log n)) at least n^(-c^2/(4epsilon^2)+o(1)), uniformly. This lower bound follows by integrating the chi-square density over a left interval of length sqrt(n/log n) using Stirling's formula; the interval contributes only a logarithmic prefactor. The independent U_i give a vanishing product of no-hit probabilities. Add the denominator-sandwich failure probability without conditioning the independent innovations on that event. These two inequalities prove the normalized first hit, and the convention T=n+1 causes no exception because a hit occurs with probability tending to one. Pruning changes the preappend rank by at most one. Exact projection gives e_n^2=1-K_n/n, and dividing the scaled difference of squares by e_n+epsilon yields 1/sqrt(2). Read RESULT.md lines 29–61, VERIFICATION.md and CHECK.py. The checker was inspected, not executed: it is only finite corroboration and its simulation assertion of a final hit in its chosen trials is not an all-trajectory guarantee. The motivating paper independently specifies the cumulative estimator and supports the unit-block pruning rule; the exact companion files could not be independently re-read. No part of the result is extrapolated to finite precision, arbitrary block sizes or spectra.

## originality

PASS

The supported contribution is the sharp first-hit and accuracy law for the actual cumulative-denominator, unit-block stop on identity inputs, together with its exact unconditional beta inspection law. Neither fresh Gaussian residual estimation, a chi-square ratio calculation by itself, nor generic repeated-testing effects are the claimed originality. The motivating primary algorithm was inspected and the closest distinct catalogue theorem has a different denominator, marginal law and leading constant.

## value

PASS

The identity is the natural flat-spectrum calibration case for this adaptive stopping rule. The theorem identifies a diverging rank deficit with an explicit constant and a tolerance violation with probability tending to one, despite each fresh inspection using an unbiased residual-energy estimate before normalization. That is a useful sequential failure mode; a finite marginal, finite simulation or generic multiple-testing warning cannot supply the rank and error scales. The actual excess relative error tends to zero; the finding does not imply comparable miscalibration for arbitrary QB implementations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
