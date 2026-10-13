# Four-set obstructions and two optimal forcing-triple types in the Heawood graph

## Finding
Let \(H\) be the incidence graph of the Fano plane and \(M\) any perfect matching of \(H\). A **forcing set for \(M\)** is an edge subset \(S\subseteq M\) contained in no other perfect matching. Every perfect matching has forcing number \(3\). More precisely, the generating polynomial of all its forcing subsets, including nonminimum ones, is
\[
F_M(z)=\sum_{S\subseteq M\,\mathrm{forcing}}z^{|S|}=14z^3+28z^4+21z^5+7z^6+z^7.
\]
Every matching has exactly fourteen minimum forcing sets, belonging to two inequivalent symmetry classes of seven each under its matching stabilizer. Across all twenty-four perfect matchings, the \(336\) minimum forcing triples fall into two orbits, each of size \(168\), under the full graph automorphism group of order \(336\).

There is a stronger intrinsic obstruction description. Label the graph's point vertices \(p_i\) and line vertices \(\ell_j\), indexed by \(i,j\in\mathbb Z/7\mathbb Z\), with \(p_i\ell_j\) an edge exactly when \(j-i\in\{0,2,3\}\). Fix the diagonal perfect matching \(M_0=\{e_i=p_i\ell_i:i\in\mathbb Z/7\mathbb Z\}\). Set
\[
 B_t=\{e_t,e_{t+1},e_{t+3},e_{t+5}\},\qquad t\in\mathbb Z/7\mathbb Z.
\]
For every \(S\subseteq M_0\), **\(S\) forces \(M_0\) if and only if \(S\) is contained in none of the seven sets \(B_t\)**. Exactly the fourteen forcing triples are
\[
\{e_t,e_{t+1},e_{t+4}\}\quad\text{and}\quad\{e_t,e_{t+1},e_{t+6}\},\qquad t\in\mathbb Z/7\mathbb Z.
\]

## Assumptions and scope
The graph is finite, undirected, simple, and its fourteen vertices are the seven points and seven lines of \(\mathrm{PG}(2,2)\). The chosen cyclic incidence representation uses the difference set \(\{0,2,3\}\) and all subscripts are read modulo seven. A forcing set is **local to a specified perfect matching**: each selected edge belongs to that matching, and exactly one perfect matching extends the selection. This is not the separate notion of a global edge-set forcing every matching simultaneously, nor is it ordinary vertex zero forcing or anti-forcing by edge deletion.

## Proof
**Step 1: exhaustive matching classification with a short finite certificate.** Any perfect matching corresponds uniquely to a permutation \(\pi\) of \(\mathbb Z/7\mathbb Z\) with displacement word \(d_i=\pi(i)-i\in\{0,2,3\}\). There are exactly twenty-four such permutations, as can be verified by the seven-row depth-first enumeration in `verify.py`, independently confirmed by the exact Ryser permanent of the seven-by-seven incidence matrix. Under cyclic rotation of the indices, the displacement words split into six disjoint families; one representative of each, with its orbit size and number of zero positions, is:

| Displacement word | Orbit size | Zero positions |
|---|---:|---|
| `(0,0,0,0,0,0,0)` | 1 | `0,1,2,3,4,5,6` |
| `(2,2,2,2,2,2,2)` | 1 | none |
| `(3,3,3,3,3,3,3)` | 1 | none |
| `(0,0,2,0,2,0,3)` | 7 | `0,1,3,5` |
| `(0,2,3,3,0,3,3)` | 7 | `0,4` |
| `(0,2,2,2,2,3,3)` | 7 | `0` |

The six listed words obey the incidence restrictions and are permutations; their twenty-four distinct cyclic rotations exhaust the twenty-four matchings certified by the permanent. Hence the intersections of a different perfect matching with \(M_0\) are: seven four-element sets \(B_t\), seven two-element sets that are contained in some \(B_t\), seven singleton sets, and two empty sets. In particular, **every intersection with a different matching lies inside one of the seven \(B_t\)**, and every \(B_t\) occurs as such an intersection.

