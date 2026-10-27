# Exact dual-lattice Fourier zeros and quadratic folds for every planar triangle

## Finding

Let \(P\subset\mathbb R^2\) be an arbitrary nondegenerate closed triangle, with vertices \(v_0,v_1,v_2\). Write \(A=[v_1-v_0\;v_2-v_0]\), regarded as an invertible real matrix whose columns are the two edge vectors, and use the Fourier convention
\[
\widehat{\mathbf 1_P}(\omega)=\int_Pe^{-i\omega\cdot x}\,dx.
\]
The **complete real zero locus** is the affine dual-lattice set
\[
\boxed{\{\omega\in\mathbb R^2:\widehat{\mathbf 1_P}(\omega)=0\}
=\{2\pi A^{-T}(m,n)^T:m,n\in\mathbb Z,\;mn(m-n)\ne0\}.}
\]
In particular, the real zeros are isolated: there are no arcs of real Fourier zeros, and none occurs on a frequency line orthogonal to an edge of \(P\).

If \(N_P(R)\) denotes the number of distinct real zeros in the closed Euclidean ball of radius \(R\), then
\[
\boxed{N_P(R)=\frac{\operatorname{area}(P)}{2\pi}R^2+O_P(R)}
\qquad(R\to\infty).
\]
The first-real-zero radius is therefore the exactly computable excluded-line shortest-vector invariant
\[
\boxed{\kappa(P)=2\pi\min_{m,n\in\mathbb Z,\;mn(m-n)\ne0}
\left\|A^{-T}(m,n)^T\right\|_2.}
\]
For the standard right triangle \(T=\{(u,v):u,v\ge0,\ u+v\le1\}\), this equals \(2\pi\sqrt2\).

At each zero, the real two-component Fourier map has a rank-one derivative and a nonzero quadratic second derivative along its derivative kernel. More explicitly, for \(X=2\pi m\), \(Y=2\pi n\) with \(mn(m-n)\ne0\),
\[
\widehat{\mathbf 1_T}((1+t)X,(1+t)Y)=\frac{t^2}{2}+O_{m,n}(t^3)
\qquad(t\to0).
\]
Thus the isolated zeros are quadratic real folds, not regular transverse intersections of two independent nodal curves.

## Assumptions and scope

The vertices of \(P\) are three distinct affinely independent points in \(\mathbb R^2\). The Euclidean norm is the standard one in the fixed physical coordinates. The transform uses angular frequency \(\omega\) without a \(2\pi\) factor in the exponential. Boundaries of triangles have area zero and cause no ambiguity. The statement concerns **real** frequency vectors, not the full complex zero variety of the entire Fourier–Laplace transform. The first-zero radius is strictly positive because the nonzero allowed integer lattice is discrete.

## Proof

**Step 1: Exact transform in barycentric coordinates.** Parameterize the standard triangle by \(0\le v\le1\) and \(0\le u\le1-v\). Direct integration gives, for real \(\xi,\eta\) away from the three exceptional lines \(\xi=0\), \(\eta=0\), and \(\xi=\eta\),
\[
F(\xi,\eta):=\int_Te^{-i(\xi u+\eta v)}\,du\,dv
=\frac{\xi e^{-i\eta}-\eta e^{-i\xi}-(\xi-\eta)}
{\xi\eta(\xi-\eta)}.
\]
This is the two-dimensional simplex specialization of the standard vertex-exponential formula. Its denominator is a removable artifact of the integration; the defining integral extends continuously, indeed entirely, across every exceptional line.

**Step 2: A unit-circle rigidity argument, including all signs.** Suppose \(\xi\eta(\xi-\eta)\ne0\), and \(F(\xi,\eta)=0\). Let \(z=e^{-i\xi}\), \(w=e^{-i\eta}\), and \(\lambda=\eta/\xi\in\mathbb R\setminus\{0,1\}\). The numerator equation becomes
\[
w=(1-\lambda)+\lambda z.
\]
Since \(|z|=|w|=1\), taking squared absolute values gives
\[
0=2\lambda(1-\lambda)(1-\operatorname{Re}z).
\]
The real scalar \(\lambda(1-\lambda)\) is nonzero even if \(\lambda\) lies outside the unit interval. Hence \(\operatorname{Re}z=1\), so \(z=1\) and then \(w=1\). Thus \(\xi=2\pi m\) and \(\eta=2\pi n\) for integers \(m,n\ne0\) with \(m\ne n\). Conversely, each such pair makes the numerator vanish while the denominator is nonzero.

**Step 3: Removable-line exclusions.** On \(\xi=0\), integration gives
\[
F(0,\eta)=\frac{1-e^{-i\eta}-i\eta}{\eta^2}\quad(\eta\ne0).
\]
A zero would force \(e^{-i\eta}=1-i\eta\), whose right-hand modulus is \(\sqrt{1+\eta^2}>1\). By exchanging the coordinates, the same conclusion holds on \(\eta=0\). On \(\xi=\eta\), direct integration gives
\[
F(\xi,\xi)=\int_0^1s e^{-i\xi s}\,ds
=\frac{1-(1+i\xi)e^{-i\xi}}{(i\xi)^2}\quad(\xi\ne0).
\]
A zero would force \(|1+i\xi|=1\), again impossible for \(\xi\ne0\). Finally \(F(0,0)=1/2\). Hence Step 2 is the **entire** real-zero census.

