# Complete integral persistence of rank-span filtered proper Boolean lattices
## Finding
For an integer \(n\geq3\), let \(P_n\) be the poset of nonempty proper subsets of \([n]\), ordered by inclusion. For \(0\leq k\leq n-2\), let \(K_{n,k}\) be the simplicial complex whose simplices are the nonempty chains \(A_0\subsetneq\cdots\subsetneq A_j\) with \(|A_j|-|A_0|\leq k\). The inclusions \(K_{n,0}\subseteq\cdots\subseteq K_{n,n-2}\), followed by a constant tail, define a filtered space.

**Exact integral persistence classification.** Define integers \(b_{n,k}\) by
\[
 b_{n,0}=2^n-3,\qquad
 b_{n,k}=\binom nk\bigl(2^{n-k}-2\bigr)-b_{n,k-1}
 \quad(1\leq k\leq n-2).
\]
Then each \(K_{n,k}\) has homotopy type \(\bigvee^{b_{n,k}}S^k\), where a wedge of \(b_{n,0}\) copies of \(S^0\) denotes a discrete space of \(b_{n,0}+1\) points. For the reduced homology persistence module with **integral** coefficients, every class in degree \(k<n-2\) is born at filtration level \(k\) and dies at the next level \(k+1\). There are exactly \(b_{n,k}\) such bars, while exactly one degree-\(n-2\) class born at \(n-2\) persists forever. Equivalently, in any coefficient field these are all the reduced interval bars; all integral homology groups are torsion free. The homotopy wedge existence is a known theorem of Kitajima; the asserted contribution is the **uniform, closed integer multiplicity recurrence and consequent entire barcode** for every \(n\) and every level.

Equivalently, for \(0\leq k\leq n-2\),
\[
 b_{n,k}=(-1)^k\left(2^n-3+\sum_{s=1}^k(-1)^s\binom ns(2^{n-s}-2)\right).
\]
In particular \(b_{n,n-2}=1\). Initial multiplicity sequences \((b_{n,0},\ldots,b_{n,n-2})\) for \(n=3,4,5,6\) are \((5,1)\), \((13,11,1)\), \((29,41,19,1)\), and \((61,119,91,29,1)\), respectively.

## Assumptions and scope
The filtration index \(k\) is an integer and rank span means the difference of the *largest and smallest cardinalities in the same chain*, not a global selection of allowed ranks. We use the reduced singular (equivalently simplicial) homology of finite simplicial complexes, with coefficients in \(\mathbb Z\), and take the filtration to be constant for all \(k\geq n-2\). Statements about interval bars over fields follow by tensoring the explicitly determined integral groups and zero transition maps. Reduced degree-zero homology is used at the first level. The endpoints of the bars are half-open because the filtration uses inclusive rank-span cutoffs.

## Proof
**1. Known concentrated homotopy.** The full Boolean lattice on \([n]\) is a geometric lattice of rank \(n\). Kitajima's Corollary 4.19 (arXiv:2606.15241) applies to its proper part and gives \(K_{n,k}\simeq\bigvee S^k\) for all \(0\leq k\leq n-2\). Thus reduced integral homology is free, supported in degree \(k\), with some positive multiplicity \(b_{n,k}\). We do not re-prove or claim originality of this structural theorem.

**2. Count chains by their rank span.** For each \(j\geq1\), a \(j\)-simplex \(A_0\subsetneq\cdots\subsetneq A_j\) has rank span \(s\geq j\). Choose the \(s\) coordinates of \(A_j\setminus A_0\) in \(\binom ns\) ways. The initial subset lies entirely among the other \(n-s\) coordinates and cannot be empty or make the last subset all of \([n]\); hence there are \(2^{n-s}-2\) choices. Finally, distribute the \(s\) added coordinates among the \(j\) successive, ordered, nonempty increments. Their number is \(j!\,\operatorname{S}(s,j)\), where \(\operatorname{S}(s,j)\) denotes a Stirling number of the second kind. Consequently, writing \(f_j\) for the number of \(j\)-dimensional faces,
\[
 f_0(K_{n,k})=2^n-2,\qquad
 f_j(K_{n,k})=\sum_{s=j}^k\binom ns(2^{n-s}-2)j!\,\operatorname{S}(s,j)
 \quad(1\leq j\leq k).
\]
This counts each chain exactly once, by its uniquely determined first and last sets and ordered nonempty increments. The formula also covers \(k=0\) with no positive-dimensional faces.

