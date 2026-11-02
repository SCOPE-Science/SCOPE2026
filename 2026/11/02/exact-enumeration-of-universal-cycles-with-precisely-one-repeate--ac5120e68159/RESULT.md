# Exact enumeration of universal cycles with precisely one repeated symbol per triple

## Finding

Let \(\Sigma\) be a labeled alphabet of cardinality \(q\ge2\), and let
\[\mathcal T_q=\{abc\in\Sigma^3:\lvert\{a,b,c\}\rvert=2\}.\]
A *universal cycle* for \(\mathcal T_q\) is a cyclic word whose indexed circular length-three factors are exactly the \(3q(q-1)\) distinct words in \(\mathcal T_q\), each exactly once. Two cyclic words are identified only under rotation, not reversal or alphabet relabeling.

**Theorem.** Universal cycles for \(\mathcal T_q\) exist for every integer \(q\ge2\), and their exact number is
\[
\boxed{U_q=2^{q-1}3^{(q-1)(q-2)/2}q^{q-2}\bigl((q-2)!\bigr)^q.}
\]
Every such cycle has length \(3q(q-1)\), and each alphabet letter occurs exactly \(3(q-1)\) times. The first numbers, for \(q=2,3,4,5,6\), are \(2,36,55296,11337408000,467988280328060928\).

## Assumptions and scope

The symbols are distinct and labeled. Factors are contiguous and cyclic, i.e., they may wrap around the end. Each permitted triple has exactly two equal letters, so triples with three distinct letters and constant triples are both excluded. The count concerns full cyclic words with no additional length-three factors, up to rotation only. No claim is made about linear words, unlabeled alphabets, other triple predicates, or longer factor lengths.

## Proof

**1. Overlap graph and existence.** Construct the directed overlap graph \(G_q\) with vertices the \(q^2\) ordered pairs \((a,b)\). Each target triple \(abc\in\mathcal T_q\) supplies its own directed edge from \((a,b)\) to \((b,c)\). All edges are distinct. At a diagonal vertex \((a,a)\), the outgoing edges are \(aab\) for \(b\ne a\), and the incoming edges are \(baa\), hence both degrees equal \(q-1\). At an off-diagonal vertex \((a,b)\), \(a\ne b\), the outgoing edges are \(aba,abb\), and the incoming edges are \(aab,bab\), so both degrees are \(2\).

The graph is strongly connected. From any off-diagonal pair \((a,b)\) there is an edge \(abb\) to the diagonal pair \((b,b)\). From any diagonal \((a,a)\) there is an edge \(aab\) to any off-diagonal \((a,b)\) with \(b\ne a\), followed by \(abb\) to \((b,b)\). Thus all diagonal vertices communicate, and every off-diagonal vertex can be reached from a diagonal vertex. Balancedness and strong connectivity guarantee an Eulerian circuit. Reading the overlapping edges produces a cyclic word visiting every target triple exactly once.

**2. Reduction to rooted arborescences.** Fix distinct letters designated \(0\) and \(1\). Every universal cycle has the triple \(001\) at exactly one cyclic position. Rotating to that position gives a bijection between cyclic words and Euler circuits starting with the prescribed edge \(001\), leaving the root vertex \((0,0)\). The directed BEST theorem therefore gives
\[
U_q=\tau_q\prod_{v\in V(G_q)}(d^+(v)-1)!=\tau_q\bigl((q-2)!\bigr)^q,
\]
where \(\tau_q\) is the number of in-arborescences rooted at \((0,0)\). The off-diagonal vertices contribute \((2-1)!=1\) each. As each triple is a unique labeled edge, no parallel-edge quotient or periodic-word divisor enters this count.

**3. Exact directed matrix-tree evaluation.** Let \(L=\operatorname{diag}(d^+)-A\) be the directed outgoing Laplacian. Order its vertices so that the \(q\) diagonal pairs come first and the \(q(q-1)\) off-diagonal pairs come second. Write the matrix in blocks \(L_{DD},L_{DO},L_{OD},L_{OO}\). On off-diagonal ordered pairs, let \(R\) swap \((a,b)\leftrightarrow(b,a)\); then
\[
L_{OO}=2I-R,\qquad L_{OO}^{-1}=(2I+R)/3,\qquad
\det L_{OO}=3^{\binom q2}.
\]
Indeed, each unordered pair contributes the \(2\times2\) block \(\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\) of determinant \(3\). The diagonal-to-off-diagonal block selects \((a,b)\) for every \(b\ne a\); the off-diagonal-to-diagonal block selects \((b,b)\) from \((a,b)\). Consequently the Schur complement on the diagonal vertices has entries \(2(q-1)/3\) on its diagonal and \(-2/3\) off diagonal, i.e.,
\[
S=L_{DD}-L_{DO}L_{OO}^{-1}L_{OD}=\tfrac23(qI-J),
\]
where \(J\) is the all-ones matrix of order \(q\).

