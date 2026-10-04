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
The universal claim is proved symbolically from the bordered-alternating rank dichotomy.

For a specialization \(B\) of rank \(2s\), the checker-independent proof establishes:
- exactly \(q^{2s}\) borders lie in \(\operatorname{im}B\);
- those borders leave the rank at \(2s\);
- all other borders raise the rank to \(2s+2\).

The packaged checker at `artifacts/verify.py` performs an independent finite replay. It:
- enumerates every simple graph on at most four vertices;
- over \(\mathbf F_2\) and \(\mathbf F_3\), enumerates every edge specialization of each graph and every border created by a new universal vertex;
- computes ranks by modular Gaussian elimination and verifies the complete cone rank histogram against the recurrence;
- directly enumerates \(K_{1,a,b}\) for \(1\le a,b\le2\) over \(\mathbf F_2\) and \(\mathbf F_3\);
- verifies the closed rectangular-rank formula and the graphical-group sum-of-squares identity induced by the resulting character multiplicities.

The replay returns `VERIFY_OK`.

Finite enumeration is not used as the proof of the universal theorem. No claim is made for arbitrary graph joins.
