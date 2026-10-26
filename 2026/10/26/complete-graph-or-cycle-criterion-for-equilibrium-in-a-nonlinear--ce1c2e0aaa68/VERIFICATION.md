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

# Verification of the finite-graph detailed-balance classification

The complete analytic proof is in `RESULT.md`, and the standalone Python 3 verification program is `verify_graph_balance.py`. Run `python verify_graph_balance.py` from this directory; it needs only the standard library.

The program computes forward/reverse products around spin-configuration four-cycles, directly from the nonnegative spin-flip rates, on all labelled simple graphs with one through five vertices. It checks agreement with the proposed connected-component classification on 1,099 graphs. It also verifies 608 pairwise detailed-balance identities for the explicit \(K_4\), \(C_5\) and \(K_6\) weights, plus the exact three-vertex-path affinity and a nonzero \(K_4\) four-spin coupling. The run with \(s=0.63\), \(J=0.47\) produced all PASS results and a maximum allowed floating-point tolerance of \(5\times10^{-11}\).

These finite tests are diagnostics rather than proof of the all-size theorem. The theorem relies on the explicit affinity identity, strict monotonicity of the response increment and a combinatorial characterization of neighborhoods, none of which assumes an enumerated graph-size cutoff. The checks concern continuous-time strong-dephasing population rates, not finite-dephasing quantum channels.
