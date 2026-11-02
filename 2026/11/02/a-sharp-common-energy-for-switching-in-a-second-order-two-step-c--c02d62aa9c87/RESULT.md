# A sharp common energy for switching in a second-order two-step Chebyshev integrator

## Finding
Consider the explicit two-stage, two-step scheme below. For frozen scalar decay rates whose normalized step parameters \(x_n=h\lambda_n\) may vary arbitrarily from one step to the next in \([0,4]\), the corresponding companion errors \(z_n=(y_n,y_{n-1})^{\mathsf T}\) satisfy the **same sharp energy law**, independently of switching order:

\[
 z_{n+1}^{\mathsf T}Pz_{n+1}
 \leq \left(1-\frac{x_n(4-x_n)}5\right)
 z_n^{\mathsf T}Pz_n,
 \qquad
 P=\begin{pmatrix}1&-1/3\\-1/3&1/5\end{pmatrix}\succ0.
\]

Thus the energy tends to zero whenever \(\sum_{n\geq0}x_n(4-x_n)=\infty\), without assumptions of periodicity, independence, or bounded switching frequency. The coefficient \(1/5\) is the largest possible universal coefficient among **all** positive-definite quadratic energies of this form; at that coefficient the matrix \(P\) is unique up to positive rescaling. The same matrix is nonexpansive on the entire frozen Schur-stability interval of an associated affine companion family, a strictly stronger statement than individual frozen-rate stability.

## Assumptions and scope
The uniform step is \(h>0\), and for a smooth scalar autonomous or nonautonomous right-hand side the two-stage formula is

\[
\begin{aligned}
 v_0&=\tfrac32 y_n-\tfrac12y_{n-1},\\
 v_1&=v_0+\tfrac h2 f(t_n+h/2,v_0),\\
 v_2&=2v_1-v_0+h f(t_n+h,v_1),\\
 y_{n+1}&=\tfrac35 y_n+\tfrac25 v_2.
\end{aligned}
\]

This is a second-order member of the two-step stabilized Runge–Kutta stability-polynomial template of Moisa and Faleichik: take two stages and the template parameters \(\alpha=3/5\), \(\eta^2=1/5\), \(\omega=1\), and \(\beta=2\). For the stability assertion, each step uses a **single frozen scalar** \(f=-\lambda_n y\) at both stage evaluations, where \(\lambda_n\geq0\) can depend arbitrarily on \(n\). This is not a claim of second-order convergence when the rate jumps discontinuously between time steps, nor of energy contraction for noncommuting matrix operators or nonlinear equations.

Write \(x_n=h\lambda_n\) and

\[
 t_n=T_2(1-x_n/2)=1-2x_n+x_n^2/2,
 \qquad T_2(u)=2u^2-1.
\]

For \(x_n\in[0,4]\), necessarily \(t_n\in[-1,1]\). The exact companion matrix is

\[
 z_{n+1}=A(t_n)z_n,\qquad
 A(t)=\begin{pmatrix}\frac35(1+t)&-t/5\\1&0\end{pmatrix}.
\]

All claims concern these exact real-arithmetic recurrences and arbitrary real initial states \(z_0\). The word *energy* refers to the explicit quadratic form above, not physical energy or a stochastic expectation.

## Proof
**Second order and realization.** Put \(F=f(t_n,y(t_n))\) and \(\dot F= f_t+f_yF\). On exact starting values,
\(y(t_n-h)=y(t_n)-hF+\frac12h^2\dot F+O(h^3)\). Taylor expansion gives
\(v_0=y(t_n)+\frac12hF-\frac14h^2\dot F+O(h^3)\),
\(v_1=y(t_n)+hF+O(h^3)\), and
\(v_2=y(t_n)+\frac52hF+\frac54h^2\dot F+O(h^3)\).
Consequently \(y_{n+1}=y(t_n)+hF+\frac12h^2\dot F+O(h^3)\). For a frozen rate, the two inner stages give \(v_2=T_2(1-x/2)v_0\), so the stated companion matrix follows exactly.

**Positive-definite common energy and the sharp budget.** The matrix \(P\) has first principal minor \(1\) and determinant \(4/45>0\). Direct multiplication at the two Chebyshev extrema gives

\[
 A(-1)^{\mathsf T}PA(-1)=\tfrac15P,
\qquad
 P-A(1)^{\mathsf T}PA(1)=\tfrac4{25}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0.
\]

For any \(t\in[-1,1]\), \(A(t)=wA(-1)+(1-w)A(1)\), where \(w=(1-t)/2\). The squared norm induced by \(P\) is convex in its vector argument. For every \(z\),

\[
\begin{aligned}
 \|A(t)z\|_P^2
 &\leq w\|A(-1)z\|_P^2+(1-w)\|A(1)z\|_P^2\\
 &\leq \left(\frac w5+1-w\right)\|z\|_P^2
 =\left(\frac35+\frac{2t}5\right)\|z\|_P^2.
\end{aligned}
\]

