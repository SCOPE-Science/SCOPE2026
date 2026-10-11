---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

In real ell_4², smoothness makes x=(a,b) Birkhoff-orthogonal to y precisely when a³ y_1+b³ y_2=0. After normalization this gives y=c(b³,-a³) with c=(a¹²+b¹²) raised to (-1/4). The fourth-power expansions reduce the Du-Li i-angle objective to F(u)²=[1+3u-sqrt(1+2u+9u²+4u³)]/4 on u in [0,1]. Differentiation gives the stationary identity (1+9u+6u²)²-9(1+2u+9u²+4u³)=4(9u⁴+18u³+3u²-2). The quartic derivative is 6u(6u²+9u+1)>0 for u>0, so there is a unique critical root u0 in (0,1) and it is the global maximum. At that root the value simplifies to sqrt(1/6-u0²/2)=0.287390271399524... . Independent symbolic and high-precision checks reproduced the identity, unique root and value.

## originality

PASS

The defining Du-Li article was inspected in full. It defines C_B, proves general comparisons and the universal bound 0<=C_B<=3/4, computes square/hexagonal examples, and gives Radon-plane characterizations, but it contains no ell_4² evaluation. Its comparison C_B with older orthogonality constants is by inequalities, so an exact value of those different constants would not imply the audited value. Targeted Resultary searches for C_B on ell_4² and Birkhoff i-angle/cosine variants returned nearby Banach-space constants but no equivalent computation.

## value

PASS

The defining article introduces C_B precisely to quantify the discrepancy between Birkhoff and isosceles orthogonality. Computing it exactly on the canonical non-Hilbert smooth plane ell_4² gives a natural benchmark value and an explicit extremal geometry, rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
