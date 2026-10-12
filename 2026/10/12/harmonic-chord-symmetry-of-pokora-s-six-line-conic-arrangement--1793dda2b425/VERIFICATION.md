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

The standalone verifier uses exact integer and rational arithmetic. It performs these checks:

1. It parametrizes the conic by \(\nu([u:v])=[2uv:v^2-u^2:v^2+u^2]\) and confirms that the six printed lines cut out exactly the six two-element subsets of \(\{0,\infty,1,-1\}\).
2. It computes the ordered cross-ratio \(\operatorname{cr}(0,\infty;1,-1)=-1\).
3. It exhausts all \(24\) permutations of the marked set and finds exactly \(8\) that preserve the cross-ratio, which is the complete Möbius stabilizer.
4. It verifies generators \(r(t)=(t-1)/(t+1)\) and \(s(t)=-t\) satisfy the dihedral relations and generate all eight elements.
5. It verifies the corresponding plane transformations \(R[x:y:z]=[-y:x:z]\) and \(S[x:y:z]=[-x:y:z]\) permute all six line factors.
6. It computes all fifteen line-line intersections and finds exactly four points carrying three chord lines and three further simple chord intersections; the former lie on the conic and the latter do not.

The verifier does not attempt literature novelty testing, historical-priority resolution, or any claim about automorphisms outside the embedded projective plane model.
