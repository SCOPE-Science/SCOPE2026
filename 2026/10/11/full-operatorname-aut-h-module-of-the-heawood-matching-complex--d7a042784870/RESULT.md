# Full \(\operatorname{Aut}(H)\)-module of the Heawood matching complex

## Finding
Let \(H\) be the Heawood graph, the bipartite incidence graph of the Fano plane. Write \(G=\operatorname{Aut}(H)\) and \(B\le G\) for the subgroup preserving the two vertex classes. There are exactly \(336\) automorphisms in \(G\) and \(168\) in \(B\). Let \(\mathcal M(H)\) be the **ordinary** simplicial matching complex: its vertices are the \(21\) edges of \(H\), and its simplices are sets of mutually vertex-disjoint edges. Over the rational numbers,
\[
\widetilde H_i(\mathcal M(H);\mathbb Q)=0\qquad(i\ne4),
\qquad
\widetilde H_4(\mathcal M(H);\mathbb Q)\cong \mathbf1\oplus T\oplus W.
\]
Here \(\mathbf1\) is the trivial one-dimensional \(G\)-representation, \(T\) is the seven-dimensional reduced permutation module on the eight Sylow-\(7\) subgroups of \(B\), which \(G\) permutes by conjugation, and \(W\) is an irreducible eight-dimensional rational \(G\)-representation. Thus the invariant fourth homology has dimension exactly one.

The *entire* fourth-homology character is given by the following table. The first column tells whether an automorphism preserves or exchanges the two vertex classes; the second column is its order, the third is the number of such automorphisms, the fourth is the trace of its action on fourth homology, and the last two are the traces on \(T\) and \(W\), respectively. Each pair of class action and order is a single character type for the present calculation.

| Action | Order | Count | \(\chi_{H_4}\) | \(\chi_T\) | \(\chi_W\) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Preserves | 1 | 1 | 16 | 7 | 8 |
| Preserves | 2 | 21 | 0 | -1 | 0 |
| Preserves | 3 | 56 | 1 | 1 | -1 |
| Preserves | 4 | 42 | 0 | -1 | 0 |
| Preserves | 7 | 48 | 2 | 0 | 1 |
| Exchanges | 2 | 28 | 4 | 1 | 2 |
| Exchanges | 6 | 56 | 1 | 1 | -1 |
| Exchanges | 8 | 84 | 0 | -1 | 0 |

The nonequivariant homotopy equivalence to sixteen four-spheres was previously calculated and is **not** asserted to be new; the finding here is the rational symmetry-module decomposition and complete action character.

## Assumptions and scope
Label the points \(p_0,\ldots,p_6\) and lines \(\ell_0,\ldots,\ell_6\), with subscripts modulo \(7\). The incidence relation is \(p_i\sim\ell_j\) if and only if \(i-j\pmod7\in\{0,1,3\}\). Every pair of distinct lines intersects at exactly one point, determining the Fano plane. Every graph automorphism acts simplicially on \(\mathcal M(H)\). Homology and module decompositions are **over \(\mathbb Q\)**: the theorem does not assert an integral decomposition into irreducible lattices or an equivariant homotopy equivalence. In particular, \(\mathcal M(H)\) is not the complex whose vertices are perfect matchings.

The Sylow-subgroup module is unambiguous: \(B\) acts on its own order-\(7\) subgroups by conjugation, and the full group \(G\) normalizes \(B\), hence also acts. The augmentation kernel of the resulting rational permutation module on eight subgroups is \(T\).

## Proof
**1. The complete chain ranks.** Enumerate all nonempty matchings of the \(21\) incidences. The numbers of simplices in dimensions \(0\) through \(6\) are
\[
(21,168,644,1218,1050,336,24).
\]
Direct binary Gaussian elimination on each complete simplicial boundary matrix gives ranks over \(\mathbb F_2\), from degree \(1\) through \(6\),
\[
(20,148,496,722,312,24).
\]
These are also the ranks over \(\mathbb Q\), without any appeal to an unsupported equality of field ranks: for an integer matrix its rational rank is at least its rank modulo \(2\); moreover, the chain-complex identities imply \(r_{k}+r_{k+1}\le\dim C_k\). The upper bound \(r_1\le20\) gives \(r_1=20\), and successively \(r_2\le168-20=148\), \(r_3\le644-148=496\), and \(r_4\le1218-496=722\); the displayed binary lower bounds force equality in each case. At the top \(r_6\le24\), so \(r_6=24\), and then \(r_5\le336-24=312\), again forcing equality. It follows that the only nonzero reduced rational homology is \(\widetilde H_4\), of dimension \(1050-722-312=16\).

