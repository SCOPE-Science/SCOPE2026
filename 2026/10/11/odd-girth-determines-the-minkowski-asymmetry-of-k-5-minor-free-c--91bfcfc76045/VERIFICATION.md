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

# Reproducible verification and its limits

The theorem is proved analytically in `RESULT.md`; finite computational tests are corroborative only. The self-contained `verify.py` requires Python 3 with its standard library. Run `python3 verify.py` from a directory containing that file.

The program enumerates every nonempty simple graph on two through five labeled vertices, except the excluded complete five-vertex graph; additional deterministic six-vertex graphs with fewer than ten edges; cycles of lengths five through eleven; four wheels; three complete bipartite graphs; and a disconnected mixed-cycle graph. Each test explicitly generates the cut-incidence vectors and chordless cycles, builds cycle and coordinate inequalities, evaluates their exact maxima/minima, and asserts both the claimed optimal facet ratio and the reflected containment for every cut against each inequality. Fractions are exact and no numerical tolerances are used.

Successful execution reports:

`EXACT_CHECKS_OK graphs=1288 cut_vectors=25286 facet_rows=23906 reflected_inequalities=1867540`

The finite suite does not exhaust all finite graphs, cannot establish that a graph with many edges avoids all forbidden minors unless the chosen test family guarantees it, and does not replace the Barahona–Mahjoub facet theorem. No separate independent audit has been performed. The full proof does not rely on experimental completeness.
