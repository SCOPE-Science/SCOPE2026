# Sharp one-fifth parasitic bound for two-periodic BDF3 meshes

## Finding

For every pair of positive fixed step lengths \(a,b>0\), apply the standard interpolation-defined variable-step third-order backward differentiation formula (BDF3) to the scalar equation \(y'(t)=0\), on a mesh with \(h_{2j+1}=a\) and \(h_{2j+2}=b\). For any three real initial values, the solution sequence is bounded and converges to a constant. More sharply, the two-step monodromy on first differences has both eigenvalues strictly inside the disk of radius \(1/5\), for **every** ratio \(r=a/b>0\). This radius is globally sharp:

\[
\sup_{r>0}\rho(M(r))=\frac15,
\]

with the supremum approached as \(r\to0\) or \(r\to\infty\), not attained at any positive finite ratio. The bound concerns asymptotic two-step eigenvalues; it does **not** provide an initial-error amplification constant uniform in the ratio. Indeed, a single step can amplify a bounded starting discrepancy by an arbitrarily large factor as \(r\to\infty\).

## Assumptions and scope

Let \(h_n=t_n-t_{n-1}>0\) for \(n\ge1\), and fix \(h_1=h_3=h_5=\cdots=a\), \(h_2=h_4=h_6=\cdots=b\), with \(a,b>0\). At each \(n\ge3\), BDF3 means the derivative at \(t_n\) of the cubic interpolant through \((t_{n-j},y_{n-j})\), \(j=0,1,2,3\), set equal to zero. The three starting values \(y_0,y_1,y_2\in\mathbb R\) are arbitrary. Put \(d_n=y_n-y_{n-1}\) and let \(r=h_n/h_{n-1}\); successive ratios alternate between \(a/b\) and \(b/a\).

Set

\[
A(r)=\frac{r^2(4r+3)}{5r^2+5r+1},\qquad
B(r)=-\frac{r(r+1)}{5r^2+5r+1},\qquad
T(r)=\begin{pmatrix}A(r)&B(r)\\1&0\end{pmatrix}.
\]

A complete two-step difference monodromy is \(M(r)=T(1/r)T(r)\). Reversing the starting phase gives the reversed product, which has the same eigenvalues since both factors are invertible.

## Proof

**1. Exact variable-step difference recurrence.** Normalize the latest step to one. The four interpolation nodes relative to its right endpoint are

\[
0,\quad -1,\quad -(1+r^{-1}),\quad -(2+r^{-1}).
\]

Differentiating the four Lagrange basis polynomials yields, after multiplication by the latest step, the coefficients

\[
(w_0,w_1,w_2,w_3)
=\left(\frac{5r^2+5r+1}{(r+1)(2r+1)},\;-(2r+1),\;
\frac{r(2r+1)}{r+1},\;-\frac r{2r+1}\right).
\]

Since \(\sum_jw_j=0\), the BDF3 equation \(\sum_{j=0}^3w_jy_{n-j}=0\) is exactly

\[
w_0d_n+(w_0+w_1)d_{n-1}+(w_0+w_1+w_2)d_{n-2}=0.
\]

It follows by direct simplification that \(d_n=A(r)d_{n-1}+B(r)d_{n-2}\). Hence the difference-state vector \((d_n,d_{n-1})^\mathsf T\) advances via \(T(r)\), and the two-period block via \(M(r)\).

**2. Exact characteristic coefficients.** Write

\[
K(r)=(r^2+5r+5)(5r^2+5r+1)>0.
\]

Matrix multiplication gives

\[
\operatorname{tr}M(r)=-\frac{r^4-r^3-5r^2-r+1}{K(r)},\qquad
\det M(r)=\frac{r(r+1)^2}{K(r)}.
\]

The two nonconstant Floquet multipliers are the roots of \(\lambda^2-(\operatorname{tr}M)\lambda+\det M=0\). Rescale \(\mu=5\lambda\). For a real monic quadratic \(\mu^2-s\mu+p\), both roots lie strictly in the unit disk if and only if \(1+s+p>0\), \(1-s+p>0\) and \(1-p>0\). In this case the three required strict inequalities are

\[
\begin{aligned}
1+5\operatorname{tr}M+25\det M
 &=\frac{6r(10r^2+21r+10)}{K(r)}>0,\\
1-5\operatorname{tr}M+25\det M
 &=\frac{2(5r^4+25r^3+38r^2+25r+5)}{K(r)}>0,\\
1-25\det M
 &=\frac{5r^4+5r^3+r^2+5r+5}{K(r)}>0.
\end{aligned}
\]

Every numerator is strictly positive for \(r>0\). Thus \(\rho(M(r))<1/5\) for every finite positive ratio. Moreover, as \(r\to\infty\), the trace approaches \(-1/5\) and the determinant approaches zero. The eigenvalues therefore approach \(-1/5\) and zero, proving sharpness. The symmetry under \(r\mapsto1/r\) follows as well from the characteristic coefficients.

**3. Boundedness and convergence of the numerical solution.** For each fixed \(r>0\), the spectral radius is less than one. Consequently, the powers \(M(r)^j\) decay exponentially (allowing for a polynomial factor at repeated eigenvalues); the intervening matrices \(T(r)\) and \(T(1/r)\) are fixed and finite. Thus \(\sum_{n\ge3}|d_n|<\infty\), and \(y_n=y_2+\sum_{j=3}^{n}d_j\) converges. In particular, its sup norm is bounded by a finite constant depending on \(r\) times \(\max\{|y_0|,|y_1|,|y_2|\}\).

**4. Failure of ratio-uniform transient control.** Choose \(h_1=h_3=a\), \(h_2=b\), and initial values \((y_0,y_1,y_2)=(0,0,1)\). The first new increment is \(d_3=A(a/b)\), so \(y_3=1+A(a/b)\). Since

\[
\lim_{r\to\infty}\frac{A(r)}r=\frac45,
\]

no bound on all initial-error amplification can be independent of the step ratio. This does not contradict the sharp spectral statement, which is about completed two-step periods at each fixed ratio.

## Verification

Run `python verify.py` with Python 3.10+ and SymPy 1.12+. The standalone verifier derives the interpolation weights from Lagrange polynomials, checks the resulting recurrence and two-step matrix against independently computed rational examples, confirms the characteristic polynomial and all three positive polynomial identities symbolically, and checks the sharp limiting behavior. It reports `PASS: 116 exact/symbolic checks.` The analytic positivity arguments above, rather than any finite experiments, establish the all-ratio theorem.

## Relationship to prior work

Li and Liao, *Stability of variable-step BDF2 and BDF3 methods* (arXiv:2201.00527, first posted 2022-01-03), develop the general variable-coefficient BDF3 difference recurrence and give a sufficient adjacent-step-ratio bound of approximately \(2.553\) for their perturbed-equation stability theorem. Their source formula underlies the setting here; that sufficient bound does not imply this result for arbitrary two-periodic ratios. Söderlind, Fekete and Faragó (arXiv:1804.04553) prove zero stability on smooth nonuniform grids with adjacent ratios approaching one, a different mesh class. Earlier work by Guglielmi and Zennaro (2001) and by Grigorieff and Paes-Leme (1984) develops variable-step BDF3 stability criteria; their complete texts were not accessible in this comparison. No novelty claim is made for the Lagrange formula, the companion-matrix idea or the quadratic disk criterion. Publication priority of the special all-ratio sharp spectral law remains open to independent literature review.

## Limitations

The claim applies to the homogeneous scalar test equation, two exactly repeated positive step lengths and exact arithmetic. It does not claim ratio-uniform zero-stability constants, convergence or bounded-error guarantees for a general nonperiodic grid, nonlinear or stiff-equation absolute stability, or superior accuracy with uneven steps. The fixed ratio must not be allowed to diverge with refinement when invoking the ordinary ratio-dependent zero-stability bound.

## References

1. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527 (first posted 2022-01-03), SIAM Journal on Numerical Analysis 60 (2022), 2253–2272. https://arxiv.org/abs/2201.00527
2. G. Söderlind, I. Fekete and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, arXiv:1804.04553 (2018). https://arxiv.org/abs/1804.04553
3. N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445–458. https://iris.gssi.it/handle/20.500.12571/302
4. R. D. Grigorieff and P. J. Paes-Leme, *On the zero-stability of the 3-step BDF-formula on nonuniform grids*, BIT Numerical Mathematics 24 (1984), 85–91.
