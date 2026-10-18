# A finite nonnormality defect for Bernstein–Kantorovich averaging

## Finding
For each integer \(n\ge1\), let \(K_n:L^2(0,1)\to L^2(0,1)\) be the classical Bernstein–Kantorovich operator
\[
(K_nf)(x)=(n+1)\sum_{k=0}^n\binom nk x^k(1-x)^{n-k}
\int_{k/(n+1)}^{(k+1)/(n+1)}f(t)\,dt.
\]
Its nonzero eigenvalues (including algebraic multiplicities) are
\[
\lambda_{n,k}=\frac{n!}{(n-k)!(n+1)^k},\qquad 0\le k\le n.
\]
Its Hilbert–Schmidt energy has the exact closed form
\[
\|K_n\|_{S_2}^2=\frac{n+1}{2n+1}\frac{4^n}{\binom{2n}{n}}.
\]
Define the spectral–singular energy defect
\[
\Delta_n=\|K_n\|_{S_2}^2-\sum_{k=0}^n\lambda_{n,k}^2.
\]
Then \(\Delta_n>0\) for every \(n\ge1\), and the following two-term asymptotic holds:
\[
\boxed{\displaystyle
\Delta_n=\frac16-\frac{5\sqrt\pi}{96\sqrt{n+1}}
+O\!\left(\frac1{n+1}\right).}
\]
In particular, \(\lim_{n\to\infty}\Delta_n=1/6\). The defect is the Hilbert–Schmidt energy not accounted for by the squared moduli of the eigenvalues; for a finite-rank operator it vanishes precisely when the operator is normal. The theorem does not identify \(\Delta_n\) with a metric distance to the set of normal operators.

## Assumptions and scope
The scalar field is real or complex, with Lebesgue measure on \((0,1)\). Polynomial degree is at most \(n\), and bin endpoints have no effect on the integral operator. Singular values and Hilbert–Schmidt norms refer to the Hilbert-space operator on \(L^2(0,1)\), not to a matrix obtained by sampling its kernel. The only nonzero eigenvalues listed above are those of the invariant polynomial range; all other spectral points equal zero. No assumption of self-adjointness or of a normal eigenbasis is made. The asymptotic error constant is absolute as \(n\to\infty\).

## Proof
**Step 1: polynomial eigenvalues.** Write \(N=n+1\). For an integer \(m\ge0\), the average over the \(k\)-th bin of \(t^m\) is
\[
N\int_{k/N}^{(k+1)/N}t^m\,dt
=\frac{(k+1)^{m+1}-k^{m+1}}{(m+1)N^m},
\]
a polynomial in \(k\) of degree \(m\) with leading coefficient \(N^{-m}\). The Bernstein expectation of a degree-\(m\) polynomial in a binomial variable with parameters \((n,x)\) has leading \(x^m\) coefficient \((n)_m\) times the leading coefficient of that polynomial, where \((n)_m=n!/(n-m)!\). Thus \(K_n\) leaves each degree filtration invariant and its diagonal on the ordered monomial basis is \((n)_m/N^m\), \(0\le m\le n\). The functions \(\binom nk x^k(1-x)^{n-k}\) are linearly independent, and their coefficient functionals, the disjoint-bin integrals, are independent, so the range is precisely the \((n+1)\)-dimensional polynomial space. This proves the eigenvalue assertion, with each nonzero eigenvalue simple.

**Step 2: exact Hilbert–Schmidt energy.** The integral kernel is \(N\binom nk x^k(1-x)^{n-k}\) for \(t\in[k/N,(k+1)/N)\). Integrating the squared kernel over the disjoint bins gives
\[
\|K_n\|_{S_2}^2=N\sum_{k=0}^n\binom nk^2 B(2k+1,2n-2k+1)
=\frac{N}{2n+1}\sum_{k=0}^n\frac{\binom nk^2}{\binom{2n}{2k}}.
\]
The identity
\[
\binom{2n}{n}\frac{\binom nk^2}{\binom{2n}{2k}}
=\binom{2k}{k}\binom{2n-2k}{n-k}
\]
reduces the sum by the central-binomial generating function: the coefficient of degree \(n\) in \((1-4z)^{-1/2}(1-4z)^{-1/2}=(1-4z)^{-1}\) is \(4^n\). Hence the exact formula follows.

**Step 3: asymptotic squared-eigenvalue sum.** Put \(h=N^{-1/2}\), \(x=kh\), and
\[
a_{N,k}=\left(\prod_{j=1}^k(1-j/N)\right)^2,\qquad a_{N,0}=1.
\]
For \(0\le k\le\lfloor N^{3/5}\rfloor\), Taylor's formula for \(\log(1-u)\), with \(0\le j/N\le N^{-2/5}\), and exact power sums give
\[
\log a_{N,k}=-x^2-hA(x)-h^2B(x)+R_{N,k},
\quad A(x)=x+\frac{x^3}3,\quad
B(x)=\frac{x^2}2+\frac{x^4}6,
\]
where, for all sufficiently large \(N\),
\[
|R_{N,k}|\le Ch^3(x+x^3+x^5).
\]
Since \(hA(x)=O(N^{-1/5})\) throughout this range, exponentiation and the remainder formula for the exponential yield
\[
a_{N,k}=e^{-x^2}\left[1-hA(x)+h^2Q(x)\right]
+O\left(h^3e^{-x^2}P(x)\right),
\quad Q(x)=\frac{x^4}6+\frac{x^6}{18},
\]
where \(P\) is a fixed polynomial with nonnegative coefficients (for example a sufficiently large constant times \(x+x^2+\cdots+x^9\)). For the omitted range, the inequality \(\log(1-u)\le-u\) gives \(a_{N,k}\le e^{-k(k+1)/N}\le e^{-(kh)^2}\); its total contribution and the corresponding truncated Gaussian model tails decay faster than every power of \(h\). As \(\sum_{k\ge0}e^{-(kh)^2}P(kh)=O(h^{-1})\), summing the local expansion leaves a total error \(O(h^2)\).

