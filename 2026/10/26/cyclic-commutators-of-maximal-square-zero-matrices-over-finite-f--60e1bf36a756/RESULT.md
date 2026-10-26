# Cyclic commutators of maximal square-zero matrices over finite fields

## Finding

Let \(q\) be a prime power, let \(m\geq1\), and choose \(E,F\) independently and uniformly among rank-\(m\) matrices in \(M_{2m}(\mathbb F_q)\) satisfying \(E^2=F^2=0\). Put \(C=EF-FE\). Write \({2m\brack m}_q\) for the Gaussian binomial coefficient and \(\Phi_q=\prod_{j\geq1}(1-q^{-j})\).

**Exact invertibility and conditional similarity law.** One has
\[
\Pr(C\text{ invertible})=\frac{q^{m^2}}{{2m\brack m}_q}.
\]
Conditional on invertibility, the similarity class of \(C\) has exactly the distribution of \(T\oplus(-T)\) for \(T\) uniform in \(\operatorname{GL}_m(\mathbb F_q)\). In particular, this determines the full rational-canonical-form law of invertible commutators.

**Cyclicity dichotomy.** Call a matrix *cyclic* if its minimal and characteristic polynomials coincide. If \(q\) is even, \(\Pr(C\text{ cyclic and invertible})=0\) for every \(m\geq1\). If \(q\) is odd, let \(\mathcal P_q\) consist of the unordered two-element orbits of the involution \(\phi(t)\mapsto\phi^{\mathrm{op}}(t)=(-1)^{\deg\phi}\phi(-t)\) on monic irreducible polynomials with nonzero constant term. Then, with \(d=\deg\phi\) for either member of an orbit,
\[
H_q(z)=\prod_{\{\phi,\phi^{\mathrm{op}}\}\in\mathcal P_q}
\left(1+\frac{2z^d}{(q^d-1)(1-z^d/q^d)}\right)
\]
is a well-defined formal power series, and the exact conditional cyclicity probability is
\[
\Pr(C\text{ cyclic}\mid C\text{ invertible})=[z^m]H_q(z).
\]
For every fixed odd \(q\), this conditional probability converges exponentially fast as \(m\to\infty\) to the **rational constant**
\[
\boxed{\kappa_q=\frac{(1-q^{-1})(1-q^{-3})}{1-q^{-4}}}.
\]
Consequently, over odd fields,
\[
\boxed{\lim_{m\to\infty}\Pr(C\text{ cyclic and invertible})=\Phi_q\,\frac{(1-q^{-1})(1-q^{-3})}{1-q^{-4}}>0,}
\]
whereas the same probability vanishes identically in characteristic two. For example, the conditional cyclicity probabilities at \(m=2\) are \(7/12\), \(47/60\), and \(143/168\) for \(q=3,5,7\); the limiting conditional probabilities at these three field orders are \(13/20\), \(31/39\), and \(171/200\).

## Assumptions and scope

All matrices are over the indicated finite field, including nonprime extension fields; no bilinear form, adjointness, or commuting condition is imposed. The square-zero matrices are sampled uniformly from their **fixed maximal-rank class**, not uniformly from all square-zero matrices. The space has dimension \(2m\), so their images equal their kernels. The inverse and the word "cyclic" apply to the commutator \(C\), not to the individual nilpotents \(E,F\). Statements involving the product over \(\mathcal P_q\) require odd characteristic; the even-characteristic result is separate. No finite-sample assertion about large \(m\) follows merely from the asymptotic limit.

## Proof

**1. Transverse kernels.** Each maximal-rank square-zero \(E\) has \(U=\ker E=\operatorname{im}E\), an \(m\)-subspace; after \(U\) is specified, \(E\) is exactly an isomorphism \(V/U\to U\). Hence each \(U\) supports \(|\operatorname{GL}_m(\mathbb F_q)|\) such matrices, and \(U\) is a uniform \(m\)-plane. Similarly \(W=\ker F=\operatorname{im}F\) is independent and uniform. If \(U\cap W\ne0\), every vector in the intersection lies in \(\ker C\). Conversely, when \(V=U\oplus W\), the restrictions \(A=E|_W:W\to U\) and \(B=F|_U:U\to W\) are invertible, and in this decomposition
\[
E=\begin{pmatrix}0&A\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\B&0\end{pmatrix},\quad
C=\begin{pmatrix}AB&0\\0&-BA\end{pmatrix}.
\]
Therefore \(C\) is invertible exactly when \(U,W\) are complementary. For a fixed \(U\), the complements are the graphs of the \(q^{m^2}\) linear maps from a fixed complement to \(U\). Since there are \({2m\brack m}_q\) \(m\)-planes, the claimed probability follows. Given complementary \(U,W\), the two isomorphisms \(A,B\) are independent and uniform, so \(T=AB\) is uniform in \(\operatorname{GL}_m\), and \(BA\) is similar to \(AB\). This proves the pushforward similarity law.

