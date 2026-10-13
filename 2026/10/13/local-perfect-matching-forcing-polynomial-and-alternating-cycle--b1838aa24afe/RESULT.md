# Local perfect-matching forcing polynomial and alternating-cycle packing gap of the Coxeter graph

## Finding
Let \(X\) be the Coxeter graph, and let \(M\) be **any** perfect matching of \(X\). For each subset \(S\subseteq M\), call \(S\) forcing when \(M\) is the unique perfect matching containing all edges of \(S\). Define the local forcing-subset polynomial
\[
P_M(z)=\sum_{\substack{S\subseteq M\\S\text{ forcing}}}z^{|S|}.
\]
Then, independently of the choice of \(M\),
\[
\begin{aligned}
P_M(z)={}&198z^4+1018z^5+2300z^6+3124z^7\\
&+2918z^8+1988z^9+1000z^{10}\\
&+364z^{11}+91z^{12}+14z^{13}+z^{14}.
\end{aligned}
\]
Thus every perfect matching has forcing number \(4\) and exactly \(198\) minimum forcing four-sets. The \(84\) perfect matchings together contribute \(16{,}632\) different minimum forcing four-sets. Under the full automorphism group of size \(336\), these four-sets form exactly \(51\) orbits: \(48\) orbits of size \(336\) and \(3\) of size \(168\).

Write \(\nu_M\) for the maximum number of pairwise vertex-disjoint \(M\)-alternating cycles. Then every perfect matching satisfies
\[
\nu_M=2,\qquad f(X,M)=4,\qquad f(X,M)-\nu_M=2.
\]
The complete multiset of lengths of \(M\)-alternating cycles is \(8:1,\ 10:4,\ 12:4,\ 14:12,\ 16:9,\ 18:4,\ 20:16,\ 22:16,\ 24:8\), giving \(74\) cycles per matching. Here an alternating cycle means a simple even cycle whose successive edges alternate between belonging and not belonging to \(M\).

## Assumptions and scope
Realize the graph without any external adjacency file. Take the seven nonzero vectors of \(\mathbb F_2^3\), identified with integers \(1,\ldots,7\) using binary-coordinate order. There are seven three-point Fano lines \(\{a,b,a\oplus b\}\). Let \(\mathcal T\) be the set of three-element subsets of the seven points which are **not** lines. Then \(|\mathcal T|=28\), and the vertices of \(X\) are the triples in \(\mathcal T\), with adjacency exactly when the triples are disjoint. Order \(\mathcal T\) lexicographically and use zero-based vertex labels \(0,\ldots,27\) in machine-readable certificates. This is the standard Fano-triangle model of the Coxeter graph; it has \(42\) edges and all degrees \(3\).

For every assertion quantified over perfect matchings, the quantifier ranges over all perfect matchings of this fixed \(28\)-vertex simple graph, without geometric restrictions on those matchings. The polynomial above counts **forcing edge subsets of one fixed matching**, not matchings classified by their forcing numbers (the distinct invariant sometimes called the forcing spectrum) and not arbitrary edge subsets of the graph.

## Proof
**Forcing-set criterion.** For every perfect matching \(N\ne M\), let \(D_N=M\setminus N\). Then a subset \(S\subseteq M\) is forcing if and only if \(S\cap D_N\ne\varnothing\) for every \(N\ne M\). Indeed \(S\subseteq N\) is equivalent to \(S\cap(M\setminus N)=\varnothing\). Consequently the polynomial is obtained by exhausting the \(2^{14}\) subsets of \(M\) and checking those \(83\) nonempty difference masks. This is an exact finite decision procedure, not a sampling argument.

**Exhaustive complete-matching enumeration.** At each step select the least unmatched vertex and branch over every unmatched neighbor, deleting both vertices. The root has \(28\) vertices and the recursion terminates on an empty vertex set. Every perfect matching appears in exactly one branch, because its partner at the least unmatched vertex is forced in that branch. The explicit implementation `verify.py` enumerates exactly \(84\) perfect matchings and checks the forcing-subset criterion for every one; the resulting coefficient vector in degrees \(0,\ldots,14\) is
\[
(0,0,0,0,198,1018,2300,3124,2918,1988,1000,364,91,14,1).
\]
For independent confirmation, `verify_independent.cpp` computes, for every subset \(S\) of a canonical \(M\), the number of perfect-matching extensions via the recurrence
\[
c(U)=\sum_{u\in N(v)\cap U}c(U\setminus\{u,v\}),\qquad c(\varnothing)=1,
\]
where \(v\) is the least vertex of nonempty even-sized \(U\), and \(c(U)=0\) for odd-sized \(U\). A forcing \(S\) is characterized by \(c(V\setminus V(S))=1\). This second implementation reproduces the same coefficient vector without using the first implementation's stored matching list in its subset test.

