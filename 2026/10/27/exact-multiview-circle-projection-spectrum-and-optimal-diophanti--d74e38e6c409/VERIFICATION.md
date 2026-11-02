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

For f∈L²(S¹) and arcsine-normalized output, the two-preimage cosine change of variables gives q_phi(cos t)=(f(phi+t)+f(phi−t))/2. In orthonormal real Fourier degree n basis the k-view observation is the k×2 matrix B_n whose rows are (cos nphi_j,sin nphi_j), while the constant mode has squared singular value k. Its real Gram spectrum is exactly λ±(n)=(k±|Σ_j exp(2inphi_j)|)/2. The identity k²−|Σ exp(2inphi_j)|²=4Σ_{i<j}sin²(n(phi_i−phi_j)) and elementary sin-distance bounds give (4/k)δ_n²<=λ−(n)<=4π²(k−1)δ_n² for δ_n=max_{j>=2}dist(n(phi_j−phi_1)/π,Z). Parseval proves injectivity iff at least one difference irrational and the complete H^{−τ} observability iff inf_n n^τ δ_n>0. Simultaneous Dirichlet approximation excludes τ<1/(k−1) for injective configurations; badly approximable vectors attain the borderline. Fourier interpolation gives observed-data exponent s(k−1)/(1+s(k−1)), sharp along the unbounded Dirichlet subsequence of least eigenvectors. Condition number including constants is k/min_{1<=n<=N}λ−(n). Fresh numerical Gram and distance checks tested 280 k,n pairs; no finite numerical test certifies Dirichlet or sharp all-frequency results.

## originality

PASS

Best-of-knowledge statement-level primary-literature comparison: the identified antecedents cover qualitative mechanisms, methods or partial counts but no inspected theorem implies the precise assessed evaluated claim; limitations and possible older equivalents remain explicit. The two-line determinant detects qualitative noninjectivity and small divisors for a related operator. The claim instead uses complete arcsine-normalized projected density measurements and evaluates the entire k×2 Fourier Gram spectrum with exact norms and all-τ stability.

## value

PASS

Finite-view tomography of circle-supported densities has a motivated ill-posed inverse problem. The exact singular spectrum and necessary/sufficient Diophantine Sobolev loss give a complete quantitative answer for any number of views, while the sharp Hölder exponent directly describes optimal conditional reconstruction. The result is more than qualitative uniqueness or a textbook orthogonality calculation because the multiview arithmetic threshold and attainable loss are evaluated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
