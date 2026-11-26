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

In each harmonic below d, the first two entries on the Hermitian diagonal for that harmonic produce an invertible two-radius coefficient map (determinant proportional to r²−1); the top harmonic has only one entry, shared with scaling r^d. An individual vanishing profile at 2d distinct unit nodes has one real degree of freedom and leading direction given by the inverse square root of the angular product, modulo real scaling. For the determinant, use complex lower-frequency columns z^(−d+1),…,z^(d−1). Appending z^d gives a Vandermonde times the product of z^(−d+1); appending z^(−d) instead gives a ratio −1/Pi. Thus the two-circle determinant in complex columns has modulus r^d |Delta(U)Delta(V)| |Pi_U−Pi_V|. Converting the lower pairs on both circles and the one shared top pair has total modulus factor 2^(1−2d). Hadamard equality for each Fourier Vandermonde forces every ratio of distinct nodes to be a nontrivial 2d-th root of unity; the remaining factor is maximized exactly at opposite angular products. Off resonance, equality of full circle moduli leads to multiplicative dilation invariance of P/Q by r², hence a constant rational ratio. In degree two the singular odd cubic determinant on a circle in the real two-plane kernel vanishes; no nonzero semidefinite kernel element is possible because the outer nodes span the evaluation space. The resulting indefinite rank-two matrix gives an ambiguity. Independent exact Gaussian-rational checks verified the determinant square and ranks in four nonregular designs in degrees 2 and 3, including distinct resonant angular sets.

## originality

PASS

The regular-grid angular criterion and half-step geometry are covered by two distinct catalogue findings and are not separate novelty. The supported distinct claim is the arbitrary-distinct-node determinant with the specified normalization and lifting ranks, the global determinant upper bound and all equality cases over arbitrary angular sets, and the quadratic converse for arbitrary four-plus-four nodes. The regular-grid results do not imply these nonregular statements.

## value

PASS

The exact invariant detects one global sampling resonance even with distinct nodes, including highly nonregular layouts. It gives all global determinant maximizers, not just an optimum among regular grids. In degree two it determines nonlinear failure as well as linear singularity, so practical design and ambiguity can both be read from arbitrary sample angles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
