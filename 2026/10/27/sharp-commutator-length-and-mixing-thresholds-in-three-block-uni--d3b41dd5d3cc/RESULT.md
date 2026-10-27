# Sharp commutator-length and mixing thresholds in three-block unipotent radicals

## Finding

For any finite field \(\mathbb F_q\), any integers \(a,b,c\geq1\), and the three-block unipotent radical \(G=G_{a,b,c}(\mathbb F_q)\) defined below, the subgroup \([G,G]\) is its center, naturally identified with \(M_{a,c}(\mathbb F_q)\). The exact minimum number of group commutators whose product is a prescribed central element with matrix coordinate \(C\) is
\[
\ell(C)=\left\lceil\frac{\operatorname{rank}(C)}{2b}\right\rceil,
\qquad
\operatorname{cw}(G)=\left\lceil\frac{\min(a,c)}{2b}\right\rceil.
\]
The identity has length zero. In particular, these class-two finite groups have unbounded commutator width as \(\min(a,c)\) increases with \(b\) fixed.

More precisely, put \(d=2bt\) and \(r=\operatorname{rank}(C)\). The number of ordered \(2t\)-tuples of elements of \(G\) whose product of \(t\) group commutators equals the prescribed element is, for every \(t\geq1\),
\[
R_t(C)=q^{2tac}\sum_{s=r}^{\min(a,d)}
{a-r\brack s-r}_q
\left(\prod_{i=0}^{s-1}(q^d-q^i)\right)
q^{(d-s)c}.
\]
An empty sum is zero; the Gaussian coefficient \({n\brack j}_q\) counts \(j\)-dimensional subspaces of \(\mathbb F_q^n\). Thus \(R_t(C)>0\) exactly when \(r\leq d\).

Let \(\mu_t\) be the distribution of the product of \(t\) independent commutators of uniformly and independently chosen group elements, and \(u\) the uniform distribution on the center. Set \(m=\min(a,c)\), \(M=\max(a,c)\), and \(K_q=\prod_{j\geq1}(1-q^{-j})^{-1}\). Then
\[
\|\mu_t-u\|_{\mathrm{TV}}\geq1-K_q q^{-(m-d)(M-d)}\quad(d<m),
\qquad
\|\mu_t-u\|_{\mathrm{TV}}\leq\frac{q^{m-d}}{q-1}\quad(d\geq m).
\]
Consequently, for fixed \(q\) and \(b\), as \(m\to\infty\) with \(M\geq m\), the commutator-product distribution has a total-variation cutoff on an \(O(1)\)-step window about \(t=m/(2b)\). The first time its support is the whole center is exactly \(\lceil m/(2b)\rceil\), the commutator width.

## Assumptions and scope

The prime-power \(q\) is arbitrary, including powers of two. The three block sizes \(a,b,c\) are positive integers. The group comprises matrices
\[
g(X,Y,Z)=\begin{pmatrix}I_a&X&Z\\0&I_b&Y\\0&0&I_c\end{pmatrix},
\quad X\in M_{a,b}(\mathbb F_q),\;Y\in M_{b,c}(\mathbb F_q),\;Z\in M_{a,c}(\mathbb F_q).
\]
For \(g,h\in G\), use the convention \([g,h]=g^{-1}h^{-1}gh\). The central block parameter \(C\) has exactly \(ac\) entries. No restriction on the characteristic or on the relative block sizes is imposed. The total-variation statement concerns independent uniformly sampled pairs of group elements at each of \(t\) steps and probability distributions supported on \([G,G]\), not on the entire nonabelian group.

## Proof

**Group law.** Direct block multiplication gives
\[
g(X,Y,Z)g(U,V,W)=g(X+U,Y+V,Z+W+XV).
\]
The resulting commutator is \(g(0,0,XV-UY)\). Every elementary matrix in the upper-right corner occurs as \(XV\), by taking compatible elementary matrices for \(X\) and \(V\), and these central matrices generate the full additive \(M_{a,c}\). Therefore \([G,G]=Z(G)=\{g(0,0,C):C\in M_{a,c}\}\). To see that there are no other central elements, commute against all \(g(0,V,0)\) to force \(X=0\), and against all \(g(U,0,0)\) to force \(Y=0\).

**Rectangular factorization and the exact fibers.** For a product of \(t\) commutators write the resulting central coordinate as
\[
C=\sum_{i=1}^t(X_iV_i-U_iY_i)=AB,
\]
where \(A\in M_{a,d}\) is formed by concatenating \(X_1,-U_1,\ldots,X_t,-U_t\), and \(B\in M_{d,c}\) is the corresponding vertical concatenation of \(V_1,Y_1,\ldots,V_t,Y_t\). This is a bijective rearrangement of the \(2t\) noncentral coordinate pairs; the \(2t\) arbitrary upper-right coordinates contribute the factor \(q^{2tac}\).

Fix \(C\) of rank \(r\), and stratify the matrices \(A\) by their rank \(s\). Their images must contain \(\operatorname{im}(C)\), and there are \({a-r\brack s-r}_q\) possible \(s\)-dimensional images. Each such image is reached by exactly \(\prod_{i=0}^{s-1}(q^d-q^i)\) surjections \(\mathbb F_q^d\twoheadrightarrow\mathbb F_q^s\). For such an \(A\), each of the \(c\) column equations in \(AB=C\) has \(q^{d-s}\) solutions. This establishes the exact expression for \(R_t(C)\) and also shows its positivity is precisely equivalent to \(r\leq\min(a,c,d)\). A rank-\(r\) central target is therefore reachable with \(t\) commutators exactly when \(r\leq2bt\); maximizing \(r\) proves the length and width formulas.

