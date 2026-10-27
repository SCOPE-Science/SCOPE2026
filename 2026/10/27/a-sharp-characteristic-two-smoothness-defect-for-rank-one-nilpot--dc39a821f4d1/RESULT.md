# A sharp characteristic-two smoothness defect for rank-one nilpotent evolution algebras

## Finding

Let \(k\) be a field and \(n\geq 1\). On the \((n+1)\)-dimensional vector space \(N_n(k)=k e_1\oplus\cdots\oplus k e_n\oplus kz\), define a commutative product by \(e_i e_j=\delta_{ij}z\) and \(ze_i=z^2=0\). For \(n\geq2\), this is an indecomposable, non-perfect, nilpotent evolution algebra with one-dimensional annihilator and square. Its multiplication is \((u+az)(v+bz)=(u^Tv)z\).

**Theorem.** The affine automorphism group scheme \(\mathbf{Aut}(N_n)\) is smooth over \(k\) if and only if \(\operatorname{char}(k)\neq2\) or \(n=1\). More precisely, it has a natural functorial presentation
\[
\mathbf{Aut}(N_n)(R)=\left\{\begin{pmatrix}A&0\\ \ell&c\end{pmatrix}: A\in\operatorname{GL}_n(R),\;\ell\in R^{1\times n},\;c\in R^\times,\;A^TA=cI_n\right\}
\]
for every commutative \(k\)-algebra \(R\). In characteristic two its tangent and geometric dimensions are, respectively,
\[
\dim_k\operatorname{Der}(N_n)=n+\frac{n(n+1)}2,\qquad
\dim\mathbf{Aut}(N_n)_{\overline k}=n+\frac{n(n-1)}2+1.
\]
Thus the excess tangent dimension is exactly \(n-1\). For \(n\ge2\), a subgroup scheme \((\mu_2)^{n-1}\subseteq\mathbf{Aut}(N_n)\) supplies \(n-1\) explicit infinitesimal directions. The geometric reduced automorphism group is connected in characteristic two.

For every finite field \(\mathbb F_q\) of characteristic two, with \(q=2^f\), the exact number of automorphisms is
\[
|\operatorname{Aut}_{\mathbb F_q}(N_n)|=q^n(q-1)\begin{cases}
q^{m^2}\displaystyle\prod_{i=1}^{m}(q^{2i}-1),&n=2m+1,\\
q^{n-1+(m-1)^2}\displaystyle\prod_{i=1}^{m-1}(q^{2i}-1),&n=2m.
\end{cases}
\]
Empty products are one. These formulas include \(n=1\) and \(n=2\).

## Assumptions and scope

The algebra and its group scheme are defined over **every** field; smoothness is geometric. The order formula concerns finite fields of characteristic exactly two. The group scheme is represented by invertible matrices preserving multiplication after **all** commutative base changes; counting only field-valued automorphisms is insufficient to detect nonsmoothness. The similarity presentation is a known consequence of the bilinear-form description of this family and is included for completeness; the results assessed here are the characteristic boundary, sharp tangent excess, connected reduced group and all-rank finite-field automorphism counts.

## Proof

**1. Functorial automorphisms.** For any commutative \(k\)-algebra \(R\), write \(N_R=R^n\oplus Rz\). If \(a=(u,t)\) annihilates all \(e_i\), its \(i\)-th product is \(u_i z\); thus \(\operatorname{Ann}(N_R)=Rz\), even over nonreduced \(R\). Every automorphism has block form \(T=\begin{pmatrix}A&0\\\ell&c\end{pmatrix}\) with \(c\) and \(A\) invertible. Preservation of \(uv=(u^Tv)z\) is equivalent to \((Au)^T(Av)=c(u^Tv)\), equivalently \(A^TA=cI_n\). Conversely all such blocks are automorphisms. The free parameter \(\ell\) yields a vector-group factor of dimension \(n\).

**2. Tangent dimension.** Linearize at the identity over \(k[\epsilon]/(\epsilon^2)\), setting \(A=I+\epsilon X\), \(c=1+\epsilon h\), and \(\ell=\epsilon t\). The sole linear condition is \(X^T+X=hI_n\). In characteristic two the diagonal equations force \(h=0\), and the off-diagonal equations force \(X=X^T\), giving \(n(n+1)/2\) free entries plus \(n\) for \(t\). In characteristic different from two, the symmetric part of \(X\) is fixed by \(h\) and the skew part arbitrary, giving \(n(n-1)/2+1+n\) dimensions. In the latter case the defining equations have the expected constant Jacobian rank \(n(n+1)/2\) at the identity. Since this is an algebraic group, translates show smoothness everywhere.

**3. Geometric characteristic-two isometries.** Work over an algebraic closure \(K\) of a characteristic-two field and put \(b(u,v)=u^Tv\), \(w=(1,\ldots,1)^T\). Then \(b(v,v)=b(w,v)^2\). Every \(b\)-isometry \(g\) therefore satisfies \(b(w,gv)=b(w,v)\) because square roots are unique in a field; nondegeneracy yields \(gw=w\).

If \(n=2m+1\), then \(b(w,w)=1\) and \(K^n=Kw\perp W\), where \(W=w^\perp\) carries a nondegenerate alternating form. Restriction gives an isomorphism of geometric point groups \(O(I_n)(K)\cong\operatorname{Sp}_{2m}(K)\); the reduced geometric variety has dimension \(m(2m+1)=n(n-1)/2\).

