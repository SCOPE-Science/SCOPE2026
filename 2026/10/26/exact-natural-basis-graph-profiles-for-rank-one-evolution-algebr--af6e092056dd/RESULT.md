# Exact natural-basis graph profiles for rank-one evolution algebras over odd finite fields

## Finding
Let \(q\) be an odd prime power, \(n\ge 2\), and \(E\) a nondegenerate \(n\)-dimensional evolution algebra over \(\mathbb F_q\) with \(\dim E^2=1\). Fix a nonzero generator \(v\) of \(E^2\), and write \(xy=B(x,y)v\), where \(B\) is a nondegenerate symmetric bilinear form. Set \(c=B(v,v)\), \(\delta=\chi(\det B)\in\{\pm1\}\), and \(\varepsilon=\chi(-1)\), with \(\chi\) the quadratic character extended by \(\chi(0)=0\).

For \(j\ge1\), define
\[
 A_j(c)=\begin{cases}
 \big((q-1)^j+(q-1)(-1)^j\big)/q,&c=0,\\
 \big((q-1)^j-(-1)^j\big)/q,&c\ne0,
 \end{cases}
\]
and, for \(n\ge2\), define
\[
 G_n(c)=\begin{cases}
 \varepsilon^{n/2}q^{n/2-1}(q-1),&n\text{ even},\ c=0,\\
 -\varepsilon^{n/2}q^{n/2-1},&n\text{ even},\ c\ne0,\\
 0,&n\text{ odd},\ c=0,\\
 \chi(c)\varepsilon^{(n-1)/2}q^{(n-1)/2},&n\text{ odd},\ c\ne0.
 \end{cases}
\]
Put \(T=q^{n-1}-\mathbf1_{c=0}+\delta G_n(c)\), which is positive for the given algebra. For a uniformly chosen **ordered natural basis** \(\mathcal B\), let \(K(\mathcal B)\) be the number of vertices with positive indegree in its directed graph. Then
\[
 \boxed{\Pr(K=k)=
 \begin{cases}
 \displaystyle\binom nk\frac{A_k(c)}{T},&1\le k<n,\\[4pt]
 \displaystyle\frac{A_n(c)+\delta G_n(c)}{T},&k=n.
 \end{cases}}
\]
Every basis graph is a digraph \(H_{n,k}\) having all \(n\) vertices pointing to a common set of \(k\) vertices, including the \(k\) loops. These \(n\) graph types are pairwise nonisomorphic. The total number of ordered natural bases is \(\frac{(q-1)^n}{2}|O(B)|\); multiplying by the displayed probabilities gives the exact number of bases of each graph type.

The attainable graph types admit a sharp description: \(k=1\) occurs precisely when \(c\ne0\); every \(2\le k<n\) occurs; and \(k=n\) occurs except for exactly the following feasible parameter regimes:
\[
 (q,n,c\ne0,\delta)=(3,2,\text{true},-1),\qquad
 (q,n,c\ne0,\delta\chi(c))=(3,3,\text{true},1),\qquad
 (q,n,c=0,\delta)=(3,4,\text{true},-1).
\]
The qualifications “feasible” mean that the specified \((B,v)\) exists, equivalently \(T>0\); all three exclusions are realized by actual algebras. Under a rescaling of the chosen generator \(v\), the right-hand sides remain unchanged, so the distribution is intrinsic to the algebra rather than the choice of generator.

## Assumptions and scope
A *natural basis* means an ordered vector-space basis \((e_1,\ldots,e_n)\) such that \(e_ie_j=0\) for distinct indices. The graph has an arc \(i\to j\) exactly when the coefficient of \(e_j\) in \(e_i^2\) is nonzero, including loops. “Uniform” means equal weight for each ordered basis, not for natural bases modulo rescaling, permutation, or algebra automorphisms. An evolution algebra is *nondegenerate* if its annihilator is zero. The claim holds for any odd prime power \(q\) (not merely prime \(q\)), all \(n\ge2\), and all nondegenerate rank-one-square evolution algebras. It does not address characteristic two, annihilator-bearing algebras, or higher-dimensional squares.

The expression \(xy=B(x,y)v\) is possible because \(E^2=\mathbb F_qv\). It is symmetric because the algebra is commutative. Its radical equals the annihilator; thus \(B\) is nondegenerate. A basis is natural precisely when it is \(B\)-orthogonal, and each diagonal \(B(e_i,e_i)\) must be nonzero. Write \(v=\sum_iw_ie_i\); then \(e_i^2=B(e_i,e_i)\sum_jw_je_j\), so its arrows are exactly the indices \(j\) where \(w_j\ne0\). Thus \(K\) is the support size of \(v\) in the natural basis, always at least one.

