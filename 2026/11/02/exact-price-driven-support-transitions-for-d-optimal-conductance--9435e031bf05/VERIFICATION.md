---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Cactus spanning trees contain each bridge and omit one edge of every cycle, yielding exact product factorization and homogeneous block degrees 1 or l-1 totaling n-1. Injectivity of edge weights into grounded Laplacian for simple graph plus strict logdet concavity proves global uniqueness on positive-tree domain, including boundary. Scaling each positive block gives d_H B/(n-1); one-sided KKT derivative at unique zero face is (l-1)/D Σ_{e≠k}p_e and multiplier (l-1)/D, proving sharp iff. Differentiation gives one-exception a,b. Independently rationally checked 7-vertex cofactor 27/98 and 35 priced-cycle KKT cases. Numerical checks alone cannot establish all graphs.

## originality

PASS

Matrix–Tree, logdet concavity and D-optimal methods are known. Sagnol–Harman present broad conic D-design, while Khosoussi et al study fixed candidate weights/edge selection, not independently scalable positive-cost conductances. The particular cactus homogeneous block budget and dominant-price deletion criterion are not shown in inspected primary results; specialized optimal-tree entropy results remain a priority risk.

## value

PASS

Gives a sharp support decision and exact budget decomposition for heterogeneous prices on an arbitrarily large natural graph class without numerical optimizer, distinguishing full-cycle retention and edge-deletion regimes at a meaningful phase boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
