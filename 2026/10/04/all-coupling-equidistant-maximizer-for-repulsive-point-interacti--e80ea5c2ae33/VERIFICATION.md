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
# Verification

The proof is analytic. The checker is a corroborating replay of two independently written representations of the same periodic point-interaction operator.

`verify.py` constructs the cyclic Dirichlet-to-Neumann matrix from gap endpoint data, computes its largest eigenvalue with a Jacobi diagonalization, and locates the positive ground-state root. Independently, it multiplies exact free-propagation and delta-jump transfer matrices around the loop and checks that the resulting monodromy has trace \(2\) at that root. For several unequal gap vectors, dimensions \(N=2,3,4,5,6,7\), and couplings spanning weak to strong repulsion, it checks:

1. every reconstructed ground-state phase satisfies \(0<kd_j<\pi\);
2. the monodromy trace is numerically \(2\);
3. the exact Rayleigh/Jensen lower bound on \(\alpha\) holds;
4. the ground-state wave number is strictly below the equidistant value for unequal gaps;
5. the equidistant root satisfies \(\alpha=2k_*\tan(\pi k_*/N)\).

Run:

`python3 verify.py`

Expected terminal line: `VERIFY_OK`.

The numerical suite is finite and therefore does not certify the universal quantifier. The universal theorem rests on positivity, the exact Dirichlet-to-Neumann identity, Perron--Frobenius, strict Jensen convexity, and monotonicity, all written out in `RESULT.md`.
