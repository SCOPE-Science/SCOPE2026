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

# Verification of the uniform four-cut classification

The independent audit status is unperformed. This file records reproducibility checks, not an independent certification.

Execute `python verify.py` from the folder containing `verify.py`. No nonstandard Python packages or network access are needed. It regenerates each vertex set and edge of the Möbius ladder from first principles. For every \(5\le n\le12\), it exhausts the \(\binom{2n}{4}\) possible four-subsets and compares their induced connectivity against the six symbolic classes, checking \(11n\) connected sets. It then reconstructs all triangle-to-tetrahedron coface incidences after each of \(11n\) free-face collapses. For \(5\le n\le10\), it also checks every five-subset has a disconnected four-subset. At \(n=5,6,7\), signed simplicial boundary ranks of the primal lower skeleton are computed modulo \(2,3,5,101\), yielding top ranks \(29,99,209\).

Expected final line: `All finite stress tests passed; the uniform proof is in RESULT.md.` Computational rank checks over finitely many primes do not imply absence of arbitrary integral torsion and do not establish an infinite theorem by themselves. The actual uniform proof rests on the complete graph-theoretic classification, explicit free triangles, integral Alexander duality, and connectivity/Hurewicz arguments in `RESULT.md`.
