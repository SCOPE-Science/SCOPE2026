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

# Exact reproducibility

Execute `python3 verify.py collapse_templates.json` with Python 3. The output file `verification_output.txt` records the actual run. No packages are required beyond the standard library.

The program checks an exhaustive 170-element normalized face-orbit poset with the bounded integer witness-center criterion. It replays 58 free orbit-pair deletions down to 54 core types and checks complete concrete complexes at five distinct orders. It constructs the fundamental four-cycle over \(\mathbb F_2\), the cut cocycle, the cap-product chain, and a closed dual-facet loop whose three-cochain evaluates oddly on the octahedral three-cycle. These data prove a nonzero degree-one times degree-three cup product. The universal proof additionally uses the explicit bound \(n\ge17\), guaranteeing that the local integer residues and adjacency tests do not wrap ambiguously.

This is finite exact computation plus a mathematical reduction of the infinite family, not an exhaustive execution for infinitely many sizes. This package has not undergone independent mathematical audit.
