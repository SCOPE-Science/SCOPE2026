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
The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative only.

Critical checks:
- the standard complete-bipartite graphical building set consists of all singletons and all subsets meeting both bipartition classes;
- after omitting singleton point summands, the total coordinate sum is \(M=(2^p-1)(2^q-1)\);
- a tube with \(a\) left and \(b\) right vertices has offset \((2^a-1)(2^b-1)\);
- a \(k\)-vertex subset hyperplane has intrinsic normal norm \(\sqrt{k(N-k)/N}\);
- singleton facets give the sharp all-center upper bound and force the uniform center at equality;
- the density \(F(r,s)=((2^r-1)(2^s-1))/((r+s)(r+s-1))\) is coordinatewise nondecreasing and is strictly smaller for every proper \((a,b)\) inside a genuine \((p,q)\) biclique;
- this density bound makes every non-singleton connected-tube distance strictly larger than the singleton radius.

`verify.py` checks every pair \(2\le p,q\le35\) and every connected proper tube cardinality pair using exact rational squared-distance comparisons. It also checks the facet count and the center formula. It does not assess originality and does not replace the arbitrary-parameter proof.
