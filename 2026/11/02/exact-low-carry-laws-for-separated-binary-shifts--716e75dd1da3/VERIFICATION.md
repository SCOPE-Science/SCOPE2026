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

Run the included standalone \(`verify.py`\) with Python 3 and no third-party dependencies, using \(`python3 verify.py`\). It constructs the exact binary-carry automaton with rational probabilities and accounts for arbitrarily long carry chains beyond the highest shift bit via a geometric distribution. For weights \(1\) to \(7\), four sets of separated positions are tested at each weight (\(28\) shift families, \(140\) low-carry probabilities). Exact dyadic enumeration independently checks several small shifts. A below-threshold counterexample checks \(c_5=5/8\ne 11/16=c_9\).

Expected terminal output: `VERIFY_OK families 28 low-carry profiles 140`.

Finite checks are not a proof of arbitrary weights. The proof in RESULT.md uses independence of disjoint bit windows and counts every low-carry outcome via weak compositions. The density limit is justified using dyadic-cylinder approximation; no unproved ergodicity premise is needed. No external or independent audit is asserted.
