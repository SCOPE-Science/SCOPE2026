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

Independently rebuilt the integer compressed-walk matrix B for each half-separation from the coin/shift, keeping the full ordered matrix-unit space rather than using the frozen symmetry reduction. For each B its exact characteristic polynomial P(z) is coprime with z^deg(P) P(2/z); a root of modulus sqrt(2) would supply a common root by conjugation. As B/sqrt(2) is a contraction, this certifies strict spectral radius less than one and geometric survival tails. Using F=2I-B^T⊗B^T, solved Fv=2vec(I) and Fw=2v exactly over the rationals; at the index of the initial diagonal matrix unit, v gives the mean and 2w-v the second moment. Obtained (mean, second, variance, slope) equal to (1,1,0,0), (4,24,8,2), (9,145,64,4), and (16,560,304,-32). A single, zero-cost reset attempt succeeds with generating-function weight f(1-r)/(1-r), and lasts on average [1-f(1-r)]/r; expansion gives (mean^2-mean-variance)/2. The quotient as written applies for 0<r<1; at r=1 with L>1 detection is impossible, and L=1 is always detected in one step. This endpoint does not alter the stated weak-reset finding. The classical Dirichlet equations give m_1(x)=L^2-x^2 and m_2(x)=(x^4+(2-6L^2)x^2+5L^4-2L^2)/3, so the slopes are 0,2,12,40. Replay is given by the backward linear systems above and the specified basis and one-step coefficients in RESULT.md; frozen verify_variance.py was inspected, not run. No claim is checked beyond the four sizes or about a global optimum.

## originality

PASS

Credit the four-size exact second-moment/local-threshold classification for the specified post-nondetection, zero-time reset rule, not the known no-reset mean or the general reset-advantage concept. The closest source counts reset updates as elapsed steps; the frozen relationship note's claim of protocol equivalence needs that qualification. Relevant inaccessible articles leave a specific residual risk for second-moment tables, not evidence of coverage.

## value

PASS

The four consecutive smallest widths are an exhaustive, motivated search for the onset of a qualitative sign reversal, not arbitrary table entries. The matched classical calculation shows that equal no-reset mean times can coexist with opposite local reset effects. The precise threshold is useful when selecting small benchmark systems; the value is limited to this coin, preparation, monitoring and reset rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
