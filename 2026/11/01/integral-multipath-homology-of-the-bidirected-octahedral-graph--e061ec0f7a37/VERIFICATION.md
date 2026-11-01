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

# Exact computational checks

Run `python3 verify_octahedral_multipath.py` using Python 3.10+ with only the standard library. The verifier reconstructs all 24 arcs from the three antipodal pairs; enumerates faces by two separate methods; compares exact face sets; checks the full 1,816-face incidence graph and 835 reversed matching pairs for cycles; makes 835 integral unit chain cancellations; checks the reduced differential squares to zero; finds nine integer unit pivots and a zero residual \(12\times101\) boundary; and independently reduces all full simplicial boundaries over \(\mathbb F_2\). It asserts the final reduced integral ranks and numerical consistency.

Actual recorded results: face-vector \((24,192,616,744,240)\), incidences \(6408\), critical-cell counts \((1,0,12,101,32)\), mod-two boundary ranks \((23,169,444,208)\), and reduced integral Betti numbers \((3,92,32)\). The full textual output is in `verification_stdout.txt`.

**Limits.** An executable finite exhaustive argument, not a proof of any all-order statement. A successful verification output is not independently audited. The integral calculation determines homology only, not the homotopy attaching maps or cup products.
