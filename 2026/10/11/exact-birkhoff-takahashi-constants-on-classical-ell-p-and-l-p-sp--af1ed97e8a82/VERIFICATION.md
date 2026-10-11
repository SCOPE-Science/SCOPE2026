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

The claim was checked from the defining supremum and not inferred from numerical samples.

For the upper bound, the verified chain is
\[
C_t^B(X)\le C_2^B(X)\le C_2(X)=C_{\mathrm{NJ}}(X)\qquad(-\infty\le t\le2).
\]
The first two inequalities are stated in arXiv:2608.07146v1, Proposition 2, and the last identification is part of the Takahashi normalization used there. Clarkson’s exact formula gives \(C_{\mathrm{NJ}}=2^{|2/p-1|}\) on the classical real \(L_p\) and \(\ell_p\) models.

For the lower bound, the witnesses were recomputed exactly. Disjoint unit vectors/functions give equal endpoint chords \(2^{1/p}\) for \(p\le2\). Balanced sign pairs give equal endpoint chords \(2^{1-1/p}\) for \(p\ge2\). Their Birkhoff orthogonality follows directly at \(p=1,\infty\) and from the standard norm-derivative criterion for \(1<p<\infty\). Because the endpoint chord lengths are equal, their power mean is independent of \(t\), so each witness works simultaneously for every \(t\le2\).

The focal preprint was inspected through all eighteen pages. The later isosceles-orthogonal exact-value paper was inspected at statement and implication level and was found not to cover Birkhoff–James orthogonality. Targeted database and prior-record searches did not locate an equivalent Birkhoff theorem. The remaining originality risk is an unindexed equivalent observation.

No computation, timeout, failed search, or inaccessible source is being treated as mathematical proof or as a proof of novelty. The range \(t>2\) remains unproved here.
