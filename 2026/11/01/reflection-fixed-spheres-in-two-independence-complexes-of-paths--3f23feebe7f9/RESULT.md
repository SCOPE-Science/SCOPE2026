# Reflection-fixed spheres in two-independence complexes of paths

## Finding

For every integer \(n\ge1\), let \(P_n\) denote the path on \(\{1,\ldots,n\}\) and let \(K_n=\operatorname{Ind}_2(P_n)\) be its two-independence complex: a vertex subset is a face precisely when it contains no three consecutive indices. Let the involution \(\rho\) reverse the path, \(\rho(i)=n+1-i\). Put \(m=\lceil n/2\rceil\).

Define the **boundary-obstructed path complex** \(E_m\) on \(\{1,\ldots,m\}\) by forbidding the pair \(\{1,2\}\) and all consecutive triples \(\{j,j+1,j+2\}\), with only forbidden subsets lying inside \([m]\) considered. There is a canonical piecewise-linear homeomorphism

\[
|K_n|^{\langle\rho\rangle}\cong_{\mathrm{PL}}|E_m|.
\]

The complete geometric fixed-point homotopy classification is

\[
|K_n|^{\langle\rho\rangle}\simeq
\begin{cases}
\{\mathrm{pt}\},&m\text{ odd},\\
S^{k-1},&m=2k\text{ even}.
\end{cases}
\]

In terms of the original path size, the fixed space is \(S^{k-1}\) at \(n=4k-1\) and \(n=4k\), for every \(k\ge1\); it is contractible at \(n=4k+1\) and \(n=4k+2\), for every \(k\ge0\). In particular, fixed sphere dimensions are unbounded, even though each action is a simple reflection.

## Assumptions and scope

All graphs are finite and simple. The two-independence condition refers to connected components of the **induced** graph on a selected vertex set, each with at most two vertices. In a path, this is equivalent to the absence of three consecutive selected vertices. A fixed point means an actual fixed point of the induced PL involution on the geometric realization, not a fixed vertex or an invariant homology class. For \(n=1,2\), the fixed space is a point. No statement about higher independence parameters, other group actions, or equivariant homotopy equivalence is asserted.

## Proof

**1. Geometry of orbit barycenters.** Let a finite simplicial complex \(L\) have an involution permuting its vertices. Form an auxiliary simplicial complex whose vertices are involution-orbits \(O\) that individually form faces of \(L\), and whose simplices are orbit collections whose unions form faces of \(L\). Send the vertex representing \(O\) to the average of the standard barycentric vertices in \(O\). On each simplex this extends affinely; its image consists precisely of barycentric points with weights constant on each orbit. Every fixed point has such weights and a unique inverse, so this yields a PL homeomorphism onto \(|L|^{\langle\rho\rangle}\).

**2. The exact reflected orbit complex.** Number the \(m\) vertex orbits of path reversal from the center outwards by \(1,\ldots,m\). Each face of the orbit complex corresponds to a palindromic binary word. Away from the center, three consecutively occupied path vertices occur exactly when three consecutive outward orbits are chosen. At the center, occupancy of the first two outward orbits creates three consecutively occupied vertices: for odd path size, the center vertex and its two neighbors; for even path size, the central two vertices and a neighbor. Conversely, if the first two orbits are not both occupied and there are no three consecutive occupied outward orbits, no run of three can occur anywhere. The orbit complex is therefore *exactly* \(E_m\), including at \(m=1\) and \(m=2\). This proves the PL identification, not merely an equality of Betti numbers.

**3. Uniform explicit discrete-Morse matching.** Work with the augmented face poset of \(E_m\), including the empty face. For \(m=1\) match the empty face with \(\{1\}\). For \(m=2\) make the same match, leaving \(\{2\}\) unmatched.

Inductively, for \(m\ge3\), match every face \(F\) with \(1,2\notin F\) to \(F\cup\{1\}\). The remaining faces are exactly the sets \(\{2\}\cup T\), where \(T\) is a face of a copy of \(E_{m-2}\) on vertices \(3,\ldots,m\): the selected vertex \(2\) forbids the simultaneous selection of \(3\) and \(4\), and the subsequent restrictions are the usual consecutive triples. Transfer the matching already constructed on \(E_{m-2}\) to these faces.

The matching is acyclic. In the oriented Hasse diagram, paired arrows point upward and other cover arrows point downward. All matching edges preserve the membership of vertex \(2\), and every cover relation changing its membership is directed from a face containing \(2\) to one omitting \(2\). Hence a directed cycle cannot cross between these two families. Among faces omitting \(2\), toggling vertex \(1\) is a single-element acyclic matching. Among faces containing \(2\), the translated matching is acyclic by induction.

Inductively, for odd \(m\), all augmented faces are paired. For even \(m=2k\), exactly one augmented face remains unmatched, namely \(\{2,4,\ldots,2k\}\), of dimension \(k-1\). The empty face was always matched with \(\{1\}\). Removing only that pair from the augmented matching gives an ordinary acyclic matching with one critical vertex \(\{1\}\) for odd \(m\), and with precisely \(\{1\}\) and the above critical \((k-1)\)-simplex for even \(m\). By discrete Morse theory, the first complex is contractible and the second is homotopy equivalent to \(S^{k-1}\). At \(k=1\) there are two critical vertices and the complex is \(S^0\). For \(k\ge2\) the Morse CW complex has one zero-cell and one \((k-1)\)-cell, necessarily a sphere. This completes the proof for all \(n\).

## Verification

The proof is an infinite argument; the computations below check finite instances independently and are not being substituted for it. Run the two standalone scripts from the containing directory with Python 3:

```
python verification/check_reflect_ind2.py
python verification/check_reflect_ind2_morse.py
```

The first independently enumerates the geometric invariant orbit faces and the forbidden-subset model at every \(1\le n\le25\) (8,900 admissible orbit subsets in total), and compares their mod-two reduced Betti numbers with the theorem for \(1\le n\le21\). The second checks the complete recursively defined augmented matching, its critical sets, and directed Hasse acyclicity for \(1\le m\le14\). All stated checks passed when executed from the packaged source. The homotopy and integral conclusions rely on the mathematical matching proof rather than finite-field computations.

## Relationship to prior work

Sawant (2026, arXiv:2605.25150v1) proves vertex decomposability of higher-independence complexes of all trees, which motivates asking for their more refined symmetry-fixed topology. Deshpande and Singh (2020/2021, arXiv:2001.05448v2, Theorem 4.2 and Proposition 4.3) provide the known *nonequivariant* periodic sphere/point homotopy classification and perfect matchings for path higher-independence complexes. Ghosh and Selvaraja (2025, arXiv:2505.06614v3) study shellability and related combinatorial criteria. These results do not state the actual geometric fixed-point PL identification with \(E_m\), the boundary-obstructed matching, or its fixed-locus sphere dimensions. Nonequivariant homotopy data alone do not determine the fixed-point topology of an involution.

## Limitations

Only path reversal and the two-independence parameter are treated. The PL assertion is a homeomorphism to the explicitly defined finite complex \(E_m\); the subsequent sphere/point classification is a *homotopy equivalence*, not a claim that every fixed sphere is PL-homeomorphic to a round or triangulated sphere. Literature discovery cannot exclude all unpublished or unindexed equivalent results. No independent mathematical audit is implied.

## References

1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, first public 2026-05-24, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v2, first public 2020-01-15, https://arxiv.org/abs/2001.05448.
3. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614v3, first public 2025-05-10, https://arxiv.org/abs/2505.06614.
