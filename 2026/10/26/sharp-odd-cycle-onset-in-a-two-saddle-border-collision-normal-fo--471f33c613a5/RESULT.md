# Sharp odd-cycle onset in a two-saddle border-collision normal form

## Finding
Consider the planar continuous border-collision normal form \(F(x,y)=(\tau_i x+y+1,-\delta_i x)\), with branch \(i=L\) for \(x<0\) and \(i=R\) for \(x>0\). Put \(\tau_L=L\), \(\delta_L=d\), \(\tau_R=-B\), and \(\delta_R=-u\). In the *two-saddle non-invertible regime*
\[
 d>0,\quad u>0,\quad L>1+d,\quad B>|1-u|,
\]
let an \(LLR\) cycle mean a least-period-three orbit whose forward successive abscissae have signs \((-,-,+)\), and let *attracting* mean that both eigenvalues of the three-step derivative have modulus strictly below one. Define
\[
 U(d)=\frac{3d^3+6d^2+2d+1}{d(-d^2+d+3)},\qquad 0<d<\frac{1+\sqrt{13}}2.
\]
The minimum \(u_*=\min U(d)\) is attained at the unique positive root \(d_*\) of
\[
 9d^4+22d^3+19d^2-2d-3=0.
\]
Numerically \(d_*=0.3636210327378812\ldots\), \(u_*=2.2679028114032818\ldots\). **An attracting strict \(LLR\) period-three orbit exists for some parameters \((L,d,B)\) in the two-saddle regime at a prescribed \(u>0\) if and only if \(u>u_*\).** Equality never permits such an orbit. This is a sharp *existential* parameter frontier, not a claim about all parameters with \(u>u_*\).

## Assumptions and scope
The switching line is excluded from strict itineraries. The map uses constant forcing \(+1\); no global boundedness, uniqueness of other cycles, or global attractor is asserted. Saddleness of both affine fixed points follows from \(L>1+d\) and \(B>|1-u|\): their characteristic polynomials are \(z^2-Lz+d\) and \(z^2+Bz-u\), respectively, and each has an eigenvalue outside the unit circle and the other inside. Cyclic permutations of \(LLR\) describe the same orbit.

## Proof
Write
\[
 A_L=\begin{pmatrix}L&1\\-d&0\end{pmatrix},\qquad A_R=\begin{pmatrix}-B&1\\u&0\end{pmatrix}.
\]
The derivative along an \(LLR\) orbit is \(M=A_RA_L^2\), with determinant \(-d^2u\) and trace \(-B(L^2-d)+L(u-d)\). Define
\[
 J_+=\det(I+M)=1-B(L^2-d)+L(u-d)-d^2u,\\
 J_-=\det(I-M)=1+B(L^2-d)-L(u-d)-d^2u.
\]
The two-dimensional real Schur criterion gives strict attraction exactly when \(J_+>0\), \(J_->0\), and \(1-\det M>0\); the last inequality is automatic. Thus necessarily \(d^2u<1\), \(L^2-d>0\), and
\[
 B<B_{\max}:=\frac{1+L(u-d)-d^2u}{L^2-d}.
\]
Solving the affine three-step fixed-point equation yields the abscissae of the successive \(L,L,R\) points:
\[
 x_0=-\frac{B(L+1)+u(L+d)+d-1}{J_-},\quad
 x_1=-\frac{B(L+d)-L-u(1-d)-1}{J_-},\quad
 x_2=\frac{L^2+Ld+L+d^2-d+1}{J_-}.
\]
These identities hold wherever \(J_-\ne0\). A strict attracting orbit requires \(x_1<0\), hence
\[
 B>B_{\min}:=\frac{L+u(1-d)+1}{L+d}.
\]
Indeed \(x_2>0\) automatically for \(L>1+d\), \(J_->0\). Therefore \(H:=(B_{\max}-B_{\min})(L+d)(L^2-d)>0\) is necessary. Write \(L=1+d+t\), \(t>0\). Direct multiplication gives
\[
\begin{aligned}
H={}&-t^3+[d(u-4)-4]t^2\\
&+[d^2(u-6)+3d(u-3)-4]t\\
&+d(-d^2+d+3)u-(3d^3+6d^2+2d+1).
\end{aligned}
\]
For \(u\le u_*<3\), all coefficients of positive powers of \(t\) are strictly negative. The constant is nonpositive: when \(-d^2+d+3\le0\), it is visibly negative; otherwise it is \(d(-d^2+d+3)(u-U(d))\le0\). This contradicts \(H>0\), proving necessity.

