# Rigidity of efficient edge domination in \(\mathrm{GP}(n,2)\)

## Finding

For every integer \(n\ge5\), let \(G_n=\mathrm{GP}(n,2)\) be the generalized Petersen graph with outer vertices \(u_i\), inner vertices \(v_i\) and edges
\[
 O_i=u_iu_{i+1},\qquad S_i=u_iv_i,\qquad I_i=v_iv_{i+2},\qquad i\in\mathbb Z/n\mathbb Z.
\]
A **dominating induced matching** (DIM) is a matching whose selected edges are pairwise nonadjacent even through an intervening edge, and such that every graph edge has a common endpoint with a selected edge or is itself selected. The following completely classifies these matchings:

**Theorem.** A DIM of \(G_n\) exists if and only if \(5\mid n\). If \(5\mid n\), there are **exactly five** DIMs, and they are precisely
\[
 M_r=\{I_i:i\equiv r\pmod5\}\ \cup\
     \{S_i:i\equiv r+1\pmod5\}\ \cup\
     \{O_i:i\equiv r+3\pmod5\},\qquad r=0,1,2,3,4.
\]
Each contains \(3n/5\) edges, and the five DIMs partition \(E(G_n)\).

A **strong edge coloring** is a coloring in which each color class is an induced matching. The five DIMs above form a strong five-edge coloring. In fact, **every strong five-edge coloring of \(G_n\) is obtained from this partition by permuting the five colors**. Hence \(\chi_s'(G_n)=5\) precisely when \(5\mid n\), and for these orders there is one unlabelled five-color partition and exactly \(5!=120\) proper strong colorings with the prescribed distinct color names \(1,\ldots,5\).

The existence condition and the five-color *index* are not claimed as new. The retained assertion is the exact enumeration/classification of all DIMs and the rigidity of **all** optimal five-edge colorings throughout the infinite family.

## Assumptions and scope

Indices are taken modulo \(n\); the graph is simple and cubic because \(n\ge5\). The five color names are regarded as labelled when counting \(120\) edge colorings. A matching is induced when there is no edge joining endpoints of distinct matching edges. A DIM is equivalently an exact cover of the edge set by closed edge neighborhoods of the selected edges. The theorem makes no assertions about the exact strong chromatic index for \(5\nmid n\), beyond it being at least six.

## Proof

**1. A vertex-bicoloring formulation.** Given a DIM, call a vertex black if it belongs to a selected edge and white otherwise. A white vertex cannot be adjacent to another white vertex: their connecting edge would be undominated. Every black vertex has exactly one black neighbor, its partner in the selected edge, because any other black neighbor would join endpoints of distinct selected edges. Conversely, any two-coloring in which white vertices have zero white neighbors and black vertices have exactly one black neighbor defines a DIM: the black–black edges form an induced matching, and every edge has a black endpoint incident to exactly one member of that matching.

Let \(x_i\in\{0,1\}\) indicate that \(u_i\) is white and \(y_i\in\{0,1\}\) that \(v_i\) is white. Every white vertex has three black neighbors and every black vertex two white neighbors. Consequently, the bicoloring condition is **equivalent** to the following pair of equations at every index:
\[
 x_{i-1}+2x_i+x_{i+1}+y_i=2,\qquad
 y_{i-2}+2y_i+y_{i+2}+x_i=2.\tag{1}
\]
Indeed, when the central indicator is one, its neighbor indicators sum to zero; when it is zero, they sum to two.

**2. Divisibility.** Put \(X=\sum_i x_i\) and \(Y=\sum_i y_i\). Summing the two cyclic equations (1) gives
\[
 4X+Y=2n,\qquad X+4Y=2n,
\]
so \(X=Y=2n/5\). Their integrality forces \(5\mid n\), establishing necessity.

**3. Only period-five bicolorings can occur.** Eliminate \(y_i=2-x_{i-1}-2x_i-x_{i+1}\) from the second equation in (1). Then
\[
 x_{i-3}+2x_{i-2}+3x_{i-1}+3x_i+3x_{i+1}+2x_{i+2}+x_{i+3}=6.\tag{2}
\]
Let \(T\) denote the shift \((Tx)_i=x_{i+1}\), and set \(z_i=x_i-2/5\). Equation (2), after multiplication by \(T^3\), becomes
\[
 (T^2+T+1)(T^4+T^3+T^2+T+1)z=0.\tag{3}
\]
The two factors \(\Phi_3\) and \(\Phi_5\) are coprime over \(\mathbb Q[T]\). Bezout's polynomial identity therefore splits \(z\) uniquely into a sequence \(p\) annihilated by \(\Phi_3(T)\) and a sequence \(q\) annihilated by \(\Phi_5(T)\). In particular,
\[
 x_i=2/5+p_{i\bmod3}+q_{i\bmod5},\qquad
 \sum_{a=0}^2p_a=\sum_{b=0}^4q_b=0.\tag{4}
\]
This identity holds on all integer indices by cyclic extension, regardless of whether three divides \(n\).

We use the following elementary **binary rectangle lemma**. If a function on the Cartesian product of two nonempty finite sets has the form \(c+p_a+q_b\) and takes only the values zero and one, then it depends on at most one of \(a\) and \(b\). To prove this, if two row offsets differ, then the corresponding two rows have the same nonzero difference at every column. That difference must be \(+1\) or \(-1\), so both rows are constant, forcing all column offsets to coincide. If no two row offsets differ, the function depends only on the column coordinate.

As \(\gcd(3,5)=1\), all fifteen combinations of residues \((i\bmod3,i\bmod5)\) occur in (4). Applying the lemma, \(x\) is either three-periodic or five-periodic. A three-periodic binary word has density among \(0,1/3,2/3,1\), inconsistent with its density \(X/n=2/5\). Therefore \(x\) is five-periodic, with exactly two white outer vertices in each five positions.

White vertices are independent; in particular adjacent outer positions cannot both be white. The only two-subsets of a five-cycle containing no consecutive positions are the five rotations of \(\{0,2\}\). After rotating the index, we may take
\[
 (x_0,x_1,x_2,x_3,x_4)=(1,0,1,0,0).
\]
The first equation of (1) then **uniquely** determines
\[
 (y_0,y_1,y_2,y_3,y_4)=(0,0,0,1,1).
\]
Direct substitution verifies both equations of (1), including every index wraparound. By the correspondence in Step 1, the black–black edges are exactly \(I_i\) at residue zero, \(S_i\) at residue one and \(O_i\) at residue three. Rotating gives precisely \(M_0,\ldots,M_4\), with no other DIMs. The five sets have disjoint edge types and residues covering every edge exactly once.

**4. Rigidity of strong coloring.** In any cubic graph, the five edges consisting of a fixed edge together with the other four edges incident with either endpoint must receive pairwise distinct colors in a strong edge coloring. If exactly five colors are used, then **each** such closed edge neighborhood contains each color exactly once. It follows that every color class is a DIM: its edges form an induced matching, and every edge's closed edge neighborhood contains one edge of that color. For \(G_n\), the classification above forces the five color classes to be the five \(M_r\), each used once. Conversely their partition is a strong five-edge coloring. Permuting the names gives all \(120\) labelled colorings. If \(5\nmid n\), a strong five-edge coloring would produce a DIM, contradicting Step 2.

## Verification

Two standalone, standard-library Python 3 programs accompany this result. `verify_exact_cover.py` constructs the closed edge neighborhoods directly from the graph definition and exhaustively enumerates their disjoint exact covers for **every** order \(5\le n\le40\). It obtains five DIMs exactly when \(5\mid n\), verifies their formulas, and confirms that they partition the edges.

Independently, `verify_transfer.py` builds all length-four words over the eight possible edge-type selection triples. A legal transition appends a triple when all three edge-neighborhood exact-cover equations at the middle index hold. A directed closed walk of length \(n\ge5\) corresponds to a DIM. The transition digraph has \(346\) active states and \(576\) arcs. An exhaustive strongly connected component computation finds exactly one cyclic component: a directed five-cycle with no alternative internal arcs. This proves that **every** closed walk has length divisible by five and is a repetition of one of the five shifts, providing a separate all-orders finite-state certificate for the classification. The analytic proof above does not rely on either program.

From the directory containing the four verification artifacts, run `python3 verify_exact_cover.py` and `python3 verify_transfer.py`. Their stdout must match `exact_cover_output.json` and `transfer_output.json`, respectively, byte for byte (add the final newline after JSON output). No third-party packages are required.

## Relationship to prior work

The basic DIM definitions and algorithms appear in Lin, Mizrahi and Szwarcfiter (2013). Alaeiyan and Karami (2016, Section 3.5, Theorem 3.9) explicitly **establish existence** of a perfect two-coloring of \(\mathrm{GP}(n,2)\) with quotient matrix \(\left(\begin{smallmatrix}0&3\\2&1\end{smallmatrix}\right)\) precisely when five divides \(n\). This is equivalent to DIM existence; their theorem supplies one periodic construction and does **not** classify all solutions or count them. Yang and Wu (2018) study the strong chromatic index for the same generalized Petersen subfamily; the index and existence are not claimed as new here. Lužar, Mačajová, Škoviera and Soták (2021) establish the relation between strong five-edge coloring and Petersen covering graphs, including uniqueness up to color names for the **Petersen base graph** \(n=5\), and show that **general** such covers can support inequivalent five-edge colorings. The present theorem extends rigidity to the entire specific family \(\mathrm{GP}(5m,2)\) is rigid under color permutation and supplies the complete five-DIM classification. Mahmoodi and coauthors (2024, Observation 7) provide a DIM construction for divisible-by-five orders, compatible with the family here.

## Limitations

This theorem classifies only \(\mathrm{GP}(n,2)\), \(n\ge5\), not arbitrary generalized Petersen graphs or arbitrary cubic covers of the Petersen graph. The index for nondisible-by-five orders is not determined here. The 2018 strong-index paper was available only through its abstract despite lawful open-text searches. Unindexed sources and unexamined supplementary material could contain an equivalent count, so publication priority remains a risk. The finite verification is exhaustive in the specified ranges, and the transfer certificate addresses all orders under the stated state correspondence, but independent scientific audit has not been performed.

## References

1. M. C. Lin, M. J. Mizrahi and J. L. Szwarcfiter, *Exact algorithms for dominating induced matchings* (2013), arXiv:1301.7602; accessible later arXiv manuscript arXiv:1303.0035.
2. M. Alaeiyan and H. Karami, *Perfect 2-colorings of the generalized Petersen graph*, Proceedings of the Indian Academy of Sciences (Mathematical Sciences) 126 (2016), 289–294, doi:10.1007/s12044-016-0285-4, especially Theorem 3.9.
3. Z. Yang and B. Wu, *Strong edge chromatic index of the generalized Petersen graphs*, Applied Mathematics and Computation 321 (2018), 431–441, doi:10.1016/j.amc.2017.10.047.
4. B. Lužar, E. Mačajová, M. Škoviera and R. Soták, *Strong edge colorings of graphs and the covers of Kneser graphs* (2021), arXiv:2101.04768; Journal of Graph Theory (2022), doi:10.1002/jgt.22802.
5. A. Mahmoodi, A. Behmaram, T. Došlić and N. Asadi, *Dominating induced matchings and other graph parameters* (2024), doi:10.1080/09728600.2024.2342310, Observation 7.
