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

The accompanying `verify.py` works entirely with exact arithmetic in \(\mathbb Q(\sqrt3)\).

It performs the following checks:

1. constructs the twelve side-lines of a regular dodecagon;
2. verifies that their pairwise intersections are sixty-six distinct double points;
3. applies \(\Lambda_{\{2\},4}\) by enumerating every line containing at least four of those points and obtains exactly forty-nine lines;
4. recomputes the complete singularity census \(n_2=204\), \(n_3=96\), \(n_4=6\), \(n_5=24\), \(n_6=6\), \(n_7=12\), \(n_{12}=1\);
5. uses the unique twelvefold point together with a projective frame of three sevenfold points to exhaust all \(12\cdot11\cdot10=1320\) possible ordered image triples;
6. finds exactly twenty-four projective transformations preserving all forty-nine lines;
7. verifies that the displayed rotation and reflection preserve the arrangement and satisfy the dihedral relations;
8. checks the element-order distribution \(1^1,2^{13},3^2,4^2,6^2,12^4\);
9. computes line-orbit sizes \(1,6,6,12,12,12\) and identifies the singleton as \(z=0\).

The finite enumeration is exhaustive because every projective stabilizer must fix the unique twelvefold point, permute the twelve sevenfold points, and is uniquely determined by the image of one projective frame.

No independent audit has been performed.