If \(n=2m\), then \(b(w,w)=0\). Choose \(t\) with \(b(t,w)=b(t,t)=1\) (for instance \(t=e_1\)), and set \(U=(Kw+Kt)^\perp\). The form on \(U\) is nondegenerate alternating and has dimension \(n-2\). An arbitrary isometry fixing \(w\) is uniquely determined by \(B\in\operatorname{Sp}(U)\), \(v\in U\), and \(\alpha\in K\), via
\[
g(w)=w,\qquad g(u)=Bu+b(v,Bu)w\quad(u\in U),\qquad g(t)=t+v+\alpha w.
\]
Direct pairing checks show that every such map is an isometry and that every isometry has this form. Thus the reduced geometric isometry variety is \(K^{n-1}\times\operatorname{Sp}_{n-2}(K)\), of dimension \((n-1)+(m-1)(2m-1)=n(n-1)/2\). These descriptions also prove connectedness of the reduced isometry groups.

**4. Similitudes and smoothness.** For each geometric similitude \(A\) with multiplier \(c\in K^\times\), choose the unique \(s\in K^\times\) satisfying \(s^2=c\), and write \(A=sg\), \(g\in O(I_n)(K)\). This **pointwise** factorization gives geometric dimension \(1+n(n-1)/2\) for \(\mathbf{GO}(I_n)\); it is not asserted to be a separable or scheme-theoretic product. Including the shear parameters yields dimension \(n+1+n(n-1)/2\). Compared with Step 2, the tangent excess in characteristic two is exactly \(n-1\), so the group scheme fails the smoothness criterion for all \(n\ge2\). For \(n=1\), the equation is \(c=A^2\), and the scheme is \(\mathbb G_a\rtimes\mathbb G_m\), which is smooth. Geometric connectedness follows from the point parametrizations, the connectedness of symplectic groups, and the vector and multiplicative group factors.

Concretely, diagonal matrices \(A=\operatorname{diag}(t_1,\ldots,t_{n-1},1)\) with \(t_i^2=1\), \(c=1\), and \(\ell=0\) embed \((\mu_2)^{n-1}\) in the automorphism group scheme. Over characteristic two this is a nonreduced subgroup, and its \(n-1\) tangent directions remain linearly independent modulo the tangent space of the reduced geometric group (whose points fix \(w\) up to scalar).

**5. Finite-field orders.** Over \(\mathbb F_q\) of characteristic two the square map is bijective. Hence \(|GO(I_n)(\mathbb F_q)|=(q-1)|O(I_n)(\mathbb F_q)|\). The parametrizations in Step 3 give \(|O_{2m+1}|=|\operatorname{Sp}_{2m}(q)|\) and \(|O_{2m}|=q^{2m-1}|\operatorname{Sp}_{2m-2}(q)|\). Count ordered symplectic frames inductively: the first nonzero vector has \(q^{2m}-1\) choices, its symplectic mate has \(q^{2m-1}\) choices, and the complement contributes \(|\operatorname{Sp}_{2m-2}(q)|\). Therefore \(|\operatorname{Sp}_{2m}(q)|=q^{m^2}\prod_{i=1}^m(q^{2i}-1)\). Multiplication by the \(q^n\) choices for \(\ell\) yields the stated formula. No unverified finite-pattern extrapolation is involved.

## Verification

A standalone pure-Python verifier is included as `verify.py`. It separately enumerates all Gram similitudes \(A\) over \(\mathbb F_2\) for \(1\le n\le4\) and over \(\mathbb F_4\) for \(1\le n\le3\), compares the isometry/similitude counts against the formula, and checks the full automorphism count after multiplying by \(q^n\). It also computes the rank of the tangent constraint matrix in 44 cases with dimensions through 11 and characteristics 2, 3, 5, 7. Its terminal output is `VERIFY_OK finite_field_count_cases=7 tangent_cases=44 total_cases= 51`. The all-parameter assertion is supported by the preceding proof, not these finite tests.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (2026, arXiv:2610.22248v1) formulate smoothness of automorphism group schemes for non-perfect evolution algebras as Question 37; their Proposition 14 analyzes a **non-nilpotent** family with orthogonal symmetries. Hegazi and Abdelwahab (2015, arXiv:1508.06860v1, Lemma 15) previously described matrices for automorphisms of annihilator extensions, and Elduque and Labra (2016, arXiv:1602.01590v2, Definition 4.1 and Theorem 4.7(i)) previously described these rank-one nilpotent algebras using symmetric bilinear forms and similarities, working in characteristic different from two. Thus neither the algebra's construction nor the block-similitude condition is claimed new. The claimed addition is the all-rank modular smoothness criterion, exact infinitesimal excess, reduced-group geometry, and characteristic-two finite-field enumeration. Classical symplectic-group structure and order formulas are likewise used, not claimed as new results.

## Limitations

The smoothness classification is only for the specific rank-one nilpotent family, not all non-perfect evolution algebras. The finite-field count is stated only in characteristic two; the group scheme may have nontrivial infinitesimal automorphisms invisible in these counts. While the cited primary literature and mathematical-record comparisons did not identify an earlier all-rank packaged statement, a direct consequence recorded under classical modular bilinear-group schemes or a different evolution-algebra terminology remains a priority risk. Independent mathematical validation has not been performed.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public posting 2026-10-15), Proposition 14 and Question 37. https://arxiv.org/abs/2610.22248
2. A. S. Hegazi and H. Abdelwahab, *Nilpotent evolution algebras over arbitrary fields*, arXiv:1508.06860v1 (2015), Lemma 15. https://arxiv.org/abs/1508.06860
3. A. Elduque and A. Labra, *On nilpotent evolution algebras*, arXiv:1602.01590v2 (2016), Definition 4.1 and Theorem 4.7. https://arxiv.org/abs/1602.01590
