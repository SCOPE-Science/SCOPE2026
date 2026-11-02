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

Three iterations of a radius-one cellular automaton have effective radius three. A 64-state de Bruijn walk records a six-bit overlap and appends a seventh bit only when the central output of Rule62^3 equals the original central input. Closed walks of length n therefore biject to labelled cyclic points fixed by f^3, even at short cyclic sizes by periodic closure. A separately generated 4-state one-step walk has characteristic polynomial x^3(x-1), hence tr(H^n)=1 for all n>=1 and exactly one temporally fixed state. Prime temporal period three gives C_n=(tr(M^n)-1)/3. Independent construction of M and exact SymPy characteristic polynomial factorization matches x^51(x-1)(x²+1)(x²-x-1)Q(x); the separate rational Schur-Cohn reduction in the source establishes |lambda_j|<3/2 and justifies the uniform exponential remainder. Fresh exhaustive ring tests for n=1..12 yield C_n=(0,0,1,0,5,7,7,24,22,35,77,87). Enumeration is corroboration, whereas transfer path correspondence and exact polynomial certificate establish all n.

## originality

PASS

A period-three dynamical signature is known for Rule62, and generic finite-state Koopman spectra can encode finite orbit lengths. But Stricker (2023) computes and classifies finite ring spectra only in finite sampled ranges; Taga et al. (2021) calculate ECA Koopman spectra at a fixed 13-cell size. Zhu–Richard (October 2026) concerns Koopman classification on finite rings, but its full preprint was not obtainable here. Chen et al. (2012) is directly on Rule62 chaos and gliders but full text was unavailable. No accessible exact all-length count or its golden-ratio rate was found; priority remains qualified by these plausible works.

## value

PASS

An all-ring exact cycle census for a nonlinear elementary automaton yields an explicit rational dynamical zeta contribution, distinct spatial growth rate and finite-size spectral correction. It resolves a natural quantitative gap between finite-state period detection and asymptotic cycle abundance, without conflating spatial n with temporal period three.

The dated certificate retains the supplied scientific assessment, sources and limitations.
