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

The provided `verify_prism.py` is a standard-library-only, deterministic reproduction script. Run it with `python verify_prism.py` in the directory containing `prism_witnesses.json` and compare its stdout to `verify_prism_output.txt`.

The checker generates graph adjacency data rather than importing predetermined hyperedges. Breadth-first search supplies actual graph distances. A depth-limited enumeration generates simple paths and retains those whose lengths match the endpoint distance; their unordered vertex triples are exactly the monochromatic patterns to prohibit. Every finite witness is checked against the entire resulting list. The canonical-labeling backtracker considers each unlabeled palette partition by first-occurrence color names and exhaustively visits every possibility without time limits. It establishes a three-color obstruction on the linear five-column strip, plus lower bounds for every prism with three to nine columns. Four pumpable seeds are checked both before pumping and at several increasing lengths.

The finite checker cannot on its own establish an infinite-family formula. The proof relies additionally on the independently stated locality of six-column windows for cycle circumferences at least ten, and on the closed-walk repetition argument. Neither reviewer independence nor formal-machine certification is claimed. The scientific review is self-review only.