To characterize \(u_*\), \(U\) diverges at both endpoints of its positive-denominator interval. Its derivative has the sign of \(q(d)=9d^4+22d^3+19d^2-2d-3\). The signs of the coefficients of \(q\), in descending order, have exactly one change, and \(q(0)<0\), \(q(d)\to\infty\); hence Descartes' rule gives exactly one positive root and therefore the unique minimum. Direct rational bounds on \(q\) place the root strictly between \(363621/10^6\) and \(363622/10^6\); substitution gives \(u_*<3\).

For sufficiency first suppose \(u_*<u\le(3+\sqrt5)/2\). Take \(d=d_*\) and begin at \(L=1+d\). The constant term of \(H\) is positive, so \(B_{\min}<B_{\max}\). At \(B=B_{\min}\), one has
\[
J_- =\frac{3(d^2+d+1)(1+d-du)}{2d+1}>0,\qquad
B_{\min}-(u-1)=\frac{3(1+d-du)}{2d+1}>0.
\]
Also \(d^2u<1\), and \(u>1\), so \(B_{\min}>|1-u|\). By continuity choose \(L>1+d\) sufficiently close to \(1+d\), then choose \(B\) strictly between \(B_{\min}\) and \(B_{\max}\), sufficiently close to the lower endpoint, preserving \(J_->0\). The resulting \(x_0,x_1<0<x_2\); both Jury inequalities and both strict saddle inequalities hold.

Now suppose \(u>(3+\sqrt5)/2\). Choose \(1/(u-1)<d<1/\sqrt u\), possible exactly in this range, and begin at \(L=1+d\), \(B=u-1\). Here \(J_-=0\), \(J_+=2(1-d^2u)>0\), and the numerator defining \(-x_1J_-\) equals \(3[d(u-1)-1]>0\). Perturb \(B\) upward and \(L\) upward by sufficiently small positive amounts, with the \(B\)-perturbation sufficiently dominant to make \(J_->0\). All strict signs, including \(x_0,x_1<0<x_2\), \(J_+>0\), and \(B>u-1\), then hold by continuity. The strict three-cycle exists and is attracting. These two ranges prove sufficiency for every \(u>u_*\).

## Verification
The accompanying standalone `verify.py` independently reconstructs the return matrix, fixed-point abscissae, polynomial \(H\), the quartic derivative and exact rational sample, checking each identity symbolically. An explicit interior example is
\[
(L,d,B,u)=(7/5,1/3,8/3,3),\quad
(x_0,x_1,x_2)=(-1230/143,-25/143,518/143).
\]
Here \(J_+=14/225>0\) and \(J_-=286/225>0\), and the prescribed itinerary is strict.

## Relationship to prior work
Fatoyinbo and Simpson (2022, arXiv:2210.14445) already establish the existence of attracting \(LLR\) cycles for non-invertible border-collision maps in broader parameter sectors, and supply general symbolic-stability tests. The present result does **not** claim the first attracting \(LLR\) example: it optimizes precisely the contraction/expansion balance under the simultaneous *two-saddle* inequalities, obtaining a necessary and sufficient sharp threshold for the right negative determinant magnitude. Ghosh, McLachlan and Simpson (2024, arXiv:2402.05393) define and investigate this two-saddle region and provide different short-cycle analyses, without the stated three-cycle feasibility frontier in the material inspected. Simpson (2024, arXiv:2408.04790) concerns a zero-determinant boundary, outside our strict regime.

## Limitations
The assertion is about existence *for some left-branch parameters* at each prescribed \(u\), not a universal attractor statement or a parameter-volume estimate. Stable cycles with other itineraries are not classified. The result has self-review analytical and symbolic checks but no independent external audit. An equivalent threshold could exist in incompletely indexed literature; exact historical priority remains subject to independent verification.

## References
1. O. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445 (2022), https://arxiv.org/abs/2210.14445.
2. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393 (first version 2024-02-08), https://arxiv.org/html/2402.05393.
3. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (2024), https://arxiv.org/abs/2408.04790.
