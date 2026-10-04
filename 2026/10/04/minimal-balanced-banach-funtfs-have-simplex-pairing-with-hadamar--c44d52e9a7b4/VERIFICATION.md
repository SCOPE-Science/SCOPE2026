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

The analytic proof checks the following chain.

1. Tightness implies the synthesis map is onto, so the vectors span the \(n\)-dimensional space.
2. Vector balance rules out \(N=n\), yielding \(N\ge n+1\).
3. At \(N=n+1\), trace gives \(\lambda=(n+1)/n\).
4. The pairing matrix \(A\) satisfies \(A^2=\lambda A\), has rank \(n\), and has the all-ones vector as both its left and right null vector. This forces \(A/\lambda=I-(n+1)^{-1}\mathbf 1\mathbf 1^{\mathsf T}\).
5. For a normalized real Hadamard matrix of order \(n+1\), deleting the first row gives a sign matrix \(S\) with \(S\mathbf1=0\) and \(SS^{\mathsf T}=(n+1)I\). The vectors \(s_j/n\) and functionals \(s_j^{\mathsf T}\) therefore satisfy the Banach unit-norm, balance, and tightness equations.

The standalone `verify.py` replays the Hadamard identities for Sylvester orders \(4,8,16,32,64,128,256\) using exact arithmetic. Its expected terminal line is `VERIFY_OK sylvester_cases=7 r_range=2..8`.

The script verifies representative finite instances only. It does not replace the universal linear-algebra proof, and it does not test Hadamard existence outside the Sylvester family.
