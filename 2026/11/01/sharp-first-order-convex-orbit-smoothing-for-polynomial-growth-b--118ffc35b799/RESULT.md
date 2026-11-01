# Sharp first-order convex-orbit smoothing for polynomial-growth bilateral shifts

## Finding
Let \(\theta\ge1\), \(\lambda>1\), and let \(B=B_{\theta,\lambda}\) act on the complex Hilbert space \(\ell^2(\mathbb Z)\) by \(Be_j=w_je_{j-1}\), where
\[
w_j=\begin{cases}
\lambda,&j\ge1,\\
1,&j=0,\\
((k+1)/k)^\theta,&j=-k,\quad k\ge1.
\end{cases}
\]
Put \(y=(I-B)e_0\). For every integer \(N\ge0\), consider the **degree-budgeted convex-orbit distance**
\[
\mathcal E_N(\theta)=\min\left\{\|P(B)y\|_2^2:
P(z)=\sum_{k=0}^Na_kz^k,\quad a_k\ge0,\quad\sum_{k=0}^Na_k=1\right\}.
\]
Write \(n=N+1\) and define
\[
R_0=1,\quad R_j=j^{-2\theta}\ (1\le j\le n),\qquad
S_h=\sum_{j=0}^n j^hR_j\ (h=0,1,2),
\quad D=S_0S_2-S_1^2,
\]
where \(S_0=\sum_{j=0}^nR_j\), avoiding any \(0^0\) convention. Then \(D>0\) and the exact optimum is
\[
\boxed{\mathcal E_N(\theta)=\frac{S_0}{D}.}
\]
The unique minimizing convex polynomial has the strictly positive coefficients
\[
\boxed{a_k^*=\frac1D\sum_{j=0}^kR_j(S_1-jS_0),\qquad 0\le k<n.}
\]
Neither formula depends on \(\lambda\). The sharp large-degree phase diagram is
\[
\mathcal E_N(\theta)\sim
\begin{cases}
(3-2\theta)n^{-(3-2\theta)},&1\le\theta<3/2,\\
1/\log n,&\theta=3/2,
\end{cases}
\]
while for \(\theta>3/2\) the squared distance tends to the strictly positive constant
\[
\boxed{\mathcal E_\infty(\theta)=\left[\zeta(2\theta-2)-
\frac{\zeta(2\theta-1)^2}{1+\zeta(2\theta)}\right]^{-1}>0.}
\]
Consequently, \(0\) belongs to the norm closure of \(\{P(B)y:P\text{ convex polynomial}\}\) **if and only if** \(1\le\theta\le3/2\). The borderline \(\theta=3/2\) admits logarithmic decay; beyond it even unrestricted polynomial degree cannot annihilate this first-order coboundary by convex averaging.

## Assumptions and scope
The weights are real and positive. The shift \(B\) is bounded and invertible because \(1\le w_j\le\max\{\lambda,2^\theta\}\). Convex polynomials have nonnegative **real** coefficients totaling one, and the comparison is in the Hilbert \(\ell^2\)-norm. The parameter \(\lambda>1\) is arbitrary but fixed. The integer \(N\) includes zero; \(n=N+1\ge1\). The first-public motivating work's primary classification is operator dynamics (MSC 47A16). The theorem concerns the fixed vector \(y=(I-B)e_0\), not the distance to zero for every vector or a classification of convex-cyclicity of the full operator.

## Proof
**1. Exact orbit reduction.** From the telescoping negative-side weights, \(B^0e_0=e_0\) and \(B^ke_0=k^\theta e_{-k}\) for every \(k\ge1\). Because \(P(B)\) commutes with \(I-B\), if \(a_{-1}=a_n=0\), orthogonality of the standard basis gives
\[
\|P(B)y\|_2^2=\sum_{j=0}^n\beta_j^2(a_j-a_{j-1})^2
=\sum_{j=0}^n\frac{b_j^2}{R_j},
\quad b_j=a_j-a_{j-1},\quad
\beta_0=1,\quad\beta_j=j^\theta\ (j\ge1).
\]
The endpoints imply \(\sum_{j=0}^nb_j=0\). The convex-mass constraint is equivalently
\[
\sum_{k=0}^{n-1}a_k=\sum_{j=0}^n(n-j)b_j=1.
\]
This identity follows by exchanging two finite sums; the term with \(j=n\) has coefficient zero.

**2. A sharp weighted Cauchy–Schwarz bound.** Set \(\mu=S_1/S_0\). Since \(\sum b_j=0\), the preceding normalization says
\[
1=\sum_{j=0}^n(\mu-j)b_j.
\]
By Cauchy–Schwarz,
\[
1\le\left(\sum_{j=0}^n\frac{b_j^2}{R_j}\right)
\left(\sum_{j=0}^nR_j(\mu-j)^2\right)
=\|P(B)y\|_2^2\left(S_2-\frac{S_1^2}{S_0}\right).
\]
Here the first inequality denotes the inequality for **squared** absolute values. The second factor is \(D/S_0>0\), as the supported indices \(0\) and \(n\) are distinct. Hence every admissible polynomial satisfies \(\|P(B)y\|_2^2\ge S_0/D\).

