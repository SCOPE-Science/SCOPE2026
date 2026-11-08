---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Theorem 13 of Rampersad–Wiebe (2023) directly supplies the sum-to-binary-run-product identity, with S(0..3)=1 and recurrence S(l)=S(l-1)+S(l-2)-S(l-3)+S(l-4). The four-dimensional recurrence has determinant +/-1, so explicit state returns modulo 2 at step 5 and modulo 4 at step 10 prove full periodicity: run weights valuation 0 unless l=4 mod 5, valuation 1 exactly l=4 mod 10. Binary-run decomposition yields A(t,z)=(1+R)/(1-t(1+R)), hence G0=(1+t+t^2+t^3)/Q and G1=t^4(1-t^5)/((1+t^5)Q^2). For fixed v, every R_j is rational modulo 2^(v+1); the k=v term has the unique positive highest-order pole at rho, giving a_r(v)~c_v r^v rho^-r. Independently enumerated all binary words for r=0..12; zero- and one-valuation sequences matched (r=10 gives 881 and 138). Neither bounded check alone proves rationality or asymptotics.

## originality

PASS

The published sum identity and zero valuation enumerator are prior. New assessment is valuation-one rational series and fixed-higher-v exact rational/asymptotic hierarchy.

## value

PASS

Higher divisibility strata of a natural published binomial parity sum form a meaningful arithmetic refinement. The squared pentanacci denominator for valuation one and polynomial r^v inflation at every fixed valuation provide exact quantitative information for infinitely many indices, beyond the previously known parity baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
