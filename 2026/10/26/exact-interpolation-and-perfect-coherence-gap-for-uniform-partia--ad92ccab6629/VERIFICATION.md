---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the exact operator and complete uniform support in RESULT.md:4–20, T is monotone and extensive on this iteration (choose U empty, noting the empty-set value is nonnegative). The candidate F(s)=max_{m>=0}{mr−(mk−s)_+} majorizes d0 and has F(0)=0. It is nondecreasing and 1-Lipschitz, and superadditivity follows by adding maximizers and using (a+b)_+<=a_++b_+. Splitting U into its intersection with S and its excess shows T(F)=F; the bounded increasing integer iteration therefore stabilizes below F. At a fixed point, adding disjoint certified sets is superadditive and shrinking by b elements loses at most b, by taking U equal to the certified set in T. For s<k extend to a k-set and shrink; otherwise take q disjoint k-sets and, if t>k−r, one extra k-set containing all t leftovers with overlap k−t. These constructions attain F, whose maximum over m is qr+(t−(k−r))_+, including r=k and s=0. For D, a feasible complement has size at most k−r, since any k−r+1 elements can be extended to a k-set; maximizing the complement inside S gives D=(s−(k−r))_+. The exact ratio at n=2k−r and the limiting ratio and linear difference follow; in fact D<=(k/r)F follows directly by splitting on t<=k−r. Replay is analytic via RESULT.md:22–50. The frozen VERIFICATION.md and verify.py describe 5,630 finite subset cases, which were inspected rather than rerun and are not the general proof.

## originality

PASS

Pass applies to the exact all-cardinality iterated-interpolation classification and quantitative gap on complete uniform families. The general operators, the coherent envelope as a direct specialization, and the (n,k,r)=(3,2,1) strict gap are credited as prior or directly implied. No inspected source classifies the iterated fixed point on this family or gives the parameter-wide sharp gap.

## value

PASS

The complete uniform support is a natural benchmark for simultaneous partial-conjunction bounds, not an arbitrary input sample. The formula determines the retained guarantee for every query size and exposes a sharp, unbounded loss relative to logical closure; for fixed r<k the loss is linear in n. The scientific contribution is the extent of that loss, not the existing fact that a loss can occur. It makes no statistical power or calibration claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