**3. Evaluate Euler characteristic exactly.** The identity
\[
 \sum_{j=1}^s(-1)^j j!\,\operatorname{S}(s,j)=(-1)^s\quad(s\geq1)
\]
follows by evaluating the standard expansion of \(x^s\) into falling factorials at \(x=-1\). Substituting the face numbers gives
\[
 \widetilde\chi(K_{n,k})=2^n-3+\sum_{s=1}^k(-1)^s\binom ns(2^{n-s}-2).
\]
Because the reduced homology is free and concentrated in degree \(k\), \(\widetilde\chi(K_{n,k})=(-1)^k b_{n,k}\). This yields the explicit alternating-sum formula, and subtracting its formulas at consecutive \(k\) gives the claimed recurrence with \(b_{n,0}=2^n-3\). At \(k=n-2\), the filtered complex is the entire order complex of nonempty proper subsets, namely the barycentric subdivision of the boundary of an \((n-1)\)-simplex; it is \(S^{n-2}\), so \(b_{n,n-2}=1\).

**4. Compute every persistence map.** For any integer \(k<n-2\), the only nonzero reduced integral homology of \(K_{n,k}\) is in degree \(k\), whereas that of \(K_{n,k+1}\) is in degree \(k+1\). Therefore each inclusion induces zero in **every** reduced degree. The chain of filtration maps has no class surviving from one nonterminal level into the next. At the terminal level the complex is unchanged, and its sole top-degree generator survives indefinitely. The asserted intervals, their multiplicities and the integral torsion statement now follow. Over a field the same zero maps and free groups produce precisely the stated ordinary interval decomposition. This completes the infinite-family argument.

## Verification
The included `verify.py` uses only the Python standard library. It independently enumerates chains as simplices, builds simplicial boundary matrices over \(\mathbb F_2\), and checks all reduced Betti numbers and the recurrence for every level when \(3\leq n\leq6\). Separately it checks the face-count and reduced Euler-characteristic formulas for every \(3\leq n\leq40\). Execute `python3 verify.py` from the extracted file directory; successful output ends in `VERIFY_OK`. The finite calculations corroborate the explicit combinatorics, but only the mathematical proof above establishes all \(n\). The structural wedge theorem is cited, rather than inferred from computation.

## Relationship to prior work
Kitajima's December 15, 2025 public poster abstract already introduced the filtration and proved wedge-shape existence for geometric semilattices. The fuller article (first posted June 13, 2026), particularly Corollary 4.19, already proves the **existence** of wedge-of-spheres types for the filtered proper parts of geometric lattices, and Example 4.21 already computes the values \((29,41,19,1)\) for the proper Boolean lattice on five elements. The present classification uses that theorem and establishes the missing all-parameter multiplicities and explicit persistence bars; it is not an alternative proof of the wedge theorem. A published rank-span-two Boolean-lattice calculation gives the entire permutation character and in particular the previously known closed value of \(b_{n,2}\). Our recurrence reproduces that degree-two value exactly; its claim to new information is for the *whole filtration*, particularly all variable \(k\) and the barcode. Hersh–Sundaram study fixed rank-selected subposets of geometric lattices, a different filtration from moving rank-span windows. Their representation-theoretic stability results do not directly specify the reduced intervals here. The possibility that equivalent formulas were derived elsewhere or follow implicitly from an unindexed presentation remains a residual originality risk.

## Limitations
The result concerns the proper Boolean lattice, not arbitrary geometric semilattices or arbitrary rank-filtered posets. It gives the nonequivariant **integral** barcode and homotopy multiplicities, not the symmetric-group action on persistent homology, canonical generators, or a natural equivariant wedge splitting. General wedge existence and the rank-span-two multiplicity are prior results, not newly claimed. No exhaustive novelty assertion is made.

## References
1. Yoh Kitajima, *Filtered order complexes and magnitude homology of pure shellable posets*, poster abstract, Arrangements in Osaka 2025, presentation December 15, 2025, https://sites.google.com/view/arrangements-in-osaka-2025/posters .
2. Yoh Kitajima, *Filtered order complexes and magnitude homology of finite graded posets*, arXiv:2606.15241, first public June 13, 2026, https://arxiv.org/abs/2606.15241. Especially Corollary 4.19 and Example 4.21.
3. Patricia Hersh and Sheila Sundaram, *Stability and ribbon bases for the rank-selected homology of geometric lattices*, arXiv:2604.06479, first public April 7, 2026, https://arxiv.org/abs/2604.06479.
4. *Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-symmetric-group-characters-and-contractible-quotients-of-rank-sp--a68d321e2fa8, inspected `RESULT.md`.
