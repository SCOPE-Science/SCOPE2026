# A spectral-gap characterization of smooth points of the numerical-radius weighted-shift norm

## Finding
Let \(\mathbb F\) be \(\mathbb R\) or \(\mathbb C\). Define the numerical-radius norm \(N(a)=w(T_a)\) for every \(a=(a_n)_{n\ge1}\in\ell_\infty(\mathbb F)\), where the unilateral weighted shift \(T_a e_n=a_ne_{n+1}\) acts on complex \(\ell_2\). Suppose that every \(a_n\ne0\) and that \(|a_n|\to b>0\). Then

\[
N\text{ is real-Fréchet differentiable at }a\quad\Longleftrightarrow\quad N(a)>b.
\]

If \(N(a)=b\), the norm fails even real-Gâteaux differentiability at \(a\). When \(N(a)>b\), let \(u=(u_n)_{n\ge1}\) be the unique positive, unit, top eigenvector of the Jacobi matrix whose \((n,n+1)\) and \((n+1,n)\) entries are \(|a_n|/2\). Its associated derivative is

\[
DN(a)[h]=\sum_{n\ge1}u_nu_{n+1}
\operatorname{Re}\left(\frac{\overline{a_n}h_n}{|a_n|}\right)
\qquad\bigl(h\in\ell_\infty(\mathbb F)\bigr).
\]

For the one-defect weights \(a=(t,1,1,\ldots)\), \(t>0\), the criterion becomes the exact threshold \(t>\sqrt2\). In this regime its derivative in the first coordinate is

\[
\frac{\partial N}{\partial t}=
\frac{t(t^2-2)}{2(t^2-1)^{3/2}}.
\]

The numerical-radius formula giving this last scalar derivative was known; the full differentiability dichotomy (including failure of Gâteaux differentiability at and below the threshold) is the asserted finding.

## Assumptions and scope
The norm is defined on the entire real or complex Banach space \(\ell_\infty(\mathbb F)\), regarded over \(\mathbb R\) when differentiability is discussed. The theorem concerns a point \(a\) with \(a_n\ne0\) for all \(n\) and \(|a_n|\to b>0\). These assumptions imply \(m:=\inf_n|a_n|>0\): sufficiently late moduli exceed \(b/2\), and finitely many remaining moduli are positive. No summability rate of \(|a_n|-b\) is assumed. The differentiability conclusion is for perturbations in the **full** uniform norm, not merely perturbations that preserve convergence. The theorem does not classify weights with infinitely many zeros, or weights without a nonzero modulus limit.

Write \(J_a\) for the bounded real-symmetric tridiagonal operator on real \(\ell_2\), with zero diagonal and off-diagonals \(|a_n|/2\). Its Rayleigh maximum is \(\sup\sigma(J_a)\). Throughout, a derivative in the complex case is real-linear, as appropriate for a real-valued norm.

## Proof
**1. Jacobi reduction and the spectral edge.** A diagonal unitary eliminates the phases of the unilateral shift. The resulting nonnegative shift has circular numerical range, and taking real parts yields

\[
N(a)=\sup_{\|x\|_2=1}\sum_{n\ge1}|a_n|\,|x_n||x_{n+1}|
=\sup\sigma(J_a).
\]

In particular, \(N(a+h)\le N(a)+\|h\|_\infty\) and \(N(h)\le\|h\|_\infty\). Let \(J_b\) have all off-diagonal entries equal to \(b/2\). Because \(|a_n|-b\to0\), \(J_a-J_b\) is a norm limit of finite-rank operators, hence compact. The constant Jacobi operator has essential spectrum \([-b,b]\); equivalently, long constant-tail Rayleigh vectors show \(N(a)\ge b\). The spectrum of \(J_a\) above \(b\), if nonempty, consists of isolated finite-multiplicity eigenvalues.

**2. Simplicity, positivity, and a spectral gap.** Suppose \(r=N(a)>b\). The maximum \(r\) is an eigenvalue. An eigenvector for a tridiagonal Jacobi operator with every off-diagonal nonzero is uniquely determined by its first coordinate through the three-term recurrence, so the eigenspace is one-dimensional. A Rayleigh maximizer can be replaced by its coordinatewise absolute value without decreasing its quotient. Since \(r\) is the upper spectral bound, equality persists, giving a nonnegative eigenvector. The eigenvalue equation and strictly positive off-diagonals imply that all its coordinates are strictly positive. Thus there is a unique positive normalized eigenvector \(u\). Simplicity and isolation give a positive gap \(\delta=r-\sup\sigma(J_a|_{u^\perp})\).

**3. Uniform Fréchet estimate and derivative.** Let \(E\) be any real-symmetric perturbation with \(\|E\|<\delta/4\). Write every unit vector as \(v=\alpha u+z\) with \(z\perp u\). Applying the spectral gap to \(\langle J_av,v\rangle\) and estimating the cross term of \(\langle Ev,v\rangle\) gives, for an absolute constant \(C\),

\[
0\le \sup\sigma(J_a+E)-r-\langle Eu,u\rangle
\le C\|E\|^2/\delta.
\]

The coordinatewise modulus map is real-Fréchet differentiable at \(a\), **uniformly** because \(m>0\): for \(\|h\|_\infty<m/2\),

\[
\left\|\,|a+h|-|a|-
\left(\operatorname{Re}\frac{\overline{a_n}h_n}{|a_n|}\right)_{n\ge1}\right\|_\infty
\le C_m\|h\|_\infty^2.
\]

