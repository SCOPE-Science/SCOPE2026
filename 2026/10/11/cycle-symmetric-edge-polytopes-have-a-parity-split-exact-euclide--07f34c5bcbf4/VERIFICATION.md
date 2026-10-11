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
The all-\(n\) proof is contained in `RESULT.md`.

Critical checks:
- every facet is represented by an integer cycle labeling whose edge increments have absolute value at most \(1\), with a spanning connected equality-edge subgraph;
- subtracting the label mean gives the exact intrinsic normal in the zero-sum space and leaves support value \(1\);
- central symmetry implies that recentering any inscribed ball at the origin cannot reduce its radius;
- for even \(n=2k\), facet increments are exactly \(k\) \(+1\) steps and \(k\) \(-1\) steps;
- for odd \(n=2k+1\), every facet has exactly one zero step and \(k\) steps of each sign;
- the pairwise-variance identity and endpoint convexity give sharp range profiles
  \[
  V_{\mathrm e}(h)=\frac{h(3hk+2-2h^2)}6
  \]
  and
  \[
  V_{\mathrm o}(h)=
  \frac{h\left(3hk(k+1)+(2k+1)(1-h^2)\right)}{3(2k+1)};
  \]
- both profiles are strictly increasing through the admissible ranges;
- their endpoint values are exactly the squared normal norms stated in the theorem;
- tangent-normal rank is \(n-1\) for odd cycles and \(n/2\) for even cycles;
- the even tangent-normal orthogonal complement inside \(H_0\) is the periodic space \(c_{i+n/2}=c_i\).

`verify.py` exhaustively enumerates every facet-label pattern for \(3\le n\le14\) using exact rational arithmetic. It checks the complete facet counts, maximum normal norms, tangent-facet counts, tangent-normal ranks, and the even periodic-kernel basis. The finite replay is corroborative only and does not establish originality.