**2. Characteristic-sensitive cyclicity.** A direct sum of two finite-dimensional polynomial modules is cyclic precisely when each is cyclic and their minimal polynomials are coprime. Consequently, \(T\oplus(-T)\) is cyclic if and only if \(T\) is cyclic and \(\gcd(\chi_T(t),\chi_T(-t))=1\), with the sign of the leading coefficient ignored. In characteristic two, \(T\oplus T\) has minimal polynomial of degree at most \(m\) and cannot be cyclic in dimension \(2m\). For odd \(q\), factor \(\chi_T\) into monic irreducibles. The condition means: on each two-element orbit \(\{\phi,\phi^{\mathrm{op}}\}\), at most one member occurs, with a single primary Jordan block of arbitrary positive exponent; no self-opposite irreducible may occur. For an irreducible of degree \(d\), a single primary block \(\phi^k\) has centralizer order \(q^{d(k-1)}(q^d-1)\). Summing \(1/|\mathrm{centralizer}|\) over the allowed \(\operatorname{GL}_m\)-conjugacy classes yields the displayed product \(H_q\) and its coefficient formula, by the ordinary conjugacy-class counting identity.

**3. Existence of the limit.** Define \(F_d(z)=\prod_{j\geq1}(1-z^d/q^{jd})^{-1}\). The general-linear cycle index, with all class variables equal to one, reads
\[
\frac1{1-z}=\prod_{\phi\ne t}F_{\deg\phi}(z).
\]
Let \(\mathcal S_q\) denote the self-opposite irreducibles. Thus \(R_q(z)=(1-z)H_q(z)\) is the product, over two-element orbits, of the ratio of the displayed local factor to \(F_d(z)^2\), and over \(\mathcal S_q\) of \(F_d(z)^{-1}\). The paired ratios have cancellation of their linear term and differ from one by \(O((r^2/q^2)^d)\) uniformly on \(|z|\le r\); self-opposites exist only in even degree and their number in degree \(d\) is \(O(q^{d/2})\). Since there are \(O(q^d)\) irreducibles of degree \(d\), the product defining \(R_q\) converges normally for each \(r<\sqrt q\). In particular, choosing any \(1<r<\sqrt q\), its Taylor coefficients are absolutely summable with exponential tails. As \(H_q=R_q/(1-z)\), coefficient extraction gives \([z^m]H_q(z)=R_q(1)+O(r^{-m})\), with a constant depending on \(q,r\).

**4. Evaluation of the limit.** Set \(Q=q^d\). At \(z=1\), a paired local factor is \(1+2Q/(Q-1)^2=(Q^2+1)/(Q-1)^2\). Dividing by \(F_d(1)^2\) leaves \((1+q^{-2d})\prod_{j\geq2}(1-q^{-jd})^2\); a self-opposite factor leaves \(\prod_{j\geq1}(1-q^{-jd})\). By the unique-factorization identity
\[
\prod_{\phi\ne t}(1-u^{\deg\phi})=\frac{1-qu}{1-u},
\]
the factors with \(j\geq2\), taken over all \(\phi\ne t\), telescope to \(1-q^{-1}\).

