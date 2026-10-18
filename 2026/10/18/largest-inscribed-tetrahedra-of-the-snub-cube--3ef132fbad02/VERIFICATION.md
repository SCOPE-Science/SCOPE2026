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

# Verification of the contained-tetrahedron result

Run `python snub_exact_verifier.py` in a directory containing the included script. The script uses only standard-library `fractions`, `collections`, `itertools`, and `math`. It checks that there are \(24\) distinct vertices, exhausts \(\binom{24}{4}=10626\) distinct four-vertex subsets, checks every absolute determinant against the sharp candidate with exact root-isolating rational intervals, and counts exactly \(24\) maximizers. It determines the \(80\) three-vertex support triples, with multiplicities \(72\) having one maximal apex and \(8\) having three, then checks the unique special triple per maximal vertex tetrahedron, the supporting-plane strictness of all eight variable-apex faces, and one rotation orbit of the eight equality families.

The included source is the complete dependency-free certificate: all assertions must succeed before the final `all_exact_checks_passed` message. The finite computation is combined with the determinant's separate affinity in each argument to establish the **global**, continuously quantified theorem, including movable nonvertex apices. The proof does not substitute random sampling for exhaustive reasoning.

The polynomial \(\tau^3-\tau^2-\tau-1\) has one real root; the rational interval endpoints are certified by opposite signs, and a cubic-derivative argument establishes uniqueness. The comparator bounds each coefficient term on this interval, so all reported strict determinant and facet-plane signs are exact.

No independent audit has been conducted. Verification is restricted to the stated snub-cube normalization and is not a certified solver for unrelated solids.
