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

# Reproducible integral and combinatorial checks

The standalone `check_four_cut_hypercube.py` script requires Python 3.10 or newer and SymPy. Run it directly with `python3 check_four_cut_hypercube.py` from the extracted package.

For \(Q_3\), the script enumerates all 38 connected induced four-sets, checks that their faces contain every triple, builds the full signed integral three-boundary matrix of size \(56\times38\), and obtains exactly 35 unit Smith entries and three zero entries. The signed two-boundary has rank 21. These calculations give the integral local group \(H_3(L(Q_3);\mathbb Z)=\mathbb Z^3\), with vanishing integral groups in degrees one and two.

The script independently enumerates four-sets and computes signed-boundary ranks modulo two for \(Q_3,Q_4,Q_5,Q_6\). The respective connected-four counts are 38, 280, 1360, 5360; the respective mod-two ranks of the three-boundary are 35, 255, 1231, 4831; and the predicted free ranks of the dual three-homology are 3, 25, 129, 529. It asserts all equalities and prints `FINITE_CHECKS_OK` if successful.

**Limits:** The finite-field checks alone cannot exclude odd torsion or prove an infinite-family theorem. Torsion-freeness and all-d validity follow from the integral local Smith computation, exact relative pair splitting, and the integral long exact sequence proved in the main text. This verification is not an independent audit.
