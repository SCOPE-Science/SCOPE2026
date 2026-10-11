# The ternary Hamming Rips filtration and the \(K_3\times K_3\times K_3\) case

## Finding

Let \(X=\{0,1,2\}^3\), endowed with the Hamming metric \(d_H(x,y)=|\{i\in\{1,2,3\}:x_i\ne y_i\}|\). For every real radius \(r\ge0\), define the **inclusive** Vietoris--Rips complex \(\operatorname{VR}_{\le}(X;r)\) to contain exactly those nonempty vertex subsets whose pairwise Hamming distances are at most \(r\). Then

\[
\operatorname{VR}_{\le}(X;r)\simeq
\begin{cases}
\bigsqcup^{27}\mathrm{pt},&0\le r<1,\\
\bigvee^{28}S^1,&1\le r<2,\\
\bigvee^{46}S^3,&2\le r<3,\\
\mathrm{pt},&r\ge3.
\end{cases}
\]

At \(r=2\) there is an equality of abstract simplicial complexes
\[
\operatorname{VR}_{\le}(X;2)=\operatorname{Ind}(K_3\times K_3\times K_3),
\]
where \(\times\) denotes the categorical (tensor) graph product, with adjacency if and only if all three coordinate values differ. Thus the claimed wedge gives a proof of the \((3,3,3)\) case of Conjecture 26 in Antolín Camarena and Carnero Bravo [3], which **predicted** 46 three-spheres but did not prove this case.

The complete ordinary persistence barcode over any field consists of 26 degree-zero intervals \([0,1)\), one degree-zero interval \([0,\infty)\), 28 degree-one intervals \([1,2)\), and 46 degree-three intervals \([2,3)\); there are no other positive-length intervals. The reduced integral homology in the noncontractible connected ranges is free of the indicated ranks.

## Assumptions and scope

The vertex labels are triples of digits \((a,b,c)\in\{0,1,2\}^3\), ordered lexicographically. Their metric is the usual Hamming distance and the Rips filtration uses the weak inequality \(d_H\le r\), not a strict open threshold. The theorem concerns this exact 27-point metric for all real \(r\ge0\). It does not assert an all-parameter classification of categorical graph products.

## Proof

**Small and large radii.** For \(0\le r<1\) only the 27 singletons occur. At \(1\le r<2\), the Rips graph is the Cartesian Hamming graph \(K_3\square K_3\square K_3\): it is connected with 27 vertices and 81 edges. Any clique of size at least two lies on a line in which exactly one coordinate varies, because two neighbors of a given vertex differing from it in different coordinates are at distance two. Hence there are exactly 27 triangular faces and no higher-dimensional faces. Every edge belongs to a unique triangle. Remove one edge together with its unique triangle for each of the 27 triangles; these are elementary simplicial collapses onto a connected graph with 27 vertices and 54 edges. Its cycle rank is \(54-27+1=28\), establishing \(\bigvee^{28} S^1\). For \(r\ge3\), every vertex pair is within the radius, so the complex is the full 26-simplex.

**The radius-two graph duality.** The maximum pairwise Hamming distance in \(X\) is three. Thus a subset spans a radius-two simplex precisely when it contains no pair whose three coordinates are all distinct. The forbidden-pair graph is exactly \(K_3\times K_3\times K_3\), proving the displayed identity with its independence complex.

**Complete finite acyclic matching.** Write the 27 lexicographically ordered vertices as \(v_0,\ldots,v_{26}\). Enumerate all nonempty independent subsets of the forbidden-pair graph, each as a 27-bit mask. The resulting face counts in cardinalities zero through nine (including the empty face only for enumeration) are
\[
(1,27,243,945,1728,1620,945,351,81,9).
\]
In particular there are exactly 5949 nonempty faces. Start with all nonempty faces unmatched. For each \(i=0,\ldots,26\), match every still-unmatched face \(\sigma\) not containing \(v_i\) to \(\sigma\cup\{v_i\}\) if that upper face also remains unmatched, and remove both from the unmatched set before advancing to the next index. Within a stage, every lower face has \(v_i\) absent and every upper face has it present, so the pairs are disjoint; all are valid covering relations in the face poset.

