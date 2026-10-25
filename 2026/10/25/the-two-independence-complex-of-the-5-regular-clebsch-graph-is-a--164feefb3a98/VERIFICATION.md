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
# Reproducibility and evidence

Execute `python3 verify.py` in the folder containing `certificate.json`. Both files are complete and require only Python 3 standard-library support, including the built-in integer `bit_count()` method.

The verifier regenerates all sixteen even five-bit vertices and forty distance-four edges; exhaustively tests the exact induced-degree predicate for all 65,535 nonempty subsets; verifies the face vector and 2,142 complete face set; independently reconstructs the sequential element matching from its explicit pivot ordering and confirms the complete 1,070-pair set and two critical simplices. It then orients all 9,280 codimension-one face incidences, reverses the matched pairs, and topologically sorts the resulting directed graph, confirming acyclicity over all 2,142 faces. These checks reproduce a complete finite discrete-Morse certificate.

For automorphisms the verifier constructs each of the 16 even-bit translations composed with each of 120 coordinate permutations. It checks graph-adjacency preservation for every pairwise edge and computes the exact integral reduced Lefschetz number using signed fixed simplices. The 1,920 computed characters agree with coordinate-permutation parity, with 960 positive and 960 negative values.

The mathematical implication from the acyclic matching to the four-sphere is Forman's standard discrete-Morse theorem; the group structure is proved separately by the vertex-stabilizer argument in the result. The script does not certify novelty, does not independently audit the written proof, and does not extrapolate to graphs outside the finite specified domain.
