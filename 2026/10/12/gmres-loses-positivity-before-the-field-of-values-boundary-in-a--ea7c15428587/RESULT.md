# GMRES loses positivity before the field-of-values boundary in a four-state M-matrix family
## Finding
Let \(S\in\mathbb R^{4\times4}\) be the upper shift,
\[
S_{i,i+1}=1,\qquad S_{ij}=0\ \text{otherwise},
\]
and define
\[
A_t=I-tS,\qquad t>0.
\]
Since \(S\ge0\) is nilpotent,
\[
A_t^{-1}=I+tS+t^2S^2+t^3S^3\ge0,
\]
so \(A_t\) is a nonsingular \(M\)-matrix for every \(t>0\). All four eigenvalues of \(A_t\) are equal to \(1\).

Apply unrestarted GMRES to
\[
A_tx=b,\qquad
b=(1,2,2,1)^{\mathsf T},\qquad
x^{(0)}=0.
\]
The Hermitian part is
\[
H_t=\frac{A_t+A_t^{\mathsf T}}2
=
I-\frac t2(S+S^{\mathsf T}).
\]
The largest eigenvalue of the path adjacency matrix \(S+S^{\mathsf T}\) is
\[
2\cos\!\left(\frac{\pi}{5}\right),
\]
hence
\[
H_t>0
\quad\Longleftrightarrow\quad
0<t<\sec\!\left(\frac{\pi}{5}\right)
=
\sqrt5-1.
\]
Therefore, throughout this interval, the numerical range of \(A_t\) lies strictly in the open right half-plane.

The first GMRES iterate is
\[
x^{(1)}=\alpha_1b,
\qquad
\alpha_1=
\frac{b^{\mathsf T}A_tb}{\|A_tb\|_2^2}
=
\frac{2(5-4t)}{9t^2-16t+10}.
\]
Because
\[
\sqrt5-1<\frac54,
\]
one has
\[
x^{(1)}>0
\qquad
\text{for every }0<t<\sqrt5-1.
\]
In fact, positive definiteness of \(H_t\) implies a positive first-step coefficient for every nonzero real right-hand side.

The second GMRES iterate is
\[
x^{(2)}=a(t)b+\beta(t)A_tb,
\]
where
\[
D(t)=9t^4-32t^3+58t^2-56t+26,
\]
\[
a(t)=
\frac{2(13-8t)(t^2-2t+2)}{D(t)},
\qquad
\beta(t)=
-\frac{2(6t^2-14t+13)}{D(t)}.
\]
Its coordinates are
\[
x^{(2)}_1=
\frac{2(4t^3-5t^2-2t+13)}{D(t)},
\]
\[
x^{(2)}_2=
\frac{4(-2t^3+9t^2-15t+13)}{D(t)},
\]
\[
x^{(2)}_3=
\frac{2(-10t^3+32t^2-43t+26)}{D(t)},
\]
and
\[
x^{(2)}_4=
-\frac{2(t-1)(8t^2-15t+13)}{D(t)}.
\]

For every \(t>0\), \(D(t)>0\). Moreover,
\[
8t^2-15t+13>0
\]
for every real \(t\), because its discriminant is \(-191\). On
\[
0<t<\sqrt5-1
\]
the first three numerators are also strictly positive. Consequently, inside the entire right-half-plane numerical-range regime,
\[
x^{(2)}\ge0
\quad\Longleftrightarrow\quad
0<t\le1,
\]
with strict positivity for \(0<t<1\), a single zero coordinate at \(t=1\), and
\[
x^{(2)}_4<0
\qquad
\text{for }1<t<\sqrt5-1.
\]

Thus the coordinatewise positivity boundary \(t=1\) occurs strictly before the field-of-values boundary \(t=\sqrt5-1\).

