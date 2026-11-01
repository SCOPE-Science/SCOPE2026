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

# Verification notes

`verify.py` is a stand-alone Python 3 standard-library program. Run with `python verify.py` from the same directory.

The exact \(\mathbb Q(\sqrt2)\) part constructs the 24 signed-permutation vertices, detects 48 pairwise Euclidean-length-two edges, separates the within-square and coordinate-swap families, and verifies all six sign-chamber tables at integer representatives. It additionally checks 3916 nonboundary integer normal triples using exact arithmetic and confirms the geometric criterion and crossing count. It performs an independent gnomonic-coordinate numerical area integration in the regular case, compared with the analytic solid-angle identity, and 80,000 independent Gaussian-normal Monte Carlo samples per each of four fixed stretch vectors.

The finite numerical tests cannot establish a universal assertion or publication priority; proof of the universal claim is the exhaustive 48-edge sign decomposition followed by exact spherical-cone integration in `RESULT.md`. The program is ordinary computational verification and does not constitute independent mathematical validation.

The relevant literature comparison is based on accessible full text for arXiv:2609.16195, arXiv:2603.25643, and arXiv:2304.14239, plus a standard geometry reference. Earlier unindexed or inaccessible equivalent calculations may exist. No external expert audit has been performed.
