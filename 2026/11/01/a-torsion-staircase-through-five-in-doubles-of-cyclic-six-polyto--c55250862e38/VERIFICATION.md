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
# Reproduction of integral homology

Use a Python 3 interpreter with `sympy>=1.12,<2` installed. Execute `python3 verify.py` from this extracted directory. The script imports no private data, downloads nothing, and deterministically enumerates the ten complexes and verifies every assertion. It reports `ALL_VERIFY_OK exact_homology_and_acyclicity m=7..16` on success.

The verifier implements Gale-evenness enumeration and exact disjoint-pairing construction, a complete acyclic simplicial matching check over the entire Hasse graph, the signed integral Morse differential by projection along matching gradient paths, exact Hermite/Smith normal forms over the integers, and an independent mod-two rank computation on the unreduced simplicial chain complex for each parameter. All values in the finite theorem are asserted by executable comparisons. Modular ranks are corroboration; they are not substituted for integral Smith normal forms.

Scientific limits: only the finite parameter range \(7\le m\le16\) is proved, and only integral homology is classified. This does not determine higher homotopy types or establish a theorem for all cyclic polytopes. No independent mathematical audit has been performed.
