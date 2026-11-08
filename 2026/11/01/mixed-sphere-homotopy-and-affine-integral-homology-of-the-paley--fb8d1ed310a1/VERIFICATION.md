---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The Paley(13) graph is the quadratic-residue graph on F13 with residues {1,3,4,9,10,12}, degree 6. Ind_2(P13) comprises subsets with induced degrees <=1, equivalent to avoiding all two-neighbor triples and to first forest-filtration stage F1(P13). Independently verified 312 nonempty faces, f=(13,78,143,78), 78 top-dimensional facets, 149 acyclic matched pairs and 897 oriented Hasse incidences. Independently reconstructed 6x7 integral critical Morse boundary rank five and a 5x5 unimodular minor (-1); hence the simply connected Morse model is S2 wedge two S3. The exact signed 78-element affine Lefschetz computation and rank restrictions show translations act trivially, multiplier 4 acts by sign on H2 and a rank-one Eisenstein lattice on H3. Therefore positive-degree rational homology has no affine-invariant vectors, which gives rational acyclicity of the finite quotient, not integral acyclicity.

## originality

PASS

Searched dissociation/2-independence, forbidden-two-neighbor-triples and Carnero Bravo first forest-filtration F1 equivalents. The complete primary text of Deshpande–Singh and Carnero Bravo does not include the Paley-13 affine module or mixed wedge. Published Paley tournament, ordinary independence or Vietoris-Rips modules are for different graph/complex definitions. No covering source was found, with explicit priority uncertainty.

## value

PASS

Paley13 is the first prime Paley graph beyond five vertices and has a distinguished 78-element affine symmetry. Its natural first forest-filtration/2-independence complex is pure but non-shellable because H2 and H3 both survive; the integral wedge and inequivalent sign/Eisenstein lattice actions resolve a canonical equivariant invariant that cannot be inferred from ordinary face counts. This supplies an exact benchmark and a rational quotient consequence, without claiming a general Paley-order classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
