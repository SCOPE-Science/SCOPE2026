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

The killed operator H=K-Q is self-adjoint in L²(π), strictly positive by irreducibility and nonzero killing. Equilibrium survival is the Laplace transform of the spectral law of H at the unit vector 1. The tilted log curvature is the eigenvalue variance; equality occurs exactly if H1=k is a multiple of 1. A successful live redraw regenerates the starting law, hence survival is the product and strict Jensen gives the unique equal spacing for nonconstant k (q=1 has only one schedule). Splitting any positive segment strictly improves survival; spectral Jensen gives the strict lower bound exp(-t k̄). The first derivative gives its infinite-budget limit. Self-adjointness gives spectral moments k̄, Eπ[k²] and Eπ[k³]+<k,-Qk>π; the centered log cumulants give the stated coefficient including the factor 1/6 and negative sign. The fourth-order segment Taylor error is O(q^-3) after multiplying by q at fixed t,Q,k. Constant killing makes every inequality an equality and all schedules equivalent. The three-site path has variance 8/3, zero centered third moment, energy 8r/3. Independent replay `cd /workspace && python audit_checks/check_frozen.py 2` computes exact formal log coefficients in three rational networks and high-precision survival from their matrix exponentials, including nonuniform π with nonzero skewness and a constant killing case. The proof, not the finite checks, supplies the general quantifiers.

## originality

PASS

Best-knowledge pass for the explicit cubic Dirichlet-energy correction and its placement in the strict finite-budget equilibrium-redraw result. Restart factorization, generic equi-hazard stationarity and log-convexity of the spectral mixture are familiar mechanisms, not claims of priority. No examined result supplied the stated network coefficient.

## value

PASS

For a canonical zero-cost stationary redraw protocol, the theorem separates the first penalty (equilibrium killing heterogeneity) from the first graph-dependent correction (transport energy). The three-site example distinguishes networks with identical equilibrium hazard statistics. The strict finite-budget statement and constant-rate degeneracy make the asymptotic quantitatively interpretable rather than a generic renewal expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
