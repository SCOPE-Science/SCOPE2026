---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

The supplied `verify.py` is standalone Python 3 standard-library code. Run it as

```sh
python3 verify.py
```

The expected complete success line is:

```text
VERIFY_OK D4_24cell vertex_sets=42504 max_det=12 maximizers=48 B4_orbit=48 shared_four=0
```

The code constructs the \(24\) four-coordinate roots, checks their squared radii and even coordinate sums, examines **every** unordered five-root combination (exactly \(42{,}504\)), and recomputes each determinant by two distinct exact-integer methods (cofactor expansion and permutation expansion). It checks the full seven-bin determinant spectrum, all \(48\) maximum determinant configurations, and the absence of any common set of four vertices among two maxima. It also computes the entire \(384\)-element signed-coordinate-permutation orbit of a concrete maximum, checks that it agrees with the complete 48-member maximum family, and verifies the six/four squared-edge-length spectrum of every maximizer.

The certificate is exhaustive only over the explicitly enumerated finite vertex subsets, not over continuum-many points inside the polytope. The proof of the universal upper bound, the four-volume of the containing polytope, and the reduction of an arbitrary optimizer to a vertex optimizer with rigidity are supplied analytically in `RESULT.md`. No timeout, stochastic sample, or approximate computation is used as evidence for an infinite or exhaustive statement.

Historical originality is compared with the referenced root-system, spherical-simplex and published lattice-Voronoi results, with an explicit residual possibility of unnoticed classical tables. No independent validation has been performed.
