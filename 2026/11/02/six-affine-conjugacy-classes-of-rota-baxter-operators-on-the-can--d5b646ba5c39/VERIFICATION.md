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

Independently expanded the affine identity for P(u)=Ru+p: evaluation at (0,0) gives Rp=0; evaluation at (u,0) gives commutation with ad_p; evaluation at (0,v) then gives R²=R. The remaining bilinear terms give the weight-minus-one identity. This uses no restriction on characteristic. The projection identity is equivalent to its image and kernel being subalgebras, and the condition on p says that it is in the kernel and normalizes the image. A plane is a subalgebra exactly when it contains the center. In a rank-one splitting the two complementary directions modulo the center are independent, so the only permitted p is central and can be removed. In rank two p is arbitrary on the kernel line, a central affine translation does not change it, and the split stabilizer scales that line by every nonzero scalar. The quotient GL₂ and central shears move any ordered planar/line splitting of the given ranks to the displayed representative. Constants split by centrality and rank three gives only the identity. Counting q+1 central planes with q² complementary lines per plane gives all six orbit sizes and total 2q⁴+3q³+1. The proof explains both exhaustion and inequivalence.

## originality

PASS

The verified distinct contribution is the fixed-canonical Heisenberg orbit partition and finite-field counts, not the general factorization or conjugacy criterion. The closest general theorem does not identify the Heisenberg subalgebra-pair orbits, which translations survive central conjugacy, or their multiplicities. The closest indexed census solves a different, linear weight-λ identity.

## value

PASS

The Heisenberg algebra is the basic three-dimensional nonabelian nilpotent test case for turning canonical-affgebra factorization into a complete classification. In particular, the two rank-two orbits identify a translation invariant that gets lost when changing brackets is allowed. The all-field result, including characteristic two, and exact orbit sizes make this a usable benchmark for affine, rather than merely linear, classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