A fully rational witness is
\[
t=\frac65.
\]
Then
\[
A=
\begin{pmatrix}
1&-6/5&0&0\\
0&1&-6/5&0\\
0&0&1&-6/5\\
0&0&0&1
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\2\\2\\1
\end{pmatrix}.
\]
The Hermitian part is positive definite because
\[
\frac65<\sqrt5-1.
\]
GMRES gives
\[
x^{(1)}
=
\frac1{47}
\begin{pmatrix}
5\\10\\10\\5
\end{pmatrix}>0,
\]
but
\[
x^{(2)}
=
\frac1{1777}
\begin{pmatrix}
6445\\5630\\2000\\-815
\end{pmatrix}.
\]
Meanwhile the exact solution is strictly positive:
\[
A^{-1}b=
\begin{pmatrix}
1001/125\\
146/25\\
16/5\\
1
\end{pmatrix}>0.
\]
The residual norm still decreases:
\[
\|r_0\|_2^2=10,\qquad
\|r_1\|_2^2=\frac{468}{47},\qquad
\|r_2\|_2^2=\frac{6480}{1777}.
\]
The sign loss therefore does not reflect failure of the GMRES residual-minimization objective.

## Assumptions and scope
The result concerns exact-arithmetic, unrestarted GMRES with zero initial guess on the explicit real nonsymmetric family \(A_t=I-tS\). Coordinatewise positivity refers to the original coordinate basis.

The statement does not claim that \(t=1\) is a universal threshold for all \(M\)-matrices. It is an exact phase boundary for the fixed four-state family and the fixed positive right-hand side above.

The field-of-values statement concerns the Hermitian part \(H_t\). For \(0<t<\sqrt5-1\), every Rayleigh quotient has positive real part. No claim is made about positivity of later GMRES iterates for this family.

## Proof
The inverse formula follows from \(S^4=0\):
\[
(I-tS)^{-1}=I+tS+t^2S^2+t^3S^3.
\]
Thus \(A_t\) is inverse-positive and, equivalently, a nonsingular \(M\)-matrix.

The eigenvalues of \(S+S^{\mathsf T}\) are
\[
2\cos\!\left(\frac{k\pi}{5}\right),
\qquad
k=1,2,3,4.
\]
Hence
\[
\lambda_{\min}(H_t)
=
1-t\cos\!\left(\frac{\pi}{5}\right),
\]
which is positive exactly for
\[
t<\sec\!\left(\frac{\pi}{5}\right)=\sqrt5-1.
\]

At the first GMRES step, \(x^{(1)}=\alpha b\) and the residual is
\[
r_1=b-\alpha A_tb.
\]
The normal equation
\[
(A_tb)^{\mathsf T}r_1=0
\]
gives
\[
\alpha_1
=
\frac{(A_tb)^{\mathsf T}b}{\|A_tb\|_2^2}
=
\frac{b^{\mathsf T}A_tb}{\|A_tb\|_2^2}.
\]
Direct substitution of \(b=(1,2,2,1)^{\mathsf T}\) yields the stated rational expression. In the field-of-values interval its numerator is positive.

For the second step,
\[
\mathcal K_2(A_t,b)=\operatorname{span}\{b,A_tb\}.
\]
Write
\[
x^{(2)}=ab+\beta A_tb.
\]
Orthogonality of the residual to
\[
A_t\mathcal K_2(A_t,b)
=
\operatorname{span}\{A_tb,A_t^2b\}
\]
gives a \(2\times2\) Gram system for \(a,\beta\). Exact elimination gives the displayed formulas.

The Gram determinant is
\[
\det G=t^2D(t).
\]
For \(t>0\), the vectors \(A_tb\) and \(A_t^2b\) are linearly independent: if they were equal up to a scalar, their fourth coordinates force the scalar to be \(1\), while \(A_t^2b=A_tb\) would imply
\[
S(A_tb)=0,
\]
which is impossible because the fourth component of \(A_tb\) is \(1\). Therefore
\[
D(t)>0.
\]

