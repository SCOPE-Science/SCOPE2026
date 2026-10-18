# Exact turning-point census for Fourier zeros of planar circular annuli

## Finding

Let \(A_q=\{u\in\mathbb R^2:q<|u|<1\}\) for \(0<q<1\), and use the Euclidean Fourier convention \(\widehat f(\xi)=\int_{\mathbb R^2}f(u)e^{-i u\cdot\xi}\,du\). Write \(j_{\nu,n}\) for the \(n\)-th positive zero of the ordinary Bessel function \(J_\nu\), and put \(j_{0,0}=0\). The radial Fourier transform has the explicit form

\[
\widehat {\mathbf 1}_{A_q}(\xi)=\frac{2\pi}{|\xi|}\bigl[J_1(|\xi|)-qJ_1(q|\xi|)\bigr]\qquad(|\xi|>0).
\]

For every integer \(n\ge1\) and every \(q\in(0,1)\), there is exactly one positive real Fourier-zero radius \(x_n(q)\) in \((j_{0,n},j_{0,n+1})\); these are **all** positive real Fourier-zero radii, and they are all simple zeros in the radial variable. Each function \(x_n\) is real analytic on \((0,1)\). Its endpoint limits are

\[
\lim_{q\downarrow0}x_n(q)=j_{1,n},\qquad
\lim_{q\uparrow1}x_n(q)=j_{0,n}.
\]

The number of stationary points of the \(n\)-th zero-radius trajectory \(q\mapsto x_n(q)\) is **exactly \(n-1\)**. More precisely, for each integer \(1\le m<n\), there is a unique

\[
X_{n,m}\in(j_{0,n},j_{0,n+1})\quad\text{such that}\quad
X_{n,m}J_1(X_{n,m})=j_{0,m}J_1(j_{0,m}).
\]

The stationary parameters are precisely

\[
q_{n,m}=\frac{j_{0,m}}{X_{n,m}},\qquad
0<q_{n,1}<\cdots<q_{n,n-1}<1,
\]

and each stationary point is nondegenerate, with

\[
x_n''(q_{n,m})=-\frac{q_{n,m}X_{n,m}^{2}J_1(j_{0,m})}{J_0(X_{n,m})}\ne0,
\qquad \operatorname{sgn}x_n''(q_{n,m})=(-1)^{n+m}.
\]

Thus the first dark-ring radius decreases strictly as the inner hole enlarges, whereas the \(n\)-th radius has an alternating sequence of exactly \(n-1\) maxima and minima. The second ring, for example, has its unique maximum at \(q_{2,1}\approx0.315585469\), where \(x_2\approx7.620203696\).

For every fixed \(n\), the endpoint expansions sharpen the above limits:

\[
 x_n(q)=j_{1,n}+\frac{j_{1,n}}{2J_0(j_{1,n})}q^2+O_n(q^4)
 \quad(q\downarrow0),
\]
\[
 x_n(q)=j_{0,n}\left(1+\frac{1-q}{2}\right)+O_n((1-q)^2)
 \quad(q\uparrow1).
\]

## Assumptions and scope

The outer annulus radius is normalized to \(1\), the hole ratio is strictly \(0<q<1\), Fourier frequencies are real, and only positive radial zeros are counted. Changing the physical outer radius simply rescales frequency. The Fourier value at zero is the positive annular area \(\pi(1-q^2)\), so it is never a zero. The statements concern Fourier zeros of the *indicator of an annulus*, not Dirichlet or Neumann eigenfrequencies for a Laplacian on the annulus. No claim about the complex zeros of the Bessel combination is made.

## Proof

