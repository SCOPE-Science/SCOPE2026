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

The final claim is an exact theorem for every nondegenerate centrally symmetric convex hexagon in the Euclidean plane.

The verification reconstructs the following chain from the published planar translative-hull formula:

1. After centering, write the cyclic vertices as \(v_1,v_2,v_3,-v_1,-v_2,-v_3\) and set \(a=\det(v_1,v_2)\), \(b=\det(v_2,v_3)\), \(c=\det(v_1,v_3)\). Convexity gives \(a,b,c>0\), and shoelace gives \(\operatorname{area}(K)=a+b+c\).
2. The support-triangle values at \(v_1,v_2,v_3\) are exactly \(\frac12\max\{a,c\}\), \(\frac12\max\{a,b\}\), and \(\frac12\max\{b,c\}\).
3. Therefore \(\max A_K\ge\operatorname{area}(K)/6\), and the published identity gives \(c^{\mathrm{tr}}(K)\ge7/3\).
4. Equality forces \(a=b=c\). In the affine coordinates \(v_1=(1,0)\), \(v_3=(0,1)\), determinant ratios force \(v_2=(1,1)\), so the hexagon is affine-regular.
5. For the canonical model \(H=\operatorname{conv}\{(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)\}\), every boundary edge has support-triangle area \(1/2\) by an explicit determinant calculation and a determinant-one cyclic linear symmetry. Since \(\operatorname{area}(H)=3\), equality follows.

No numerical search, sampling argument, asymptotic estimate, or unproved computational certificate enters the proof. The claim does not cover nonsymmetric hexagons and does not assert the full value of \(t_6\).
