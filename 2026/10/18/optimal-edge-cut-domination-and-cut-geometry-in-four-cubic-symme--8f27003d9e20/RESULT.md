# Optimal edge-cut domination and cut geometry in four cubic symmetric graphs

## Finding
For the four cubic bipartite symmetric graphs \(H\) (Heawood), \(M\) (Möbius–Kantor), \(P\) (Pappus), and \(D\) (Desargues), the exact edge-cut domination numbers, numbers of minimum sets, and edge-domination numbers are:

| Graph | Vertices | Edges | \(\gamma_e\) | \(\gamma_{ct}\) | Minimum edge-cut dominating sets |
|---|---:|---:|---:|---:|---:|
| Heawood | 14 | 21 | 5 | 6 | 98 |
| Möbius–Kantor | 16 | 24 | 6 | 6 | 8 |
| Pappus | 18 | 27 | 6 | 7 | 27 |
| Desargues | 20 | 30 | 6 | 6 | 5 |

Every minimum edge-cut dominating set leaves **exactly two** connected components. The full component-size and graph-automorphism-orbit classification is:

| Graph | Component sizes after deletion | Number of minimum sets in this orbit | Number of selected edges crossing the two components |
|---|---|---:|---:|
| Heawood | \((1,13)\) | 56 | 3 |
| Heawood | \((4,10)\) | 14 | 6 |
| Heawood | \((6,8)\) | 28 | 6 |
| Möbius–Kantor | \((8,8)\) | 8 | 6 |
| Pappus | \((9,9)\) | 27 | 7 |
| Desargues | \((10,10)\) | 5 | 6 |

In particular, all minima for each of Möbius–Kantor, Pappus and Desargues are exact **balanced edge cuts** (all selected edges join the two resulting components). The Heawood graph behaves differently: 56 minima isolate one vertex with its three incident edges plus three internal edges; its other 42 minima are exact cuts, dividing the graph into a four-vertex claw and a ten-vertex component (14 cases) or a six-cycle and an eight-vertex component (28 cases). Within each displayed row all minima form a single orbit under graph automorphisms, and the three Heawood rows are distinct orbits because the component-size profiles differ.

Thus the cost \(\gamma_{ct}-\gamma_e\) of imposing disconnection on an edge-dominating set is exactly \((1,0,1,0)\) in the displayed order. This distinguishes two different types of optimal edge-dominating connectivity barriers on these natural cubic incidence graphs.

## Assumptions and scope
Graphs are finite, simple, undirected, and have the following **explicit labels**. The complete canonical edge lists in `certificate.json` remove any dependence on drawing conventions.

* Heawood: vertices \(0,\ldots,13\), with points \(0,\ldots,6\) and lines \(7,\ldots,13\). Join point \((j+d)\bmod7\) to line \(7+j\), for \(j\in\{0,\ldots,6\}\), \(d\in\{0,1,3\}\).
* Möbius–Kantor: \(\operatorname{GP}(8,3)\), vertices \(u_i=i\), \(v_i=8+i\), for \(i\in\mathbb Z/8\mathbb Z\); edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+3}\).
* Pappus: points \(p_{x,y}=3x+y\) and lines \(\ell_{a,b}=9+3a+b\), for \(x,y,a,b\in\mathbb F_3\); incidence edges satisfy \(y=ax+b\) in \(\mathbb F_3\).
* Desargues: \(\operatorname{GP}(10,3)\), vertices \(u_i=i\), \(v_i=10+i\), for \(i\in\mathbb Z/10\mathbb Z\); edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+3}\).

An **edge-dominating set** is \(F\subseteq E(G)\) such that every edge of \(G\) belongs to \(F\) or shares an endpoint with an edge of \(F\). An **edge-cut dominating set** is an edge-dominating set for which the spanning graph \((V(G),E(G)\setminus F)\) is disconnected; isolated vertices count as connected components. The minima over the two classes are denoted \(\gamma_e(G)\) and \(\gamma_{ct}(G)\). An automorphism acts on an edge set by sending each edge's endpoints under the corresponding vertex permutation.

## Proof
**1. Exact finite reduction.** Let \(U(F)\) denote the union of endpoints of the edges in \(F\). Then \(F\) dominates every edge **if and only if** \(U(F)\) is a vertex cover: any edge not incident to \(U(F)\) is not adjacent to a selected edge, and conversely every edge incident to \(U(F)\) shares an endpoint with a selected edge. Deletion connectivity is tested on all labeled vertices, including isolates. Both properties are monotone upward under inclusion of selected edges. Thus if no qualifying set of size \(k-1\) exists but at least one of size \(k\) does, \(\gamma_{ct}=k\) follows for every smaller size as well: any smaller qualifying set could be extended to size \(k-1\).

