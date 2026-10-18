# The content-height zeta function of rank-one polynomial matrices

## Finding
Let \(q\) be any prime power, let \(m,n\ge 2\), and put \(R=\mathbb F_q[T]\). For each nonzero \(m\times n\) matrix \(M\) over \(R\) of rank one over \(\mathbb F_q(T)\), define its height degree \(d(M)=\max_{i,j}\deg M_{ij}\) (using \(\deg 0=-\infty\)), and its content degree \(c(M)=\deg\gcd_{i,j}M_{ij}\), with the gcd chosen monic. Then the **joint content-height generating function** is exactly
\[
\boxed{\sum_{\operatorname{rank}M=1}z^{d(M)}w^{c(M)}=
\frac{(q^m-1)(q^n-1)}{q-1}\cdot
\frac{(1-qz)^2}{(1-q^mz)(1-q^nz)(1-qwz)}.}
\]
The sum is a formal power series in \(z\), with polynomial coefficients in \(w\). In particular, if \(M_D\) is uniform on the finite set of rank-one matrices with \(d(M)=D\), then as \(D\to\infty\), its content degree converges in law to a geometric variable on \(\mathbb Z_{\ge0}\) with exact parameter
\[
\boxed{\lim_{D\to\infty}\Pr(c(M_D)=h)=(1-\rho)\rho^h,\qquad
\rho=q^{1-\max\{m,n\}},\quad h=0,1,2,\ldots.}
\]
The height-only specialization has a degree-growth transition between square and rectangular matrices: in the square case the exact shell count has a linear factor in \(D\), while for unequal dimensions it has a pure leading exponential.

## Assumptions and scope
The field \(\mathbb F_q\) may have nonprime cardinality. Matrix rank is over the rational function field, not after evaluation at a particular value of \(T\). The zero matrix is excluded. Polynomial gcds are normalized monic. The content is the unique nonzero Smith invariant factor of a rank-one matrix over the principal ideal domain \(R\), up to multiplication by a unit. Both dimensions are integers at least two. There is no restriction on the degrees or leading coefficients of individual entries other than the stated maximum degree.

