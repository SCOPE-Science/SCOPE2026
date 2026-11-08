---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Conditioning on a prescribed isolated K2 removes its two vertices and forces the other m−1 edges to be uniform in the Q=C(n−2,2) remaining potential edges. The conditional triangle mean C(n−2,3)(m−1)_3/(Q)_3 minus the unconditional mean yields the stated exact covariance and factorization. The positive prefactor times A_n(m−3)−B_n m changes sign at m*=n/2+1−(n+5)/(3n²−6n−1), strictly between ceil(n/2) and its successor. In G(n,p) conditioning on K2 excludes both endpoints and yields strictly negative −C(n,2)(n−2)^2p^4(1−p)^{2n−4}. Sparse scale m=⌊cn/2⌋ gives c³(c−1)e^(−2c)/2.

## originality

PASS

Resultary returns a related total-component-count versus triangle identity in independent bond percolation, not isolated-edge component count in fixed-edge G(n,m). Reviewed random graph process and triangle tail papers do not explicitly state current covariance transition.

## value

PASS

The exact finite-size sign reversal at the critical linear edge count contrasts the fixed-edge and independent-edge ensembles for a natural local-component/global-subgraph pair. A practitioner studying conditioned random graphs can use the closed covariance and sparse limit; the location is sharp, not merely numerical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