The exhaustive reconstruction in `ternary_hamming_verifier.py` yields exactly 2951 pairs. The unmatched nonempty faces consist of **one vertex and 46 three-dimensional simplices**, and none in any other dimension. A second exhaustive check builds every codimension-one covering relation between nonempty faces, orienting matched relations from lower to upper and all other relations from upper to lower. This directed Hasse graph has 5949 vertices and 27189 directed edges. A topological sort processes all 5949 vertices, a complete acyclicity certificate. Therefore the matching is an acyclic discrete-Morse matching, not merely a numerical homology computation. The discrete-Morse CW theorem gives a homotopy-equivalent CW complex with one zero-cell and 46 three-cells and no positive-dimensional lower cells. Each three-cell attaches to a single point, yielding \(\bigvee^{46}S^3\).

**Persistence.** At successive integer radii, the only nonzero positive-dimensional reduced homology groups are degree one at radius one, and degree three at radius two; all vanish at radius three. Therefore no positive-dimensional class can survive across more than one threshold. Connectivity gives the degree-zero intervals. Wedge-of-spheres homotopy types establish the assertion over every field and over the integers.

## Verification

The self-contained Python 3 verifier `ternary_hamming_verifier.py` recomputes the Hamming distances, exact face vector, entire staged matching, all 27189 face incidences, a complete topological ordering of the oriented Hasse graph, and mod-two simplicial boundary ranks independently of the Morse critical-cell count. Its successful output includes `VERIFY_OK`, the 2951 pairs, the 46 critical three-cells, and mod-two Betti rank 46. For radius one it independently checks all 81 edges and 27 triangles, and confirms each edge is in exactly one triangle. There are no stored precomputed face or matching certificates; all are reconstructed from the 27 labeled points. The finite exhaustive check is decisive for this finite complex, but provides no all-size theorem.

## Relationship to prior work

Adamaszek and Adams [1] classify Rips complexes of subsets of a circle, not the ternary Hamming cube. Goyal, Shukla, and Singh [2, Proposition 3.1] give the staged matching machinery and [2, Proposition 3.2] classify two-factor categorical products, but do not prove this three-factor instance. Antolín Camarena and Carnero Bravo [3, Proposition 25] prove the three-factor case in which **one factor is** \(K_2\). Their Conjecture 26 predicts the three-factor homotopy formula with multiplicity
\[
f(n,m,l)=\frac{(n-1)(m-1)(l-1)(nml-4)}{4},
\]
which equals 46 at \((n,m,l)=(3,3,3)\). The conjecture's prediction is acknowledged and not described as a new numerical formula; the present contribution is an exact finite homotopy proof for the first fully symmetric instance with no \(K_2\) factor, plus the whole associated Rips filtration. The hypercube work [4] concerns the binary alphabet, not the ternary metric.

## Limitations

Only \(K_3\times K_3\times K_3\) and the 27-point Hamming filtration are established. The matching does not settle Conjecture 26 for arbitrary triples. The complete computation is reproducible, but originality could be affected by an independently known equivalent proof outside the inspected sources. It is a finite theorem and not evidence of asymptotic behavior. No independent external audit is claimed.

## References

[1] M. Adamaszek and H. Adams, *The Vietoris--Rips complexes of a circle*, arXiv:1503.03669, originally submitted 2015-03-12, and Pacific Journal of Mathematics 290 (2017), 1--40. https://arxiv.org/abs/1503.03669 ; https://msp.org/pjm/2017/290-1/pjm-v290-n1-p01-s.pdf .

[2] S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926; see Proposition 3.1, Proposition 3.2 and the discussion following. https://arxiv.org/pdf/1905.06926 .

[3] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, original submission 2023-07-23; see Section 4, Proposition 25 and Conjecture 26. https://arxiv.org/pdf/2307.12401 .

[4] M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040. https://arxiv.org/pdf/2103.01040 .
