# Sharp non-Hilbert numerical-radius deficit of finite nilpotent shifts

## Finding

For every fixed exponent \(1<p<\infty\), for either scalar field \(\mathbb F=\mathbb R\) or \(\mathbb F=\mathbb C\), and every integer \(n\ge2\), let the nilpotent left shift on \(\ell_p^n(\mathbb F)\) be
\[
S_n(x_1,\ldots,x_n)=(x_2,\ldots,x_n,0).
\]
Write \(v_p(S_n)\) for its spatial numerical radius (the supremum of \(|f(S_nx)|\) over \(\|x\|_p=\|f\|_{p'}=1\) and \(f(x)=1\)). Then
\[
\boxed{\displaystyle \lim_{n\to\infty}(n+1)^2\bigl[1-v_p(S_n)\bigr]=\frac{2(p-1)}{p^2}\pi^2.}
\]
For the Hilbert exponent \(p=2\), this agrees with the exact identity \(v_2(S_n)=\cos(\pi/(n+1))\). The sharp coefficient for general \(p\) equals the Dirichlet spectral gap \(\pi^2\) multiplied by the local curvature \(2(p-1)/p^2\) of the shift's Young deficit.

## Assumptions and scope

The result concerns the spatial numerical radius on a finite-dimensional real or complex \(\ell_p\) space with its canonical norm; \(1<p<\infty\) is **fixed** before taking \(n\to\infty\). No assumption of Hilbert structure or linear self-adjointness is made. The norming functional of a nonzero \(x\in\ell_p^n\) is uniquely given by the coordinate coefficients \(\overline{x_j}|x_j|^{p-2}/\|x\|_p^{p-1}\), with the standard zero convention. In the real case conjugation is omitted. The symbol \(p'=p/(p-1)\) denotes the conjugate exponent.

## Proof

**1. Positive-vector reduction and exact energy.** Smoothness of \(\ell_p^n\), followed by taking absolute values term by term, yields
\[
v_p(S_n)=\max_{x_j\ge0,\ \sum_{j=1}^n x_j^p=1}\ \sum_{j=1}^{n-1}x_j^{p-1}x_{j+1}.
\tag{1}
\]
The inequality from complex or signed vectors to the nonnegative expression is immediate; equality is available because the positive candidate itself is admissible. Put
\[
D_p(a,b)=\frac{p-1}{p}a^p+\frac1p b^p-a^{p-1}b\qquad(a,b\ge0).
\]
Weighted Young's inequality gives \(D_p\ge0\), with equality precisely at \(a=b\). Summing the coefficients of the coordinate powers gives the *exact* identity
\[
1-v_p(S_n)=\min_{\substack{x_j\ge0\\\sum x_j^p=1}}
\left[\sum_{j=1}^{n-1}D_p(x_j,x_{j+1})+
\frac1p x_1^p+\frac{p-1}{p}x_n^p\right].
\tag{2}
\]
The minimum exists by compactness, and both endpoint terms are nonnegative.

**2. Uniform comparison and the local coefficient.** Set \(u_j=x_j^{p/2}\), so that \(\sum_j u_j^2=1\). The homogeneous ratio for positive \(a,b\) can be expressed as
\[
\frac{D_p(a,b)}{(a^{p/2}-b^{p/2})^2}
=F_p(b/a),\qquad
F_p(r)=\frac{(p-1+r^p)/p-r}{(1-r^{p/2})^2}.
\tag{3}
\]
At \(r=1\) this ratio has the removable value
\[
\lim_{r\to1}F_p(r)=c_p:=\frac{2(p-1)}{p^2};
\]
at \(r=0\) its value is \((p-1)/p\), and at \(r=\infty\) the limiting value is \(1/p\). These assertions follow by direct Taylor expansion and leading homogeneous terms. Young's strict equality condition implies \(F_p(r)>0\) for \(r\ne1\). Thus the continuous extension to the compactification \([0,\infty]\) is bounded above and below by positive constants \(M_p\) and \(m_p\):
\[
 m_p(u-v)^2\le D_p(u^{2/p},v^{2/p})\le M_p(u-v)^2
 \qquad(u,v\ge0).
\tag{4}
\]
In particular, the edge energy has an exact quadratic tangent with coefficient \(c_p\) whenever adjacent positive \(u\)-values become asymptotically equal in *relative* size.

**3. Upper bound by Dirichlet sine vectors.** Set \(h=(n+1)^{-1}\), \(s_j=\sin(\pi jh)\) for \(1\le j\le n\), and \(s_0=s_{n+1}=0\). Normalize \(u_j=s_j/(\sum_{k=1}^n s_k^2)^{1/2}\), \(x_j=u_j^{2/p}\). The identity \(\sum_{k=1}^n s_k^2=(n+1)/2\) is exact. Inequality (4) shows that the trial energy in (2) is \(O(h^2)\): the interior sum has this order because \(\sum_{j=0}^n(s_{j+1}-s_j)^2=O(h)\), while the two normalized endpoint penalties are \(O(h^3)\).

On a fixed closed subinterval of \((0,1)\), successive positive sine values have relative ratio approaching one uniformly. Therefore the ratio in (3) tends to \(c_p\). Outside that subinterval, inequality (4) controls the edge contribution by the squared sine differences, which after multiplication by \(h^{-2}\) converge to the integral of \(2\pi^2\cos^2(\pi t)\) over the omitted endpoint regions. That integral vanishes as the regions shrink. The Riemann-sum identity
\[
 h^{-2}\sum_{j=0}^n (u_{j+1}-u_j)^2\longrightarrow\pi^2
\]
then proves the limsup inequality
\[
\limsup_{n\to\infty}h^{-2}(1-v_p(S_n))\le c_p\pi^2.
\tag{5}
\]

**4. Compactness for arbitrary minimizers.** For every \(n\), choose a nonnegative minimizing vector in (2), put \(u_j=x_j^{p/2}\), and extend \(u_0=u_{n+1}=0\). Combining the trial bound from step 3 with (4) and the endpoint terms of (2) gives the uniform discrete Dirichlet estimate
\[
 h^{-2}\sum_{j=0}^n(u_{j+1}-u_j)^2\le C_p.
\tag{6}
\]
Indeed, the missing endpoint squares are bounded by the endpoint penalties, since \(u_1^2=x_1^p\) and \(u_n^2=x_n^p\). Define the piecewise-linear interpolant \(w_n\in H_0^1(0,1)\) by \(w_n(jh)=u_j/\sqrt h\), including zeros at the endpoints. Then exactly
\[
\int_0^1|w_n'|^2\,dt=h^{-2}\sum_{j=0}^n(u_{j+1}-u_j)^2\le C_p.
\tag{7}
\]
Its mass satisfies the exact piecewise-linear quadrature identity
\[
\int_0^1 w_n^2\,dt=\sum_{j=1}^n u_j^2-\frac16\sum_{j=0}^n(u_{j+1}-u_j)^2=1+O(h^2).
\tag{8}
\]
Consequently, after passing to a subsequence, \(w_n\rightharpoonup w\) in \(H_0^1(0,1)\), and \(w_n\to w\) uniformly and in \(L^2(0,1)\). Here \(w\ge0\) and \(\int w^2=1\).

**5. Localization gives the sharp lower bound.** Every edge increment of \(w_n\) is at most \(C_p\sqrt h\) in absolute value by Cauchy--Schwarz and (7). Let \(\chi\) be a continuous cutoff taking values in \([0,1]\) and compactly supported in \(\{t:w(t)>0\}\). Uniform convergence puts the adjacent nodal values of \(w_n\) uniformly away from zero on the support of \(\chi\), and the last increment estimate shows their *relative* differences converge uniformly to zero. Formula (3) then implies, on those edges,
\[
D_p(x_j,x_{j+1})\ge(c_p-o(1))(u_{j+1}-u_j)^2.
\]
Multiplication by \(h^{-2}\) and nonnegative weighted summation, followed by weak lower semicontinuity of the localized \(L^2\) gradient norm, yields
\[
\liminf_{n\to\infty}h^{-2}\sum_{j=1}^{n-1}D_p(x_j,x_{j+1})
\ge c_p\int_0^1\chi(t)|w'(t)|^2\,dt.
\]
Using an increasing family of cutoffs that exhausts \(\{w>0\}\) and the Sobolev fact \(w'=0\) almost everywhere on \(\{w=0\}\), we obtain
\[
\liminf_{n\to\infty}h^{-2}(1-v_p(S_n))\ge c_p\int_0^1|w'|^2\,dt.
\]
The sharp Dirichlet Poincaré inequality in \(H_0^1(0,1)\) gives \(\int|w'|^2\ge\pi^2\int w^2=\pi^2\). Combined with (5), this proves the displayed limit, independently of the selected subsequence.

## Verification

The accompanying `verify.py` checks one exact quartic identity for \(D_4\) by rational polynomial arithmetic, verifies the finite-dimensional Hilbert sine-eigenvector relation at several sizes, and evaluates the explicit sine recovery vectors numerically for different non-Hilbert exponents. The program prints `CHECK_OK` when these finite checks succeed. The general asymptotic and the compactness/localization steps are proved in the text, **not** inferred from finite numerical testing.

## Relationship to prior work

Gaaya, *On the numerical radius of the truncated adjoint shift* (arXiv:1202.3963, initial public version 2012-02-17), studies sharp numerical-radius phenomena for compressions of shifts on Hilbert-space model spaces; in particular the Hilbert nilpotent-shift formula is known. That formula is the \(p=2\) specialization but does not imply the nonlinear curvature \(c_p\) for all non-Hilbert \(\ell_p\) spaces. Müller--Tomilov, *Numerical and essential numerical ranges on \(\ell_p\)* (arXiv:2606.22693, Section 4.6 and Proposition 4.16), studies truncated shifts on \(\ell_p\), including polynomial functional-calculus norm ratios; that is a distinct operator invariant, not the spatial numerical radius's sharp \(n^{-2}\) deficit. Published work titled *Powered-Bohr upper bounds and duality for the ell_p shift calculus* determines bounds for a disk-contractivity radius of the infinite shift, another distinct invariant. No covering general-exponent sharp leading coefficient was found in the inspected sources; the possibility of overlooked historical Banach-space numerical-radius literature remains.

## Limitations

This is a pointwise-in-exponent leading asymptotic for \(1<p<\infty\); it gives neither an exact closed formula for finite \(n\) when \(p\ne2\), nor a convergence rate, a second-order term, or uniform behavior as \(p\) approaches an endpoint. It does not address arbitrary weighted shifts, other norms, or operator norms of shift polynomials. The originality assessment cannot rule out unindexed or inaccessible equivalent treatments of the same nonlinear eigenvalue asymptotic.

## References

1. H. Gaaya, *On the numerical radius of the truncated adjoint shift*, arXiv:1202.3963 (initially posted 2012-02-17), especially the discussion of numerical radii of truncated Hilbert-space shifts.
2. V. Müller and Y. Tomilov, *Numerical and essential numerical ranges on \(\ell_p\)*, arXiv:2606.22693 (2026), particularly Section 4.6 and Proposition 4.16 concerning truncated shifts.
3. *Powered-Bohr upper bounds and duality for the ell_p shift calculus*, published mathematical research record, 2026-09-19, `published-finding corpus/2026/2026/9/19/SCOPE-powered-bohr-bounds-duality-ellp-shift--1b567bc40ed8/RESULT.md` (separate disk-contractivity invariant).
4. Standard Dirichlet Poincaré inequality: the first eigenvalue of \(-d^2/dt^2\) on \(H_0^1(0,1)\) is \(\pi^2\).
