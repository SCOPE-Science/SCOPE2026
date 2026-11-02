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

Analytical verification decomposes every zero-sum load \((t\mathbf 1+x,-Nt)\) with \(x\perp\mathbf 1\). The powered-distance quadratic form is exactly the sum of a constant-mode scalar and the matrix \((1-c)A-cI\) on \(\mathbf 1^\perp\). The largest nonconstant eigenvalue is \((s-1)c-s\) when \(c\ge1\). The constant-mode scalar is \(F(p,h)=k+(N-1-k)c-2Nh^p\). The theorem establishes the unique first roots and their intersection, including boundary weights, without relying on finite enumeration.

Execute `python check.py` with packages in `requirements.txt` to reconstruct twelve graph adjacency matrices and full \((N+1)\)-point powered-distance matrices. The script diagonalizes restrictions to zero-sum coefficients at five weights per graph, checks both sides of the threshold, and performs exact rational rank calculations at the simultaneous critical mode for base graphs with integral least eigenvalue. Successful output ends with `CHECK_OK: twelve adjacency-matrix families, five cone weights each, independent centered spectral reconstructions and exact-rational crossover ranks`.

Finite numerics do not prove the universal graph theorem; exact rational tests cover only the specified graphs at the indicated critical points. No independent audit or external verification was performed. Historical priority remains a qualified inference from inspected sources, not a theorem.
