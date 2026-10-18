# Exact rank, inertia, and Schatten cancellation for opposing Volterra powers

## Finding
Let \(Jf(x)=\int_0^x f(t)\,dt\) on complex \(L^2(0,1)\). For every integer \(m\ge1\) and \(\lambda\in\mathbb C\) put \(T_{m,\lambda}=J^m+\lambda(J^*)^m\), and let \(s_n\) denote decreasing singular values, counted with multiplicity. Then precisely one parameter, \(\lambda_m=(-1)^{m-1}\), produces finite rank:
\[
\operatorname{rank}T_{m,\lambda}=\begin{cases}m&\lambda=\lambda_m,\\\infty&\lambda\ne\lambda_m.\end{cases}
\]
At every nonexceptional parameter the *sharp coefficient*, not merely the rate, is
\[
\lim_{n\to\infty}(\pi n)^m s_n(T_{m,\lambda})=|1-(-1)^{m-1}\lambda|,
\quad T_{m,\lambda}\in\mathcal S_p\ \Longleftrightarrow\ p>1/m\quad(p>0).
\]
At the exceptional parameter, \(T_{m,\lambda_m}=P_m\) has kernel \((x-t)^{m-1}/(m-1)!\) on the entire unit square. Its \(m\) nonzero eigenvalues have strictly positive product
\[
\prod_{j=1}^{m}\nu_j(P_m)=\frac{\prod_{j=0}^{m-1}(j!)^2}{\prod_{j=0}^{2m-1}j!},
\quad \|P_m\|_{\mathcal S_2}^2=\frac{1}{m(2m-1)((m-1)!)^2}.
\]
For odd \(m=2k+1\), \(P_m\) is self-adjoint and has exactly \(k+1\) positive and \(k\) negative eigenvalues if \(k\) is even, and \(k\) positive and \(k+1\) negative eigenvalues if \(k\) is odd. For even \(m=2k\), \(P_m\) is skew-adjoint with exactly \(k\) eigenvalues on the positive imaginary axis and \(k\) on the negative imaginary axis. All multiplicities are algebraic (which equal geometric multiplicities for this normal finite-rank operator). In particular \(P_m\) is trace zero for \(m\ge2\), and is in every \(\mathcal S_p\) for \(p>0\).

## Assumptions and scope
The Hilbert space is complex \(L^2(0,1)\) with Lebesgue measure. The integration order \(m\) is a positive integer, the parameter \(\lambda\) is arbitrary complex, and Schatten membership for \(0<p<1\) refers to summability of the \(p\)-powers of singular values. The limit keeps \(m\) and \(\lambda\) fixed while \(n\to\infty\). The finite-rank transition for \(m=1\) is classical; the interest of the complete statement is in all higher powers, the exact exceptional inertia and determinant, and the sharp nonexceptional singular-value coefficient. No claim is made for noninteger fractional powers or parameter limits depending on \(n\).

## Proof
**1. Kernel cancellation and rank.** Iterated integration and Fubini give, for each integer \(m\ge1\),
\[
(J^mf)(x)=\frac{1}{(m-1)!}\int_0^x(x-t)^{m-1}f(t)\,dt,
\quad ((J^*)^mf)(x)=\frac{1}{(m-1)!}\int_x^1(t-x)^{m-1}f(t)\,dt.
\]
Let \(P_mf(x)=(m-1)!^{-1}\int_0^1(x-t)^{m-1}f(t)\,dt\). On the two triangles the polynomial identity gives \(P_m=J^m+(-1)^{m-1}(J^*)^m\), so
\[
T_{m,\lambda}=\bigl(1-(-1)^{m-1}\lambda\bigr)J^m+(-1)^{m-1}\lambda P_m.
\]
The range of \(P_m\) lies in polynomials of degree at most \(m-1\). Expanding \((x-t)^{m-1}\), its output coefficients are an invertible anti-diagonal transformation of the first \(m\) moments \(M_j(f)=\int_0^1t^j f(t)\,dt\), \(0\le j<m\). The moments are independent (their Gram matrix is the invertible Hilbert matrix); hence \(\operatorname{rank}P_m=m\). The operator \(J^m\) is injective, since the \(m\)-th weak derivative of \(J^mf\) is \(f\); its rank is infinite. The displayed decomposition therefore gives exactly the asserted exceptional parameter and rank dichotomy.

**2. Sharp singular-value coefficient.** On the Fourier orthonormal basis \(e_n(x)=e^{2\pi inx}\), \(n\in\mathbb Z\), define the compact periodic inverse derivative \(B_m e_n=(2\pi in)^{-m}e_n\) if \(n\ne0\), and \(B_me_0=0\). Its positive singular values are \((2\pi j)^{-m}\), each with multiplicity two, hence \((\pi n)^m s_n(B_m)\to1\). For every \(f\in L^2\), the \(m\)-th distributional derivatives obey \((J^mf)^{(m)}=f\) and \((B_mf)^{(m)}=f-\int_0^1 f\). Thus \((J^m-B_m)f\) is a polynomial of degree at most \(m\), making \(J^m-B_m\) finite rank, at most \(m+1\). The kernel decomposition in Step 1 shows \(T_{m,\lambda}=cB_m+F\) for \(c=1-(-1)^{m-1}\lambda\) and finite-rank \(F\). Singular-value interlacing for a finite-rank perturbation gives, for \(r\ge\operatorname{rank}F\) and \(n>r\),
\[
|c|s_{n+r}(B_m)\le s_n(T_{m,\lambda})\le |c|s_{n-r}(B_m).
\]
For \(c\ne0\) the squeeze proves the sharp limit. The p-series test proves precisely \(p>1/m\); for \(c=0\) the rank-m result applies instead.

