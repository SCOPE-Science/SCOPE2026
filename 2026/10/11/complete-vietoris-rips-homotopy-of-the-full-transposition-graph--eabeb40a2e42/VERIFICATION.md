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

## Exact reproducibility

With Python 3, run `python3 verify.py`. No third-party modules, downloads, external datasets, or generated prerequisite files are necessary. The code enumerates all \(24\) permutations of \(S_4\), computes all-pairs shortest-path distances independently of permutation-cycle distances, and checks the enumerated Vietoris–Rips simplices at radii 1 and 2.

The exact radius-two matching has 4,935 disjoint codimension-one pairs and critical-face distribution one in dimension zero plus 33 in dimension three. A topological sort of the complete 56,328-incidence oriented Hasse diagram establishes the absence of directed cycles. The code additionally calculates all mod-two boundary ranks directly.

Expected output: `VERIFY_OK faces=9904 pairs=4935 critical=1x0+33x3 incidences=56328 mod2_beta3=33 graph_edges=72`.

## Verification limits

The computational claim is finite and exhaustive for exactly this complex. Acyclic discrete-Morse theory, not mod-two homology alone, establishes the integral homotopy type. No result for higher-degree symmetric groups or alternative metrics follows. Independent review and independent validation have not been performed.
