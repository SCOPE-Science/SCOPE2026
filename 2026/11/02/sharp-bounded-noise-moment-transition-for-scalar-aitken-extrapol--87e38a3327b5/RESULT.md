# Sharp bounded-noise moment transition for scalar Aitken extrapolation

## Finding

A scalar fixed-point contraction with two **independently and uniformly bounded** evaluation errors has a sharp, nonzero noise-amplitude boundary for the unregularized three-term Aitken \(\Delta^2\) extrapolate. Below the boundary every absolute moment exists; at the boundary the extrapolate has a \(t^{-2}\) tail and finite mean but infinite variance; above the boundary it has a \(t^{-1}\) tail and no finite first absolute moment. Both tail coefficients and the logarithmic divergence of mean-square error as the boundary is approached from below are explicit.

For \(0<\rho<1\), \(s>0\), \(\eta>0\), define
\[
 x_0=s,\quad x_1=\rho x_0+\varepsilon_0,\quad
 x_2=\rho x_1+\varepsilon_1,\qquad
 \varepsilon_0,\varepsilon_1\overset{\rm iid}{\sim}\operatorname{Unif}[-\eta,\eta].
\]
The fixed point is zero. The unregularized Aitken estimate is
\[
 Z=x_0-\frac{(x_1-x_0)^2}{x_2-2x_1+x_0},
\]
with a probability-zero pole assigned any arbitrary value. Set
\[
 c=1-\rho,\quad a=2-\rho,\quad d=c^2s,\quad
 \eta_c=\frac{c^2s}{a+1}=\frac{(1-\rho)^2s}{3-\rho}.
\]

**Exact moment trichotomy.** For every real \(p>0\),
\[
\begin{array}{c|c|c}
 \text{noise range}&\Pr(|Z|>t)\text{ as }t\to\infty& \mathbb E|Z|^p<\infty\text{ iff}\\\hline
 0<\eta<\eta_c&\text{compact support}& p>0\\
 \eta=\eta_c&K t^{-2}(1+o(1))&0<p<2\\
 \eta>\eta_c&T_\eta t^{-1}(1+o(1))&0<p<1
\end{array}
\]
where
\[
 K=\frac{2s^2}{(2-\rho)(3-\rho)^2},\qquad
 L=\max\left\{-\eta,\frac{d-\eta}a\right\},\quad
 U=\min\left\{\eta,\frac{d+\eta}a\right\},\quad
 T_\eta=\frac1{2\eta^2}\int_L^U(cs-u)^2\,du>0.
\]
At the threshold, \(Z\) has a finite first absolute moment but infinite mean-square error; above it, the expectation does not exist absolutely.

**Approach from the safe side.** As \(\eta\uparrow\eta_c\) through \(0<\eta<\eta_c\),
\[
\boxed{\mathbb EZ^2=
 \frac{4s^2}{(2-\rho)(3-\rho)^2}
 \log\frac{\eta_c}{\eta_c-\eta}+O(1).}
\]
The \(O(1)\) bound is for fixed \(\rho\) and \(s\); no uniformity as either parameter varies is claimed.

## Assumptions and scope

The only randomness comes from the two independent errors, each exactly uniform on the same interval; they are independent of the deterministic initial state. The contraction coefficient is real and lies strictly between zero and one. The sample uses a *successive noisy Picard trace*: the second evaluation takes the first noisy output as its input. The conclusions concern the single Aitken transform of these three trace values, not a repeated or restarted algorithm, and assume no denominator clipping or regularization.

## Proof

**1. Reduction and the safe regime.** Direct expansion of the noisy iterates yields
\[
 D:=x_2-2x_1+x_0=d-a\varepsilon_0+\varepsilon_1,
 \qquad W:=(x_1-x_0)^2=(cs-\varepsilon_0)^2,
 \qquad Z=s-\frac WD.
\]
Since the errors have a joint density, \(\Pr(D=0)=0\). The minimum of \(D\) over the full error square is \(d-(a+1)\eta\). When \(\eta<\eta_c\) it is strictly positive, so the continuous expression for \(Z\) is bounded throughout the compact square.

**2. Exact critical tail.** At \(\eta=\eta_c\), the sole zero of \(D\) on the square is \((\varepsilon_0,\varepsilon_1)=(\eta_c,-\eta_c)\). Write \(u=\eta_c-\varepsilon_0\) and \(v=\varepsilon_1+\eta_c\). Both are nonnegative and
\[
 D=au+v,\quad W=(b+u)^2,\quad
 b=cs-\eta_c=\frac{2cs}{3-\rho}>0.
\]
For \(t>s\), the event \(|Z|>t\) is exactly \(D<W/(t+s)\). Rescale \((u,v)=(\xi,\zeta)/(t+s)\). The rescaled domain converges to the triangle \(\xi,\zeta\ge0\), \(a\xi+\zeta<b^2\). Its area equals \(b^4/(2a)\). More precisely, for all large \(t\), the rescaled domain is uniformly bounded and has uniformly convergent boundary functions, so dominated convergence applies. With constant joint density \(1/(4\eta_c^2)\),
\[
 \lim_{t\to\infty}t^2\Pr(|Z|>t)
 =\frac{b^4}{8a\eta_c^2}
 =\frac{2s^2}{(2-\rho)(3-\rho)^2}=K.
\]
The strictly positive corner numerator is essential: the pole sits on a two-dimensional corner rather than a line across positive area.

