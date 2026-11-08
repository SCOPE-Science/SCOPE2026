---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For any finite connected simple cactus H, a connected spanning subgraph retains every host bridge and omits at most one edge from each cycle. The block-cut tree has a unique itinerary between any two vertices, so distances satisfy d_G(x,y)-d_H(x,y)=sum_(e omitted)[d_(H-e)(x,y)-d_H(x,y)], even for articulation-shared cycles. If e={a,b} is deleted, each endpoint's utility shift equals q_endpoint(e)-alpha; it is profitable unilaterally exactly when tau_e=max(q_a,q_b)>alpha. Conversely bilateral addition profits for both exactly when alpha>tau_e. Hence Phi=sum_C(alpha for intact C, tau_e for deleted e) is a strict ordinal potential. Cycle-independent stable choices are intact for alpha>=max_e tau_e and broken at e for alpha<=tau_e, proving the exact product enumeration and nonempty factors at equality. Summing the same distance increments over ordered vertex pairs gives W(G)=W(H)+sum_(omitted e)(Q_e-2alpha), which yields cyclewise polynomial-time optimal/best-stable/worst-stable welfare. In the triangle with k-1 leaves at each of two vertices, tau_e=k and the ab deletion improves welfare by 2(k²-alpha), so for k<alpha<k² the intact state is uniquely stable but not optimal; at k=5,alpha=10 welfares are 450 and 480, with PoS approaching 8/7 along alpha=k+1/2. Read the frozen RESULT, supporting source, verification script, and source tree. Finite script tests are supporting rather than all-cactus proof.

## originality

PASS

The source model and a one-cycle inefficiency example are prior art from Friedrich et al. The complete all-alpha cactus-specific exact ordinal potential, equilibrium product and welfare decomposition were not found in inspected stronger general-host theorems or indexed findings. Distinguish prior cycle examples and general parameter-range bounds from an exact every-cactus classification; unindexed specialist overlap remains possible.

## value

PASS

Cactus graphs form a natural maximal block structure on which shortest-path distance increments decouple, sharply contrasting with improving-response cycles on unrestricted host graphs. The exact all-parameter potential, equilibrium count, and welfare optimization solve structural, algorithmic and price-of-stability questions beyond a textbook substitution. The earlier one-cycle inefficiency observation is not counted as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