**2. Exhausting the symmetry group.** A colour-preserving automorphism is a permutation of the seven points taking each of the seven line sets \(\{j,j+1,j+3\}\) to another line set, with a uniquely induced permutation of lines. Enumerating these point permutations gives exactly \(168\) such automorphisms. The explicit duality \(p_i\mapsto\ell_{-i}\), \(\ell_j\mapsto p_{-j}\) preserves incidence and exchanges the two bipartition classes. Because the connected incidence graph has a unique bipartition, all its automorphisms either preserve or exchange the parts; composing duality with all \(168\) colour-preserving automorphisms gives all \(336\), with no missing case.

**3. A complete Lefschetz character.** For \(g\in G\), enumerate the matching simplices fixed *setwise* by the induced permutation of the \(21\) graph edges. A fixed simplex \(\sigma\) of dimension \(k\) contributes \((-1)^k\operatorname{sgn}(g|_\sigma)\) to the ordinary Lefschetz number. Since the fixed homology is concentrated in degrees \(0\) and \(4\),
\[
\operatorname{tr}\bigl(g\mid\widetilde H_4\bigr)
=-1+\sum_{\substack{\varnothing\ne\sigma\in\mathcal M(H)\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma).
\]
The checker independently evaluates the same quantity by decomposing the edge permutation of \(g\) into cycles, selecting only collections of cycles whose union is a matching, and applying the signed-cycle identity
\[
\operatorname{tr}\bigl(g\mid\widetilde H_4\bigr)
=-\sum_{\substack{J\text{ a collection of edge cycles}\\\cup J\text{ is a matching}}}(-1)^{|J|},
\]
including the empty collection. The two computations agree for every one of the \(336\) automorphisms, yielding exactly the eight rows in the table.

**4. Identifying the rational constituents.** The colour-preserving group has exactly eight Sylow-\(7\) subgroups, obtained by generating cyclic groups from its order-seven automorphisms. For each \(g\in G\), conjugate each of these eight subgroups and count the fixed ones. That count minus one is the character \(\chi_T(g)\). Define \(\chi_W=\chi_{H_4}-1-\chi_T\); direct summation over all \(336\) group elements gives
\[
\left\langle\chi_X,\chi_Y\right\rangle_G=\delta_{XY}
\quad\text{for }X,Y\in\{\mathbf1,T,W\}.
\]
Over \(\mathbb Q\), Maschke's theorem and the ordinary character inner-product criterion imply that the trivial constituent and \(T\) each occur with multiplicity one and the eight-dimensional residual constituent \(W\) is irreducible. No classification table of representations of \(G\) is assumed. The dimensions \(1+7+8=16\) complete the decomposition.

## Verification
The accompanying standalone `verify_heawood_action.py` is Python-standard-library-only. Execute `python3 verify_heawood_action.py`. It rebuilds the incidence graph, enumerates the \(3461\) nonempty matching simplices and all six binary boundary ranks, lists all \(336\) graph automorphisms, computes the signed Lefschetz trace and an independent orbit-cycle trace for each, identifies all eight Sylow-\(7\) subgroups, and computes the three exact character inner products. A successful run prints `VERIFY_OK` and the character-type counts. These finite calculations are exhaustive for the explicitly specified finite graph, not sampling or an extrapolation to other graphs.

## Relationship to prior work
Donovan and Scoville (2022) introduce star-cluster techniques and calculate homotopy types of matching complexes for paths, cycles and Dutch windmill families, rather than this particular incidence graph or its homology character. Li (2022) proves equivariant log-concavity for the *graded permutation representations on sets of matchings*; this does not itself state the irreducible decomposition of the fourth simplicial homology of the Heawood matching complex. A separate previously published calculation of \(\mathcal M(H)\) gives the sixteen-sphere homotopy type, which supplies nonequivariant context but no \(336\)-element trace table or \(1\oplus7\oplus8\) module statement. Thus this result refines a known homotopy type by determining its rational action, rather than relabeling the previously known Betti number.

## Limitations
The proof is finite and specific to the Heawood graph, with exhaustive (reproducible) rather than closed-form character enumeration. It gives a complete rational representation character but neither an integral lattice splitting nor an equivariant CW-homotopy classification. Failure to locate a published equivalent representation calculation is not a mathematical proof of absolute novelty; literature under alternate indexing or specialized incidence-geometry terminology may remain. No claim is made about higher projective-plane incidence graphs.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1 (first public 2022-07-27), primary MSC 57Q70.
2. S. Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828 (first public 2022-02-17).
3. *The Heawood matching complex is a wedge of sixteen 4-spheres*, public mathematical report, identifier 7150930ba12a (2026). Its nonequivariant claim is treated as prior work, not as part of the new assertion.
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
