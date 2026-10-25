# Three-connected nonplanar graphs are mature

## Finding

Let \(\Gamma\) be a finite simple 3-vertex-connected nonplanar graph. Then \(\Gamma\) is mature: for the ordered configuration space
\[
F(\Gamma,2)=\{(x,y)\in |\Gamma|\times|\Gamma|:x\ne y\},
\]
the inclusion \(\alpha:F(\Gamma,2)\hookrightarrow|\Gamma|\times|\Gamma|\) induces an isomorphism
\[
\alpha_*:H_1(F(\Gamma,2);\mathbb Z)\longrightarrow H_1(|\Gamma|\times|\Gamma|;\mathbb Z).
\]

This establishes the 3-connected nonplanar case of the maturity classification proposed by Farber and Hanbury.

## Assumptions and scope

Graphs are finite and simple. “3-connected” means that the graph has at least four vertices and remains connected after deletion of any set of at most two vertices. The configuration space is ordered and collision-free, and all homology groups use integral coefficients. Maturity is the isomorphism property above. No claim is made here for arbitrary graphs with cut vertices or 2-vertex separators.

## Proof

The Kuratowski theorem gives a subdivision in \(\Gamma\) of \(K_5\) or \(K_{3,3}\). Farber–Barnett establish that \(K_5\) and \(K_{3,3}\) are mature, and Farber–Hanbury prove that maturity is invariant under subdivision.

The prescribed-subdivision form of the Barnette–Grünbaum construction theorem says that, because \(\Gamma\) is 3-connected and contains a subdivision of the 3-connected graph \(K_5\) or \(K_{3,3}\), \(\Gamma\) can be built from the chosen base graph by a finite sequence of basic Barnette–Grünbaum operations, with the embedded subdivision specifying the sequence. The sequence therefore starts at a mature base graph and ends at \(\Gamma\). Each operation preserves 3-connectivity.

It remains to show that every operation preserves maturity. Farber–Hanbury’s edge-addition theorem says that adding an edge between existing vertices \(u,v\) to a mature graph preserves maturity whenever deleting \(u,v\) from the graph before the addition leaves it connected.

* **Edge addition.** In a 3-connected graph, deleting the two endpoints leaves a connected graph, so the criterion applies.
* **Subdivide one edge \(ab\) by \(x\), then add \(xy\), with \(y\notin\{a,b\}\).** Subdivision preserves maturity. After deleting \(x,y\) from the subdivided graph, the remainder is the original graph with \(y\) and edge \(ab\) removed. Deleting one vertex from a 3-connected graph leaves a 2-connected graph; deleting an edge from a 2-connected graph does not disconnect it. The edge-addition criterion therefore applies.
* **Subdivide two distinct nonparallel edges \(ab,cd\) by \(x,y\), then add \(xy\).** After deleting \(x,y\) from the subdivided graph, the remainder is the original graph with edges \(ab,cd\) removed. A 3-connected graph is 3-edge-connected, so deleting two edges leaves it connected. The edge-addition criterion again applies.

Every step in the construction sequence therefore preserves maturity. Induction over the sequence proves that \(\Gamma\) is mature. \(\square\)

## Verification

The proof depends on three independently stated ingredients: maturity of \(K_5\) and \(K_{3,3}\), the edge-addition criterion for maturity, and the prescribed-subdivision Barnette–Grünbaum construction theorem. The three operation cases above verify the connectivity hypothesis required by the edge-addition criterion; no computational enumeration is used.

## Relationship to prior work

Farber–Hanbury explicitly proposed a classification conjecture for mature graphs and supplied the edge-addition criterion, subdivision invariance, and the base cases \(K_5,K_{3,3}\). Schmidt’s construction theorem supplies the missing construction step from a prescribed 3-connected subgraph. The result here is the explicit compatibility argument showing that all three Barnette–Grünbaum operations preserve maturity, closing the 3-connected nonplanar case of that conjecture. The cited sources do not state this combined conclusion.

## Limitations

This argument proves the 3-connected nonplanar case only. It does not establish the full classification for graphs with cut vertices or 2-vertex separators. The conclusion uses the standard Kuratowski theorem and the published prescribed-subdivision construction theorem; it does not claim a new construction theorem for 3-connected graphs.

## References

1. K. Barnett and M. Farber, “Topology of configuration space of two particles on a graph, I,” arXiv:0903.2180 (first posted 12 March 2009), especially the classification data for \(K_5\) and \(K_{3,3}\). https://arxiv.org/abs/0903.2180
2. M. Farber and E. Hanbury, “Topology of configuration space of two particles on a graph, II,” arXiv:1005.2300 (first posted 13 May 2010), Definition 1, Theorem 1, subdivision invariance, and Section 8. https://arxiv.org/abs/1005.2300
3. J. M. Schmidt, “Construction Sequences and Certifying 3-Connectedness,” arXiv:0912.2561 (first posted 14 December 2009), Theorem 2.11 on construction from a prescribed subdivision by basic Barnette–Grünbaum operations. https://arxiv.org/abs/0912.2561
