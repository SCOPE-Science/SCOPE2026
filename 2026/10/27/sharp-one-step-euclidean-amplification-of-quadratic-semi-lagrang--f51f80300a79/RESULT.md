# Sharp one-step Euclidean amplification of quadratic semi-Lagrangian interpolation

## Finding

For every integer \(N\ge 2\), let \(T_s:\mathbb C^{2N}\to\mathbb C^{2N}\) be the periodic uniform-grid, nodal piecewise-quadratic semi-Lagrangian interpolation update with real signed displacement \(s\), measured in grid spacings. Put \(t=s-\lfloor s\rfloor\) and \(u=t(1-t)\). In the **unweighted nodal Euclidean norm**, the exact induced one-step norm is
\[
\boxed{\|T_s\|_{2\to2}^{2}=1-2u+2u^{2}+2u\sqrt{1+(1-u)^{2}}.}
\]
The norm is independent of the number of cells, depends only on the distance of \(s\) from the nearest integer, and is strictly increasing with \(u\) on \([0,1/4]\). Hence
\[
\boxed{\sup_{N\ge2,\ s\in\mathbb R}\|T_s\|_{2\to2}=\frac{\sqrt5}{2},}
\]
with equality precisely when \(s\in\mathbb Z+1/2\). For a noninteger displacement, the largest singular value occurs at the zero Fourier frequency, and every nonzero Fourier frequency has a strictly smaller largest singular value. Integer displacements induce permutations and have norm one.

At half-grid displacement the positive two-periodic input \((1,3,1,3,\ldots)\) is mapped to \((5/2,5/2,\ldots)\), attaining the norm \(\sqrt5/2\). This demonstrates a sharp \(25\%\) increase in **squared nodal norm after one update** despite power stability of the underlying scheme.

## Assumptions and scope

The periodic grid has \(2N\) equally spaced nodes \(x_j=jh\), indexed modulo \(2N\), with \(N\ge2\). On each element \([x_{2k},x_{2k+2}]\), reconstruct the unique quadratic interpolant passing through the values at \(x_{2k},x_{2k+1},x_{2k+2}\). The update \(T_s\) evaluates this periodic reconstruction at \(x_j+sh\) for each nodal index \(j\). The sign convention is immaterial to the norm because grid reflection is unitary. Exact arithmetic and the Euclidean norm of the \(2N\) nodal values are used. This is not the function-space \(L^2\) norm weighted by the finite-element mass matrix.

For a displacement \(r\in[0,1]\), the three reference Lagrange basis polynomials are
\[
L_0(v)=\tfrac12(v-1)(v-2),\quad L_1(v)=v(2-v),\quad L_2(v)=\tfrac12v(v-1).
\]
The even and odd output values of each element are obtained by inserting \(v=r\) and \(v=1+r\), respectively, in these polynomials. Periodic indices are taken modulo \(2N\). The formulas also define the endpoint interpolation unambiguously.

## Proof

**1. Reduction to a cell Fourier symbol.** Group the nodal components by consecutive even–odd pairs. For \(0\le r\le1\), the update is block circulant with its only nonzero block columns given by
\[
A_0=\begin{pmatrix}\frac{(r-1)(r-2)}2&r(2-r)\\ \frac{r(r-1)}2&1-r^2\end{pmatrix},\qquad
A_1=\begin{pmatrix}\frac{r(r-1)}2&0\\ \frac{r(r+1)}2&0\end{pmatrix}.
\]
The discrete block Fourier transform is unitary after normalization. Accordingly, with \(q\) ranging over the \(N\)th roots of unity,
\[
\|T_r\|_{2\to2}=\max_{q^N=1}\|B_r(q)\|_2,\qquad
B_r(q)=A_0+qA_1.
\]
Writing \(a,b,c,d\) for the four entries of \(B_r(q)\), direct substitution yields
\[
B_r(q)=\begin{pmatrix}
\frac{(r-1)(r-2)+q r(r-1)}2&r(2-r)\\
\frac{r(r-1)+q r(r+1)}2&1-r^2
\end{pmatrix}.
\]

**2. Exact singular-value invariants.** Set \(u=r(1-r)\in[0,1/4]\) and \(z=(1-\operatorname{Re}q)/2\in[0,1]\). Since \(|q|=1\), expanding \(\operatorname{tr}(B_r(q)^*B_r(q))\) and \(|\det B_r(q)|^2\) gives, exactly,
\[
F(z)=2-4u+4u^2+2u(1-u)z,\qquad
D(z)=1-4u+u(2+u)z.
\]
Thus the squared singular values are precisely the two real nonnegative roots of \(\xi^2-F(z)\xi+D(z)=0\). At \(q=1\), or \(z=0\), the larger root is
\[
X(u)=\frac{F(0)+\sqrt{F(0)^2-4D(0)}}2
=1-2u+2u^2+2u\sqrt{1+(1-u)^2}.
\]
In particular, \(B_r(1)(1,1)^{\mathsf T}=(1,1)^{\mathsf T}\), so \(X(u)\ge1\).

