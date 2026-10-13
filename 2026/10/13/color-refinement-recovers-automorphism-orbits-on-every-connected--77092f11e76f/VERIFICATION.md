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
The theorem has a uniform proof for all finite connected graphs of cyclomatic number at most one. The accompanying `verify.py` provides an independent finite consistency check.

The script embeds graph6 representatives for all \(79\) connected Graph Atlas graphs on at most seven vertices whose cyclomatic number is \(0\) or \(1\). For each graph it:

1. checks connectedness and the cyclomatic number;
2. computes the stable color-refinement partition directly;
3. computes the automorphism-orbit partition by exhaustive testing of all vertex permutations; and
4. asserts equality of the two partitions.

It also constructs the explicit \(8\)-vertex bicyclic counterexample consisting of two triangles joined through two internal path vertices. The script verifies that its cyclomatic number is \(2\), that its stable color partition differs from its automorphism-orbit partition, and that the six degree-\(2\) vertices form one stable color class while splitting into two automorphism orbits.

The checker returns:

`VERIFY_OK atlas_graphs=79 n<=7 beta<=1 counterexample_beta2=PASS`

The embedded atlas check is finite and corroborative only. The theorem for arbitrary order rests on the universal-cover proof in `RESULT.md`. No external or independent certification is claimed.
