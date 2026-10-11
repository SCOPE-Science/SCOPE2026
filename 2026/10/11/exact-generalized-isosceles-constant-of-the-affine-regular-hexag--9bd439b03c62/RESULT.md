# Exact generalized isosceles constant of the affine-regular hexagonal plane
## Finding
For the real affine-regular hexagonal Banach plane \(X_H=(\mathbb R^2,N)\), with
\[
N(s,t)=\begin{cases}
\max\{|s|,|t|\},&st\ge 0,\\
|s|+|t|,&st\le 0,
\end{cases}
\]
the generalized isosceles-orthogonality constant introduced by Liu, Yang, Fu and Li satisfies
\[
\Omega'(X_H)=\frac54.
\]
The same source computes \(\Omega(X_H)=49/40\), so the relaxation from unit isosceles pairs to arbitrary isosceles pairs is strict and has the exact size
\[
\Omega'(X_H)-\Omega(X_H)=\frac1{40}.
\]

## Assumptions and scope
All spaces and scalars are real. Isosceles orthogonality means \(x\perp_I y\) if and only if \(N(x+y)=N(x-y)\). The generalized constant is
\[
\Omega'(X)=\sup_{x\perp_I y}\frac{\lVert x+2y\rVert^2+\lVert2x+y\rVert^2}{5\lVert x+y\rVert^2},
\]
with the quotient taken on nonzero admissible pairs. The source proves the equivalent identity
\[
\Omega'(X)=\frac9{10}\,\gamma_X\!\left(\frac13\right),
\qquad
\gamma_X(t)=\sup_{x,y\in S_X}\frac{\lVert x+ty\rVert^2+\lVert x-ty\rVert^2}2.
\]
The result concerns only this affine-regular hexagonal norm and this constant.

## Proof
Write \(B_H\) for the unit ball. Its six extreme points are
\[
(1,1),\ (1,0),\ (0,-1),\ (-1,-1),\ (-1,0),\ (0,1).
\]
For fixed \(t=1/3\), the function
\[
F(x,y)=\frac12\left(N\left(x+\frac13y\right)^2+N\left(x-\frac13y\right)^2\right)
\]
is convex on \(B_H\times B_H\), because the square of a norm is convex and both arguments are affine. A convex function on a compact polytope attains a maximum at an extreme point; iterating this observation in the two factors shows that the maximum of \(F\) on \(B_H\times B_H\) is attained at a pair of the six vertices. Since those vertices lie on \(S_H\), this maximum is exactly \(\gamma_{X_H}(1/3)\).

Exact evaluation of the \(36\) vertex pairs gives only the values \(10/9\) and \(25/18\). The larger value is attained, for example, by \(x=(1,1)\) and \(y=(1,0)\), because
\[
N\left(x+\frac13y\right)=\frac43,
\qquad
N\left(x-\frac13y\right)=1.
\]
Hence
\[
\gamma_{X_H}\!\left(\frac13\right)=\frac12\left(\frac{16}9+1\right)=\frac{25}{18},
\]
and therefore
\[
\Omega'(X_H)=\frac9{10}\cdot\frac{25}{18}=\frac54.
\]
For a direct extremizing pair in the definition of \(\Omega'\), take \(u=(1,1/2)\) and \(v=(0,1/2)\). Then \(N(u+v)=N(u-v)=1\), so \(u\perp_I v\), while \(N(u+2v)=3/2\) and \(N(2u+v)=2\); the defining quotient is \(5/4\).

The identity \(\Omega'(X)=\frac9{10}\gamma_X(1/3)\) can also be reconstructed directly. If \(x\perp_I y\), put \(u=(x+y)/2\) and \(v=(x-y)/2\); then \(\lVert u\rVert=\lVert v\rVert\), and rescaling the two equal-length vectors converts the defining quotient into \(9/10\) times the \(t=1/3\) profile. Conversely, starting from unit \(a,b\) and taking \(u=(a+b)/2\), \(v=(a-b)/2\) gives \(u\perp_I v\) and recovers the same value, proving equality of the suprema.

## Verification
The bundled verifier enumerates all \(36\) vertex pairs using exact rational arithmetic, checks that the maximum profile value is \(25/18\), checks the factor \(9/10\), and independently verifies the direct isosceles witness \(u=(1,1/2)\), \(v=(0,1/2)\). It prints `VERIFY_OK` only if every exact identity holds.

## Relationship to prior work
The motivating preprint introduced \(\Omega\), computed \(\Omega(X_H)=49/40\) for this same affine-regular hexagonal plane, later introduced the generalized constant \(\Omega'\), and proved \(\Omega'(X)=\frac9{10}\gamma_X(1/3)\). It did not give the corresponding exact value of \(\Omega'\) for its hexagonal example. The present calculation fills that specific gap and shows that the generalization changes the canonical example by the nonzero amount \(1/40\).

Searches for the exact value, its \(\gamma_X(1/3)\) formulation, and the affine-regular hexagonal model did not locate a prior statement of \(\Omega'(X_H)=5/4\). Later work on related isosceles constants was also checked for broader or equivalent coverage; the located results concern other constants or other classes of spaces and do not imply this exact value.

## Limitations
The proof is specific to the two-dimensional affine-regular hexagonal norm and uses the finite vertex structure of its unit ball. It does not give a formula for \(\Omega'\) on general Radon planes or on a parameterized family of hexagonal norms. The literature search is finite, so an unindexed equivalent computation under different notation remains a residual originality risk.

## References
1. Q. Liu, Z. Yang, Y. Fu, Y. Li, “New geometric constants of isosceles orthogonal type,” arXiv:2111.08392. The first public version was submitted on 16 November 2021; the inspected revision is arXiv:2111.08392v2.
2. Y. Ramadana, “Isosceles Orthogonal Geometric Constants for Morrey Spaces,” Turkish Journal of Mathematics and Computer Science 17 (2025), 184–190, DOI 10.47000/tjmcs.1606207.
