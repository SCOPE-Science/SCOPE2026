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
`artifacts/verify.py` uses only the Python standard library.

It generates all \(125\) words of \(\mathbb Z_5^3\), computes Lee distance directly, and independently constructs the seven-point radius-one Lee ball around every word. It checks all unordered pairs of centers and confirms that minimum-distance compatibility is exactly disjointness of these balls.

For the upper bound, the script runs an exact bit-set maximum-clique branch-and-bound. Each search node greedily colors its candidate-induced graph; the number of colors is a rigorous upper bound for any clique extension, and pruning occurs only when that bound cannot improve the incumbent. The complete search returns maximum \(15\) and checks an explicit attaining code.

A distinct target-size recursion enumerates every fifteen-clique containing \(000\), obtaining \(24\). Translations produce exactly \(200\) distinct labeled maxima. Applying the full declared natural action of size \(6000\) to one maximum produces all \(200\), giving one orbit and stabilizer \(30\). The script then independently recomputes every coordinate symbol count and every pairwise Lee distance in all maxima.

The computation is finite and exhaustive for the stated parameter only. It is not evidence for any larger alphabet, length, or distance, and no external solver status is used.
