# Prime decomposition and nodal strata of star-structured symmetric determinantal hypersurfaces

## Finding
For every integer \(m\ge3\) and every algebraically closed field \(k\) of characteristic different from two, consider the symmetric arrowhead matrix
\[
A_m=\begin{pmatrix}
a_0&b_1&b_2&\cdots&b_m\\
b_1&a_1&0&\cdots&0\\
b_2&0&a_2&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
b_m&0&0&\cdots&a_m
\end{pmatrix}.
\]
Let \(X_m\subset\mathbb P^{2m}\) be the hypersurface cut out by \(F=\det A_m\), and let \(I_m(A_m)\) be the ideal of all size-\(m\) minors of this size-\((m+1)\) matrix. For each leaf \(i\), let \(F_i\) denote the determinant of the principal matrix obtained by removing leaf \(i\). Set
\[
Z_i=V(a_i,b_i,F_i),\qquad L_T=V(a_i:i\in T)\quad (T\subseteq\{1,\dots,m\},\ |T|=3).
\]
Then the **scheme-theoretic prime decomposition** is
\[
I_m(A_m)=\bigcap_{i=1}^m(a_i,b_i,F_i)\ \cap\ \bigcap_{|T|=3}(a_i:i\in T).
\]
In particular, the **entire reduced singular locus** of \(X_m\) consists of exactly \(m+\binom m3\) pairwise distinct irreducible components: \(m\) codimension-three complete intersections \(Z_i\) of degree \(m\), and \(\binom m3\) codimension-three linear spaces \(L_T\) of degree one. Every component has dimension \(2m-3\), and a general point of each has a transverse ordinary surface node \(uv-w^2=0\). Consequently,
\[
\deg\operatorname{Sing}(X_m)_{\mathrm{red}}=m^2+\binom m3=\binom{m+2}{3}.
\]
The hypersurface \(X_m\) is irreducible and normal.

## Assumptions and scope
All projective spaces and schemes are over an algebraically closed field \(k\) with \(\operatorname{char}k\ne2\). We use the standard grading on \(R=k[a_0,a_1,\dots,a_m,b_1,\dots,b_m]\), so \(\deg a_i=\deg b_i=1\). For \(1\le i\le m\), put \(P_i=\prod_{j\ne i}a_j\), where the product ranges over leaf indices. The basic determinant identity is
\[
F=a_0\prod_{i=1}^m a_i-\sum_{i=1}^m b_i^2 P_i=a_iF_i-b_i^2P_i.
\]
A *general transverse ordinary surface node* means an étale-locally (or formally) nonsingular factor times the hypersurface germ \(uv-w^2=0\), over the generic point of the specified singular component. We classify the support and the radical size-\(m\)-minor ideal; the possibly nonreduced Jacobian ideal is not claimed to equal that minor ideal.

## Proof
**Irreducibility.** Regard \(F\) as a primitive polynomial of degree one in \(a_0\). Its leading coefficient is \(\prod_i a_i\). For each \(i\), reducing its constant term modulo \(a_i\) gives \(-b_i^2\prod_{j\ne i}a_j\), which is nonzero. Thus leading and constant coefficients are coprime in the polynomial ring in all other variables. Gauss's lemma gives irreducibility of \(F\). Identical reasoning proves irreducibility of each \(F_i\), which has at least two surviving leaves for \(m\ge3\). Therefore the ideals \((a_i,b_i,F_i)\) are prime. The ideals \((a_i:i\in T)\) are clearly prime; all have height three.

**Singular points are exactly the rank-deficient matrices.** For a symmetric matrix \(A\) of rank \(m\), its nonzero adjugate is a scalar times \(vv^t\), where \(0\ne v\) spans its kernel. Hence some diagonal cofactor is nonzero, since at least one \(v_i^2\ne0\). Every diagonal variable is independent, and the corresponding partial derivative of \(\det A\) equals that cofactor. Thus a rank-\(m\) point of \(X_m\) is smooth. At rank at most \(m-1\) all size-\(m\) minors, hence all first derivatives, vanish. This shows the singular support equals \(V(I_m(A_m))\).

**Full rank stratification.** At any point let \(S\) be the set of zero leaf diagonals, with \(r=|S|\). Eliminate the nonzero leaf diagonal block by invertible row/column operations. The remaining matrix is
\[
B=\begin{pmatrix}\alpha&(b_i)_{i\in S}\\(b_i)_{i\in S}^{t}&0_{r\times r}\end{pmatrix},
\qquad\alpha=a_0-\sum_{j\notin S}\frac{b_j^2}{a_j}.
\]
The full rank is \(m-r+\operatorname{rank}B\). If \(r=0\), the full rank is at least \(m\). If \(r\ge1\) and some \(b_i\ne0\) for \(i\in S\), then \(\operatorname{rank}B=2\); the full rank is at most \(m-1\) exactly when \(r\ge3\). If every \(b_i=0\) for \(i\in S\), then \(\operatorname{rank}B\le1\): for \(r\ge2\) the full rank is at most \(m-1\), while for \(r=1\) this requires \(\alpha=0\), equivalently \(F_i=0\). For \(r=2\) both corresponding \(b_i\)'s vanish, and the point belongs to both \(Z_i\) and \(Z_j\). For \(r\ge3\), the point belongs to some \(L_T\). This exhausts the rank-deficient set and proves the displayed union set-theoretically.

