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

For n>=6, rooted-path facets F_(j,r) indexed by gap vertex and root (n(n-1) facets) completely describe the PURE strong Morse cycle complex. Reflection has involution (i,b)->(a-i-1,1-b), with no fixed incidence vertices; invariant faces yield geometric fixed points via equal barycentric orbit weights. Edge and vertex-axis orbit families force precisely two disjoint maximal orbit faces, with sizes m-1 (n=2m+1 and even vertex-axis) or m-2 (even edge-axis). Their realizations are Δ^(m-2)⊔Δ^(m-2) or Δ^(m-3)⊔Δ^(m-3); fixed Euler characteristic 2 and reduced Lefschetz trace 1. Independent direct exhaustive rooted-facet/orbit enumeration verified maximal faces and all orbit-subfaces for 6<=n<=50 and every reflection conjugacy class; unbounded result follows from alternating-bit and gap obstruction in the supplied symbolic proof.

## originality

PASS

The defining Knudson–Owens-White primary source supplies the pure rooted-path complex and nonequivariant homotopy, but not geometric reflection-fixed sets. The previously published pure-complex rotation character concerns rotations; a separate full-strong-complex dihedral Euler result changes the simplicial object and cannot determine pure geometric fixed spaces. Full fixed-point topology is strictly stronger than a Lefschetz number. No dominating source found under same-object aliases; best-of-knowledge PASS with bibliographic risk.

## value

PASS

Provides an exact all-cycle-length PL-homeomorphism classification of reflection fixed spaces, with dimensions detecting distinct parity axes even though Euler characteristics coincide. This is a structural equivariant refinement motivated by cycle symmetry, not a routine restatement of known nonequivariant sphere wedge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
