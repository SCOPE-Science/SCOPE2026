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

# Reproduction and limits

Use `python3 binary16_census.py` with Python 3. The program uses only integer arithmetic, exact comparisons, the standard library's `bisect` and `fractions`, and two graph-decomposition algorithms. Its complete domain is the 15,361 binary16 values in \([0,1]\) represented by codes 0 through 15360. Its built-in assertions give the exact cycle periods, basin sizes, shared recurrent atoms, total-variation fraction, and hash of each length-15,361 transition array.

Expected cycle/basin pairs: staged \((1,5092),(1,2),(40,10267)\); one-rounding \((1,15236),(1,8),(5,117)\). Expected maximum transient depths: 83 and 109. Expected sum of transient depths: 389795 and 712352. Expected limiting total variation: \(10267/15361\). The one-rounding period-five cycle has ordered bit codes 11709, 13625, 15113, 14026, 15313. The checker also verifies the endpoint rounding assumption for the staged evaluator.

For an optional independently evaluated cross-check run `python3 binary16_census.py --crosscheck` with NumPy installed. This compares all 15,361 staged transitions against separately executed binary16 operations and each one-rounding output against an exact-fraction nearest-neighbor check. All of those comparisons were performed and passed. Independent **external** validation has not been carried out. Exhaustive finite-state computations are a proof about this exact bounded domain only.
