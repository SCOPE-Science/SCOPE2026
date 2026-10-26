# A sharp rank-three obstruction to cyclic-line separation for zero-sum-free sequences

## Finding

Let \(G_r=(\mathbb Z/3\mathbb Z)^r\), for integer \(r\ge1\). For any nonempty indexed sequence \(S\) of nonzero vectors, write \(S_H\) for the subsequence consisting of vectors in a one-dimensional subgroup \(H\), and let \(\Sigma_+(U)\) be the sums of all **nonempty** subsequences of \(U\). Say that an occupied cyclic subgroup \(H\) **separates** \(S\) if
\[
H\cap\Sigma_+(S\setminus S_H)=\varnothing.
\]
The property that every zero-sum-free sequence has a separating occupied cyclic subgroup holds for \(r=1,2\), and fails for **every \(r\ge3\)**. In the failing ranks there is a zero-sum-free witness \(S_r\) of maximum possible length \(2r\), containing one vector from each of \(2r\) distinct cyclic subgroups, such that every occupied \(H\) satisfies
\[
(H\setminus\{0\})\cap\Sigma_+(S_r\setminus (S_r)_H)\ne\varnothing.
\]

## Assumptions and scope

All vector addition is modulo three. An indexed sequence may contain repeated vectors; subsets are taken over its indexed positions, not only its distinct values. The zero-sum-free condition excludes zero sums from **nonempty** index subsets. The empty indexed sequence is excluded from the assertion about an occupied line. Every nonzero cyclic subgroup of \(G_r\) is a one-dimensional \(\mathbb F_3\)-subspace with three elements. No claim is made for other primes. The result treats the nonempty-subsums version of the cyclic-subgroup strengthening discussed by He; it is not a statement that his displayed formula is consistent with his inclusion-of-empty-subsums convention.

## Proof

**1. Davenport bound with an independent proof.** Every \(2s+1\) vectors in \(G_s\) have a nonempty zero-sum subsequence. To see this, work in the group algebra \(A=\mathbb F_3[G_s]\). For coordinate generators \(X_1,\ldots,X_s\), set \(Y_i=X_i-1\). Then \(Y_i^3=X_i^3-1=0\), and the augmentation ideal \(J=(Y_1,\ldots,Y_s)\) satisfies \(J^{2s+1}=0\), since any monomial of total degree at least \(2s+1\) contains some \(Y_i^3\). Given \(2s+1\) vectors \(v_j\), the product \(\prod_j(1-X^{v_j})\) belongs to \(J^{2s+1}\) and vanishes. If no nonempty subset sums to zero, its coefficient at the group identity would equal \(1\) (the empty subset alone), a contradiction. The bound is sharp: two copies of each basis vector form a zero-sum-free sequence of length \(2s\).

**2. A general line-return lemma.** Let \(r\ge2\) and let \(S\subset G_r\) be any zero-sum-free indexed sequence of length \(2r\) meeting each one-dimensional subgroup in at most one term. Fix any occupied line \(H\). Its complementary sequence has length \(2r-1\); its image under \(G_r\to G_r/H\cong G_{r-1}\) has a nonempty zero-sum subsequence by Step 1. The corresponding nonempty subsequence of the complement therefore sums to \(H\). Its sum cannot be \(0\), since \(S\) is zero-sum-free. Thus \((H\setminus\{0\})\cap\Sigma_+(S\setminus S_H)\ne\varnothing\). This lemma applies independently to every occupied \(H\).

**3. A six-term rank-three witness.** In \(G_3\), take the indexed terms
\[
\begin{aligned}
a&=(1,0,0),&b&=(0,1,0),&c&=(1,1,0),\\
d&=(0,0,1),&e&=(1,0,1),&f&=(2,1,1).
\end{aligned}
\]
These six vectors are pairwise nonproportional in \(\mathbb F_3^3\), hence occupy six distinct cyclic subgroups. Every subset involving \(d,e,f\) has third-coordinate sum equal to the number chosen modulo three. Therefore a zero-sum subset uses either none or all three of \(d,e,f\). Among \(a,b,c\), no nonempty subset has sum zero; the only sums with first coordinate zero are the empty sum and \(b\), so the sum \(-b\) is unattainable. Since \(d+e+f=b\), no zero-sum subset exists. The witness is zero-sum-free, has length six, and Step 2 rules out a separating occupied line. For direct inspection, exterior index subsets realizing a nonzero return to each respective line \(\langle a\rangle,\ldots,\langle f\rangle\) are respectively \(\{b,c,d,e,f\}\), \(\{d,e,f\}\), \(\{a,b\}\), \(\{b,c,f\}\), \(\{a,d\}\), and \(\{c,e\}\).

**4. Extension to every higher rank.** Suppose \(S_r\) is a maximum-length zero-sum-free sequence meeting each line at most once. Embed it with final coordinate zero in \(G_{r+1}\), and append \(u=(0,\ldots,0,1)\) and \(w=(1,0,\ldots,0,1)\). Every subset involving one or both new vectors has final coordinate one or two, hence cannot sum to zero; the remaining subsets lie in the already zero-sum-free \(S_r\). The new vectors lie in distinct lines, each different from any old line. Hence \(S_{r+1}\) is zero-sum-free, has \(2(r+1)\) terms on distinct lines, and Step 2 applies. Induction from Step 3 completes the counterexamples for all \(r\ge3\).

