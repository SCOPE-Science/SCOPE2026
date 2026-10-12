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

# Reproduction and scope

Run `python3 verify.py` with Python 3.8 or newer and no third-party modules. The expected success line is `VERIFY_OK 112 exact rank-one identities; continuum and boundary checks`.

The exact-rational core constructs \(L+\mathbf1\mathbf1^{\mathsf T}/n\), calculates its inverse by rational elimination, and verifies the Sherman–Morrison Kirchhoff-index update on path sizes \(3\) through \(8\), all possible nonadjacent chords, and two positive rational shortcut weights. It includes exact checks on the original conductances and pair-current overlap sums. It also compares floating-point evaluations of the derived \(F\) and \(\Phi\) constants with finite-size sums, including the macroscopic complete shortcut coefficient.

The finite checks do not constitute an exhaustive proof of the parameter-uniform or asymptotic statements. The mathematical proof uses strict convexity and KKT, exact combinatorial voltage-counting, and Riemann/dominated convergence. No independent audit or independent validation is claimed.
