# Global third-order Loewner-square positivity without three-matrix monotonicity

## Finding

Set
\[
q(s)=s+\frac{s^3}{3}+\frac{2s^5}{25},\qquad
u(x)=\frac{x}{100(1+x)},\qquad f(x)=q(\nu(x)),\quad x>0.
\]
For positive nodes \(x_1,\ldots,x_m\), define the real symmetric Loewner matrix \(L_f(x_1,\ldots,x_m)\) by \((L_f)_{ij}=(f(x_i)-f(x_j))/(x_i-x_j)\) if the nodes differ, with diagonal \(f'(x_i)\); use continuous divided differences for repeated nodes.

**Theorem.** The strictly increasing real-analytic function \(f\) is matrix monotone of degree two, but not of degree three. Nevertheless, for *every* triple \(x_1,x_2,x_3>0\),
\[
L_f(x_1,x_2,x_3)\circ L_f(x_1,x_2,x_3)\succeq0.
\]
For each triple of pairwise distinct positive nodes the squared Loewner matrix is positive definite, while the *unsquared* Loewner matrix has two positive and one negative eigenvalues. In particular, the unsquared matrix is indefinite for the explicit nodes \((x_1,x_2,x_3)=(1/3,1,3)\).

This gives a global, not merely one-triple, separation between the third-order squared-Loewner positivity test and degree-three matrix monotonicity.

## Assumptions and scope

All nodes are strictly positive real numbers. Matrix order refers to real symmetric (equivalently Hermitian) positive semidefiniteness. The symbol \(\circ\) means the entrywise (Hadamard) product. Repeated nodes use derivatives and limits, and are included in the positive semidefinite assertion. Matrix monotonicity of degree \(m\) is the order-preservation property of functional calculus on \(m\times m\) positive definite matrices; the standard finite-order Loewner criterion is used.

The assertion concerns the Loewner-square *differential necessary condition* arising in Frobenius radial-convexity studies; it makes **no assertion** that the metric \(\|f(A)-f(B)\|_F\) is radially convex, and does **not** disprove any conjecture identifying full radial convexity with matrix monotonicity.

## Proof

**1. The local divided-difference kernel.** For \(a,b\ge0\), the divided difference of \(q\) is
\[
k(a,b)=1+\frac{a^2+ab+b^2}{3}
       +\frac{2}{25}\sum_{j=0}^{4}a^{4-j}b^j,
\qquad d(a)=k(a,a)=1+a^2+\frac25a^4.
\]
Write \(c=1/100\). The following three polynomial inequalities hold simultaneously on \(0\le a,b,z\le c\). All their claims about coefficients are exact rational identities, reproducible using the appended standalone certificate.

First, the quotient
\[
Q_2(t,u)=\frac{d(t)d(t+u)-k(t,t+u)^2}{u^2}
\]
is a polynomial in \(t,u\), with exactly 16 nonzero terms and constant coefficient \(1/3\). For \(0\le t,u\le c\), the total absolute contribution of its negative-coefficient nonconstant monomials is less than \(1/12\), so \(Q_2(t,u)>1/4\). Hence every two-node Loewner matrix of \(q\) on \((0,c)\) is positive definite for distinct nodes; the diagonal entries \(d(a)\) are strictly positive.

Second, for \(a=t\), \(b=t+u\), \(z=t+u+v\), define
\[
Q_3(t,u,v)=\frac{\det[k(s_i,s_j)]_{i,j=1}^3}
  {(a-b)^2(a-z)^2(b-z)^2},\qquad(s_1,s_2,s_3)=(a,b,z).
\]
This is a polynomial with exactly 44 nonzero rational coefficients, **all negative**, and constant \(-7/675\). Thus \(Q_3<0\) on the nonnegative octant. Consequently every three-node Loewner matrix for pairwise distinct nodes of \((0,c)\) has negative determinant; its positive one- and two-dimensional principal minors force precisely one negative eigenvalue.

Third, set \(K=[k(s_i,s_j)^2]_{i,j=1}^3\) and let
\[
Q_3^{\langle2\rangle}(t,u,v)=\frac{\det K}
 {(a-b)^2(a-z)^2(b-z)^2}.
\]
This is a polynomial having 681 nonzero coefficients: the constant is \(22/675\), and **all 680 others are negative**. Thus it is coordinatewise nonincreasing for nonnegative \(t,u,v\), and on the cube \([0,c]^3\) satisfies
\[
Q_3^{\langle2\rangle}(t,u,v)\ge
Q_3^{\langle2\rangle}(c,c,c)>\frac3{100}.
\]
The two-node principal minors of \(K\) are strictly positive for distinct nodes, because
\[
d(a)^2d(b)^2-k(a,b)^4
=[d(a)d(b)-k(a,b)^2][d(a)d(b)+k(a,b)^2]>0.
\]
Together with the positive diagonals and determinant, this proves \(K\succ0\) for distinct nodes. If nodes collide, continuity gives \(K\succeq0\). Sorting any triple merely permutes rows and columns, so the preceding inequalities apply to arbitrary triples in \((0,c)\).

**2. Transfer to the full half-line.** The map \(\nu:(0,\infty)\to(0,c)\) is strictly increasing and has the rank-one divided difference
\[
\nu^{[1]}(x,y)=\frac{c}{(1+x)(1+y)}.
\]
For arbitrary nodes \(x_i>0\), put \(s_i=\nu(x_i)\) and \(h_i=\sqrt c/(1+x_i)>0\). The divided-difference chain rule yields the exact congruences
\[
L_f(x_1,\ldots,x_m)=\operatorname{diag}(h_i)
 [k(s_i,s_j)]\operatorname{diag}(h_i),
\]
\[
L_f\circ L_f=\operatorname{diag}(h_i^2)
 [k(s_i,s_j)^2]\operatorname{diag}(h_i^2).
\]
They preserve inertia and semidefinite positivity, respectively, even at repeated nodes. Therefore the squared-Loewner positivity holds globally for every triple, and the ordinary two-node matrices are positive semidefinite. The degree-two Loewner criterion proves degree-two matrix monotonicity. On the other hand, \(q'(s)=1+s^2+(2/5)s^4>0\), so \(f\) is strictly increasing, while every three-distinct-node Loewner matrix for \(f\) has negative determinant. The degree-three Loewner criterion rules out degree-three matrix monotonicity.

For an explicit triple, \(x=(1/3,1,3)\) maps to \(s=(1/400,1/200,3/400)\subset(0,c)\); its Loewner determinant is strictly negative by the second polynomial identity. This completes the proof.

## Verification

Run `python check_loewner.py` with Python 3 and SymPy. The script constructs exact rational matrices, divides their determinants by the squared Vandermonde polynomial, checks coefficient counts and signs, and checks strict rational positivity bounds on a cube containing every relevant ordered triple. It additionally verifies a rational explicit three-node witness. It reports three `PASS` lines. The computational identities are finite symbolic polynomial identities (not samples of an infinite family); their coefficient-sign inequalities establish the universally quantified bounds in the proof. No floating-point arithmetic, numerical root inference, or timeout assertion is used.

## Relationship to prior work

Czerwińska, Franco and Merino (2026), arXiv:2610.17393v1, relate Frobenius radial convexity to the Hadamard square of the Loewner matrix in Proposition 4.8 and isolate the three-by-three determinant obstruction in Proposition 4.14. Their work demonstrates sufficiency of the analogous necessary condition in degree two, but does not provide the globally valid third-order squared-Loewner separation proved here. The present result identifies a limitation of the *differential necessary test* only, not a counterexample to their conjecture about full radial convexity.

Hiai and Sano (2010), arXiv:1007.2478, analyze ordinary and conditionally definite Loewner matrices of matrix-monotone and matrix-convex functions. Those general criteria concern different positivity hypotheses; the available abstract does not document this global squared-kernel witness. A complete historical priority comparison with that longer paper has not been established.

## Limitations

The theorem is about Loewner matrices of size at most three and the explicitly given function. It does not determine the squared kernel's positivity in all larger sizes, nor establish full Frobenius radial convexity. The coefficient certificate uses an exact but comparatively large 681-term quotient; the supplied source is needed to replay that certificate. An equivalent construction in earlier matrix-function or positive-kernel literature remains a publication-priority possibility.

## References

1. M. M. Czerwińska, J. A. Franco and A. Merino, *Towards a Characterization of Matrix Monotonicity via Radial Convexity*, arXiv:2610.17393v1 (first posted 12 October 2026), https://arxiv.org/html/2610.17393v1 .
2. F. Hiai and T. Sano, *Loewner matrices of matrix convex and monotone functions*, arXiv:1007.2478 (2010), https://arxiv.org/abs/1007.2478 .
