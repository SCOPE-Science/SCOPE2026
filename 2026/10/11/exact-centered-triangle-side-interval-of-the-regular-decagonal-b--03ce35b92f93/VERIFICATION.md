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
The verification target is
\[
\frac{9-\sqrt5}{4}
\le
N_{10}(x+y)
\le
4-\sqrt5
\]
for every
\[
N_{10}(x)=N_{10}(y)=N_{10}(x-y)=1,
\]
with equality attained at both endpoints.

`verify.py` uses exact rational-pair arithmetic for \(\mathbb Q(\sqrt5)\). It forms the thirty half-space inequalities for \(x\), \(y\), and \(x-y\), then examines all \(10^3\) choices of one tight facet from each block. Inconsistent and empty systems are discarded exactly; all \(60\) nonempty faces are one-dimensional segments.

On each segment the ten signed facet evaluations of \(x+y\) are affine. The maximum of their upper envelope is therefore at a segment endpoint. The minimum of that convex piecewise-affine envelope is attained at an endpoint or where two affine pieces meet. The checker evaluates every such point exactly and obtains the two claimed global extrema.

The two explicit equality pairs in `RESULT.md` are checked separately. No floating-point sampling, timeout inference, or partial enumeration is used as proof. No independent audit or independent validation has been performed.
