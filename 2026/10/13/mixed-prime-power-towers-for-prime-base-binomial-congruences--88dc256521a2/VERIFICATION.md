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

For j≥1 Jacobsthal's modulus at a=q^{t+1}p^{j−1}, b=q^t p^{j−1} has valuation at least 3j. Thus the binomial limit exists, whether or not it is a unit, and its precision at B_j is at least p^{3(j+1)}. LTE gives a p^{m+1} tail for q^{p^m}→ω_p(q), so the p-part is precisely r≤ν_p(β−ω_p(q)^{q^t}), with infinity interpreted as equality. For r≤3 use B_0 and q^{p^{r−1}} at that precision. Legendre's valuation simplifies to s_q((q−1)p^r)/(q−1), and CRT gives the equivalence. At t=1 the positive digit sum is a positive multiple of q−1, including q=2. The frozen verifier and saved output were inspected, not executed. A fresh standard-library computation (branches/f5b0c272-e7a0-4375-a059-f39e3ea0c4b8/independent_check.py and independent_check.txt) directly checked both examples: at (31,5,1) B_0=B_1=251 mod 625, the target lift is 1, and 31^4=21 mod 25; the direct congruences agree through layer 3 and give residues 11501 versus 3751 at layer 4. At (19,7,2) the residues 215 and 19 mod 343 differ by 196, giving H=2, and both allowed digit sums are 18<36. The valuation argument, not finite enumeration, excludes all later layers in the examples.

## originality

PASS

Earlier coverage includes the exact r=1 mixed layer, the pure p^r tower, and the general dilation tool. These do not state a mixed higher-layer classification or the sharp arithmetic examples. A later published catalogue record gives an equivalent finite-compressed criterion on the same mixed family and includes the positive cubic example; this is substantive duplicate coverage of the criterion as currently indexed and is not to be counted as a distinct theorem. It is dated October 26, after the frozen October 13 record; the comparison does not adjudicate authorship or infer independent discovery. The earlier evidence checked does not give the complete mixed-tower statement with the sharp non-Wieferich cutoff and a separate p-adically allowed tower erased by the digit filter.

## value

PASS

For a motivated congruence, the result explains what survives prime-power lifting and what is removed by the independent digit condition. It gives a sharp cubic tower despite failure of the ordinary Wieferich condition, unlike the earlier pure-prime cubic criterion, and a separate genuine digit obstruction that deletes all layers allowed by the p-adic criterion. The value is this mixed behavior with exact boundaries, not a general bound on H or a re-computation of previously listed positive cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