The quadratic
\[
8t^2-15t+13
\]
is positive for all real \(t\). It remains to check the first three coordinates in the interval
\[
0<t<\sqrt5-1<\frac54.
\]
For the first numerator,
\[
4t^3-5t^2-2t+13
>
13-5\left(\frac54\right)^2-2\left(\frac54\right)
=
\frac{43}{16}>0.
\]
For
\[
p_2(t)=-2t^3+9t^2-15t+13,
\]
one has
\[
p_2'(t)=-6t^2+18t-15<0
\]
for all real \(t\), and
\[
p_2\!\left(\frac54\right)=\frac{141}{32}>0.
\]
For
\[
p_3(t)=-10t^3+32t^2-43t+26,
\]
the derivative
\[
p_3'(t)=-30t^2+64t-43
\]
is negative for all real \(t\), since its discriminant is negative, and
\[
p_3\!\left(\frac54\right)=\frac{87}{32}>0.
\]
Therefore the first three coordinates stay positive throughout the field-of-values interval, while the fourth coordinate changes sign exactly at \(t=1\).

For the rational witness,
\[
\frac65<\sqrt5-1
\]
because
\[
\left(\frac{11}{5}\right)^2=\frac{121}{25}<5.
\]
Substitution gives the displayed iterates and exact solution.

## Verification
The accompanying `verify.py` uses exact rational arithmetic.

It reconstructs the \(t=6/5\) matrix and right-hand side, computes the first GMRES normal equation, solves the two-step \(2\times2\) normal equations exactly, and verifies the displayed iterates, residual norms, and positive exact solution.

It also checks the closed-form second-iterate formulas at several rational parameters on both sides of \(t=1\), including the zero crossing at \(t=1\). Those finite checks corroborate the algebra; the sign classification on the full interval is proved analytically above.

The checker does not infer any statement about later GMRES iterates or about arbitrary \(M\)-matrices.

## Relationship to prior work
GMRES itself is classical. Saad and Schultz introduced the generalized minimal residual method for nonsymmetric linear systems, defining it through residual minimization over Krylov spaces.

Greenbaum and Trefethen formulate GMRES as a polynomial approximation problem and emphasize the distinction between normal and nonnormal matrices. Their dated 1992 technical report and later journal article are prior work for the polynomial/Krylov viewpoint used here.

Field-of-values bounds for nonsymmetric Krylov convergence are also classical. Such bounds control residual norms or convergence factors, not coordinate signs of iterates.

The present result isolates a different structural question. It gives an exact one-parameter \(M\)-matrix family with positive inverse and positive exact solution for which the second GMRES iterate crosses the boundary of the positive orthant at
\[
t=1,
\]
while the numerical range remains strictly in the right half-plane until
\[
t=\sqrt5-1.
\]
The earlier positivity failure therefore cannot be diagnosed from eigenvalues, from inverse positivity, from first-step positivity, or from right-half-plane numerical-range separation alone.

## Limitations
The phase boundary is family-specific. It does not classify positivity for general nonsingular \(M\)-matrices, preconditioned GMRES, restarted GMRES, or nonzero initial guesses.

The example has four states. No minimal-dimension theorem is claimed.

Older work on positivity-preserving Krylov methods, monotone matrix iterations, or \(M\)-matrix solvers may contain related sign-loss examples under different terminology. The comparison here establishes a distinct exact phase separation against the checked GMRES polynomial and field-of-values literature, not an exhaustive historical classification.

## References
1. Yousef Saad and Martin H. Schultz, *GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems*, SIAM Journal on Scientific and Statistical Computing 7 (1986), 856--869, DOI: 10.1137/0907058.
2. Anne Greenbaum and Lloyd N. Trefethen, *GMRES/CR and Arnoldi/Lanczos as Matrix Approximation Problems*, Courant Institute Technical Report TR1992-607, submitted May 18, 1992; SIAM Journal on Scientific Computing 15 (1994), 359--368, DOI: 10.1137/0915025.
