---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Translate into the difference span H. Rank three gives the affine simplex. In rank two put three points at 0,e1,e2; avoiding the three lines leaves (1,1),(1,2),(2,1), each giving a parallelogram after reordering. Equal character restrictions to H give proportional columns. Thus an invertible minor requires four different restrictions and each unordered local set has exactly (3^(d-r))^4 lifts, with unchanged Gram spectrum. Frequency translation is row-phase multiplication, and the count of (set, distinguished member) pairs is both four times the unanchored count and 3^r times the zero-anchored count. The independent exact calculation (column Gram traces plus Newton identities, not the packaged principal-minor implementation) reproduced the five planar polynomial multiplicities 16,4,16,16,4 in the order given. The first factors into t^2-9t+9 and t^2-7t+9, giving the stated extremes; the second has ratio 9, the third has cubic roots in (0,1),(4,5),(7,8) and so ratio >7; the remaining two are singular. In rank three all off-diagonal squared moduli are at least one by the integer root multiplicities, so tr(Q^2)>=76, tr(Q)=16. If the eigenvalue ratio is at most 7/3, scale into [1,7/3]; the derivative of (x^2+S)/(x+T)^2 is proportional to xT-S, so each coordinate maximum is at an endpoint and no interior coordinate attains the global maximum. The endpoint cases with 0 through 4 high values give 1/4,19/64,29/100,13/48,1/4. Only a single high value reaches 76/256, forcing spectrum (7,3,3,3) at equality and ruling out any smaller ratio. Of 2600 anchored simplex sets exactly eight have second characteristic coefficient 90 (tr(Q^2)=76), all with polynomial (t-7)(t-3)^3. The unanchored counts are therefore 16*9/4=36 and 8*27/4=54 before lifts. Independent replay: python3 /workspace/branches/d6c4f22c-73d3-47a5-b439-d187ec507290/census_replay.py; matching census_output.txt in that directory. Only the justified finite reduced spaces were enumerated.

## originality

PASS

Exact ternary four-point rank and singular-incidence tables were located, and an exact Riesz-ratio calculation for a line-plus-point support was located. None supplies the sharp squared spectral condition number or its multiplicity for the two cap supports. Tight-frame results on the same simplex exclude an orthogonal four-character basis but do not quantify the best non-tight basis. Credit here is for the new conditioning classification, not rank counts, existence, or tight-frame cardinality.

## value

PASS

The exact optimal Riesz ratio is intrinsic to a sampling support and measures whether its best exponential basis is numerically stable; the multiplicity tells how many distinct bases attain that stability. The two affine geometries are exhaustive at this size and their sharp ratios differ substantially. This is a motivated finite classification, with an analytic quantitative lower bound and exact arithmetic in precisely justified representative spaces, not just an arbitrary table or reproduced rank counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