**3. Exceptional inertia.** Put \(h_j(x)=x^j\) for \(0\le j<m\), \(H_{ij}=\langle h_j,h_i\rangle=1/(i+j+1)\), and let \(C\) be the real anti-diagonal coefficient matrix
\[
C_{ij}=\begin{cases}(-1)^j\binom{m-1}{j}/(m-1)!,&i+j=m-1,\\0,&\text{otherwise.}\end{cases}
\]
On the polynomial range, the matrix of \(P_m\) is \(A=CH\), and its quadratic form is congruent via the invertible moment map to \(C\). In general \(C^T=(-1)^{m-1}C\), proving \(P_m^*=(-1)^{m-1}P_m\). If \(m=2k+1\), \(C\) is symmetric, its \(k\) off-center two-by-two anti-diagonal blocks each have one positive and one negative eigenvalue, while the central diagonal entry has sign \((-1)^k\). Sylvester's inertia law proves the stated exact signature. If \(m=2k\), \(C\) is skew-symmetric of full rank; \(P_m\) is real skew-adjoint and has \(k\) conjugate pure-imaginary eigenvalue pairs. These statements concern the actual nonzero spectra since the operator has range equal to the invariant polynomial subspace.

**4. Exact determinant, Hilbert--Schmidt norm and trace.** For the same matrix \(A=CH\), the determinant of the Cauchy/Hilbert matrix \(H\) is
\[
\det H=\frac{\prod_{j=0}^{m-1}(j!)^4}{\prod_{j=0}^{2m-1}j!},
\]
while \(\det C=\bigl(\prod_{j=0}^{m-1}j!\bigr)^{-2}\); therefore \(\det A\) is the positive product stated above. Direct integration of the squared kernel yields
\[
\|P_m\|_{\mathcal S_2}^2=\frac{1}{((m-1)!)^2}\int_0^1\!\int_0^1|x-t|^{2m-2}\,dt\,dx=\frac{1}{m(2m-1)((m-1)!)^2}.
\]
For \(m\ge2\) the finite-rank continuous kernel has zero diagonal, so its trace is zero (equivalently \(\operatorname{tr}A=0\)); for \(m=1\) it equals one.

## Verification
The standalone `verify_mixed_volterra.py` runs exact symbolic-rational checks for orders \(1\le m\le12\): coefficient and Gram identities, rank, determinant, trace, Hilbert--Schmidt moments and the normal/skew parity. It also tests \(J^m+(-1)^{m-1}(J^*)^m=P_m\) symbolically on monomials up to degree five for orders \(1\le m\le8\). The program reports `MIXED_VOLTERRA_EXACT_OK 159 checks` when run with Python, SymPy and standard-library modules. This is finite corroboration; rank for every \(m\), the singular asymptotic for \(n\to\infty\), and inertia for every \(m\) are established by the preceding analytic proof.

## Relationship to prior work
Eveson (2004, full HTML text inspected) determines large-power behavior of one-sided Volterra convolutions but not the exceptional opposing-adjoint pencil. Lyubich--Tsedenbayar (2010, entire freely licensed PDF inspected) treats \(\phi(J)\) and its singular-number boundary problems, including earlier results for \(J^m\), rather than a sum of \(J^m\) and \((J^*)^m\). Tuan--Gorenflo (1996) establishes the \((\pi n)^{-m}\) leading behavior of one-sided fractional integrals, making the nonexceptional exponent and its unperturbed coefficient known inputs; the new assertion is the exact cancellation locus and full exceptional spectral classification. Khadkhuu--Tsedenbayar (2018) examines the norm of the \(m=1\) adjoint pencil. Khadkhuu--Tsedenbayar (2020) studies numerical range and norms of real and imaginary parts of \(J^2\), which overlap the \(m=2\) specialization. Neither specialization is claimed as an independent discovery. A related published investigation of reflection-symmetric weighted rank-one-corrected first-order integration obtains radial Schatten majorization, not the higher integer-power polynomial cancellation and spectral inertia here. The novelty comparison concerns the assembled complete higher-order rank, inertia, determinant and sharp nonexceptional coefficient theorem. These sources are not claimed to be exhaustive.

## Limitations
The result concerns fixed integer powers and one complex coefficient. It does not give closed formulas for every individual singular value off the exceptional parameter, nor classify arbitrary linear combinations of different powers. The elementary kernel identity is not itself a claimed novelty, nor are the first- and second-order special cases or the leading singular asymptotics of \(J^m\). The 2020 numerical-range paper was not available for full-text inspection during this comparison, although its abstract supplies known special-case scope. Unindexed work on adjoint-power combinations might contain the same complete classification. No independent audit was conducted.

## References
- S. P. Eveson, *Asymptotic behaviour of iterates of Volterra operators on \(L^p(0,1)\)*, arXiv:math/0409516v1 (27 September 2004), 47G10; full text via https://ar5iv.labs.arxiv.org/html/math/0409516.
- Y. Lyubich and D. Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in \(L_2(0,1)\)*, Studia Mathematica 199 (2010), 171–184, DOI:10.4064/sm199-2-3; open full text https://www.impan.pl/shop/en/publication/transaction/download/product/90183.
- V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461, DOI:10.1080/01630569608816704.
- L. Khadkhuu and D. Tsedenbayar, *A note about Volterra operator*, Mathematica Slovaca 68 (2018), 1117–1120, DOI:10.1515/ms-2017-0173.
- L. Khadkhuu and D. Tsedenbayar, *On the numerical range and operator norm of \(V^2\)*, Operators and Matrices 14 (2020), 251–259, DOI:10.7153/oam-2020-14-18.
