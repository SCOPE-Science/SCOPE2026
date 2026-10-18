# One-anchor, two-round orbit recovery in balanced subspace Kneser graphs

## Finding
Let \(q\) be any prime power and \(k\ge2\). Let \(V\) be a \(2k\)-dimensional vector space over \(\mathbb F_q\), and let \(G\) have all \(k\)-dimensional subspaces of \(V\) as vertices, with two distinct vertices adjacent exactly when they have zero intersection. Individually mark one vertex \(A\). Ordinary one-dimensional colour refinement, starting with the two colours \(\{A\}\) and \(V(G)\setminus\{A\}\), recovers the complete automorphism-orbit partition within **two rounds**, uniformly in \(q\) and \(k\). In fact, its stable classes are exactly the sets
\[
\mathcal O_s(A)=\{U:\dim(U\cap A)=s\},\qquad 0\le s\le k.
\]
They are already obtained after one round if \(k=2\); the two-round bound is sharp for every \(k\ge3\).

The number of classes is \(k+1\), and their cardinalities are
\[
|\mathcal O_s(A)|=q^{(k-s)^2}\left[\begin{matrix} k\\s\end{matrix}\right]_q^{\!2}.
\]
For any \(U\in\mathcal O_s(A)\), the number of common neighbours of \(U\) and \(A\) has the exact value
\[
|N(U)\cap N(A)|=q^{k^2}\prod_{j=1}^{k-s}(1-q^{-j}),
\]
where the empty product is one. These numbers are strictly increasing with \(s\). The contribution claimed here is the explicit sharp colour-refinement/orbit theorem and its proof; Gaussian coefficients, classical subspace orbit classifications, and general colour-refinement theory are prior mathematical tools.

## Assumptions and scope
The graph is the balanced \(q\)-Kneser or subspace-disjointness graph, often denoted \(qK_{2k:k}\), **not** the usual Grassmann graph (which joins subspaces at codimension-one intersection). Vertices are subspaces, not vectors. Dimensions are over \(\mathbb F_q\). The graph is finite, simple, undirected and unweighted. Colour refinement uses a singleton initial colour for \(A\) and another colour for all other vertices, and each round replaces the current colour by its pair with the multiset of neighbours' current colours. An orbit always means an automorphism orbit in this marked graph. No identification claim is made among arbitrary graphs having the same refinement outcome.

## Proof
**Step 1: One parameter is precisely the orbit invariant.** Fix a direct-sum decomposition \(V=A\oplus B\), with \(\dim A=\dim B=k\). For a \(k\)-subspace \(U\), let \(C=U\cap A\) of dimension \(s\), and \(D=\pi_B(U)\) of dimension \(r=k-s\). Modulo \(C\), the space \(U\) is the graph of a linear map \(D\to A/C\). A block-upper-triangular linear automorphism of \(V\) fixing \(A\) removes this map. Block-diagonal automorphisms then move any \(C\) and \(D\) of their fixed respective dimensions to standard coordinate subspaces. Thus the stabilizer of \(A\) in \(\mathrm{GL}(V)\) acts transitively on each \(\mathcal O_s(A)\). Conversely, every graph automorphism fixing the marked vertex preserves its colour at every refinement round, so no refinement class can split an orbit of this subgroup.

For the size, independently choose \(C\le A\) with dimension \(s\), \(D\le B\) with dimension \(r\), and the linear map \(D\to A/C\). This gives \(\left[\begin{smallmatrix}k\\s\end{smallmatrix}\right]_q\left[\begin{smallmatrix}k\\r\end{smallmatrix}\right]_q q^{r^2}=q^{r^2}\left[\begin{smallmatrix}k\\s\end{smallmatrix}\right]_q^2\) choices, uniquely. The \(k+1\) nonempty sets partition all vertices.

**Step 2: Count common neighbours.** Since the stabilizer of \(A\) is transitive on \(\mathcal O_s(A)\), assume \(U=C\oplus D\) with \(C\le A\), \(D\le B\), \(\dim C=s\), \(\dim D=r=k-s\). Every \(k\)-subspace \(W\) disjoint from \(A\) is the graph \(\{f(b)+b:b\in B\}\) of one linear map \(f:B\to A\); there are \(q^{k^2}\) such maps. Such a \(W\) is also disjoint from \(U\) if and only if the induced map \(D\to A/C\), obtained by composing \(f|_D\) with the quotient, is injective. Both vector spaces have dimension \(r\), hence this induced map must be invertible. It has \(|\mathrm{GL}(r,q)|\) choices, each with \(q^{sr}\) lifts to \(A\) on \(D\). On a complement of \(D\) in \(B\), the map \(f\) is arbitrary, giving \(q^{ks}\) further choices. Consequently
\[
|N(A)\cap N(U)|=|\mathrm{GL}(r,q)|q^{sr+ks}
=q^{k^2}\prod_{j=1}^{r}(1-q^{-j}).
\]
This includes the extreme cases \(r=0\) (\(U=A\), all neighbours of \(A\)) and \(r=k\) (\(U\) complementary to \(A\), with \(|\mathrm{GL}(k,q)|\) common neighbours). If \(s<k\), passing from \(s\) to \(s+1\) removes the factor \(1-q^{-(k-s)}\), strictly smaller than one; therefore these counts increase strictly with \(s\).

