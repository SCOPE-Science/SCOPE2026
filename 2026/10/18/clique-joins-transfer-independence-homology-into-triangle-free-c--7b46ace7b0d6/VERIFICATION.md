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

# Verification and reproducibility

The proof in `RESULT.md` gives the full infinite-family argument and the integral equivariant representations without numerical assumptions. A standalone verifier `verify_clique_join.py` is also included to check finite examples from the defining forbidden triangles rather than feeding the formula into the enumerator.

Run `python3 verify_clique_join.py` in a Python 3 standard-library environment. The script independently constructs each finite graph and its exact three-clique-free faces, computes mod-two boundary ranks, enumerates base independence complexes separately, and tests signed Lefschetz numbers under six sampled products of rim symmetries and hub permutations in each cycle case. Expected terminal output appears byte-for-byte in `verify_output.txt`.

Cases: clique sizes two and three joined to cycles of length five and six; clique size three joined to a five-vertex path; clique size four joined to an independent three-vertex graph. These check homology multiplicities including mixed degrees and the zero higher-homology boundary. Signed Lefschetz tests verify rational traces on cycle examples, but do not verify all automorphisms or integral module equivalences in every finite case.

The finite checker establishes no general theorem or integral torsion statement on its own. The exact simplicial decomposition, equivariant homotopy pushout, cell attachments and integral long exact sequence in `RESULT.md` supply those deductions. Independent audit remains unperformed.
