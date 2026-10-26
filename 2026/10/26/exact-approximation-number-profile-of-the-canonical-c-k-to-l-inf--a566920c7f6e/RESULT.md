# Exact approximation-number profile of the canonical \(C(K)\)-to-\(L^\infty(\mu)\) inclusion

## Finding

Let \(K\) be compact Hausdorff, let \(\mu\) be a finite positive regular Borel measure on \(K\), and put \(F=\operatorname{supp}\mu\). For the canonical operator
\[
J_\mu:C(K)\longrightarrow L^\infty(\mu),\qquad J_\mu f=[f],
\]
write
\[
a_n(J_\mu)=\inf\{\|J_\mu-R\|:\operatorname{rank}R<n\},\qquad n\ge1.
\]
Then the complete approximation-number profile is
\[
\boxed{\displaystyle a_n(J_\mu)=\begin{cases}1,&|F|\ge n,\\0,&|F|<n.\end{cases}}
\]
In particular, if the support is infinite, every finite-index approximation number and the essential norm equal \(1\). If the support has exactly \(m<\infty\) points, the operator has rank \(m\), its first \(m\) approximation numbers equal \(1\), and all later ones vanish.

## Assumptions and scope

The scalar field may be real or complex. The measure is finite, positive, and regular; \(L^\infty(\mu)\) uses the essential-supremum norm. The zero measure is included: its support is empty and \(J_\mu=0\). No metric or metrizability assumption on \(K\) is required. The result concerns this canonical inclusion only, not arbitrary operators into \(L^\infty\), vector-valued targets, entropy numbers, or ball measures of noncompactness.

## Proof

If \(|F|\ge n\), choose distinct points \(x_1,\ldots,x_n\in F\). Since a compact Hausdorff space is normal, choose pairwise disjoint open neighborhoods \(U_j\) of these points and smaller open neighborhoods \(V_j\) with \(x_j\in V_j\), \(\overline{V_j}\subset U_j\). By the definition of support, \(\mu(V_j)>0\). Urysohn's lemma gives \(f_j\in C(K)\) with \(0\le f_j\le1\), \(f_j=1\) on \(\overline{V_j}\), and support contained in \(U_j\). Hence \(\|J_\mu f_j\|_\infty=1\).

The supports are pairwise disjoint, so for all scalars \(c_1,\ldots,c_n\),
\[
\left\|\sum_{j=1}^n c_jf_j\right\|_{C(K)}=\max_j|c_j|
=\left\|J_\mu\left(\sum_{j=1}^n c_jf_j\right)\right\|_{L^\infty(\mu)}.
\]
Thus \(J_\mu\) is isometric on the \(n\)-dimensional space \(E_n=\operatorname{span}\{f_1,\ldots,f_n\}\). For any operator \(R\) of rank less than \(n\), the restriction \(R|_{E_n}\) has a nonzero kernel. Choose \(f\in E_n\) with \(\|f\|=1\) and \(Rf=0\). Then
\[
\|J_\mu-R\|\ge\|(J_\mu-R)f\|=\|J_\mu f\|_\infty=1.
\]
Since \(\|J_\mu\|=1\) for every nonzero \(\mu\), taking \(R=0\) gives \(a_n(J_\mu)\le1\), and therefore \(a_n(J_\mu)=1\). When \(\mu=0\), the claimed formula gives zero directly.

If \(|F|=m<n\), regularity implies \(\mu(K\setminus F)=0\); because \(F\) is finite, \(L^\infty(\mu)\) is \(m\)-dimensional and \(J_\mu\) has rank at most \(m<n\). Hence \(a_n(J_\mu)=0\). This proves the formula in all cases.

## Verification

The proof uses only normality of compact Hausdorff spaces, Urysohn's lemma, the support property of a regular measure, and rank-nullity for finite-dimensional spaces. No numerical computation or finite experiment is used. The lower bound is established separately for every finite index \(n\), so it is not inferred from an asymptotic limit.

## Relationship to prior work

The literature on operators from \(C(K)\)-spaces uses disjointly supported continuous functions to detect non-weak compactness; see the discussion and results in arXiv:1211.2770v1. The present statement gives a sharper, exact finite-rank approximation profile for the specific measure inclusion into \(L^\infty(\mu)\), rather than only a compactness or weak-compactness criterion. Work on maximal noncompactness of Sobolev embeddings, including arXiv:2003.11854v1, emphasizes that \(L^\infty\) endpoints can differ sharply from finite-exponent targets, but it studies different source spaces and a different noncompactness invariant. The comparison does not assert that either source contains this exact formula.

## Limitations

The theorem does not give approximation numbers for general weighted composition operators, arbitrary quotient maps, or embeddings into \(L^p(\mu)\) for finite \(p\). A search of the accessible literature and literature records did not locate this exact support-cardinality formula; absence of a match is not a proof of historical priority. The proof is elementary, so an unindexed equivalent corollary remains a priority risk.

## References

1. *A chain condition for operators from \(C(K)\)-spaces*, arXiv:1211.2770v1, first publicly posted 2012-11-12. Full text read for the disjoint-support and weak-compactness context.
2. J. Lang, V. Musil, M. Olšák, and L. Pick, *Maximal non-compactness of Sobolev embeddings*, arXiv:2003.11854v1 (2020). Abstract-level context only; its operator family is different.
