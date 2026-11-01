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

The p independent spherical vectors in dimension d=p+1 give the exact uniform correlation law. Rotational symmetry gives off-diagonal second and fourth moments 1/d and 3/[d(d+2)]; conditioning along a distinct four-cycle yields d^-3. Every nonzero trace-four closed walk has precisely four distinct vertices, one opposite repeated vertex, or two opposite repeated vertices, of counts p(p-1)(p-2)(p-3), 2p(p-1)(p-2), and p(p-1). The exact count and symbolic rational identity hold for all p≥2; independent fresh enumeration checked p=2..7 and the first asymptotic correction 42/p. This is an expectation only, not a concentration theorem.

## originality

PASS

The old uniform correlation-matrix spherical Gram and Wishart descriptions are acknowledged. Inspected prior work gives LKJ law and general asymptotic spectral behavior, but not the exact finite-p trace-four rational evaluation. Published Resultary work gives a cubic triangular cumulant, not fourth moment. A characteristic function of the spherical Wishart matrix is available in Paquette–Vander Werf, which in principle contains all moments; differentiating/integrating it to the stated closed rational finite-size formula is additional work, so novelty of this evaluated expression remains qualified.

## value

PASS

A finite-dimensional fourth spectral moment of a canonical uniform random correlation matrix is a natural statistic for covariance-prior calibration; its p-exact finite-size corrections and separation of distinct-cycle/backtracking contributions are useful beyond a generic asymptotic Marchenko–Pastur law. No general eta, fluctuations or new distribution are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
