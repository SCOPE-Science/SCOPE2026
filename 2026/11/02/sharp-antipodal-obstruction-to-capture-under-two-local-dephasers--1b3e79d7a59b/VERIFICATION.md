---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Run `python3 verify.py` using Python 3 with NumPy and SciPy. The checker exhaustively enumerates all unordered anchored triples of distinct hypercube vertices in dimensions three through seven and obtains spectral ranks via **exact integer** Krawtchouk Gram determinants. It confirms that all interior Hamming-level evaluation ranks are three without antipodal pairs and two with them, and that total bright ranks are respectively \(3d-1\) and \(2d\). It performs 59,988 finite exact-rank assertions.

The checker also constructs the density-matrix Lindblad generator separately from the Walsh argument, computes matrix exponentials for two triples in dimension three and two in dimension four, and compares their late-time capture fractions against the closed forms. The specific examples are the vertex triples \((0,1,2)\) and \((0,1,7)\) in dimension three, and \((0,1,2)\) and \((0,1,15)\) in dimension four. Numerical convergence at the tested late times is not a proof of the infinite-time limit. The proof in RESULT.md supplies that via positivity, monotone trace and stationary-state arguments.

Analytic scope: every integer dimension at least three; pairwise distinct monitored sites; nonzero uniform real hopping; strictly positive absorber and local pure-dephasing rates; arbitrary normalized positive semidefinite initial density matrices. No independent audit has been performed.
