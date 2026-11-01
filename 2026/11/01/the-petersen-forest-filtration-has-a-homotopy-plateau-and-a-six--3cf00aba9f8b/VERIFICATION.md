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

# Exact reproduction and mathematical limits

Run `python3 verify_petersen_forest.py` in this directory. It must finish with `PETERSEN_FOREST_FILTRATION_EXACT_INTEGRAL_MORSE_OK` and produce the contents of `verification_output.json` as JSON. The certificate needs only the Python 3 standard library and deterministically reconstructs the ten graph vertices from unordered pairs of a five-element set.

It enumerates every one of the 1024 vertex subsets; independently tests the degree bound and forest property by union-find and by induced-component DFS with the Euler forest identity; verifies cubic regularity and common-neighbor parameters; reconstructs all four absolute repeated-toggle Morse matchings and their Hasse orientations; and performs an exact signed integer boundary elimination of all matched pairs. The critical cells after cancellation are: for bound 0, one 0-cell and four 2-cells; for bound 1, one 0-cell and one 3-cell; for bound 2, one 0-cell and one 3-cell; for bound 3, one 0-cell and six 5-cells.

The relative certificate acts on exactly 360 new simplices of the pair (bound 2 over bound 1). Its 179 matched pairs pass the full 960-incidence Hasse acyclicity test and leave critical masks 538 and 914, in degrees 3 and 4. Integer cancellation gives boundary coefficient -1, an isomorphism. The actual inclusion follows by the relative homology sequence and Whitehead's theorem, not from comparing abstract homotopy types alone.

An independent mod-two simplicial matrix elimination recomputes all absolute reduced homology ranks. These mod-two checks corroborate rather than replace the integral and homotopy certificates. The calculation proves an exact finite statement about the Petersen graph only; no general family or group-action claim is made.
