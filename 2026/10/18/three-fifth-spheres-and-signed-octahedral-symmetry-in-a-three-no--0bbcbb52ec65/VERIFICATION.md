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

# Reproducibility and verification

Run `python3 check_oct_nm3.py` using the Python 3 standard library only. The graph is constructed independently as the complete tripartite graph with three two-vertex parts, so no pretrained lookup table is used. The checker derives all forbidden three-edge perfect matchings; checks the exact eight-to-twelve cube incidence and every one of the 256 possible dual-nerve subsets; enumerates all faces; constructs 847 elementary acyclic matching pairs and explicitly topologically sorts their entire oriented Hasse diagram; independently computes characteristic-two boundary ranks; and tests the signed reduced Lefschetz character on each of the 48 automorphisms against the formula in the result. The exact execution output is embedded as `verification_output.txt`.

The proof uses integral combinatorial Alexander duality, the nerve lemma, a direct homotopy description of the cube independence complex, simple-connectivity fillings, Hurewicz and Whitehead. The computed mod-two ranks and Morse data corroborate this proof but do not alone substitute for it. The character comparison is a complete finite 48-element group check using exact integer sums, not statistical sampling. No claim is made for larger multipartite graphs or for universal torsion phenomena.
