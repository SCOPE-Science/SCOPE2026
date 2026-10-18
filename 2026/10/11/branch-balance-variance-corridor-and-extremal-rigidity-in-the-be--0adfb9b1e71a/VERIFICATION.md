---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The actual RESULT.md at blob 4c4f232f gives X′=λX+(1−λ)S and Y′=γY−(γ−1)S. Stationarity gives E X=E Y=E S=m, and Var(S)=1−m². Centered covariance identities and Cauchy–Schwarz give sqrt(Var X/(1−m²))∈[c,1], c=(1−λ)/(1+λ), and sqrt(Var Y/(1−m²))∈[d,1], d=(γ−1)/(γ+1), for |m|<1. Upper equality yields X=S or Y=S and, from stationarity of the opposite defect under multiplier λ or γ, support on the two fixed corners. Lower equality yields S′=−S and m=0, then X=−cS,Y=dS, with the branch admissibility precisely d+kc>0. |m|=1 forces corner Diracs by stationarity. The inspected verify.py symbolically factors the scalar inequalities and checks orbit/branch identities, but analytic stationarity supplies the proof.

## originality

PASS

Persson 2005 specifies the same Belykh normalization and parameter range, but its measure theory concerns existence/regularity rather than these exact all-invariant-law branch-moment corridors and their rigid equality classification. The later correction limits an unrelated absolute-continuity argument. The Resultary returned Belykh record is the identical claim, not evidence of earlier independent coverage; other stationary moment results concerned different maps. Under bounded primary comparisons, no covering theorem was identified; this is best-of-knowledge, not priority certification.

## value

PASS

This is an all-invariant-measure, parameter-sharp pair of statistical constraints on a canonical discontinuous hyperbolic map, with equality measures classified dynamically rather than merely numerical orbit evidence. It distinguishes corner invariant mixtures and branch-alternating two-cycles and provides a natural check on invariant-measure computations; this is structural dynamical information, not a trivial parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