**Automorphism orbits.** Every invertible linear transformation of \(\mathbb F_2^3\) acts on triples. The polarity mapping each noncollinear triple \(\{a,b,c\}\) to the normals of the connecting lines \(ab,ac,bc\) produces a further graph automorphism. These maps generate \(336\) distinct adjacency-preserving permutations. A separate adjacency-preserving backtrack fixing the image of one vertex and extending over successive adjacent vertices enumerates exactly \(336\) permutations, so no other automorphisms exist. Applying the \(336\) maps to one canonical perfect matching reaches all \(84\) matchings. Thus the per-matching results hold uniformly, and orbit enumeration on all \(84\cdot198\) forcing four-sets gives the asserted \(51\) orbit sizes; `quartet_orbits.csv` records one representative per orbit.

**Alternating-cycle criterion and packing.** The symmetric difference of any two perfect matchings decomposes into vertex-disjoint alternating cycles. Conversely, flipping an \(M\)-alternating cycle gives a distinct perfect matching, so every such cycle appears as a component of the symmetric difference with some enumerated perfect matching. Extracting every connected component of every symmetric difference and deduplicating the resulting edge sets yields the \(74\) alternating cycles, with exactly the length distribution stated. The CSV `alternating_cycles.csv` lists their actual edge sets for a canonical \(M\). There is one alternating eight-cycle and four alternating ten-cycles; each of those four ten-cycles meets the eight-cycle in exactly two vertices. Any family of three pairwise vertex-disjoint alternating cycles on \(28\) vertices must contain the unique eight-cycle and two ten-cycles: without the eight-cycle the sum of their lengths is at least \(30\), and using lengths greater than \(10\) exceeds \(28\). But each ten-cycle meets the eight-cycle, so three disjoint cycles are impossible. The explicit exhaustive test finds disjoint ten- and twelve-cycles, proving \(\nu_M=2\). Matching transitivity gives this for every \(M\).

This completes the proof of the unified polynomial, orbit, and strict transversal-versus-packing assertions. All finite enumerations are deterministic, bounded, and included as standalone source files.

## Verification
Use Python 3 standard library and a C++17 compiler. From the directory containing the embedded source and certificates, run `python3 verify.py` and `g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. Python checks every forcing-subset mask for all \(84\) matchings, independently enumerates all graph automorphisms by adjacency-preserving backtracking, verifies all orbit sizes, and generates both certificates. C++ independently checks all \(2^{14}\) subsets of a representative via extension-count dynamic programming, and independently verifies cycle packing. Their expected exact assertions appear in `VERIFICATION.md`.

The compact certificates use the lexicographic triple ordering fixed above. The orbit CSV describes \(51\) orbits and the cycle CSV records all \(74\) alternating cycles of the canonical matching. The checks use only integer arithmetic and exhaustive finite loops; no probabilistic assumptions or floating-point thresholds enter.

## Relationship to prior work
Afshani, Hatami, and Mahmoodian (2009) define forcing sets and forcing numbers and record the established equality between minimum forcing-set size and the maximum number of disjoint alternating cycles for **planar bipartite** graphs. The Coxeter graph is nonplanar and nonbipartite, so that theorem's hypotheses fail; the present explicit difference \(4-2=2\) illustrates the boundary, not a contradiction. Previously published Coxeter-graph matching-polynomial work counts its \(84\) perfect matchings. That count alone does not determine which subsets force each matching, the \(51\) orbit types, or alternating-cycle packings. The latter finer classifications are the precise additional subject here.

## Limitations
This is a finite theorem about this specific \(28\)-vertex graph; no assertion is made about all nonplanar graphs, asymptotic families, or minimal possible orders for the strict gap. The claim of priority for the finer enumerations is provisional: independent verification and a comprehensive historical literature review remain outstanding, and an earlier unindexed computation may exist. The exact enumeration and algorithmic proof are self-contained and do not depend on such a priority assertion. Only self-review has been conducted; independent audit has not been performed.

## References
1. P. Afshani, H. Hatami, E. S. Mahmoodian, *On the spectrum of the forced matching number of graphs*, arXiv:0903.2578v1 (14 March 2009), https://arxiv.org/html/0903.2578v1 .
2. E. W. Weisstein, *Coxeter Graph*, MathWorld, https://mathworld.wolfram.com/CoxeterGraph.html .
3. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17(1):133 (2025), https://www.mdpi.com/2073-8994/17/1/133 .
4. *Spectral Polynomials and Spectra of Graphs Beyond Cubic and Icosahedral Symmetries*, Symmetry 17(2):247 (2025), https://www.mdpi.com/2073-8994/17/2/247 .
