---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The one-system Gram matrix is positive definite for \(0<s<1\), so the injective product states are linearly independent. Transitivity lets any unambiguous-discrimination SDP solution be averaged to a common success value, whose optimum is the minimum Gram eigenvalue. For \(k<N\), the injective Gram matrix is a principal submatrix of \(B^{\otimes k}\), giving lower bound \((1-s)^k\); the alternating tensor on any \(k+1\) labels has no repeated-coordinate support, zero coordinate sums, and attains this eigenvalue. For \(k=N\), expanding the Gram kernel into positive-semidefinite agreement matrices yields lower bound \((1-s)^{N-1}(1+(N-1)s)\); the permutation sign vector annihilates every term with at least two free labels and attains the bound. Independent exact/numerical spectra at \(s=2/5\) for \(3\le N\le5\) reproduce both branches. The local reciprocal-state measurement succeeds with probability \(1-s\) per site; all sites must succeed when \(k<N\), while at \(k=N\) zero or one local failure still identifies the permutation, matching the global optimum.

## originality

PASS

Originality passes. Murshid et al. define the same without-replacement injective ensembles, solve several small cases, and state exactly the audited unambiguous formula as Conjecture 14; the published abstract describes only strong numerical evidence for the multipartite extension. The 2024 sequence-discrimination theorem covers independent Cartesian-product sequences, a materially different prior that permits repetitions. The audited alternating-tensor and sign-representation witnesses, together with matching positive-semidefinite lower bounds, prove the conjecture for all \(N,k\).

## value

PASS

The result resolves the unambiguous-discrimination half of an explicit published conjecture for a natural without-replacement quantum-sequence ensemble. The proof also explains structurally why LOCC remains globally optimal and why the full-permutation case gains exactly the one-erasure term. This is a clear theorem-level closure of a live problem, not a routine extrapolation from computed cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
