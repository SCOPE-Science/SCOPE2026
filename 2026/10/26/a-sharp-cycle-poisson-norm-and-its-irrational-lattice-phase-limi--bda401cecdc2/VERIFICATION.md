---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For C_n with unit edges and unnormalized L=2I−shift−shift^{-1}, the circulant Green row g_n(k)=(n²−1)/(12n)−k(n−k)/(2n) has zero sum and satisfies Lg=e_0−1/n, so it is exactly L†. Its sign changes at m_n=floor[(n−sqrt((n²+2)/3))/2], and its unrestricted ℓ∞ and ℓ1 operator norms coincide with the row absolute sum. Summing the positive entries yields the exact cubic-in-m polynomial, and substitution r=m+u, t=sqrt((n²+2)/3) gives the exact identity N_n=t(n²−1)/(18n)+(t/n)u(1−u)+u(1−u)(2u−1)/(3n). Uniform expansion yields N_n=(√3/54)n²+u(1−u)/√3+O(1/n). Since u is a fractional part of c n+O(1/n), c=(1−1/√3)/2 irrational, Weyl equidistribution gives the full limit law U(1−U)/√3, with CDF 1−sqrt(1−4√3 s) on 0≤s≤1/(4√3). Independent exact rational Green identities and norms for n=3..160 and empirical phase moments for 24,000 orders agree. Those finite checks cannot establish Weyl's theorem.

## originality

PASS

The cycle pseudoinverse kernel is classical: Van Mieghem–Devriendt–Cetinay, Phys. Rev. E 96 (2017), Appendix C Theorem 9 explicitly computes it and credits earlier Bendito et al.; the Green entries are therefore not novel. Its inspected treatment focuses on matrix entries, effective resistance and network centrality, not sharp unrestricted ℓ∞/ℓ1 norms, moving positive-window endpoints, or arithmetic equidistribution of the order-one correction. Ranjan–Zhang–Boley arXiv:1304.2300 gives general dynamic pseudoinverse algorithms, not this exact norm/CDF. Older full texts not fully verified leave a priority risk.

## value

PASS

The sharp ℓ∞ amplification of a periodic graph Poisson solve is a natural numerical-analysis stability invariant. The exact all-cycle formula and nonconvergent O(1) correction, with its fully identified irrational lattice-phase distribution, capture a meaningful arithmetic stability phenomenon beyond recomputing the known Green matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
