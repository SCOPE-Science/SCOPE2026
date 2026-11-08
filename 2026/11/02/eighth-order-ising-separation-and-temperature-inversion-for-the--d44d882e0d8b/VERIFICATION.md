---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For the two explicit order-5 Latin-square graphs of 25 cells, both have 150 edges and strongly regular (25,12,5,6). Negative-spin subset S with k vertices and e induced edges has H=J(150−24k+4e)−h(25−2k). Hence exact partition function equals prefactor times P_G(y,z)=Σ_S y^k z^{e(S)} evaluated at y=exp(β(24J−2h)), z=exp(−4βJ). Independent complete 2×2^25 Gray-code enumeration (not sample) and source second recursive-row method show ΔP(y,1+t)=Σ_r A_r(y)t^r with A0..A5 identically zero, A6=−4y⁴(y−1)⁴(y+1)¹³, A7=−24y⁵(y−1)²(y+1)¹¹(17y³−15y²−3y+3) and A8(1)=−24576. Therefore all β^j,j≤7 cancel for any fixed real field h and ΔZ=−48·2^25·J^8·β^8+O(β^9) for nonzero real J. Independently exact enumeration shows both maxcuts 90, with ground-state multiplicities 35260 and 35172, yielding positive ΔZ~88exp(30βJ) as β→∞ for J>0,h=0. By continuity at least one positive-temperature crossing, not uniqueness. Exact enumeration over fixed finite pair justifies all-field analytic expansions through polynomial algebra, not an infinite graph-class claim.

## originality

PASS

Vinci et al 2014 establish the general bivariate Ising-polynomial graph framework and discuss spectral refinements, not this 25-vertex Latin-square pair or exact order-eight separation. Egan–Wanless already enumerate particular Latin-square plex invariants and Brouwer catalogs the two nonisomorphic strongly regular graphs; those do not determine exact Eulerian eight-edge subset differences or antiferromagnetic ground-state degeneracies. The prior Ising polynomial is the tool, not the new coefficient. A specialized precomputed Ising/Tutte polynomial table might cover the exact pair; disclosed as residual risk.

## value

PASS

The two nonisomorphic order-five Latin-square graphs are highly natural cospectral strongly regular examples. Their identical Ising coefficients through seventh order but first difference of precisely −48 Eulerian eight-edge edge-subsets is an exact thermodynamic discriminator with arbitrary uniform field. Reversed low-temperature order produces a mathematically forced temperature crossing in a finite system, a meaningful finite invariant beyond ordinary adjacency spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