**3. Unique positive equality case.** Equality holds precisely when
\[
b_j=\frac{R_j(\mu-j)}{D/S_0}
=\frac{R_j(S_1-jS_0)}D.
\]
This vector satisfies \(\sum b_j=0\) by the definition of \(\mu\), and its weighted mass is one because \(\sum_jR_j(\mu-j)^2=D/S_0\). Its cumulative sums are the displayed \(a_k^*\). Since \(0<\mu<n\) and \(\mu-j\) changes sign only once, every proper partial sum of the signed, total-zero sequence \(R_j(\mu-j)\) is **strictly positive**: before the sign change positivity is immediate; afterward the partial sum is minus a strictly negative tail. Thus every \(a_k^*>0\), their sum is one, and the unconstrained sharp bound is attainable within the convex simplex. Strict equality in weighted Cauchy–Schwarz and fixed total mass prove uniqueness.

**4. Sharp parameter asymptotics.** Write \(K_n=D/S_0=S_2-S_1^2/S_0\), so \(\mathcal E_N=1/K_n\). When \(1\le\theta<3/2\), \(S_0\to1+\zeta(2\theta)\) and \(S_1=O(\log n)\) at \(\theta=1\) (bounded for \(\theta>1\)), hence \(S_1^2/S_0=o(S_2)\). Integral comparison gives \(S_2=\sum_{j=1}^n j^{2-2\theta}\sim n^{3-2\theta}/(3-2\theta)\), yielding the first asymptotic. At \(\theta=3/2\), \(S_2=\sum_{j=1}^n j^{-1}\sim\log n\), while \(S_0,S_1\) tend to finite limits, giving the second. For \(\theta>3/2\), all three sums converge, namely
\[
S_0\to1+\zeta(2\theta),\qquad S_1\to\zeta(2\theta-1),\qquad S_2\to\zeta(2\theta-2).
\]
Their limiting weighted variance is strictly positive because \(R_0,R_1>0\). Taking its reciprocal gives the stated positive barrier. Finally, the minima decrease with growing degree because the feasible convex polynomials are nested, so the limiting statements characterize the full convex-polynomial infimum.

## Verification
Execute `python checker.py` using Python 3 with no external dependencies. The standalone script checks exact rational minimizers for integer exponents, the mass and positivity constraints, weighted first-difference energies, Euler–Lagrange equations and comparisons with uniform Cesàro averaging; it also checks representative noninteger parameters and finite-degree asymptotic scales. Finite checks do not establish the asymptotic theorem: the proof above uses explicit Cauchy–Schwarz equality and power-sum convergence.

## Relationship to prior work
Wang and Zhou [1], Theorems 3.1 and 4.3, use ordinary Cesàro polynomials to obtain a sufficient convex-cyclicity condition involving \(n^{-1}\prod_{j=0}^nw_{-j}\). In this family the factor is asymptotic to \(n^{\theta-1}\), so their **particular sufficient condition** does not apply for \(\theta\ge1\). The present result optimizes **all** degree-limited convex combinations for the first-order coboundary and detects the new critical exponent \(3/2\); it does not claim a new global convex-cyclicity classification. Bensaid, León-Saavedra and Romero de la Rosa [2] relate higher-order Cesàro-hypercyclicity to scaled powers. Their general orbit-density results do not calculate this one-vector optimal norm, the unique optimizing positive polynomial, or its obstruction beyond \(3/2\). The published one-generator Dirichlet approximation result [3] imposes a **value-interpolation** condition \(R(1)=1\), whereas the polynomial \((1-z)P(z)\) here obeys \(R(1)=0\) and \(R'(1)=-1\); neither objective implies the other. The published smoothest-average result [4] minimizes a Fourier **operator norm** for fixed three-point symmetric kernels, rather than the \(\ell^2\) norm of a variable-support convex-orbit vector under polynomially increasing weights.

## Limitations
The phase transition is specific to the first-order coboundary \((I-B)e_0\), polynomial negative-side growth and Hilbert norm. It does not assert the full operator is non-convex-cyclic when \(\theta>3/2\); higher-order coboundaries may behave differently. Parameterwise asymptotics are for fixed \(\theta\), not uniform near \(3/2\). The minimization is exactly solved, but novelty remains subject to the possibility of an equivalent older weighted-Dirichlet derivative-interpolation calculation under other terminology. Independent mathematical audit and publication-priority confirmation have not been performed.

## References
[1] Cui Wang and Ze-Hua Zhou, *Convex-cyclic and super convex-cyclic weighted shifts*, arXiv:2610.26978v1, first publicly submitted October 19, 2026, especially Theorems 1.2, 3.1 and 4.3. https://arxiv.org/html/2610.26978v1

[2] I. F. Z. Bensaid, F. León-Saavedra and M. del Pilar Romero de la Rosa, *Cesàro Means and Convex-Cyclic Operators*, Complex Analysis and Operator Theory 14 (2020), DOI:10.1007/s11785-019-00959-2, especially Theorem 2.3.

[3] *Exact one-generator approximation threshold in radial Dirichlet polydisk spaces*, publicly accessible mathematical result, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-one-generator-approximation-threshold-in-radial-dirichlet--a92045109063

[4] *All-order sharp three-point smoothest averages*, publicly accessible mathematical result, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-order-sharp-three-point-smoothest-averages--97ecaa4cd5e9
