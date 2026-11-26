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

For a specified center and k selected pendant labels, deletion is a bijection onto all labeled trees on the m=n-k residual labels, with one tree if m=1. Thus every marked event has positive and equal probability and E S_(k,n)=n binom(n-1,k) tau(m)/n^(n-2). Reattaching makes the center a nonleaf; the other residual leaves are precisely noncenter labels absent from the uniform length-(m-2) Prüfer word. Joint absence of j designated labels has probability ((m-j)/m)^(m-2), so expansion in z-1 gives the displayed Palm PGF. At m=2 the empty word contributes one noncenter leaf; at m=1 there are only the k marked leaves. Summing over marked events identifies the Palm mean minus n p_n with normalized covariance. The initial gap is Var(L_n)/E L_n>0 by the star and path for n>=4. For m>=3, p_m<p_(m-1)<=1: the derivative of (x-2) log(1-1/x) is less than -1/(x(x-1)) for x>2, and the function extends continuously to x=2. Hence H(m)-H(m-1)=p_(m-1)+(m-1)(p_m-p_(m-1))<1, whereas H(2)-H(1)=1. This gives exactly the single terminal equality, and explains why it corresponds to stars. Finally p_m=e^(-1)(1+3/(2m)+O(m^-2)); for fixed k the two factors in covariance are n exp(-k)/k!+O_k(1) and k-(k+1)/e+O_k(1/n). Replay: frozen RESULT.md lines 43–95. The verification script was inspected but not executed; no finite check is used for the universal claim.

## originality

PASS

Credit is confined to the sharp comparison across bouquet sizes, including its unique forced boundary tie. There is direct same-day catalogue coverage of the exact covariance and leading coefficient in the common range, and prior coverage of the k=2 Palm law. The general vacancy formula follows from the known uniform residual tree. Neither the overlapping covariance formulas nor the Palm pruning mechanism alone are original here. No priority order is inferred from the same-day catalogue entries.

## value

PASS

The exact finite comparison answers how the conditional leaf-count enhancement changes with the degree of bouquet marking, rather than just whether pairs give enhancement. It distinguishes strict gain for every smaller increment from saturation at the star boundary; the covariance coefficients and vacancy counts alone are not the value justification. This is a modest structural result for a natural Palm ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
