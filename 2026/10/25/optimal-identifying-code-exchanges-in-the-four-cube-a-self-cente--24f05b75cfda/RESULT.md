# Optimal identifying-code exchanges in the four-cube: a self-centered 960-state graph

## Finding

Let \(Q_4\) be the graph on \(\mathbb F_2^4\) with edges between vectors of Hamming distance one. A radius-one identifying code \(C\subseteq V(Q_4)\) is a set for which the sixteen sets \(N[v]\cap C\), with \(v\in V(Q_4)\), are nonempty and pairwise distinct. Let \(\mathcal R\) have as vertices all identifying codes of minimum cardinality, with \(C\) and \(D\) adjacent exactly when \(|C\setminus D|=|D\setminus C|=1\); the exchanged codewords need not be adjacent in \(Q_4\).

**Theorem.** The minimum cardinality is \(7\), and \(\mathcal R\) has exactly \(960\) vertices and \(4320\) edges. It is connected and \(9\)-regular; each vertex belongs to exactly \(12\) triangles. For **every** \(C\in V(\mathcal R)\), the numbers of optimal codes at exchange distances \(0,1,\ldots,7\) from \(C\) are

\[
(1,9,35,132,300,338,130,15).
\]

Thus \(\operatorname{rad}(\mathcal R)=\operatorname{diam}(\mathcal R)=7\). Under the natural action of \(\operatorname{Aut}(Q_4)\), the \(960\) codes form exactly three orbits, of respective sizes \(384,384,192\), despite their common distance-shell profile. There are \(3840\) triangles in total.

## Assumptions and scope

A binary vector \(x\in\mathbb F_2^4\) is encoded by \(\iota(x)=\sum_{j=0}^3 2^j x_j\in\{0,\ldots,15\}\). The closed Hamming ball \(N[v]\) consists of \(v\) and its four distance-one neighbors. A code is *identifying* only when it both covers every vertex and distinguishes every pair of vertices. All codewords and all reconfiguration states are labeled; the three symmetry orbits are reported only as a further classification, not quotiented away when computing graph statistics. Exchanges replace precisely one selected vertex by one unselected vertex, preserving cardinality seven and the full identifying-code property. No assertion is made for other cube dimensions or larger codes.

## Proof

**Exact finite criterion.** For \(0\le c<2^{16}\), let \(S(c)\subseteq\{0,\ldots,15\}\) be its set of one-bit positions. Define the sixteen fixed closed-ball bit masks \(b_v=\sum_{u:\,d_H(u,v)\le1}2^u\). Then the code represented by \(c\) is identifying if and only if the sixteen integers \(c\mathbin{\&}b_v\) are all nonzero and pairwise distinct. This is immediate from the definitions: bitwise intersection encodes the set \(S(c)\cap N[v]\), and equal masks encode equal sets. This criterion involves only sixteen explicitly determined five-element neighborhoods and is decidable for every one of the \(2^{16}=65536\) subsets without an external oracle.

**Minimum and configuration count.** The program `scripts/check_mask.py` checks this criterion for every \(c\in\{0,\ldots,65535\}\), with the vertex labels and masks defined above. It confirms that no identifying code contains fewer than seven vertices and that exactly \(960\) seven-vertex masks pass. Independently, `scripts/check_sets.py` checks all \(\binom{16}{6}=8008\) six-element sets directly as sets of four-bit tuples and all \(\binom{16}{7}=11440\) seven-element sets. It finds no identifying set of size six and exactly \(960\) identifying sets of size seven. Both programs also find exactly \(192\) six-vertex sets with *pairwise distinct* signatures if the nonemptiness requirement is dropped: such sets necessarily leave precisely one cube vertex uncovered. This separately guards the definition and the minimality calculation. Since adjoining codewords preserves coverage and distinguishability, the absence of a six-element code excludes every smaller cardinality as well. These finite exhaustive checks establish the minimum and the state count, not just sampled evidence.

**Edges, degrees, and triangles.** For every accepted bit mask \(c\) and distinct positions \(a\in S(c)\), \(b\notin S(c)\), its one-exchange candidate is exactly \(c\oplus2^a\oplus2^b\). Membership in the sorted list of \(960\) minima decides adjacency. Enumerating all seven selected and nine unselected positions at every state gives degree nine everywhere and \(\sum_C\deg(C)/2=4320\) unordered edges. Counting adjacent pairs among each vertex's nine exchange-neighbors gives exactly twelve incident triangles at every state and hence \(960\cdot12/3=3840\) total triangles. In the independent set-based implementation, two distinct seven-element codes are adjacent if and only if they occur in a common six-element-subset bucket. That construction independently gives the same degree, edge, and triangle counts.

