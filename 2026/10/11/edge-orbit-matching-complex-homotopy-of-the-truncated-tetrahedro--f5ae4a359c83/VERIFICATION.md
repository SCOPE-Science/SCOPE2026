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

# Executable verification

Use Python 3 with no third-party dependencies. Execute `python3 verify_truncated_tetra.py` and `python3 verify_alternate.py` from this directory. The first program ends with `VERIFY_OK`, the second with `INDEPENDENT_VERIFY_OK`.

The first implementation explicitly enumerates every valid graph-edge matching and every nonempty covering relation in the five simplicial face posets; the directed-Hasse acyclicity certificate checks a complete topological ordering. It outputs \(1009\), \(819\), \(189\), \(793\), \(215\) nonempty faces and, respectively, one critical vertex with \(22\) critical three-cells, \(14\) critical three-cells, \(8\) critical two-cells, \(20\) critical three-cells, and \(2\) critical two-cells. The full-complex matching-pair digest is `a1c982ad81734158933cbf65063f905df39fe7a6704632e89f33a6ad2d0ed9dc`; further digests print during replay. The Hasse check examines respectively \(3558\), \(2844\), \(512\), \(2722\), and \(608\) directed incidences.

The second implementation constructs the same graph independently as the line graph of once-subdivided \(K_4\), enumerates matchings recursively, and computes simplicial boundary ranks over \(\mathbb F_2\). The reduced Betti ranks are \(22\), \(14\), \(8\), \(20\), \(2\), with dimensions \(3\), \(3\), \(2\), \(3\), \(2\) respectively. This field computation alone cannot exclude integral torsion; the stronger homotopy statement uses the first program's exact discrete-Morse certificate and the formal cofibration proof.

The graph automorphism/orbit argument and the topology of attaching maps are given in `RESULT.md`. No infinite claim or independent external audit is certified by these finite checks.
