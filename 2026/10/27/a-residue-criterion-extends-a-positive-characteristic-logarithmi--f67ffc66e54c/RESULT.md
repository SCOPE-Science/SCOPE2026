# A residue criterion extends a positive-characteristic logarithmic foliation theorem

## Finding

Let \(k\) be an algebraically closed field of characteristic \(p>0\), let \(n\ge 3\), and let \(r\ge 3\). Choose positive integers \(1\le d_1\le\cdots\le d_r\). Suppose exactly two indices \(a,b\) satisfy \(p\nmid d_a,d_b\), and every other degree is divisible by \(p\). If

\[
p\nmid(d_a+d_b),
\]

then the logarithmic locus \(\operatorname{Log}_{(d_1,\ldots,d_r)}(\mathbb P_k^n)\) is an irreducible component of the support of the scheme of codimension-one foliations \(\operatorname{Fol}^{1}_{d}(\mathbb P_k^n)\), where \(d=\sum_{i=1}^r d_i-2\).

The condition is a genuine subcase of the parameter stratum omitted from Theorem A of Mendson–Pereira: their theorem excludes the case in which exactly two degrees are prime to \(p\). Here the two corresponding residues are allowed to have ratio in \(\mathbb F_p^\times\), as long as they are distinct.

## Assumptions and scope

All varieties and forms are over the algebraically closed field \(k\). Write \(S=\{i:p\mid d_i\}\), so \(|S|=r-2\ge 1\). Let \(a,b\) be the two indices outside \(S\). The logarithmic locus is the closure of foliations represented by

\[
\omega=\sum_{i=1}^r \lambda_i\frac{df_i}{f_i},\qquad \sum_{i=1}^r d_i\lambda_i=0,
\]

where \(f_i\) is homogeneous of degree \(d_i\) and the polar divisor \(D=\sum_i (f_i=0)\) is simple normal crossing. We prove an irreducible-component statement for the underlying reduced locus; we do not assert generic reducedness of the foliation scheme.

## Proof

**1. Choose residues.** Set \(\lambda_b=1\) and \(\lambda_a=-d_b/d_a\in\mathbb F_p^\times\). Since \(p\nmid(d_a+d_b)\), we have \(\lambda_a\ne\lambda_b\). For each \(i\in S\), choose \(\lambda_i\in k^\times\) so that the cosets \(\lambda_i\mathbb F_p^\times\) are pairwise distinct and different from \(\mathbb F_p^\times\). This is possible because \(k^\times/\mathbb F_p^\times\) is infinite. As \(d_i=0\) in \(k\) for \(i\in S\),

\[
\sum_i d_i\lambda_i=d_a\lambda_a+d_b\lambda_b=0.
\]

All residues are pairwise distinct. Moreover, for every index \(i\), there is an index \(j\) with \(\lambda_i/\lambda_j\notin\mathbb F_p\): for \(i\in S\) take \(j=a\); for \(i=a\) or \(b\), take any \(j\in S\). The latter ratios are outside \(\mathbb F_p\) because \(\lambda_a,\lambda_b\) lie in the same prime-field multiplicative coset while every \(\lambda_j\), \(j\in S\), lies in a different coset.

**2. Apply the Cartier-transform criterion.** Choose smooth hypersurfaces \(H_i=(f_i=0)\) in simple normal-crossing position and form the closed logarithmic projective \(1\)-form \(\omega=\sum_i\lambda_i\,df_i/f_i\). The residue relation above makes it projective. The exact hypothesis of Lemma 6.1 in Mendson–Pereira is that each component of the polar divisor has some other residue with ratio outside \(\mathbb F_p\); it does not require every pairwise ratio to lie outside \(\mathbb F_p\). Thus that lemma applies: the polar divisor equals the degeneracy divisor of the \(p\)-curvature, and the associated codimension-two subfoliation has degree one less than the foliation. In particular, the chosen foliation is \(p\)-dense.

**3. Use the deformation argument.** The proof of Theorem 6.2 in the same paper shows that in an open neighborhood of this foliation within any irreducible component containing it, the degeneracy divisor remains reduced and normal crossing in codimension two, and nearby foliations are represented by closed logarithmic forms. Their polar divisors have the same total degree. Since the original residues are pairwise distinct, their distinct residue values persist locally. The argument in that theorem then gives both inequalities for the number of polar components, hence exactly \(r\), and identifies each degree \(d_i\) by the number of points of that residue on a general line. The degrees can only decrease under the deformation while their sum stays fixed, so none decreases; the degree multiset is unchanged. Therefore a neighborhood in every component through the chosen foliation lies in \(\operatorname{Log}_{(d_1,\ldots,d_r)}\). Since this logarithmic locus is irreducible, it is an irreducible component.

The only modification to the published proof is the residue choice in Step 1: the pair \((\lambda_a,\lambda_b)\) has ratio in \(\mathbb F_p^\times\) but the non-collision condition makes the two residues distinct. The Cartier-transform and deformation steps use the weaker per-component condition and distinctness, not pairwise ratios outside \(\mathbb F_p\).

## Verification

The residue construction was checked algebraically: the weighted sum vanishes, all residues are nonzero and distinct, and every divisor component has a nonzero Cartier-wedge coefficient with at least one other component. The proof uses the full text of Mendson–Pereira, especially the definition of logarithmic loci, Lemma 6.1, Corollary 5.2, Corollary 5.4, and the proof of Theorem 6.2. No finite experiment is used as a substitute for the geometric argument.

## Relationship to prior work

Mendson–Pereira, Theorem A / Theorem 6.2, proves componentness when \(|S|\ne r-1,r-2\) for \(r>2\), while noting that the logarithmic locus is empty when all but one degree are divisible by \(p\). The present claim fills the subcase \(|S|=r-2\) in which the two degrees not divisible by \(p\) have sum not divisible by \(p\). It is a direct refinement of the residue-selection step in their proof, not a new classification of all positive-characteristic foliations. Calvo–Andrade's classical result concerns characteristic zero and does not settle this positive-characteristic case.

## Limitations

The argument does not cover \(p\mid(d_a+d_b)\), where the residue relation forces \(\lambda_a=\lambda_b\) and the distinct-residue argument fails. It does not establish generic reducedness, classify the remaining exceptional cases, or rule out every unpublished or unindexed treatment. The result is a proof-level extension of an existing theorem and has not received independent mathematical audit.

## References

1. Wodson Mendson and Jorge Vitório Pereira, “The space of foliations on projective spaces in positive characteristic,” arXiv:2504.12910v2 (first posted 17 April 2025; revised 6 July 2026), especially §4.4, Corollaries 5.2 and 5.4, Lemma 6.1, and Theorem 6.2. Full text: https://arxiv.org/html/2504.12910v2
2. Wodson Mendson and Jorge Vitório Pereira, “Codimension one foliations in positive characteristic,” *Journal of the Institute of Mathematics of Jussieu* 23 (2024), 1705–1750. DOI: https://doi.org/10.1017/S1474748023000361
3. J. V. Pereira and J. P. dos Santos, “Distributions with locally free tangent sheaf,” arXiv:2408.10057 (2024), Theorem B. https://arxiv.org/abs/2408.10057
4. Omegar Calvo-Andrade, “Irreducible components of the space of holomorphic foliations,” *Mathematische Annalen* 299 (1994), 751–767. This is characteristic-zero background only.