**Step 4: Arbitrary affine triangles.** Set \(x=v_0+A(u,v)^T\). Since \(A\) is invertible,
\[
\widehat{\mathbf 1_P}(\omega)
=|\det A|e^{-i\omega\cdot v_0}F(A^T\omega).
\]
The prefactors never vanish. Therefore the zero set is exactly the dual-lattice image stated above. Its allowed lattice points omit precisely the three lines \(m=0\), \(n=0\), and \(m=n\). The omitted points do not form any additional zero curves.

**Step 5: Asymptotic counting.** The dual lattice \(L=2\pi A^{-T}\mathbb Z^2\) has fundamental-cell area \((2\pi)^2/|\det A|\). Counting lattice points in a Euclidean disk by covering its boundary with a fixed number of unit cells gives
\[
\#(L\cap B_R)=\frac{\pi R^2}{(2\pi)^2/|\det A|}+O_A(R)
=\frac{|\det A|}{4\pi}R^2+O_A(R).
\]
Each of the three excluded rank-one sublattices contains only \(O_A(R)\) points in the disk. Because \(\operatorname{area}(P)=|\det A|/2\), subtraction proves the asserted area law. The first-zero expression follows immediately from the complete set and local finiteness. For \(A=I\), the least squared integer norm under \(mn(m-n)\ne0\) is \(2\), attained only by \((m,n)=(1,-1)\) or \((-1,1)\).

**Step 6: Quadratic local structure.** Near an allowed standard-triangle zero, put \(\xi=X+h\) and \(\eta=Y+k\). Taylor expansion of the *exact numerator* gives
\[
\xi e^{-i\eta}-\eta e^{-i\xi}-(\xi-\eta)
=-i(Xk-Yh)+\frac{Yh^2-Xk^2}{2}+O_{X,Y}((|h|+|k|)^3).
\]
The denominator equals \(D+O_{X,Y}(|h|+|k|)\), where \(D=XY(X-Y)\ne0\). Consequently, the real Jacobian of \((\operatorname{Re}F,\operatorname{Im}F)\) at \((X,Y)\) has rank exactly one, with kernel \(Xk-Yh=0\). Along this kernel set \(h=Xt\), \(k=Yt\). The quadratic numerator becomes \(Dt^2/2\), and therefore \(F((1+t)X,(1+t)Y)=t^2/2+O_{X,Y}(t^3)\). For a more intrinsic local-zero check, let \(q=Xk-Yh\), retaining \(h\) as a second local coordinate. The imaginary part of the numerator is \(-q+O((|h|+|q|)^3)\), so by the real implicit-function theorem its vanishing curve is \(q=O(h^3)\). The real part on that curve equals \(Y(X-Y)h^2/(2X)+O(h^3)\), nonzero away from \(h=0\). This proves the local isolated-fold classification without relying on the global census. Invertible affine changes preserve rank and nonvanishing of this kernel-restricted quadratic derivative.

## Verification

An executable checker, included as `checker.py`, uses a direct two-dimensional midpoint quadrature on the standard triangle (not the rational-exponential formula) to compare eight regular and removable-line values with the exact expression. It also checks 306 allowed lattice zeros, samples the three exceptional lines at 27 nonzero frequencies, evaluates the universal radial quadratic coefficient at four distinct zeros, and compares finite lattice counts with the proved leading asymptotic. The saved checker output and Python standard-library-only dependencies accompany this result. These finite computations serve as reproducibility checks; the infinite zero classification, fold geometry, and counting asymptotic follow from the analytic arguments above.

## Relationship to prior work

Diaz, Le, and Robins [1] give general face-poset and Stokes formulas for Fourier transforms of polytope indicators, including formulas applicable to any triangle. Those formulas provide the transform calculation used here, but their primary results concern solid-angle lattice sums; the precise real-zero locus, excluded edge-normal lines, quadratic fold structure, and zero-density law are not given there. In the subsequent work of Machado and Robins [2], theorems on the null sets of general polytopes and the Pompeiu property exclude appropriate complex circles but do not enumerate the real zeros of a triangle. The present classification is consequently a specialized zero-geometry statement requiring the unit-circle rigidity argument and explicit treatment of removable denominators. The existence of an earlier unindexed equivalent calculation remains a publication-priority risk.

## Limitations

The result does not classify real zeros of general polygons with four or more vertices, nor complex-frequency zeros of triangles. The density error \(O_P(R)\) is not asserted to be the best possible for every fixed triangle. The first-zero invariant is an exact shortest-vector formula rather than a universal elementary closed form for arbitrary edge geometry. The generic Fourier transform formula itself is established prior mathematics. No independent publication-priority or mathematical audit is claimed.

## References

[1] R. Diaz, Q.-N. Le, and S. Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, first public arXiv submission February 27, 2016. https://arxiv.org/abs/1602.08593

[2] F. C. Machado and S. Robins, *The null set of a polytope, and the Pompeiu property for polytopes*, arXiv:2104.01957, first public arXiv submission April 5, 2021. https://arxiv.org/abs/2104.01957
