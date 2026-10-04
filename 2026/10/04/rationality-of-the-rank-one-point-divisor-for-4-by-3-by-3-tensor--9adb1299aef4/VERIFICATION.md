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

The tensor space has \(36\) coordinates. For fixed \((u,K)\), the condition \(\varphi(u,K,W)=0\) contributes six independent equations, hence a projective fiber of dimension \(29\) and total incidence dimension \(34\).

For two distinct points, the two six-equation systems occupy independent \(U\)-slices after a basis change, yielding twelve independent equations. The resulting projective tensor fiber has dimension \(23\), so the ordered double-incidence locus has dimension \(10+23=33\). A rank-zero contraction imposes nine equations; even retaining a choice of \(K\), that ambiguity locus has dimension at most \(3+26+2=31\).

The included `verify_incidence.py` reproduces these coordinate counts from the actual tensor index set and prints `VERIFY_OK`. These checks support the linear-algebra counts; the birational conclusion is the exact dimension argument in `RESULT.md` together with the cited generic-finiteness theorem.

The result does not assert a global isomorphism, smoothness, quotient rationality, or uniqueness on special tensors.
