# Unique minimal seven-vertex cancellation of bold graph homology

## Finding

Let \(G\) be a finite **connected simple graph**, and let \(\mathbb H^*(G;\mathbb F_2)\) denote its bold cohomology over \(\mathbb F_2\), computed by the connected-dominating-set cochain complex of Caputi–Celoria–Collari. Then:

**Sharp order and unique extremizer.** For every connected simple graph with at most six vertices, the implication
\[
\chi(\mathbb H^*(G;\mathbb F_2))=0\quad\Longrightarrow\quad \mathbb H^*(G;\mathbb F_2)=0
\]
holds. Among connected seven-vertex graphs, exactly one graph-isomorphism class violates it. The unique graph is the join \(C_5*\overline{K_2}\) (the simplicial graph suspension of a five-cycle), with graph-atlas label `G1212`, graph6 string `Fhf~o`, and 15 edges. Its bold cohomology is
\[
\mathbb H^i(C_5*\overline{K_2};\mathbb F_2)\cong
\begin{cases}\mathbb F_2,&i=2,3,\0,&i\notin\{2,3\}.\end{cases}
\]
Thus the signed Euler characteristic vanishes through cancellation of two nonzero cohomology groups. There are exactly 252 **labeled** seven-vertex graphs with the property, all isomorphic to this graph. The *sharp minimum and uniqueness*, not existence of a suspension witness or its cohomology, are the new assertions.

## Assumptions and scope

All graphs here are finite, loopless, undirected, and simple. Graph connectivity is required. A nonempty vertex subset \(S\subseteq V(G)\) is **connected dominating** when the induced graph \(G[S]\) is connected and every vertex outside \(S\) has a neighbor in \(S\). Put
\[
D^k(G;\mathbb F_2)=\operatorname{span}_{\mathbb F_2}\{S\subseteq V(G): |S|=k,\ S\text{ connected dominating}\}.
\]
The cochain differential maps \(S\) to the sum of all its single-vertex extensions \(S\cup\{v\}\), over \(v\notin S\). The set of connected dominating subsets is upward closed, so this is a cochain complex; \(\mathbb H^k(G;\mathbb F_2)=H^k(D^*(G;\mathbb F_2))\). Its Euler characteristic is \(D_c(G;-1)=\sum_{S\,\mathrm{connected\ dominating}}(-1)^{|S|}\). No claim is made for disconnected graphs, graphs with more than seven vertices, or other coefficient fields in the census.

## Proof

**1. Exact exhaustive cutoff and uniqueness.** For \(n=1,\ldots,7\), enumerate the \(2^{\binom n2}\) labeled simple graphs by their edge masks, retaining all connected graphs. For each, enumerate every subset, test induced connectivity and domination, and compute its exact integer alternating connected-dominating count. Only when this count is zero, compute exact mod-two homology of the **non-connected-dominating subset complex** \(A(G)\): its faces are exactly those subsets that fail to be connected dominating, including the empty face. This is a simplicial complex because connected domination is upward closed.

For a nonempty vertex set, the full augmented Boolean face complex is acyclic. The subcomplex of connected-dominating cochains embeds in the acyclic full subset cochain complex \(E^*\), whose quotient is the augmented cochain complex of \(A(G)\) with cardinality grading: \(0\to D^*\to E^*\to\widetilde C^{*-1}(A(G))\to0\). The associated long exact sequence yields
\[
H^k(D^*(G;\mathbb F_2))\cong \widetilde H^{k-2}(A(G);\mathbb F_2).
\]
The cardinality grading explains the shift by two: cardinality-\(k\) faces have simplicial dimension \(k-1\), and the acyclic full-complex long exact sequence adds one. Hence the enumerator may detect nonzero bold cohomology from reduced homology of \(A(G)\).

The complete labeled enumeration, including every graph without sampling, returns:

| \(n\) | Connected labeled graphs | With \(D_c(G;-1)=0\) | With zero Euler and nonzero bold cohomology |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 3 | 4 | 3 | 0 |
| 4 | 38 | 34 | 0 |
| 5 | 728 | 660 | 0 |
| 6 | 26,704 | 24,401 | 0 |
| 7 | 1,866,256 | 1,691,767 | 252 |

For **every one** of the 252 positives, the same program directly verifies this structural criterion: exactly two nonadjacent degree-five vertices dominate the other five, which have degree four in the full graph, and the graph they induce is a connected 2-regular graph on five vertices. The latter must be \(C_5\). This proves that every positive is the claimed suspension. Its automorphism group has order \(10\cdot2=20\), so it indeed has \(7!/20=252\) labeled realizations. Both the exact coverage of all graph masks and each binary field rank computation are reproducible from `census_labeled.c`, with output `census_labeled.out`; the program uses no floating-point or randomized steps.

