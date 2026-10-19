# Exact rank delays and Loewner-error phase transitions in IF-SSPRK Gramians

## Finding

Let \(d\ge1\), \(N\ge1\) be integers, \(h>0\), \(T=Nh\), and consider the differential Lyapunov equation
\[
\dot X=AX+XA^{\mathsf T}+bb^{\mathsf T},\qquad X(0)=0,
\]
with constant real \(A\in\mathbb R^{d\times d}\) and \(b\in\mathbb R^d\). Apply the published integrating-factor SSP Runge--Kutta methods, IF-SSPRK2 or IF-SSPRK3, in exact arithmetic with the same positive step \(h\). Write \(X_N^{(2)}\) and \(X_N^{(3)}\) for their full-step outputs.

**Universal rank ceiling.** For every \(A,b\),
\[
\operatorname{rank}X_N^{(2)}\le \min\{d,N+1\},\qquad
\operatorname{rank}X_N^{(3)}\le \min\{d,2N+1\}.
\]
These bounds are attained simultaneously, for every \(N,h\), by the canonical controllable integrator chain \(A=J_d\) (ones on the superdiagonal), \(b=e_d\). The exact covariance \(X(T)\) for this chain is positive definite for every \(T>0\). Therefore IF-SSPRK2 cannot recover full rank before \(N=\max\{1,d-1\}\) steps, and IF-SSPRK3 cannot do so before \(N=\max\{1,\lceil(d-1)/2\rceil\}\) steps; the thresholds are attained. In particular, unconditional positive *semidefiniteness* does not imply positive *definiteness* of the computed Gramian at a fixed finite horizon.

**Sharp Loewner-error classification on the same chain.** Define the signed covariance error \(E_N^{(q)}=X_N^{(q)}-X(T)\), with \(q=2,3\). For every \(N\ge1\), \(h>0\), its inertia has these exact regimes:

| Method | Dimensions | Signed error |
|---|---|---|
| IF-SSPRK2 | \(d=1\) | zero |
| IF-SSPRK2 | \(d=2\) | nonzero positive semidefinite, rank one |
| IF-SSPRK2 | \(d\ge3\) | indefinite |
| IF-SSPRK3 | \(d=1,2\) | zero |
| IF-SSPRK3 | \(d=3\) | nonzero positive semidefinite, rank one |
| IF-SSPRK3 | \(d\ge4\) | indefinite |

Here *indefinite* means there are two nonzero directions with strict and opposite variance errors. These dimension thresholds are exact and **cannot be improved by reducing the positive step size or increasing the number of steps** (so long as the dimension and finite positive step remain fixed). The signed-error statement applies to the displayed undamped integrator chain; no such sign claim is made for arbitrary \(A\).

## Assumptions and scope

All matrices and vectors are real; the forcing is the fixed rank-one matrix \(bb^{\mathsf T}\), and the initial covariance is zero. Both methods use the integrating-factor equations and classical SSPRK stages defined in Zhang--Lan--Jing, arXiv:2606.15703v1, equations (3)--(6). No floating-point truncation of the matrix exponential is included. For the sharpness and inertia assertions, \(J_d\) is the \(d\)-by-\(d\) nilpotent shift, and \(e_d\) the last canonical basis vector. No Hurwitz assumption is required for a finite-time covariance.

## Proof

