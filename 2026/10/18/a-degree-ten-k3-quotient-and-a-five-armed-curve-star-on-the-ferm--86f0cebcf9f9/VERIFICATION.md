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

Taking the graded invariants gives the asserted equation. The projective fixed loci are v=0 (a smooth fixed quintic with reflection action in its normal direction) and the isolated point in the v-chart. At the latter the u derivative is 5 and the remaining smooth coordinates z,w are acted on by simultaneous sign, yielding exactly one A1 point. Weighted adjunction, crepancy and the invariant summand of H^1 of the quintic, preserved by resolution of the rational singularity, give K3. The degree-two sections have no common zero; pullback from the ample Cartier O_Y(2) gives nef and big, with only E contracted. The square is 10 and cannot be divisible by the square of any integer at least 2. Locally on the resolution use q=z/w and p=w^2: the exceptional is p=0 and the five strict transforms are q=beta with distinct simple roots. The equation at v=1 gives u as w^5(q^5+1) times a unit; u^2 pulls back to order 5 on p=0 and order 2 on each arm. Thus the divisor identity is integral and linear, not just numerical. Adjunction and the Schur complement give the star's signature and determinant. The t=0 plane quintic is disjoint from o, maps isomorphically from the fixed curve, and is a genus-six member of H. Coordinate permutations and diagonal fifth-root scalings give the stated conjugacies. Independent replay: python3 /workspace/reproductions/finite_checks.py 1 checks the polynomial, square completion, local leading form and lattice identities; the geometric assertions are proved analytically.

## originality

PASS

Best of the comparisons made, prior sources cover the involutions and general geometric tools, not the specific Fermat transposition quotient together with the marked configuration and polarization degeneration. The degree-ten K3 is its minimal resolution, not the singular weighted quotient itself.

## value

PASS

The classified Fermat involutions motivate asking what surface one obtains. The integral nef genus-six polarization and all six named curves, rather than just the K3 label, provide useful geometric data for classifying or comparing the model and its degree-two alternative. The reducible member and the fixed smooth member are in the same concrete linear system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
