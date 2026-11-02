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

# Reproduction and limits

Run `python3 verify.py` from a directory containing the embedded standalone checker. It uses only the Python standard library and reconstructs \(C_m\square K_n\) from its original vertex and edge definitions.

The exhaustive direct-graph enumeration covers \((n,m)=(5,3),(5,4),(6,3),(6,4),(7,3),(7,4)\). The raw candidate counts are respectively \(4096,65536,10648,234256,24389,707281\), with every row assignment containing zero, one or two selected vertices. Larger selected fibers are excluded by a proved clique argument, so these are exhaustive for the corresponding graphs. For all four cases with \(n\ge6\), the exact computed maxima and counts agree with \(2m\) and the theorem's formula.

A separate Kneser closed-walk dynamic program checks the trace formula for all \(6\le n\le10\) and \(3\le m\le12\). Generic base-graph tests reconstruct the direct induced-degree condition on Cartesian products over paths, a cycle, a star, a triangle with a leaf, and a complete graph. The final line is `VERIFY_OK`.

The finite checks are not a substitute for the unlimited-parameter proof. No external machine theorem prover or independent assessor was used; an independent mathematical audit has not been performed.