**2. Direct exhaustive search.** `edgecut.cpp` constructs each of the four labeled graphs independently from its defining edges, enumerates every \(k\)-element edge subset for successively increasing \(k\), tests endpoint-cover domination, and builds the connected components after deleting the selected edges by disjoint-set union. The complete level-by-level counts and all minimum bitmasks are in `bruteforce.out`. The first nonzero joint counts are at sizes \(6,6,7,6\), with counts \(98,8,27,5\), respectively. No smaller size is omitted. The preceding edge-domination counts are: Heawood at size five \(42\), Möbius–Kantor at size five \(0\), Pappus at size six \(36\), and Desargues at size five \(0\). As every cubic edge dominates at most five edges (itself and up to four incident edges), \(\gamma_e(G)\ge\lceil |E(G)|/5\rceil\). Together with the displayed nonzero and zero counts, this proves the edge-domination numbers in the table. (The direct enumeration checks the intermediate levels too.)

**3. Independent cut-first exhaustive search.** In any disconnected spanning graph, choose a nonempty proper union \(S\) of connected components, including the vertex labeled zero by replacing \(S\) with its complement when necessary. Then the original cut \(\delta_G(S)\subseteq F\). Conversely, every selected set containing such a cut disconnects the graph. `edgecut_partition.cpp` therefore enumerates all such \(S\) and all ways to add the remaining selected edges to \(\delta_G(S)\), keeping only endpoint-cover edge-dominating completions and deduplicating repeated representations of the same edge set. It finds **zero** cut-dominating sets at one below the claimed minimum for each graph, and recovers exactly the same families at the minimum. The two generalized Petersen graph representations use a different edge ordering, which `verify_certificate.py` explicitly normalizes by unordered endpoint pairs before comparing their sets.

**4. Orbit and component certification.** `certificate.json` lists all minimum bitmasks, the residual component sizes and a vertex-permutation witness for **every** configuration in each orbit. `verify_certificate.py` checks every vertex map is a permutation preserving the full graph edge set, maps the displayed representative to the claimed target edge set, and exhausts the direct-search minimum family without duplication. Graph automorphisms preserve component-size profiles, so the three Heawood rows cannot belong to the same orbit. Each other row is transitive by the explicit witnesses. Counting each profile and its crossing edges gives the second table. In the Heawood four-vertex component the induced degree sequence is \((1,1,1,3)\), hence a claw; in its six-vertex component the degree sequence is \((2,2,2,2,2,2)\), hence a six-cycle because it is connected. In the 56 isolated-vertex cases the selected star uses three edges and the other three selected edges lie internally in the remaining component. This completes the finite proof.

## Verification
From the directory containing the standalone files, run `g++ -O3 -std=c++17 edgecut.cpp -o edgecut` and, for each of `Heawood`, `MobiusKantor`, `Pappus`, and `Desargues`, run `./edgecut NAME 10`. Concatenating the four standard outputs in this order reproduces `bruteforce.out`. Independently run `g++ -O3 -std=c++17 edgecut_partition.cpp -o edgecut_partition` and `./edgecut_partition` to reproduce `partition.out`. Finally, `python3 verify_certificate.py` checks these recorded outputs against `certificate.json` and validates all orbit witnesses, producing `verification.out`. No third-party library or remote service is needed to replay the finite proof; a standard C++17 compiler and Python 3 suffice.

The complete certificate and both enumerators are included, so the assertions do not rest on logs alone. The direct algorithm enumerates every subset at the stated sizes; the cut-first algorithm independently enumerates every separating partition and permissible completion. Those are finite exhaustive proofs for the four specified labeled graphs, not sampling arguments.

## Relationship to prior work
Fenstermacher, Hedetniemi and Laskar [1] define the edge-cut domination parameter (also called split-edge domination in earlier literature), establish its relationship to edge domination and edge connectivity, and compute standard graph families. Their full accessible preprint does **not** give the four graph-specific optimum counts, decomposition profiles or automorphism classifications established here. Spiro, Adriaensen and Mattheus [2] investigate **edge domination without the cut requirement** in incidence structures, including general structural techniques; their results do not imply these simultaneous edge-domination and edge-disconnection classifications. General matching-cut problems and vertex-based cut complexes are distinct: they do not impose the present endpoint-cover condition on a selected set of edges, so they do not directly yield the table or orbit classification. The 2004 original article introducing the split-edge formulation [3] is acknowledged, but its full text was not available for comparison. A search without a covering result is not a proof of literature uniqueness.

## Limitations
All four graphs and the edge-deletion convention are fixed; there is no claim about arbitrary cubic graphs, all symmetric graphs, or higher-order incidence structures. Classification of these finite instances does not imply a general asymptotic pattern or a new polynomial-time algorithm. The search for prior results was limited by indexing and the unavailability of the full 2004 source. The result has received self-review only; **no independent external scientific audit has been performed**.

## References
[1] Todd Fenstermacher, Stephen Hedetniemi, Renu Laskar, *Edge Cut Domination, Irredundance, and Independence in Graphs*, arXiv:1605.04330v1 (public 2016-05-06), https://arxiv.org/html/1605.04330v1.

[2] Sam Spiro, Sam Adriaensen, Sam Mattheus, *Incidence-free sets and edge domination in incidence graphs*, arXiv:2211.14339v1 (public 2022-11-25), https://arxiv.org/html/2211.14339v1.

[3] P. S. Neeralagi, G. K. Nayak, *The split edge domination and split edge neighbourhood numbers of a graph*, in *Graph Theory and Its Applications*, 2004, pp. 112–115. Full text not inspected.
