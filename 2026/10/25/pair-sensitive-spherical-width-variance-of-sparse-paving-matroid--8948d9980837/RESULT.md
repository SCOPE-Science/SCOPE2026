# Pair-sensitive spherical width variance of sparse-paving matroid polytopes

## Finding
For integers \(n\ge4\) and \(2\le k\le n-2\), let \(\mathcal F\subseteq\binom{[n]}k\) consist of \(m\) distinct sets such that no two members intersect in \(k-1\) elements. Let \(P_{\mathcal F}\) be the convex hull of the indicator vectors of all \(k\)-subsets outside \(\mathcal F\). These are rank-\(k\) sparse-paving matroid base polytopes. Write \(\Delta_{k,n}\) for the full hypersimplex and \(W_K(U)=h_K(U)+h_K(-U)\) for width in a Haar-uniform unit direction \(U\) of the common zero-sum direction space \(\{u:\sum_i u_i=0\}\).

Set
\[
\ell=\max(0,2k-n),\qquad N=\binom nk,\qquad L=\binom k\ell\binom{n-k}{k-\ell},
\]
and define the *compatible-pair count*
\[
C(\mathcal F)=\#\{(A,B)\in\mathcal F^2:|A\cap B|=\ell\}.
\]
Let \(G_1,\ldots,G_n\) be independent standard Gaussians, with decreasing order statistics \(G_{(1)}>\cdots>G_{(n)}\), and put
\[
R^2=\sum_{i=1}^n(G_i-\overline G)^2,\quad
S_+=\frac{G_{(k)}-G_{(k+1)}}R,\quad
S_-=\frac{G_{(n-k)}-G_{(n-k+1)}}R,\quad
\gamma_{n,k}=\mathbb E[S_+S_-]>0.
\]
For any two such families \(\mathcal F,\mathcal F'\) of the same size \(m\), their polytopes have **exactly equal spherical mean widths**, whereas
\[
\boxed{\operatorname{Var}(W_{P_{\mathcal F}}(U))-
\operatorname{Var}(W_{P_{\mathcal F'}}(U))
=\frac{2\gamma_{n,k}}{NL}\bigl(C(\mathcal F)-C(\mathcal F')\bigr).}
\]
Thus the second spherical width moment detects a pair-intersection statistic that the number of circuit-hyperplanes alone does not detect.

In particular, on \([6]\) at rank \(3\), take
\[
\mathcal F_{\mathrm c}=\{\{1,2,3\},\{4,5,6\}\},\qquad
\mathcal F_{\mathrm i}=\{\{1,2,3\},\{3,4,5\}\}.
\]
Their base polytopes have the same Ehrhart polynomial, the same Euclidean volume, and the same spherical mean width; nonetheless,
\[
\boxed{\operatorname{Var}(W_{P_{\mathcal F_{\mathrm c}}}(U))-
\operatorname{Var}(W_{P_{\mathcal F_{\mathrm i}}}(U))
=\frac15\mathbb E\left[\frac{(G_{(3)}-G_{(4)})^2}{\sum_i(G_i-\overline G)^2}\right]>0.}
\]
The underlying width-defect distributions are exactly \(2S B_{1/10}\) and \(S B_{1/5}\), respectively, where \(S=(G_{(3)}-G_{(4)})/R\), and each Bernoulli variable is independent of \(S\). This last statement describes each width defect relative to the hypersimplex, not the width itself.

## Assumptions and scope
The ambient metric is the standard Euclidean metric restricted to the \((n-1)\)-dimensional zero-sum subspace. All widths use the same Haar-uniform intrinsic unit direction; no independent direction is introduced when comparing two polytopes. The sets in \(\mathcal F\) are pairwise nonadjacent in the Johnson graph, meaning their intersections have size at most \(k-2\). The rank, size, and pair count are combinatorial; \(\gamma_{n,k}\) depends only on \(n,k\) and is an exact finite Gaussian expectation.

## Proof
**Matroid structure.** The allowed \(k\)-sets satisfy basis exchange. Given allowed bases \(A,B\) and \(a\in A\setminus B\), the exchanges \(A-\{a\}+\{b\}\), indexed by \(b\in B\setminus A\), are pairwise adjacent in the Johnson graph. At most one can lie in \(\mathcal F\). If there is only one candidate, it is \(B\), already allowed; otherwise at least one candidate is allowed. Every \((k-1)\)-set extends to an allowed basis and every \((k+1)\)-set contains an allowed basis, since all their constituent \(k\)-sets are pairwise adjacent. Consequently each member of \(\mathcal F\) is a circuit-hyperplane and every other \(k\)-set is a basis, so the matroid is sparse paving.

**Exact support defect.** For distinct real scores \(g_1,\ldots,g_n\), the hypersimplex maximizer is the indicator vector of the indices of its \(k\) largest scores. If this set is allowed, the two support functions agree. If it is forbidden, all its one-element-swap neighbors are allowed by Johnson nonadjacency; among all other \(k\)-sets the best is the swap of the \(k\)th with the \((k+1)\)th score. The support deficit is therefore exactly their gap. The same argument applied to negative scores gives the lower-tail gap. The Gaussian construction \(U=(G-\overline G\mathbf1)/R\) is uniform on the intrinsic unit sphere, and subtracting \(\overline G\) changes no ranking or support difference. Denote the upper and lower \(k\)-sets by \(T_+,T_-\). Almost surely,
\[
W_{\Delta_{k,n}}(U)-W_{P_{\mathcal F}}(U)
=S_+\mathbf1_{\{T_+\in\mathcal F\}}+S_-\mathbf1_{\{T_-\in\mathcal F\}}.
\tag{1}
\]

**Rank permutation and moments.** The random permutation of Gaussian labels is uniform and independent of their sorted numerical values; therefore both \(S_+,S_-\), and \(W_{\Delta_{k,n}}(U)\), are independent of the labeled pair \((T_+,T_-)\). Each of \(T_+,T_-\) is uniform among the \(N\) subsets. Their intersection has exactly \(\ell\) labels, and the ordered pair is uniform among the \(NL\) possibilities with this intersection size. Write \(p=m/N\) and \(c=C(\mathcal F)/(NL)\). Equation (1) gives
\[
\mathbb E D_{\mathcal F}=2p\mathbb E S_+,
\qquad \mathbb E D_{\mathcal F}^{2}
=2p\mathbb E S_+^{2}+2c\gamma_{n,k},
\]
where \(D_{\mathcal F}=W_{\Delta_{k,n}}-W_{P_{\mathcal F}}\). Reflection symmetry identifies the upper and lower marginal moments. Further,
\[
\mathbb E[W_{\Delta_{k,n}} D_{\mathcal F}]
=2p\mathbb E[W_{\Delta_{k,n}}S_+].
\]
The mean widths are therefore functions of \(n,k,m\) alone; when \(m\) is fixed, the two mean-width and mixed-moment terms cancel in the variance comparison. The only remaining term is \(2\gamma_{n,k}(C(\mathcal F)-C(\mathcal F'))/(NL)\), proving the formula. Each spacing is almost surely positive and bounded by \(\sqrt2R\), so \(0<\gamma_{n,k}<\infty\).

**Six-element separation and Ehrhart equality.** For \(n=6,k=3\), one has \(N=20\), \(\ell=0\), \(L=1\), and \(S_+=S_-=S\). The two forbidden triples are complements in \(\mathcal F_{\mathrm c}\), giving \(C(\mathcal F_{\mathrm c})=2\); the forbidden triples intersect in one index in \(\mathcal F_{\mathrm i}\), giving \(C(\mathcal F_{\mathrm i})=0\). This yields the displayed positive difference. Uniformity of \(T_+\) shows that the defect is \(2S\) for two of its \(20\) possible values in the complementary case, and \(S\) for four possible values in the intersecting case. Finally, both are sparse-paving rank-three matroids with precisely two circuit-hyperplanes. Ferroni's sparse-paving Ehrhart formula, also recalled as Proposition 7.12 in Ferroni and Schröter, depends only on \(n,k,m\). Hence the two polytopes have equal Ehrhart polynomials and, in particular, equal Euclidean volumes.

## Verification
The included `verify_sparse_paving.py` independently enumerates support-function maxima over all allowed and all hypersimplex vertices. It verifies the one-swap formula for 13,800 strict-score comparisons from several ranks and sizes. For the six-element examples it examines all \(6!=720\) score permutations and obtains exact defect-class counts \((648,72)\) at multipliers \((0,2)\), versus \((576,144)\) at multipliers \((0,1)\). With fixed sorted centered scores \((3,2,1,-1,-2,-3)\), the conditional width-variance difference is exactly \(1/35\). Direct Ehrhart-point enumeration through the fifth dilate gives equal sequences \(18,121,488,1459,3590\) for the two examples. The infinite-dimensional or all-size assertions rest on the preceding proof, not on finite numerical tests.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez, and Yin explain the hypersimplex-slicing description of paving-matroid polytopes and the corresponding Ehrhart formulas. Ferroni and Schröter establish that all valuative invariants of sparse-paving matroids of fixed rank and size are controlled by the number of circuit-hyperplanes, and explicitly state the Ehrhart formula. The present result does not claim this previously known Ehrhart or valuative invariance as new. Instead it isolates the first pair-sensitive correction to **squared spherical directional width**, a non-linear metric statistic not specified by those formulas. Faustini and Vargas identify pairwise data in a different, combinatorial non-valuative invariant (the cd-index); their result does not compute spherical width moments.

## Limitations
The precise coefficient \(\gamma_{n,k}\) is supplied as a positive, finite Gaussian expectation; no elementary closed evaluation is claimed. The general statement concerns sparse-paving base polytopes in their canonical coordinate metric, not arbitrary affine realizations or arbitrary matroids. Equality of Ehrhart polynomials uses a published formula, with independent low-dilate counts as a check rather than an all-dilate replacement proof. No independent mathematical audit has been performed. A directly covering treatment in less-indexed geometric-probability literature remains possible.

## References
1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (first publicly available January 28, 2022), especially Sections 2, 5, and 8. https://arxiv.org/abs/2201.12442
2. L. Ferroni and B. Schröter, *Valuative Invariants for Large Classes of Matroids*, arXiv:2208.04893 (first publicly available August 9, 2022); *Journal of the London Mathematical Society* 110 (2024), e12984, Corollary 5.4 and Proposition 7.12. https://doi.org/10.1112/jlms.12984
3. T. Faustini and A. Vargas, *Almost-valuative Invariants of Connected Split Matroids: The cd-index*, arXiv:2512.05250 (December 4, 2025), introduction and main structural statement. https://arxiv.org/abs/2512.05250
