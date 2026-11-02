---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The arithmetic-mean absolute-deviation BMOd seminorm has denominator 1/2 on every jump e^(m) (bounded range and interval [1,2m]). For Ce^(2), starts s>=4 have range at most 1/2, hence oscillation <=1/4. Starts s=1,2,3 with t>=128 have oscillation <=4H_t/(t-2)<4/21<1/4. Exhaustive exact rational calculation on the remaining 3x127 short blocks yields maxima 3371/13440 at [1,8], 76/375 at [2,6], 1663/13440 at [3,10]. For m=1, the [1,3] ratio is 14/27. For m>=3, interval [1,4m] and k=floor(5m/3) give L_m=1+H_k-H_m - (k/(4m))(1+H_4m-H_m). For 3<=m<=199 exact rational enumeration gives min L_3=167723/332640>3371/6720. For m>=200, harmonic integral comparisons and verified rational bounds log(997/600)>507/1000, log4<1387/1000 give L_m>6089/12000>3371/6720. Thus m=2 uniquely minimizes over all positive integers, with no infinite inference from finite computations alone.

## originality

PASS

The precise one-jump BMOd infimum alpha_d is introduced but not evaluated in Caldera (2026), §5.1, equations (74)-(75), where the universal inequality for decreasing sequences remains a conjecture. The sharp continuous inequality is distinct from the discrete benchmark. Full primary source comparison of Cesaro-minus-identity l^p operators does not cover the BMOd seminorm of Ce^(m). Available searches found no independently published exact alpha_d evaluation. This is a best-of-knowledge assessment, with residual bibliographic risks.

## value

PASS

The constant alpha_d is explicitly singled out in a primary research conjecture as the precise one-jump benchmark/necessary ceiling for any universal discrete reverse Hardy–BMO constant. Its exact evaluation over all jump lengths is a naturally motivated invariant, and the discrete optimizer m=2 differs from scale-invariant continuous one-jump extremizers. The result neither proves nor claims the universal conjecture for arbitrary decreasing sequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
