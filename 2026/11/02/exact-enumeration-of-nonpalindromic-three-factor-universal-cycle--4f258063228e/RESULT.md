# Exact enumeration of nonpalindromic three-factor universal cycles

## Finding

Let \(\Sigma\) be a labeled alphabet of size \(q\ge2\), and let
\[\mathcal N_q=\{abc\in\Sigma^3:a\ne c\}.\]
A universal cycle for \(\mathcal N_q\) is an oriented circular word whose consecutive cyclic three-letter factors contain every element of \(\mathcal N_q\) exactly once. Cyclic rotations are identified, but symbol permutations and reversal are not.

**Theorem.** Such cycles exist for every \(q\ge2\) and have length \(q^2(q-1)\). Their exact number is \(U_2=1\) and, for all \(q\ge3\),
\[
U_q=q^{q(q-1)/2+q-3}(q-2)^{(q-1)(q-2)/2}(q-1)^{q-1}\bigl((q-2)!\bigr)^{q^2}.
\]
In particular, \(U_3=108\) and \(U_4=231928233984\). The same proof determines the complete adjacency spectrum of the restricted overlap graph:
\[
\chi_q(\lambda)=(\lambda-q+1)(\lambda+1)^{q(q-1)/2}(\lambda-1)^{(q-1)(q-2)/2}(\lambda^2+q-1)^{q-1}.
\]
Here \(\chi_q(\lambda)=\det(\lambda I-A_q)\); the factor formula holds also at \(q=2\).

## Assumptions and scope

Every letter of \(\Sigma\) is distinct and labeled. The ordering of a circular word is retained (only changes of its starting index are identified). A factor crossing the end of the word is interpreted cyclically. A palindrome of length three is exactly a word of the form \(aba\); hence the permissible set \(\mathcal N_q\) comprises all nonpalindromic length-three words. The result concerns the precise once-only coverage requirement, not arbitrary palindrome-avoiding circular words. Nothing is asserted about factors of any other length, quotienting by the alphabet-permutation group, or reversal equivalence.

## Proof

**1. Edge representation.** Define a directed graph \(G_q\) with vertex set \(\Sigma^2\). For every \(abc\in\mathcal N_q\), add the uniquely labeled edge \((a,b)\to(b,c)\). Every vertex has indegree and outdegree \(d=q-1\), and there are exactly \(q^2(q-1)\) edges. A cyclic word covering all allowed three-factors once gives an Euler tour of this graph, and conversely. Distinct edge labels make this correspondence one-to-one after cyclic rotations.

**2. Characteristic polynomial.** On the complex vector space of \(q\)-by-\(q\) matrices, write \(\mathbf 1\) for the all-ones column. Adjacency acts on a matrix \(F\) indexed by \((a,b)\) as
\[
(A_qF)_{ab}=\sum_{c\ne a}F_{bc},\qquad
A_qF=\mathbf1(F\mathbf1)^{\mathsf T}-F^{\mathsf T}.
\]
Let \(H=\{x\in\mathbb C^q:\mathbf1^{\mathsf T}x=0\}\), of dimension \(q-1\). The matrix space splits as the direct sum of \(H\otimes H\), the line spanned by \(\mathbf1\mathbf1^{\mathsf T}\), and, for every basis vector \(x\) of \(H\), the two-dimensional space spanned by \(\mathbf1x^{\mathsf T}\) and \(x\mathbf1^{\mathsf T}\).

On \(H\otimes H\), row sums vanish and \(A_qF=-F^{\mathsf T}\). The symmetric subspace has dimension \(q(q-1)/2\) and eigenvalue \(-1\); the skew-symmetric subspace has dimension \((q-1)(q-2)/2\) and eigenvalue \(+1\). On the all-ones line the eigenvalue is \(q-1\). For each \(x\in H\),
\[
A_q(\mathbf1x^{\mathsf T})=-x\mathbf1^{\mathsf T},\qquad
A_q(x\mathbf1^{\mathsf T})=(q-1)\mathbf1x^{\mathsf T}.
\]
The last block has characteristic polynomial \(\lambda^2+q-1\). These spaces have total dimension \(q^2\) and establish the displayed characteristic polynomial with its exact multiplicities.