**1. Radial reduction and a strict Bessel energy.** Radial polar integration and \((xJ_1(x))'=xJ_0(x)\) give, for \(x>0\),

\[
G_q(x):=J_1(x)-qJ_1(qx)=x\int_q^1 tJ_0(tx)\,dt.
\]

The standard recurrences \(J_0'=-J_1\) and \(J_1'=J_0-J_1/x\) imply

\[
E(x):=x^2(J_0(x)^2+J_1(x)^2),\qquad E'(x)=2xJ_0(x)^2.
\]

Hence \(E\) is **strictly increasing** for \(x>0\): its derivative is nonnegative and cannot vanish identically on any nonempty interval. At any positive root \(G_q(x)=0\), the relation \(J_1(x)=qJ_1(qx)\) and \(E(x)>E(qx)\) yield the strict inequality

\[
|J_0(x)|>q|J_0(qx)|.
\tag{1}
\]

Differentiation of \(G_q\) with respect to \(x\), followed by the root identity, gives

\[
\partial_xG_q(x)=J_0(x)-q^2J_0(qx)
\quad\text{when }G_q(x)=0.
\tag{2}
\]

By (1), the right side is nonzero and has exactly the sign of \(J_0(x)\). In particular every positive root is simple, and no root lies at any \(j_{0,n}\).

**2. One root in every Bessel gap, and no others.** At \(x=j_{0,n}\), strict energy growth gives

\[
|J_1(j_{0,n})|>q|J_1(qj_{0,n})|.
\]

Thus \(G_q(j_{0,n})\) has the sign of \(J_1(j_{0,n})\), alternating with \(n\). The intermediate-value theorem produces a root in every \((j_{0,n},j_{0,n+1})\). On a fixed gap the sign of \(J_0\) is constant, so (2) shows that **all** simple root crossings have the same orientation. Two distinct such roots cannot exist: between crossings of identical orientation an opposite-orientation crossing would be necessary. Finally, \(G_q(x)=x\int_q^1tJ_0(tx)\,dt>0\) for \(0<x\le j_{0,1}\). This gives exactly the claimed enumeration and excludes other positive real roots. Analyticity follows by the implicit-function theorem using (2).

**3. The inner sampled radius is strictly increasing.** A direct differentiation of \(G_q\) gives

\[
\partial_qG_q(x)=-qxJ_0(qx).
\]

Consequently, writing \(D_n(q)=J_0(x_n(q))-q^2J_0(qx_n(q))\),

\[
x_n'(q)=\frac{q x_n(q)J_0(qx_n(q))}{D_n(q)},
\qquad
\frac{d}{dq}(qx_n(q))=\frac{x_n(q)J_0(x_n(q))}{D_n(q)}>0.
\tag{3}
\]

Strict positivity in (3) follows from the sign and nonvanishing given by (1). In particular, \(y_n(q)=qx_n(q)\) increases strictly.

For \(q\downarrow0\), \(G_q\) converges locally uniformly to \(J_1\), and the unique root of \(J_1\) in the \(n\)-th \(J_0\) gap is \(j_{1,n}\) by classical Bessel interlacing. Hence \(y_n(q)\to0\). For \(q\uparrow1\), uniformly on bounded intervals,

\[
\frac{G_q(x)}{1-q}=
\frac{x}{1-q}\int_q^1tJ_0(tx)\,dt\longrightarrow xJ_0(x).
\]

The only root of the limiting function in the closure of the \(n\)-th gap is \(j_{0,n}\) (its right endpoint \(j_{0,n+1}\) is also a zero, but the sign of \(G_q\) at that endpoint and the positive root orientation exclude convergence to it). Alternatively, the implicit-function theorem at \((q,x)=(1,j_{0,n})\) applied to \(G_q(x)/(1-q)\) constructs the unique nearby root on the right of \(j_{0,n}\), forcing the globally unique root to coincide with that branch. Thus \(y_n(q)\to j_{0,n}\).

**4. Exactly \(n-1\) turning points.** The denominator \(D_n\) in (3) never vanishes. Therefore \(x_n'(q)=0\) precisely when \(J_0(y_n(q))=0\). Since \(y_n\) is a strictly increasing bijection from \((0,1)\) onto \((0,j_{0,n})\), it crosses exactly the values \(j_{0,1},\ldots,j_{0,n-1}\), and crosses each once. At its crossing of \(j_{0,m}\), the equation \(G_q(x)=0\), with \(q=j_{0,m}/x\), is exactly

\[
xJ_1(x)=j_{0,m}J_1(j_{0,m}).
\]

Put \(h(x)=xJ_1(x)\); then \(h'(x)=xJ_0(x)\), so \(h\) is strictly monotone on each \(J_0\) gap. At the endpoints, \(h(j_{0,k})\) alternates sign and has strictly increasing absolute value, by \(E'(x)\ge0\) and \(h(j_{0,k})^2=E(j_{0,k})\). Hence for \(m<n\), the right-hand side lies strictly between \(h(j_{0,n})\) and \(h(j_{0,n+1})\), giving the asserted unique solution \(X_{n,m}\). The strict order of the \(q_{n,m}\) follows from monotonicity of \(y_n\), not from monotonicity of the unsorted \(X_{n,m}\).

At a turning point, \(D_n=J_0(X_{n,m})\) and \(y_n'=X_{n,m}\). Differentiating the first identity of (3) once more produces

\[
x_n''(q_{n,m})=
\frac{q_{n,m}X_{n,m}J_0'(j_{0,m})X_{n,m}}{J_0(X_{n,m})}
=-\frac{q_{n,m}X_{n,m}^2J_1(j_{0,m})}{J_0(X_{n,m})}.
\]

Interlacing ensures the numerator is nonzero; the alternating Bessel signs yield the stated sign \((-1)^{n+m}\). In particular all extrema are nondegenerate, and \(x_n'\) is strictly negative near \(q=1\).

**5. Endpoint expansions.** Near \(q=0\), the Taylor series \(qJ_1(qx)=q^2x/2+O(q^4)\) and the nonzero derivative \(J_1'(j_{1,n})=J_0(j_{1,n})\) yield the first expansion. For \(h=1-q\downarrow0\), the averaged integral has the uniform expansion

\[
\frac{G_{1-h}(x)}h=x\left[J_0(x)-\frac h2\bigl(J_0(x)+xJ_0'(x)\bigr)+O(h^2)\right].
\]

Solving near the simple zero \(j_{0,n}\) gives the second expansion. This completes the theorem.

## Verification

The standalone file `check_annular_zeros.py` evaluates ordinary Bessel functions and uses bracketed Brent root finding. It tests \(84\) roots from the first twelve gaps at seven annulus ratios; all \(66\) stationary pairs \((n,m)\) with \(2\le n\le12\); and \(24\) endpoint convergence cases. It checks the Bessel equation residuals, strict interval inclusions, monotonicity of \(qx_n(q)\), nondegenerate alternating curvature and critical-parameter ordering. Run with `python check_annular_zeros.py` after installing NumPy and SciPy. The finite-precision check is a reproducibility aid; it is not a proof of the quantified all-order result.

## Relationship to prior work

Classical Bessel interlacing provides the limit \(j_{0,n}<j_{1,n}<j_{0,n+1}\); see Pálmai and Apagyi (2010) and DLMF §10.21. The optical literature, including Khonina (2013), discusses the filled-pupil first dark-ring radius and the thin-annulus \(J_0\) limit. Guo, Müller, Wang and Wang (2019) study **different** zeros \(J_\nu(Rx)Y_\nu(rx)-J_\nu(rx)Y_\nu(Rx)\), relevant to annular Laplacian eigenvalues rather than to the Fourier transform of an annulus indicator. None of those identified statements gives the interior-radius derivative in (3), the all-ring gap uniqueness, or the exact \(n-1\) critical-point census. The present argument uses the strict Bessel energy identity as an elementary mechanism specific to \(J_1(x)-qJ_1(qx)\). Equivalent results could be indexed under annular point-spread functions or special-function difference zeros, and absence from searched sources is not a proof of publication priority.

## Limitations

The conclusions apply to a uniformly illuminated circular annulus in the scalar two-dimensional Fourier model. They do not classify complex-frequency zeros, aberrated apertures, vector electromagnetic focusing, nonradial masks, or zero motion when both physical radii vary independently. Exact turning-point locations are defined implicitly, with numerical approximations supplied only as illustrations. The originality comparison cannot exclude equivalences in unindexed older optical or Bessel-function literature. No independent audit has been performed.

## References

1. T. Pálmai and B. Apagyi, *Interlacing of positive real zeros of Bessel functions*, first posted 2010-02-04, arXiv:1002.0976v1, https://arxiv.org/abs/1002.0976.
2. NIST Digital Library of Mathematical Functions, §10.21, *Zeros*, https://dlmf.nist.gov/10.21.
3. S. N. Khonina, *Minimizing the Bright/Shadow Focal Spot Size with Controlled Side-Lobe Increase in High-Numerical-Aperture Focusing Systems*, *Advances in Optical Technologies* (2013), DOI:10.1155/2013/267684, https://doi.org/10.1155/2013/267684.
4. J. Guo, W. Müller, W. Wang, and Z. Wang, *The Weyl formula for planar annuli*, 2019 preprint, arXiv:1907.03669, https://arxiv.org/abs/1907.03669.
