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

# Computational reproducibility and scope

The proof is mathematical and applies to arbitrary finite projective planes. Two different finite checks serve as corroboration only.

`verify_local.py` constructs the incidence graphs of \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\), enumerates all \(2744\) and \(17576\) ordered triples, and verifies that geometric three-tuple types determine fourth-vertex atomic adjacency/equality spectra. It also checks attainable geometric triple types after any ordered pair and the corresponding one-vertex profiles. Both planes produce \(48\) matching coloured geometric triple types, \(8\) pair types and \(2\) one-point types. The full console output is `local_output.txt`.

`verify_ef.cpp` independently evaluates bottom-up exact graph-language quantifier-rank-four types over all vertices of \(\mathrm{PG}(2,2)\), \(\mathrm{PG}(2,3)\), and \(\mathrm{PG}(2,5)\), allowing repetitions and all equality/adjacency diagrams. After forming fourth-vertex spectra, the number of three-vertex one-step types is \(24\) in every tested plane, and the complete empty-tuple rank-four types coincide. The full output is `ef_output.txt`.

Run `sh reproduce.sh` with Python 3 and a C++17 compiler. The script compares new console output against the two included output files. No network access or external datasets are required. These finite tests do not prove the infinite order-uniform assertion, which is established by the explicit geometric case argument in `RESULT.md`. No external mathematical audit or formal proof certification has been performed.
