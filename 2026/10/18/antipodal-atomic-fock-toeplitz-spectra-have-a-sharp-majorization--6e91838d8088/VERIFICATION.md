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

The Gaussian holomorphic monomials are orthogonal to the nonconstant antiholomorphic monomials, so the two kernels are exp(z·conj(w)/α) and its sum with its conjugate minus 1. With evaluation weighted by e^(−t/2)√m_±, T=E*E shares its nonzero spectrum with EE*. The normalized two-by-two matrices have identical diagonal (m_+,m_−); their off-diagonals divided by √(m_+m_−) are respectively u² and q/D, q=u(2u−1), D=2−u. Both have rank two: 1−u⁴>0 and (D−q)(D+q)=4(1−u²)(1−u+u²)>0. At fixed diagonal the upper eigenvalue [m_++m_−+√((m_+−m_−)²+4m_+m_−c²)]/2 is strictly increasing in |c|, independently of the two positive masses. When u≥1/2, q≥0 and u²>q/D is equivalent to 1>u². When u<1/2, |q|/D>u² exactly when 1−4u+u²>0. This changes sign only at u=2−√3 in that interval. Since u falls as t rises, the claimed majorizations follow. At equality q/D=−u², sign conjugation gives equality of the whole spectrum. This also covers repeated positive eigenvalues when the pluriharmonic off-diagonal vanishes and the masses are equal. Convex/concave x^p gives the strict p>1 and 0<p<1 directions; p=1 is always equal after normalization; p=∞ follows from the top eigenvalue. At a=0 both masses merge with D=1. This direct symbolic comparison is a full replay of the result; the frozen numerical diagnostic was inspected, not executed, and is not needed for any quantifier.

## originality

PASS

The supported distinct claim is the exact mass-independent crossover of the two equal-trace spectra, not the trace factor or the reproducing kernels. Looi's general trace identity already implies D on any single sphere; both that identity and the one-atom example should be credited. Looi's norm and partial-sum comparisons do not supply the ordering of the two normalized eigenvalue lists as a function of radius. No inspected indexed or published theorem establishes the two-atom threshold; the residual scope and access limitations below prevent a priority certification.

## value

PASS

Two positive masses form the first rank at which trace-normalized spectral order can differ at all; at rank one trace equality fixes the spectrum. The antipodal geometry, a natural symmetric test for the two kernel types, has a strict and sharp reversal, rather than a universal ordering suggested by a one-atom norm ratio. The exact boundary is useful for testing spectral comparisons simultaneously across all positive mass ratios and convex or concave power sums.

The dated certificate retains the supplied scientific assessment, sources and limitations.
