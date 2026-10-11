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
The standalone script `verify.py` reconstructs the graph \(R_n=L(K_{2,n})\cong K_2\square K_n\) for \(4\le n\le8\), derives the neighborhood facets from adjacency, verifies the \(X\cup Y\) decomposition and the crown-graph intersection, and computes mod-two boundary ranks for the full neighborhood complex.

The replay checks are finite consistency tests. They do not prove the all-\(n\) theorem; the infinite statement rests on the explicit decomposition, the relative simplex collapses, the crown-graph cycle-rank calculation, and the null-map homotopy-pushout argument.

Expected reduced Betti ranks are:
\[
\begin{array}{c|c}
n & \text{nonzero reduced Betti ranks}\\ \hline
4 & \widetilde\beta_2=7\\
5 & \widetilde\beta_2=11,\ \widetilde\beta_3=2\\
6 & \widetilde\beta_2=19,\ \widetilde\beta_4=2\\
7 & \widetilde\beta_2=29,\ \widetilde\beta_5=2\\
8 & \widetilde\beta_2=41,\ \widetilde\beta_6=2.
\end{array}
\]