**3. Supercritical tail.** At \(\eta>\eta_c\), the zero set \(D=0\) is the line \(\varepsilon_1=a\varepsilon_0-d\). Its projection on the first error coordinate has strictly positive length \([L,U]\). Fix \(x=\varepsilon_0\) in the relative interior of that interval. A conditional error interval of width \(W(x)/(t+s)\) immediately above the zero line gives \(Z<-t\); the interval of width \(W(x)/(t-s)\) below it gives \(Z>t\) for \(t>s\). Multiplying by the square's density, the sum has first-order width \(2W(x)/t\). Boundary truncation affects only a vanishing set of first-coordinate values. The conditional widths are at most \(2\sup W/(t-s)\), so dominated convergence gives
\[
 \lim_{t\to\infty}t\Pr(|Z|>t)
 =\frac1{2\eta^2}\int_L^U(cs-x)^2\,dx=T_\eta.
\]
The integrand cannot vanish on any interval of positive length, and hence the coefficient is strictly positive for all \(\eta>\eta_c\). Applying \(\mathbb E|Z|^p=p\int_0^\infty t^{p-1}\Pr(|Z|>t)\,dt\) establishes all moment cutoffs.

**4. Logarithmic risk boundary.** For \(\eta<\eta_c\), put \(\tau=d-(a+1)\eta>0\), \(u=\eta-\varepsilon_0\), \(v=\varepsilon_1+\eta\). Now \(D=\tau+au+v\) and \(W=(cs-\eta+u)^2\). In the expansion
\[
 \mathbb EZ^2=s^2-2s\mathbb E\frac WD+\mathbb E\frac{W^2}{D^2},
\]
the middle expectation remains bounded as \(\tau\downarrow0\), because the reciprocal of a nonnegative affine form is integrable on a two-dimensional quadrant. Put \(b_\eta=cs-\eta\). Since \((b_\eta+u)^4-b_\eta^4=O(u)\) uniformly for \(\eta\) near \(\eta_c\), the corresponding correction to the final expectation is bounded by the integrability of \(u/(au+v)^2\). The leading integral is therefore
\[
 \frac{b_\eta^4}{4\eta^2}
 \int_0^{2\eta}\int_0^{2\eta}
 \frac{dv\,du}{(\tau+au+v)^2}+O(1).
\]
The double integral is exactly
\[
 \frac1a\log\frac{(\tau+2a\eta)(\tau+2\eta)}{\tau(\tau+2(a+1)\eta)}.
\]
Replacing its prefactor by the limiting value \(b^4/(4a\eta_c^2)\) changes the expression by only \(O(1)\). Because \(\tau=(a+1)(\eta_c-\eta)\), the required logarithmic asymptotic follows with coefficient \(b^4/(4a\eta_c^2)=4s^2/[a(3-\rho)^2]=2K\).

## Verification

The standalone standard-library script `verification/verify_aitken.py` checks 32,008 deterministic algebraic and numerical assertions with a fixed seed. It reconstructs the denominator and numerator from the two successive noisy evaluations using exact rational arithmetic, verifies the coefficient formulas, integrates the conditional tail independently for the supercritical example, and numerically checks the exact critical tail and subcritical logarithmic slope. These finite diagnostics do **not** establish the infinite-tail or all-parameter theorems; those follow from the four analytic proof steps.

For a reproducible rational example, take \(\rho=1/2\), \(s=1\). Then \(\eta_c=1/10\), critical tail coefficient \(K=16/75\), and subcritical squared-risk logarithm coefficient \(32/75\). At \(\eta=1/5\), \(L=1/30\), \(U=1/5\), and \(T_\eta=403/1296\). Run `python3 verification/verify_aitken.py` from the directory containing this file.

## Relationship to prior work

Aitken's \(\Delta^2\) transform is classical; Pomeranz (2017) analyzes a deterministic extension and properties of sequence acceleration. The theorem here is not a new transform. Lupo Pasini and Laiu (2022) analyze approximate Anderson acceleration for fixed-point problems, controlling accuracy sufficiently to preserve convergence; their analysis does not directly supply the sharp uniform-noise moment phase diagram or the critical constants above. Toth and collaborators (2017) study Anderson acceleration with inaccurate function evaluations and are a particularly relevant potential antecedent, but their full text could not be inspected; no assertion of full-document noncoverage is made. Pollock and Rebholz (2022) consider least-squares filtering against instability, a related motivation with a different question. The novelty claim is restricted to this particular distributional threshold and its constants.

## Limitations

The result assumes exactly two independent uniform additive perturbations of a scalar affine contraction, and applies to the unregularized one-shot transform only. Other bounded distributions can have different local densities and corner exponents; no universal bounded-noise theorem is asserted. The main risk for originality is specialized literature on noisy Aitken/Anderson extrapolation and the inaccessible complete Toth et al. analysis. No claim is made for finite-precision division, guard rules, correlated errors, higher-dimensional maps, or downstream iterative convergence.

## References

1. S. B. Pomeranz, "Aitken's \(\Delta^2\) method extended," *Cogent Mathematics* (2017), DOI: 10.1080/23311835.2017.1308622; earliest verified public posting 2017-03-20.
2. M. Lupo Pasini and M. P. Laiu, "Anderson acceleration with approximate calculations: applications to scientific computing," arXiv:2206.03915 (first posted 2022-06-08), https://arxiv.org/abs/2206.03915.
3. A. Toth et al., "Local improvement results for Anderson acceleration with inaccurate function evaluations," *SIAM Journal on Scientific Computing* (2017), DOI: 10.1137/16M1080677; complete text not verified here.
4. S. Pollock and L. G. Rebholz, "Filtering for Anderson acceleration," arXiv:2211.12953 (first posted 2022-11-23), https://arxiv.org/abs/2211.12953.
