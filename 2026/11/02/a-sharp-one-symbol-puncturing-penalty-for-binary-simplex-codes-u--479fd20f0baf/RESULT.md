# A sharp one-symbol puncturing penalty for binary simplex codes under cyclic pair reads

## Finding

For every integer \(m\ge3\), put \(q=2^m\), \(k=2^{m-2}\) and \(n=q-2=4k-2\). Start from the binary simplex code with one coordinate punctured, so the generator matrix has every nonzero column of \(\mathbb F_2^m\) except one. The remaining columns may be put in any cyclic order. Then

\[
\max_{\text{cyclic column orders}} d_{\mathrm{pair}}=3k-1.
\]

There is an explicit optimal order with complete pair-weight enumerator

\[
W(z)=1+3kz^{3k-1}+(k-1)z^{3k}.
\]

By contrast, simply deleting the missing column from a standard Singer cyclic order gives minimum pair distance \(3k-2\). Thus a concrete two-edge exchange recovers exactly one unit of otherwise lost pair distance; no order can do better.

## Assumptions and scope

All vector spaces and linear functionals are over \(\mathbb F_2\). The length of each codeword is \(n\), coordinates are indexed around a cycle, and a position contributes one to the **cyclic symbol-pair weight** exactly when at least one of the two symbols at that position and its cyclic successor is nonzero. The pair distance of a linear code is the minimum such weight over its nonzero codewords. The enumerator includes the zero codeword.

An arbitrary nonzero puncture column may be changed to \(1\) by a vector-space automorphism; doing so relabels nonzero messages without altering pair weights. We therefore work in \(F=\mathbb F_{2^m}\), with remaining generator columns precisely \(F^*\setminus\{1\}\). The columns span the ambient \(m\)-dimensional space for all \(m\ge3\). Denote the nonzero linear functionals by \(a\) and the character \(\chi_a(x)=(-1)^{a(x)}\).

## Proof

**1. Universal upper bound for every ordering.** Fix any cyclic listing \(v_0,\ldots,v_{n-1}\) of the nonzero field elements except \(1\), with subscripts modulo \(n\). For a nonzero functional \(a\), set

\[
e_a=\#\{i:a(v_i)=a(v_{i+1})=0\}.
\]

The codeword's pair weight is exactly \(n-e_a\). Any two distinct nonzero binary vectors are linearly independent, so for each cyclic edge precisely \(2^{m-2}-1=k-1\) nonzero functionals vanish on both ends. Double counting gives

\[
\sum_{a\ne0}e_a=n(k-1)=(4k-2)(k-1).
\]

There are \(4k-1\) nonzero functionals. If each \(e_a\le k-2\), then the sum would not exceed \((4k-1)(k-2)\), strictly less than the displayed sum by \(3k\). Hence some \(e_a\ge k-1\) and

\[
d_{\mathrm{pair}}\le n-(k-1)=3k-1.
\]

**2. Explicit cycle surgery.** Choose any primitive element \(g\in F^*\). The Singer cycle

\[
(1,g,g^2,\ldots,g^{q-2})
\]

has its adjacent additive differences equal to \((g+1)g^j\), each nonzero field element exactly once. Delete vertex \(1\), replacing the two edges through it by the edge \((g^{-1},g)\). Write

\[
t=1+g^{-1},\qquad s=1+g,\qquad c=g^{-1}+g=t+s.
\]

The surviving Singer cycle has the directed edge \((t,s)\) because \(gt=s\); it also has the new edge \((g^{-1},g)\). These edges are disjoint: if any endpoints coincided, \(g\) would satisfy a polynomial of degree at most two over \(\mathbb F_2\), which contradicts primitivity when \(m\ge3\). Cut those two edges and reconnect as the undirected edges \((g^{-1},t)\) and \((g,s)\). The result is a **single Hamiltonian cycle**, not two: in the original directed cyclic list after deleting \(1\), write the edge \((t,s)\) as \((v_j,v_{j+1})\); reverse the entire suffix \((v_{j+1},\ldots,v_{n-1})\). The two new boundary edges are precisely the specified reconnections.

Before puncturing, the adjacent differences form the multiset containing every nonzero field element once. Puncturing removes the difference values \(t,s\) and introduces one extra \(c\), duplicating the existing edge difference \(c\) at \((t,s)\). The suffix-reversal reconnection deletes those two \(c\) differences and introduces two differences equal to \(1\). Consequently the final multiset of cyclic adjacent differences contains every element of \(F^*\) once, except \(t,s,c\) are missing and \(1\) occurs three times. Here \(t,s,c\) are three distinct nonzero members of one two-dimensional binary subspace, and none equals \(1\).

**3. Exact pair-weight spectrum.** For every nonzero functional \(a\), since \(\sum_{x\in F^*}\chi_a(x)=-1\), the final difference multiset implies

