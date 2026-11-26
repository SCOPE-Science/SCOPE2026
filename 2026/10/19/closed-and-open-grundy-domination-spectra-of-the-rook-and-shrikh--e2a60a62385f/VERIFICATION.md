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

The covered-set recurrence counts exactly the completed sequences: the neighborhoods contributing terms are precisely legal next vertices, each term increases coverage strictly, and the full set terminates with one empty continuation. A previously used vertex has zero gain, so this counts ordered distinct vertices without a separate exclusion condition. I rebuilt both graphs from their coordinates and directly traversed the sequence tree without merging states. The checks confirmed degree six, pairwise two common neighbors, and respectively eight and zero 4-cliques. In ascending length order, the rook-closed coefficients were (11712,114048,266112) at lengths 4–6, the Shrikhande-closed coefficients (192,10176,127296,492480,48384) at lengths 3–7, and both open cases (1920,103680,1658880) at lengths 4–6, with no others. These also give the four Grundy maxima. I additionally verified an explicit open-neighborhood incidence isomorphism in the replay. It acts by one bijection on selecting vertices and another on covered vertices; hence each open sequence has the same successive gains and termination under transport. It does not preserve closed neighborhoods.

## originality

PASS

Credit the exact coefficient lists and quantitative closed/open comparison. Do not credit equality of the open spectra as an independent new fact: it follows immediately from the prior isomorphism of bipartite double covers, even though the older source does not state sequence polynomials. Likewise the closed rook lower bound six and the general sequence frameworks are prior; the full coefficient comparisons, not the bare equal-open assertion or endpoints, are the distinct contribution supported here.

## value

PASS

This canonical minimal strongly regular parameter collision permits a comparison that holds size, degree and pairwise intersection parameters fixed. The complete ordered sequence counts quantify what closes differently: the closed rook case has no completed triples or length-seven sequences, while Shrikhande has 192 and 48384 respectively, with different coefficients also on their shared support. The independently useful exact invariant consists of the three distinct polynomials; value is not assigned to recomputing the known consequence that the open spectra coincide or to recovering the rook lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