**Step 2: all forcing sets.** A subset of \(M_0\) is nonforcing exactly when it is included in an intersection \(M_0\cap M'\) for some \(M'\ne M_0\). Step 1 proves the stated seven-block obstruction criterion. Every singleton and every pair lies in a block. Of the \(\binom73=35\) triples, exactly \(21\) are included in a block; the remaining fourteen are precisely the two displayed seven-element cyclic families, as can be checked directly from the seven explicitly specified blocks. Exactly seven four-subsets are nonforcing (the blocks themselves). Every subset of five or more edges is forcing because no competing matching shares five edges with \(M_0\). Consequently the coefficients by size three through seven are \(14,\binom74-7=28,\binom75=21,\binom76=7,\binom77=1\).

**Step 3: matching equivalence and symmetry.** The linear collineation group \(\mathrm{GL}(3,2)\), of order \(168\), acts on the Fano incidence graph; adjoining point-line duality yields all \(336\) graph automorphisms. Enumerating the group as the invertible binary three-by-three matrices and the duality action, `verify.py` shows that the \(24\) perfect matchings form one orbit and that the stabilizer of \(M_0\) has order \(14\). Each seven-member forcing-triple family above is preserved by this stabilizer and is internally transitive, and the two families are not exchanged. Thus their full automorphism orbits each have \(24\cdot7=168\) members. A forcing triple extends to a unique perfect matching by definition, so the orbits are disjoint and together contain exactly \(24\cdot14=336\) triples.

## Verification
Run `python3 verify.py` from the directory containing the embedded verifier; no third-party dependencies are needed. The program reconstructs the graph in two independent coordinatizations (cyclic difference set and nonzero vectors over the two-element field), computes the permanent independently of permutation enumeration, tests all \(128\) possible edge subsets for each of the \(24\) matchings against the direct unique-extension definition, and independently constructs the full \(336\)-element automorphism action. Assertions check all claimed counts, the seven-block obstruction criterion, both cyclic families and orbit multiplicities. These are complete finite searches on a specified fourteen-vertex graph, not samples or an asymptotic inference.

## Relationship to prior work
Afshani, Hatami, and Mahmoodian develop forcing numbers and forcing spectra for perfect matchings. Che and Chen survey the local forcing-set definition, alternative-matching characterizations, and general bounds. Work on 2-factor Hamiltonicity identifies the Heawood graph as a distinguished cubic brace, but a Hamiltonian complement alone does not specify which collections of matching edges determine a matching, nor the fourteen triples and obstruction blocks here. Earlier matching-count information, including the number twenty-four, likewise does not determine the local forcing-subset polynomial. The separate concept of a global perfect-matching forcing set is not asserted as new here. No claim of exhaustive priority verification beyond the inspected sources and database searches is made.

## Limitations
The explicit polynomial and orbit classification apply only to the Heawood graph. The proof uses finite exhaustive classification of its twenty-four matchings and a full automorphism enumeration; it does not give a closed classification for larger projective-plane incidence graphs. Prior literature may contain a numerically or structurally equivalent result under another name or in an unindexed source. The calculation is reproducible but no independent external mathematical audit has been performed.

## References
- O. Afshani, H. Hatami, E. S. Mahmoodian, “On the spectrum of the forced matching number of graphs,” arXiv:0903.2578, initial public posting 2009-03-14, https://arxiv.org/abs/0903.2578.
- Z. Che and Z. Chen, “Forcing on perfect matchings — a survey,” *MATCH Communications in Mathematical and in Computer Chemistry* **66** (2011), 93–136, https://match.pmf.kg.ac.rs/electronic_versions/Match66/n1/match66n1_93-136.pdf.
- M. Gorsky, M. Johanni, S. Wiederrecht, “A note on the 2-Factor Hamiltonicity Conjecture,” arXiv:2408.08128, 2024, https://arxiv.org/abs/2408.08128.
