# Exact algebra-generation spectra of transverse square-zero pairs

## Finding
Let \(k=\mathbb F_q\), with \(q\) any prime power, and let \(m\ge1\). Call an ordered pair \((X,Y)\in M_{2m}(k)^2\) *transverse square-zero* when
\[
X^2=Y^2=0,\quad \operatorname{rank}X=\operatorname{rank}Y=m,\quad \operatorname{im}X\cap\operatorname{im}Y=0.
\]
Let \(D(X,Y)=\dim_k k\langle I_{2m},X,Y\rangle\), where the angle brackets denote the associative unital subalgebra.

**Structure and orbit theorem.** Every such pair is simultaneously similar to exactly one similarity class of pairs
\[
X_0=\begin{pmatrix}0&I_m\\0&0\end{pmatrix},\qquad
Y_C=\begin{pmatrix}0&0\\C&0\end{pmatrix},\quad C\in\operatorname{GL}_m(k).
\]
Two choices \(C,C'\) give simultaneously similar pairs precisely when \(C\) and \(C'\) are similar. If \(\mu_C\) is the monic minimal polynomial of \(C\), then the generated algebra is isomorphic to
\[
k\langle I_{2m},X,Y\rangle\ \cong\ M_2(k[t]/(\mu_C(t))),\qquad D(X,Y)=4\deg\mu_C.
\]
Thus every and only the dimensions \(4,8,\ldots,4m\) occur on the transverse locus.

**Exact finite-field frequencies.** Set \(g_m(q)=|\operatorname{GL}_m(q)|=\prod_{i=0}^{m-1}(q^m-q^i)\), and let \(c_{m,d}(q)\) denote the number of invertible \(m\times m\) matrices with minimal-polynomial degree \(d\). For each \(1\le d\le m\), the number of transverse square-zero ordered pairs generating a \(4d\)-dimensional algebra is exactly
\[
T_{m,d}(q)={2m\brack m}_q\,q^{m^2}\,g_m(q)\,c_{m,d}(q).
\]
The number of all transverse pairs is \({2m\brack m}_q q^{m^2}g_m(q)^2\), so their conditional \(D=4d\) probability equals \(c_{m,d}(q)/g_m(q)\).

