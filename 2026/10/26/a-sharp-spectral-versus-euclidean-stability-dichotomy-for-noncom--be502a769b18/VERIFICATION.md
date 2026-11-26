---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Exact exponential Euler yields S_h=I-W_hK. Its K-energy transform is I-K^{1/2}W_hK^{1/2}, symmetric, so its energy operator norm equals its spectral radius. Since 0<W_h<H^{-1} for finite positive h, K<=2H makes the positive eigenvalues of K^{1/2}W_hK^{1/2} strictly below two even at equality in the Loewner bound; if K is not <=2H its limit has an eigenvalue above two and all sufficiently large h are unstable. Each step decreases the same energy on nonzero states. The alternative similarity through W_h gives the bound sqrt(cond(W_h)), and the eigenvalue ratio of W_h is (b/a)(1-exp(-ha))/(1-exp(-hb)) for extremal eigenvalues a<=b of H. Swapping the extreme eigenvectors in the H-scaled admissible K gives limiting norms eta sqrt(b/a) as h goes to infinity for eta<1, then eta tends to one. For scalar H the norm is at most one and tends to one as h tends to zero. For each fixed h and nonscalar H, a rank-one K along a mixture of two H-axes gives a shear block [xi,0; zeta,1] with zeta nonzero because W_h distinguishes those axes; the determinant of its squared singular-value matrix minus I is -zeta^2. Perturbing into the strict SPD interval preserves expansion. Exact replay gives determinants 19/25 for K and 2H-K and squared amplification 224729/204800 on (1,1).

## originality

PASS

Credit the family-specific exponential-Euler classification, especially failure of uniform Euclidean nonexpansivity at each prescribed positive step for nonscalar H, together with the exact admissible Loewner region. Do not credit the general phenomenon or the sharp similarity amplification constant as independent novelty: the latter is already available in the corresponding preconditioned-Richardson problem and applies in the large-step limit. No inspected source supplies the full finite-step family statement.

## value

PASS

The split has a natural stability-design question: an unconditional spectral or physical-energy guarantee does not imply a step-size restriction that guarantees uniform Euclidean nonexpansivity. The exact classification shows the failure at every fixed step in every anisotropic reference matrix, not merely at one counterexample or in a large-step limit. The sharp scale quantifies the protection available when the physical energy, rather than Euclidean size, controls the application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
