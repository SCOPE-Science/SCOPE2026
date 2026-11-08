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

Fourier diagonalization E_k=2J cos((2pi k+Phi)/N) yields the exact indexed two-energy difference 4J|sin((Phi+pi(j+k))/N) sin(pi(j-k)/N)|. For odd N, 2 invertible modulo N means independent sum/difference residues, giving the nearest-zero sine gap, uniquely maximized by quarter flux. For even N, equal parity of sum and difference gives min{sin(alpha)sin(alpha-theta),sin(2alpha)sin(theta)} in the reflected half-cell. Opposite strict monotonicities cross once at tan(theta*)=tan(alpha)/3; reflection yields exactly two maximizers and gap expression. Fourier Hilbert-Schmidt matrix units diagonalize the Cesaro dephasing difference with sinc factors; upper bound 2/(T Delta) is saturated at T=(2m+1)pi/Delta, establishing the claimed limsup and its parity asymptotics. Independent direct gaps across N=3..40 and 4560 flux comparisons matched; finite checks corroborate, not prove, all N.

## originality

PASS

Preexisting chiral ring Hamiltonian Fourier spectrum and average uniform mixing are fully credited. Levine et al. Theorem 5 concerns vertex average mixing for any simple-spectrum abelian circulant, not optimization of the smallest indexed energy difference or exact 2/Delta Hilbert–Schmidt superoperator limsup. Thermometry work optimizes a ground-to-first gap, not the minimum over all pairs. No covering parity-dependent all-size formula found; priority not certified.

## value

PASS

Spectral min-gap directly controls the sharp long-time worst matrix-mode averaging envelope, a natural design criterion for finite quantum transport rings. The optimal flux changes discontinuously by parity in the large-N limit, a motivated structural design distinction rather than a trivial reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
