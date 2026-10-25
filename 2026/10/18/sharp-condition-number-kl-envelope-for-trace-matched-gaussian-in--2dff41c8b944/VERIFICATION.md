---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS. The directed Gaussian KL from hI to B^(−1) reduces exactly to (k/2)(ah−1−ln h−ell), where a is arithmetic precision mean, h harmonic inverse mean, ell mean log precision. Scale eigenvalues into [1,K]; differentiating in one eigenvalue gives positive second derivative (1/k)[(1−2/k)/x²+1/(k h² x⁴)+2(a−h^(−1))/x³] for k≥2, so each maximizing eigenvalue is 1 or K. Interior constant spectra have zero divergence and are excluded for fixed K>1. For multiplicity t=m/k this yields precisely Phi_K(t), with unique interior continuous maximum by endpoint derivative signs and strict convexity of Phi′. The grid extremum, k→∞ envelope and K→1 and K→∞ limits follow. The explicit positive definite 2×2 Lanczos block with nonzero residual 1/2 and direct-sum B yields Schur complement diag(1,B), so its matched bulk achieves the same KL bound without artificial zero coupling. Independent floating-point arithmetic confirmed K=4,k=10,m=4 value D/k≈0.171078599745388 and sampled 300 random precision spectra for K=5, k=3,5,10 stayed below sharp limit. These tests supplement exact calculus.

## originality

PASS

Best-of-knowledge PASS after reading the motivating Fifen–Karambal–Hennig 2026 primary article, Section 4.3 Theorem 13 and its proof: it bounds KL by quadratic (K−1)^2/2 per coordinate, whereas the assessed theorem optimizes exactly over all finite spectra and classifies every extremizer, with O(K) large-K sharp growth. Related Gaussian KL comparison and classical harmonic/arithmetic mean literature do not directly state this fixed-condition-number joint mean/log objective. A prior unindexed spectral-mean extremal inequality remains a genuine risk.

## value

PASS

PASS. The sharp KL loss of trace-matched isotropization is a natural information-geometric invariant in numerical covariance approximation. Replacing a loose quadratic-in-condition-number upper bound by a dimension-sensitive exactly attainable envelope, complete optimizer multiplicities and a genuine nonzero-residual Lanczos witness is useful to worst-case uncertainty analyses; it adds more than a routine numerical benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
