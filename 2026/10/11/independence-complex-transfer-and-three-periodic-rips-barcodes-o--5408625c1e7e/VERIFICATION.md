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

The claim is an exact all-parameter symbolic theorem under the displayed degree restrictions. Its critical distance assertions are justified by strict neighbor-intersection inequalities; these are not probabilistic or computational assumptions. The equality between \(\mathrm{VR}_{\le}(G;2)\) and \(\operatorname{Ind}(H)\) is simplex-by-simplex, following from the explicitly characterized pairwise distances. The zero integral first-persistence map is witnessed by the explicit oriented triangles and same-part fan in the proof. The cycle-factor calculation uses the established three-periodic path/cycle independence-complex recurrence and the join identity.

Reproduce the finite corroborations by running `python3 verify.py` with a standard Python 3 interpreter. The accompanying `verification_output.txt` reports seventeen exhaustive small cycle-factor parameter cases with \(5\le n\le8\), two irregular forbidden-edge examples, exact breadth-first graph distances, full independent-face enumeration, mod-two boundary ranks and support checks, and mod-two fillings of a fundamental-cycle basis. The implementation does not attempt symbolic topology or infinite certification; finite results do not imply the unrestricted case without the written proof. The published cycle homotopy formula is reused with attribution. No independent audit or external certification has been performed.
