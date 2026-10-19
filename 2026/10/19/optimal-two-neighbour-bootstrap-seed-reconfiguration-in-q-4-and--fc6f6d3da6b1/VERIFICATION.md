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

# Reproduction and mathematical limits

Use Python 3.11 or later. Extract the files without changing their relative paths, then execute `python3 code/verify_direct.py` and `python3 code/verify_boxes.py` from the package directory. Only the Python standard library is required. Compare complete stdout to `evidence/direct-output.txt` and `evidence/boxes-output.txt` respectively. Both enumerators perform exhaustive rather than sampled searches.

The direct verifier generates every subset up to the minimum successful cardinality and iterates the two-neighbour infection rule synchronously to stabilization. It constructs both complete adjacency lists and partitions the state families into cube-isometry orbits via generators before breadth-first distance calculations. The alternative verifier uses internally spanned coordinate-subcube mergers instead of simulation, enumerates all complete coordinate-permutation/translation images of orbit representatives, and reconstructs distances from its own adjacency dictionary. Each program supplies its own count, edge total, eccentricity histogram and complete orbit-representative distance-layer data. The canonical accepted-seed list digest must match between programs.

The shared accepted-seed list hashes are `98038473d31775e85da42f0cba78cc0d8515c900edcc89fdd7fffffe07f6b99c` for \(Q_4\) and `359127dfbab8d1227813648543501eece0f7a72a546b826ff26e81f65ea2ce10` for \(Q_5\). In \(Q_5\), the exact slide graph has 120000 undirected edges, with eccentricity counts 960 at nine, 11200 at ten and 4800 at eleven. All 16960 vertices belong to one component.

The orbit argument is sound because binary translations and coordinate permutations preserve Hamming adjacency and therefore preserve both the two-neighbour update rule and the allowed exchange moves. Breadth-first search from one representative of each fully enumerated orbit determines the eccentricity of every vertex in that orbit. The calculation does not make claims for \(Q_d\) with \(d\ge6\); no independent external scientific audit has been performed.
