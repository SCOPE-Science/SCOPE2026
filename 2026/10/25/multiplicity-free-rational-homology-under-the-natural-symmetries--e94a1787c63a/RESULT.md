# Multiplicity-free rational homology under the natural symmetries of \(K_2\times K_4\times K_4\)

## Finding

Let \(G=K_2\times K_4\times K_4\) be the categorical graph product, and let \(X=\operatorname{Ind}(G)\) be its simplicial independence complex. Its **natural coordinate symmetry** is
\[
\Gamma=C_2^{\mathrm{layer}}\times((S_4\times S_4)\rtimes C_2^{\mathrm{exchange}}),\qquad |\Gamma|=2304.
\]
The unique nonzero reduced rational homology group \(\widetilde H_3(X;\mathbb Q)\) is a 63-dimensional **multiplicity-free** \(\Gamma\)-representation with precisely eight rational irreducible constituents.

For partitions \(\lambda\ne\mu\) of four, write
\(R_{\lambda,\mu}=\operatorname{Ind}_{S_4\times S_4}^{(S_4\times S_4)\rtimes C_2}(S^\lambda\boxtimes S^\mu)\). For a partition \(\lambda\), write \(R_{\lambda,\lambda}^-\) for the extension of \(S^\lambda\boxtimes S^\lambda\) on which exchange acts by *minus* the tensor-factor flip. Let \(\epsilon\) be the character of the central layer involution, trivial on coordinate symmetries. Then
\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong{}&R_{(4),(4)}^-\oplus R_{(4),(3,1)}\oplus R_{(4),(2,2)}\\
&\oplus R_{(3,1),(3,1)}^-\oplus R_{(3,1),(2,2)}\\
&\oplus(\epsilon\otimes R_{(3,1),(2,1,1)})\oplus R_{(2,2),(2,2)}^-\\
&\oplus(\epsilon\otimes R_{(2,1,1),(2,1,1)}^-).
\end{aligned}
\]
The eight dimensions are respectively \(1,6,4,9,12,18,4,9\). Thus the layer involution has \(+1\) and \(-1\) eigenspaces of dimensions \(36\) and \(27\). The \(S_4\times S_4\)-invariant subspace is one-dimensional, on which coordinate exchange acts by \(-1\), so \(\widetilde H_3(X;\mathbb Q)^\Gamma=0\).

The full character is specified by the following 40 conjugacy classes (two central-layer parities over twenty coordinate types). An unswapped type is an unordered pair of the two \(S_4\) cycle types. A swapped type is the cycle type of the product of the two permutations. Class sizes are for each fixed layer parity.

| Coordinate type | Class size at each layer parity | No layer flip | With layer flip |
|---|---:|---:|---:|
| \((1,1,1,1),\,(1,1,1,1)\) | 1 | 63 | 9 |
| \((1,1,1,1),\,(2,1,1)\) | 12 | 9 | 15 |
| \((1,1,1,1),\,(2,2)\) | 6 | 3 | 21 |
| \((1,1,1,1),\,(3,1)\) | 16 | 0 | 0 |
| \((1,1,1,1),\,(4)\) | 12 | 3 | -3 |
| \((2,1,1),\,(2,1,1)\) | 36 | 3 | 5 |
| \((2,1,1),\,(2,2)\) | 36 | 5 | 3 |
| \((2,1,1),\,(3,1)\) | 96 | 0 | 0 |
| \((2,1,1),\,(4)\) | 72 | 1 | -1 |
| \((2,2),\,(2,2)\) | 9 | 7 | 1 |
| \((2,2),\,(3,1)\) | 48 | 0 | 0 |
| \((2,2),\,(4)\) | 36 | -1 | 1 |
| \((3,1),\,(3,1)\) | 64 | 0 | 0 |
| \((3,1),\,(4)\) | 96 | 0 | 0 |
| \((4),\,(4)\) | 36 | -1 | 1 |
| \(\mathrm{swap}:(1,1,1,1)\) | 24 | -9 | -3 |
| \(\mathrm{swap}:(2,1,1)\) | 144 | -1 | -3 |
| \(\mathrm{swap}:(2,2)\) | 72 | -1 | -3 |
| \(\mathrm{swap}:(3,1)\) | 192 | 0 | 0 |
| \(\mathrm{swap}:(4)\) | 144 | -1 | 1 |

## Assumptions and scope

The vertex set is \(\{0,1\}\times\{1,2,3,4\}^2\), with \((a,i,j)\) and \((b,k,l)\) adjacent precisely when \(a\ne b\), \(i\ne k\), and \(j\ne l\). Elements act by separate permutations of the last two coordinates, their exchange, and the independent flip of the first coordinate. We determine the character of this specified natural subgroup; no claim that it is the complete abstract automorphism group is required. Homology and decomposition are over \(\mathbb Q\); no integral equivariant splitting is asserted.

## Proof

