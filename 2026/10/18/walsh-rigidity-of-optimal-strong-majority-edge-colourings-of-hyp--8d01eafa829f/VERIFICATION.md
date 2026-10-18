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
# Reproducibility and scope

The proof in `RESULT.md` is symbolic and applies to every integer \(d\ge2\). The supplied Python 3 checker uses only the standard library. Run `python verify_hypercube.py` alongside this file.

The checker independently constructs the undirected edge set of each hypercube, its edge-neighbourhood relation, and the explicit parity-sign colourings. For \(d=2,3\) it compares the formula against **every** assignment of two named signs to the edges. It further verifies all \(2^d\) prescribed sign patterns and translation orbit sizes for each dimension through eight. The exhaustive cases produce counts \(4\) and \(8\), and all larger finite tests pass.

These checks do not exhaust all edge assignments in dimensions at least four and do not certify novelty. Completeness in every dimension is a mathematical consequence of the Walsh eigenspace decomposition and edge-sign reconstruction. The orbit conclusion uses the proved action of translations and coordinate permutations; it does not rely on finite orbit enumeration. Independent audit has not been performed.
