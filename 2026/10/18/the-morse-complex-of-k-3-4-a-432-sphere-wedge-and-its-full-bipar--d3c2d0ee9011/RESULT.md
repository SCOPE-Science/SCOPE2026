# The full bipartition-symmetry character on Morse homology of \(K_{3,4}\)

## Finding

Let \(\mathcal M(K_{3,4})\) be the ordinary simplicial Morse complex of acyclic discrete vector fields on the graph \(K_{3,4}\). The bipartition-preserving automorphisms act on its reduced rational homology. The character of \(\widetilde H_5(\mathcal M(K_{3,4});\mathbb Q)\) under \(S_3\times S_4\) is:

| \(S_3\) type \(\backslash\) \(S_4\) type | \((1,1,1,1)\) | \((2,1,1)\) | \((2,2)\) | \((3,1)\) | \((4)\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \((1,1,1)\) | 432 | −16 | 4 | 0 | −2 |
| \((2,1)\) | 0 | 0 | 4 | 0 | −2 |
| \((3)\) | −3 | −1 | 1 | −3 | 1 |

The multiplicities of the rational irreducible outer products \(\operatorname{Sp}^\lambda\boxtimes\operatorname{Sp}^\mu\) are
\[
\begin{pmatrix}
2&8&7&9&4\\
5&17&12&19&8\\
2&8&6&10&3
\end{pmatrix},
\]
with rows \(\lambda=(3),(2,1),(1,1,1)\) and columns \(\mu=(4),(3,1),(2,2),(2,1,1),(1,1,1,1)\). In particular the invariant subspace has dimension two, whereas the whole module has dimension 432.

## Assumptions and scope

Write \(A=\{0,1,2\}\) and \(B=\{3,4,5,6\}\). A vertex of the Morse complex is an incidence \((u,\{u,v\})\) along a graph edge, encoded as an arc \(u\to v\). A face has distinct sources and underlying edges and contains no directed cycle. These are exactly the acyclic Forman matchings on a graph: the distinctness is the matching condition, and a closed alternating path in the incidence matching is a directed cycle of arcs. Equivalently the faces are rooted forests oriented toward their roots. In the outgoing-neighbor description, a repeated underlying edge in opposite orientations is a directed cycle of length two and is rejected. The empty face contributes to reduced chain traces. The result concerns rational homology, not an equivariant wedge equivalence or the graph's two-matching complex.

## Proof

The previously established ordinary homotopy equivalence \(\mathcal M(K_{3,4})\simeq\bigvee^{432}S^5\) [1] gives the homological concentration in degree five. We use this homotopy type as input; it does not determine how graph automorphisms act.

Enumerate faces by assigning to each of the seven vertices either no outgoing arc or one outgoing neighbor across the bipartition. Discard a choice if following outgoing arcs from any vertex returns to a vertex already visited on that path. The remaining choices enumerate every face exactly once, because a face determines each outgoing choice and these are precisely the acyclic choices. By cardinality \(0,1,\ldots,6\) the counts are \((1,24,234,1192,3357,4968,3024)\). They also agree with the coefficients of \((t+7)(t+4)^2(t+3)^3\) in descending degree by the rooted matrix-forest identity.

For \(g=(\sigma,\tau)\), permute the sources and targets of all arcs in each face. A face that is not setwise fixed gives no diagonal chain contribution. For a fixed face \(F\), let \(o_g(F)\) count the orbits of its arcs under \(g\). Its orientation sign is \((-1)^{|F|-o_g(F)}\). The reduced chain sign is \((-1)^{|F|-1}\), also valid for the empty face with its degree −1 contribution. Consequently the reduced Lefschetz number is the sum of \((-1)^{o_g(F)-1}\) over fixed faces; homological concentration in odd degree five gives
\[
\chi(g)=\sum_{F:\,gF=F}(-1)^{o_g(F)}.
\]
In particular the empty face contributes \(+1\) in this last sum. Evaluating by the outgoing-neighbor enumeration for all \(3!\,4!=144\) elements gives the character table above; the trace is constant within each of the 15 pairs of conjugacy classes. For example, at the identity the signed sum is \(1-24+234-1192+3357-4968+3024=432\).

For partitions \(\lambda\vdash 3\) and \(\mu\vdash 4\), take the inner product of this table with the product of the two Specht characters. Explicitly, sum \(\chi(\alpha,\beta)\chi^\lambda(\alpha)\chi^\mu(\beta)/(z_\alpha z_\beta)\) over class types \(\alpha,\beta\), where \(z_\gamma=\prod_i i^{m_i}m_i!\) for type \(\gamma\) with \(m_i\) parts of length \(i\). This gives the displayed matrix. The irreducibles of each symmetric group are defined and absolutely irreducible over \(\mathbb Q\), so it gives the rational decomposition as stated.

## Reproducibility

`verify_character.py` enumerates the rooted forests, checks the complete face counts, computes the signed reduced Lefschetz traces for every element, and performs the exact weighted character inner products. The additional `verify_morse.py` independently certifies the previously known homological concentration (and the ordinary wedge type): its acyclic matching leaves one vertex, two four-cells and 434 five-cells. Its integral Morse boundary has a determinant −1 two-column minor, giving two unit cancellations. The latter is a check of the baseline used here, not a second originality claim.

## Relationship to prior work and limitations

The earlier exact \(K_{3,4}\) record [1] proves the same ordinary wedge type but does not give the bipartition-symmetry character. Scoville–Zaremsky [2, Example 4.6] establish connectivity bounds for complete bipartite examples; Chari–Joswig [3, Proposition 3.1] give the graph Morse-complex interpretation by rooted forests. Neither the ordinary homotopy type nor that rooted-forest interpretation alone evaluates the signed fixed-forest sums and gives the irreducible multiplicities for this action. The complete-source or essentially undirected tree criteria in Jojić [4] do not cover the bidirected \(K_{3,4}\); ordinary connectivity or shellability would not by itself determine the character. This result treats only the rational homology representation for this graph, without an integral module classification or a conclusion for arbitrary bipartition sizes.

## References

1. *The Morse complex of \(K_{3,4}\) is a wedge of 432 five-spheres*, Resultary record 48c1007aa5a6 (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-morse-complex-of-k-3-4-is-a-wedge-of-432-five-spheres--48c1007aa5a6.
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, https://arxiv.org/abs/2004.10481.
3. M. K. Chari and M. Joswig, *Discrete Morse complexes*, https://arxiv.org/abs/math/0011234.
4. D. Jojić, *Shellability of complexes of directed trees*, https://arxiv.org/abs/1109.4475.
