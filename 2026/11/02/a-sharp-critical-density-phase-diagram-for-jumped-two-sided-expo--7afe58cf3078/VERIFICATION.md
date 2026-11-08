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

Independent reconstruction of the unitary integer Zak multiplier for g(t)=exp(-lambda t) on t>=0 and c exp(lambda t) on t<0 gives P/(1-rz)+Q/(z-r), P=e^{-lambda x}, Q=c r e^{lambda x}, r=e^{-lambda}. At z=-1 and 1 the reverse/ordinary triangle inequalities attain exact frequency extrema |P-Q|/(1+r) and (P+Q)/(1-r). Strictly decreasing P-Q and convex P+Q give the claimed optimal A,B and iff c<r or c>1/r. |Zg|² is real-analytic and nonconstant on connected cylinder, so its essential range is [A,B] with null level sets and no eigenvalues; elementary rational comparisons yield the unattained conditioning infimum. Independently sampled 293,020 Zak points for 4 lambda values and 7 amplitudes each and checked bounds/conditioning. Mesh is corroboration, not the universal proof.

## originality

PASS

Best-of-knowledge original contribution limited to complete claimed classification and quantitative threshold; classical ingredients and exact previously known special cases credited. Primary comparisons distinguish same mathematical objects from similar names; remaining equivalence risk explicitly documented.

## value

PASS

The family interpolates naturally between the one-sided critical-density Gabor frame and the continuous two-sided nonframe. A complete jump-amplitude frame/nonframe classification, exact operator spectrum, quadratic onset and strict condition-number bound quantify a meaningful design and stability boundary, not a random parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