**The ideal equality and component minimality.** Deng--Kretschmer, *Ideals of submaximal minors of sparse symmetric matrices*, Theorem 1 (arXiv:2211.07020), proves that the size-\(m\)-minor ideal is radical for any symmetric sparsity graph with independent diagonal variables (including the star); its connectedness additionally gives height three and a Cohen--Macaulay quotient. Taking the radical of the set-theoretic classification therefore gives the exact scheme-theoretic equality above. Each \(Z_i\) contains points with all other leaf diagonals nonzero, and each \(L_T\) contains points with all three corresponding \(b_i\) nonzero and all other diagonals nonzero; hence no listed prime contains another. All are minimal. Their projective dimensions are \(2m-3\). The degree of \(Z_i\) is \(1\cdot1\cdot m=m\) by the irreducible hypersurface \(F_i\) in its codimension-two coordinate space; each \(L_T\) has degree one. Additivity of top-dimensional degree over distinct reduced components proves the displayed total.

**Transverse singularities.** At a general point of \(Z_i\), all other \(a_j\) are nonzero; \(F_i\) is a local coordinate because its derivative in \(a_0\) is \(P_i\ne0\). In coordinates transverse to \(Z_i\), the identity \(F=a_iF_i-b_i^2P_i\) is a nondegenerate split quadratic node. At a general point of \(L_T\), all \(b_i\) for \(i\in T\) and all remaining \(a_j\) are nonzero. With \(T=\{p,q,r\}\), the quadratic part transverse to \(L_T\), up to a unit, is
\[
Q=-b_p^2a_qa_r-b_q^2a_pa_r-b_r^2a_pa_q.
\]
The determinant of its coefficient matrix is a nonzero scalar multiple of \(b_p^2b_q^2b_r^2\), and is therefore nonzero when the characteristic is not two. The formal Morse lemma yields the ordinary node. Irreducibility and the codimension-two singular locus inside the hypersurface, together with the hypersurface \(S_2\) property, prove normality by Serre's criterion.

## Verification
The accompanying `verify_arrowhead.py` performs independent exact finite-field determinant/rank/gradient/component-membership checks for all normalized projective points over \(\mathbb F_3\) for \(m=3,4\) and over \(\mathbb F_5\) for \(m=3\). It also checks the degree identity. Execution prints `VERIFY_OK`. These computations corroborate but do not replace the all-\(m\) proof; the scheme-theoretic step uses the stated published radicality theorem.

## Relationship to prior work
Deng--Kretschmer (2022) already establish radicality, height, Cohen--Macaulayness and free resolutions for the **general** sparse symmetric submaximal-minor ideal. These are prerequisites, explicitly not new assertions here. Kerner--Vinnikov (2009) develop the theory of determinantal representations of singular hypersurfaces, including symmetric representations, without this particular star minimal-prime decomposition. Alper--Bogart--Velasco (2015) prove general codimension constraints relevant to determinantal complexity, not this singular-component list. The contribution here is the explicit all-size star **prime decomposition, number and geometry of components, and generic transverse nodal types**. The numerical total degree agrees with the standard corank-two symmetric determinantal degree and is not asserted to be an independently novel invariant.

## Limitations
The result is about this independent-variable star family, not arbitrary symmetric matrices or star matrices with identified coefficients. The generic transverse-node statement is restricted to characteristic different from two; characteristic-two local geometry is not determined. The scheme-theoretic equality concerns the radical minor ideal, not the complete (possibly nonreduced) gradient ideal. Analytic germs at component intersections and the full incidence stratification are not classified. Related older sparse-matrix literature might implicitly imply this special prime list without stating it.

## References
- D. Kerner and V. Vinnikov, *Determinantal representations of singular hypersurfaces in P^n*, arXiv:0906.3012 (first publicly posted 16 June 2009), https://arxiv.org/abs/0906.3012.
- J. Deng and A. Kretschmer, *Ideals of submaximal minors of sparse symmetric matrices*, arXiv:2211.07020 (2022), https://arxiv.org/abs/2211.07020, especially Theorem 1 and the reducedness proof.
- J. Alper, T. Bogart and M. Velasco, *A lower bound for the determinantal complexity of a hypersurface*, arXiv:1505.02205 (2015), https://arxiv.org/abs/1505.02205.