**Three symmetry orbits and complete distances.** The \(384=2^4\cdot4!\) transformations \(x\mapsto \sigma(x)\oplus t\), with \(\sigma\in S_4\) and \(t\in\mathbb F_2^4\), are all automorphisms of the cube. They preserve closed balls, identifying codes, and the one-exchange relation. Every automorphism of the cube has this form: after fixing the image of the zero vertex and the permutation of its four neighbors, the images of all remaining vertices are forced recursively by the cube adjacency relations (equivalently, by preserving Hamming distances from these five vertices). The exact bit-mask enumeration, applied to all \(384\) transformations of each successive unused code, yields the following complete orbits (sets of integer vertex labels displayed as representatives):

| Representative code | Orbit size | Distance shells from representative |
| --- | ---: | --- |
| \(\{0,3,4,6,7,8,9\}\) | 384 | \((1,9,35,132,300,338,130,15)\) |
| \(\{0,2,4,5,7,9,10\}\) | 384 | \((1,9,35,132,300,338,130,15)\) |
| \(\{2,3,5,7,9,10,12\}\) | 192 | \((1,9,35,132,300,338,130,15)\) |

These disjoint orbit sizes sum to \(960\), exhausting all minimum codes. A complete breadth-first search from each representative visits every state and produces the displayed profile, ending at distance seven. Because each transformation is an exchange-graph automorphism, every state in that representative's orbit has the same distance profile. Thus *all* states have the stated profile, proving connectedness, radius, and diameter. Separately, `scripts/check_sets.py` performs breadth-first search from **each** of the \(960\) vertices, confirming this profile without relying on the orbit reduction. This completes the finite proof. \(\square\)

## Verification

Run both standalone checkers from the package root using Python 3.10 or later:

```sh
python3 scripts/check_mask.py
python3 scripts/check_sets.py
```

Their expected complete outputs are embedded verbatim as `outputs/check_mask.json` and `outputs/check_sets.json`. The first exhausts all \(65536\) candidate subsets and checks symmetry orbits and one-exchange adjacency by bit operations. The second uses a distinct tuple/set representation, enumerates six- and seven-element candidates, constructs adjacency through shared six-element cores, and computes \(960\) separate breadth-first searches. No randomness, network, external packages, precomputed graph files, solver assertions, or unseen certificates are needed.

## Relationship to prior work

Karpovsky, Chakrabarty, and Levitin introduced the identifying-code framework and studied binary cubes, including size bounds and constructions; their binary-cube table gives the number six at dimension four. Under the explicitly stipulated **nonempty** closed-ball-signature definition, exhaustive checking instead establishes the later conventional value seven. In fact, six vertices can distinguish all sixteen signatures only when one signature is empty (there are exactly 192 such six-subsets). This observation establishes the relevant mathematical normalization boundary but does not establish why the early numerical table differs. The early work does not describe the optimum-state exchange graph. Blass, Honkala, and Litsyn investigated identifying-code bounds and constructions in Hamming spaces. Charon, Cohen, Hudry, and Lobstein develop stronger constructions and local replacement heuristics; a heuristic replacing one codeword to find a code is not a theorem classifying all optimal code exchanges. The modern small-cube compilation by Herva, Laihonen, and Lehtilä records \(M(4)=7\) as known, while primarily studying **local** identifying codes, a different optimization problem. The known value seven is therefore background, not claimed as novel. The contribution here is the complete graph of optimal single-codeword exchanges, its common distance-shell profile, uniform local triangle count, and its three orbits under natural cube symmetry.

## Limitations

This is an exact result for the labeled four-cube under nonempty signatures; the weaker pairwise-distinct-only convention has different extrema. The early literature gives an inconsistent small-case number relative to this explicit convention; the proved result does not depend on that numerical entry. The proof is exhaustive finite enumeration with two transparent checkers, not an unverified inference from low-dimensional samples, and it does not assert analogous behavior in higher-dimensional cubes. The full publisher article by Charon and collaborators was only partly available in accessible text; potential unindexed equivalent statements about minimum-code exchanges remain a literature-priority risk. Natural cube orbits do **not** by themselves determine the full automorphism group of the exchange graph, and no such classification is asserted. Independent external validation is not represented by the included computational cross-checks.

## References

1. M. G. Karpovsky, K. Chakrabarty, and L. B. Levitin, “On a New Class of Codes for Identifying Vertices in Graphs,” *IEEE Transactions on Information Theory* **44** (1998), 599–611. DOI: 10.1109/18.661507. Author-accessible PDF: https://sites.bu.edu/mark/files/2018/02/132.pdf.
2. U. Blass, I. Honkala, and S. Litsyn, “Bounds on identifying codes,” *Discrete Mathematics* **241** (2001), 119–128. DOI: 10.1016/S0012-365X(01)00113-3.
3. I. Charon, G. Cohen, O. Hudry, and A. Lobstein, “New identifying codes in the binary Hamming space,” *European Journal of Combinatorics* **31** (2010), 491–501. DOI: 10.1016/j.ejc.2009.03.032.
4. P. Herva, T. Laihonen, and T. Lehtilä, “Optimal Local Identifying and Local Locating-dominating Codes,” *Fundamenta Informaticae* **191** (2024), 351–378. arXiv:2302.13351; https://arxiv.org/pdf/2302.13351.