## Proof
**Canonical factorization.** Every nonzero rank-one matrix has a factorization \(M=uv^{\mathsf T}\) with \(u\in R^m\) a primitive nonzero column (its coordinates have monic gcd one) and \(v\in R^n\) nonzero: clear denominators from a generating column of the one-dimensional fraction-field column space, and divide by its coordinate gcd. If \(M=u'v'^{\mathsf T}\) is another such factorization with both columns \(u,u'\) primitive, then \(u'=\alpha u\), \(v'=\alpha^{-1}v\) for some \(\alpha\in\mathbb F_q^\times\). Indeed \(\alpha\) and its reciprocal must be polynomials by the Bézout identities for the coordinates of primitive vectors. Thus there are exactly \(q-1\) representations with primitive first vector.

Write \(g=\gcd(v_1,\ldots,v_n)\) monic, and \(v=gv_0\). The vector \(v_0\) is primitive. Since the first vector is primitive, the monic gcd of all entries of \(M\) equals \(g\). Therefore every matrix has exactly \(q-1\) representations
\[
M=g\,u\,v_0^{\mathsf T},\qquad
\gcd(u_1,\ldots,u_m)=\gcd((v_0)_1,\ldots,(v_0)_n)=1,
\]
with \(g\) monic. Furthermore the degree of the largest entry is exactly
\(d(M)=\deg g+\max_i\deg u_i+\max_j\deg(v_0)_j\). This follows by choosing a nonzero entry of maximal degree from each primitive vector and using additivity of polynomial degree for nonzero products.

**Primitive-vector enumeration.** For any integer \(k\ge1\), the number of nonzero vectors in \(R^k\) with maximum coordinate degree exactly \(a\ge0\) is \((q^k-1)q^{ka}\). Its height generating series is therefore
\[
V_k(z)=\frac{q^k-1}{1-q^kz}.
\]
Every nonzero vector is uniquely a monic common factor times a primitive vector. Since the number of monic polynomials of degree \(b\) is \(q^b\), the generating function for monic factors is \((1-qz)^{-1}\). It follows that the primitive-vector generating series is
\[
P_k(z)=(1-qz)V_k(z)=\frac{(q^k-1)(1-qz)}{1-q^kz}.
\]
Multiplying \(P_m(z)P_n(z)\) and the monic content series \((1-qwz)^{-1}\), and dividing by the exactly \(q-1\) unit scalings, gives the asserted joint formula coefficient by coefficient. This proves the finite exact identity without asymptotic approximations.

**The limiting law.** Set \(A=q^{\max\{m,n\}}\) and \(B=q^{\min\{m,n\}}\). The height generating series at \(w=1\) is
\[
H(z,1)=C\frac{1-qz}{(1-Az)(1-Bz)},
\qquad C=\frac{(q^m-1)(q^n-1)}{q-1}.
\]
When \(A>B\), its coefficients have a simple leading pole at \(z=A^{-1}\); when \(A=B\), they have a double leading pole. In either case, for each fixed \(h\ge0\), the ratio of the coefficient of \(z^Dw^h\) in \(H(z,w)\) to the coefficient of \(z^D\) in \(H(z,1)\) tends to \((1-q/A)(q/A)^h\). The limiting probabilities sum to one, so pointwise convergence on the countable space \(\mathbb Z_{\ge0}\) implies convergence in distribution. Hence \(\rho=q/A\), as claimed.

**Sharp dimension transition.** Write \(R_{m,n}(D)=\#\{M:\operatorname{rank}M=1,\ d(M)=D\}\). By extracting coefficients at \(w=1\), for \(A>B\),
\[
R_{m,n}(D)=C\frac{(A-q)A^D-(B-q)B^D}{A-B};
\]
while for \(m=n=r\ge2\),
\[
R_{r,r}(D)=Cq^{rD}\bigl((D+1)-Dq^{1-r}\bigr).
\]
These are exact for every integer \(D\ge0\), and show the stated linear enhancement precisely in equal dimensions.

## Verification
The accompanying standalone `verify.py` enumerates actual coefficient arrays, checks every \(2\times2\) minor as a polynomial identity, calculates the monic common-factor degree by Euclidean gcd, and compares each joint cell with the exact coefficient formula. The exhaustive tested cases are \((q,m,n,D_{\max})=(2,2,2,1),(2,2,3,1),(3,2,2,1)\). The separately preserved `checks.txt` contains the actual outputs. Algebraically, specializing to \(m=n=2\), summing shells of heights at most \(D\), and adding the excluded zero matrix reproduces the published \(2\times2\) formula from the motivating paper, including the \(D=0\) boundary.

## Relationship to prior work
Afifurrahman's *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first public October 8, 2026), Theorem 2.1, already determines the total number of \(2\times2\) polynomial matrices with determinant zero and bounded entry degrees. That special case is not new and is a consistency check; its treatment of nonzero entries and monic normalization appears in Section 4. The result here concerns **all rectangular dimensions**, the **joint Smith-content degree** rather than the unweighted count alone, and its **limiting geometric law**, none of which are stated in the motivating theorem. General height-zeta theory for Segre/toric varieties supplies broader geometric context, but the specific affine polynomial-matrix content-height refinement was not located in the compared sources.

## Limitations
This theorem treats only rank-one matrices over the one-variable polynomial ring and does not address higher rank, coefficients in arbitrary curves, or uniformly varying dimensions. The limiting law holds for fixed \(q,m,n\) as \(D\to\infty\), not uniformly in these parameters. The exact two-by-two unweighted specialization is already published. A potentially equivalent formula in broader function-field height literature may exist and would require independent bibliographic confirmation. Exhaustive tests cover finite prime-field examples; they are not offered as proof of the general formula.

## References
1. Muhammad Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (October 8, 2026), Theorem 2.1 and Section 4. https://arxiv.org/html/2610.11240v1
2. Sebastián Herrero, Tobías Martínez, and Pedro Montero, *Counting rational points on Hirzebruch–Kleinschmidt varieties over global function fields*, arXiv:2408.07631 (2024), general height-zeta context. https://arxiv.org/abs/2408.07631
