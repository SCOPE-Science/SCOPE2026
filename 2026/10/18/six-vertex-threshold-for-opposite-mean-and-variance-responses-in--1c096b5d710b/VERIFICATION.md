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

# Exact verification record

The supplied `moran_absorption.py` implements the neutral birth-death process on finite connected simple undirected graphs using only standard Python 3. Every step, including a reproduction into an identically typed neighbor, consumes one unit. For transient configuration \(S\), the program builds \(A=I-Q\) from rational transition weights \(1/(n\deg_G(u))\). It solves \(Aa=\mathbf 1\) and \(Ab=2a-\mathbf1\) using fraction-preserving Gaussian elimination. It then averages the single-mutant first and second moments over **the same uniform initial-vertex mixture** and computes variance as \(\mathbb E[T^2]-\mathbb E[T]^2\).

Command: `python moran_absorption.py`. Observed full-comparison counts:

| Vertex count | Labeled connected graph/nonedge comparisons | Opposite-sign products |
| --- | ---: | ---: |
| 2 | 0 | 0 |
| 3 | 3 | 0 |
| 4 | 84 | 0 |
| 5 | 3140 | 0 |

For edge insertion \(45\) into the graph with edges \(01,12,14,15,23,24,25\), the checker gives exactly
\[
\Delta\mu=-\frac{1081916058162303045866787}{963350233128823627873660},\quad
\Delta v=\frac{2649703944786197307161267260643446006651173670039}{37121746866774353314903473528963649187716871824}.
\]
For insertion \(04\) into the path with edges \(01,05,23,34,45\), it gives exactly
\[
\Delta\mu=\frac{105624967578948244284048503408}{1743903055352674650362722242735},\quad
\Delta v=-\frac{202967717778556498291917406194774045071459109551713420605765406}{3041197866468393825501595763452504490989129760874708260280225}.
\]
An independent symbolic computation using a separate matrix construction and SymPy inversion reproduced the four fractions on the two witnesses. The exhaustive comparison is **finite** and applies only through five vertices; the two six-vertex cases are examples, not a complete census. The program does not perform independent scientific auditing or verify external literature originality.
