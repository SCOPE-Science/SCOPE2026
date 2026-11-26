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

For the positive-exponent convention the gamma transform is exp[-m log(1-it/c)] on the principal branch. For t>0 the argument gap before multiplying by m has derivative (b-a)(ab-t^2)/[(a^2+t^2)(b^2+t^2)], so its range, together with t=0, is the entire interval from 0 to Theta_r. After normalizing component magnitudes, the squared modulus is 1-4u(1-u)sin^2(m theta/2). Its minimum over u gives the asserted sharp margin and unique balanced weight at each of the two subcritical minimizing frequencies. At a zero the gap must be an odd multiple of pi and the weights balanced. Tangent subtraction gives the stated quadratic; when its discriminant is zero there is only one positive frequency but the Fourier zero is still simple, since the log modulus ratio has a nonzero derivative there. Strict monotonicity of that ratio separates all exceptional weights. Conjugacy, F(0)=1, the derivative of Theta_r with respect to r, and the L1 Wiener theorem give the remaining claims, including the exact threshold and slope. The bound is relative, not uniform in absolute magnitude. Independent finite cross-check: python /workspace/checks/3.py with mpmath (output /workspace/checks/3.txt) brackets frequencies without using the quadratic and tests first and higher mergers, distinct weights, and shapes on either side. It is not the proof of the universal quantifiers. The submitted scripts were inspected, not executed.

## originality

PASS

Pass is for the full fixed-endpoint, fixed-weight real-zero classification (including uniqueness and simplicity even at mergers), and the optimized phase diagram as a whole, not for angular nonvanishing, midpoint projection, antipodal balancing, or Wiener cyclicity. The earlier generalized Stieltjes result is substantial overlap: its no-zero direction and midpoint-rotation proof already give the subcritical quantitative lower bound; its measure class differs for supercritical zero attainability at a specified frequency. The checked prior statements do not give the fixed-weight exceptional locus and multiplicity classification. Gharib's full text was available for this review. This is a best-of-knowledge assessment.

## value

PASS

A union of attainable zeros does not say which particular positive mixtures lose cyclicity. The fixed-endpoint classification isolates finitely many weights, identifies and distinguishes all higher branches, and shows that a merger in the frequency equation still gives a simple transform zero. That exact locus is useful for deciding cyclicity of a specific mixture; the relative margin quantifies conditioning in the regime where none are exceptional.

The dated certificate retains the supplied scientific assessment, sources and limitations.
