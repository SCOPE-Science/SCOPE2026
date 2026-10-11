---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

For \(1<p\le2\), substituting \(u=\lambda x\) and \(v=(1-\lambda)y\) into Clarkson's inequality gives the claimed unrestricted upper bound. Two normalized disjoint indicators have unit norm, satisfy the Birkhoff--James definition for every real scalar, and attain both weighted norms exactly.

For \(2\le p<\infty\), Hanner's inequality gives the unrestricted upper bound. With disjoint unit indicators \(e,f\), the balanced pair
\[
x=2^{-1/p}(e+f),\qquad y=2^{-1/p}(e-f)
\]
has unit norms. The smooth \(L^p\) duality pairing of \(x\) with \(y\) vanishes because the two disjoint pieces cancel, so \(x\perp_B y\). Direct substitution gives both weighted norms with \(p\)-th power
\[
\frac{1+|2\lambda-1|^p}{2}.
\]

At \(p=1\), disjoint indicators attain the triangle upper bound \(1\). At \(p=\infty\), the two-valued pair \(x=e+f\), \(y=e-f\) satisfies
\[
\|x+t y\|_\infty=\max\{|1+t|,|1-t|\}\ge1
\]
for every real \(t\), and both weighted endpoint norms are \(1\).

No numerical experiment, truncation, or finite enumeration is used to prove the quantified theorem. The main unresolved verification risk is bibliographic rather than mathematical: the focal preprint's full body was inaccessible, so exact whole-document noncoverage is not asserted.
