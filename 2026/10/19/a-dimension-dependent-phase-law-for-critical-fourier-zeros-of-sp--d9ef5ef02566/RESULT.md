# A dimension-dependent phase law for critical Fourier zeros of spherical shells

## Finding

Let \(d\ge2\) be an integer and let \(0<q<1\). The Fourier transform of the shell \(S_{d,q}=\{y\in\mathbb R^d:q<|y|<1\}\) has precisely one simple positive radial zero \(x_n(q)\) in every interval \((\alpha_n,\alpha_{n+1})\), where \(\alpha_n=j_{d/2-1,n}\) is the \(n\)-th positive zero of the Bessel function \(J_{d/2-1}\). There are no other positive radial zeros. Each trajectory \(x_n\) has exactly \(n-1\) nondegenerate stationary points, indexed by \(1\le m<n\).

Let \(X_{n,m}\) be the zero radius at the \(m\)-th critical point, \(q_{n,m}=\alpha_m/X_{n,m}\), and let
\[
U_{n,m}=\frac{X_{n,m}-\alpha_n}{\alpha_{n+1}-\alpha_n}\in(0,1).
\]
For each fixed dimension \(d\ge2\), the empirical measures \((n-1)^{-1}\sum_{m=1}^{n-1}\delta_{U_{n,m}}\) converge weakly as \(n\to\infty\) to the probability measure with density
\[
\boxed{\rho_d(u)=\frac{\pi}{d-1}\sin(\pi u)\,|\cos(\pi u)|^{(3-d)/(d-1)},\quad 0<u<1.}
\]
For \(d\ge4\) this density has an integrable power-law singularity at \(u=1/2\); for \(d=3\) it has a finite positive value there, and for \(d=2\) it vanishes there. In particular, for \(0\le\varepsilon\le1/2\),
\[
\boxed{\lim_{n\to\infty}\frac{\#\{1\le m<n:|U_{n,m}-1/2|<\varepsilon\}}{n-1}=\sin(\pi\varepsilon)^{2/(d-1)}.}
\]
In dimension \(d=3\), the Bessel critical points are exactly \(\alpha_n=n\pi\), and the limiting density simplifies to \(\rho_3(u)=\frac\pi2\sin(\pi u)\). In dimension \(d=4\), the first singular case, it is \(\rho_4(u)=\frac\pi3\sin(\pi u)|\cos(\pi u)|^{-1/3}\). These are different probability laws for the same natural geometric sampling statistic.

The corresponding critical radii satisfy \(\sup_{1\le m<n}|q_{n,m}-m/n|\to0\), so their empirical distribution is uniform on \((0,1)\).

There is also a resolved two-parity law. If \(m=m(n)\) satisfies \(m/n\to\theta\in(0,1)\) and \((-1)^{m-n}=\sigma\in\{-1,1\}\) eventually, set \(\gamma=(d-3)/4\) and
\[
s_\sigma(\theta)=\frac{1}{\pi}\arccos\left(\sigma\theta^{(d-1)/2}\right).
\]
Then
\[
\boxed{U_{n,m}\to s_\sigma(\theta),\qquad n\left(q_{n,m}-\frac mn\right)\to\gamma(1-\theta)-\theta s_\sigma(\theta).}
\]
The phase-density and parity-correction formulas are the main focus. The existence and turning-point census for \(d=2\) are already known and are not asserted to be new here.

## Assumptions and scope

The ambient dimension is an integer \(d\ge2\), Fourier convention \(\widehat f(\xi)=\int_{\mathbb R^d}f(y)e^{-i\xi\cdot y}\,dy\), and the outer shell radius is fixed to one (other outer radii reduce by scaling). Put \(\nu=d/2\) and \(f_\nu(x)=x^\nu J_\nu(x)\). The Fourier transform for radial frequency \(x>0\) equals
\[
(2\pi)^\nu x^{-d}\left(f_\nu(x)-f_\nu(qx)\right).
\]
Thus only positive-frequency zeros of this real function are counted. At frequency zero the transform is the strictly positive shell volume, not a zero. The limit \(n\to\infty\) keeps \(d\) fixed; uniformity as \(d\to\infty\) is not asserted.

## Proof

**1. Ordered and strictly growing extrema.** The standard Bessel identities give
\[
f_\nu'(x)=x^\nu J_{\nu-1}(x),\qquad f_\nu''(x)+f_\nu(x)=\frac{d-1}{x}f_\nu'(x).
\]
Consequently the energy \(E(x)=f_\nu(x)^2+f_\nu'(x)^2\) obeys
\[
E'(x)=\frac{2(d-1)}x f_\nu'(x)^2.
\]
Since \(d>1\), it is strictly increasing between any two distinct nonnegative radii, in the integral sense. The critical points \(\alpha_n\) of \(f_\nu\) are simple and alternate as maxima and minima; their absolute heights strictly increase. The function increases from zero on \((0,\alpha_1)\), and has derivative sign \((-1)^n\) on \((\alpha_n,\alpha_{n+1})\).

**2. Fourier zero count and simplicity.** Let \(F_q(x)=f_\nu(x)-f_\nu(qx)\). The energy comparison implies \(|f_\nu(q\alpha_n)|<|f_\nu(\alpha_n)|\). Thus \(F_q\) has opposite signs at consecutive \(\alpha_n\), while \(F_q(x)>0\) for \(0<x\le\alpha_1\). At any zero \(F_q(x)=0\), comparison of energies at \(x\) and \(qx\) yields
\[
|f_\nu'(x)|>|f_\nu'(qx)|.
\]
Hence \(\partial_x F_q=f_\nu'(x)-qf_\nu'(qx)\ne0\) and has the sign of \(f_\nu'(x)\). Since all root crossings within a fixed critical gap have the same strict orientation, exactly one root lies in each gap, and it is simple. The implicit-function theorem gives real-analytic trajectories.

**3. Critical-point census.** Implicit differentiation at the root gives
\[
x_n'(q)=\frac{x_n(q)f_\nu'(qx_n(q))}{f_\nu'(x_n(q))-qf_\nu'(qx_n(q))},\qquad
\frac d{dq}\bigl(qx_n(q)\bigr)=\frac{x_n(q)f_\nu'(x_n(q))}{f_\nu'(x_n(q))-qf_\nu'(qx_n(q))}>0.
\]
By comparison as \(q\downarrow0\), \(x_n(q)\to j_{\nu,n}\) and \(qx_n(q)\to0\). As \(q\uparrow1\), use \(F_q(x)/(1-q)\to xf_\nu'(x)\) on interior compact intervals and the endpoint sign orientation to obtain \(x_n(q)\to\alpha_n\), hence \(qx_n(q)\to\alpha_n\). Thus each \(qx_n(q)\) runs once through \((0,\alpha_n)\), and \(x_n'(q)=0\) exactly when \(qx_n(q)=\alpha_m\), for \(1\le m<n\). At this point \(X_{n,m}=x_n(q_{n,m})\) is the unique solution to \(f_\nu(X_{n,m})=f_\nu(\alpha_m)\) in \((\alpha_n,\alpha_{n+1})\). Differentiating again at stationarity shows
\[
x_n''(q_{n,m})=\frac{X_{n,m}^{2}f_\nu''(\alpha_m)}{f_\nu'(X_{n,m})}\ne0,\qquad \operatorname{sgn}x_n''(q_{n,m})=(-1)^{n+m}.
\]

**4. High-frequency phase asymptotics.** Fixed-order Bessel asymptotics imply, with \(a=(d-1)/2>0\) and \(\gamma=(d-3)/4\),
\[
\alpha_j=\pi(j+\gamma)+O_d(j^{-1}),\qquad
f_\nu(\alpha_j)=(-1)^{j-1}\sqrt{2/\pi}\,\alpha_j^a\bigl(1+O_d(j^{-1})\bigr).
\]
In the gap \(x=\alpha_n+u(\alpha_{n+1}-\alpha_n)\), the Bessel expansion is uniform in \(u\in[0,1]\) and gives
\[
\frac{f_\nu(x)}{f_\nu(\alpha_n)}=\cos(\pi u)+O_d(n^{-1}).
\]
For \(m/n\to\theta\in(0,1)\), the critical equation \(f_\nu(X_{n,m})=f_\nu(\alpha_m)\) therefore gives
\[
\cos(\pi U_{n,m})\to (-1)^{m-n}\theta^a.
\]
The cosine is strictly decreasing on \([0,\pi]\); this proves the parity-resolved limit. Also \(q_{n,m}=\alpha_m/X_{n,m}\). Substituting the zero asymptotics and \(X_{n,m}=\pi(n+\gamma+U_{n,m})+o(1)\) yields
\[
n\left(q_{n,m}-\frac mn\right)\to\gamma(1-\theta)-\theta s_\sigma(\theta).
\]
The bounds \(\alpha_m/\alpha_{n+1}<q_{n,m}<\alpha_m/\alpha_n\) imply \(q_{n,m}=m/n+O_d(1/n)\) uniformly over \(1\le m<n\) (with finite small-index exceptions absorbed into the constant).

**5. Distribution and the cusp transition.** Split indices \(m\) by parity relative to \(n\). Within either parity, \(m/n\) tends to the uniform measure on \((0,1)\), and the two parities each occupy asymptotic weight \(1/2\). On any closed \(\theta\)-range away from zero and one, the preceding phase limit is uniform, and the excluded endpoints contain arbitrarily small proportions, proving weak convergence. Thus the limiting law is the equal mixture of the pushforwards \(\theta\mapsto\pi^{-1}\arccos(\theta^a)\) and \(\theta\mapsto\pi^{-1}\arccos(-\theta^a)\). Change of variables gives
\[
\rho_d(u)=\frac\pi{2a}\sin(\pi u)|\cos(\pi u)|^{1/a-1},
\]
which simplifies to the announced formula. Its integral over \((0,1)\) is one. The event \(|u-1/2|<\varepsilon\) corresponds to \(0<\theta<\sin(\pi\varepsilon)^{1/a}\), proving the exact limiting central-window proportion. The exponent at the midpoint is \((3-d)/(d-1)>-1\), so the dimension-four-and-higher cusp is integrable.

## Verification

The self-contained reproducibility files `checks/shell_phase_check.py` and `checks/shell_phase_distribution.py` use Python, NumPy, and SciPy. Run these from the directory containing `checks` with `python checks/shell_phase_check.py` and `python checks/shell_phase_distribution.py` after making `checks` importable through `PYTHONPATH=checks`. The first checks 40 different combinations of dimension and indices against exact defining Bessel equations and parity-offset predictions. The second solves all \(399\) critical phase equations at \(n=400\), for each dimension \(2,3,4,5,6\), and compares three central-window frequencies per dimension with the limiting formula. An additional checker, `checks/shell_transform_3d.py`, independently compares the three-dimensional Fourier shell integral with the Bessel normalization for 32 cases. The tests corroborate numerical behavior only; they do not establish the infinite-dimensional-in-index limits. Those are proved in the preceding steps using uniform fixed-order Bessel asymptotics.

## Relationship to prior work

Pálmai and Apagyi's full-text Bessel zero interlacing results are used for standard facts about Bessel zeros, not for the Fourier-shell phase law. Grafakos and Teschl establish the radial Fourier transform and dimension-raising relation; Adkins develops three-dimensional spherical-Bessel Fourier integral identities. Ziener and coauthors' shell Bessel cross-products describe boundary-value eigenvalue problems, rather than the transform difference \(f_\nu(x)-f_\nu(qx)\). Earlier analysis already determined the planar shell's \(n-1\) critical points; that part is background here. The principal claim not implied by the identified prior statements is the all-dimension high-order two-parity phase law and the density with its threshold cusp behavior at dimension four.

## Limitations

The phase results take the zero index to infinity at each *fixed* dimension; no uniform high-dimensional limit or distribution for varying shell thickness is asserted. The theorem concerns the indicator of a perfectly concentric shell, not arbitrary radial densities or nonconcentric shells. The planar stationary-point census is preexisting. The originality comparison cannot rule out equivalent formulas hidden in early optical diffraction literature: Weick's 1974 spherical-shell paper was identifiable but not fully accessible for comparison. Publication priority requires further independent checking; no independent mathematical audit is claimed.

## References

1. T. Pálmai and B. Apagyi, “Interlacing of positive real zeros of Bessel functions,” arXiv:1002.0976, first posted February 4, 2010, https://arxiv.org/pdf/1002.0976 .
2. L. Grafakos and G. Teschl, “On Fourier transforms of radial functions and distributions,” arXiv:1112.5469, first posted December 22, 2011, https://arxiv.org/abs/1112.5469 .
3. G. S. Adkins, “Three-dimensional Fourier transforms, integrals of spherical Bessel functions, and novel delta function identities,” arXiv:1302.1830, first posted February 7, 2013, https://arxiv.org/abs/1302.1830 .
4. T. Ziener, G. Kurz, M. Buschle, and T. Kampf, “Orthogonality, Lommel integrals and cross product zeros of linear combinations of Bessel functions,” SpringerPlus 4 (2015), article 390, https://doi.org/10.1186/s40064-015-1142-0 .
5. NIST Digital Library of Mathematical Functions, §10.17 and §10.21 (fixed-order asymptotics and zero locations), https://dlmf.nist.gov/10.17 and https://dlmf.nist.gov/10.21 .
