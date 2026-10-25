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

The accompanying `check_liquid_profiles.py` uses exact integer arithmetic and the Python standard library. It enumerates **all** delegation functions on each labeled set of sizes 1 through 6 and checks the counts of distinct positive-length reachability matrices against the Cayley-tree and SET recurrences. For **every** resulting matrix it counts its exact preimage and checks the explicit formula \(\prod_a(s_a-1)!s_a^{b_a}\). It checks the connected-profile count for each size as well.

Exact results, in increasing order of sizes 1 through 6: total mappings \(1,4,27,256,3125,46656\); distinct approval matrices \(1,4,23,185,1942,25315\); connected matrices \(1,3,13,87,821,10023\). Additional computations at sizes 20, 50, 100 and 150 compare exact recurrence values to the analytic limiting constants.

Analytic premises checked in the proof: every component has one sink cycle; contraction and its reversal preserve precisely the approval matrix; the labels and direct child attachments explain all fiber multiplicity; \(T=ze^T\) has the stated square-root expansion at \(e^{-1}\); and the mapping-component EGF is \(-\log(1-T)\). The square-root transfer arguments, not finite enumeration, support general and asymptotic conclusions. This is a self-review; independent audit has not been performed.