**3. Zero frequency strictly dominates.** For \(0<u\le1/4\), the inequality \(\sqrt{1+(1-u)^2}<3/2\) implies
\[
X(u)<1+u+2u^2\le1+\tfrac32u\le\frac{2+u}{2(1-u)}.
\]
The endpoint \(u=1/4\) is harmless: \(\sqrt{1+(3/4)^2}=5/4<3/2\). Also \(F(z)\le2\), because \(F(z)\le2-2u+2u^2\le2\). For the singular-value characteristic polynomial \(P_z(\xi)=\xi^2-F(z)\xi+D(z)\), the identities above give
\[
P_z(X(u))=uz\bigl[(2+u)-2(1-u)X(u)\bigr]>0\qquad(z>0).
\]
Moreover, \(X(u)\ge1\ge F(z)/2\), so \(X(u)\) lies to the right of the vertex of this upward-opening quadratic. Its strictly positive value therefore places it strictly above the larger root of \(P_z\). Thus \(\|B_r(q)\|_2^2<X(u)\) whenever \(q\ne1\). Since every finite Fourier set contains \(q=1\), the exact full-matrix norm squared equals \(X(u)\) for every \(N\ge2\). For \(u=0\), the update is a nodal permutation, and the same formula gives one.

**4. Sharp displacement envelope.** For \(R(u)=\sqrt{1+(1-u)^2}\), differentiating gives
\[
X'(u)=2(R(u)-1)+4u-\frac{2u(1-u)}{R(u)}>0\qquad(0<u\le1/4).
\]
Indeed \(R(u)>1\), and \(4u-2u(1-u)/R(u)\ge2u>0\). Therefore the unique maximum of \(X\) on \([0,1/4]\) occurs at \(u=1/4\), equivalent to \(r=1/2\). Direct substitution gives \(X(1/4)=5/4\). At \(r=1/2\), the zero-frequency symbol has both rows equal to \((1/4,3/4)\); the vector \((1,3)\) maps to \((5/2,5/2)\), with squared norm ratio \(5/4\). Repeating the pair supplies a nonnegative equality witness for every \(N\).

**5. Arbitrary real displacement.** A displacement change by two grid spacings is composition with an even-node cyclic permutation, hence preserves the induced norm. Grid reflection conjugates the update with displacement \(s\) to the update with displacement \(-s\), also preserving the norm. Modulo these transformations, every real displacement is represented by some \(r\in[0,1]\). The corresponding value \(r(1-r)\) equals \(t(1-t)\) for \(t=s-\lfloor s\rfloor\). This extends the established formula and its unique half-integer maximizers to all real \(s\). \(\square\)

## Verification

The embedded stand-alone `check.py` uses exact rational arithmetic for the zero-frequency trace/determinant identities, the half-shift symbol and the positive equality witness. It also evaluates the complex Fourier-symbol trace/determinant and its singular norm at multiple phases; exhaustively sweeps every discrete Fourier block for several finite mesh sizes and a dense sample of fractional displacements. In the packaged version the script reports `PASS` for 7,870 arithmetic/block/witness checks. The algebraic identities and strict inequalities in the proof establish the continuum and all-mesh assertions; sampled checks do not substitute for that proof.

## Relationship to prior work

Ferretti and Mehrenberger (2026) establish power-bounded stability of the same periodic uniform-grid \(\mathbb P_2\) semi-Lagrangian operator via block Fourier diagonalization and eigenstructure. Their block matrices supply the starting representation used here. Their power-bound result does **not** provide the sharp one-step Euclidean induced norm, which can exceed one. The present result gives an exact closed form for that distinct one-step norm, proves its zero-frequency singular maximizer, and supplies a positive equality witness.

Ferretti and Perrone (2007) analyze eigenvalue bounds for quadratic finite-element semi-Lagrangian advection; their available institutional abstract describes eigenvalue estimation rather than the induced-norm envelope. The full 2007 text was not accessible in this investigation and remains an explicit priority uncertainty. Ferretti and Mehrenberger (2020) study stability for **odd-degree** symmetric interpolations, for which their contractivity arguments do not directly imply this even-degree \(\mathbb P_2\) norm law. Generic Fourier block-diagonalization and singular-value formulas are classical ingredients; their use alone is not the claimed contribution.

## Limitations

The theorem covers only uniform one-dimensional periodic grids, quadratic nodal elements, constant displacement, exact arithmetic, and the **unweighted discrete nodal Euclidean norm**. It neither computes mass-matrix-weighted physical energy nor gives a new long-time power bound, positivity theorem, nonlinear stability statement, or variable-coefficient result. A sharp amplification of one update is compatible with uniform boundedness of all powers. The 2007 full text remains an uninspected plausible earlier source, so prior equivalence cannot be excluded solely by the bibliographic checks performed.

## References

1. R. Ferretti and M. Mehrenberger, “Stability of the \(\mathbb P_2\) Semi-Lagrangian scheme,” arXiv:2610.19806v1, first public 2026-10-14, https://arxiv.org/html/2610.19806v1 . See §2, §3.1 equations (7)–(8), and main stability theorem.
2. R. Ferretti and G. Perrone, “On the stability of semi-Lagrangian advection schemes under finite element interpolation,” *Applied and Industrial Mathematics in Italy II*, 2007, pp. 339–350, https://hdl.handle.net/11590/160128 ; full text not inspected.
3. R. Ferretti and M. Mehrenberger, “Stability of semi-Lagrangian schemes of arbitrary odd degree under constant and variable advection speed,” *Mathematics of Computation* 89 (2020), 1783–1805, https://doi.org/10.1090/mcom/3494 .
