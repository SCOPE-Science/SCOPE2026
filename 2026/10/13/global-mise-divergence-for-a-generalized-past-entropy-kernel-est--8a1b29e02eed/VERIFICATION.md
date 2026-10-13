---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The estimator definition, parameter range, kernel assumptions, bandwidth assumptions, primary MSC classification, first-publication date, and Theorem 3.3 statement were checked against the publisher's open full text.

For the proposed counterexample, the following analytic checks were completed:

1. IID \(\operatorname{Exp}(1)\) observations are \(\alpha\)-mixing and have a smooth density on \((0,\infty)\).
2. The Gaussian kernel is nonnegative, symmetric, integrates to one, is Lipschitz, and is an order-two kernel; \(b_n=n^{-1/2}\) has \(b_n\to0\) and \(n b_n\to\infty\).
3. For \(\beta=1/2\), the target generalized past entropy is
   \[
   2\log\!\bigl(2(1-e^{-t/2})\bigr)-\log(1-e^{-t}),
   \]
   and tends to \(\log4\).
4. For an all-equal deterministic sample at location \(c\), exact Gaussian integration gives
   \[
   A_n(c)=\Phi(c/b_n),
   \qquad
   B_n(c)=\sqrt{b_n}\,2^{3/4}\pi^{1/4}\Phi(c/(\sqrt2 b_n)).
   \]
   Therefore its tail estimator level tends, as \(c\to\infty\), to \(\log\sqrt{8\pi/n}\), which differs from \(\log4\) for every integer \(n\ge1\).
5. Continuity of the tail functional in the finite sample vector gives an open positive-probability exponential-sample event on which the limiting estimation error stays nonzero. The squared error is then bounded below by a positive constant for all sufficiently large \(t\), so its integral over \((0,\infty)\) is infinite.

The source's equation (3.11) was also checked: its displayed nonnegative variance term contains a factor proportional to \(\beta^2/F(t)\), whose integral over an unbounded-support model diverges because \(F(t)\to1\). This is consistent with, but is not used to prove, the direct counterexample.

Limits: no claim is made about a compact time interval, an integrably weighted time risk, fixed-time asymptotic normality, or the source's compact-interval strong-consistency theorem. The closest 2014 generalized-past-entropy estimator paper could not be inspected in full and remains an originality-access risk.
