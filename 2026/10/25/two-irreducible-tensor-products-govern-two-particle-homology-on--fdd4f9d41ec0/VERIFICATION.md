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

# Verification

`verify_rectangular.py` uses only the Python standard library. Invoke `python verify_rectangular.py` in a directory containing the standalone script. It independently constructs deleted-product cells and signed cellular boundary matrices, computes ranks over \(\mathbb F_{1000003}\), and tests signed simplicial/cubical Lefschetz traces against the relevant Specht character values on all conjugacy-class representative pairs. The sample set is \((3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6)\). The captured actual output appears in `verification_output.txt`, ending in `VERIFY_OK_RECTANGULAR_BIPARTITE_CONFIGURATION_H2`.

The calculations alone do not establish a result at arbitrarily large sizes, rational semisimplicity, or the cited maturity theorem. Those mathematical ingredients are justified in the proof and cited literature. Mod-prime ranks are cross-checks and not claims of absence of integral torsion. No external or independent scientific audit has been performed.
