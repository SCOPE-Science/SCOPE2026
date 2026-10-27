# Sharp Riesz-stability threshold despite exponential mixing for non-autonomous inner dynamics

## Finding
Let \(\mathbb D\) be the unit disc, \(\mathbb T=\partial\mathbb D\), and \(m\) normalized Haar measure on \(\mathbb T\). Let \(f_n:\mathbb D\to\mathbb D\) be centered inner functions, \(f_n(0)=0\), with \(c_n=f_n'(0)\) and \(|c_n|<1\). Define \(F_0(z)=z\) and \(F_n=f_n\circ F_{n-1}\) for every integer \(n\ge1\).

The boundary orbit functions \(\{F_n:n\ge0\}\) form a Riesz sequence in \(L^2(\mathbb T,m)\) **if and only if** \(q:=\sup_{n\ge1}|c_n|<1\). More precisely, for every integer \(N\ge0\) and every complex coefficient vector \((a_0,\ldots,a_N)\), if \(q<1\),

\[
\frac{1-q}{1+q}\sum_{j=0}^{N}|a_j|^2
\le \left\|\sum_{j=0}^{N}a_jF_j\right\|_{L^2(m)}^2
\le \frac{1+q}{1-q}\sum_{j=0}^{N}|a_j|^2.
\]

These two bounds are jointly sharp as **universal bounds** over all eligible centered inner-function sequences satisfying \(\sup_n|c_n|\le q\), for every \(q\in[0,1)\). The autonomous centered degree-two Blaschke product \(f(z)=z(z+q)/(1+qz)\) attains both extremal bounds as limits of finite vectors. For \(q=0\), the orbit is orthonormal.

For every finite prefix, the covariance matrix \(C^{(N)}_{ij}:=\int_{\mathbb T}F_i(\zeta)\overline{F_j(\zeta)}\,dm(\zeta)\) satisfies, when \(i>j\),

\[
C^{(N)}_{ij}=\prod_{k=j+1}^{i}c_k,\qquad
C^{(N)}_{ii}=1,\qquad
C^{(N)}_{ij}=\overline{C^{(N)}_{ji}}\quad(i<j).
\]

Writing \(L_{nn}=1\), \(L_{n,n-1}=-c_n\) for \(1\le n\le N\), all other entries zero, and \(D=\operatorname{diag}(1,1-|c_1|^2,\ldots,1-|c_N|^2)\), one has

\[
(C^{(N)})^{-1}=L^*D^{-1}L,
\qquad
\det C^{(N)}=\prod_{n=1}^{N}(1-|c_n|^2).
\]

There are degree-two Blaschke sequences for which the 2026 non-autonomous inner-function criteria imply **exponential strong mixing and positive lower metric entropy**, yet the Gram matrices of \((F_0,\ldots,F_N)\) have condition numbers at least \(2^N\) for infinitely many horizons. Hence neither of those two strong dynamical properties implies uniform Riesz stability of the orbit observables.

## Assumptions and scope
An inner function means a bounded analytic self-map of \(\mathbb D\) whose radial boundary values are unimodular almost everywhere. Composition preserves innerness for centered inner functions. The boundary functions are identified up to Haar-null sets, and all norms and inner products are in complex \(L^2(m)\). The Riesz property means that a single pair of positive finite bounds works for **all finitely supported** complex coefficient vectors. No independence or Gaussianity assumption is made. The main theorem applies to arbitrary centered inner maps with \(|c_n|<1\); its sharpness and separation examples use degree-two rational Blaschke maps.

## Proof
**1. Haar preservation and exact covariance.** If \(g\) is centered inner, then \(g_\#m=m\). Indeed, every positive Fourier coefficient of the pushforward is \(\int_{\mathbb T}g(\zeta)^k\,dm(\zeta)=g(0)^k=0\), for integers \(k\ge1\); the negative coefficients vanish by conjugation. Uniqueness of Fourier coefficients gives Haar preservation. Thus each \(F_j\) has Haar boundary law. For \(i>j\), set \(G_{i,j}=f_i\circ\cdots\circ f_{j+1}\). Since \(F_i=G_{i,j}\circ F_j\),

\[
\int F_i\overline{F_j}\,dm
=\int_{\mathbb T}G_{i,j}(w)\overline w\,dm(w)
=G_{i,j}'(0)=\prod_{k=j+1}^{i}c_k.
\]

The second equality is the first Taylor coefficient of the bounded analytic function \(G_{i,j}\); the last is the chain rule at its common fixed point. This proves the covariance formula.

**2. Orthogonal innovations and the exact inverse.** Put \(E_0=F_0\) and \(E_n=F_n-c_nF_{n-1}\) for \(n\ge1\). For every \(j<n\), the covariance identity gives \(\langle E_n,F_j\rangle=0\) with the convention \(\langle U,V\rangle=\int U\overline V\,dm\). Hence \(E_0,\ldots,E_N\) are mutually orthogonal. Their squared norms are \(1\) for \(n=0\), and \(1-|c_n|^2\) for \(n\ge1\). In matrix form \(LC^{(N)}L^*=D\). Because \(L\) is unipotent and \(D\) has strictly positive diagonal, both the precision and determinant formulas follow. These are exact finite-dimensional identities, not limiting approximations.

**3. Universal Riesz bounds.** Suppose \(q<1\). By the covariance product formula, \(|C^{(N)}_{ij}|\le q^{|i-j|}\). The Schur row-sum bound gives \(\|C^{(N)}\|\le 1+2\sum_{k\ge1}q^k=(1+q)/(1-q)\). Conversely, \(D^{-1}\le(1-q^2)^{-1}I\) and \(\|L\|\le1+q\), since \(L\) is identity minus a weighted backward shift of norm at most \(q\). Therefore

\[
\|(C^{(N)})^{-1}\|\le\frac{(1+q)^2}{1-q^2}=\frac{1+q}{1-q},
\]

which yields the matching lower bound. These Hermitian spectral estimates give the stated inequalities for \(\sum a_jF_j\) (conjugating a coefficient vector does not change its Euclidean norm).

If \(\sup_n|c_n|=1\), choose indices along which \(|c_n|\to1\). The two-term coefficients in \(F_n-c_nF_{n-1}\) have squared Euclidean norm \(1+|c_n|^2\ge1\), while the resulting boundary function has squared norm \(1-|c_n|^2\to0\). No uniform lower Riesz bound can exist. This proves the if-and-only-if assertion.

**4. Optimality of both universal constants.** For \(0\le q<1\), take \(f(z)=z(z+q)/(1+qz)\) at every time; then \(f'(0)=q\), and the covariance is the positive Toeplitz matrix \(C_{ij}=q^{|i-j|}\). The Rayleigh quotient for the constant length-\(N+1\) vector tends to \(1+2\sum_{k\ge1}q^k=(1+q)/(1-q)\); that for the alternating-sign vector tends to \(1+2\sum_{k\ge1}(-q)^k=(1-q)/(1+q)\). Thus neither constant can be improved uniformly. The argument includes \(q=0\).

**5. Exponential mixing and entropy without uniform Gram stability.** For positive integers \(n\), set

\[
q_n=
\begin{cases}
1-2^{-2^k},&n=2^k\text{ for an integer }k\ge1,\\
1/2,&\text{otherwise},
\end{cases}
\qquad f_n(z)=z\frac{z+q_n}{1+q_n z}.
\]

Every \(f_n\) is a centered degree-two Blaschke product with \(f_n'(0)=q_n\). In particular \(1/2\le q_n<1\), \(\sup_n q_n=1\), and

\[
\prod_{n=1}^{N}q_n\le2^{-N+\lfloor\log_2N\rfloor}\le2^{-N/2}
\quad\text{for every integer }N\ge2.
\]

The mixing theorem of Evdoridou–Fagella–Rippon–Stallard (Theorem A of arXiv:2609.31476v1) applies with \(a=1/2\), hence its arc-versus-measurable-set mixing discrepancy is at most \(K\bigl(\prod_{n\le N}q_n\bigr)^{1/18}\le K2^{-N/36}\), for a fixed finite constant \(K\). Further, the exceptional times have zero density, so \(N^{-1}\sum_{n=1}^{N}(1-q_n)\to1/2\). Theorem C(a) of the same paper therefore supplies strictly positive lower metric entropy.

Nevertheless, for each power of two \(N=2^k\), the principal covariance block indexed by \((N-1,N)\) equals \(\begin{psmallmatrix}1&q_N\\q_N&1\end{psmallmatrix}\), whose smaller eigenvalue is exactly \(1-q_N=2^{-N}\). By eigenvalue interlacing, \(\lambda_{\min}(C^{(N)})\le2^{-N}\). The diagonal of \(C^{(N)}\) is identically \(1\), hence \(\lambda_{\max}(C^{(N)})\ge1\). Consequently

\[
\operatorname{cond}_2(C^{(N)})\ge2^N
\quad\text{whenever }N=2^k,\ k\ge1.
\]

This proves the claimed separation, with both entropy and exponential mixing supplied by precisely stated published theorems and the Gram instability proved here.

## Verification
The exact-rational checker tests four finite Gram/precision identities (including a complex derivative), nine exact composition derivative products, six exponentially small two-point Gram eigenvalues, and numerical convergence toward the two universal sharp constants. Independent Haar-grid quadrature for three nonidentical Blaschke maps reproduces the predicted covariance with maximal error below \(10^{-10}\) on 65,536 equally spaced boundary points. Run \(\texttt{python CHECKER.py}\) with Python, SymPy, and NumPy; the expected output is supplied in \(\texttt{CHECKER_OUTPUT.txt}\). These finite checks do not establish the universal Riesz statement, its sharpness, or the mixing and entropy claims; those rest on the proof above and the cited theorems.

## Relationship to prior work
Evdoridou, Fagella, Rippon and Stallard (2026, arXiv:2609.31476v1) establish non-autonomous mixing and entropy conditions for centered inner maps. Their Theorems A and C are used here; their paper does not give a characterization of Riesz stability of the boundary orbit functions, and its conclusions alone do not imply that stability. Nicolau (2021, arXiv:2103.07238v1) established \(L^2\)-bounds for **autonomous** iterates of a single centered inner map, including the familiar constants governed by \(|f'(0)|\). Those autonomous bounds, and the covariance calculation underlying them, are not claimed as new. The contribution here is the exact **non-autonomous** if-and-only-if classification, universal sharp simultaneous bounds, the tridiagonal finite precision description, and the positive-entropy/exponentially-mixing counterexample with exponential Gram ill-conditioning. Earlier work on shrinking targets for non-autonomous inner maps studies a different dynamical observable, not this Gram classification. A 2026 indexed finite-tail result concerns the opposite, summable-derivative-deficit regime.

## Limitations
The theorem concerns one distinguished sequence of boundary observables \(F_n\), rather than the full transfer-operator spectrum or all possible observables. The exact Gram law does not imply Gaussianity, probabilistic independence, or uniform conditional mixing. The entropy statement in the example is a strictly positive bound obtained from the 2026 source theorem, not an exact entropy evaluation. Near-singularity of the Gram matrices measures linear dependence of these observables, not a failure of dynamical entropy or strong mixing. The result does not assert novelty of the classical autonomous estimates, the general Toeplitz or weighted-autoregression linear algebra, or any theorem already proved in the cited literature.

## References
1. V. Evdoridou, N. Fagella, P. J. Rippon, G. M. Stallard, *Non-autonomous dynamics of inner functions: mixing and entropy*, arXiv:2609.31476v1 (September 25, 2026), especially Theorems A and C and Section 6, https://arxiv.org/html/2609.31476v1 .
2. A. Nicolau, *Convergence of linear combinations of iterates of an inner function*, arXiv:2103.07238v1 (March 12, 2021), especially the exact \(L^2\) covariance calculation and the autonomous norm bounds, https://arxiv.org/abs/2103.07238 .
3. A. M. Benini, V. Evdoridou, N. Fagella, P. J. Rippon, G. M. Stallard, *Shrinking targets and recurrent behaviour for forward compositions of inner functions*, arXiv:2405.11866 (May 20, 2024), https://arxiv.org/abs/2405.11866 .
