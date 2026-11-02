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

# Reproducibility and limits

Run `python verify_double_cover.py` in an environment with `networkx` installed. The program constructs the original clique-bouquet graph and its canonical double cover directly from adjacency lists, then enumerates all their automorphisms using NetworkX's general graph-isomorphism iterator. The eleven explicit parameter lists include the single-blade case, mixed blades, three triangular blades, and larger peripheral cliques; it checks that both automorphism orders and the expected-group index agree with the theorem.

The expected final line is `VERIFY_OK cases= 11`. A program execution on the packaged source returned exactly that line. These checks are finite; the all-parameter result depends on the component and group-action proof in `RESULT.md`. The script does not establish results about untested clique sizes, nor does it establish publication priority or independence of any external assessment.
