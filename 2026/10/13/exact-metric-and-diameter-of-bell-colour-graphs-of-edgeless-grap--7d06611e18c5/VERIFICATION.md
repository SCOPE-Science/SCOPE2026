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

The theorem is proved analytically. The bundled `verify.py` is a finite independent stress test of the definitions.

For every \(1\le n\le6\), the program generates every set partition in restricted-growth form. For every \(1\le k\le n\), it retains exactly those partitions having at most \(k\) blocks, constructs adjacency by literal one-element moves, and performs breadth-first search from every retained partition. Separately, it computes the maximum block-intersection matching weight by dynamic programming and checks
\[
d(P,Q)=n-\mu(P,Q)
\]
for every ordered pair. It also checks
\[
\operatorname{diam}\mathcal B_k(\overline{K_n})
=n-\left\lceilrac{n}{k}
ight
ceil.
\]

Replay command:

`python3 verify.py`

Expected output:

`ALL CHECKS PASSED; n_max=6; bell_vertices_full=278; parameter_graphs=21; ordered_pair_checks=140668; diameter_checks=21`

These finite checks are supplementary evidence and do not prove the universal statement.
