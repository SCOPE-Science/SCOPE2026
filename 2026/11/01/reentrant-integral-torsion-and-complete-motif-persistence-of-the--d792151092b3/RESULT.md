# Reentrant integral torsion and complete motif persistence of the Paley-eleven tournaplex

## Finding
Let \(T\) be the Paley tournament with vertex set \(\mathbb F_{11}\), oriented by \(i\to j\) exactly when \(j-i\in\{1,3,4,5,9\}\). For each real \(t\ge0\), let \(F_t\) be the simplicial complex of all nonempty \(S\subseteq\mathbb F_{11}\) with at most \(t\) cyclically oriented three-vertex subtournaments. Thus \(F_t\) is the \(c_3\)-directionality stage of the complete flag tournaplex of \(T\).

**Theorem.** The entire reduced integral homology of each \(F_t\), and the entire positive-degree persistent homology over both \(\mathbb F_2\) and \(\mathbb F_3\), are specified by the three adjoining exact CSV tables `integral_stages.csv`, `barcode_F2.csv`, and `barcode_F3.csv`. In particular, integral torsion occurs at precisely two distinct stages:
\[
\widetilde H_2(F_0;\mathbb Z)\cong\mathbb Z^{10}\oplus\mathbb Z/2,
\qquad
\widetilde H_5(F_{12};\mathbb Z)\cong\mathbb Z/2,
\]
and no other integral torsion occurs anywhere in the filtration. The only other nonzero integral group at \(t=12\) is \(\widetilde H_6(F_{12};\mathbb Z)\cong\mathbb Z^{65}\). The torsion disappears for every \(1\le t<12\), reappears for \(12\le t<13\), and is absent for all \(t\ge13\).

The mod-two barcode contains exactly \(727\) positive-length intervals of \(20\) types, whereas the mod-three barcode contains \(726\) such intervals of \(18\) types. In degree three, the mod-two barcode includes one interval \([0,4)\) absent over \(\mathbb F_3\). At degree five the mod-two barcode includes one interval \([6,13)\) absent over \(\mathbb F_3\). All bars are finite, and the reduced degree-zero persistence vanishes. Neither barcode is claimed to be integral or to hold for all coefficient fields.

The stage boundaries, with repetitions of integral homology ranks encoded in the table, are
\[
0,1,2,3,4,5,6,7,8,11,12,13,18,19,28,40,55.
\]
At \(t\ge55\), the complex is the full ten-simplex and is contractible. At each nonnegative real \(t\), use the row indexed by the greatest boundary not exceeding \(t\).

### Complete mod-two barcode

| Degree | Birth | Death | Multiplicity |
| ---: | ---: | ---: | ---: |
| 2 | 0 | 1 | 11 |
| 3 | 0 | 4 | 1 |
| 3 | 1 | 3 | 40 |
| 3 | 1 | 4 | 4 |
| 3 | 2 | 3 | 55 |
| 4 | 3 | 6 | 5 |
| 4 | 3 | 7 | 10 |
| 4 | 4 | 6 | 210 |
| 4 | 4 | 7 | 5 |
| 5 | 6 | 12 | 4 |
| 5 | 6 | 13 | 1 |
| 5 | 7 | 11 | 55 |
| 5 | 7 | 12 | 40 |
| 5 | 8 | 11 | 110 |
| 6 | 12 | 18 | 55 |
| 6 | 12 | 19 | 11 |
| 6 | 13 | 19 | 54 |
| 7 | 19 | 28 | 45 |
| 8 | 28 | 40 | 10 |
| 9 | 40 | 55 | 1 |

### Complete mod-three barcode

| Degree | Birth | Death | Multiplicity |
| ---: | ---: | ---: | ---: |
| 2 | 0 | 1 | 10 |
| 3 | 1 | 3 | 40 |
| 3 | 1 | 4 | 5 |
| 3 | 2 | 3 | 55 |
| 4 | 3 | 6 | 5 |
| 4 | 3 | 7 | 10 |
| 4 | 4 | 6 | 210 |
| 4 | 4 | 7 | 5 |
| 5 | 6 | 12 | 5 |
| 5 | 7 | 11 | 55 |
| 5 | 7 | 12 | 40 |
| 5 | 8 | 11 | 110 |
| 6 | 12 | 18 | 55 |
| 6 | 12 | 19 | 10 |
| 6 | 13 | 19 | 55 |
| 7 | 19 | 28 | 45 |
| 8 | 28 | 40 | 10 |
| 9 | 40 | 55 | 1 |

## Assumptions and scope
The tournament is the explicit quadratic-residue orientation above. A cyclic triple is either of the two cyclic orientations of three vertices, not a directed path. A simplicial \(k\)-face is a vertex subset of cardinality \(k+1\). All faces of a given weight are entered simultaneously, with inclusions at the integer threshold itself. Persistent homology is ordinary reduced simplicial homology with coefficients in the stated field, including its induced inclusion maps. Intervals are half-open, and zero-length intervals are omitted. The complete tournaplex is a genuine abstract simplex here because each vertex set induces exactly one tournament, so no multiple simplices are identified. Integral pointwise homology is not being interpreted as an interval decomposition.

## Proof
**1. Finite object and its critical values.** The nonzero quadratic residues modulo eleven are exactly \(1,3,4,5,9\). Every vertex has five out-neighbors and every pair has two common out-neighbors. An unordered triple is cyclic exactly when its three arrows form a directed cycle. Examining the \(165\) triples gives precisely \(55\) cyclic triples. All \(2047\) nonempty vertex subsets are enumerated by their eleven-bit masks. Independently, the weights are reconstructed by adding the highest set bit and counting only the newly introduced cyclic triples. Both determinations agree and yield the exact critical values displayed above. The weights are nondecreasing under inclusion, so \(F_t\) is a simplicial filtration.

