# The two-extra-mode Nyquist defect of periodic quadratic rectangular Morley spaces

## Finding

Let \(m,n\ge2\) and divide a flat rectangular two-torus into a uniform periodic \(m\times n\) array of axis-aligned rectangles. Define \(V_{m,n}^{\mathrm{per}}\) by taking polynomials of **total degree at most two** on each element, enforcing (i) equality of all incident element values at each periodic grid vertex, and (ii) equality of the averaged **physical normal derivative** across each periodic grid edge, with one common oriented normal at that edge. Then

\[
\boxed{\dim V_{m,n}^{\mathrm{per}}=mn+2\mathbf 1_{\{2\mid m,\;2\mid n\}}.}
\]

In the even-by-even case, the double-Nyquist Fourier character has a **three-dimensional** local polynomial fiber instead of the usual one-dimensional fiber. On reference coordinates \((x,y)\in[-1,1]^2\) in element \((i,j)\), an explicit basis of this exceptional fiber is
\[
(-1)^{i+j}(x^2-1),\qquad(-1)^{i+j}(y^2-1),\qquad(-1)^{i+j}xy.
\]
The same physical functions use each cell's affine reference coordinates; the dimensions are independent of aspect ratio. When either cell count is odd, there is no double-Nyquist character and no defect.

## Assumptions and scope

The domain is a flat two-dimensional torus obtained by identifying opposite faces of a rectangle. Both coordinate meshes are **uniform** and have \(m,n\ge2\) cells. Polynomial degree is total degree two (six coefficients per rectangle), not tensor-product biquadratic \(Q_2\). Periodic continuity is imposed directly on the identified vertex values and edge-averaged coordinate derivatives, as in the two-dimensional specialization of the weak continuity conditions in Ma--Xing--Zhang (2026). No Dirichlet or clamped boundary conditions are imposed. The dimension is over \(\mathbb R\), though complex Fourier fibers are used in the proof.

## Proof

Scale each cell affinely to \([-1,1]^2\). Since each direction's cell width is constant, the common physical derivative scaling cancels from each edge-matching equation. Write a local polynomial as
\[
 p(x,y)=a_0+a_1x+a_2y+a_3x^2+a_4y^2+a_5xy,
 \qquad S=a_0+a_3+a_4.
\]

Translations by one element in the two directions commute. Complexifying the global constraint space and applying the discrete Fourier transform diagonalizes both translations. In the fiber with characters \(z^m=w^n=1\), the coefficients in element \((i,j)\) are \(z^iw^j(a_0,\ldots,a_5)\). Matching the two vertex values on each vertical edge, the two on each horizontal edge, and the mean normal derivatives gives exactly these six equations:
\[
\begin{aligned}
(1-z)S+(1+z)a_1&=0,&(1-z)a_2+(1+z)a_5&=0,\\
(1-w)S+(1+w)a_2&=0,&(1-w)a_1+(1+w)a_5&=0,\\
(1-z)a_1+2(1+z)a_3&=0,&(1-w)a_2+2(1+w)a_4&=0.
\end{aligned}
\]

**Ordinary fibers.** When \(z\ne-1\) and \(w\ne-1\), put \(t=(z-1)/(z+1)\) and \(u=(w-1)/(w+1)\). Solving the equations gives exactly one free scalar \(S\):
\[
(a_0,a_1,a_2,a_3,a_4,a_5)
=S\bigl(1-(t^2+u^2)/2,\ t,\ u,\ t^2/2,\ u^2/2,\ tu\bigr).
\]
In particular, this fiber has complex dimension one; the global real dimension is recovered after pairing complex conjugate characters.

**One Nyquist direction.** If \(z=-1\ne w\), the six equations imply \(S=a_1=a_2=a_4=a_5=0\); only \(a_3\) is free and \(a_0=-a_3\). The sole local shape is a multiple of \(x^2-1\). Interchanging coordinates proves the same one-dimensional conclusion for \(w=-1\ne z\).

**Double Nyquist.** If \(z=w=-1\), the equations reduce to \(S=a_1=a_2=0\), leaving the three independent parameters \((a_3,a_4,a_5)\). They give precisely the three displayed checkerboard polynomials.

There are \(mn\) character pairs. Every fiber contributes one dimension, except the single pair \((-1,-1)\), which contributes three when and only when \(m,n\) are both even. Thus the complex dimension is \(mn+2\mathbf1_{2\mid m,2\mid n}\). As the constraints have real coefficients, complexification preserves dimension, giving the asserted real dimension. This argument classifies every mode without assuming that translates of a compact patch generator span the periodic space.

## Verification

The accompanying standalone `check.py` independently constructs the physical, cellwise interface matrix with six unknown coefficients per cell, with both periodic wraparound directions. Exact integer row reduction returns nullities \(6,6,9,10,12,18\) for grids \(2\times2\), \(2\times3\), \(3\times3\), \(2\times4\), \(3\times4\), \(4\times4\), respectively, matching the theorem. It independently substitutes the three checkerboard modes into every periodic interface equation on the \(2\times2\) torus. Run `python3 check.py` with a standard Python 3 installation. The proof, not the finite tests, establishes the result for all \(m,n\ge2\).

## Relationship to prior work

Ma, Xing and Zhang (2026, arXiv:2610.32048v1) introduce the arbitrary-dimensional weak quadratic rectangular space and prove a basis/dimension theorem with **homogeneous boundary conditions** and a lexicographic boundary-to-interior argument; their paper does not analyze periodic identification. The dimension on a bounded, clamped rectangular mesh is therefore not the periodic-torus result here. Zeng, Zhang and Zhang (2019/2020, arXiv:1903.00938v2) analyze the same two-dimensional reduced rectangular Morley continuity space on bounded domains and obtain, for a different boundary-restricted space, their Theorem 4.1 dimension \(mn+1\). Their result is not a periodic identification theorem. Yim and Sheen (2023, DOI:10.1002/num.23023) explicitly report mesh-parity phenomena for a **piecewise linear** nonconforming periodic quadrilateral space, so parity dependence itself is known; that element has different local degree and continuity functionals. The claimed result is the exact **quadratic** periodic dimension formula and its three-mode Nyquist mechanism, not the generic concept of parity defects.

## Limitations

Only uniform two-dimensional rectangular toroidal meshes are covered. This does not prove a corresponding classification on nonuniform meshes, bounded domains, or in dimensions three and higher; nor does it establish convergence rates or a basis for a complete periodic biharmonic solver. A related older periodic quadratic spline result not located in the inspected sources remains a historical-priority risk. The three exceptional shapes are actual modes, not numerical zero-energy modes of the full Hessian bilinear form; they should not be called spurious nullvectors of the biharmonic stiffness matrix. The algebraic theorem is established here, without independent external review.

## References

1. R. Ma, Y. Xing, S. Zhang, *Piecewise \(P_2\) Finite Element Space on Rectangular Meshes in Arbitrary Dimensions for the Biharmonic Equation*, arXiv:2610.32048v1 (first public 23 October 2026), https://arxiv.org/html/2610.32048v1.
2. H. Zeng, C.-S. Zhang, S. Zhang, *Optimal quadratic element on rectangular grids for \(H^1\) problems*, arXiv:1903.00938v2, https://arxiv.org/pdf/1903.00938.
3. J. Yim, D. Sheen, *\(P_1\)-Nonconforming Quadrilateral Finite Element Space with Periodic Boundary Conditions: Part I*, Numerical Methods for Partial Differential Equations 39 (2023), 3725--3753, https://doi.org/10.1002/num.23023.