**Fourier check.** Let \(\psi\) be a nontrivial additive character of \(\mathbb F_q\) and pair a character parameter \(T\in M_{c,a}\) with \(C\in M_{a,c}\) through \(\psi(\operatorname{tr}(TC))\). If \(T\) has rank \(s\), then, given a uniform \(A\in M_{a,d}\), the conditional expectation of \(\psi(\operatorname{tr}(TAB))\) over uniform \(B\) equals one if \(TA=0\) and zero otherwise. Its unconditional expectation is \(q^{-ds}\). For the convolution distribution \(\mu_t\) the same value is \(q^{-2bts}\). Parseval therefore yields the additional exact identity
\[
q^{ac}\sum_C|\mu_t(C)-q^{-ac}|^2=
\sum_{s=1}^{m}N_{a,c}(s)q^{-4bts},
\]
where \(N_{a,c}(s)=\prod_{i=0}^{s-1}(q^a-q^i)(q^c-q^i)/(q^s-q^i)\) is the number of \(a\times c\) matrices of rank \(s\). This identity is a consistency check, not an assertion of a novel general Fourier method.

**Lower mixing bound.** If \(d<m\), the random matrix \(AB\) has rank at most \(d\). If \(m=a\), its image lies in some \(d\)-dimensional subspace of \(\mathbb F_q^m\); if \(m=c\), transpose the argument. A uniformly random \(m\times M\) matrix has image contained in one fixed \(d\)-subspace with probability \(q^{-(m-d)M}\). A union bound over \({m\brack d}_q\) subspaces and the standard estimate \({m\brack d}_q\leq K_q q^{d(m-d)}\) give \(u(\operatorname{rank}\leq d)\leq K_q q^{-(m-d)(M-d)}\). As \(\mu_t\) assigns this event probability one, the lower total-variation bound follows.

**Upper mixing bound.** Suppose \(d\geq m\). If \(m=a\), condition on \(A\) having full row rank: then \(AB\) is uniform on all \(a\times c\) matrices. If \(m=c\), condition instead on \(B\) having full column rank: then \(AB\) is uniform for the same reason. The probability of rank failure in the chosen \(m\times d\) or \(d\times m\) matrix is at most \(\sum_{j=0}^{m-1}q^{j-d}<q^{m-d}/(q-1)\), by a union bound on nonzero linear forms. The law of \(AB\) is thus a mixture containing uniform measure with weight at least one minus this failure probability; the upper total-variation bound follows. If \(m-d\to+\infty\), the lower bound tends to one; if \(d-m\to+\infty\), the upper tends to zero. For fixed \(b\), the transition occurs in a bounded number of commutator steps.

## Verification

The standalone program `verify_three_block_commutator.py` uses explicit block-matrix multiplication and inverses to enumerate commutators for seven small complete finite-field configurations, including characteristic two and the extension field \(\mathbb F_4\). It checks each prescribed target and the convolution of two commutators against the general rank-based fiber formula. Five further independent rectangular-matrix enumerations directly check every target in their respective dimensions. All tests passed with marker `VERIFY_OK_THREE_BLOCK_COMMUTATOR_FIBERS 7 5`. Direct finite checks are not a proof for unrestricted block sizes, fields, or tuple lengths; those quantifiers follow from the algebraic argument above.

## Relationship to prior work

Diaconis and Thiem's treatment of pattern groups includes the same three-block matrix group and character-theoretic information. Nien later constructed the irreducible representations of this same radical and enumerated their degrees. Their results are a significant overlap: character theory together with the classical Frobenius commutator formula can in principle recover the one-step commutator distribution, and the Fourier identity above is not claimed as independent character-theoretic novelty. The present statement isolates a different structural output: exact **minimum commutator length**, its potentially unbounded behavior inside a two-step unipotent radical, and sharp rank-driven total-variation mixing bounds with coincident support and mixing thresholds. Sosnovsky's theorem gives commutator width one for the **full triangular group**, which does not imply width one in its much smaller three-block unipotent radical. The elementary rectangular-matrix factor-count identity is used as a tool rather than claimed as a new matrix-counting formula.

## Limitations

This concerns three-block radicals, not arbitrary parabolic unipotent radicals with four or more blocks. The cutoff statement is asymptotic for fixed \(q\) and \(b\) as \(m\to\infty\); the explicit bounds themselves hold at every finite parameter. The method counts products of uniformly sampled unconstrained commutators; it does not cover constrained generators or nonuniform sampling. Existing character tables may make portions of the counting theorem implicitly derivable. Historical priority and independent mathematical validation have not been fully established.

## References

1. P. Diaconis and N. Thiem, *Supercharacter formulas for pattern groups*, arXiv:math/0610161 (first public 2006-10-04), especially the three-block example and related character formulas.
2. Y. V. Sosnovsky, *On the Width of Verbal Subgroups of the Groups of Triangular Matrices over a Field of Arbitrary Characteristic*, arXiv:1201.6513 (2012), Theorem 3.
3. C. Nien, *Characters of unipotent radicals of standard parabolic subgroups with 3 parts*, Journal of Algebraic Combinatorics 55 (2022), 325–333, doi:10.1007/s10801-021-01052-8, Theorem 2.3.
4. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504 (2012), as general rank-distribution context.
