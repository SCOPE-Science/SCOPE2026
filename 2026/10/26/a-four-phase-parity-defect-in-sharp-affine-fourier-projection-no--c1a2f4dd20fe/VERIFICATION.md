---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. Uniform even-parity H_n with n>=3 has independent proper coordinate subsets, so 1,x_i form an orthonormal family and the projection kernel is 1+sum_i x_i y_i=n+1-2d_H(x,y). Equal row/column absolute sums give the exact operator norms, with a sign-valued row extremizer. Splitting the full binomial sum by parity, using truncated alternating identities for binomial coefficients and j-binomial coefficients, gives the two closed central-binomial formulas and relative corrections; central-binomial recurrence yields all stated dimension reversals and ties. Independent exact binomial checks in dimensions 3..120, plus direct Gram/kernel construction through dimension 8, corroborated identities and n=3 boundary; these finite checks are not the all-n proof.

## originality

PASS

PASS, best-of-knowledge. The general compact-abelian Fourier projector norm integral is already proved by Defant et al. and is explicitly credited; their full-cube formulas and higher-chaos asymptotics do not state the even-parity single-check norm or evaluate the alternating conditional binomial moment and its four-phase dimension effects. Inspected Resultary matches concern Lipschitz-free cube projections and reflection-group isotypic blocks, with different operator spaces or characters. This conclusion relies on the exact difference in implications, not merely titles or a negative search.

## value

PASS

PASS. The even-parity single-check code is a standard natural linear code and the affine least-squares projector is its canonical lowest-frequency Walsh projection. Its exact sharp amplification, alternating odd/even relative correction, and infinite sequences of adjacent dimension decreases/ties resolve a meaningful norm question not answered by the general projection identity alone. Not a claim about arbitrary codes, other Fourier layers, intermediate p, or minimality of projections beyond the canonical one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
