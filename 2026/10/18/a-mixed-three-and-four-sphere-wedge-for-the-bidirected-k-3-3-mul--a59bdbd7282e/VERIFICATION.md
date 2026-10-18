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

# Reproducibility and limits

Run `python3 verify_bidirected_k33.py` followed by `python3 verify_symmetry.py` with SymPy installed. Their expected complete outputs are in `multipath_check.txt` and `symmetry_check.txt`.

The first program enumerates all nonempty arc subsets on exactly eighteen arcs and proves via the explicit face predicate that precisely 714 are multipaths. It constructs 341 discrete-Morse face pairs, tests the exact directed Hasse graph for cycles, and computes all signed four-to-three critical incidence coefficients. The second independently constructs the exact integral fourth simplicial boundary and computes all automorphism traces using rational linear algebra. Together they establish the stated finite theorem; they make no claim about any larger family.

The SymPy calculation uses exact arithmetic, not floating point or probabilistic rank estimates. The separate mod-two calculation checks homology dimensions but is not used to infer the integral attaching maps. The verification does not constitute independent external review.
