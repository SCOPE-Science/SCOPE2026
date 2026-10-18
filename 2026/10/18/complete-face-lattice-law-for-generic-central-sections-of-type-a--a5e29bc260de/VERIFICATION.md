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

# Reproducibility
The supplied `check_root_section.py` is a standalone Python 3 standard-library script. Run `python3 check_root_section.py` beside these documents. It uses exact rational arithmetic, enumerates admissible bipartitions for each \(3\le n\le7\), verifies the closed \(f\)-vector, checks every constructed section vertex against the complete family of root-polytope inequalities, and verifies facet affine ranks for three independent coordinate permutations per dimension. It independently counts the vertices on each of the 22 facets for \(n=5\) and checks the alternating-triple characterization. Observed terminal outputs: `ROOT_CENTRAL_SECTION_OK cases=15` and `A4_SECTION_FACET_SIZE_SPECTRUM_OK {3: 10, 4: 10, 5: 2}`.

The proof is symbolic and applies to all \(n\ge3\). The finite checker does not establish universality, uniqueness in the historical literature, or any independent validation. Exact `RESULT.md` definitions specify the ambient coordinate order, inclusion order and quantifiers.
