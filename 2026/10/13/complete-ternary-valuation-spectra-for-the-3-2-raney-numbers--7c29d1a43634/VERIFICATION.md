---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Legendre formula exactly gives ν3(T_n)=(s_3(2u-1)-1)/2 with u=(n+1)/3^ν3(n+1). Partitioning 1..3^m by primitive u yields V_m=1+Σ_{L<=m} A_L. The units digit and 2-state carry matrix M(x)=[[1+x²,x],[x,1+x²]], initial row (x,1) and terminal (1,x)^T give A1=2,A2=3+3q and Cayley-Hamilton A_{L+2}=2(1+q)A_{L+1}-(1+q+q²)A_L. Summation gives ((1-qz)^2)/((1-z)(1-2(1+q)z+(1+q+q²)z²)). Pole-order extraction at z=1 gives fixed-j asymptotic m^(2j+2)/(2j+2)!; leading coefficients of A_L yield max valuation m-1 multiplicity m+1 for m>=2. Independently calculated exact T_n valuations on prefixes m=1..6, matching all recurrence coefficient vectors, e.g. m6 [28,140,267,216,71,7].

## originality

PASS

Within accessible evidence, Eu-Huang-Kao provide pointwise valuation and q=0 count, the 2019 Raney divisibility paper handles selected congruences, and OEIS lists terms; none of the actual inspected statements imply the complete two-variable valuation-spectrum rational generating series. The new transfer-matrix aggregation and fixed-j asymptotics are substantive. Explicit risk: highly relevant 2026 source full text was inaccessible when authorized Oxford VPN disconnected; this alone does not force O failure.

## value

PASS

Exact aggregate valuation frequencies for a canonical Raney sequence resolve every fixed-power-of-three divisibility count and supply sharp polynomial asymptotics and extremal counts. The rational two-variable series is a genuinely structural invariant beyond a finite table or the published valuation-zero layer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