Delete the row and column of root \((0,0)\) from \(L\). Because the root lies in the diagonal block, block Gaussian elimination gives the determinant as \(\det L_{OO}\) times the corresponding principal \((q-1)\)-minor of \(S\). The principal \((q-1)\)-minor of \(qI-J\) is \(q^{q-2}\), by the complete-graph matrix-tree determinant (or its eigenvalues \(1,q,\ldots,q\) after deleting a row and column). The directed matrix-tree theorem now yields
\[
\tau_q=3^{\binom q2}\left(\tfrac23\right)^{q-1}q^{q-2}
=2^{q-1}3^{(q-1)(q-2)/2}q^{q-2}.
\]
Substitution into the BEST formula completes the count for every \(q\ge2\).

**4. Letter balance.** Exactly \(3(q-1)\) members of \(\mathcal T_q\) have any specified letter in their first position: there are \(q-1\) triples of each of the forms \(aab,aba,abb\), with the chosen symbol interpreted as the first letter. Since the first positions of successive cyclic triples are exactly the symbol positions of the cycle, every letter occurs exactly \(3(q-1)\) times.

## Verification

Run `python3 verify.py` using only the Python standard library. The code independently builds the full integer Laplacian and calculates a rooted cofactor by fraction-free elimination for every \(2\le q\le8\); it constructs and checks a universal cycle for every \(2\le q\le25\); and it exhaustively traverses all Euler circuits containing the prescribed first edge for \(q=2,3,4\). The exhaustive results are \(2,36,55296\), agreeing with the formula. These finite checks corroborate the proof but do not establish the formula for all alphabet sizes.

## Relationship to prior work

Gardner and Godbole's *Universal Cycles of Restricted Words* (arXiv:1711.07029v1, November 19, 2017) surveys existence of universal cycles for constrained words, including the binary equitable length-three case and broader non-injective cases. Chen, Kitaev, and Sun's *On the probability of existence of a universal cycle or a universal word for a set of words* (arXiv:1908.01116v1, August 3, 2019) considers deletions from the unrestricted set of words, including small exact cases. Sawada, Sears, Trautrim, and Williams's *Concatenation trees* (arXiv:2308.12405v1, August 23, 2023) develops construction techniques. These results supply the surrounding universal-cycle framework, but the inspected results do not determine the exact all-alphabet number of cycles of the prescribed three-letter equality pattern. The general BEST and directed matrix-tree theorems are used as established tools, not claimed as new.

## Limitations

The result is for labeled alphabets and rotation equivalence only. Counting up to letter permutations or reversal is a different orbit-enumeration problem. An equivalent count in less-indexed literature cannot be excluded; the 2013 *Universal Cycles of Complementary Classes* paper was located in abstract and summarized by the 2017 literature, but its complete text could not be inspected. The formula's proof uses classical Euler-tour and determinant results, with the evaluated restricted graph family being the claimed contribution. No independent scientific validation has been performed.

## References

1. K. B. Gardner and A. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029v1 (first public November 19, 2017), https://arxiv.org/abs/1711.07029.
2. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116v1 (first public August 3, 2019), https://arxiv.org/abs/1908.01116.
3. J. Sawada, J. Sears, A. Trautrim and A. Williams, *Concatenation trees: A framework for efficient universal cycle and de Bruijn sequence constructions*, arXiv:2308.12405v1 (first public August 23, 2023), https://arxiv.org/abs/2308.12405.
4. M. Champlin, A. P. Godbole and B. Tomlinson, *Universal Cycles of Complementary Classes*, arXiv:1303.3323 (first public March 14, 2013), https://arxiv.org/abs/1303.3323 (background; abstract and secondary summary only).
5. N. G. de Bruijn and T. van Aardenne-Ehrenfest, *Circuits and Trees in Oriented Linear Graphs*, Simon Stevin 28 (1951), 203–217 (classical BEST theorem).
