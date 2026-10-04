# The \(4\times4\) grid refutes all-\(k\) cut-complex shellability
## Finding
For the \(4\times4\) grid graph \(G(4,4)=P_4\mathbin{\square}P_4\), the \(10\)-cut complex satisfies
\[
\widetilde H_4\!\left(\Delta_{10}(G(4,4));\mathbb F_2\right)\cong \mathbb F_2^4,
\qquad
\widetilde H_5\!\left(\Delta_{10}(G(4,4));\mathbb F_2\right)\cong \mathbb F_2^{2747},
\]
and all other reduced mod-\(2\) homology groups vanish. In particular, \(\Delta_{10}(G(4,4))\) is not shellable. Thus \((m,n,k)=(4,4,10)\) is a counterexample to Conjecture 5.9 of Bayer, Denker, Jelić Milutinović, Sundaram, and Xue, which predicts shellability of \(\Delta_k(G(m,n))\) for every \(3\le k\le mn-3\).

## Assumptions and scope
The rectangular grid \(G(4,4)\) is the Cartesian product \(P_4\mathbin{\square}P_4\), with vertices indexed by the sixteen ordered grid positions and edges between horizontally or vertically adjacent positions. For a graph \(G\) on \(n\) vertices, the \(k\)-cut complex \(\Delta_k(G)\) is the pure simplicial complex whose facets are the \((n-k)\)-subsets whose complements induce disconnected \(k\)-vertex subgraphs. Here \(n=16\) and \(k=10\), so every facet has six vertices and the complex is pure of dimension \(5\).

The claim is finite and exact. It concerns simplicial homology over \(\mathbb F_2\) and the consequent shellability obstruction only. It does not assert integral homology, a homotopy type, or minimality among counterexamples.

## Proof
There are exactly \(\binom{16}{10}=8008\) ten-vertex subsets of \(G(4,4)\). Exhaustive connectivity testing gives \(2286\) connected induced ten-vertex subgraphs and \(5722\) disconnected ones. Taking complements therefore gives exactly \(5722\) distinct six-vertex facets of \(\Delta_{10}(G(4,4))\).

The full downward closure has face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,560,1820,4344,5722).
\]
For the simplicial chain complex over \(\mathbb F_2\), exact row reduction gives boundary ranks
\[
(\operatorname{rank}\partial_1,\operatorname{rank}\partial_2,\operatorname{rank}\partial_3,\operatorname{rank}\partial_4,\operatorname{rank}\partial_5)
=(15,105,455,1365,2975).
\]
Hence
\[
(\beta_0,\beta_1,\beta_2,\beta_3,\beta_4,\beta_5)=(1,0,0,0,4,2747),
\]
which proves the stated reduced homology groups. As a consistency check, both the face vector and Betti numbers give Euler characteristic \(-2742\).

A pure shellable \(d\)-dimensional simplicial complex has the homotopy type of a wedge of \(d\)-spheres and therefore has no reduced homology below degree \(d\). Here the complex is pure of dimension \(5\) but \(\widetilde H_4\neq0\). Therefore it is not shellable. Since \(3\le10\le16-3\), this instance lies inside the parameter range of the published grid-shellability conjecture and disproves it.

## Verification
The standalone verifier `verify_grid_4x4_k10.py` rebuilds the \(4\times4\) grid from its definition and checks all \(8008\) ten-subsets. It constructs the complex in two independent finite ways: first as the downward closure of complements of disconnected ten-subsets, and second by directly testing whether a candidate face has a complement containing a disconnected ten-subset. The resulting face sets are required to agree exactly.

The verifier then constructs every simplicial boundary matrix over \(\mathbb F_2\), computes each rank by two different bit-elimination routes (column-space and independently transposed row-space elimination), checks \(\partial^2=0\) on every basis simplex, and checks Euler characteristic independently from faces and homology. A successful replay terminates with `VERIFY_OK`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Sundaram, and Xue introduced the relevant grid-graph program in *Topology of Cut Complexes II*. Their Conjecture 5.9 states that \(\Delta_k(G(m,n))\) is shellable throughout \(3\le k\le mn-3\). Their grid results establish complete descriptions for small \(k\) and give partial higher-\(k\) information, but do not include \(G(4,4)\) at \(k=10\).

Chandrakar, Hazra, Rout, and Singh subsequently study total cut and cut complexes of rectangular grids, concentrating on \(2\times n\) and \(3\times n\) families and proving the all-\(k\) cut-complex shellability conjecture for the \(2\times n\) family. Their stated scope does not cover the \(4\times4\), \(k=10\) instance. The present computation therefore supplies a concrete obstruction outside the proven families and directly falsifies the universal conjecture.

## Limitations
Only mod-\(2\) homology is computed. The nonzero degree-\(4\) group is already sufficient to obstruct shellability, but no claim is made about torsion, integral homology, simple homotopy type, or a discrete-Morse normal form. No claim of smallest counterexample is made with respect to vertex number, grid dimensions, or \(k\). Literature comparison cannot exclude an unindexed or unpublished independent computation.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158v1, first public 11 July 2024; SIAM Journal on Discrete Mathematics 39 (2025), 1123--1157; DOI 10.1137/24M1676077.
2. H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646v1, first public 14 August 2024; DOI 10.1137/24M1687716.
