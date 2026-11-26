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

The six stated shifts are the expansion of (xy)⁻¹(1+x)(1+y)(1+xy) in characteristic two. In the Chinese-remainder local factors K[u,v]/(u^k,v^ell), the unit factors are all but the union of the two axes and the inverse-root diagonal, with r+s+g−2 excluded. The stable image has the claimed dimension; all its phase preimages under F^T have the same size by rank-nullity. On the two noncentral axes the nilpotency indices are k and ell; on the noncentral inverse-root diagonal the change v→v(1+u) gives u+v of index max(k,ell), by Frobenius and a nonzero extreme monomial one step earlier. Centrally uv(u+v+uv) is killed at the smaller truncation when k≠ell, and just before that the extreme monomial with exponent 2min(k,ell)−2 in the larger variable survives. When k=ell=2h, its h-th power is zero and the extreme term u^(2h−2)v^(h−1) survives at h−1. The frozen proof skips the local k=ell=2 case, which can occur with odd parts >1: the multiplier is then already zero by u²=v²=0, so its index is one and it does not change the global maximum. This completes the transient law and, since (r−1)(s−1)>g−1 when r,s>1, the extinction criterion. On the dyadic square, factoring u^(h−1)v^(h−1) reduces the rank calculation to multiplication by z^(h−1) in the quotient with u^(h+1)=(u+z)^(h+1)=0. After imposing z^(h−1)=0 only the additional monomial constraint u^h z=0 survives, giving quotient dimension h²−h+1 and image rank 3h. In the rectangle the penultimate multiplier differs from u^(m−1)v^(2m−2) by a unit, giving rank n−2m+2. Independent power-rank stabilization confirms all regimes, e.g. 8×8 ranks 64,42,24,12,0; 4×8 ranks 32,18,8,2,0; 6×6 ranks 36,20,8,8; 9×12 ranks 108,86,76,66,56,56.

## originality

PASS

Pass concerns the sharp transient classification and the exact dyadic penultimate ranks/last-step laws on this operator. A distinct earlier indexed finding already factors exactly the same operator and gives its one-step rank, covering the odd-by-odd recurrent dimension directly and the general recurrent dimension by Frobenius reduction. I do not credit that dimension or the extinction criterion as independently new relative to the inspected coverage. The existing one-step formula and the inspected general convolution results do not furnish the missing penultimate ranks or sharp uniform transient.

## value

PASS

For this natural six-neighbor toroidal rule, the sharp nilpotent depth says exactly when transient information has been lost, not just whether the matrix is singular or how many states remain. The precise fraction of states still surviving at the penultimate update distinguishes dyadic squares from rectangles of equal short side and is a useful exact observable not obtained from the one-step rank. The depth and last-step laws give value even after crediting the already implied stable dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
