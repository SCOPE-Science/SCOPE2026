# Edge-open packings in prism graphs: a six-periodic rigidity theorem

## Finding
For every integer \(n\geq3\), let \(Y_n=C_n\square K_2\), with \(C_3\) the triangle. Its edge-open-packing number is
\[
\rho_e^o(Y_n)=\begin{cases}n,&6\mid n,\\ n-1,&6\nmid n.\end{cases}
\]
When \(6\mid n\), there are **exactly six** maximum edge-open-packing subsets of the labeled graph. They form one orbit under graph automorphisms. Each consists of one of three possible cyclic phases of spokes (one spoke in each three consecutive columns), with two successive horizontal edges in each intervening three-column block; these horizontal pairs alternate between the two layers from block to block.

## Assumptions and scope
All graphs are finite and simple. Two distinct edges \(e,f\) *conflict* if there is a third edge \(g\notin\{e,f\}\) joining an endpoint of \(e\) to an endpoint of \(f\). An *edge-open packing* is a subset of edges with no conflicting pair; \(\rho_e^o\) denotes its maximum size.

Write the vertices of \(Y_n\) as \(u_i,v_i\), where indices range over \(\mathbb Z/n\mathbb Z\). Its three edge types are \(T_i=u_iu_{i+1}\), \(B_i=v_iv_{i+1}\) and \(S_i=u_iv_i\). An assertion about phases modulo six is applied only to the integer representatives \(0\leq i<n\). The theorem concerns the maximum cardinality of **one** edge-open packing, not the minimum number of color classes in an injective edge coloring.

## Proof
**1. A local conflict table.** Inspection of the possible third edges in the prism gives the following exact list of conflicts between distinct edges (congruences modulo \(n\)):

* Two top edges \(T_i,T_j\), or two bottom edges \(B_i,B_j\), conflict precisely when \(j-i\equiv\pm2\).
* Two spokes \(S_i,S_j\) conflict precisely when \(j-i\equiv\pm1\).
* \(T_i,B_j\) conflict precisely when \(j-i\equiv-1,0,1\).
* \(T_i,S_j\) and \(B_i,S_j\) conflict precisely when \(j-i\equiv-1,2\).

These statements remain valid at \(n=3\), where distinct residues can coincide. They follow directly by listing neighbors of each endpoint: for example \(T_i\) and \(S_j\) can be bridged by a distinct top edge only when \(j=i-1\) or \(j=i+2\). The other cases follow identically by symmetry or by considering the available vertical bridges.

**2. Two partitions into conflict triples.** For every \(i\), each of
\[
\{T_i,B_i,S_{i+2}\},\qquad \{T_i,B_i,S_{i-1}\}
\]
is a triple of mutually conflicting edges. Each family partitions the \(3n\) edges into \(n\) disjoint triples. Thus any edge-open packing \(P\) meets each triple in at most one edge, proving \(|P|\leq n\).

Suppose equality holds. Let \(t_i,b_i,s_i\in\{0,1\}\) indicate membership in \(P\). Every conflict triple contains exactly one chosen edge, so
\[
t_i+b_i+s_{i+2}=1=t_i+b_i+s_{i-1}.
\]
Consequently \(s_{i+3}=s_i\) for all indices. Adjacent spokes conflict. Therefore, if \(3\nmid n\), the only possible spoke pattern is all zero: periodicity with steps three makes the pattern constant, and the constant one pattern is prohibited.

The all-zero pattern is impossible for **any** \(n\): it would require \(t_i+b_i=1\) at every index. Since \(T_i\) conflicts with \(B_{i+1}\), choosing \(T_i\) forces \(T_{i+1}\), and cyclic repetition forces all top edges; choosing no top edge forces all bottom edges. Either full horizontal layer contains two conflicting edges. Thus equality requires \(3\mid n\), and precisely one residue class modulo three consists of chosen spokes.

Fix that residue class. Between consecutive chosen-spoke indices lie two consecutive positions \(i,i+1\) whose triples each require one horizontal edge. Because \(T_i\) conflicts with \(B_{i+1}\) and \(B_i\) with \(T_{i+1}\), the two horizontal edges must occupy the same layer. The second horizontal edge of one such pair and the first horizontal edge of the next pair have indices differing by two; they cannot be in the same layer. Hence the layers of consecutive pairs must alternate cyclically. This is possible precisely when the number \(n/3\) of pairs is even, equivalently \(6\mid n\). In that case the three spoke phases and two choices of the initial layer give exactly six allowable selections, and each is indeed conflict-free by the table above. They are equivalent under cyclic column rotations and interchange of layers. This proves both the equality classification and the upper bound \(\rho_e^o(Y_n)\leq n-1\) when \(6\nmid n\).

