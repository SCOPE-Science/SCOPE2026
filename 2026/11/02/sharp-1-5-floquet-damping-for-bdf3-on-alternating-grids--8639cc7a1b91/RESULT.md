# Sharp \(1/5\) Floquet damping for BDF3 on alternating grids

## Finding

Let \(r>0\) be fixed and let the consecutive step lengths of the variable-step third-order backward differentiation formula (BDF3) alternate forever between \(H=rh\) and \(h>0\). On the scalar homogeneous equation \(y'=0\), the exact two-update companion (Floquet) matrix has multipliers \(1,z_+(r),z_-(r)\). For **every** \(r>0\),
\[
\max\{|z_+(r)|,|z_-(r)|\}<\frac15,
\qquad
\sup_{r>0}\max\{|z_+(r)|,|z_-(r)|\}=\frac15.
\]
The constant is optimal but is not attained for any finite positive ratio. Hence BDF3 is strongly zero-stable on each fixed alternating grid, with no restriction on the size of its adjacent step jumps.

There is also an exact two-to-one transition between real and conjugate parasitic Floquet modes. Put
\[
F(u)=u^4-22u^3-173u^2-390u-279.
\]
It has a unique root \(u_*>2\), and set \(R_*=(u_*+\sqrt{u_*^2-4})/2\) (numerically \(R_*\approx28.5149315929\)). For \(1/R_*<r<R_*\) the parasitic multipliers form a nonreal conjugate pair; for \(0<r<1/R_*\) or \(r>R_*\), both are real and negative; and at either boundary they coincide at a negative real value.

## Assumptions and scope

At time \(t_n\), with \(h_n=t_n-t_{n-1}>0\), define variable-step BDF3 by differentiating at \(t_n\) the unique cubic interpolant through \(y_n,y_{n-1},y_{n-2},y_{n-3}\) at the four corresponding time nodes. For the homogeneous equation \(y'=0\), solve this derivative condition for \(y_n\) to obtain
\[
y_n=c_1(h_n,h_{n-1},h_{n-2})y_{n-1}
+c_2(h_n,h_{n-1},h_{n-2})y_{n-2}
+c_3(h_n,h_{n-1},h_{n-2})y_{n-3}.
\]
Assume one fixed \(r>0\) and an infinite step sequence alternating \(rh,h,rh,h,\ldots\), where \(h>0\) may depend on the finite-grid refinement but \(r\) does not. No hypothesis is imposed on the initial three values. Here *zero-stable* means that, for each fixed \(r\), homogeneous solution values remain uniformly bounded in the number of steps by a constant times the norm of the initial values. The claim does not imply a bound uniform in \(r\) as \(r\to0\) or \(r\to\infty\).

## Proof

**1. Interpolation coefficients.** Translating the current node to zero, the four interpolation abscissae are
\[
0,\quad -h_n,\quad -(h_n+h_{n-1}),\quad -(h_n+h_{n-1}+h_{n-2}).
\]
Differentiation of the four Lagrange basis polynomials yields, on a long step with the preceding short and long steps, the recurrence coefficients
\[
(c_1,c_2,c_3)_{\mathrm L}=
\frac{1}{5r^2+5r+1}
\big((r+1)(2r+1)^2,\;-r(2r+1)^2,\;r(r+1)\big).
\]
On a short step with preceding long and short steps, these are
\[
(c_1,c_2,c_3)_{\mathrm S}=
\left(\frac{(r+1)(r+2)^2}{r(r^2+5r+5)},\;
-\frac{(r+2)^2}{r(r^2+5r+5)},\;
\frac{r+1}{r^2+5r+5}\right).
\]
Both triples sum to \(1\), as required by constant reproduction.

**2. Floquet characteristic polynomial.** For \(c=(c_1,c_2,c_3)\), write
\[
A(c)=\begin{pmatrix}c_1&c_2&c_3\\1&0&0\\0&1&0\end{pmatrix},\qquad
M(r)=A(c_{\mathrm S})A(c_{\mathrm L}),
\]
and abbreviate
\[
\Delta(r)=(r^2+5r+5)(5r^2+5r+1)>0.
\]
Direct matrix multiplication yields \(\det M=r(r+1)^2/\Delta\) and \(\operatorname{tr}M-1=(-r^4+r^3+5r^2+r-1)/\Delta\). Because \(M(1,1,1)^{\mathsf T}=(1,1,1)^{\mathsf T}\), the other two eigenvalues are exactly the roots of
\[
 z^2-T(r)z+E(r)=0,\qquad
 T(r)=\frac{-r^4+r^3+5r^2+r-1}{\Delta(r)},\qquad
 E(r)=\frac{r(r+1)^2}{\Delta(r)}.
\]
The same spectrum is obtained with the opposite phase order of the two updates.

**3. Strict universal damping.** The elementary quadratic Schur--Jury test says that the roots of \(z^2-Tz+E\), for real \(T,E\), lie strictly in \(|z|<1/5\) if and only if
\(1-5T+25E>0\), \(1+5T+25E>0\), and \(1-25E>0\). Here direct simplification gives
\[
1-5T+25E=\frac{2(5r^4+25r^3+38r^2+25r+5)}{\Delta(r)}>0,
\]
\[
1+5T+25E=\frac{6r(10r^2+21r+10)}{\Delta(r)}>0,
\]
\[
1-25E=\frac{5r^4+5r^3+r^2+5r+5}{\Delta(r)}>0.
\]
All three numerators are manifestly positive for every \(r>0\). This proves the strict disk bound. At both endpoints \(r\to0^+\) and \(r\to\infty\), \(T(r)\to-1/5\) and \(E(r)\to0\), so the two roots tend to \(0\) and \(-1/5\). Thus \(1/5\) is sharp, and the distinct eigenvalue \(1\) is simple. For fixed \(r\), every power of the fixed monodromy \(M(r)\) is bounded: the eigenvalue \(1\) has multiplicity one, and all other eigenvalues have modulus below \(1\). An arbitrary homogeneous trajectory is a succession of full two-step powers and at most one fixed companion matrix, so the original BDF3 recurrence is zero-stable.

**4. Real/complex-mode boundary.** Its parasitic discriminant is
\[
T(r)^2-4E(r)=\frac{r^4}{\Delta(r)^2}
F\!\left(r+\frac1r\right).
\]
For \(u\ge2\), \(F(2)<0\), while \(F(u)\to\infty\). The coefficient sequence \((1,-22,-173,-390,-279)\) has one sign change, so Descartes' rule gives exactly one positive root; therefore it has exactly one root \(u_*>2\). Its sign is negative below \(u_*\) and positive above. Since \(r+1/r\) lies below \(u_*\) precisely for \(1/R_*<r<R_*\), the discriminant changes sign in the asserted way. In either exterior real-root regime, \(E>0\), and \(T<0\) by continuity and its negative endpoint limits, so the two real roots are negative. Their coincidence at the boundaries follows from the vanishing discriminant.

## Verification

The standalone program `verify_bdf3_periodic.py` derives both recurrence rows from cubic Lagrange interpolation rather than assuming them, constructs the exact monodromy, verifies all displayed trace, determinant, Schur--Jury, discriminant and endpoint identities in symbolic rational arithmetic, and checks representative numerical ratios. Run with Python 3 and SymPy:

```sh
python verify_bdf3_periodic.py
```

Finite numerical samples are supplementary; universal strict inequalities follow from the displayed positive polynomials. The phase boundary is defined exactly by the unique positive root rather than by a floating-point calculation.

## Relationship to prior work

Guglielmi and Zennaro (first publicly online November 8, 2000) use joint spectral radii to analyze general variable-step BDF3 zero stability; their reported sufficient adjacent-ratio bound near \(1.501\) does not establish the present unbounded **alternating**-ratio case. Li and Liao (2022) establish a later variable-step BDF3 stability theorem when almost all adjacent ratios are below approximately \(2.553\); with fixed \(r>2.553\), an alternating grid has infinitely many ratios exceeding that threshold. Söderlind, Fekete and Faragó (2018) treat smooth nonuniform grids with adjacent ratios approaching \(1\), not fixed nonsmooth alternation. The result here addresses the narrow Floquet subfamily with exact parasitic radius and its real/complex-mode threshold, not general variable-grid stability.

## Limitations

The theorem concerns the **homogeneous** BDF3 recurrence on one fixed two-periodic positive-step grid. It does not guarantee contractivity on \(y'=\lambda y\), A-stability, stability under perturbation of the recurrence at each update, or global error estimates for nonlinear problems. The transient bound may depend strongly on \(r\). Only the full two-update parasitic spectrum has the universal \(1/5\) bound; the one-step companion matrices need not be individually contractive. A highly relevant 2000/2001 joint-spectral-radius paper could be inspected only at the abstract/metadata level, so a previously unlocated equivalent treatment of alternating grids remains a priority risk. Independent mathematical review has not been performed.

## References

1. N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445–458. First online November 8, 2000. https://doi.org/10.1007/s211-001-8010-0
2. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, SIAM J. Numer. Anal. 60 (2022), 2253–2272. https://arxiv.org/abs/2201.00527
3. G. Söderlind, I. Fekete and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, 2018. https://arxiv.org/abs/1804.04553