**Step 1: positive quadrature form for every constant system.** Set \(W(t)=e^{-tA}X(t)e^{-tA^{\mathsf T}}\). It satisfies \(W'(t)=e^{-tA}bb^{\mathsf T}e^{-tA^{\mathsf T}}\), independent of \(W\). Substitution into the published SSPRK2 stages gives a trapezoidal rule; the SSPRK3 stages give Simpson's rule. Conjugating at \(T\) and reversing the symmetric node order gives the exact formulas
\[
X_N^{(2)}=h\sum_{j=0}^N a_j^{(2)}v(jh)v(jh)^{\mathsf T},
\quad a_j^{(2)}=\begin{cases}\tfrac12,&j=0,N,\\1,&0<j<N,\end{cases}
\]
\[
X_N^{(3)}=h\sum_{j=0}^{2N}a_j^{(3)}v(jh/2)v(jh/2)^{\mathsf T},\quad
 a_j^{(3)}=\begin{cases}
 \tfrac16,&j=0,2N,\\
 \tfrac23,&j\text{ odd},\\
 \tfrac13,&0<j<2N\text{ even}.
 \end{cases}
\]
where \(v(t)=e^{tA}b\). All weights are strictly positive, hence each numerical Gramian is positive semidefinite and has rank exactly the dimension of the span of its sampled vectors. This gives both universal rank ceilings.

**Step 2: sharp rank and exact positive definiteness.** With \(A=J_d\) and \(b=e_d\),
\[
v(t)=\left(\frac{t^{d-1}}{(d-1)!},\frac{t^{d-2}}{(d-2)!},\ldots,t,1\right)^{\mathsf T}.
\]
Any \(\min\{d,k\}\) columns from \(k\) such vectors at distinct nodes have full possible rank by the Vandermonde determinant, proving equality in each numerical rank ceiling. On the other hand
\[
z^{\mathsf T}X(T)z=\int_0^T (z^{\mathsf T}v(t))^2\,dt>0\quad(z\ne0),
\]
since a nonzero polynomial cannot vanish throughout an interval. Thus the exact Gramian is positive definite at every positive time.

The quadrature also gives a closed determinant certificate. Put \(s=1\) for IF-SSPRK2 and \(s=2\) for IF-SSPRK3, and use corresponding weights \(a_j\) above with \(j=0,\ldots,sN\). Then
\[
\det X_N^{(s+1)}=
\frac{h^{d^2}}{s^{d(d-1)}\prod_{r=0}^{d-1}(r!)^2}
\sum_{0\le j_1<\cdots<j_d\le sN}
\left(\prod_{\ell=1}^d a_{j_\ell}\right)
\left(\prod_{u<v}(j_v-j_u)^2\right),
\]
with an empty sum interpreted as zero. This is Cauchy--Binet applied to the positive weighted Vandermonde Gram matrix. At the first possible nonsingular step, the IF-SSPRK2 determinant is exactly \(h^{d^2}/4\) for \(d\ge2\); for IF-SSPRK3 with \(d=2N+1\ge3\) it is exactly
\[
h^{d^2}2^{N-2-d(d-1)}3^{-(2N+1)}.
\]
These first-threshold expressions follow by evaluating the single maximal Vandermonde minor.

**Step 3: signed quadrature moment errors.** Work in the polynomial basis ordered by powers \(t^r/r!\), \(0\le r<d\); reversing the actual coordinate order is an orthogonal permutation, so it does not change definiteness or inertia. Each error entry is the error of the scalar quadrature on \(t^{r+s}/(r!s!)\) over \([0,T]\). Composite trapezoidal integration is exact for powers zero and one, while
\[
\operatorname{Trap}_h(t^2)-\int_0^T t^2\,dt=Nh^3/6.
\]
Consequently, for \(d=1\) the error vanishes. For \(d=2\), only the power-one diagonal is nonzero, equal to \(Nh^3/6>0\). For \(d\ge3\), the error principal submatrix indexed by powers zero and two has \((0,0)\) entry zero and off-diagonal entry \(Nh^3/12>0\), hence negative determinant; the full symmetric error is indefinite.

Composite Simpson integration is exact for polynomials through degree three, and
\[
\operatorname{Simpson}_h(t^4)-\int_0^T t^4\,dt=Nh^5/120.
\]
It follows that for \(d\le2\) the error vanishes; for \(d=3\) only the squared power-two basis vector contributes, with positive error \(Nh^5/480\). If \(d\ge4\), use the powers one and three: the power-one diagonal error is zero, while their off-diagonal error is \(Nh^5/720>0\), giving a negative two-by-two principal determinant. This proves every regime, including strictness and independence from any small-step asymptotic.

## Verification

The standalone `verification.py` implements the published integrating-factor stage equations over rational inputs, and separately constructs the trapezoidal and Simpson covariance matrices with positive quadrature weights. On dimensions 1--7, step counts 1--4, and a rational positive step, it checks exact stage-to-quadrature identities, the rank formula, the Cauchy--Binet determinant, the signed-error entries, and the special first-full-rank determinants. The supplied run passes **289 exact-rational assertion families**. These finite tests provide reproducibility but are not a substitute for the universal Vandermonde and scalar-quadrature proof above.

Run: `python3 verification.py`. Only the Python standard library is required.

## Relationship to prior work

Zhang, Lan, and Jing (2026), equations (3)--(6) and Theorem 3.2, establish the integrating-factor SSPRK schemes and unconditional positive-semidefinite preservation. Their Theorem 3.4 treats norm error for the second-order method, not exact finite-step rank recovery or signed Loewner covariance errors. The identification with trapezoidal and Simpson quadrature is an algebraic consequence of their stages for constant forcing; this basic reduction is **not asserted to be a new quadrature method**.

Bertram and Faßbender (2019), especially sections 1 and 3, and Bertram and Faßbender (2020), section 1.1, discuss time-integrated/empirical Gramians, positive-weight low-rank quadrature, and connections with Runge--Kutta and model reduction. Thus a general finite-node rank upper bound was already accessible from established Gramian factorizations. The present claim is the *sharp simultaneous rank attainment and all-positive-step Loewner-inertia classification* for the explicit new methods on the controllable integrator chain; those exact thresholds are not stated in the inspected sources. An earlier specialized polynomial-quadrature observation could still cover part or all of the classification.

## Limitations

The sharp signed-error classification is restricted to nilpotent integrator chains with rank-one constant forcing, fixed equal steps, and exact arithmetic. The universal rank ceiling applies to arbitrary real \(A,b\) with rank-one forcing but does not assert that arbitrary controllable systems attain it: sampled exponentials can alias. Positive semidefiniteness alone is not a guarantee of orderwise upper or lower covariance bounds; the finding does not establish stability, conditioning, floating-point accuracy, or performance of a specific implementation. Finite exact-rational tests do not prove the quantified theorem, which rests on the analytical argument. A comprehensive theorem-by-theorem historical uniqueness guarantee is not claimed.

## References

1. W. Zhang, R. Lan, X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703v1, publicly submitted 14 June 2026. https://arxiv.org/abs/2606.15703
2. C. Bertram, H. Faßbender, *Lyapunov and Sylvester equations: A quadrature framework*, arXiv:1903.05383v1, 2019. https://arxiv.org/abs/1903.05383
3. C. Bertram, H. Faßbender, *A link between gramian based model order reduction and moment matching*, arXiv:2003.03101v1, 2020. https://arxiv.org/abs/2003.03101
