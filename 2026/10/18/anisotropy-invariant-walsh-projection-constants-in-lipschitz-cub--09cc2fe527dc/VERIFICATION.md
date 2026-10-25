---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For finite positive weights w_i, coordinate-sign translation operators are still isometries of pointed Lip_0, so averaging any projection yields the canonical Walsh projection Q_A as unique character-diagonal equivariant projector, proving minimum norm. Weighted Lipschitz norm is maximum over edge differences/w_i. Fourier derivative along i is convolution by K_i, yielding norm <=max_i c_i where c_i is the mean absolute coordinate-shadow Walsh kernel. Pick i with smallest weight and let h=sign K_i; f=(w_i/2) x_i h(x_without_i), normalized at basepoint, has Lipschitz norm 1 because every transverse edge has weight at least w_i and its amplitude difference <=w_i. Its i-th projected derivative attains c_i. Coordinate-transitive spectral support makes every c_i identical, so sharp weighted norm is the unweighted coordinate-shadow constant. The homogeneous layer count follows by binomial signs; degree-2 formula gives n=4 value 3/2 for every positive w. Zero-kernel signs, n>=2, degree 1 and n endpoints are accounted for; argument proves all weights, not only tested rational examples.

## originality

PASS

Best-of-knowledge statement-level comparison identifies no prior theorem implying the final claim at its actual hypotheses; known overlap and residual bibliographic risks are recorded, not erased.

## value

PASS

Exact relative projection constants for every coordinate-transitive Walsh support on arbitrarily anisotropic positive weighted Hamming cubes, including proper transitive groups and all homogeneous layers, reveal a non-obvious invariant of finite metric Banach spaces even though coordinate permutations cease to be isometries. The least-weight sign-gradient construction is a reusable sharpness mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