To evaluate the remaining product, use a formal variable \(v\). Put
\[
A(v)=\prod_{\mathcal P_q}(1-v^{\deg\phi})^{-1},\qquad
B(v)=\prod_{\phi\in\mathcal S_q}(1-v^{\deg\phi/2})^{-1},\qquad
Z(v)=\frac{1-v}{1-qv}.
\]
Every monic even polynomial with nonzero constant term is uniquely the substitution \(g(t^2)\) of a monic polynomial \(g\) with nonzero constant term. Its irreducible factors are either self-opposite or occur in opposite pairs, with equal multiplicity. Hence \(A(v)B(v)=Z(v)\). A self-opposite irreducible \(\phi(t)=g(t^2)\) corresponds precisely to an irreducible \(g\) whose root is nonsquare in its residue field. If \(\chi\) is the quadratic character on \(\mathbb F_q^\times\), this is \(\chi((-1)^{\deg g}g(0))=-1\). The character sum over monic polynomials of each positive degree with nonzero constant vanishes. Its Euler product therefore gives
\[
B(v)^2/B(v^2)=Z(v).
\]
Now
\[
\prod_{\mathcal P_q}(1+v^{\deg\phi})
\prod_{\phi\in\mathcal S_q}(1-v^{\deg\phi/2})
=\frac{A(v)}{A(v^2)B(v)}
=\frac{1-qv^2}{1-v^2}.
\]
Setting \(v=q^{-2}\) and reinstating the telescoped factor \(1-q^{-1}\) proves \(R_q(1)=\kappa_q\). Finally, the transverse-kernel probability satisfies
\[
\frac{q^{m^2}}{{2m\brack m}_q}
=\frac{\prod_{j=1}^{m}(1-q^{-j})}{\prod_{j=m+1}^{2m}(1-q^{-j})}
\longrightarrow \Phi_q,
\]
which proves the unconditional limit.

## Verification

The independent standard-library checker `checker.py` exhaustively enumerates general-linear matrices in nine small prime-field configurations and tests cyclicity of \(T\oplus(-T)\) by the dimension of the linear span of its successive powers, without using the factor-coprimality test. It compares counts with independently expanded rational Euler factors. The tested cases include \(q=2,3,5,7\), \(m=1,2\), and \(q=2,3\) at \(m=3\). The checker also exhaustively enumerates rank-half square-zero pairs at \((q,m)=(2,1),(3,1),(2,2)\) and checks commutator invertibility directly. The recorded output in `checker_output.txt` ends with `ALL_CYCLIC_SQUAREZERO_COMMUTATOR_CHECKS_PASSED units=13957 pairs=44173`. Run from the directory containing the files with `python3 checker.py`. The proof, not these finite tests, establishes the general prime-power and asymptotic claims.

## Relationship to prior work

The general similarity-class classification and cyclic-matrix cycle index are classical, as described and developed in Fulman's survey on random matrices over finite fields. The 2022 work of de Seguins Pazzis classifies sums of two square-zero endomorphisms (and their selfadjoint/skew variants), including the similarity-to-negative criterion. Suwama's 2021 work addresses which trace-zero matrices are commutators. None of those inspected statements gives the probability distribution of **commutators of two independently uniform maximal-rank square-zero matrices**, its conditional cyclicity generating function, or the field-characteristic dichotomy with the explicit rational limiting constant. In particular, representability as a sum of two square-zero matrices is not the same condition as representability as their commutator.

## Limitations

The complete similarity distribution is characterized as the pushforward of a uniform general-linear matrix; it is not presented as a tabulated list of every rational-canonical type. The cyclicity formula is exact only conditional on invertibility, which is essential to its complementary-kernel parametrization. The asymptotic cyclicity statement holds at fixed field order as \(m\to\infty\), not when \(q\) varies arbitrarily with \(m\). The checker covers prime fields only; the proof covers all prime powers. The cited broad matrix-decomposition and cycle-index machinery may make equivalent unindexed reformulations possible; priority should be independently checked before publication.

## References

1. C. de Seguins Pazzis, *Sums of two square-zero selfadjoint or skew-selfadjoint endomorphisms*, arXiv:2210.03955, first submitted 2022-10-08, https://arxiv.org/abs/2210.03955 (the source framing the square-zero decomposition problem).
2. J. Fulman, *Random matrix theory over finite fields*, Bulletin of the American Mathematical Society **39** (2002), 51–85, https://ocw.mit.edu/courses/18-996-random-matrix-theory-and-its-applications-spring-2004/8b95d016309930598ececb496e983f2c_s_0273.pdf (general-linear conjugacy cycle indices and cyclic matrices).
3. M. Suwama, *On trace zero matrices and commutators*, arXiv:2111.04884, first submitted 2021-11-08, https://arxiv.org/abs/2111.04884 (commutator representability over rings).
4. K. Luh, S. Meehan, H. H. Nguyen, *Some new results in random matrices over finite fields*, arXiv:1907.02575, first submitted 2019-07-04, https://arxiv.org/abs/1907.02575 (finite-field random-matrix characteristic-polynomial statistics).