The half-line trapezoidal/Euler–Maclaurin summation formula, applied to the three rapidly decreasing smooth functions involved, gives
\[
\sum_{k\ge0}e^{-(kh)^2}=\frac{\sqrt\pi}{2h}+\frac12+O(h^2),
\]
\[
h\sum_{k\ge0}e^{-(kh)^2}A(kh)
=\int_0^\infty e^{-x^2}A(x)\,dx+O(h^2)
=\frac23+O(h^2),
\]
and
\[
h^2\sum_{k\ge0}e^{-(kh)^2}Q(kh)
=h\int_0^\infty e^{-x^2}Q(x)\,dx+O(h^2)
=\frac{11\sqrt\pi}{96}h+O(h^2).
\]
The endpoint corrections used here are respectively \(1/2\), \(0\), and \(0\); integrable derivatives justify the stated errors. Consequently,
\[
\sum_{k=0}^{n}\lambda_{n,k}^2
=\frac{\sqrt\pi}{2h}-\frac16+\frac{11\sqrt\pi}{96}h+O(h^2).
\]

**Step 4: subtraction and strict positivity.** The central-binomial Stirling expansion gives
\[
\frac{4^n}{\binom{2n}{n}}=\sqrt{\pi n}\left(1+\frac1{8n}+O(n^{-2})\right),
\]
and therefore, expressed in \(N=n+1\),
\[
\|K_n\|_{S_2}^2=\frac{\sqrt\pi}{2h}+\frac{\sqrt\pi}{16}h+O(h^3).
\]
Subtracting Step 3 yields \(\Delta_n=1/6-5\sqrt\pi h/96+O(h^2)\).

To see strict positivity for every \(n\ge1\), use the invariant polynomial range \(\mathcal P_n\) and the decomposition \(L^2=\mathcal P_n\oplus\mathcal P_n^\perp\). In block form, \(K_n=\left(\begin{smallmatrix}A&B\\0&0\end{smallmatrix}\right)\). A unitary Schur triangularization of \(A\) gives
\[
\Delta_n=\sum_{i<j}|T_{ij}|^2+\|B\|_{S_2}^2\ge0,
\]
where the diagonal of \(T\) consists of the \(\lambda_{n,k}\). Equality would imply that \(K_n\) is normal and, because its eigenvalues are real and nonnegative, self-adjoint. But its real kernel is asymmetric: for \(0<x<t<1/N\), \(\kappa_n(x,t)=N(1-x)^n\) and \(\kappa_n(t,x)=N(1-t)^n\), unequal on a set of positive measure. Thus \(\Delta_n>0\).

## Verification
The standalone script `check_kantorovich.py` uses exact rational arithmetic to verify the closed Hilbert–Schmidt identity and positivity for \(1\le n\le13\), reconstructs finite bin-averaging matrices and their power traces for small \(n\), and checks the two-term asymptotic numerically at several larger dimensions. Exact finite checks test formulas but do not replace the analytic estimates in Steps 3–4. The script has no external package dependencies.

## Relationship to prior work
The classical operators and their polynomial moment structure are established in the Bernstein–Kantorovich approximation literature. Gonska, Heilmann, and Raşa (2011) study higher-order Kantorovich modifications and approximation moments. Păltănea (2012) treats generalizations and shape preservation. Acu and Gonska (2019) give detailed approximation and Voronovskaya estimates for the classical operators. Obie, Taebenu, Gunadi, and Hakim (2023) investigate Lebesgue-space boundedness and convergence. These sources provide the operator context but the inspected results do not state the Hilbert–Schmidt-versus-eigenvalue energy defect or its constant \(1/6\). Related Bernstein collocation and Bernstein–Durrmeyer spectral-energy formulas address different operators; self-adjoint spectral traces do not imply a nonnormality defect for the classical Kantorovich integral operator.

## Limitations
The theorem concerns the one-dimensional unweighted, classical, equal-bin Bernstein–Kantorovich family only. It does not describe individual singular values or the distance to normal operators in operator or Hilbert–Schmidt norm. The quantitative remainder is \(O(n^{-1})\); no sign or monotonicity assertion for the remainder is proved. The 2011 higher-order Kantorovich paper could not be inspected in full; an unindexed or otherwise inaccessible equivalent historical derivation remains a bibliographic possibility. No independent audit has been performed.

## References
1. H. Gonska, M. Heilmann and I. Raşa, “Kantorovich Operators of Order k,” *Numerical Functional Analysis and Optimization* **32** (2011), 717–738, DOI: 10.1080/01630563.2011.580877 (published online 2011-05-23).
2. R. Păltănea, “A Generalization of Kantorovich Operators and a Shape-Preserving Property of Bernstein Operators,” *Bulletin of the Transilvania University of Braşov*, Ser. III, **5(54)** (2012), 65–68, https://webbut.unitbv.ro/index.php/Series_III/article/download/2051/1764/3774 (classical formula on p. 65; the paper's generalization has an appended erratum).
3. A.-M. Acu and H. Gonska, “Classical Kantorovich Operators Revisited,” arXiv:1904.11135v1 (2019-04-25), https://arxiv.org/pdf/1904.11135.
4. M. V. Obie, E. A. Taebenu, R. Gunadi and D. I. Hakim, “Revisiting Kantorovich Operators in Lebesgue Spaces,” *Journal of the Indonesian Mathematical Society* (2023), https://jims-a.org/index.php/jimsa/article/download/1596/371/6352.
