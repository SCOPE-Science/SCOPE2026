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

For d>=6, positive detector loss and detector-supported Hermitian perturbation, the orthogonal complement to the A-Krylov detector space is dark; any non-decaying mode in its complement would be simultaneously an A-eigenvector and orthogonal to all detectors, a contradiction. On Walsh shell k, the restricted span equals F_k + epsilon_Y F_k, where F_k is the d-dimensional affine-function space for 1<=k<=d-1. Layer-constant/contrast analysis gives intersection dimension d for min(t,d-t)=0, 2 for s=1,2, 1 for s>=3 and min(k,d-k)=2, and 0 for the remaining interior shells. Summing exact shell ranks proves the three values 2d^2-4d, 2d^2-6d+8, d^2-d+2, and the exact unordered center-pair counts. Independent rational Walsh rank calculations for all d=6,7 separations and a separately inspected modular Krawtchouk/Krylov verification program corroborate but are not the infinite proof.

## originality

PASS

The detector cyclic-space/dark-space method is known from continuous-time quantum transport, particularly Novo et al.; novelty is limited to the full two-closed-radius-one-ball placement classification on Q_d including strict intermediate optimum and antipodal redundancy. Published SCOPE/Resultary nearby hypercube transport papers concern different operators/detectors, not identical ranks. This is best-knowledge with possible broader controllability coverage.

## value

PASS

The exact accessible-mode/capture probability reveals a sharp three-stratum dependence on Hamming separation and a counterintuitive antipodal inefficiency, useful for positioning two absorbing neighborhoods in symmetric hypercube transport. This is a natural infinite-dimensional-parameter classification rather than arbitrary finite parameter tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
