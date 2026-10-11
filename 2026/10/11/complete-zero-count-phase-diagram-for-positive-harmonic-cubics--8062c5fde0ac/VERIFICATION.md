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
# Reproducibility and limits

The proof does not require numerical computation. The following steps were checked separately:

1. Expand real and imaginary parts of \(z^3+az+b\overline z-1\); for nonreal zeros obtain \(P(x)=8x^3-2(2b-a)x+1\) and \(y^2=3x^2+a-b\).
2. Verify that the discriminant of \(P\) equals \(64D\), that the positive stationary point is \(\sqrt{(2b-a)/12}\), and that \(P(\sqrt{(b-a)/3})\) has sign opposite to \(E\) when \(b>a\).
3. Independently count the positive/negative real roots of \(P\) using stationary-point signs and bisection, filter by the strict positivity of \(y^2\), and compare with every regular-region row of the classification.
4. For \((a,b)=(3,5/2)\), verify the exact factorization \(P(x)=(2x-1)(4x^2+2x-1)\), the six explicit nonreal zeros, the unique real zero, and nonzero Jacobians.
5. Numerically cross-check the exact discriminant fold, the real-axis collision condition, and their common cusp; 20,000 pseudorandom positive parameter pairs passed in the standalone checker.

To rerun the supplementary checks, execute `python3 verify_cubic.py`. The script uses only the Python standard library. Finite checks do not certify the universal quantifiers; those follow from the proof in RESULT.md. No independent verification or external audit has been performed.