**3. Tree cofactor and connectivity.** Let \(L_q=(q-1)I-A_q\). The eigenvalue \(q-1\) of \(A_q\) has multiplicity exactly one for every \(q\ge2\), so \(L_q\) has a simple zero eigenvalue. Because every vertex has equal incoming and outgoing degree, both row and column sums of \(L_q\) vanish. Thus its \(q^2\) principal cofactors are equal. The directed matrix-tree theorem and the product of nonzero eigenvalues give the rooted in-arborescence count
\[
t_q=\frac{q^{q(q-1)/2}(q-2)^{(q-1)(q-2)/2}[q(q-1)]^{q-1}}{q^2}
\]
for \(q\ge3\), simplifying to
\[
t_q=q^{q(q-1)/2+q-3}(q-2)^{(q-1)(q-2)/2}(q-1)^{q-1}.
\]
This is a positive integer. Therefore every root has a spanning in-arborescence, and in particular \(G_q\) is strongly connected. At \(q=2\), its four vertices form the single directed four-cycle \((0,0)\to(0,1)\to(1,1)\to(1,0)\to(0,0)\); there is one in-arborescence per root.

**4. Euler-tour enumeration.** By the BEST theorem, fixing one particular initial edge and treating all edges as distinct, the number of Euler tours is \(t_q\prod_{v\in\Sigma^2}(d-1)! =t_q((q-2)!)^{q^2}\). Each allowed three-factor is a distinct edge and appears once; therefore exactly one cyclic rotation of each universal word begins with the chosen edge. No extra division by the cycle length or by alphabet permutations is appropriate. Substitution of the tree count proves the theorem, including existence. The special case \(q=2\) contributes one cycle.

## Verification

The standalone pure-Python program `verify.py` computes the full integer Laplacian cofactor independently with fraction-free Bareiss elimination for \(2\le q\le6\), and compares each cofactor with the closed formula. For \(q=2,3\), a separate edge-mask depth-first enumeration counts all Euler circuits with a prescribed initial edge, and checks that the cyclic three-factors of each completed word are exactly \(\mathcal N_q\). The program prints `VERIFY_OK` only after every check passes.

The resulting small values, without identifying permutations or reversals, are \(U_2=1\), \(U_3=108\), \(U_4=231928233984\). The finite checks illustrate and cross-check the identities, but the all-\(q\) result rests on the exact matrix decomposition and theorems used above.

## Relationship to prior work

Gardner and Godbole (2017) establish existence of universal cycles for several restricted word families and provide the general Eulerian framework, but their studied restrictions do not include the exact present family or its all-alphabet count. Chen, Kitaev and Sun (2020) give existence-probability formulas when up to two words are removed and small binary cases; here \(q^2\) palindromes are omitted simultaneously and the *number of Euler tours* is evaluated. Burris, Motta and Shipman (2016) study unoriented de Bruijn words, including palindrome treatment, but use reflection classes rather than including every nonpalindrome as a separate oriented factor. Bernardini and coauthors (2022) optimize Eulerian extensions of de Bruijn graphs rather than counting Euler tours of this already balanced graph. Arrigo and coauthors (2018) count non-backtracking walks through generating functions, but do not evaluate the present nonrepeating-edge Euler-tour count.

The BEST and directed matrix-tree theorems are classical, not new. The claim here is the explicit spectrum and its exact, infinite-family cyclic enumeration under ordinary three-letter palindrome exclusion.

## Limitations

A complete bibliographic search cannot exclude an unindexed equivalent spectrum or Euler-tour formula. A general non-backtracking matrix framework might be specialized to recover parts of the spectrum, though the inspected works do not directly give this enumeration. The problem does not address biological reverse-complement palindromes, and the formula should not be read as a reverse-complement DNA restriction. No independently audited mathematical validation is asserted.

## References

1. K. B. Gardner and A. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029v1 (first public 2017-11-19), https://arxiv.org/abs/1711.07029.
2. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8 (2020), 778, https://doi.org/10.3390/math8050778.
3. C. S. Burris, F. C. Motta and P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480v1 (2016), https://arxiv.org/abs/1608.08480.
4. G. Bernardini, H. Chen, G. Loukides, S. P. Pissis, L. Stougie and M. Sweering, *Making de Bruijn Graphs Eulerian*, CPM 2022, https://doi.org/10.4230/LIPIcs.CPM.2022.12.
5. F. Arrigo, P. Grindrod, D. J. Higham and V. Noferini, *On the Exponential Generating Function for Non-Backtracking Walks*, Linear Algebra Appl. 556 (2018), 381–399, https://doi.org/10.1016/j.laa.2018.07.010.
