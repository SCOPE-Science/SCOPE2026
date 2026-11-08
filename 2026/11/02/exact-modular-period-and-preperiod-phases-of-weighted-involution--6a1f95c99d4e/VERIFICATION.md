---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The theorem classifies the least eventual period and first periodic index of T_c(n)=T_c(n-1)+c(n-1)T_c(n-2) for all integer c, moduli M>=2 by prime-power binomial-shift valuations and recurrence-based lower bounds. For v2(c)>=2, the j=1 binomial term has exact valuation r+v2(c)-1 and all higher terms are divisible by 2^(r+v2(c)); for v2(c)=1 cancellation of j=1 and j=2 gives period 2^max(2,a-1); for odd c the valuations of T_c(4k),T_c(4k+1) equal k and the next two are at least k+1, hence preperiod 4a-2. The displayed Step 5 identity for T_c(4k+4) in RESULT.md IS FALSE: at c=3,k=0 it predicts 54 while the recurrence gives 46. Direct recurrence algebra gives the replacement T_c(4k+4)=(4k+2)c T_c(4k+1)+(1+(4k+3)c)T_c(4k+2); the second coefficient is even for odd c, so the published valuation conclusion still follows independently. Checked 1975 small (c,M) exact period/preperiod pairs. Scientific statement survives this corrected derivation, but a corrected complete RESULT.md is necessary before publication.

## originality

PASS

Kim and Kim (2009) explicitly cover c=1 and portions of the weighted involution polynomial; broader shift congruences from Bednarz and Wolowiec-Musial 2019 and Kallat 2026 overlap odd-modulus arguments and bound some periods. The assessed new fact is exact all-modulus minimal dyadic period for nonzero even c, especially v2(c)=1 vs >=2, plus the all-index exact shift valuation. Full primary-paper review was blocked by inaccessible PDFs/Oxford VPN; comparison qualified.

## value

PASS

Exact least periods and preperiods of weighted matching enumerators are natural arithmetic invariants. The cancellation-driven discontinuity at c≡2 mod4 versus 4|c is a meaningful general phase classification not explained by the unweighted case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
