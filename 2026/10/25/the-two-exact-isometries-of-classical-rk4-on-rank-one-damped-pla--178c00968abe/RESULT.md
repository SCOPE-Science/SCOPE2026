# The two exact isometries of classical RK4 on rank-one damped planar oscillators

## Finding
Let \(a,\omega,h>0\), and consider the strictly damped planar system \(u'=Lu\) with
\[
L=\begin{pmatrix}-a&-\omega\\ \omega&0\end{pmatrix}.
\]
The classical fourth-order Runge–Kutta matrix \(R_4(hL)\), where \(R_4(z)=1+z+z^2/2+z^3/6+z^4/24\), is Euclidean orthogonal for **exactly two** choices of the dimensionless pair \((x,Y)= (ah,(\omega h)^2)\).

Write \(\rho\) for the unique root in \((2,3)\) of \(\rho^3-4\rho^2+12\rho-24=0\). The first pair is
\[
(x,Y)=\left(4-\rho,\frac{24}{\rho}\right),\qquad R_4(hL)=I.
\]
Write \(v\) for the unique positive root of \(v^3+12v^2-96v-64=0\), and \(q=\sqrt v\). The second pair is
\[
(x,Y)=\left(2+q,4+q+\frac v2-\frac4q\right),\qquad R_4(hL)=-I.
\]
The first gives a false fixed trajectory under RK4; the second gives a false period-two trajectory. Both contradict the strict Euclidean decay of every nonzero exact trajectory. They also differ under frequency perturbation at fixed \(x\): at the first pair, increasing \(Y\) makes every singular value of \(R_4(hL)\) exceed one and decreasing \(Y\) makes every singular value less than one, locally; at the second pair, for *either* sufficiently small nonzero change in \(Y\), one singular value is above one and the other below one.

## Assumptions and scope
All parameters \(a,\omega,h\) are positive real numbers. The norm is the ordinary Euclidean norm; the RK method is the classical explicit four-stage fourth-order scheme in exact arithmetic. 'Orthogonal' means \(R_4(hL)^{\mathsf T}R_4(hL)=I\), for all initial vectors. The theorem classifies orthogonal steps, not all steps of nonexpansion or absolute stability. The root equations uniquely define the displayed pairs.

## Proof
Put \(A=hL\), \(x=ah\), \(y=\omega h>0\), and \(Y=y^2\). Cayley–Hamilton gives \(A^2+xA+YI=0\), hence
\[
R_4(A)=UI+VA,\quad U=1+\frac{Y(Y-x^2+4x-12)}{24},\quad
V=-\frac{x^3-4x^2-2xY+12x+4Y-24}{24}.
\]
Therefore
\[
R_4(A)=\begin{pmatrix}U-xV&-yV\\yV&U\end{pmatrix},\qquad
(R_4(A)^{\mathsf T}R_4(A))_{12}=xyV^2.
\]
Since \(x,y>0\), orthogonality forces \(V=0\), so \(R_4(A)=UI\) with \(U=\pm1\). Thus all isometries are **exact scalar identities or sign reversals**, and the problem reduces to finding left-half-plane quadratic factors of the scalar polynomials \(R_4(z)\mp1\).

For \(+I\),
\[
24(R_4(z)-1)=z(z^3+4z^2+12z+24).
\]
The cubic has exactly one real root, \(-\rho\): its derivative \(3z^2+8z+12\) is everywhere strictly positive. Its two remaining roots form a nonreal pair. By Vieta, their sum is \(\rho-4<0\) and their product is \(24/\rho\). Thus their real companion matrix has trace \(\rho-4=-x\) and determinant \(24/\rho=Y\). No other admissible pair exists: the zero root is excluded because \(Y>0\), and the unique other real root cannot form a negative-real pair. These conjugate roots are simple, so polynomial evaluation yields \(R_4(A)=I\).

For \(-I\), substitute \(t=z+1\) to obtain
\[
24(R_4(z)+1)=t^4+6t^2+8t+33.
\]
There is one positive root \(v\in(5,6)\) of \(v^3+12v^2-96v-64=0\): the derivative has one positive zero and the polynomial changes from negative to positive after that minimum. Put \(q=\sqrt v\), \(B=3+v/2-4/q\), and \(C=3+v/2+4/q\). The cubic identity implies \(BC=33\), and direct expansion yields
\[
t^4+6t^2+8t+33=(t^2+qt+B)(t^2-qt+C).
\]
Both quadratics have negative discriminant because \(q^2-4B=-12-v+16/q<0\) and \(q^2-4C=-12-v-16/q<0\). Their root pairs have real parts \(-q/2\) and \(+q/2\), respectively, in \(t\). Since \(q>2\), exactly the first pair becomes a strictly left-half-plane pair after shifting back by one. Its sum in \(z\) is \(-2-q\), and its product is \(1+q+B=4+q+v/2-4/q\). The quartic has no real roots, since \(t^4+(6t^2+8t+33)>0\); hence the left conjugate pair is the only admissible one, with no repeated-root degeneracy. Evaluation gives \(R_4(A)=-I\).

For the perturbation classification, keep \(x\) fixed and differentiate \(Q(Y)=R_4(A)^{\mathsf T}R_4(A)\) at a scalar resonance \(R_4(A)=sI\), \(s\in\{1,-1\}\), along the family \(y=\sqrt Y\). Since \(V=0\), variations of \(A\) carry no first-order contribution. Writing \(U_Y=(2Y-x^2+4x-12)/24\), \(V_Y=(x-2)/12\), we obtain
\[
Q'(Y)=2s\operatorname{diag}(U_Y-xV_Y,U_Y).
\]
At the \(+I\) resonance, \(U_Y=1/\rho>0\) and \(U_Y-xV_Y>0\) because \(V_Y=(2-\rho)/12<0\). Thus \(Q'\) is positive definite. At the \(-I\) resonance, \(U_Y=(v-4)/(12q)>0\) and \(U_Y-xV_Y=-(q+4/q)/12<0\), making \(Q'\) indefinite. Eigenvalue continuity gives the asserted strict signs for all sufficiently small nonzero perturbations.

Finally, \(L+L^{\mathsf T}=\operatorname{diag}(-2a,0)\) gives \(\frac{d}{dt}\|u(t)\|_2^2=-2a\,u_1(t)^2\). If a nonzero exact solution retained its original norm at positive time, \(u_1\) would vanish on an interval, forcing \(u_2=0\) from \(u'_1=-au_1-\omega u_2\), a contradiction. Hence the continuous semigroup is strictly contracting on nonzero vectors for every positive time.

## Verification
The accompanying standalone `verify.py` checks the Cayley–Hamilton polynomial reduction and orthogonality obstruction using exact rational matrix arithmetic at multiple inputs; it also bisects the two defining cubic roots at high decimal precision, reconstructs both scalar resonances, checks the factorization and discriminants, and confirms all first-order perturbation signs. Run `python3 verify.py`; it prints `VERIFY_OK` on success. General uniqueness, strict signs, and all-time exact decay are proved above and do not follow merely from finite tests.

## Relationship to prior work
Achleitner, Arnold, and Jüngel (arXiv:2308.05689v1) study strong stability of explicit Runge–Kutta methods on semi-dissipative and hypocoercive linear systems, primarily focusing on sufficiently small step sizes and method order. Sun, Wei, and Wu (arXiv:2201.06501v1) develop energy identities for Runge–Kutta methods. Sun and Shu (arXiv:1811.10680v1) analyze strong stability and multistep contractivity. These results motivate the setting but do not, in the inspected material, provide the complete positive-parameter exact-isometry classification or its two opposite frequency-perturbation signatures. The existence of special stability-polynomial levels is elementary; the new claim is the rigid full classification and the perturbation dichotomy for this partially damped coupled system.

## Limitations
The theorem is exclusively a classification of exact Euclidean isometries for one rank-one damped planar family with positive coupling, not a general characterization of all stable RK4 timesteps. No inference is made about floating-point exact equality, nonlinear integration, adaptive controllers, or higher dimensions. An equivalent interpretation of scalar RK4 level curves in older stability literature remains an originality risk; independent validation has not been performed.

## References
1. F. Achleitner, A. Arnold, and A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge–Kutta methods*, arXiv:2308.05689v1 (2023), https://arxiv.org/abs/2308.05689.
2. Z. Sun, J. Wei, and K. Wu, *On Energy Laws and Stability of Runge–Kutta Methods for Linear Seminegative Problems*, arXiv:2201.06501v1 (2022), https://arxiv.org/abs/2201.06501.
3. Z. Sun and C.-W. Shu, *Stability of the fourth order Runge–Kutta method for a linear semi-bounded operator*, arXiv:1811.10680v1 (2018), https://arxiv.org/abs/1811.10680.
