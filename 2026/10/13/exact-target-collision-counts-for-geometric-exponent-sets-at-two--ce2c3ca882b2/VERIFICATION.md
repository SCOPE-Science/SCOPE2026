---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The fixed total of n coins cancels the constant shift from b^i to b^i−1. For n≥3 the lower n−2 denominations must represent W=L+sP, with P=b^(n−2), L=1+⋯+b^(n−3) and s≥0. Normalize by carrying below the largest available lower denomination. The terminal coefficients are one at each lower position other than the largest, whose coefficient is 1+bs. Thus the minimum coin count is n−2+bs, which exceeds n for s≥1. When s=0 the canonical representation leaves two upper coins; their scaled target differences are 0 and ±(b−1). To spend the two extra coins below requires b=3 and exactly one reverse carry, because each reverse carry costs b−1 coins. It can split any of the n−3 eligible lower coins, leaves both upper positions empty, and has scaled difference −4. These classes are disjoint and count indexed vectors even if residues coincide. At n=2 the same three upper allocations are the whole problem, including M=1. A separate exact corroboration used the series product of (1−z x^(b^i))^−1 truncated to z-degree n: start H[0,0]=1, and for each denomination v iterate k upward from 1 through n and increment H[k,s+v] by H[k−1,s]. Filter the degree-n coefficients by the target congruence. All 2,625 cases with b in {3,4,5,7,12}, 2≤n≤8 and 1≤q≤75 agreed. This check is finite; the carry argument proves the full claim. The frozen checker source and recorded 1,911-case output were inspected, not executed.

## originality

PASS

The modular uniqueness framework and positional carrying are prior. Within the checked material the complete unweighted nonbinary fiber count, including its ternary one-split term, is a distinct claim. Neither the binary optimization theorem, the twice-each ternary theorem, nor the general cyclic exactness criterion evaluates this fiber.

## value

PASS

Exact all-ones isolation is the natural invariant in the cyclic extraction problem. The modulus family preserves all lower digits and leaves exactly two upper allocations to analyze, so the two-coin budget and exceptional ternary splitting are structural rather than an arbitrary parameter sample. The result computes every fiber in that family, not just Boolean validity, and makes no claim about unrestricted least moduli or transform speed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
