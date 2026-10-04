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

`verify.py` reconstructs the finite optimization from definitions. It creates all increasing triples, defines conflict exactly by coordinatewise distance at most \(2\), verifies the explicit 52-triple witness, and asks SciPy's HiGHS mixed-integer solver for a complete optimum with zero requested MIP gap.

As a model sanity check, the same code reconstructs all published exact values for \(3\le n\le12\): \(1,2,3,6,9,13,18,24,32,41\). It then obtains \(52\) at \(n=13\), where there are 286 candidate triples and 2255 conflict pairs.

The computation is exhaustive only for these finite instances. It does not prove a formula for larger lengths, uniqueness of the optimum, or any asymptotic statement. The numerical optimizer uses integer variables and integral constraints; verification additionally checks the returned solution and explicit witness combinatorially.
