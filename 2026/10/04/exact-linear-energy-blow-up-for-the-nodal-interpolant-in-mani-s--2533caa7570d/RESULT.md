# Exact linear energy blow-up for the nodal interpolant in Manià's Lavrentiev example
## Finding
For Manià's functional
\[
I[u]=\int_0^1 (u(x)^3-x)^2(u'(x))^6\,dx,
\]
with boundary data \(u(0)=0\) and \(u(1)=1\), the exact minimizer is \(u_*(x)=x^{1/3}\) and has energy zero. Let \(u_n\) be the continuous piecewise-affine interpolant through the exact nodal values
\[
u_n(j/n)=(j/n)^{1/3},\qquad j=0,\ldots,n.
\]
For \(j\ge 0\), put
\[
d_j=(j+1)^{1/3}-j^{1/3},\qquad p_j(s)=j^{1/3}+s d_j,
\]
and
\[
c_j=d_j^6\int_0^1igl(p_j(s)^3-(j+s)igr)^2\,ds.
\]
Then the energy has the exact cell decomposition
\[
I[u_n]=n\sum_{j=0}^{n-1}c_j.
\]
The series \(C=\sum_{j=0}^\infty c_j\) converges and
\[
C=0.07619104142716668\ldots.
\]
Moreover,
\[
c_j=rac{1}{196830}j^{-6}+O(j^{-7}),
\]
so
\[
I[u_n]=Cn-rac{1}{984150}n^{-4}+O(n^{-5}).
\]
Thus this canonical geometric approximation converges uniformly to the exact singular minimizer while its exact continuous energy diverges linearly. The first cell already contributes exactly \(8n/105\); the remaining cells change the linear coefficient only from \(8/105\) to \(C\).

## Assumptions and scope
The mesh is uniform, with nodes \(x_j=j/n\). The interpolation is the ordinary nodal piecewise-affine interpolation of \(u_*(x)=x^{1/3}\), and the energy is the exact integral of the original Manià integrand along that interpolant. No quadrature replacement of the energy is used. The statement concerns this canonical interpolant, not the minimizer of a finite-dimensional discretized optimization problem.

## Proof
Fix a cell \([j/n,(j+1)/n]\) and write \(x=(j+s)/n\), where \(0\le s\le1\). Nodal interpolation gives
\[
u_n(x)=n^{-1/3}p_j(s),\qquad u_n'(x)=n^{2/3}d_j.
\]
Hence
\[
u_n(x)^3-x=n^{-1}igl(p_j(s)^3-(j+s)igr),\qquad dx=rac{ds}n.
\]
Substitution into the functional shows that the cell energy is exactly \(n c_j\), proving the decomposition.

For \(j=0\), one has \(d_0=1\) and \(p_0(s)=s\), so
\[
c_0=\int_0^1(s^3-s)^2\,ds=rac17-rac25+rac13=rac8{105}.
\]
For \(j\ge1\), let \(f(t)=t^{1/3}\) on \([j,j+1]\). Its chord is \(p_j\), and concavity gives \(p_j\le f\). The standard linear-interpolation remainder and \(|f''(t)|\le(2/9)j^{-5/3}\) give
\[
0\le f(j+s)-p_j(s)\lerac1{36}j^{-5/3}.
\]
Also \(d_j\le(1/3)j^{-2/3}\). Therefore
\[
0\le (j+s)-p_j(s)^3\lerac{2^{2/3}}{12}j^{-1},
\]
which implies \(c_j=O(j^{-6})\). Thus \(C=\sum_{j=0}^\infty c_j\) converges.

To obtain the sharp tail, write \(q=1/j\) and
\[
(1+q)^{1/3}-1=rac q3-rac{q^2}9+O(q^3).
\]
Uniformly for \(0\le s\le1\), this yields
\[
d_j^6=rac1{729}j^{-4}igl(1+O(j^{-1})igr)
\]
and
\[
p_j(s)^3-(j+s)=rac{s(s-1)}{3j}+O(j^{-2}).
\]
Since \(\int_0^1s^2(1-s)^2\,ds=1/30\), it follows that
\[
c_j=rac1{729\cdot9\cdot30}j^{-6}+O(j^{-7})=rac1{196830}j^{-6}+O(j^{-7}).
\]
Finally,
\[
\sum_{j=n}^\infty j^{-6}=rac1{5n^5}+O(n^{-6}),
\]
so
\[
I[u_n]=n\left(C-\sum_{j=n}^\infty c_jight)=Cn-rac1{984150}n^{-4}+O(n^{-5}).
\]

## Verification
The accompanying checker evaluates the exact polynomial integral defining each \(c_j\) at high precision, verifies \(c_0=8/105\), encloses the numerical value of \(C\), and checks the predicted \(j^6c_j\) and scaled tail against the analytic constants. It uses only the Python standard library and prints `VERIFY_OK` on success.

For direct evaluation, if \(a=j^{1/3}\), \(d=d_j\), and
\[
A=3a^2d-1,\qquad B=3ad^2,\qquad D=d^3,
\]
then
\[
\int_0^1igl(p_j(s)^3-(j+s)igr)^2\,ds
=rac{A^2}3+rac{AB}2+rac{B^2+2AD}5+rac{BD}3+rac{D^2}7.
\]
This is the formula used by the checker.

## Relationship to prior work
Pereira, Cruz, and Torres define the same Manià functional, identify \(u_*(x)=x^{1/3}\), and in their Table 3 report the exact-energy values of the piecewise-linear curve through points of the optimal solution for several uniform meshes. Their displayed PLFOpt values \(0.229,0.381,0.610,0.762,1.143,1.524\) for \(n=3,5,8,10,15,20\) numerically track the linear law above after rounding, but the paper gives only the qualitative divergence theorem for Lipschitz approximants and does not derive the exact cell decomposition, the linear coefficient \(C\), or the sharp tail term.

Ball and Knowles give the classical piecewise-linear finite-element discussion for the same example and cite the broader result that sufficiently regular approximants converging almost everywhere to \(u_*\) have energy tending to infinity. That qualitative implication already covers divergence of the nodal interpolants, so divergence itself is not claimed as new here. Ball's 2001 survey also computes the boundary-layer test function that is linear only on \((0,h)\) and equal to \(u_*\) afterward, obtaining the exact first-cell energy \(8/(105h)\); accordingly, the first-cell calculation is also treated as prior-covered. The new quantitative content here is the exact energy of the fully piecewise-affine uniform nodal interpolant on every cell, the convergent full coefficient \(C\), and the sharp tail asymptotic. Feng and Schnake likewise motivate an enhanced finite-element method from the failure of standard finite elements, without this full nodal-interpolant asymptotic.

## Limitations
The result is specific to the uniform nodal interpolant of \(x^{1/3}\) and to exact integration of the original energy. It does not classify nonuniform meshes, optimized piecewise-linear approximants, or quadrature-discretized energies. The originality comparison is limited to the inspected primary and closely related literature plus targeted semantic and web searches; an unindexed source could contain an equivalent asymptotic.

## References
1. C. T. L. M. Pereira, P. A. F. Cruz, and D. F. M. Torres, *A Discrete Algorithm to the Calculus of Variations*, arXiv:1003.0934v1 (2010); later Int. J. Math. Stat. 9 (2011), 26–41.
2. J. M. Ball and G. Knowles, *A numerical method for detecting singular minimizers*, Numerische Mathematik 51 (1987), 181–197, doi:10.1007/BF01396748.
3. J. M. Ball, *Singularities and computation of minimizers for variational problems*, in *Foundations of Computational Mathematics*, London Mathematical Society Lecture Note Series 284, Cambridge University Press (2001), 1–20.
4. X. Feng and S. Schnake, *An enhanced finite element method for a class of variational problems exhibiting the Lavrentiev gap phenomenon*, arXiv:1610.03111v1 (2016).
