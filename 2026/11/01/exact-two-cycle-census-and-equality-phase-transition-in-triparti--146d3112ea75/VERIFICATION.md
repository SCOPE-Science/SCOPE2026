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

# Verification and reproducibility

The scientific claim is the exact number of primitive temporal two-cycle orbits of synchronous strict-neighbor majority, with tie retention, on complete tripartite graphs of all positive part sizes. All hypotheses, strict boundary inequalities and count normalization are specified in `RESULT.md`.

To replay finite evidence, run:

```sh
python3 verify_tripartite_recurrence.py
```

No third-party packages are needed. The program performs two independent enumeration strategies: direct binary-state majority on 89 sorted part-size triples (1,236,504 labelled state tests) and a weighted part-count update on 1,137 triples. Every comparison of actual and closed-form primitive two-orbit counts passed. The output file `verification_output.txt` is an included replay result and can be regenerated from the program. The program also checks a known fixed-state count as an auxiliary consistency test; that is not part of the new originality claim.

The infinite-parameter proof is mathematical, not empirical: changing parts must be uniform, one toggler is impossible, two togglers require opposite phase and equal sizes, and three togglers require a unique largest part. The open inequality is essential, including ties and smallest allowed sizes. The stated test ranges are finite; neither exhaustive checks nor a successful log establishes originality or an all-size theorem on its own.

Independent audit has not been performed.
