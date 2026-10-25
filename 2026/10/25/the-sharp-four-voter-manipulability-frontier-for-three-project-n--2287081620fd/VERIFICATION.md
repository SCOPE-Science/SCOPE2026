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

# Verification of the finite frontier

Run `python verify.py` with Python 3.11+ and the pinned dependency in `requirements.txt` (`python -m pip install -r requirements.txt`). The program verifies Nash optimality using exact Karush–Kuhn–Tucker marginal-score equalities and inequalities, not numerical optimization. It enumerates 329 anonymous count profiles across one through four voters and all truthful ballot types and other nonempty misreports. For each report, it enumerates all vertices of the Nash-optimal allocation face to test the true utility under any permitted tie-break.

Expected checked profile counts: 7, 28, 84, 210. Expected manipulable counts: 0, 0, 0, 6, with 12 profitable ballot-type/report-type pairs at four voters, two project-relabeling orbits and exact gains \(5/4\) and \((9-\sqrt{17})/4\). Rational optimality certificates lie on a denominator-24 grid except three symmetric four-voter profiles whose exact optimum has \((7-\sqrt{17})/16\) in two coordinates. The code certifies these exceptional points algebraically and terminates with `All KKT, face-vertex and deviation checks passed.`

The grid is a means to locate certificates: each returned point is independently checked against the necessary and sufficient global concave-optimality conditions; absence of a grid point is not used as a mathematical impossibility inference. The all-voter-count two-project strategyproofness claim is proved analytically and is not based on finite checking. Independent audit and independent validation have not been performed.
