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

# Reproduction and scope

Run `python3 artifacts/verify_tripartite.py` followed by `python3 artifacts/verify_tripartite_mod3.py` from the package root. Only standard-library Python 3 is required. Expected exact outputs are in `artifacts/verification_output.txt` and `artifacts/mod3_output.txt` respectively.

The first program constructs all unordered two-point deleted-product cubical cells, checks \(\partial_1\partial_2=0\) over \(\mathbb F_2\), computes boundary ranks for part sizes \((3,3,3),(3,3,4),(3,4,4),(4,4,4)\), and checks every element of \(S_3^3\) and \(S_3^2\times S_4\) against both the oriented-cell trace formula and rational Specht character expansion. The second independently constructs signed boundaries and obtains ranks over \(\mathbb F_3\) for \((3,3,3),(3,3,4),(3,4,4)\), agreeing with the claimed rational Betti numbers. Degree-one \(\mathbb F_2\) Betti numbers exceed the rational values by one in these examples; this is compatible with, but does not establish, 2-primary torsion and is not used in the rational theorem.

These finite checks verify particular parameter values and signs. They cannot prove the general representation for untested sizes; that relies on the exact general argument in `RESULT.md`. None of this is an independent audit or a claim of machine certification for every parameter.
