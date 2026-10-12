# A sharp large-ratio damping reversal for alternating variable-step BDF3

## Finding
Let the standard, physical-time-interpolatory, three-step backward differentiation formula (BDF3) be used on the scalar equation \(y'=-\lambda y\), where \(\lambda>0\), with exactly alternating positive timesteps \(H,h,H,h,\ldots\). Set \(r=H/h>0\) and \(q=\lambda h>0\). Let \(P_r(q)\) be the two-step transfer matrix on three stored solution values, and let \(\rho\) denote its spectral radius.

**Theorem.** For each fixed \(q>0\),
\[
\lim_{r\to\infty}\rho(P_r(q))=\frac{2}{1+q}.
\]
Consequently, for every fixed \(0<q<1\) there is \(R_q<\infty\) such that \(r>R_q\) gives \(\rho(P_r(q))>1\), even though the exact differential equation is strictly dissipative. For every fixed \(q>1\), sufficiently large ratios instead satisfy \(\rho(P_r(q))<1\). The asymptotic dividing value is exactly \(q=1\); no finite-ratio classification is asserted at equality.

An exact finite instability witness is \(r=100\), \(q=1/10\), for which
\[
\det(I+P_{100}(1/10))=-\frac{4621393451}{14621500436}<0.
\]
Thus \(P_{100}(1/10)\) has a real Floquet multiplier strictly below \(-1\). The result concerns asymptotic stability of the repeated period, not accuracy, arbitrary nonperiodic steps, or stability of a single step.

## Assumptions and scope
The BDF3 derivative is obtained by differentiating the unique cubic interpolant at the newest time, using the current value and three immediately preceding stored values. At each step the equation \(y'=-\lambda y\) is imposed implicitly at the newest time. No startup procedure or special initialization restricts the initial triple; stability here means decay of every possible stored-value state under repeated alternating periods.

Normalize \(h=1\), so that the long step has length \(r\). For any \(r>0\), define
\[
E_1=5r^2+5r+1,\quad E_2=r^2+5r+5,\quad
d_1=\frac1r+\frac1{r+1}+\frac1{2r+1},\quad
d_2=1+\frac1{r+1}+\frac1{r+2}.
\]
All denominators are strictly positive.

## Proof
Interpolation differentiation on the time nodes \(0,-r,-r-1,-2r-1\), followed by the zero-test-equation relation, gives the long-step companion matrix
\[
A_0(r)=\begin{pmatrix}
\frac{(r+1)(2r+1)^2}{E_1}&-\frac{r(2r+1)^2}{E_1}&\frac{r(r+1)}{E_1}\\
1&0&0\\0&1&0
\end{pmatrix}.
\]
For the following short step, use nodes \(0,-1,-1-r,-2-r\) to obtain
\[
B_0(r)=\begin{pmatrix}
\frac{(r+1)(r+2)^2}{rE_2}&-\frac{(r+2)^2}{rE_2}&\frac{r+1}{E_2}\\
1&0&0\\0&1&0
\end{pmatrix}.
\]
The coefficient of the newest value in the interpolatory derivative is \(d_1\) or \(d_2\), respectively. Replacing the zero equation by \(y'=-\lambda y\) therefore multiplies just the first row of \(A_0\) by \(d_1/(d_1+q)\), and just the first row of \(B_0\) by \(d_2/(d_2+q)\). Write these damped matrices as \(A_r(q)\) and \(B_r(q)\), respectively. Thus the exact Floquet matrix is \(P_r(q)=B_r(q)A_r(q)\).

For every fixed \(q>0\), direct division by highest powers of \(r\) yields the entrywise limits
\[
A_r(q)\longrightarrow
\begin{pmatrix}2/q&-2/q&0\\1&0&0\\0&1&0\end{pmatrix},
\qquad
B_r(q)\longrightarrow
\begin{pmatrix}1/(1+q)&0&0\\1&0&0\\0&1&0\end{pmatrix}.
\]
Multiplying the limits gives
\[
P_\infty(q)=\begin{pmatrix}
\frac{2}{q(1+q)}&-\frac{2}{q(1+q)}&0\\
\frac2q&-\frac2q&0\\
1&0&0
\end{pmatrix}.
\]
Its characteristic polynomial is exactly
\[
\det(zI-P_\infty(q))=z^2\left(z+\frac{2}{1+q}\right).
\]
Spectral radius is continuous in the entries of a finite matrix (equivalently, polynomial roots are continuous as an unordered multiset). It follows that \(\rho(P_r(q))\to 2/(1+q)\), proving both strict inequalities away from \(q=1\) for all sufficiently large \(r\).

For the finite certificate substitute \(r=100\), \(q=1/10\) in the exact rational matrices and compute the displayed negative determinant. Any real three-by-three matrix having all eigenvalues of modulus at most one has \(\det(I+P)\ge0\): each nonreal conjugate pair contributes \(|1+z|^2>0\), while each real eigenvalue contributes a nonnegative factor. In fact the strict negative determinant forces at least one real eigenvalue below \(-1\). This supplies a finite, parameter-specific counterexample independently of the limiting argument.

## Verification
Run `python3 verify.py` in the same directory as this document; it uses only Python's standard library and exact rational arithmetic. The checker reconstructs the two interpolatory transfers, verifies nine zero-equation trace/determinant identities, evaluates 45 rational damped monodromies, and independently recomputes the exact determinant certificate. The analytical matrix limits and root-continuity argument, rather than finitely many tests, establish the universal statement.

## Relationship to prior work
Classical fixed-step BDF3 has negative-real-axis absolute stability; that statement does not imply the same property for periodically changing coefficients. Guglielmi and Zennaro (2001) investigate variable-step BDF3 zero-stability using a joint-spectral-radius approach. Hadjimichael, Ketcheson, Lóczi and Németh (2015) analyze variable-step, **explicit** strong-stability-preserving multistep methods. Li and Liao (2022) prove variable-step BDF stability under quantified adjacent-ratio hypotheses. Those published statements do not, on the inspected material, yield the displayed dissipative test-equation Floquet limit or the exact negative-axis instability certificate. The specialized 2001 paper's complete text was unavailable for decisive inspection; historical originality remains subject to that specific risk.

## Limitations
The conclusion is for the standard third-order interpolatory BDF, scalar real negative eigenvalue, exactly two-periodic positive timesteps, and unrestricted stored-value initial states. It is not a result about local error, convergence along a simultaneously refined mesh, all complex eigenvalues, arbitrary nonperiodic steps, or the boundary \(q=1\) at finite \(r\). The large-ratio instability does not contradict strong zero-stability at each fixed ratio, since \(r\to\infty\) and \(q\downarrow0\) need not commute. The new claim is the positive-damping Floquet law, not the previously established zero-equation root condition.

## References
1. N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445–458, DOI: `10.1007/s211-001-8010-0`.
2. Y. Hadjimichael, D. Ketcheson, L. Lóczi, and A. Németh, *Strong stability preserving explicit linear multistep methods with variable step size*, arXiv:1504.04107v1 (first public 2015-04-16).
3. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527 (2022), DOI: `10.1137/21M1462398`.
4. M. Calvo, T. Grande, and R. D. Grigorieff, *On the zero stability of the variable order variable stepsize BDF-formulas*, Numerische Mathematik (1990), DOI: `10.1007/BF01386395`.