## Proof
**1. Replace bases by diagonal presentations.** For each tuple \(b=(b_1,\ldots,b_n)\in(\mathbb F_q^*)^n\) with \(\chi(\prod b_i)=\delta\), let \(D_b\) be the diagonal bilinear form with entries \(b_i\). The standard classification of nondegenerate symmetric forms over odd finite fields shows \(D_b\simeq B\). There are \((q-1)^n/2\) such tuples; for each, exactly \(|O(B)|\) isometries from \(D_b\) to \(B\), each giving an ordered natural basis and uniquely recording its diagonal values. Hence there are \((q-1)^n|O(B)|/2\) ordered natural bases.

Write \(w\) for the coordinates of the fixed nonzero vector \(v\) under such an isometry. They satisfy \(\sum_i b_iw_i^2=c\) and \(w\ne0\). Witt's extension theorem implies that the isometry group acts transitively on nonzero vectors of each fixed norm \(c\), including the isotropic orbit when it exists. Consequently, for each admissible \(b\), every such nonzero \(w\) occurs equally often among the associated isometries. Therefore relative frequencies can be counted by pairs \((b,w)\) satisfying the norm equation and determinant-square-class restriction. This step does **not** identify a finite experiment with an infinite proof.

**2. Count non-full supports.** Fix a support \(S\subsetneq\{1,\ldots,n\}\), of cardinality \(k\ge1\). Put \(a_i=b_iw_i^2\) for \(i\in S\). Every \(a_i\) is nonzero and \(\sum_{i\in S}a_i=c\). For each such \(a\), the \(k\) nonzero coordinates \(w_i\) may be chosen in \((q-1)^k\) ways; each choice determines the corresponding \(b_i\). The remaining \(n-k\ge1\) diagonal entries can be chosen in \((q-1)^{n-k}/2\) ways subject to \(\chi(\prod b_i)=\delta\). Thus the number of pairs for this particular support is exactly \((q-1)^n A_k(c)/2\), independent of its location. Summing over all supports gives \(\binom nk(q-1)^n A_k(c)/2\).

**3. Count full support.** When \(k=n\), the discriminant restriction becomes \(\chi(\prod a_i)=\delta\) because multiplication by nonzero squares does not change quadratic characters. Every admissible \(a\) gives \((q-1)^n\) choices of \(w\) and uniquely determines \(b\). The number of full-support pairs is therefore
\[
 \frac{(q-1)^n}{2}\big(A_n(c)+\delta G_n(c)\big),
\]
where \(G_n(c)=\sum_{a_i\ne0,\sum_i a_i=c}\chi(\prod_i a_i)\).

**4. Evaluate both character sums.** Additive-character orthogonality gives \(A_j(0)=((q-1)^j+(q-1)(-1)^j)/q\) and \(A_j(c\ne0)=((q-1)^j-(-1)^j)/q\). For a nontrivial additive character \(\psi\) define \(\mathcal G=\sum_{a\ne0}\chi(a)\psi(a)\). Then \(\mathcal G^2=\varepsilon q\), and
\[
 G_n(c)=\frac1q\sum_{t\ne0}\psi(-tc)\chi(t)^n\mathcal G^n.
\]
If \(n\) is even, the remaining character sum equals \(q-1\) for \(c=0\) and \(-1\) otherwise. If \(n\) is odd, it vanishes for \(c=0\), while for \(c\ne0\) it equals \(\chi(-c)\mathcal G\). This proves the displayed four cases for \(G_n\) for all odd prime powers.

