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

# Exact finite verification

The scripts `verify.py` and `independent_check.py` are standalone Python 3 programs requiring no external dependencies. Execute them in this directory. Their deterministic standard output is included as `verify_output.txt` and `independent_output.txt`.

`verify.py` enumerates all \(65,536\) subsets of the sixteen vertices of the four-dimensional cube, tests the definition of both forest complexes, reconstructs signed boundaries over \(\mathbb Z\), and eliminates every nonzero matrix entry with unit pivots using integral elementary operations. This certifies that all nonzero invariant factors of the degree-two forest complex's boundary maps equal \(1\), independently of field-only calculations. It checks the chain identity, all boundary ranks, exact face counts, the terminal complex's mod-two ranks, and the mod-two inclusion rank.

`independent_check.py` uses a separately written depth-first-search cycle oracle rather than the disjoint-set oracle of `verify.py`, and independently confirms all face counts and the complete two-skeleton.

The theorem's homotopy upgrade uses the complete two-skeleton, integral homology, Hurewicz and Whitehead. The target's rational Betti number uses the mod-two upper bound together with Euler characteristic. The inclusion's rational rank follows from its full mod-two rank together with universal coefficients. No generalization to other graph dimensions, and no integer-surjectivity assertion for the inclusion, is claimed.
