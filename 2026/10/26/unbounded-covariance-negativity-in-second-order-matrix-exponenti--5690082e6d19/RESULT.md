# Unbounded covariance negativity in second-order matrix exponential time differencing

## Finding

For the published METD1, METD2, and METD2RK formulas of Shkeir and Grafke, consider the differential Lyapunov equation
\[
\dot Q=AQ+QA+\Sigma,\qquad Q(0)=0,\qquad
A=-\operatorname{diag}(a,b),\quad \Sigma=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
with any \(a,b>0\) and step length \(h=1\). The exact covariance \(Q(1)\) is positive definite whenever \(a\ne b\). Nevertheless:

1. The symmetric part of the METD1 one-step matrix has **negative determinant for every \(a\ne b\)**.
2. Fix any \(b>0\). The METD2 and METD2RK one-step matrices coincide for this constant forcing. Writing \(S_2(a,b)\) for their symmetric part and
\[
g(b)=\frac{1-(1+b)e^{-b}}{b^2}>0,
\]
we have the exact asymptotic eigenvalue law
\[
\boxed{\lim_{a\to\infty}\frac{\lambda_{\min}(S_2(a,b))}{a}=-\frac{g(b)}2.}
\]
Thus their symmetrized outputs have an unboundedly negative eigenvalue in the stiff limit, while the true covariance stays positive semidefinite and bounded. These conclusions concern the published full-matrix formulas and not alternative integrating-factor quadratures.

This is an exact structural non-preservation result; it is *not* a contradiction to convergence at fixed \(A\) as the step length tends to zero.

## Assumptions and scope

The coefficient matrix \(A\) is real symmetric and strictly negative definite; its two eigenvalues are distinct for the positivity comparison. Both left and right matrices in the source's matrix equation \(\dot Q=LQ+QR+N\) equal \(A\), hence commute. The forcing \(\Sigma\) is constant, positive semidefinite, and rank one. The step size is exactly \(h=1\), and \(Q(0)=0\). For METD2, the preceding forcing evaluation is the same constant matrix, so its backward difference is zero. For METD2RK, both stage forcing evaluations are identical. The phrase *symmetric part* denotes \(\operatorname{sym}(K)=(K+K^{\mathsf T})/2\); a non-symmetric output is not itself a covariance matrix.

Define, for \(x>0\),
\[
f(x)=\frac{1-e^{-2x}}{2x}=\int_0^1e^{-2xt}\,dt,
\qquad
 g(x)=\frac{1-(1+x)e^{-x}}{x^2}=\int_0^1te^{-xt}\,dt.
\]
Both are positive; \(f\) is strictly decreasing. The primary MSC2020 classification is 65L04 (numerical methods for initial value problems).

## Proof

**Exact solution.** Variation of constants gives
\[
Q(1)=\int_0^1e^{tA}\Sigma e^{tA}\,dt
=\left(\frac{1-e^{-(d_i+d_j)}}{d_i+d_j}\right)_{i,j=1}^2,
\quad (d_1,d_2)=(a,b).
\]
This is the Gram matrix in \(L^2[0,1]\) of the real functions \(e^{-at}\) and \(e^{-bt}\). If \(a\ne b\), these functions are linearly independent, so \(Q(1)\succ0\). Moreover, since the matrix is positive semidefinite,
\[
\|Q(1)\|_2\le\operatorname{tr}Q(1) = f(a)+f(b)
\le \frac1{2a}+\frac1{2b}.
\]
Thus the true covariance is bounded as \(a\to\infty\) for fixed \(b>0\).

**Reduction of the published schemes.** Their \(\varphi\)-functions satisfy
\[
\varphi_1(z)=\int_0^1e^{(1-s)z}\,ds,\qquad
\varphi_2(z)=\int_0^1s e^{(1-s)z}\,ds.
\]
Equation (7) of Shkeir--Grafke gives, on this initial step,
\[
K_1=\varphi_1(2A)\Sigma.
\]
Their equation (9), with zero backward forcing difference, gives
\[
K_2=\varphi_1(2A)\Sigma+
 \bigl(\varphi_1(A)-\varphi_2(A)\bigr)[\Sigma,A].
\]
Equation (their METD2RK formula) has the same right-hand side because the forcing is constant. The commutator uses the source convention \([\Sigma,A]=\Sigma A-A\Sigma\). Therefore, with \(d_1=a,d_2=b\), the entries are exactly
\[
(K_1)_{ij}=f(d_i),\qquad
(K_2)_{ij}=f(d_i)+(d_i-d_j)g(d_i).
\]
No approximation or commutation of \(\Sigma\) with \(A\) has been made.

**First-order obstruction.** Let \(S_1=\operatorname{sym}(K_1)\). Directly,
\[
S_1=\begin{pmatrix}
f(a)&\frac{f(a)+f(b)}2\\
\frac{f(a)+f(b)}2&f(b)
\end{pmatrix},\qquad
\det S_1=-\frac{(f(a)-f(b))^2}{4}.
\]
Since \(f'(x)=-2\int_0^1te^{-2xt}\,dt<0\), unequal rates give \(\det S_1<0\). The symmetric part has one strictly negative eigenvalue at every unequal pair.

**Second-order asymptotic.** The diagonal entries of \(S_2=\operatorname{sym}(K_2)\) are \(f(a),f(b)\), and the off-diagonal entry is
\[
s(a,b)=\frac{f(a)+f(b)+(a-b)(g(a)-g(b))}{2}.
\]
At fixed \(b>0\), the elementary exponential formulas yield
\[
f(a)=\frac1{2a}+O(e^{-2a}/a),\qquad
 g(a)=\frac1{a^2}+O(e^{-a}/a).
\]
Consequently, \(s(a,b)/a\to -g(b)/2\), while \(f(a)/a\to0\) and \(f(b)/a\to0\). Entrywise,
\[
\frac{S_2(a,b)}a\longrightarrow
\begin{pmatrix}0&-g(b)/2\\-g(b)/2&0\end{pmatrix}.
\]
The eigenvalues of a real symmetric matrix depend continuously on its entries, proving the boxed limit. Since \(g(b)=\int_0^1te^{-bt}\,dt>0\), the negative eigenvalue diverges linearly while the positive one diverges linearly in the opposite direction. The exact bounded covariance cannot share this behavior.

**Finite exact-inequality witness.** Take \((a,b)=(10,1)\). The elementary bounds \(8/3<e<11/4\) and \(e^{10}>1000\) imply
\[
f(10)<\frac1{20},\quad f(1)<\frac7{16},\quad
g(10)<\frac1{100},\quad g(1)>\frac14.
\]
Thus
\[
s(10,1)<\frac12\left(\frac1{20}+\frac7{16}+9\left(\frac1{100}-\frac14\right)\right)
=-\frac{669}{800},
\]
so
\[
\det S_2(10,1)<\frac7{320}-\left(\frac{669}{800}\right)^2<0.
\]
The easy exponential bounds can be justified using the positive Taylor series for \(e\) and its geometric tail estimate. This supplies a finite certificate independently of asymptotics or floating-point output.

## Verification

The accompanying standalone `verify.py` computes the matrices directly from the published \(\varphi\)-function specialization, checks the analytical determinant formulas, checks the finite rational certificate, compares the exact Gram solution with numerical quadrature, and confirms the asymptotic slopes on increasing stiffness scales. It is supplementary numerical evidence, not a substitute for the preceding universal proof. Run `python3 verify.py` with the Python standard library. All mathematical formulas used by the verifier are fully stated above.

## Relationship to prior work

Shkeir and Grafke, *Exponential time differencing for matrix-valued dynamical systems*, arXiv:2406.13761, provide METD1 (equation (7)), METD2 (equation (9)), and METD2RK (Section 2.4) and test them on differential Lyapunov systems (Section 6.1). Their results establish convergence orders, not the rank-one covariance-positivity statements above. The phenomenon occurs inside their commuting-coefficient setting and does not contradict the established fixed-operator convergence orders.

Ostermann, Piazzola, and Walach, arXiv:1803.10473, analyze a different low-rank Lie--Trotter/projector splitting method for stiff matrix differential equations; their step is not the left-sided \(\varphi_1(L+R)\) plus commutator correction studied here. Li, arXiv:1907.12971, applies the exact Sylvester superoperator formula \(h\varphi_1(h\mathcal S)(\Sigma)\) with \(\mathcal S(X)=AX+XA\) for constant forcing (Section 2, Lemma 1). That two-sided covariance integral is not the METD commutator-truncated update; its exact structure preservation does not imply the present METD2 negative-eigenvalue slope. Zhang, Lan, and Jing, arXiv:2606.15703, construct symmetry- and positivity-preserving integrating-factor SSP Runge--Kutta methods for differential Lyapunov equations. Their two-sided congruence-based stages avoid the left-weighted forcing of these METD formulas; they do not state the displayed unbounded negative-eigenvalue law for METD2. These related works contextualize the importance of positivity but do not imply the particular claim by an identified theorem.

## Limitations

The result studies exact-arithmetic one-step formulas, constant rank-one forcing, two real modes, step length one, and the symmetric part of outputs that need not themselves be symmetric. It does not claim divergence of METD2 at fixed \(A\) under mesh refinement, does not classify finite stiffness thresholds for all rate pairs, and does not apply to all matrix-valued exponential integrators. In particular, exact two-sided variation-of-constants quadrature and the cited positivity-preserving integrating-factor methods are different algorithms. An independently established equivalent analysis in other literature remains possible; no independent audit is claimed.

## References

1. N. Shkeir and T. Grafke, *Exponential time differencing for matrix-valued dynamical systems*, arXiv:2406.13761 (first posted 2024-06-19; inspected 2026 revision, Sections 2 and 6), https://arxiv.org/abs/2406.13761 .
2. A. Ostermann, C. Piazzola, and H. Walach, *Convergence of a low-rank Lie--Trotter splitting for stiff matrix differential equations*, arXiv:1803.10473, https://arxiv.org/abs/1803.10473 .
3. D. Li, *Exponential integrators for large-scale stiff matrix Riccati differential equations*, arXiv:1907.12971, https://arxiv.org/abs/1907.12971 .
4. W. Zhang, R. Lan, and X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703, https://arxiv.org/abs/2606.15703 .
