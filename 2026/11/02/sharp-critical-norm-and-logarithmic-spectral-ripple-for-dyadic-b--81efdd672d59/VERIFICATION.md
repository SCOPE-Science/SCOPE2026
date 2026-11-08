---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The Bergman–Laplace isometry Ug(z)=(2pi)^(-1/2)int_0^infinity sqrt(2t)g(t)e^(itz)dt converts horizontal-line mass into the positive multiplier m_beta(t)=2t sum_{j>=0}2^(-beta j)e^(-2t2^(-j)). Setting u=2t and adding negative dyadic indices gives m_beta(u/2)=u^(1-beta){P_beta(log_2 u)-R_beta(u)} with P_beta=sum_{k in Z}2^(beta(k+theta))e^(-2^(k+theta)), R_beta=sum_{k>=1}(2^ku)^beta e^(-2^ku). Mellin substitution yields Fourier coefficients Gamma(beta-2pi i ell/log2)/log2, with rapidly convergent series. Positivity and boundedness of P_beta, and exponential decay of R_beta at infinity, yield boundedness iff beta>=1. At beta=1, the omitted R_1 is positive for all finite u while the completed periodic supremum K is approached along u=2^(n+theta*), so the optimal one-sided and two-sided constants coincide and no nonzero extremizer exists. The exact Gamma modulus bound makes the second and higher harmonic derivative tails <9e-6 of the first, giving exactly one maximum and one minimum per period. Multiplier real analyticity and nonconstancy on nonatomic L2 explain noncompactness, absence of eigenvalues and spectrum [0,norm] for bounded cases. An independent mpmath Mellin and Fourier evaluation agreed to better than 1e-24 and recovered theta*=.8611035250777802693 and K=1.4427093011329494542; numerical agreement supports, but does not replace, the proof.

## originality

PASS

Known Toeplitz diagonalization covers the general spectral viewpoint and each line term, but its inspected statements do not identify the infinite one-sided dyadic critical maximizing phase, its exact K, or the equality of one/two-sided norms. Broader vertical-symbol functional calculus makes the scalar representation available and Carleson theory can yield boundedness. Neither inspected theorem implies the precise beta=1 norm and unique log-phase without a separate Fourier tail and extremal argument. Nonmatching indexed findings do not establish originality. The specific Gamma-Fourier constant is not an interpolation from a known finite table. The conjunction of known pieces does not automatically state the sharp K or its unique maximizer. The threshold part alone may be accessible from classical Carleson theorems, so originality is assigned to the complete quantitatively sharp package, not the underlying functional calculus. Best-of-knowledge PASS with specifically identified historical-priority risks; an unsuccessful search is not proof of novelty.

## value

PASS

The exact sharp critical embedding constant and logarithmic maximizing phase are independently useful for sampling/trace bounds on a canonical scale-invariant geometric family of Bergman lines. The nonattainment and one-sided/two-sided same-norm phenomenon identify the essential spectral edge; neither follows from a routine boundedness statement alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
