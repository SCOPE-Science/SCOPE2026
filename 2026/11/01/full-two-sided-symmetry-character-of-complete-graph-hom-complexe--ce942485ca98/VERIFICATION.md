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

# Reproducibility and mathematical scope

The executable `homkmkn_verify.py` requires Python 3 with its standard library only. From a directory containing this file and the source, run `python3 homkmkn_verify.py`; the expected full output is recorded in `homkmkn_verify_output.txt`.

For each of the four parameter pairs \((m,n)=(2,4),(3,4),(3,5),(4,5)\), the program exhaustively enumerates the product-of-simplices cellular faces, verifies that every integral signed cellular boundary composition is zero, computes homology dimensions by modular exact linear algebra, and enumerates all simultaneous group elements. For each action it obtains a cellular Lefschetz trace by separately following each actual stable cell and its orientation sign, then compares it with the closed formula derived in `RESULT.md`. The four full group sizes sum to 3,792. Separate exact integer averages check \(S_n\)- and \(A_n\)-fixed dimensions for those cases and also for \((3,6)\) and \((4,6)\).

These are **finite computational checks**, not a proof of a statement for unbounded \(m,n\). The universal proof uses the known sphere-wedge theorem, a general cellular orientation determinant, invariant cycle assignments, inclusion–exclusion, the Hopf trace formula and cycle-index identities. The boundary ranks are computed over a prime field as a finite consistency check, and no unsupported integral torsion or integral representation classification is asserted.

The checked output ends with the exact line `HOM_COMPLETE_GRAPH_EQUIVARIANT_CHARACTER_OK`. All scientific claims are subject to the proof's stated range and to bibliographic priority limitations. No independent audit has been performed.
