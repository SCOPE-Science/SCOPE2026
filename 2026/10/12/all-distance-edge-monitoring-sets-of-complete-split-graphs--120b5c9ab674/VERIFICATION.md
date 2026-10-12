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
# Verification

The verifier constructs every complete split graph
\[
S_{m,n}=K_m\vee\overline{K_n}
\]
with
\[
1\le m,n\le6.
\]

For every edge \(e\) and every probe vertex \(x\), it computes all distances from \(x\) in the original graph and after deleting \(e\). The probe monitors \(e\) exactly when at least one target distance increases. A set is then tested directly by requiring that the union of its probes' monitored-edge sets contains every edge.

The direct computation is compared with the theorem's structural classification. It also checks every coefficient of
\[
(1+z)^{n+1}-1
\]
for \(m=1\), every coefficient of
\[
z^m(1+z)^n+mz^{m+n-1}
\]
for \(m\ge2\), the distance-edge-monitoring number, and the minimum-basis count.

Recorded output:

```text
VERIFY_OK
parameter_pairs_checked = 36
m,n ranges = 1..6
vertex_subsets_checked = 15876
edge_probe_checks = 5607
minimum_bases_checked = 77
all direct DEM tests matched the two-family classification
all DEM-set polynomial coefficients matched
all dimensions and minimum-basis counts matched
```

The finite checks are corroborative only. The arbitrary-parameter theorem follows from the proof that every probe monitors exactly its incident edges when \(m\ge2\), together with the vertex-cover classification of complete split graphs.