**2. Independent unlabeled and direct-cochain check.** A second implementation iterates all 1,253 graphs in the Read–Wilson/NetworkX seven-vertex-and-smaller atlas, retains all 996 connected ones, and constructs the *connected-dominating cochain matrices themselves*, not the complementary complex. Exact Gaussian elimination over \(\mathbb F_2\) computes all cochain Betti numbers. This returns exactly one zero-Euler positive: atlas `G1212`, with Betti profile \(\{2:1,3:1\}\). The counts of connected unlabeled graphs in orders 1–7 are \(1,1,2,6,21,112,853\), and the counts with zero Euler are \(0,0,1,4,16,91,732\); 731 of those at order seven have trivial bold cohomology. The direct and complement implementations have different graph enumerations and different chain constructions, reducing the risk of a shared transcription or indexing error.

**3. Explicit topological calculation of the unique witness.** Write the cycle vertices as \(0,1,2,3,4\), joined cyclically, and add nonadjacent apex vertices \(5,6\), each adjacent to all cycle vertices. A set meeting both the cycle and the apices is connected dominating; a set entirely within the apices is not. Therefore \(A(G)\) is the *disjoint* union of the one-simplex on \(\{5,6\}\) and the non-connected-dominating complex \(A(C_5)\) on \(\{0,\ldots,4\}\).

The latter has all ten edges on five vertices and exactly five triangular facets `013`, `023`, `024`, `124`, `134`. Each triangle possesses a distinct free edge (`01`, `23`, `04`, `12`, `34`, respectively). Collapsing these five triangle–edge pairs leaves the cycle with edges `02`, `03`, `13`, `14`, `24`. Thus
\[
A(G)\simeq S^1\sqcup\{\mathrm{pt}\},\qquad
\widetilde H^0(A(G);\mathbb Z)\cong\widetilde H^1(A(G);\mathbb Z)\cong\mathbb Z,
\]
with other reduced cohomology zero, and hence the displayed two-group bold cohomology formula follows over \(\mathbb F_2\). The five collapses also establish the corresponding *integral cohomology groups of this witness*, independently of any finite-field rank computations; no integral assertion is required for the full census.

## Verification

Compile and execute the standalone exhaustive labeled verifier:

```sh
cc -O3 -std=c11 -Wall -Wextra -o census_labeled census_labeled.c
./census_labeled
```

Its output must match `census_labeled.out`, ending with `unexpected_witness_patterns=0` and exactly 252 positive labeled seven-vertex cases. The source loops through every edge mask and calculates ranks with exact bitwise arithmetic. At most \(\binom72=21\) edge bits occur and the largest relevant face-vector space has dimension \(\binom73=35\), within the 64-bit elimination rows. For independent graph-isomorphism and direct-cochain verification, install NetworkX and run:

```sh
python census_direct.py
```

Compare with `census_direct.out`. This program also checks known complete graphs, cycles, complete bipartite graphs, paths, and suspended cycles against published families. No reliance on a time-limited search, sampled subset, or external stored matrix is needed.

## Relationship to prior work

Caputi, Celoria, and Collari introduced the connected-dominating cochain model and the Euler characteristic identity; their 2022 work explicitly asked whether nontrivial bold cohomology could cancel to Euler zero. Their later 2023 suspension theorem **already entails the existence of this kind of witness and the two nonzero groups for the suspension of a five-cycle**. Those assertions are not new here. Neither theorem provides a universal absence proof for all smaller connected graphs or an isomorphism classification at the minimal order. The present exhaustive two-way census supplies precisely that missing sharp-order/unique-extremizer statement. This finding is about *bold graph cohomology*, not the different graph-space complexes defined by domination-number thresholds or by graph matchings.

## Limitations

The smallest-order assertion is an exhaustive finite classification, not an all-order theorem. The explicit cohomology of the suspension is covered by existing broader work, and cannot by itself establish novelty. This census uses \(\mathbb F_2\) coefficients; it does not classify possible torsion or integral cohomology in all other seven-vertex graphs. The independent code uses the standard Read–Wilson atlas packaged with NetworkX; the labeled implementation does not require that database. Reproducibility relies on inspection and execution of both included scripts and the explicitly given homological identification; no formally verified proof object is asserted. An earlier unindexed census of the exact sharp threshold remains possible.

## References

1. Luigi Caputi, Daniele Celoria, Carlo Collari, *Categorifying connected domination via graph überhomology*, arXiv:2201.00721v1 (first public 2022-01-03), especially Theorems 1.2–1.3 and Question 5.11; https://arxiv.org/abs/2201.00721 .
2. Luigi Caputi, Daniele Celoria, Carlo Collari, *From the Mayer–Vietoris spectral sequence to überhomology*, arXiv:2304.10134 (2023), especially Theorem 5.8 on suspensions; https://doi.org/10.1017/prm.2023.104 .
3. NetworkX documentation, `graph_atlas_g`: Read–Wilson list of all simple graphs on at most seven vertices; https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html .
