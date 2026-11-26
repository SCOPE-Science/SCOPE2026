---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For real depth-three leaf data with F_3(x) ≤ 1, fix folding signs ε and root mean-deviation signs s. The linear objective has coefficients ε_i(8s_i−Σs) and the maximum over s equals 64 times the folded root mean deviation. The 63 inequalities correctly encode the seven node bounds and the orthant, with eight free leaf variables and 24 nonnegative auxiliaries. For each certificate, nonnegative row multipliers give the required leaf coefficients, nonnegative auxiliary coefficients, and right-hand side at most 64, proving a bound for all real points in the sign region. Independent replay canonicalized all 4^8 colorings by subtree swaps and confirmed exact coverage by 1,540 supplied cases, and verified the multiplier identities, signs and bounds in rational arithmetic; maximum certified bound 64. The root bound also gives the four-leaf descendant bound by applying it to two identical copies of the four-leaf datum (no change in input tree BMO or folded root deviation). The two-leaf case follows from the reverse triangle inequality. Nonconstant nonnegative data give equality. Direct 16-leaf recomputation yielded F_4(x)=5 and F_4(|x|)=41/8, with only the folded root above 5.

## originality

PASS

Mohajer explicitly leaves the unrestricted rooted depth-three value and the least failing depth open; the earlier depth-four witness is not new. A separate Resultary record states the same theorem and uses the same cited example, with a materially different certificate formulation; it is listed on a later catalogue date. The mathematical overlap is established, but there is no evidence that this is prior coverage of the assigned result, or that either proof derives from the other. The distinct contribution relative to the verified prior literature is the depth-three bound resolving the threshold.

## value

PASS

This is the exact missing case of a specifically posed extremal problem. The four-leaf scalar bound and the known depth-four failure do not settle the eight-leaf inequality. The result fixes the first failing depth and the sharp last contractive constant, not just a sampled or approximate bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
