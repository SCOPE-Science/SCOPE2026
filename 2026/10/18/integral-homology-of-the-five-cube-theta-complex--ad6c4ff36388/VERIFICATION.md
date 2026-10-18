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

# Reproduction instructions

Extract this package without renaming `VERIFY_Q5.py`; execute `python3 VERIFY_Q5.py` with Python 3.10+ (only the standard library is used). The verifier runs through every independent vertex subset, not a subsample, and checks its own output against `critical_faces.json`'s recorded critical masks and polynomial.

The executable validates the following independent proof obligations: exact list of \(254475\) independent subsets including the empty set; disjoint matching coverage of all \(254474\) nonempty faces by \(127231\) pairs and \(12\) critical faces; critical dimensions \(0,5,7\) with multiplicities \(1,1,10\); all \(99497\) permitted gradient transitions between matched pairs; and a complete topological elimination of all \(127231\) vertices in the transition graph, proving no directed cycle. It independently recomputes the independence polynomial using the vertex-deletion/closed-neighborhood recurrence and checks reduced Euler characteristic \(-11\).

The usual integral cellular Morse theorem supplies a CW model with no adjacent nonzero cell dimensions. Thus all integral boundary maps vanish; combinatorial Alexander duality on \(32\) vertices transfers the resulting integral cohomology to theta homology with shift \(29-i\).

Limits: a complete homotopy type of theta or of the independence complex is not certified; no external independent audit was carried out. The independent-polynomial check verifies counts, whereas the exhaustive gradient-graph check verifies acyclicity. Running tests over finite coefficient fields alone would not be enough for the claimed integral homology; the nonexistence of adjacent Morse dimensions is the decisive integral argument.
