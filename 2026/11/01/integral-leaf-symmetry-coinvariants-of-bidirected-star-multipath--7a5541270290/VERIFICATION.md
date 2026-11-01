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

`verify.py` is standalone except for SymPy. Run it with `python verify.py` from the directory holding this document. It builds the crown graph for \(m=3,\ldots,8\), obtains a fundamental integral homology basis via a spanning tree, constructs the diagonal group action on that basis from a transposition and a full cycle, then computes the Smith normal forms of the corresponding coinvariant matrices. The printed results are order-two torsion at three and four leaves, and trivial coinvariants for five through eight leaves. It also verifies integral generation by four-cycles for each tested \(m\ge4\).

These tests were executed successfully on the embedded source. The infinite theorem is established separately by the four-cycle-generation proof and five-label relation. No computer calculation was used to infer higher-size validity, and no independent audit has been performed.
