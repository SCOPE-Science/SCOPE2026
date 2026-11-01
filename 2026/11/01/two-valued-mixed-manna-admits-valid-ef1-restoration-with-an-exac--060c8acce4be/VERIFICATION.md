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
# Mathematical verification

The proof in `RESULT.md` treats all finite numbers of agents, every real \(a,b>0\), empty bundles, final-chore transfers, and final-good transfers. The signed pair shortfall is defined with a zero threshold if neither eligible deletion exists. The chore branch verifies the recipient by newly removable chore and separates other agents according to whether they have an own chore or the designated agent has a good. The good branch verifies the former good-holder against every bundle. Each step preserves all other agents' EF1 happiness and every signed shortfall of agent \(1\) is nonincreasing.

The finite budget follows from each initial chore held by agent \(1\) and each initial good held by somebody else being moved at most once. When \(a=b\), the integer-score argument uses initial near-EF1 to trap all other scores in two consecutive integer levels; the low-score agent's final score equals the floor of the conserved average, proving shortest possible transfers. This is a symbolic all-size certificate, not a finite enumeration extrapolation.

# Reproducible exact checks

Run `python3 verify_restoration.py` with Python 3 (standard library only). The script checks all allocations of \(2\)–\(8\) signed items to \(2\)–\(4\) agents with both signs represented, seven integer ratios, and exact integer arithmetic. Every near-EF1 initial state is followed to termination. It asserts invariance of all unaffected agents' EF1 happiness, monotonicity of every distinguished-agent signed shortfall, the item-count bound, and the sharp equal-magnitude formula.

The observed run prints:

```
PASS: all finite states tested; near-EF1 cases 8331 total verified transfers 14259 both-direction candidates 608
```

The sample three-agent signed instance in `RESULT.md` was also checked exactly. These finite checks supplement, but do not establish, the universal proof. There is no claim of global optimal transfer count when the positive and negative magnitudes differ. No independent audit is asserted.
