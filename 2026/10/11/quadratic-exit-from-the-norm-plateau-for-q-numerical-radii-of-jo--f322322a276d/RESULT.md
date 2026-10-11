# Quadratic exit from the norm plateau for \(q\)-numerical radii of Jordan shifts

## Finding
For every integer \(n\ge4\), let \(J_n\in M_n(\mathbb C)\) be the nilpotent Jordan shift, with \(J_ne_{j+1}=e_j\) and \(J_ne_1=0\). For \(0\le q\le1\), define its \(q\)-numerical radius by
\[
r_n(q)=\max\big\{|\langle J_nx,y\rangle|:\ \|x\|_2=\|y\|_2=1,\ \langle x,y\rangle=q\big\}.
\]
Put \(s_n(t)=\|J_n+tI_n\|_2\), \(q_n=\cos(\pi/n)\), and \(a_n=\frac{n+2}{n}\sin^2(\pi/n)\). Then the **entire radius profile** is determined by the one-variable singular-norm envelope
\[
\boxed{\ r_n(q)=\inf_{t\ge0}\big(s_n(t)-qt\big),\qquad 0\le q\le1.\ }
\]
The sharp plateau and its quadratic exit are
\[
\boxed{\ r_n(q)=1\ \Longleftrightarrow\ 0\le q\le q_n,\qquad
\lim_{\delta\downarrow0}\frac{1-r_n(q_n+\delta)}{\delta^2}
=\frac{n}{2(n+2)\sin^2(\pi/n)}.\ }
\]
For \(q_n<q<1\), a unique \(t=t_n(q)>0\) satisfies \(s_n'(t)=q\), and \(r_n(q)=s_n(t)-qt\). On this interval \(r_n\) is differentiable and strictly concave. At the endpoint, \(r_n(1)=\cos(\pi/(n+1))\). In particular, the quadratic coefficient is \(2/3\) when \(n=4\), and it is asymptotic to \(n^2/(2\pi^2)\) as \(n\to\infty\).

## Assumptions and scope
The field is \(\mathbb C\); \(n\) is an arbitrary but fixed integer at least \(4\), and \(q\) is real in the closed interval \([0,1]\). The inner product is \(\langle v,w\rangle=w^*v\), linear in its first slot; norms on vectors are Euclidean and on matrices are induced spectral norms. The symbol \(J_n\) denotes the unweighted nilpotent shift, not an arbitrary nilpotent or weighted Jordan block. Since \(q_n<1\), the limit \(\delta\downarrow0\) only involves admissible \(q_n+\delta\le1\). The infimum at \(q=1\) is generally approached as \(t\to\infty\). The statement applies also to \(n=2,3\) by the same proof, but these dimensions are excluded from the novelty claim because the low-dimensional cases have earlier literature coverage.

## Proof
**Step 1: upper envelope and plateau.** For all admissible unit vectors \(x,y\) and every \(t\ge0\),
\[
\operatorname{Re}\langle J_nx,y\rangle
=\operatorname{Re}\langle (J_n+tI_n)x,y\rangle-tq
\le s_n(t)-tq.
\]
A diagonal unitary conjugates \(J_n\) to every phase multiple of itself. Consequently the maximum of the real part over all admissible pairs equals \(r_n(q)\), proving the envelope's upper inequality. Taking \(t=0\) gives \(r_n(q)\le1\). The subspace of vectors \(x=(0,v_1,\ldots,v_{n-1})\) satisfies \(\|J_nx\|_2=1\) whenever \(\|v\|_2=1\). With \(y=J_nx\), one has \(\langle x,y\rangle\in W(J_{n-1})\), up to conjugation, and every member of that numerical range arises. Diagonal phase symmetry and the tridiagonal eigenvalue formula give
\[
W(J_{n-1})=\{z\in\mathbb C:|z|\le\cos(\pi/n)\}.
\]
Thus every \(q\in[0,q_n]\) has an admissible pair achieving \(\langle J_nx,y\rangle=1\). If \(r_n(q)=1\), the equality case of Cauchy--Schwarz and the norm bound for \(J_n\) give \(y=\zeta J_nx\) with \(\|J_nx\|_2=1\), forcing \(x_1=0\) and \(|q|\le q_n\). Therefore the plateau is **exactly** \([0,q_n]\).

**Step 2: attainment of the envelope after the plateau.** For \(t>0\), the Hermitian matrix \((J_n+tI_n)^*(J_n+tI_n)\) is a real symmetric irreducible tridiagonal matrix with positive off-diagonal entries \(t\). Its top eigenvalue is simple and has a strictly positive unit eigenvector \(x(t)\). The corresponding unit left singular vector \(y(t)=(J_n+tI_n)x(t)/s_n(t)\) is also positive. Differentiability of a simple top singular value gives
\[
s_n'(t)=\langle x(t),y(t)\rangle\in(0,1).
\]
The norm of the affine matrix \(J_n+tI_n\) is strictly convex in \(t\ge0\). Indeed, equality in a nontrivial norm-convexity secant would force a common norming pair \(x,y\) at both endpoints, hence \((t_2-t_1)x=(s_n(t_2)-s_n(t_1))y\). Both vectors must be parallel. The common norming equation would then make \(x\) an eigenvector of the nilpotent \(J_n\) with \(s_n(t_i)=t_i\), contradicting \(s_n(t_i)>t_i\). This proves strict convexity. Its right derivative at zero is \(s_n'(0+)=\cos(\pi/n)=q_n\), as calculated in Step 3; and \(s_n'(t)\to1\) as \(t\to\infty\), since \(t+\cos(\pi/(n+1))\le s_n(t)\le t+1\). Consequently for each \(q\in(q_n,1)\) there is a unique \(t>0\) with \(s_n'(t)=q\). The positive singular vectors are then admissible and satisfy
\[
\langle J_nx(t),y(t)\rangle=s_n(t)-tq>0.
\]
This gives the reverse envelope inequality and the unique-minimizer assertion. Strict convexity yields that \(q\mapsto t_n(q)\) strictly increases and \(r_n'(q)=-t_n(q)\), so \(r_n\) is strictly concave on \((q_n,1)\). For \(q=1\), necessarily \(x=y\), whence \(r_n(1)=w(J_n)=\cos(\pi/(n+1))\). Uniform first-order expansion of \(\|I_n+t^{-1}J_n\|_2\) as \(t\to\infty\) yields \(s_n(t)-t\to w(J_n)\), completing the envelope identity at this endpoint.

**Step 3: singular-norm perturbation at the plateau edge.** Put \(T_{n-1}=J_{n-1}+J_{n-1}^*\) and \(E_{11}=e_1e_1^*\) on \(\mathbb C^{n-1}\). In the decomposition \(\mathbb C e_1\oplus\operatorname{span}(e_2,\ldots,e_n)\),
\[
(J_n+tI_n)^*(J_n+tI_n)=
\begin{pmatrix}t^2&t e_1^*\\t e_1&(1+t^2)I_{n-1}+tT_{n-1}\end{pmatrix}.
\]
The top eigenvalue approaches \(1\) for \(t\downarrow0\). Eliminating the first coordinate by the Schur complement gives, for this eigenvalue, the effective lower-block equation
\[
\lambda z=\big[I_{n-1}+tT_{n-1}+t^2(I_{n-1}+E_{11})+O(t^3)\big]z.
\]
The simple largest eigenvalue of \(T_{n-1}\) is \(2q_n\), with normalized eigenvector \(v_j=\sqrt{2/n}\sin(j\pi/n)\), \(1\le j\le n-1\). Standard simple-eigenvalue perturbation (after dividing the lower block by \(t\)) therefore gives
\[
\lambda_{\max}=1+2q_n t+
\left(1+\frac2n\sin^2(\pi/n)\right)t^2+O(t^3).
\]
Taking the square root and using \(1-q_n^2=\sin^2(\pi/n)\) yields the **explicit second-order expansion**
\[
s_n(t)=1+q_nt+\frac{a_n}{2}t^2+O(t^3),\qquad
 a_n=\frac{n+2}{n}\sin^2(\pi/n)>0.
\]
Thus \(s_n'(0+)=q_n\). By analytic perturbation of the simple positive spectral branch after the first-order eigenvalue splitting, \(s_n'(t)=q_n+a_nt+O(t^2)\) for small positive \(t\). If \(q=q_n+\delta\) with \(\delta>0\) small, the unique minimizer satisfies \(t_n(q)=\delta/a_n+O(\delta^2)\). Substituting into \(r_n(q)=s_n(t_n(q))-qt_n(q)\) proves
\[
r_n(q_n+\delta)=1-\frac{\delta^2}{2a_n}+O(\delta^3).
\]
This proves the claimed limit and concludes the argument.

## Verification
The proof is valid for each integer \(n\ge4\) without numerical truncation or enumeration. The standalone file `verify_qshift.py` checks \(n=4,5,6,7,8\) with NumPy and SciPy. It compares the one-variable variational minimum and independently computed singular norms against the exact plateau coefficient and the derived expansion for several small positive perturbations. Running `python verify_qshift.py` returned `JORDAN_Q_RADIUS_EDGE_NUMERICAL_CHECK_OK`. These tests are finite consistency checks only; the infinite family and strict inequalities are proved analytically above.

## Relationship to prior work
Kaunisto--O'Loughlin--Virtanen (arXiv:2610.00443, first public version 30 September 2026) study scaled \(q\)-numerical ranges, unitary dilation, and complete spectral-set constants; their stated theorems do not determine \(r_n(q)\) for nilpotent shifts. The earlier Chien--Nakazato paper proves a unit-radius interval for the \(3\times3\) shift, which corresponds to \(n=3\) and is expressly excluded from the new dimension claim. Ogasawara--Nakazato (2014) compute an algebraic boundary for a **different** nilpotent \(4\times4\) matrix, with additional upper-triangular ones above the superdiagonal, at one fixed value of \(q\); neither the matrix nor the parameter range matches the present theorem. The classic Tsing circular-union description and the ordinary Jordan-shift numerical-radius formula are known and are not claimed as new. The claimed contribution is the all-dimension \(n\ge4\) sharp radius transition, exact one-variable singular-norm profile, and its nonzero, explicit quadratic exit coefficient.

## Limitations
No claim is made for general nilpotent matrices, arbitrary weighted shifts, or nonreal \(q\). The coefficient is a local expansion at \(q_n\), not a closed elementary formula for \(r_n(q)\) throughout the strict-decay regime; there the exact profile is given by a one-variable minimization. A relevant 1998 paper of Li--Nakazato on general \(q\)-numerical ranges could not be inspected in full; an equivalent unindexed treatment of the special Jordan-shift profile remains possible. These limitations do not affect the analytic correctness of the stated theorem. No independent audit has been performed.

## References
1. M. Kaunisto, R. O'Loughlin, and J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, arXiv:2610.00443v1 (2026-09-30), https://arxiv.org/abs/2610.00443 .
2. M.-T. Chien and H. Nakazato, *The \(q\)-Numerical Range of 3 by 3 Tridiagonal Matrices*, Electronic Journal of Linear Algebra 20 (2010), 376--390, doi:10.13001/1081-3810.1382, https://journals.uwyo.edu/index.php/ela/article/download/765/765/765 .
3. Y. Ogasawara and H. Nakazato, *The \(q\)-Numerical Range of a Nilpotent 4 by 4 Matrix*, International Mathematical Forum 9 (2014), 1631--1637, doi:10.12988/imf.2014.49157, https://www.m-hikari.com/imf/imf-2014/33-36-2014/nakazatoIMF33-36-2014-1.pdf .
4. C.-K. Li and H. Nakazato, *Some Results on the \(q\)-Numerical Range*, Linear and Multilinear Algebra 43 (1998), 385--409, doi:10.1080/03081089808818539 (abstract consulted; full text unavailable).
5. P. Y. Wu, *A Numerical Range Characterization of Jordan Blocks*, Linear and Multilinear Algebra 43 (1998), 351--361, doi:10.1080/03081089808818536 (ordinary numerical-range reference).
