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

The frozen RESULT.md had undefined ring indices C_m: it defined C_0,...,C_{m−1} but used C_1+Σ_{j=1}^m C_j and Σ_{j=1}^m again in pairing. Fully corrected both occurrences in a complete UTF-8 RESULT.md: c_m=C_0^(1)+Σ_{j=0}^{m−1} C_j^(2), φ_m(c_m)=m^-1Σ_{j=0}^{m−1}η_m(C_j^(2))=1. All m rings in each triangulated annulus are homologous, with disjoint edge supports; [c_m]=γ1+mγ2 is primitive, each deletion of <m edges leaves at least one ring in each annulus, so MHC≥m. The seam cocycle η has 1 on each of m ring wraparounds plus m−1 matching diagonals, δ η=0, each ring pairing 1 and ||η||_1=2m−1. Scaling by 1/m on the second annulus gives LP≤(2m−1)/m<2, so the ratio >m/2 unbounded. Independently verified all triangle cocycle equations and ring pairings m=2..12; analytical cut proof covers every m≥2. The unchanged source CHECK script also uses the corrected zero-based index domain. No claim LP optimality.

## originality

PASS

Hoefgeest–Slot formulate MHC as minimum cocycle support and LP minimizing ||φ||_1 with φ(c)=1; their SoCG 2026 Example 6.3 shows finite non-tight ratio 2, not an all-m planar primitive-chain unbounded gap in inspected conference material. The present double-annulus family proves ratio >m/2 with primitive [c_m]=(1,m) even when chain coefficients ±1. Maxwell–Nayyeri and Chambers–Erickson–Nayyeri study distinct flow/cut formalisms and do not mechanically imply this LP separation. Search of Resultary exact-table topics uncovered no equivalent annulus family; full arxiv draft inaccessible leaves coverage risk.

## value

PASS

The natural unweighted ℓ1 relaxation for minimum homological edge cuts has no constant integrality-gap bound even for planar simplicial complexes and primitive integral ±1-support cycles. An explicit seam cocycle and edge-disjoint cycle-packing witness exposes the obstruction, of direct potential use in LP-approximation and algorithmic-topology research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
