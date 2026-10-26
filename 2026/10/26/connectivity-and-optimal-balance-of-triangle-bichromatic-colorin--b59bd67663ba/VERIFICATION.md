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

# Verification record

The scientific claims concern arbitrarily large finite simple graphs, so the four mathematical arguments in `RESULT.md` carry the infinite conclusions; exact finite computation is corroborating evidence only. The standalone program `verify.py` uses Python 3 standard library and needs no external datasets. Execute `python verify.py` from the directory containing that program.

The program lists every labelled simple graph with at most six vertices, a total of \(33{,}868\), and identifies \(26{,}342\) that satisfy the vertex-removal definition of \(2\)-degeneracy. For each qualifying graph, it separately constructs all triangles, enumerates all binary vertex assignments, rejects precisely those with a monochromatic triangle, constructs legal one-vertex-flip neighbors, breadth-first-searches the resulting state graph, and checks existence of a coloring with minimum parity discrepancy. It also builds \(B_m\) for all \(1\le m\le8\), checks every coloring-polynomial coefficient, checks state counts and computes all-pairs shortest paths and exact diameters. For \(A_m\) with \(1\le m\le9\), it directly checks degeneracy, six legal states, their isolation, and exact discrepancy.

**Observed successful run:**

`VERIFY_OK labelled_graphs=33868 2_degenerate_graphs=26342 books=8 book_states=1036 rigid_examples=9`

**Scope and limits.** The test never asserts to enumerate infinitely many graphs and never derives an infinite theorem from finite data. It does not establish a diameter bound on general \(2\)-degenerate graphs or historical originality. The proof depends critically on the single-triangle fiber intersection fact and the explicit hub classifications, which must be checked mathematically. Self-review was performed; independent audit has not been performed.
