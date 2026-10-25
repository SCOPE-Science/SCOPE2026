---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For every genus-4 F2 curve, its zeta numerator has degree 8 with functional symmetry c5=2c3, c6=4c2,c7=8c1,c8=16. The initial N1..N4 determine the first coefficients via exact Newton identities and hence N6=65−s6; Möbius inversion gives B6=(N6−N3−N2+N1)/6. The bundled DATA.b64 decodes to 620 distinct quadruples and all 620 were independently compared ENTRY-BY-ENTRY to the original Xarles repository ListCurvesGenus4p2.txt (original Git blob 99610bd76b48b74b1ebf59c2df8052ff74d6e278), with zero discrepancies. Independent integer coefficient recurrence over these tuples produced B6 histogram for values 1..19: (1,3,6,22,26,52,46,80,94,55,78,58,37,26,17,10,7,1,1). Unique minimum B6=1 occurs at (N1,N2,N3,N4)=(3,9,9,45), N6=21, L=1+2T²+9T⁴+8T⁶+16T⁸. This is conditional on Xarles Theorem 10 exhaustively realizing the 620 rational Jacobian isogeny classes, not a newly proved genus-4 curve census. For the explicit genus-4 Artin–Schreier curve y²+y=x⁹+x⁵+1, trace over F32 gives Tr(x⁹)=Tr(x⁵) and Tr(1)=1, so N5=N1=1, B5=0. Weil gives N7−N1≥126−72√2>0, and the published general bound yields B_n>0 for all n≥8 because (2^(n/4)−1)²≥9≥8. Hence every such curve has closed degree-n points for all n≥6 and some curve lacks a degree-5 point, yielding rho(2,4)=6. The finite 620-row enumeration proves only the conditional table extraction; no independent primary curve enumeration is asserted.

## originality

PASS

The exact genus-four degree-six minimum and eventual closed-point threshold are not stated in the two most relevant primary sources: Aubry–Herbaut–Monaldi classify rho(q,g) for g<=3, Xarles provides the 620-row genus-4 curve data. The synthesis computes a meaningful new sharply classified invariant while crediting the pre-existing data and genus-four degree-five witness.

## value

PASS

The exact uniform eventual degree threshold rho(2,4) closes the next natural genus case after the published genus-1/2/3 determinations and separates degrees five, six, seven and the tail. The sharp degree-six minimum and unique isogeny class are intrinsic, reproducible arithmetic facts a later researcher could use. Although derived from a known full census, the result is a motivated missing invariant rather than an arbitrary table rescan.

The dated certificate retains the supplied scientific assessment, sources and limitations.
