# Exact Tor dimensions count bounded polynomial witnesses

## Finding
Let \(k\) be an algebraically closed field of characteristic zero, let \(m\geq1\), and let \(P\in k[X_1,\ldots,X_m,T]\). In \(R=k[t,x_1,\ldots,x_m,y_1,\ldots,y_m]\), define
\[
f(t,x_1,\ldots,x_m,y_1,\ldots,y_m)=\bigl(t+1,x_1,\ldots,x_m,y_1(x_1-t-1),\ldots,y_m(x_m-t-1)\bigr).
\]
\[
Z=V(t,y_1-x_1,\ldots,y_m-x_m),\qquad
V_P=V(y_1,\ldots,y_m,P(x_1,\ldots,x_m,t)).
\]
For \(n\geq0\), put
\[
F_{i,n}(t,x_i)=\prod_{j=1}^{n}(x_i-t-j),\qquad
I_n=\bigl(y_iF_{i,n}:1\leq i\leq m,\ P(x_1,\ldots,x_m,t+n)\bigr),
\]
where an empty product is \(1\). Whenever the \(m+1\) displayed generators of \(I_n\) form a regular sequence, the exact identity is
\[
\boxed{\dim_k\operatorname{Tor}_1^R\bigl((f^n)^*\mathcal O_{V_P},\mathcal O_Z\bigr)
=\#\{a\in\{0,\ldots,n\}^{m}:P(a,n)=0\}.}
\]
Thus the first Tor dimension is not merely a yes/no indicator of a return: under the stated complete-intersection hypothesis, it is exactly the number of bounded integer witnesses.

## Assumptions and scope
All intersections and structure sheaves are scheme-theoretic over \(k\). The iterate is \(f^n\), and \((f^n)^*\mathcal O_{V_P}\) is represented by \(R/I_n\). The regular-sequence hypothesis is required for the Koszul complex on the generators of \(I_n\) to resolve \(R/I_n\); the result makes no assertion for indices where this hypothesis fails. The field has characteristic zero so that the roots \(0,1,\ldots,n\) are distinct. No assertion is made about higher Tor groups.

## Proof
An induction on \(n\) gives
\[
f^n(t,x_1,\ldots,x_m,y_1,\ldots,y_m)=\bigl(t+n,x_1,\ldots,x_m,y_1F_{1,n}(t,x_1),\ldots,y_mF_{m,n}(t,x_m)\bigr).
\]
Pulling back the ideal \((y_1,\ldots,y_m,P(x,t))\) therefore gives \(I_n\). The ideal of \(Z\) is \(J=(t,y_1-x_1,\ldots,y_m-x_m)\), so \(R/J\cong A:=k[x_1,\ldots,x_m]\). Tensoring the Koszul resolution of \(R/I_n\) with \(R/J\) turns its generators into
\[
H_n(x_1),\ldots,H_n(x_m),P(x_1,\ldots,x_m,n),\qquad
H_n(u)=\prod_{j=0}^{n}(u-j).
\]
The first \(m\) polynomials form a regular sequence in \(A\), and the Chinese remainder theorem gives
\[
B:=A/(H_n(x_1),\ldots,H_n(x_m))
\cong\prod_{a\in\{0,\ldots,n\}^{m}} k.
\]
The Koszul complex on \(H_n(x_1),\ldots,H_n(x_m),P(x,n)\) is the mapping cone of multiplication by \(P(x,n)\) on the Koszul resolution of \(B\). Its first homology is therefore \(\ker(P(x,n):B\to B)\). Under the displayed product decomposition, multiplication by \(P(x,n)\) is diagonal, with coordinate at \(a\) equal to \(P(a,n)\). Its kernel has one copy of \(k\) for each grid point satisfying \(P(a,n)=0\), and no other summands. This proves the identity.

As a specialization, take \(m=1\) and \(P(X,T)=T-(X+1)^2\). The regular-sequence hypothesis holds for every \(n\), and the formula gives Tor dimension \(1\) exactly when \(n\) is a positive square, and \(0\) otherwise. This refines the square-time nonvanishing example in the source by giving the exact dimension and proves the counting formula for every regular-sequence instance above.

## Verification
The proof uses an induction for the iterate, the explicit pullback ideal, the Koszul resolution under the stated regular-sequence hypothesis, and the Chinese remainder decomposition of the square-free polynomials \(H_n\). The final dimension is read off from the diagonal multiplication operator; no numerical experiment or finite enumeration is used to infer the theorem. The case \(n=0\) is included with \(H_0(u)=u\). If \(P(x,n)\) vanishes at every grid point, the kernel is all of \(B\), consistent with the count \((n+1)^m\). For \(m=2\) and \(P=X_1+X_2-T\), the grid count is \(n+1\); the final equation is nonzero on each component of the preceding complete intersection, so the regular-sequence hypothesis holds.

## Relationship to prior work
Bell's *An undecidable problem in dynamics* gives the same return construction and proves that, for one specific polynomial, the first Tor module is nonzero exactly at positive square times. Its general return-set theorem identifies the support condition \(P(a,n)=0\) on the finite grid, but the inspected statements do not identify the Tor dimension with the number of grid witnesses for arbitrary regular-sequence instances. The present claim is a counting refinement of that construction, not a new construction of the return map. Yang and Zhong record the earlier Lee–Nam construction for set-theoretic return sets; the inspected example does not give a Tor-length formula.

## Limitations
The identity is conditional on the pullback generators being a regular sequence at the chosen iterate. It does not classify when that hypothesis holds for arbitrary \(P\), does not handle non-complete-intersection pullbacks, and does not compute higher Tor groups. The novelty assessment is based on the inspected primary texts and mathematical-record searches; unindexed or unpublished equivalent observations remain possible. Independent audit has not been performed.

## References
1. Jason Bell, “An undecidable problem in dynamics,” arXiv:2610.22123v1 (submitted 2026-10-15), Sections 3 and 6, especially Theorem 1.1 and Theorem 1.3 with its proof.
2. She Yang and Xiao Zhong, “Dynamical GCD Problems and a Variant of the Dynamical Mordell–Lang Conjecture,” arXiv:2602.18302v1 (submitted 2026-02-20), Section 1.3, Example 1.12.
