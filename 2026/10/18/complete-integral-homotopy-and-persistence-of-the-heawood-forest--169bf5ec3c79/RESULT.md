# Complete integral homotopy and persistence of the Heawood forest filtration

## Finding
Let \(H\) be the Heawood graph, realized as the incidence graph of the Fano plane, and let \(\mathcal F_d(H)\) be the simplicial complex of vertex subsets inducing forests of maximum degree at most \(d\). Its complete integer-indexed filtration has the following homotopy types:

\[
\begin{aligned}
\mathcal F_0(H)&\simeq\bigvee^6 S^3,\\
\mathcal F_1(H)&\simeq\bigvee^{13} S^5,\\
\mathcal F_2(H)&\simeq S^6,\\
\mathcal F_3(H)&=\mathcal F_\infty(H)\simeq\bigvee^8 S^8.
\end{aligned}
\]

All reduced integral homology is free abelian, and every map induced by a **strict** inclusion between successive stages is zero on reduced homology. The full reduced integral persistence module therefore decomposes into six intervals in degree \(3\) on \([0,1)\), thirteen in degree \(5\) on \([1,2)\), one in degree \(6\) on \([2,3)\), and eight in degree \(8\) on \([3,\infty)\); all other reduced bars are absent. The first stage's homotopy type was established previously; the new claims are the three subsequent homotopy types and their complete persistence consequences.

## Assumptions and scope
The vertex set of \(H\) is \(\{p_i,\ell_j:i,j\in\mathbb Z/7\mathbb Z\}\). There is an undirected edge \(p_i\ell_j\) precisely when \((i-j)\bmod7\in\{0,1,3\}\), and there are no other edges. This is the fourteen-vertex, twenty-one-edge, cubic point-line incidence graph of the Fano plane. A set \(\sigma\) is a simplex of \(\mathcal F_d(H)\) if and only if the induced undirected graph \(H[\sigma]\) contains no cycle and all degrees in it are at most \(d\). The empty simplex belongs to the abstract simplicial complex but is omitted from the nonempty face-poset Morse matching. All spaces are geometric realizations, all homotopy equivalences are nonequivariant, and homology/persistence are over \(\mathbb Z\) unless a field is stated. Since \(H\) is cubic, the filtration stabilizes at \(d=3\).

## Proof
**1. Exhaustive face characterization.** Label \(p_0,\ldots,p_6,\ell_0,\ldots,\ell_6\) by integers \(0,\ldots,13\), and identify each subset with its fourteen-bit indicator. Test every integer from \(1\) through \(2^{14}-1\). For every selected edge, union its endpoints in a disjoint-set forest; an edge connecting endpoints already in the same component detects an induced cycle. Independently compute the maximum induced degree. Retain precisely the sets passing both predicates. The four resulting numbers of nonempty faces are \(457,2256,8654,12791\) at \(d=0,1,2,3\), respectively. Their face counts by dimension, starting with dimension zero, are

| Stage | Face counts by increasing dimension |
| --- | --- |
| \(\mathcal F_0\) | \(14,70,154,147,56,14,2\) |
| \(\mathcal F_1\) | \(14,91,322,651,728,392,58\) |
| \(\mathcal F_2\) | \(14,91,364,987,1862,2366,1906,882,182\) |
| \(\mathcal F_3\) | \(14,91,364,1001,2002,2975,3208,2254,812,70\) |

These counts are not inferred from samples: the standalone programs examine all \(16{,}384\) vertex masks. Every codimension-one face of every enumerated simplex is also checked to occur in the same stage.

