---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Let U=x^d,V=y^d,W=z^d with d odd over algebraically closed char2. Seven Fano linear forms in U,V,W have zero sum and zero sum of cubes. Thus D_1=(x^(d+1),y^(d+1),z^(d+1)) and D_2=(x^(3d+1),...) annihilate F_d, while Euler E sends F_d to F_d since degree 4d+3 is odd. The 3x3 coefficient determinant is xyz(U+V)(V+W)(U+W)(U+V+W)=F_d, whose distinct components for odd d let the Saito determinant/reflexivity argument yield a free logarithmic basis and syzygy degrees (d+1,3d+1). Hilbert–Burch then gives tau=(4d+2)^2-(d+1)(3d+1)=13d^2+12d+3. Independently the local germs yield d^2 transverse triples (tau4), three ordinary (d+2)-fold coordinate vertices (tau(d+1)^2) and 3d three-branch contacts st(t+s^d) (tau2d+2), summing to the same length. Exact independent F2 polynomial derivative/syzygy tests for d=3,5 corroborate the symbolic identities; original verify_fano.py tests universal Fano/Moore identities and d=1,3,5,7,9. No proof is claimed for even d or other characteristics.

## originality

PASS

Best-of-knowledge: the evaluated exact final statement differs from inspected antecedents on hypothesis, characteristic, invariant or quantifier; fundamental mechanisms/prior special cases credited. The source inspections and four implication comparisons below state actual reading and residual priority risks, without interpreting a failed search as proof of novelty.

## value

PASS

A single fixed reduced free curve family undergoes a large arithmetic specialization jump from balanced char-zero exponents (2d+1,2d+1) to (d+1,3d+1), with excess Tjurina d^2 and an explicitly changed singularity basket. This characteristic-dependent failure of constant splitting type is a natural phenomenon in arrangements and logarithmic vector-field theory; the explicit all-d basis and singularity classification are substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