Consequently \(J_{a+h}-J_a\) is the tridiagonal operator whose off-diagonals are \(\operatorname{Re}(\overline{a_n}h_n/|a_n|)/2\), up to an operator-norm error of order \(\|h\|_\infty^2\). Since \(\langle Eu,u\rangle\) for a Jacobi perturbation with off-diagonals \(d_n/2\) is \(\sum_n d_nu_nu_{n+1}\), the two quadratic remainders prove the asserted Fréchet derivative. It is bounded because \(\sum_nu_nu_{n+1}\le\|u\|_2^2=1\).

**4. No Gâteaux derivative at the spectral edge.** Now let \(N(a)=b\). Set \(s_n=(-1)^{\lfloor\sqrt n\rfloor}\) and \(h_n=a_ns_n/|a_n|\). The sign sequence has arbitrarily long positive and negative constant blocks whose starting indices tend to infinity. For \(0<\varepsilon<m\), and either sign \(\tau\in\{-1,1\}\), the weights of \(a+\tau\varepsilon h\) have modulus \(|a_n|+\tau\varepsilon s_n\). On arbitrarily long remote blocks with \(\tau s_n=1\), these moduli are uniformly as close to \(b+\varepsilon\) as desired. Taking the positive top sine vector on each finite chain gives

\[
N(a+\tau\varepsilon h)\ge b+\varepsilon.
\]

The reverse inequality follows from the norm triangle inequality and \(N(h)\le\|h\|_\infty=1\). Hence **both** \(N(a+\varepsilon h)=b+\varepsilon\) and \(N(a-\varepsilon h)=b+\varepsilon\). The one-sided directional slopes are \(+1\) and \(-1\), so the two-sided Gâteaux derivative does not exist.

**5. Exact one-defect boundary.** For \(a=(t,1,1,\ldots)\) with \(t>0\), any eigenvalue \(r>1\) of \(J_a\) has a decaying tail geometric ratio \(q\in(0,1)\) obeying \(2r=q+q^{-1}\). Its first two recurrence equations reduce to \(q^2=(t^2-1)^{-1}\), which admits such a \(q\) precisely when \(t>\sqrt2\). Then \(r=(q+q^{-1})/2\). Otherwise the spectral upper edge is \(1\). Thus

\[
N(t,1,1,\ldots)=
\begin{cases}
1,&0<t\le\sqrt2,\\
\frac12\left(\sqrt{t^2-1}+\frac1{\sqrt{t^2-1}}\right),&t>\sqrt2.
\end{cases}
\]

Differentiating the second scalar expression gives the coordinate derivative stated above. Step 4, rather than the scalar formula, establishes the failure of full Gâteaux smoothness when \(0<t\le\sqrt2\).

## Verification
The standalone `check.py` computes top eigenvalues of finite Jacobi sections, checks monotone convergence toward the established one-defect formula at several exponents and section sizes, compares finite-section Hellmann–Feynman derivatives to exact derivatives and finite differences, and exercises long alternating-block directions and nonconstant converging positive weights. Run with `python check.py`, with NumPy and SciPy installed. The observed result is `VERIFY_OK finite_section_checks=86 one_defect_cases=7 Frechet_directional_cases=3 alternating_block_sizes=2 infinite_proof_required=True`. These numerical checks are consistency tests only; the preceding argument supplies all infinite-dimensional assertions.

## Relationship to prior work
Sharif (arXiv:2303.00876, first posted 2 March 2023), §§1–5, studies \(w(T_a)\) as a norm on \(\ell_\infty\), derives inequalities relating it to Banach limits and compares operator norms. The introduction explicitly cites the classical Berger–Stampfli one-defect radius formula used as a boundary example here. Undrakh, Nakazato, Vandanjav and Chien (2015) investigate eigenvalues and exact radii when finitely many weights differ from a constant tail. Roy and Sain (2021) study numerical-radius smoothness for operator spaces, especially finite-dimensional spaces. None of the materially inspected results supplies the present necessary-and-sufficient Fréchet/Gâteaux smoothness characterization for **all** nonvanishing convergent-modulus weights, including the full-\(\ell_\infty\) tail perturbations. This comparison does not exclude unknown equivalent formulations or stronger general theorems elsewhere.

## Limitations
The theorem excludes zero coordinates and nonconverging or zero-limit moduli, and does not classify the full numerical-radius norm on all \(\ell_\infty\). The one-defect numerical-radius values themselves are historical facts, not claimed new. Finite-dimensional checks cannot certify the spectral-edge argument. An older paper on numerical ranges of weighted shifts was only partially accessible, and unindexed spectral perturbation literature could contain an equivalent special case; independent literature verification remains desirable.

## References
1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876v1 (first posted 2023-03-02), https://arxiv.org/abs/2303.00876.
2. B. Undrakh, H. Nakazato, A. Vandanjav and M.-T. Chien, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra 30 (2015), 944–963, doi:10.13001/1081-3810.2821.
3. S. Roy and D. Sain, *Numerical radius and a notion of smoothness in the space of bounded linear operators*, arXiv:2107.03490 (2021), https://arxiv.org/abs/2107.03490.
4. C. A. Berger and J. G. Stampfli, *Mapping theorems for the numerical range*, American Journal of Mathematics 89 (1967), 1047–1055 (one-defect formula as cited by Sharif).
