---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The two explicit character polynomials A=X_1-1 and B=binom(X_1,2)+X_2-X_1 are orthonormal. Counting marked disjoint cycles gives E[(X_1)_i(X_2)_j]=2^{-j} whenever i+2j<=n, zero otherwise. Every quartic mixed term has cycle weight <=8, yielding exact moments (4,2,2,0,3), (4,3,4,4,6), (4,3,5,6,13), (4,3,5,7,15), and (4,3,5,7,16) in regimes n=4,5,6,7,>=8. A positive u^2v^2 coefficient makes phase maximization strict at aligned phases; one-sign-change derivative polynomials give unique positive t_n and strict boundary comparison. Numerator differences prove four strict K_n jumps and exact stabilization n>=8. Independently enumerated conjugacy classes n=4..14 and symbolic derivatives for all five regimes (C1_OK). Finite checks corroborate, not replace, the all-n cycle argument.

## originality

PASS

PASS, qualified: Character polynomials and permutation-cycle factorial moments are published inputs. Primary literature on central Fourier algebras computes amenability, not this sharp two-character L4 synthesis. The relevant public symmetric-group (n-2,2) Fourier block theorem computes full-isotypic ell1/ell∞ projection norms, not the mixed central L2-to-L4 ratio and extremizers. A direct, equivalently named sharp character-packet norm may remain unindexed; result is best-of-knowledge, not historical priority certification.

## value

PASS

PASS: The first two nontrivial symmetric-group irreducibles make a canonical low-degree central Fourier packet. Its exact fourth-moment distortion and complete equality cases are genuine sharp harmonic invariants. Mixed synthesis gives 25.267327... versus pure second-character fourth moment 16, and the cycle-weight mechanism explains precisely four low-rank transitions and an exact rank-eight cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