**2. Complete acyclic matching.** On each stage's nonempty face poset, process vertices in the fixed order \(0,\ldots,13\). At vertex \(i\), pair each still-unmatched face \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\) if both faces occur and are still unmatched. For every cover relation, orient a matched cover from its lower to its upper face and orient every other cover from its upper to its lower face. `verify_morse.py` constructs this entire finite directed Hasse graph and topologically sorts it, thereby verifying acyclicity, not merely assuming it from the matching recipe. The number of oriented covering relations is respectively \(1568,10150,50764,81634\), and the topological sort visits respectively \(457,2256,8654,12791\) vertices; hence there is no directed cycle. The matching has respectively \(225,1121,4326,6391\) pairs. In the four stages, the complete lists of critical-cell counts by dimension are respectively \(\{0:1,3:6\}\), \(\{0:1,5:13\}\), \(\{0:1,6:1\}\), and \(\{0:1,8:8\}\). The provided checker specifies every pair deterministically and checks each face's participation.

**3. Integral homotopy conclusion.** The discrete-Morse CW theorem gives a CW model having precisely the critical cells in each stage. Each model has a single zero-cell and only cells of one other dimension, which is at least three. The attaching map for each positive-dimensional cell lands in the preceding skeleton, consisting of that single zero-cell. Every such attaching map is constant. The four CW models are consequently the four asserted wedges of spheres, as genuine homotopy equivalences and not just field-homology isomorphisms. In particular all their integral homology is torsion-free.

**4. Persistence.** Nonzero reduced homology occurs in distinct dimensions \(3,5,6,8\) in the successive stages. Thus the induced map in every fixed positive degree between distinct successive stages has either zero source or zero target and must be zero. All reduced degree-zero groups also vanish, since each Morse model is connected. The persistence intervals in the finding follow. Since the ambient graph has maximum degree three, all maps from stage three onward are identities.

## Verification
The self-contained `verify_morse.py` tests membership of all nonempty vertex subsets using cycle-detecting union/find, builds the four sequential matchings, verifies the full oriented Hasse DAG with a topological sort, and prints the exact face, pair, critical-cell and covering-relation counts. Independently, `verify_homology.py` enumerates the complexes using a different forest predicate based on connected components and the identity \(|E|=|V|-c\), then reduces every simplicial boundary matrix over \(\mathbb F_2\). The latter obtains reduced ranks \(6\) in degree \(3\), \(13\) in degree \(5\), \(1\) in degree \(6\), and \(8\) in degree \(8\), with no other reduced homology. The two programs and their actual outputs are provided as standalone artifacts. The mod-two calculation is a cross-check; the integral and homotopy conclusions follow from the verified acyclic matchings, not from field ranks.

## Relationship to prior work
Carnero Bravo introduced the induced-vertex forest filtration and calculated it for paths, cycles, double stars, cactus graphs, joins and selected graph products; the Heawood graph and its intermediate stages are not evaluated by those listed classifications. Related work on polyhedral joins addresses different graph families. The independence polynomial of the Heawood graph, and hence the \(d=0\) face-count vector, was already recorded by Perarnau and Perkins. A publicly available earlier homotopy calculation also gives exactly \(\operatorname{Ind}(H)\simeq\bigvee^6 S^3\); **that result is acknowledged as prior and is not asserted to be new**. Its single-stage statement and the cited polynomial do not determine the higher forest stages or their inclusion-induced persistence. The new value here is the complete four-stage integral homotopy and persistence description for this canonical cubic incidence graph.

## Limitations
The theorem is for the fourteen-vertex Fano incidence graph only. It does not classify forest filtrations of all projective-plane incidence graphs, all cubic graphs, or arbitrary degree thresholds on larger graphs. No equivariant homotopy or automorphism action is claimed. The computational proof is exhaustive for this finite object, not a general infinite-family theorem; it relies on a complete explicit acyclic matching verified by executable finite calculations. An equivalent result in unindexed literature is still possible, and independent mathematical validation has not been performed.

## References
- A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first posted July 25, 2023, especially Sections 3 and 4.
- A. Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321, first posted July 26, 2023, especially Sections 4 and 5.
- G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, *Journal of Combinatorial Theory, Series B* (2018), DOI:10.1016/j.jctb.2018.04.009.
- *The Heawood independence complex is a wedge of six three-spheres*, public 2026 result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2 (the previously known \(d=0\) case).
- R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