**2. Exact persistence over each field.** Sort all faces by the triple \((c_3(S),\dim S,\operatorname{mask}(S))\). For \(\mathbb F_2\), form the boundary columns using the faces obtained by deleting one vertex, represented as bitsets. Reduce each column using the previously reduced column with the same maximal nonzero row. If a column becomes zero, it creates a class; if not, its maximal row pairs the earlier creator with the current killing face. For \(\mathbb F_3\), run the same filtration with the increasing-vertex signed boundary and exact sparse modular elimination, with coefficient inverses mod three. In both fields the boundary operator squares to zero, all faces precede their cofaces, and the standard persistence pairing theorem applies. The calculations give \(1023\) finite simplex pairs and one enduring ordinary degree-zero generator. After omitting zero-length pairs, the positive-degree intervals are exactly the tables above. Direct, separately implemented mod-two boundary-rank calculations at all seventeen stages agree with the bar-derived Betti numbers. Affine maps \(i\mapsto ai+b\), with \(a\) a nonzero square, preserve every subset weight; all \(55\) are checked.

**3. Exact integral homology.** For every critical value and every differential, construct the signed integer matrix of \(\partial_d:C_d(F_t;\mathbb Z)\to C_{d-1}(F_t;\mathbb Z)\). Repeatedly pivot on an entry \(\pm1\). An integral row operation clears the pivot column, and an integral column operation clears the pivot row without changing the remaining matrix. Thus each step splits off an invariant Smith factor one. For every matrix in the finite list, the remaining matrix is zero or has rank one, checked against *all* two-by-two minors including zero entries. The sole nontrivial invariant factor of a rank-one residual is the greatest common divisor of its entries. The only factors larger than one found anywhere are a single factor two in \(\partial_3\) at level zero (after \(54\) unit factors) and a single factor two in \(\partial_6\) at level twelve (after \(209\) unit factors). Every other Smith factor is one. The free ranks follow from the exact integer matrix ranks by \(\operatorname{rank}\widetilde H_d=\operatorname{rank}C_d-\operatorname{rank}\partial_d-\operatorname{rank}\partial_{d+1}\), using the reduced augmentation in degree zero. Because \(\operatorname{im}\partial_d\) is free, the torsion in \(\operatorname{coker}\partial_{d+1}\) belongs to \(\ker\partial_d/\operatorname{im}\partial_{d+1}\); hence those Smith factors identify precisely the integral homology torsion. This proves every row of `integral_stages.csv` and both displayed torsion assertions.

**4. Coefficient consistency.** The universal coefficient theorem gives the mod-two Betti numbers from the integral ranks and the unique adjacent-degree \(2\)-torsion factors at the two exceptional stages; they agree with the independently computed mod-two stage boundary ranks. The mod-three Betti numbers match the integral free ranks at all stages. These pointwise checks do not replace the persistence reduction for the inclusion maps.

## Verification
Run `python verify.py` in the directory containing `barcode_F2.csv`, `barcode_F3.csv`, and `integral_stages.csv`. The Python standard library is sufficient. The program performs exhaustive simplex generation, direct and recurrence-based cycle counting, the \(55\) affine-symmetry checks, the signed chain-identity check, both full field reductions, all integral Smith reductions, and independent stagewise mod-two boundary ranks. It compares computed values byte-independently to the three attached CSV tables. `verification_output.txt` records a completed execution. The expected terminal marker is `PALEY11_TOURNAPLEX_PERSISTENCE_AND_INTEGRAL_SMITH_OK`.

## Relationship to prior work
Govc, Levi, and Smith introduced the flag tournaplex and its three-cycle directionality filtration; the earliest verified public version appeared on February 29, 2020. Their paper defines the filtration and studies general examples and low-order constructions, but does not calculate this Paley-eleven barcode. Govc's later 2020 preprint classifies doubly regular tournament *directed flag complexes* and already determines the zero-stage homotopy type here as a Moore space with ten additional two-spheres. Accordingly, **the level-zero torsion is prior work, not part of the novelty claim**. The new information is the exact full persistence over two fields, all later integral stages, and the isolated return of integral two-torsion at level twelve.

An earlier result for the cyclic tournament family determines its first two three-cycle-filtration stages; the Paley-eleven tournament is not that cyclic tournament. Previously published equivariant results for the Paley-eleven directed flag complex concern only the zero stage, not the subsequent inclusion maps. Likewise, other published persistence calculations for geometric or graph-metric filtrations have different input objects and filtrations. The literature comparison did not identify a theorem implying this complete statement.

## Limitations
The theorem concerns the explicit eleven-vertex tournament and its canonical motif-count filtration only. It is **not** an all-order formula for Paley tournaments, an integral interval decomposition, a homotopy classification of every intermediate stage, or a statement about characteristics other than two and three. The integral calculations determine the homology groups, not the homotopy groups. The proof uses exhaustive finite computations implemented in the attached verifier; an equivalent unindexed publication remains a bibliographic risk.

## References
1. D. Govc, R. Levi, and J. P. Smith, *Complexes of Tournaments, Directionality Filtrations and Persistent Homology*, arXiv:2003.00324v1 (first posted 2020-02-29); *Journal of Applied and Computational Topology* 5 (2021), 313–337, DOI 10.1007/s41468-021-00068-0. See Definitions 2.2 and 3.3 and Section 3.
2. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333v1 (2020-06-09), especially Proposition 3.4 and Section 3.4.
3. Standard simplex-boundary reduction and the persistent homology pairing theorem; the exact finite implementation and data are provided with this result.