1. **Homological concentration.** Proposition 25 in Antolín Camarena–Carnero Bravo shows for \(m,n\ge2\) that \(\operatorname{Ind}(K_2\times K_m\times K_n)\simeq \bigvee^{(m-1)(n-1)(mn-2)/2}S^3\). At \(m=n=4\), the sphere count is \(63\). Hence \(\widetilde H_i(X;\mathbb Q)=0\) for \(i\ne3\), and its third homology has dimension \(63\).

2. **An exact character formula.** For \(g\in\Gamma\), form a graph \(Q_g\) on the cycles of the permutation of the 32 vertices of \(G\), deleting any cycle containing both endpoints of a graph edge; join two surviving cycles when an edge of \(G\) joins their vertices. A \(g\)-invariant independent vertex set is exactly a union of mutually nonadjacent vertices of \(Q_g\). A face consisting of \(t\) permutation cycles contributes \((-1)^t\) to the alternating signed face sum. The reduced Lefschetz formula and concentration in degree three therefore give
\[
\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))
=\sum_{F\subseteq V(Q_g)\,\mathrm{independent}}(-1)^{|F|}.
\]
The empty set is included. For any induced orbit graph on vertex set \(U\), evaluate the right side exactly by
\[
P(\varnothing)=1,\qquad P(U)=P(U\setminus\{v\})-P(U\setminus N[v]),
\]
with closed neighborhood \(N[v]\) taken *in the induced orbit graph*. This is an exhaustive finite recurrence, not probabilistic sampling.

3. **Only 40 types.** Conjugation and coordinate exchange identify unswapped pairs of cycle types up to order (15 cases). For a coordinate-exchanging element, conjugation reduces its two permutations to the conjugacy type of their product (five cases). The central layer flip doubles these 20 classes, giving 40. The recurrence produces the table above. Every one of the 2304 group elements was also evaluated directly and agreed with its class entry.

4. **Exact irreducible multiplicities.** The rational irreducibles of \(S_4\) have partitions \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\). For unequal partitions, the induced wreath-product module has the sum of the two tensor-product characters on the unswapped sector and trace zero on the exchanged sector. For equal partitions, the two extensions have unswapped character \(\chi_\lambda(\sigma)\chi_\lambda(\tau)\) and exchanged character \(\pm\chi_\lambda(\sigma\tau)\). Multiplying by \(\epsilon\) changes the sign of the layer-flipping sector. Exact inner products of these 40 irreducible characters with the displayed 40-class table give multiplicity one for precisely the eight modules stated, zero for the other 32, and total dimension 63. Thus the decomposition and invariant/eigenspace assertions follow.

## Verification

The included `verify_character.py` and `character_table.json` are complete standalone artifacts; run `python verify_character.py` in their directory with a standard Python 3 interpreter. The verifier constructs the full 32-vertex graph and checks the automorphism condition for all 2304 specified elements, computes the 40 character values via independent-set recursion on vertex-orbit graphs, and verifies all exact irreducible inner products. An **independent face-list implementation** enumerates all 136063 independent subsets, including the empty set, and directly checks signed stable-face sums for all 40 class representatives. The dimension-63 agreement checks the published homotopy theorem but does not independently reprove that theorem. Expected output: `TRIPLE_COMPLETE_GRAPH_INDEPENDENCE_EQUIVARIANT_CHARACTER_VERIFIED` followed by exact counts.

## Relationship to prior work

Antolín Camarena–Carnero Bravo, Proposition 25 (arXiv:2307.12401, pp. 27–30), establishes the nonequivariant wedge of 63 three-spheres in this case. Goyal–Shukla–Singh (arXiv:1905.06926, §3) establishes the two-factor circle-wedge case and discusses three-factor Betti computations, not this symmetry character. The current result determines the 40 character values and full eight-constituent decomposition for the 32-vertex product. A previously indexed rotation-character classification for \(C_{3r}\times K_n\) does not cover this graph: \(K_2\times K_4\times K_4\) has two four-point factors rather than a cycle first factor. Standard Lefschetz and wreath-product character theory supply methods, not this computed decomposition.

## Limitations

This is a finite exact classification under the displayed natural coordinate group, not a uniform family formula. The homology-concentration premise is the published 2023 nonequivariant theorem. The independent face enumeration corroborates the character calculation, but its finite character data alone would not prove the concentration premise. The result does not assert integral equivariant splittings, independent mathematical audit, or uniqueness relative to all unpublished or unindexed literature.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first posted 23 July 2023), Proposition 25, pp. 27–30. https://arxiv.org/abs/2307.12401
2. S. Goyal, S. Shukla and A. Singh, *Homotopy type of independence complexes of certain families of graphs*, arXiv:1905.06926 (first posted 16 May 2019), §3. https://arxiv.org/abs/1905.06926
3. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, §1 and Theorem 5 (related nonequivariant constructions). https://arxiv.org/abs/2601.13432
