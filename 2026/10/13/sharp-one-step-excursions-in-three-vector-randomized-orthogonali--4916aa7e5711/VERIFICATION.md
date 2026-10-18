---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For any invertible congruence supported on a chosen pair that diagonalizes its principal 2x2 block, trace invariance proves DeltaGamma=2 B_ij (B^-1)_ij. Diagonal normalization to a 3x3 correlation matrix and cofactor calculation give Gamma=2(a²+b²+c²-3abc)/Delta and ratio increment a(bc-a)/H. All three upward increments cannot be positive simultaneously because 0<correlations<1 after sign reductions, so at most one pivot rises. For an upward pair put z=bc,d=(b-c)^2: Delta=(1-a)(1+a-2z)-d>0 gives a<z<(1+a)/2; the rational gain is maximized as z approaches the strict boundary and is strictly less than a/(a+2)<1/3. The exact positive-definite family a=1-4h+3h²,b=c=1-h (0<h<1/3) yields ratio 4/3-h and upward probability exactly 1/3. Thus full tail one-third for each t in [1,4/3), zero at >=4/3; zero-Gamma and 2D boundaries are covered. This is an algebraic proof, not an inference from finitely many pivots.

## originality

PASS

Detherage–Shah arXiv:2505.02023v4 already proves the general pair update and mean contraction E[Gamma prime]=(2/3)Gamma at dimension three, and remarks that individual steps may increase Gamma. Their inspected text does not optimize the 3x3 correlation cone, count upward pairs, or give the sharp 4/3 and 1/3 distributional constants. Its precursor uses a different monotone logarithmic-volume potential, and Steinerberger a different directional norm process. The new low-dimensional, pathwise, sharp frontier is not implied by mean contraction alone.

## value

PASS

The initiating random-pivot method guarantees contraction in expectation despite possible per-step worsening. For algorithmic stability and risk, maximum one-step excursion and probability of worsening are independent natural quantities. Their exact sharp boundaries in the smallest nontrivial dimension, including an explicit near-singular extremal family, are motivated finite-dimensional structure, not a routine copy of the expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
