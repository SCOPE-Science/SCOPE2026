---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently reconstructed the trace identity and all optimizer comparisons. For a cut pendant edge, the diagonal difference after restoring the edge is (p-q)/(1+p+q), where p=1/alpha and q is the adjacent inverse diagonal in the connected remaining tree. The Laplacian spectral decomposition gives q<p since that coordinate is not constant. Each internal vertex therefore loses to its own leaf. To check the cancellation set x=alpha, s=x+1, h=x^2+(m+2)x+1, c=x^2+4x+2. Eliminating leaves and then the two hub coordinates gives G_ee-G_oo=(h^2+s^2-ch)/(s h (ch-2s^2)). The numerator is x[(m-2)h-m] and ch-2s^2=x[x^3+(m+6)x^2+(4m+9)x+2m+4]. This gives the exact identity with a positive denominator. For m=2 the numerator after cancellation is -2; for m>=3 it is strictly increasing on x>=0 with exactly one positive root and all leaves tie there. The root equation x(m+2+x)=2/(m-2) gives m^2 x -> 2 and gives (sqrt(33)-5)/2 at m=3. Symmetric stable dynamics give trace equal to half the inverse diagonal by integrating e^{-2t(L+alpha I)}.

## originality

PASS

The inspected overlap establishes the optimization framework, group-inverse ranking, or phase changes in different two-leader problems. It does not establish the explicit positive-damping crossing and exact optimizer sets for this two-hub tree and unit single actuator.

## value

PASS

This is a complete exact example of reversal of the optimal trace-Gramian site under uniform damping alone, with the graph, metric and input magnitude held fixed. The threshold, equality class, and m^-2 scale quantify when a low-damping site ranking ceases to be reliable; they are not supplied by modularity or degree. The margin formula allows comparison without computing the full inverse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
