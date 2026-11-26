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

For a nonconstant binary palindrome the initial and final symbols agree, so the factor has an odd number of runs. The single-run counts are the two symbol-wise maxima. Each internal run of a three- or five-run factor is traversed in full. The two 0-1-0 families intersect in min(a,c,e) factors if and only if b=d; in that case the five-run family adds min(a,e) factors. With x=min(a,e) and v=max(a,e), the three zero-run terms sum to v+c+min(x,c), while the two one-run terms sum to b+d. This gives the exact defect. For at most four runs the two possible three-run families have distinct end symbols and the corresponding maxima plus minima sum to the length (omitting absent families). At positive defect r, ordered unequal (b,d) have series 2z^3/((1-z)^2(1+z)), and the outer pair with minimum c+r has series z^(2c+2r)(1+z)/(1-z). Summing over c and marking r gives the stated coefficients and joint series after replacing the positive-defect terms of the unmarked composition series. The positive count and first-moment series have dominant terms (1-z)^(-5)/3 and (1-z)^(-6)/6 respectively, with other poles of lower order; division by binomial(n-1,4) gives the claimed asymptotics. The first possible length at defect r>0 is 2r+6; (r+1,1,1,2,r+1) realizes it and lengthening one of its outer runs realizes every larger length. Complementation handles initial symbol 1.

## originality

PASS

The supported distinction is the full length-by-defect multiplicity law and its consequences, not exclusive novelty for the defect formula, attainable values, or the qualitative richness criterion. Two distinct published catalogue findings contain the identical pointwise five-run formula; one also gives the attainable spectrum and maximum, but neither contains the joint count, density or first moment. Both are listed later than the frozen record; chronology alone is not evidence about their derivations or priority. The older sources inspected do not establish the multiplicity law by a covering result.

## value

PASS

Five runs are the first binary run restriction in which positive defect is possible. The distribution distinguishes how often richness fails and by how much, including an exact sparse-length cutoff, a positive limiting fraction and a linear mean. It is a natural baseline for defect statistics with more runs, not just a zero-defect test or list of attainable values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