**Step 3: One refinement step identifies adjacency to \(A\).** Initially only \(A\) is marked. The first round retains its singleton colour, and distinguishes \(N(A)=\mathcal O_0(A)\) from the remaining nonmarked vertices because only the former see one marked neighbour. Every vertex has degree \(q^{k^2}\), by Step 2 with \(U=A\), so no additional splitting occurs. For \(k=2\) these are already exactly the three orbit sets.

**Step 4: A second round distinguishes every orbit.** Since \(N(A)\) is a complete first-round colour class, the next refinement sees, for each \(U\), the number \(|N(U)\cap N(A)|\). By Step 2, this count has distinct values for every \(s=0,\ldots,k\). Hence the second-round colour determines \(s\). Step 1 ensures no class can be finer than the \(\mathcal O_s(A)\), proving equality and immediate stability. For \(k\ge3\), round one has only three classes whereas \(k+1\ge4\); the second round is necessary. All statements are for every prime power \(q\) and every integer \(k\ge2\), not merely checked finite examples. \(\square\)

## Verification
Two executable Python 3 programs accompany this document and need only the standard library. Run `python3 check_refinement.py` and `python3 check_formula.py` from their containing directory. `CHECK_OUTPUT.txt` records the outputs.

The first program independently enumerates every \(k\)-subspace using row-reduced matrices for \((q,k)=(2,2),(3,2),(2,3)\), totaling \(35,130,1395\) graph vertices respectively, builds adjacency by disjointness, computes two refinement rounds, compares the partition with exact intersection-dimensional classes, and directly checks every vertex's common-neighbour count. The second uses Gaussian-subspace Möbius inversion (rather than graph-of-a-linear-map enumeration) for \(35\) parameter configurations and \(210\) intersection signatures, and checks the orbit-size sum and monotonicity. All stated checks passed. These finite tests **do not** prove the unbounded claim: the four proof steps above do.

## Relationship to prior work
Blokhuis, Brouwer, and Szőnyi studied precisely the balanced subspace-disjointness graph \(qK_{2k:k}\), determining chromatic numbers in substantial ranges and structural properties of intersecting families. Their primary article (full open-access PDF, including theorems and bibliography, inspected) is about chromatic and extremal properties rather than colour-refinement recovery of single-anchor orbit classes. The object and its elementary linear-algebraic symmetries are therefore prior, not claimed as introduced here.

Arvind, Köbler, Rattan, and Verbitsky give the standard colour-refinement formalism, its relation with two-variable counting logic, and general classes of refinable graphs; their full HTML article (including definitions and refinability discussion, inspected) does not specialize its results to balanced \(q\)-Kneser graphs or assert the above uniform two-round bound. Classical finite Grassmann association-scheme intersection numbers could entail the common-neighbour formula; numerical counts alone are not claimed novel. The complete implication from relevant earlier intersection-number formulas to the stated exact two-round orbit classification is a residual publication-priority risk. This statement is stronger than the ordinary set-Kneser-graph analyses and distinct from colour refinement on finite subspace lattices (whose relation and vertex set differ).

## Limitations
The ambient vector-space dimension is exactly \(2k\). Neither nonbalanced \(q\)-Kneser parameters nor arbitrary relational structures are classified. The argument gives recovery of orbits **inside the marked graph**, not complete graph identification by counting logic. No claim is made that the familiar association-scheme constants or Gaussian enumeration formulas are new. Comparison with specialized earlier association-scheme and dissertation literature is not exhaustive. Reproducibility does not substitute for independent peer review; no independent scientific audit has been performed.

## References
1. A. Blokhuis, A. E. Brouwer, T. Szőnyi, *On the chromatic number of q-Kneser graphs*, Designs, Codes and Cryptography 65 (2012), 187–197; published online 10 May 2011. DOI: `10.1007/s10623-011-9513-1`. Open-access PDF: `https://link.springer.com/content/pdf/10.1007/s10623-011-9513-1.pdf`.
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, initial version 4 February 2015, especially Sections 1, 2, and 8. `https://arxiv.org/html/1502.01255v3`.
3. T. J. J. Mussche, *Extremal combinatorics in generalized Kneser graphs*, doctoral dissertation, Eindhoven University of Technology, 2009, DOI: `10.6100/IR642440`. The abstract was inspected; full text could not be retrieved for the present comparison.
