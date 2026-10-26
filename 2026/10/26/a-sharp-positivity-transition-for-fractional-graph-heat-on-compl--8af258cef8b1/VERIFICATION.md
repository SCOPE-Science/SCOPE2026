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
# Verification record

The reproducible `checker.py` reconstructs each complete multipartite graph Laplacian from edges, performs an independent symmetric spectral decomposition with SciPy, evaluates the fractional exponential, and compares all its entries to the three-eigenspace algebraic formula. It also compares absolute row sums to the asserted exact norm, verifies positivity and post-cutoff behavior, and checks the ratio of the cutoff and peak excess against the analytical near-critical coefficients. It completed 11,556 assertions successfully.

To reproduce, run `python checker.py` with NumPy and SciPy installed. The code treats the combinatorial zero eigenvalue as zero when tiny numerical diagonalization errors are present. Numerical assertions are finite regression tests and do not establish the general theorem or novelty; those require the explicit spectral decomposition, convexity argument, and Taylor proof in `RESULT.md`. All time and spectral normalizations are stated there. No independent audit has occurred.