**5. The sharp positive cases.** For \(r=1\), the only occupied line contains every term, so its complement is empty and separates. For \(r=2\), the length is at most four by Step 1. A sequence of length one or two has a separating occupied line. For length three: if some line contains two terms, the complement has one vector off that line, and the line separates. Otherwise all three terms occupy distinct lines. Were every occupied line nonseparating, the sum of the two terms outside each such line would lie on the line; adding its sole occupied term would place the total sum of the three terms in every one of the distinct lines, so it would equal zero, contradicting zero-sum freeness. For length four, four occupied distinct lines are impossible: choose independent terms \(a,b\), with other two terms \(c=\pm(a+b)\) and \(d=\pm(a-b)\); if \(c=-(a+b)\) then \(a+b+c=0\); otherwise either \(a+c+d=0\) or \(b+c+d=0\). Thus some line \(H\) contains a pair of terms. They must be equal, since opposites would sum to zero. Three equal terms would also sum to zero, so exactly two terms occupy \(H\). The other two terms are off \(H\); if their sum belonged to \(H\), that sum is nonzero by zero-sum freeness, and its sum with one or both of the two equal terms in \(H\) would be zero, a contradiction. Consequently no nonempty subsum of the exterior two terms is in \(H\), and \(H\) separates. (This argument also covers when those two exterior terms share a different line.)

## Verification

The standalone `verify.py` enumerates all nonempty subsets of the rank-three seed, confirms the six distinct occupied lines and the nonzero exterior-return witnesses, checks extensions to ranks four and five, and exhaustively examines all unordered zero-sum-free indexed sequences in \(G_2\) of lengths at most four. It reports `VERIFY_OK`, including rank-two accepted counts \(8,32,72,72\) for lengths one through four. The infinite-rank conclusion depends on the group-algebra and quotient arguments in Steps 1–4; finite enumeration is corroborative, not the universal proof.

## Relationship to prior work

Xiaoyu He's *Cross Number Invariants of Finite Abelian Groups* (arXiv:1308.3896, first posted 2013-08-18), Section 5, Conjecture 23, proposes a cyclic-subgroup separation strengthening. In its formal definition on page 2, \(\Sigma(U)\) includes the empty sum, so the conjecture's displayed disjointness condition is literally impossible. The present theorem does not rely on this syntactic problem: it studies the stronger, mathematically meaningful question after **excluding the empty sum**, and proves a sharp rank threshold with maximal-length counterexamples.

Gao and Geroldinger (2003), Theorem 6.2, give the different bound \(|\Sigma_+(T)\cap H|\le|T|\) for arbitrary subsequences of a maximal zero-sum-free sequence, and Corollary 6.3 makes unequal occupied terms independent. Their Remark 6.4(2)(c) gives squarefree maximal minimal zero-sum sequences for ranks at least five in the ternary case; combined with their corollary and the quotient Davenport argument above, this already supplies **higher-rank** counterexamples by implication, although not the sharp rank-three threshold. The distinctive contribution here is the explicit rank-three seed, its no-separation proof, the rank-one/two converse, and the complete threshold. Kim (arXiv:1410.6867), whose different Conjecture 23 concerns maximal cross-number decompositions, treats a distinct structural question. Qu, Xia, Xue and Zhong (2015) study cardinalities of subsum sets, rather than cyclic-line separation.

## Limitations

This result does not disprove He's weaker Conjecture 22 and does not settle any other prime characteristic. The statement separates the literal empty-sum convention from the nonempty-sum version, and claims novelty only for the sharp ternary rank threshold, not for the standard Davenport constant or for the existence of squarefree extremal examples in all sufficiently high ranks. Equivalent accounts of the rank-three witness or its line-separation implication could exist outside the inspected sources. No independent audit has been performed.

## References

1. X. He, *Cross Number Invariants of Finite Abelian Groups*, arXiv:1308.3896v1 (2013-08-18), especially Section 5, Conjecture 23 and the introductory definition of \(\Sigma\). https://arxiv.org/abs/1308.3896
2. W. Gao and A. Geroldinger, *Zero-sum problems and coverings by proper cosets*, European J. Combin. 24 (2003), 531–549, DOI:10.1016/S0195-6698(03)00033-7, especially Theorem 6.2, Corollary 6.3 and Remark 6.4. https://kam.mff.cuni.cz/~ksemweb/clanky/GaoGeroldinger-zero_sums_covering.pdf
3. B. Kim, *The Cross Number of Minimal Zero-sum Sequences in Finite Abelian Groups*, arXiv:1410.6867 (2014), especially Introduction, Section 4, concluding discussion. https://arxiv.org/abs/1410.6867
4. Y. Qu, X. Xia, L. Xue and Q. Zhong, *Subsequence sums of zero-sum free sequences over finite abelian groups*, Colloq. Math. 140 (2015), 119–127, DOI:10.4064/cm140-1-10. https://www.impan.pl/en/publishing-house/journals-and-series/colloquium-mathematicum/all/140/1/87545/subsequence-sums-of-zero-sum-free-sequences-over-finite-abelian-groups
