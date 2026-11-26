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

The commutator lands in the six-dimensional arrow ideal J. With three distinct diagonal values its restriction to J is triangular with six nonzero pivots. For a double value, conjugation by 1+h with h of degree one eliminates the cross-block degree-one terms modulo J² because [h,D] scales each cross-block path by a nonzero diagonal difference. A second conjugation with h in J² eliminates the residual cross-block degree-two terms. Each cross block then contributes full rank, and the radical-square-zero repeated-value corner adds one precisely when its internal radical component is nonzero. For fixed diagonal D, the rank-four elements are exactly its 1+J orbit, of size q^4 since the stabilizer consists of 1 plus the two internal paths. For scalar diagonal, the length-one commutator on arrows is exterior multiplication by the arrow coefficient vector (up to row ordering), so has rank two whenever that vector is nonzero, including characteristic two. The incidence on idempotents then adds one or two according as the arrow support has one or at least two edges: in the one-edge case the only missing degree-two coordinate is the reverse path whose endpoints are identified by the kernel, and in the two-or-more case that kernel is constant. With zero arrow vector only the length-two incidence remains, of rank zero, one or two. These strata give all seven coefficients; summing q^(9-r) per element and dividing by q^18 gives the displayed probability. Split Fourier idempotents, with the cyclic labeling chosen to match the arrow direction, realize the ordinary Taft algebra multiplication for q ≡ 1 mod 3. The supplied checker was inspected, not run; the argument applies to every finite field without computer enumeration.

## originality

PASS

No covering all-element ordinary commutator census was found in the inspected evidence. The closest exact radical census counts a restriction with a different domain and does not supply the diagonal-collision strata or even the scalar-diagonal incidence contributions in the full algebra. Green-ring and singularity-category results organize modules, not the ranks of L_a−R_a indexed by elements of A. This is a best-of-knowledge statement, not a priority claim.

## value

PASS

The full ordinary centralizer distribution of this natural small cyclic algebra is usable beyond its first moment, the commuting probability. It shows precisely how repeated diagonal values and the length-two radical layer create ranks missing from the square-zero truncation, with an exact all-field classification rather than a test at selected field orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
