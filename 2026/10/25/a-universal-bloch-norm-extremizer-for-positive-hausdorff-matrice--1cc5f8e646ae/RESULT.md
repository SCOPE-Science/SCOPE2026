# A universal Bloch-norm extremizer for positive Hausdorff matrices

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and let the complex Bloch space \(\mathcal B\) have the norm
\[
\|f\|_{\mathcal B}=|f(0)|+\beta(f),\qquad
\beta(f)=\sup_{z\in\mathbb D}(1-|z|^2)|f'(z)|.
\]
For a finite positive Borel measure \(\mu\) on \((0,1]\) satisfying
\[
I_\mu=\int_{(0,1]}\frac{d\mu(t)}{t}<\infty,
\]
consider the lower-triangular Hausdorff operator
\[
(\mathcal H_\mu f)(z)=\int_{(0,1]}\frac{1}{1-(1-t)z}\,
f\!\left(\frac{tz}{1-(1-t)z}\right)d\mu(t).
\]
**Universal extremizer theorem.** The single function
\[
g(z)=\operatorname{arctanh}z=\frac12\log\frac{1+z}{1-z},
\qquad \|g\|_{\mathcal B}=1,
\]
norms **every** such positive Hausdorff operator: \(\|\mathcal H_\mu\|=\|\mathcal H_\mu g\|_{\mathcal B}\). In particular, let
\[
Q_t(r)=1-(1-t)r,\quad x_t(r)=\frac{tr}{Q_t(r)},
\]
\[
K_t(r)=(1-r^2)\left[
\frac{(1-t)\operatorname{arctanh}(x_t(r))}{Q_t(r)^2}
+\frac{t}{Q_t(r)^3(1-x_t(r)^2)}\right].
\]
Then the exact norm, with no unspecified multiplicative constant, is
\[
\boxed{\|\mathcal H_\mu\|_{\mathcal B\to\mathcal B}
=\sup_{0\le r<1}\int_{(0,1]}K_t(r)\,d\mu(t).}
\]

For the one-atom measure \(\mu=\delta_t\), let \(N(t)=\|\mathcal H_{\delta_t}\|\) and, for \(0\le y<1\), put
\[
G_t(y)=(1-t)(1-y)(t+(2-t)y)\operatorname{arctanh}y
+\frac{(t+(1-t)y)(t+(2-t)y)}{1+y}.
\]
Set \(G_t(1)=1\) by continuity. The norm has the exact scalar maximization
\[
\boxed{N(t)=\frac1t\max_{0\le y\le1}G_t(y)}\qquad(0<t\le1).
\]
For \(0<t<1\), the maximum occurs strictly inside \((0,1)\), and
\[
\boxed{N(t)>r(\mathcal H_{\delta_t})=1/t.}
\]
At the identity parameter \(t=1\), \(N(1)=1\). The sharp small-parameter coefficient is
\[
\boxed{\lim_{t\downarrow0}tN(t)=C_*=
\max_{0\le y\le1}\left[2y(1-y)\operatorname{arctanh}y+
\frac{2y^2}{1+y}\right]>1.}
\]
Standard high-precision scalar optimization gives the illustrative decimal \(C_*\approx1.1176848412\) at \(y\approx0.9028314178\); the boxed variational expression, not the decimal, is the exact statement.

## Assumptions and scope
The measure is positive and finite; the integral \(I_\mu\) must be finite. The disk, Bloch norm, and normalization of \(\operatorname{arctanh}\) are exactly as displayed. Operator coefficients are the Hausdorff (binomial/moment) coefficients \(\binom nk\int t^k(1-t)^{n-k}d\mu(t)\). No result is asserted for signed or complex measures, different Bloch normalizations, or arbitrary weighted compositions. The zero measure yields the zero operator and is included.

