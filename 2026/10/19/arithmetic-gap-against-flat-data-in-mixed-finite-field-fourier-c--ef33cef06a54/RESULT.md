# An arithmetic gap against flat data in mixed finite-field Fourier convolution

## Finding
Let \(F=\mathbb F_q\) be a finite field of odd order \(q\ge5\). Write \(P=\{(t,t^2):t\in F\}\) and \(H=\{(u,u^{-1}):u\in F^\times\}\). For any \(f:F\to\mathbb C\), place \(f(t)\) at \((t,t^2)\), extend by zero elsewhere, and write \(f_P\) for that function. The hyperbola indicator is \(1_H\). Define the normalized mixed-convolution quotient
\[
Q(f)=\frac{\|f_P*1_H\|_{\ell^2(F^2)}^2}{(q-1)\|f\|_{\ell^2(F)}^2},\qquad f\ne0.
\]
The constant input \(f(t)=1\) has \(Q(1)=2(q-1)/q\), but is never a maximizer, even locally. In fact, the sharp quotient \(\mathcal C_q=\max_{f\ne0}Q(f)\) obeys the explicit strict gap
\[
\boxed{\mathcal C_q\ge\frac{2(q-1)}q+\frac{q-2}{q(q-1)^3}>Q(1).}
\]
The theorem includes all odd prime powers, not just prime fields. The precise optimum \(\mathcal C_q\) is not determined.

## Assumptions and scope
Counting measures are used in all \(\ell^2\) norms and convolution: \((h*k)(z)=\sum_{v\in F^2}h(v)k(z-v)\). The hyperbola input is fixed at its constant value one, while the parabolic input varies freely over nonzero complex functions. Distinct input points are parameterized by \(t\in F\) and \(u\in F^\times\). Characteristic two is excluded because the uniqueness calculation below divides by two. No assertion about the operator norm when both inputs vary is made.

## Proof
Let \(v_t=1_{(t,t^2)+H}\in\mathbb R^{F^2}\), and define the real symmetric Gram matrix \(A=(\langle v_t,v_s\rangle)_{t,s\in F}\). It is positive semidefinite with integer entries and
\[
\|f_P*1_H\|_2^2=f^*Af,\qquad A_{tt}=q-1.
\]
The sum \(\sum_{t,s}A_{ts}\) counts ordered pairs of representations of the same vector as a sum of one point of \(P\) and one point of \(H\). The diagonal representation pairs contribute \(q(q-1)\). For two different hyperbola parameters \(u,v\in F^\times\), equality of the sums requires
\[
t+u=s+v,\qquad t^2+u^{-1}=s^2+v^{-1}.
\]
Here \(s-t=u-v\ne0\). Subtract the second coordinates, divide by \(u-v\), and obtain \(t+s=-(uv)^{-1}\). Since the characteristic is odd, these two linear equations have exactly one solution \((t,s)\in F^2\) for each ordered \((u,v)\), \(u\ne v\). Thus
\[
S:=\mathbf1^*A\mathbf1=q(q-1)+(q-1)(q-2)=2(q-1)^2.
\]
This immediately gives \(Q(\mathbf1)=S/[q(q-1)]=2(q-1)/q\).

Write \(R=A\mathbf1\), whose components are nonnegative integers. Since \(\sum_t R_t=S=2(q-1)^2=q(2q-4)+2\), the \(q\) integer row sums cannot all be equal. In particular \(A\mathbf1\) is not proportional to \(\mathbf1\), which is a necessary critical-point condition for the Hermitian Rayleigh quotient. Therefore constant inputs are not even stationary and cannot maximize.

More quantitatively, among all integer vectors with coordinate sum \(q(2q-4)+2\), the squared norm is minimized by \(q-2\) coordinates equal to \(2q-4\) and two coordinates equal to \(2q-3\). With \(\mu=S/q\), this gives
\[
\|A\mathbf1\|_2^2=\|R\|_2^2\ge\frac{S^2}{q}+\frac{2(q-2)}q.
\]
As \(A\) is positive semidefinite, \(A^2\preceq\lambda_{\max}(A)A\). Evaluating at \(\mathbf1\) yields
\[
\lambda_{\max}(A)\ge\frac{\mathbf1^*A^2\mathbf1}{\mathbf1^*A\mathbf1}\ge\frac Sq+\frac{q-2}{q(q-1)^2}.
\]
Dividing by \(q-1\) proves the boxed lower bound and strictness. Every argument applies over any finite field of odd order.

## Verification
The proof uses two exact identities: a unique off-diagonal collision for every ordered pair of distinct nonzero hyperbola parameters, and the congruence \(S\equiv2\pmod q\). A reproducible exact-integer checker `verify.py` constructs the Gram matrix directly for prime orders \(5,7,11,13,17,19\), checks \(A=A^T\), positive diagonal \(q-1\), total entry sum \(2(q-1)^2\), and nonconstant integral row sums, and verifies the stated variance lower bound. Its finite checks are not an infinite-field proof.

## Relationship to prior work
González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first public 2024-05-26), prove constant-extremizer statements for certain **single** finite-field parabola and paraboloid extension problems and calculate corresponding self-convolutions. Their surface pairings and convolution identities do not include the mixed planar parabola–inverse-hyperbola Gram matrix above. The present statement concerns the fixed-hyperbola, varying-parabola mixed operator; it neither disproves nor modifies their single-surface results. The exact-integer nondivisibility certificate gives a uniform, explicit obstruction to transferring flat-input extremality to this mixed configuration.

## Limitations
The sharp constant, its maximizers, the possibility of larger explicit gains, and the version with both inputs variable remain open here. The displayed bound is a strict and quantified obstruction, not an exact spectral formula. The comparison to prior literature is best-knowledge and cannot rule out an unindexed equivalent mixed-convolution result.

## References
1. Cristian González-Riquelme and Diogo Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, initial submission May 26, 2024; https://arxiv.org/html/2405.16647v2 . Relevant discussion: introduction and Section 3.
2. Alex Iosevich, Doowon Koh and Mark Lewko, *Finite field restriction estimates for the paraboloid in high even dimensions*, arXiv:1712.05549 (2017); https://arxiv.org/abs/1712.05549 . Background on additive energy and finite-field extension, rather than on the mixed planar convolution.
