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

Independent check: remove the designated vertex k and label the remaining path from 0 to d=n−2. The start lies at position j=n−1−k if the path begins at k+1 and proceeds clockwise. The time U to first hit a path endpoint has mean j(d−j). From either first endpoint the conditional probability of visiting the opposite one before hitting k is 1/(d+1), by ruin on an interval of length d+1 starting at distance one from the failure boundary. Success in that second leg is exactly L=k. Its probability is independent of the history through U, so it leaves E[U] unchanged. For ruin on [0,b], the joint exit moment for the right boundary is w(i)=i(b²−i²)/(3b), obtained by substituting into w(i)−(w(i−1)+w(i+1))/2=i/b with zero boundary values. The crossing leg conditioned on L=k therefore has mean w(1)/(1/b)=(b²−1)/3 for b=n−1. After the opposite endpoint is hit, the remaining mean to hit k is b by the unconditioned ruin formula; at this point L=k is already determined. Adding yields the exact stated profile and the uniform marginal. This includes n=3 and starts at either path endpoint (U=0); integer maximization gives floor((n−2)²/4) and averaging gives n(n−1)/2. The frozen arc induction is consistent with the independent argument: the next-discovery weights are joint exit-time moments, not conditional times, and the final waiting time has constant mean from either endpoint.

## originality

PASS

Prior work covers the uniform last vertex, unconditioned mean and useful hitting-order representations. The supported distinct claim is the conditional time–location moment, not those ingredients. The inspected close statements do not state the moment or a joint time–location law that provides it by specialization.

## value

PASS

The exact conditional moment quantifies a dependence hidden by the uniform last-vertex marginal: conditioning at the antipode rather than a neighbor of the start changes the mean by order n², the same scale as the unconditional mean. It provides a finite-n benchmark for joint coverage laws, not merely a recalculation of the classical cover time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