**3. Sharp constructions in every residue class.** Define a six-periodic edge template \(P(n,\phi)\). For \(0\leq i<n\), let \(j\equiv i+\phi\pmod6\); include \(T_i\) when \(j\in\{0,1\}\), \(B_i\) when \(j\in\{3,4\}\), and \(S_i\) when \(j\in\{1,4\}\). When \(n\geq4\), make the following choices:

| \(n\bmod6\) | \(\phi\) | Additional deletion | Size |
|:--:|:--:|:--:|:--:|
| 0 | 0 | none | \(n\) |
| 1 | 2 | none | \(n-1\) |
| 2 | 1 | \(T_{n-2}\) | \(n-1\) |
| 3 | 0 | \(T_{n-2}\) | \(n-1\) |
| 4 | 2 | none | \(n-1\) |
| 5 | 2 | none | \(n-1\) |

Here the deletion is made only after selecting the template; it always removes a selected edge. For the exceptional smallest cycle \(n=3\), choose \(P=\{T_1,S_1\}\), which has size two.

For completeness, the finite seam check verifying this infinite construction is as follows. By the exact conflict table in step 1, a forbidden pair has cyclic index separation at most two; all pairs strictly inside a length-six template block are compatible. The only pairs to check are those crossing the cyclic seam. Their edge-type and index-residue patterns depend solely on \(n\bmod6\), \(\phi\), and the optional deletion. Direct substitution of the six rows above into the four rules in step 1 gives no forbidden seam pair. The short representatives \(n=4,5,6,7,8,9\) also obey the same four rules (including the wraparound coincidences). Appending any complete block of six preserves the interior rules and the seam residue pattern. Hence the construction works for every \(n\geq4\), not merely for tested examples. It gives \(n\) edges exactly when \(6\mid n\), and \(n-1\) otherwise. Combined with step 2 this proves the theorem. \(\square\)

## Verification
The accompanying standalone `verify.py` implements the original adjacency graph and independently computes conflict edges. It checks the complete cyclic conflict table for \(5\leq n\leq15\); validates all 178 explicit construction witnesses for \(3\leq n\leq180\); exactly optimizes the corresponding finite conflict graphs for \(3\leq n\leq10\); and exhaustively counts upper-bound equality cases for \(n\in\{3,6,9,12\}\), obtaining \(0,6,0,6\). Run with `python3 verify.py` using the Python standard library. The file `verification_output.txt` contains the actual captured output. Exhaustive checks are finite corroboration; the proof above establishes the unbounded theorem.

## Relationship to prior work
Brešar and Samadi (2024, arXiv:2403.00750v1, Sections 1 and 4.1) provide the general bound \(\rho_e^o(G)\leq |E(G)|/\delta(G)\). On this cubic prism it yields \(\rho_e^o(Y_n)\leq n\) but neither the strict deficit outside multiples of six nor the six-optimum classification. Brešar, Dravec, Hedžet and Samadi (2024, arXiv:2406.04020v2, Section 5, Corollary 5.3 and Proposition 5.9) provide lower bounds for Cartesian products and a three-packing estimate for prisms, not the present exact EOP result. Bhanupriya, Dominic and Sunitha (2023) discuss injective edge-coloring of products and cite known injective edge chromatic-index results for generalized Petersen prisms; partitioning **all** edges into color classes does not determine the maximum size or census of a single class. Chelladurai, Kalimuthu and Soundararajan (2022) introduce edge-open packing and several classical families; the inspected source does not determine these prisms. No assertion of exhaustive historical novelty is made.

## Limitations
The six-fold extremal classification applies only to the cases \(6\mid n\), when the optimum reaches the universal \(n\) upper bound. For the remaining residues this theorem gives an exact numerical optimum and explicit witnesses, but it does **not** enumerate all \(n-1\)-edge packings. All results use the stated third-edge conflict convention. An equivalent treatment in unindexed literature or under injective-edge-coloring terminology is a residual originality risk. The finite computational checks do not serve as an infinite proof.

## References
1. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1 (public 2024-03-01), https://arxiv.org/html/2403.00750v1.
2. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v2 (2024), https://arxiv.org/html/2406.04020v2.
3. C. K. Bhanupriya, C. Dominic and M. S. Sunitha, *Injective edge coloring of product graphs and some complexity results*, Filomat 37 (2023), DOI:10.2298/FIL2312963K.
4. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Oper. Res. 56 (2022), 3765–3776, DOI:10.1051/ro/2022171.
