---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For B=-(p d/dx) d/dx+1>=I, the form -B plus positive point traces is a selfadjoint finite-rank form perturbation. The resolvent eigenproblem for t>=0 is equivalent, with multiplicity, to K(t)z=z. Positivity and strict quadratic-form decrease of (B+t)^-1 on finite nonzero combinations of point masses show exactly eigenvalues K(0)>1 cross 1 once, with K(0)=1 giving zero modes; essential spectrum <=-1. For an isolated crossing b' = V_s'(s)+G(s,s), giving d=G/(G-b')<1 on P phases and >1 on Q phases. Source Theorem 5.3 gives exponentially close crossing positions and isolated slopes; the Floquet Green off-diagonals decay exponentially, so the full K is uniformly close to its finite diagonal gap around 1. Weyl perturbation therefore gives exactly one positive direction per Q and no neutral mode for large separation. The proof correctly limits to selfadjoint transmission spectrum and does not claim nonlinear stability. Independent analytic reconstruction of the Birman–Schwinger index argument was performed; numerical checker was inspected, but its output alone was not treated as proof.

## originality

PASS

The primary Mori–Ogawa–Sintavanuruk full-text paper proves the exact family of 2^m distant fronts and stability of monotone fronts; the nonmonotone cases are explicitly left open in discussion. Bastiaansen–Doelman–Kaper study qualitatively analogous spectral selection for smooth small-amplitude topography but cannot imply the fixed-contrast discontinuous McKean transmission law. Birman–Schwinger machinery is classical, but the exact Q-letter index for these pinned profiles is not an automatic consequence of front existence.

## value

PASS

The finite Green-matrix index criterion is an exact check for arbitrary simple crossing configurations. Its large-gap specialization gives the complete binomial Morse-index spectrum of a natural 2^m multistable-front family at order-one periodic heterogeneity; it distinguishes the unique spectrally negative all-P word and isolates where nonlinear stability remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