Here is an explicit terminating formula for all the frequencies, requiring no unknown parameters. Let \(f\) range over monic irreducible polynomials over \(k\) with \(f(0)\ne0\). A rational-canonical similarity type is a finite family of partitions \(\lambda_f\) with \(\sum_f\deg(f)|\lambda_f|=m\). Write \(\lambda_f'\) for its conjugate, \(m_j(\lambda_f)\) for the number of parts equal to \(j\), and \(\lambda_{f,1}\) for its largest part, interpreted as zero for the empty partition. Put
\[
Z(\boldsymbol\lambda)=\prod_f q^{\deg(f)\sum_i(\lambda'_{f,i})^2}\prod_{j\ge1}\prod_{\ell=1}^{m_j(\lambda_f)}(1-q^{-\ell\deg(f)}).
\]
Then
\[
c_{m,d}(q)=g_m(q)\!\sum_{\substack{\sum_f\deg(f)|\lambda_f|=m\\\sum_f\deg(f)\lambda_{f,1}=d}}Z(\boldsymbol\lambda)^{-1}.
\]
In particular \(c_{m,1}(q)=q-1\). The extremal multiplicity \(T_{m,m}(q)\) counts precisely cyclic invertible \(C\), i.e. matrices with equal characteristic and minimal polynomials; equivalently
\[
c_{m,m}(q)=g_m(q)\!\sum_{\substack{h\in k[t]\text{ monic},\ \deg h=m\\h(0)\ne0}}\frac{1}{q^m\prod_{f\mid h\text{ irreducible}}(1-q^{-\deg f})}.
\]
These formulas apply in every characteristic. For \((m,q)=(2,2)\) there are precisely \(20{,}160\) transverse pairs: \(3{,}360\) generate dimension \(4\) and \(16{,}800\) generate dimension \(8\). For \(m>1\), no transverse pair generates all of \(M_{2m}(k)\).

## Assumptions and scope
All matrices act on a \(2m\)-dimensional vector space over the same finite field. Square-zero means literal \(X^2=0\) and \(Y^2=0\), with neither a restriction on characteristic nor on semisimplicity of \(C\). Transversality and both rank assumptions are essential: the statement does not enumerate pairs with intersecting images or smaller ranks. This is a count of ordered matrices in a fixed ambient vector space, not of similarity orbits; the orbit bijection is stated separately.

## Proof
1. Since \(X^2=0\) and \(\operatorname{rank}X=m\), \(\ker X=\operatorname{im}X=:U\); similarly \(\ker Y=\operatorname{im}Y=:W\). Transversality gives \(V=U\oplus W\). The restrictions \(X|_W:W\to U\) and \(Y|_U:U\to W\) are isomorphisms. Choose a basis of \(U\), and transport it to \(W\) using \(X|_W\); this produces \(X_0,Y_C\), with \(C\) invertible.
2. The subspaces \(U=\operatorname{im}X\) and \(W=\operatorname{im}Y\) are intrinsic. Any conjugacy between two normalized pairs must preserve both and commute with \(X_0\). Its block form is therefore \(\operatorname{diag}(P,P)\), so the remaining action is \(C\mapsto PCP^{-1}\). This proves the orbit criterion.
3. Direct multiplication gives \(X_0Y_C=\operatorname{diag}(C,0)\), \(Y_CX_0=\operatorname{diag}(0,C)\), with upper-right blocks \(C^j\) obtained from \((X_0Y_C)^jX_0\) and lower-left blocks \(C^{j+1}\) from \((Y_CX_0)^jY_C\). Since \(C\) is invertible, its minimal polynomial has nonzero constant term; hence \(I_m\) and \(C^{-1}\) are polynomials in positive powers of \(C\). All four independent block positions therefore contain exactly \(k[C]\). They form \(M_2(k[C])\), of dimension \(4\deg\mu_C\), and \(k[C]\cong k[t]/(\mu_C)\).
4. Every minimal-polynomial degree \(d\in\{1,\ldots,m\}\) occurs: take a unipotent Jordan block of size \(d\), with an identity block of size \(m-d\), using the latter only when nonempty. The minimal polynomial is \((t-1)^d\) in every characteristic.
5. Choose \(U=\operatorname{im}X\) in \({2m\brack m}_q\) ways and then choose the isomorphism \(V/U\to U\) in \(g_m(q)\) ways; these choices determine \(X\). For a fixed \(X\), its complementary \(m\)-planes \(W\) number \(q^{m^2}\) (graphs of linear maps from any fixed complement to \(U\)). Once \(W\) is chosen, \(Y|_U:U\to W\) is an arbitrary isomorphism. Composing with \(X|_W\) bijects such maps with \(C\in\operatorname{GL}(U)\), proving the frequency formula.
6. Rational canonical form parametrizes invertible similarity classes by families \(\lambda_f\). The minimal polynomial is \(\prod_f f^{\lambda_{f,1}}\); its degree is the displayed sum. The invertible centralizer of the corresponding primary module has order \(Z(\boldsymbol\lambda)\), by counting units in its endomorphism ring, giving class size \(g_m(q)/Z(\boldsymbol\lambda)\) and the first explicit formula. A cyclic matrix with characteristic polynomial \(h\) is conjugate to its companion matrix; its centralizer group equals \((k[t]/h)^\times\), of order \(q^m\prod_{f\mid h}(1-q^{-\deg f})\). Summing its conjugacy-class size over \(h\) proves the second.

## Verification
The standalone `VERIFY.py` computes algebra closures as spans of matrix words over prime fields, independently compares their dimensions with the minimal-polynomial degree, and checks the complete finite \(\operatorname{GL}_m\) distributions for \((q,m)=(2,1),(3,1),(5,1),(2,2),(3,2),(5,2),(2,3)\). It also enumerates every \(4\times4\) binary square-zero matrix \(Y\) for a fixed maximal-rank \(X\), filters the transverse pairs, and verifies the exact dimension distribution; its actual assertions are \(16\) pairs of dimension \(4\), \(80\) of dimension \(8\), and \(16{,}800\) dimension-eight ordered pairs after varying \(X\). Run with `python3 VERIFY.py`; successful completion prints `VERIFY_OK`.

## Relationship to prior work
Gaines, Laffey and Shapiro (1983) proved the general \(2n\)/\(2n-1\) upper bound for associative algebras generated by two quadratic-minimal-polynomial matrices, so that global upper bound is NOT asserted as new. Kandić and Šivic (arXiv:1603.08413, originally publicly posted 2016-03-04) discuss that theorem in Section 6, Theorem 6.10, and idempotent constructions; those statements do not give the transverse square-zero orbit-to-similarity correspondence or the enumerated dimension distribution. Neumann and Praeger (1995) and Wall (1999) study cyclic matrices over finite fields, whose known similarity-class framework is explicitly used here. The new mathematical claim is the exact reduction of this constrained two-generator-algebra census, including every dimension stratum and its finite-field multiplicity, to invertible rational-canonical types. Existing classical ingredients are not claimed as discoveries.

## Limitations
The result is restricted to the open transverse locus of pairs with maximal possible square-zero ranks in even ambient dimension; it is not the full space of two square-zero matrices. It does not classify all extremal pairs outside that locus. The available 1983 original-paper record gave its abstract but not readable full text, leaving bibliographic risk about whether a similar normal-form argument appeared there. The present derivation verifies the statement independently, but does not establish global bibliographic priority. Finite checks cannot replace the all-field proof.

## References
- F. J. Gaines, T. J. Laffey, H. M. Shapiro, *Pairs of matrices with quadratic minimal polynomials*, Linear Algebra and its Applications 52–53 (1983), 289–292, DOI: 10.1016/0024-3795(83)80019-6.
- M. Kandić and K. Šivic, *On the dimension of the algebra generated by two positive semi-commuting matrices*, arXiv:1603.08413v2 (original submission 2016-03-04), especially Section 6.
- T. J. Laffey, O. Markova, H. Šmigoc, *The effect of assuming the identity as a generator on the length of the matrix algebra*, arXiv:1501.05806v1 (2015).
- P. M. Neumann and C. E. Praeger, *Cyclic matrices over finite fields*, Journal of the London Mathematical Society 52 (1995), 263–284, DOI: 10.1112/jlms/52.2.263.
- G. E. Wall, *Counting cyclic and separable matrices over a finite field*, Bulletin of the Australian Mathematical Society 60 (1999), 253–284, DOI: 10.1017/S000497270003639X.
