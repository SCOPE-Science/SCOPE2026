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

The source rank formula and jump condition give u=2|r|, continuous positive quantile u+(b^2-1)artanh(u), and its truncation at 2b-1 for b<1. The resulting plateaus have probability 1-b at each signed edge. Before either plateau the ratio for b2>b1 is a strictly increasing fractional linear function of artanh(u)/u; once the smaller-b quantile flattens, the numerator continues to increase until any second plateau. An independent way to transfer this to moments is to normalize the squared quantiles to mean one. Their ratio is nonconstant and nondecreasing, so their difference has negative values below a crossing and positive values above it. At the crossing the common quantile value is c. Subtract the tangent at c from the strictly convex function y^m: the resulting function decreases below c and increases above c, so it is strictly larger on the second normalized quantile wherever the two differ. The tangent's linear part integrates equally, proving strict increase for every integer m>=2, including comparisons through b=1. The logarithmic endpoint gives finite moments and the variance is positive. For b>=1, the transform T=artanh(W) for W uniform on (-1,1) makes (1+W)/2 a Beta(1+z/2,1-z/2) variable under exponential z tilt. Its moment polynomials give M2=1/3+t+pi^2 t^2/12 and the displayed M4; direct subtraction gives the quartic with exactly one positive root. Independent decimal bisection gave b*=1.5435938337944687791701585849909913..., and the cumulant signs at 1.543593833794468779 and 1.543593833794468780 were opposite. The lower limit uses the quantile divided by its edge height: this is bounded by one and equals one on the plateau of probability tending to one. The uniform law gives 9/5 at b=1; the b^2-rescaled quantile converges in all required moments to T, giving 21/5. Subtracting three gives the quoted excess limits.

## originality

PASS

The stationary law, edge masses and morphological boundaries, and raw-moment integral are prior inputs. The supported distinct contribution is the family-specific strict standardized-moment ordering through the edge-cluster and smooth regimes, and the exact kurtosis sign boundary. General star-order implications require establishing the quantile ratio order here; raw-moment integrals do not supply it or its strictness across the junction. The closest compared catalogue results address different dynamics, observables and varied parameters.

## value

PASS

A single quantile comparison orders every standardized even moment across a change in the structure of the stationary measure, from edge atoms to unbounded smooth support. It adds information not obtainable by treating the known morphological boundaries as shape thresholds, and separates the exact kurtosis sign change from both known boundaries. The significance comes from the strict order valid at all orders and across regimes, not the decimal root alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
