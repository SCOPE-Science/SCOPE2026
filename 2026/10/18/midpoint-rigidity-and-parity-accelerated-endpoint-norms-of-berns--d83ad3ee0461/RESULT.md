# Midpoint rigidity and parity-accelerated endpoint norms of Bernstein overiterates

## Finding
Fix an integer \(n\ge2\). On \(C([0,1])\) with the uniform norm, define the degree-\(n\) Bernstein operator and endpoint interpolation by
\[
(B_nf)(x)=\sum_{j=0}^n\binom nj x^j(1-x)^{n-j}f(j/n),\qquad (Lf)(x)=(1-x)f(0)+xf(1).
\]
For every positive integer \(m\), put \(E_{n,m}=\|B_n^m-L\|_{C\to C}\). Let \(Q_n\) be the \((n-1)\)-square matrix with entries
\[
(Q_n)_{ij}=\binom nj(i/n)^j(1-i/n)^{n-j}\quad(1\le i,j<n),
\]
and let \(b_n\) be the column with entries \(\binom nj2^{-n}\) for \(1\le j<n\). Then
\[
\boxed{E_{n,m}=2b_n^{\mathsf T}Q_n^{m-1}{\bf1}.}
\]
For every \(m\), **the unique evaluation point at which the sharp row norm is attained is \(x=1/2\)**. In particular, \(E_{n,1}=2(1-2^{1-n})\), and \(E_{n,m+1}<E_{n,m}\) for all \(m\ge1\).

Let \(\lambda_r=(n)_r/n^r\) (falling factorial, \(2\le r\le n\)), let \(\pi_n\) be the strictly positive probability row satisfying \(\pi_nQ_n=\lambda_2\pi_n\), and put
\[
H_n=\sum_{j=1}^{n-1}(\pi_n)_j\,\frac jn\left(1-\frac jn\right)>0.
\]
Then, for each fixed \(n\),
\[
\boxed{E_{n,m}=\frac{\lambda_2^m}{2H_n}+R_{n,m},\qquad
R_{n,m}=\begin{cases}0,&n=2,3,\\O_n(\lambda_4^m),&n\ge4.\end{cases}}
\]
The faster remainder is governed by \(\lambda_4\), not by the generic second eigenvalue \(\lambda_3\): reflection symmetry removes *every odd eigenmode* at the unique norming point. At degree four the complete closed form is
\[
\boxed{E_{4,m}=2\left[\frac{25}{21}\left(\frac34\right)^m-\frac4{21}\left(\frac3{32}\right)^m\right] \quad(m\ge1).}
\]
The all-iteration formulas for smaller degrees are \(E_{2,m}=2(1/2)^m\) and \(E_{3,m}=(9/4)(2/3)^m\).

## Assumptions and scope
The degree \(n\ge2\) and iteration count \(m\ge1\) are integers. All norms are ordinary operator norms on the real or complex Banach space \(C([0,1])\) with its supremum norm. No limit in \(n\) is taken in the spectral assertion. An extremizing input is continuous and can be piecewise linear between Bernstein nodes. The matrix \(Q_n\) is substochastic, not a stochastic matrix on its own; it describes survival in the interior states of an absorbing binomial Markov chain.

## Proof
**1. Exact signed-row identity.** On states \(\{0,1/n,\ldots,1\}\), consider the Markov chain with transition probabilities \(\Pr(X_{t+1}=j/n\mid X_t=i/n)=\binom nj(i/n)^j(1-i/n)^{n-j}\), started at any \(X_0=x\in[0,1]\) using the same binomial transition. Its endpoint states are absorbing and \(\mathbb E_xX_t=x\). The signed evaluation measure of \(B_n^m-L\) consists of nonnegative interior masses \(w_j=\Pr_x(X_m=j/n)\) and endpoint masses
\[
w_n-x=-\sum_{1\le j<n}(j/n)w_j,\qquad
w_0-(1-x)=-\sum_{1\le j<n}(1-j/n)w_j.
\]
Thus its total variation is exactly twice its interior mass, and the piecewise-linear continuous input equal to \(+1\) at every interior node and \(-1\) at both endpoints attains that row norm. Therefore
\[
\|B_n^m-L\|=2\max_{0\le x\le1}\Pr_x\{X_m\in(0,1)\}.
\]
The interior survival probability equals \(b_n(x)^{\mathsf T}Q_n^{m-1}{\bf1}\), with \(b_n(x)_j=\binom njx^j(1-x)^{n-j}\).

