---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For R_{d,m}=conv(0,e1,...,e_{d-1},sum e_i+m e_d), barycentric nonnegativity for integral projected height z is equivalent to all x_i>=z/m and sum x_i<=n+(d-2)z/m. Taking x_i=ceil(z/m) proves the sharp if-and-only-if section criterion (d-1)ceil(z/m)<=n+(d-2)z/m. Separating z=mq+s gives all multiples mq (0<=q<=n) and each nonzero residue s with 0<=q<=n-d+1+floor((d-2)s/m). At n0=d-1-floor((d-2)/m), s=1 is exactly the final residue to appear, and from n0 every missing height in [0,mn] is mn-(m j-s), 1<=j<=d-2-floor((d-2)s/m). The standard floor-sum over m-1 residues, including gcd(d-2,m), yields G=((d-1)(m-1)-gcd(d-2,m)+1)/2. Independent direct integer point searches matched all 90 triples for d∈{3,4,5}, m∈{2,...,7}, n∈{0,...,4}; all 550 parameter pairs (d=3..24,m=2..26) passed three post-threshold gap tests. The unrestricted theorem uses the exact barycentric and gcd identities, not finite enumeration.

## originality

PASS

Haase–Nill–Paffenholz lecture notes establish the Reeve simplex coordinates and original emptiness; no all-dilation height-range formula in inspected Reeve material. De Loera–Marsters–O’Neill (2025) full paper defines arithmetic projected width and proves eventual almost arithmetic progressions, translated gap structure and quasilinear width for broad polytopes, but neither states the explicit sharp Reeve threshold, gcd count, or all-n residue formula. Resultary semantic results concerned other simplex invariants and dilation saturation problems. The new result refines general eventual structure to an exact two-parameter canonical family in a fixed coordinate direction; possible older height-semigroup equivalent remains a real priority risk.

## value

PASS

Reeve simplices are a canonical empty-lattice-simplex family with anomalous lattice dilation behavior. Exact projected integer height spectra in all dimensions and dilation factors, earliest full-residue threshold, and gcd-sensitive finite hole pattern give an independently useful benchmark for the arithmetic-width invariant and semigroup gap stabilization. It is specifically height-direction cardinality, not the globally minimized lattice width.

The dated certificate retains the supplied scientific assessment, sources and limitations.