## Proof
**1. Radial Bloch bounds.** Write \(a=|f(0)|\), \(b=\beta(f)\). For \(w\in\mathbb D\), integration of the derivative along the radial segment gives
\[
|f(w)|\le a+b\operatorname{arctanh}|w|,\qquad
|f'(w)|\le\frac b{1-|w|^2}.
\]
For \(g(z)=\operatorname{arctanh}z\), \(g(0)=0\) and \(g'(z)=1/(1-z^2)\); the bound \((1-|z|^2)/|1-z^2|\le1\) is sharp on the real radius. Thus \(\beta(g)=1\).

**2. Differentiation and sharp radial coefficients.** Fix \(0<t\le1\) and write \(q=1-t\), \(\phi_t(z)=tz/(1-qz)\), \(m_t(z)=1/(1-qz)\). We have \(m_t'(z)=q/(1-qz)^2\), \(\phi_t'(z)=t/(1-qz)^2\), and
\[
(\mathcal H_{\delta_t}f)'(z)=
\frac q{(1-qz)^2}f(\phi_t(z))+
\frac t{(1-qz)^3}f'(\phi_t(z)).
\]
For \(r=|z|\), \(|\phi_t(z)|\le x_t(r)\), \(|1-qz|\ge Q_t(r)\); hence
\[
(1-r^2)|(\mathcal H_{\delta_t}f)'(z)|
\le A_t(r)a+K_t(r)b,
\quad A_t(r)=\frac{(1-t)(1-r^2)}{Q_t(r)^2}.
\]
Both contributions to the expression defining \(K_t(r)\) are nonnegative. On the positive real radius \(z=r\), the upper derivative bound for \(g\) is attained exactly in both summands, so
\[
\beta(\mathcal H_{\delta_t}g)=\sup_{0\le r<1}K_t(r).
\]
For a general positive measure, integrate the derivative identity. The interchange is justified on every compact disk because \(|\phi_t(z)|\le|z|\) and the coefficients are bounded there uniformly in \(t\); finiteness of \(\mu\) suffices locally. Positivity preserves equality for \(g\) at each positive real \(r\). Thus
\[
\beta(\mathcal H_\mu f)
\le a\sup_r\int A_t(r)d\mu(t)+b\sup_r\int K_t(r)d\mu(t),
\]
while \(\beta(\mathcal H_\mu g)=\sup_r\int K_t(r)d\mu(t)\).

**3. Why the constant component cannot dominate.** For \(0<t<1\), differentiation of \(A_t\) shows its maximum occurs at \(r=1-t\), with
\[
\max_{0\le r<1}A_t(r)=\frac{1-t}{t(2-t)}.
\]
For \(t=1\), \(A_1\equiv0\). In either case
\[
1+A_t(r)\le 1+\frac{1-t}{t(2-t)}\le\frac1t,
\]
with the second inequality having difference \((1-t)^2/[t(2-t)]\). Because \((\mathcal H_\mu f)(0)=\mu((0,1])f(0)\), the norm contribution from \(a\) is at most \(I_\mu a\).

**4. Boundary layer dominates constants.** For every fixed \(t\in(0,1]\), direct substitution gives \(\lim_{r\uparrow1}K_t(r)=1/t\). The first summand tends to zero, while the second tends to \(1/t\). Consequently Fatou's lemma implies
\[
\sup_{0\le r<1}\int K_t(r)d\mu(t)\ge
\int\liminf_{r\uparrow1}K_t(r)d\mu(t)=I_\mu.
\]
The right-hand side is finite. To verify finiteness of the left-hand side explicitly, introduce \(y=x_t(r)\). The formulas in Step 5 show
\[
tK_t(r)=(1-t)(1-y)(t+(2-t)y)\operatorname{arctanh}y
+\frac{(t+(1-t)y)(t+(2-t)y)}{1+y}\le3.
\]
Here \((1-y)\operatorname{arctanh}y\le y/(1+y)\le1/2\), and the two summands are bounded by \(1\) and \(2\). Hence \(\int K_t(r)d\mu(t)\le3I_\mu\). Combining Steps 2–4,
\[
\|\mathcal H_\mu f\|_{\mathcal B}
\le I_\mu a+b\sup_r\int K_t(r)d\mu(t)
\le(a+b)\sup_r\int K_t(r)d\mu(t).
\]
Equality of the operator norm with the rightmost quantity follows from the single unit Bloch vector \(g\), proving the general assertion.

**5. Exact atomic reduction.** For a fixed \(t\), the map \(r\mapsto y=x_t(r)\) is an increasing bijection from \([0,1)\) onto itself, with inverse \(r=y/[t+(1-t)y]\). Elementary algebra gives
\[
A_t(r)=\frac{(1-t)(1-y)(t+(2-t)y)}{t},
\]
\[
\frac{t(1-r^2)}{Q_t(r)^3(1-x_t(r)^2)}
=\frac{(t+(1-t)y)(t+(2-t)y)}{t(1+y)}.
\]
These identities give \(tK_t(r)=G_t(y)\) as stated. The continuous endpoint is \(G_t(1)=1\), using \(\lim_{y\uparrow1}(1-y)\operatorname{arctanh}y=0\).

**6. Strict norm-to-spectral-radius gap.** If \(0<t<1\) and \(y=1-\varepsilon\), then the first term of \(G_t(y)\) equals
\[
(1-t)\varepsilon\bigl(2-(2-t)\varepsilon\bigr)
\operatorname{arctanh}(1-\varepsilon)
\sim(1-t)\varepsilon\log(2/\varepsilon),
\]
while its rational term equals \(1+O_t(\varepsilon)\). Therefore \(G_t(1-\varepsilon)>1\) for all sufficiently small positive \(\varepsilon\), establishing \(N(t)>1/t\) and an interior maximizer. For \(t=1\), \(G_1\equiv1\).

The weighted-composition identities yield \(\mathcal H_{\delta_s}\mathcal H_{\delta_t}=\mathcal H_{\delta_{st}}\) for \(s,t\in(0,1]\). In particular \(\mathcal H_{\delta_t}^{\,n}=\mathcal H_{\delta_{t^n}}\). By Step 7, \(uN(u)\to C_*\in(1,\infty)\) as \(u\downarrow0\). The spectral-radius formula then gives
\[
r(\mathcal H_{\delta_t})=
\lim_{n\to\infty}N(t^n)^{1/n}=1/t\qquad(0<t<1).
\]
The identity case is immediate.

**7. Sharp small-parameter limit.** The function \(h(y)=(1-y)\operatorname{arctanh}y\), extended by \(h(1)=0\), is continuous on \([0,1]\). The displayed polynomial/rational expression for \(G_t(y)\) therefore converges uniformly on \([0,1]\) as \(t\downarrow0\) to
\[
G_0(y)=2y(1-y)\operatorname{arctanh}y+\frac{2y^2}{1+y}.
\]
Uniform convergence passes through the maximum and yields \(\lim_{t\downarrow0}tN(t)=\max G_0\). For a strict analytical witness that the constant exceeds one, evaluation at \(y=9/10\) gives
\[
G_0(9/10)=\frac9{100}\log19+\frac{81}{95}>1.
\]
The formulas are exact; decimal values are secondary numerical approximations.

## Verification
Symbolic differentiation of \(A_t\) gives derivative \(2(1-t)[(1-t)-r]/[1-(1-t)r]^3\) and its maximum \((1-t)/[t(2-t)]\). A separate symbolic substitution of \(r=y/[t+(1-t)y]\) into both components of \(K_t(r)\) reproduces the two rational expressions in Step 5. Direct one-dimensional numerical maximization gives, illustratively, \(N(1/2)\approx2.1223931485\), \(N(1/10)\approx11.0673957791\), and \(C_*\approx1.1176848412\). These numeric checks do not replace the exact analytic proof. The proof handles the zero measure, the identity atom, all positive parameters, and measures with mass accumulating at zero subject to the stated moment integrability.

## Relationship to prior work
Galanopoulos–Mahillo–Oliva-Maza–Siskakis (2026), arXiv:2610.22554v1, introduce the same binomial Hausdorff family on the Bloch and BMOA spaces and study its spectrum and Fredholm essential spectrum; their integral representation is formula (1.4). The present assertion is an *operator-norm identity with a universal norming function*, which does not follow from spectral location. For the atomic subfamily, the proved strict inequality between norm and spectral radius explicitly distinguishes these invariants. Liu–Li (2015), arXiv:1511.06200v1, develop two-sided estimates for general weighted composition operators on Bloch spaces, not this exact positive-measure norm identity. Published analyses of the Hilbert *Hankel* matrix on Bloch-type spaces concern a different coefficient matrix and do not automatically imply a theorem for binomial lower-triangular Hausdorff matrices.

## Limitations
The theorem uses positivity and the exact classical Bloch normalization; cancellation for signed measures may destroy the common extremizer. The atomic strict gap is not asserted uniformly over every positive measure. No claim of a closed elementary expression for \(C_*\) or uniqueness of the scalar maximizer is made. Literature comparisons concern inspected sources and available mathematical records and do not constitute a proof of global uniqueness or independent certification. Decimal approximations are not certified interval bounds.

## References
1. P. Galanopoulos, A. Mahillo, J. Oliva-Maza, A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, arXiv:2610.22554v1, first posted 15 October 2026, https://arxiv.org/html/2610.22554v1.
2. X. Liu and S. Li, *Norm and essential norm of a weighted composition operator on the Bloch space*, arXiv:1511.06200v1, first posted 19 November 2015, https://arxiv.org/abs/1511.06200.
3. H. Hu and S. Ye, *Norm of the Hilbert matrix operator between some spaces of analytic functions*, arXiv:2410.16598, first posted 22 October 2024, https://arxiv.org/abs/2410.16598 (a different, Hankel-matrix setting).