**2. Uniqueness of the midpoint.** Write \(s_m(x)=\Pr_x\{X_m\in(0,1)\}\). Initially \(s_1(x)=1-x^n-(1-x)^n\) is symmetric about \(1/2\) and strictly concave for \(0<x<1\). Moreover \(s_{m+1}=B_ns_m\). For every concave function \(u\) on the node mesh,
\[
(B_nu)''(x)=n(n-1)\sum_{j=0}^{n-2}\bigl[u((j+2)/n)-2u((j+1)/n)+u(j/n)\bigr]
\binom{n-2}{j}x^j(1-x)^{n-2-j}.
\]
Strict concavity makes every bracket strictly negative; hence \(B_nu\) is strictly concave on \((0,1)\). Reflection commutes with \(B_n\). Induction gives that every \(s_m\) is strictly concave and reflection-symmetric; its sole maximizer is \(1/2\), proving the finite-iteration formula and uniqueness. Each interior state has a strictly positive probability of hitting an endpoint in one step; therefore \(s_{m+1}(1/2)<s_m(1/2)\).

**3. Spectral amplitude and parity.** The degree-preserving action of \(B_n\) on polynomials of degree at most \(n\) is upper triangular in monomials, with distinct eigenvalues \(\lambda_0=\lambda_1=1\) and \(\lambda_r=(n)_r/n^r\) for \(2\le r\le n\). An eigenpolynomial of degree \(r\ge2\) vanishes at both endpoints and, since reflection commutes with \(B_n\), has reflection parity \((-1)^r\). These eigenpolynomials restricted to the interior nodes give a basis of eigenvectors of \(Q_n\). Thus the symmetric subspace has exactly the eigenvalues \(\lambda_2,\lambda_4,\lambda_6,\ldots\).

For \(h_j=(j/n)(1-j/n)\), the binomial variance identity gives \(Q_nh=\lambda_2h\). Every entry of \(Q_n\) is strictly positive, so Perron--Frobenius theory supplies the unique strictly positive normalized left eigenvector \(\pi_n\). The spectral projection of an interior vector \(v\) onto the leading mode is \(h(\pi_nv)/H_n\). For \(v={\bf1}\), this is \(h/H_n\). Since \(b_n(1/2)^{\mathsf T}h=\lambda_2/4\), the exact norm representation becomes
\[
E_{n,m}=2b_n(1/2)^{\mathsf T}\left[\lambda_2^{m-1}\frac h{H_n}+O_n(\lambda_4^{m-1})\right]
=\frac{\lambda_2^m}{2H_n}+O_n(\lambda_4^m).
\]
For \(n=2,3\) there is no nonleading even interior eigenmode, making the formula exact. The degree-four symmetric subspace has just \(\lambda_2=3/4\) and \(\lambda_4=3/32\). Its coefficients follow from the central starting-state survival probabilities \(s_0(1/2)=1\) and \(s_1(1/2)=7/8\), yielding the displayed closed formula.

## Verification
The standalone `check_bernstein_overiteration.py` uses exact rational arithmetic to independently form the binomial transition matrix, calculate signed endpoint rows and interior survival probabilities, test midpoint dominance and strict discrete concavity, compute Perron vectors, and verify the degree-four formula for multiple powers. It passes 940 finite assertions for degrees \(2\) through \(8\), together with additional powers at degree four. These finite checks are **not** a proof of the all-degree theorem; the argument above establishes it.

## Relationship to prior work
Kelisky and Rivlin (1967) proved convergence of Bernstein overiterates to endpoint interpolation. Cooper and Waldron's eigenstructure manuscript gives the full polynomial eigenvalues and parity of eigenpolynomials; these ingredients are treated as known. Nagler and Kähler (2013), and Nagler, Cerejeiras and Forster (2014), give iterated Schoenberg-operator bounds and convergence mechanisms. The present result identifies the **sharp uniform operator error at every finite iteration**, proves that its maximizing evaluation point is uniquely the midpoint, and computes the exact Perron amplitude with an even-parity remainder. The literature checked did not state these combined endpoint conclusions; equivalent older formulations remain possible.

## Limitations
The infinite-iteration asymptotic is for each fixed degree only: the constants implicit in \(O_n\) are not uniform as \(n\to\infty\). No closed elementary formula is supplied for \(H_n\) in arbitrary degree. The norm is a full-space supremum over all continuous inputs, not a smoothness-constrained approximation error. The exact full-text historical priority of several general positive-operator iteration papers could not be settled independently.

## References
- R. P. Kelisky and T. J. Rivlin, *Iterates of Bernstein Polynomials*, Pacific J. Math. 21 (1967), 511–520. https://doi.org/10.2140/pjm.1967.21.511
- S. Cooper and S. Waldron, *The eigenstructure of the Bernstein operator*, author manuscript (1999), and J. Approx. Theory (2000). https://www.math.auckland.ac.nz/~waldron/Preprints/Eigenstructure/eigenstructure.pdf
- J. Nagler and U. Kähler, *A lower bound for the uniform Schoenberg operator*, arXiv:1312.5546v1, 19 December 2013. https://arxiv.org/abs/1312.5546
- J. Nagler, P. Cerejeiras and B. Forster, *Lower bounds for the approximation with variation-diminishing splines*, arXiv:1402.2403v1, 11 February 2014. https://arxiv.org/abs/1402.2403
