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

# Reproducibility
Run `python3 verify.py` and compare its single JSON output line to `certificate.json`. Both files are included in this package; the script has no nonstandard dependencies.

The enumerator traverses every labeled simple graph with \(2\), \(3\), or \(4\) vertices, excludes disconnected graphs, considers each root, and for each connected rooted graph traverses every missing edge between nonroot vertices. It verifies strict positivity of the exact rational difference at every eligible insertion. There are respectively \(0\), \(3\), and \(168\) insertions, a total of \(171\), and the computed minimum nonvacuous difference is \(2\). The exhaustive domain is finite and completely specified, making the lower-order classification conclusive.

The witness comparison uses a separate \(16\)-state continuous-time voter reward generator, independently of the grounded-Laplacian path calculation. Both produce expected dissent person-time \(23\) before and \(21\) after adding edge \(24\).

The closed-form rank-one response applies to every connected finite graph. Its mathematical proof is in `RESULT.md`; finite computations confirm rather than substitute for this unrestricted identity. The witness-extension argument adds root-adjacent leaves and is likewise exact. No independent external audit has been conducted.
