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

# Reproduction and scope of checks

Run `python3 verify_z3.py` using only a standard Python 3 interpreter. The verifier implements the field \(\mathbb F_{27}=\mathbb F_3[t]/(t^3-t-1)\), enumerates all projective points and evaluates the homogeneous quartic and four characteristic-three gradient polynomials. It checks exactly six geometric singular points over this field, three in each coordinate plane, their non-rationality over \(\mathbb F_3\), the two Artin–Schreier cubics, and the nonzero local coordinate Jacobians. It also tests the displayed polynomial identities on \(\mathbb F_3\) inputs.

For the infinite-field assertion, the independent mathematical steps required are: (i) \(F_x=yq\), \(F_y=xq\), so outside \(q=0\) singularity would require a multiple root of \(g\); (ii) at \(q=0\), division of \(F-w^3\) by the transverse coordinate \(s\) gives \(H\); (iii) separability of the monic \(P_r=H(0,X,0)\) yields exactly three singular points per root and an invertible completed coordinate change; (iv) \(F=s\xi+w^3\) implies the Jacobian singular algebra \(k[[w]]/(w^3)\) in characteristic \(3\). The finite-field program does not replace steps (i)–(iv), nor does it test the full parameter family.

Observed output:

`VERIFY_OK: exact gradient witness and F27 singular support, local normal-form identities, 6 points / 2 Frobenius triples; each wild A2 Jacobian scheme length 3`

No independent audit has been performed.
