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
# Reproducibility and verification

`check_three_agent.py` requires only Python 3 standard library. Run `python check_three_agent.py` in a directory containing the extracted script. The program implements the specified epoch transition from scratch using `fractions.Fraction` and checks finite-time **exact** distribution inequalities against the closed-form theorem. It does not use floating-point arithmetic in the proof tests.

Actual check: `PASS: 96 distinct rational parameter pairs, 288 exact probability enclosures`. Four open-phase examples at \(a=3/5\) use \(\tau=1/3,9/25,2/5,9/20\); the predicted infection-count probabilities are respectively \((0,0,1)\), \((0,1/9,8/9)\), \((1/3,1/9,5/9)\), \((1/3,1/6,1/2)\). Exact boundary cases at \((a,\tau)=(18/25,2/5),(2/3,2/5),(8/15,2/5)\) test the inclusive threshold directions. The enumerated 24-epoch unresolved probability never exceeds \(0.0000594034\) across the tested cases.

A finite-horizon probability enclosure is *not* an infinite-time proof: unclassified paths are bounded by their remaining total probability and the theorem's infinite-time claim follows instead from the explicit first-appearance race argument, which resolves almost every infinite update sequence. The code does not certify bibliographic novelty or cover larger populations.
