# Explicit completion of the additive degenerate exponent for two-step \(p\)-Laplacian problems
## Finding
Let \(p>1\), \(0<\tau<T\), and
\[
a(t)=\begin{cases}a_+>0,&0\le t<\tau,\\-a_-<0,&\tau\le t\le T.\end{cases}
\]
Consider the additive degenerate exponent \(\gamma=0\):
\[
(\phi_p(u'))'+a(t)=0,\qquad \phi_p(s)=|s|^{p-2}s.
\]
A positive Neumann solution or a positive \(T\)-periodic solution exists if and only if
\[
a_+\tau=a_-(T-\tau).
\]
When this condition holds, each boundary-value problem has exactly one solution shape modulo addition of constants. Put
\[
M=a_+\tau=a_-(T-\tau),\qquad q=\frac{p}{p-1},\qquad A(t)=\int_0^t a(s)\,ds.
\]
Then every Neumann solution satisfies
\[
\phi_p(u'(t))=-A(t),
\]
and every periodic solution satisfies
\[
\phi_p(u'(t))=\frac M2-A(t).
\]
The corresponding oscillations are
\[
\Delta_N=\frac{T}{q}M^{1/(p-1)},\qquad
\Delta_P=\frac{T}{q\,2^q}M^{1/(p-1)}=2^{-p/(p-1)}\Delta_N.
\]
Thus the exponent omitted from the focal existence-and-uniqueness theorem has a complete quotient-by-translation classification, and the periodic and Neumann solution shapes have a universal oscillation ratio.

## Assumptions and scope
A positive solution means a function \(u\in C^1([0,T])\) with \(\phi_p(u')\in W^{1,1}(0,T)\), satisfying the equation almost everywhere and \(u(t)>0\) for every \(t\in[0,T]\). The Neumann conditions are \(u'(0)=u'(T)=0\); the periodic conditions are \(u(0)=u(T)\) and \(u'(0)=u'(T)\).

The result concerns only the structurally degenerate exponent \(\gamma=0\) and the two-step weight above. It does not address the other excluded exponent \(\gamma=p-1\), nor weights with nonconstant profiles inside the positive and negative subintervals.

## Proof
Let
\[
y(t)=\phi_p(u'(t)).
\]
At \(\gamma=0\), the equation becomes \(y'=-a(t)\), hence
\[
y(t)=y(0)-A(t).
\]
Both Neumann and periodic derivative conditions force \(y(T)=y(0)\), so
\[
A(T)=\int_0^T a(t)\,dt=0.
\]
For the two-step weight this is exactly \(a_+\tau=a_-(T-\tau)\). This proves necessity for both boundary conditions.

Assume now that the mean is zero and write \(M=a_+\tau=a_-(T-\tau)\). Then \(A\) increases linearly from \(0\) to \(M\) on \([0,\tau]\) and decreases linearly from \(M\) to \(0\) on \([\tau,T]\). Since \(\phi_p^{-1}=\phi_q\), where \(q=p/(p-1)\), the Neumann conditions impose \(y(0)=0\), and therefore
\[
u'(t)=\phi_q(-A(t)).
\]
This derivative is fixed independently of the additive constant. Integrating it gives one profile \(U_N\); every Neumann solution is \(U_N+C\), and choosing \(C\) sufficiently large makes it positive. Conversely, every Neumann solution has this derivative, so all positive Neumann solutions belong to that one additive orbit.

Because \(A(t)>0\) for \(0<t<T\), the Neumann profile is strictly decreasing. Its oscillation is
\[
\begin{aligned}
\Delta_N
&=\int_0^T A(t)^{q-1}\,dt\\
&=\left(\frac1{a_+}+\frac1{a_-}\right)\int_0^M z^{q-1}\,dz\\
&=\frac{T}{M}\frac{M^q}{q}=\frac{T}{q}M^{q-1}.
\end{aligned}
\]
Since \(q-1=1/(p-1)\), this is the displayed formula for \(\Delta_N\).

For the periodic problem write \(c=y(0)\). The derivative is \(u'=\phi_q(c-A(t))\), and position periodicity is equivalent to
\[
0=\int_0^T\phi_q(c-A(t))\,dt.
\]
The two linear branches of \(A\) traverse the same interval \([0,M]\), so
\[
\int_0^T\phi_q(c-A(t))\,dt
=\left(\frac1{a_+}+\frac1{a_-}\right)\int_0^M\phi_q(c-z)\,dz.
\]
Using \(d(|r|^q/q)/dr=\phi_q(r)\), the last integral is
\[
\frac{|c|^q-|c-M|^q}{q}.
\]
It vanishes exactly when \(c=M/2\). Hence the periodic derivative is uniquely fixed, every periodic solution is one translate of a single profile \(U_P\), and sufficiently large translates are positive.

The periodic derivative vanishes when \(A=M/2\), namely at \(t=\tau/2\) and \(t=(T+\tau)/2\). These are respectively the maximum and minimum of the periodic profile. Therefore
\[
\begin{aligned}
\Delta_P
&=\left(\frac1{a_+}+\frac1{a_-}\right)\int_{M/2}^M(z-M/2)^{q-1}\,dz\\
&=\frac{T}{M}\frac{(M/2)^q}{q}
=\frac{T}{q\,2^q}M^{q-1}.
\end{aligned}
\]
Dividing by the Neumann formula gives \(\Delta_P/\Delta_N=2^{-q}=2^{-p/(p-1)}\).

## Verification
Every step is analytic. The key checks are: integration of the momentum equation; equivalence of the boundary derivative condition with zero mean of the weight; the exact inverse \(\phi_p^{-1}=\phi_q\); the two-branch change of variables through the triangular primitive \(A\); uniqueness of the periodic momentum from \(|c|^q=|c-M|^q\); and the two elementary power integrals yielding the oscillations. No finite experiment or numerical certificate is used as a substitute for proof.

## Relationship to prior work
Cagnetta's 2026 preprint proves the existence-and-uniqueness classification for every \(\gamma\notin\{0,p-1\}\). It explicitly identifies \(\gamma=0\) as structurally degenerate under additive translations and observes that its normalized scalar condition can hold only at zero mean. The paper does not state the complete \(\gamma=0\) solution families, quotient uniqueness, the periodic initial momentum \(M/2\), or the oscillation formulas above.

The 2021 paper of Boscaggin, Feltrin and Zanolin develops the two-step time-map framework and treats nondegenerate exponent ranges. The 2026 source describes its earlier discussion of \(\gamma=0\) as a degenerate case motivating exclusion from ordinary uniqueness. The present result resolves that excluded additive case directly rather than by extending the nondegenerate time-map monotonicity argument.

## Limitations
The classification relies crucially on the fact that \(u^0=1\), which makes the momentum equation independent of \(u\), and on the two-step geometry, which makes the primitive \(A\) traverse \([0,M]\) once in each direction. For a general mean-zero sign-changing weight, quotient uniqueness still follows from strict monotonicity of the periodic closure integral, but the closed oscillation ratio need not equal \(2^{-p/(p-1)}\). That broader statement is not claimed here.

## References
1. A. Cagnetta, “A uniqueness result for two-step indefinite \(p\)-Laplacian equations,” arXiv:2610.06068v1, first public 2026-10-05.
2. A. Boscaggin, G. Feltrin, F. Zanolin, “Uniqueness of positive solutions for boundary value problems associated with indefinite \(\phi\)-Laplacian-type equations,” Open Mathematics 19 (2021), 163–183, arXiv:2009.00854v1, DOI:10.1515/math-2021-0003.
