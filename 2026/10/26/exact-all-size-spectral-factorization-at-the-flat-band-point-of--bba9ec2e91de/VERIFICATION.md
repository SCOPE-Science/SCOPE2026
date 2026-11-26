---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stated u,v are orthonormal, the off-diagonal site block is J|u><v| and σ_z interchanges the two basis vectors with a minus sign. Ordering the basis along the resulting path gives N−1 links of weight J with two uncoupled boundary vertices until the onsite perturbations join them via links of weights ±iγ/2. End sites give disjoint three-vertex components, interior noncentral sites give disjoint four-vertex components, and central sites share one dimer, producing a six-vertex component. With z=λ² and g=γ²/4, expanding path determinants over disjoint edges gives λ(z−J²+g), (z−J²)²+gz, and (z−J²)³+2gz(z−J²)+g²z respectively. For the six-vertex path, using neither imaginary link yields the first term, exactly one yields gz(z−J²) per link, and using both yields g²z. Counting untouched dimers and isolated vertices gives exactly the three stated characteristic polynomials, including N=4 where no noncentral interior placement exists. Both boundary roots stay real through γ=2J, and both boundary blocks there have rank two and characteristic polynomial λ³, hence each has one Jordan block of size three. The noncentral quadratic discriminant is g(g−4J²), negative for small positive γ. In the central factor put z=J²+√g b and divide by g^(3/2): as g tends to zero through positive values the polynomial tends to b(b²+2J²), with two simple non-real roots; their continuations prove the zero infimum. Independent exact symbolic site-basis determinants for (N,m)=(4,1),(4,2),(6,1),(6,2),(6,3) match the formulas. The frozen checker was read, not run; its finite transform/recurrence checks use floating-point tolerance, even at rational test inputs. The invariant block proof, not those checks, gives the exact all-size conclusion for the specified single-particle matrix.

## originality

PASS

The model, sweet-spot edge threshold and exceptional-point phenomenon are prior. The endpoint spectral mechanism is also directly accessible from known Majorana couplings. Prior work observes zero-threshold interior behavior. The independently supported distinct content is the exact even-size spectrum resolved over all mirror positions, especially the two inequivalent interior characteristic factors and untouched multiplicities. The threshold split alone is not credited as original.

## value

PASS

The factorization gives exact multiplicities and the complete moving part of the finite-size spectrum at the standard dimerized point. It explains structurally why the centrally adjacent defect pair and the separated interior pair are spectrally different even though both have zero onset threshold, and supplies checks for exact diagonalization results beyond the already-known end transition. It makes no statement about the many-body spectrum or parameters away from flat-band dimerization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