Since \(1-t=x(4-x)/2\), this is the claimed bound. Iteration gives the product inequality. Since \(1-u\leq e^{-u}\) for \(u\in[0,1]\), divergence of the sum gives convergence to zero.

**Sharpness and uniqueness of the quadratic certificate.** Suppose a positive-definite \(Q\) and a coefficient \(c\) satisfy \(A(t)^{\mathsf T}QA(t)\preceq[1-c(1-t)]Q\) for every \(t\in[-1,1]\). The matrix \(A(-1)\) has characteristic equation \(\zeta^2-1/5=0\). Consequently its spectral radius squared is \(1/5\), and at \(t=-1\) the bound requires \(1-2c\geq1/5\), hence \(c\leq2/5\). In terms of \(x(4-x)\), this is precisely the coefficient bound \(1/5\).

At equality \(c=2/5\), the determinant identity and Loewner inequality force \(A(-1)^{\mathsf T}QA(-1)=Q/5\). Writing \(Q=\begin{pmatrix}p&q\\q&r\end{pmatrix}\), this implies \(r=p/5\). At \(t=1\), \(A(1)(1,1)^{\mathsf T}=(1,1)^{\mathsf T}\). Positivity of \(Q-A(1)^{\mathsf T}QA(1)\) makes its product with \((1,1)^{\mathsf T}\) vanish. A left eigenvector of \(A(1)\) for eigenvalue one is \((1,-1/5)^{\mathsf T}\); therefore \(Q(1,1)^{\mathsf T}\) is proportional to that direction. Together with \(r=p/5\), this forces \(q=-p/3\). Thus \(Q=pP\) with \(p>0\). Both extrema also provide equality witnesses.

**Entire scalar Schur interval.** The characteristic polynomial of \(A(t)\) is \(\zeta^2-\frac35(1+t)\zeta+t/5\). The three quadratic Schur inequalities reduce to \(t<5\), \(t<1\), and \(t>-2\), so the strict frozen stability interval is exactly \((-2,1)\). With \(D(t)=P-A(t)^{\mathsf T}PA(t)\), exact algebra gives

\[
 D_{22}(t)=\frac{5-t^2}{25},\qquad
 \det D(t)=\frac{32}{1125}(1-t)(t+2).
\]

For \(-2\leq t\leq1\), the first quantity is positive and the second nonnegative; hence \(D(t)\succeq0\), and it is positive definite for \(-2<t<1\). It follows that even arbitrary switching between **any** parameters in a compact subinterval of the frozen Schur region contracts the same energy uniformly. No larger interval of strict frozen stability exists. Notice that \(t<-1\) is not reached by the real scalar Chebyshev argument \(1-x/2\); this full-interval assertion is an algebraic property of the companion family, not an additional physical rate range.

## Verification
The standalone standard-library script `verify.py` performs 2,932 exact-rational checks: the stage-to-companion reduction, both endpoint identities, degree-at-most-four polynomial identities for \(\det D(t)\), sample Loewner inequalities, and 2,401 four-step arbitrary-switching energy tests. The exact polynomial identities are determined by seven distinct rational points, more than the five required for polynomials of degree at most four. The script does not substitute finite testing for the all-parameter proof above. Run with `python verify.py`.

## Relationship to prior work
Moisa and Faleichik (arXiv:2303.16267, version 1 posted 2023-03-28) introduce two-step stabilized Runge–Kutta characteristic polynomials and stage realizations, and analyze frozen scalar stability and damping. The recurrence template and second-order construction are prior work. The result here is the **single explicit, sharp, unique quadratic switching certificate** for an exactly specified rational second-order instance, plus its validity on the complete affine-family frozen Schur interval; these statements do not follow from scalar root locations alone. Variable-step BDF stability results of Li and Liao (arXiv:2201.00527) and the earlier Dahlquist–Liniger–Nevanlinna framework concern different implicit multistep/one-leg formulas and do not furnish this certificate or its sharp coefficient. General common-Lyapunov and matrix-convexity techniques are established; novelty is not claimed for the tools themselves.

## Limitations
Only the stated rational two-stage method, exact frozen scalar stage rates, and scalar companion dynamics are covered. The switching result does **not** establish full second-order accuracy across coefficient jumps, variable-step-size accuracy, unconditional stability, monotonicity of individual numerical solution values, or extension to nonnormal/noncommuting spatial discretizations. A stronger published characterization of this specific recurrence could supersede publication priority; no independent audit has been performed.

## References
1. A. Moisa and B. Faleichik, *Second order stabilized two-step Runge-Kutta methods*, arXiv:2303.16267v1 (2023-03-28), https://arxiv.org/html/2303.16267v1 .
2. Z. Li and H.-l. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527v1 (2022-01-03), https://arxiv.org/html/2201.00527v1 .
3. G. Dahlquist, W. Liniger, and O. Nevanlinna, *Stability of Two-Step Methods for Variable Integration Steps*, SIAM J. Numer. Anal. (1983), DOI:10.1137/0720076, https://doi.org/10.1137/0720076 .