**5. Normalize and classify realization.** Summing pair counts for \(1\le k\le n\) gives \((q-1)^nT/2\), because \(\sum_{k=1}^n\binom nk A_k(c)=q^{n-1}-\mathbf1_{c=0}\). This total is positive for the existing \((B,v)\); dividing proves the probability formula. For \(k=1\), \(A_1(c)\) is one if \(c\ne0\) and zero otherwise. For \(2\le k<n\), \(A_k(c)>0\) for any odd \(q\). Full support fails precisely when \(A_n(c)+\delta G_n(c)=0\), and since \(A_n(c)\ge0\), it requires \(A_n(c)=|G_n(c)|\). Substitution of the explicit formulas shows this equality only in the three regimes stated: for \(q=3\), \(n=2\) with \(c\ne0\), \(n=3\) with \(c\ne0\), and \(n=4\) with \(c=0\), with the displayed discriminant signs. For \(q\ge5\), direct comparison using \((q-1)^n\) versus the terms of size at most \((q-1)q^{n/2-1}\) is strict except for an inadmissible zero-norm anisotropic plane; for \(q=3\), direct checks at \(n=5,6\) and the recurrence in increments of two yield strictness thereafter. The exceptional cases are realized by \(B=\operatorname{diag}(1,2),v=(1,0)\) at \(n=2\); \(B=I_3,v=(1,0,0)\) at \(n=3\); and \(B=\operatorname{diag}(1,1,1,2),v=(1,1,1,0)\) at \(n=4\), all over \(\mathbb F_3\).

Finally, replacing \(v\) by \(\lambda v\) replaces \(B\) by \(\lambda^{-1}B\), hence \(c\) by \(\lambda c\) and \(\delta\) by \(\chi(\lambda)^{-n}\delta\). In even dimension \(\delta\) is fixed and all the expressions only distinguish \(c=0\) from \(c\ne0\). In odd dimension the relevant nonzero invariant \(\delta\chi(c)\) is fixed. Thus the distribution is independent of the generator of \(E^2\). This completes the proof.

## Verification
The standalone `verify.py` uses only standard Python and independently enumerates every nonzero diagonal tuple \(b\) of the required discriminant, every nonzero coordinate vector \(w\), and the resulting norm and support. It compares exact integer counts against the formulas for \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9\) in dimensions \(2\) through \(5\) (the largest dimension depending on field size), including all \(128\) feasible parameter combinations. The implementation of \(\mathbb F_9\) uses the irreducible relation \(u^2=2\) over \(\mathbb F_3\). Additionally it independently enumerates ordered orthogonal bases of four small fixed forms, solves for the coordinates of \(v\), and checks probabilities; the four base counts are \(8,192,192,64\). Execute `python3 verify.py` in the directory containing this document. The final line is `VERIFY_OK table_cases= 12 parameter_types= 128 actual_form_cases= 4`. Finite tests do not establish the general theorem; the preceding proof does.

## Relationship to prior work
Kaygorodov, Martín González and Viruel, *Evolution algebras: a survey of results and a list of open problems* (arXiv:2610.22248v1, publicly submitted October 15, 2026), Question 27, explicitly asks for basis-independent graph information in nondegenerate evolution algebras and their natural classes. The present result gives a fully evaluated **distribution of graph types as the natural basis varies**, a stronger quantitative profile than merely listing possible graphs, for one natural infinite family.

Martín Barquero, Martín González and Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square* (Mediterranean Journal of Mathematics 22 (2025), article 48, DOI:10.1007/s00009-025-02812-7), Theorems and discussion in Sections 3–4, supplies the underlying bilinear-form classification and the use of isometries/Witt extension; those are credited ingredients, not novelty claims. Its full accessible text does not enumerate digraph supports or their finite-field natural-basis frequencies. General algebraic classifications and finite-field quadratic-form counting alone do not state this joint graph-profile distribution without the present support/discriminant analysis. The related *Natural families in evolution algebras* (arXiv:2006.14460) discusses extensions and classification of natural families; full-text access was unsuccessful and remains an originality risk. Accessible mathematical research records related to rank-one evolution algebras, including a two-dimensional natural-basis orbit census, do not include this all-dimensional, exact graph-support frequency theorem.

## Limitations
This theorem concerns *ordered* natural bases; weighting their equivalence classes uniformly would give a different distribution. The underlying classical form classification and quadratic Gauss sum are standard. The only claimed new content is the resulting complete graph-type profile, exact multiplicities, and finite-field realization boundary for this algebra family. It does not address characteristic two, arbitrary evolution algebras, graph invariants outside the rank-one-square class, or automorphism-orbit-weighted graph frequencies. Relevant unavailable full texts and unindexed literature could contain equivalent results; no independent external audit is claimed.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (October 15, 2026), especially Question 27. https://arxiv.org/html/2610.22248v1
2. D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square*, Mediterranean Journal of Mathematics 22, article 48 (2025). https://doi.org/10.1007/s00009-025-02812-7
3. Y. Cabrera Casado et al., *Natural families in evolution algebras*, arXiv:2006.14460 (2020), related work with full text not inspected here. https://arxiv.org/abs/2006.14460