\[
\sum_i\chi_a(v_i+v_{i+1})
=-1-\chi_a(t)-\chi_a(s)-\chi_a(c)+2\chi_a(1).
\]

Expanding the two zero indicators and using \(\sum_i\chi_a(v_i)=-1-\chi_a(1)\), we obtain

\[
4e_a=n-3-\chi_a(t)-\chi_a(s)-\chi_a(c).
\]

Because \(c=t+s\), the last three characters sum to \(3\) if \(a(t)=a(s)=0\), and to \(-1\) otherwise. Thus \(e_a=k-2\) for the \(k-1\) nonzero functionals annihilating \(\langle t,s\rangle\), and \(e_a=k-1\) for the other \(3k\) functionals. Their pair weights are respectively \(3k\) and \(3k-1\), proving the exact enumerator and attainment of the universal bound.

**4. The loss under naive puncturing is exactly two.** Before puncturing, the Singer cycle has exactly \(k-1\) adjacent-zero pairs for each nonzero functional. Removing vertex \(1\) and joining its neighbors can increase this count by at most one, so the naive order has minimum pair weight at least \(3k-2\). Because \(1,g^{-1},g\) are linearly independent for \(m\ge3\), some functional takes values \(1,0,0\) on them. For that functional the deletion creates exactly one new zero-zero edge, and its pair weight equals \(3k-2\). This proves the claimed strict gain of the surgery. \(\square\)

## Verification

The included standalone Python program `verify.py` constructs the field and performs the specified cyclic suffix reversal for primitive binary polynomials of degrees \(3\) through \(8\). It independently checks all generator columns, adjacent-difference multiplicities and every nonzero message's pair weight, and confirms the closed formula. It also enumerates all \(6!\) punctured orderings for degree \(3\), finding precisely \(96\) optimal orders and \(624\) nonoptimal orders. The expected terminal marker is `VERIFY_OK`. These finite computations corroborate but do not replace the all-degree proof above.

For example, the new enumerators at degrees \(3,4,5\) are respectively \(1+6z^5+z^6\), \(1+12z^{11}+3z^{12}\) and \(1+24z^{23}+7z^{24}\).

## Relationship to prior work

Chen, Lin and Liu (2016) introduced bounds and constructions for constacyclic and repeated-root symbol-pair codes; their results are not an optimum over all cyclic coordinate permutations of a singly punctured binary simplex code. Ma and Luo (2019 preprint; 2021 journal) proved that the unpunctured Singer-ordered simplex code is pair-equiweight and observed that changing coordinate order changes pair weights. Their constant-weight result provides the full-length comparison but neither the sharp punctured optimum nor this two-edge repair or two-weight spectrum. Wang, Su, Zheng and Lu (2023 preprint) investigate reducible cyclic codes and a different puncturing construction of symbol-pair MDS codes, not the binary punctured simplex under arbitrary orders.

Liang and Liu (2024, 2025) study symbol-pair equiweight/simplex codes and general constructions; the available abstracts describe constant-weight frameworks, whereas the constructed code here has two distinct nonzero pair weights. Their complete texts were not accessible in this review, so exact historical priority against all theorems within those papers remains a documented risk. The statement is about an exact arrangement-constrained optimum, not a universal MDS pair-code bound or a general characterization of arbitrary code equivalence.

## Limitations

The proof applies to binary simplex codes with exactly one punctured coordinate and permits arbitrary coordinate reorderings. It concerns cyclic overlapping reads of two symbols only. It does not classify all maximizing coordinate orders or establish analogues over larger alphabets, with multiple punctures or with longer read windows. The relation to earlier inaccessible equiweight literature has not been independently audited.

## References

- B. Chen, L. Lin and H. Liu, *Constacyclic symbol-pair codes: lower bounds and optimal constructions*, arXiv:1605.03460 (first submitted 2016-05-11), https://arxiv.org/abs/1605.03460 .
- J. Ma and J. Luo, *Symbol-pair Weight Distributions of Some Linear Codes*, arXiv:1911.02184 (first submitted 2019-11-06), https://arxiv.org/abs/1911.02184 .
- X. Wang, Y. Su, D. Zheng and W. Lu, *Two classes of reducible cyclic codes with large minimum symbol-pair distances*, arXiv:2309.04068 (first submitted 2023-09-08), https://arxiv.org/abs/2309.04068 .
- Y. Liang and Z. Liu, *The Plotkin-Type Bound on the Generalized Symbol-Pair Weight and Symbol-Pair Equiweight Codes*, IEEE Transactions on Information Theory (2024), https://doi.org/10.1109/TIT.2024.3392744 .
- Y. Liang and Z. Liu, *New Constructions of Symbol-Pair Simplex Codes*, IEEE Transactions on Information Theory (2025), https://doi.org/10.1109/TIT.2025.3621494 .
