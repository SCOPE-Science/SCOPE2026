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

The accompanying `verify_rs_sunflower_q7.py` reconstructs the finite instance from first principles over \(\mathbb F_7\). It checks:

- all ordered 5-tuples of distinct field elements generate exactly 60 distinct \([5,3]_7\) Reed--Solomon row spaces;
- affine-normalized vectors \((0,1,a,b,c)\) give exactly the same 60 codes;
- among the 1770 unordered code pairs, exactly 1200 have intersection dimension \(1\) and 570 have intersection dimension \(2\);
- the resulting compatibility graph is 40-regular;
- the ten displayed evaluation vectors form a clique;
- exhaustive Bron--Kerbosch enumeration finds maximal-clique histogram \(\{6:30,7:1920,8:5070,9:1800,10:138\}\), so no clique has size greater than \(10\);
- a separate exact branch-and-bound maximum-clique routine also returns \(10\).

Replay command: `python3 verify_rs_sunflower_q7.py`. Expected final line: `VERIFY_OK`.

Limits: this checker proves only the finite \((5,3,7;1)\) instance. It is not evidence for an infinite-field formula. The literature comparison is not independently audited, and independent validation has not been performed.
