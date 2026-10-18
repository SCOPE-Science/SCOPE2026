# A sharp dimension-dependent log-concavity threshold for two-scale Gaussian mixtures

## Finding

Let \(d\ge1\) be an integer, let \(0<\sigma<\tau\), and let \(0<w<1\). For \(x\in\mathbb R^d\), define
\[
 f_d(x)=(1-w)(2\pi\tau^2)^{-d/2}e^{-\|x\|^2/(2\tau^2)}
       +w(2\pi\sigma^2)^{-d/2}e^{-\|x\|^2/(2\sigma^2)}.
\]
Put
\[
 Q=\frac{\tau}{\sigma}>1,\qquad
 q=\frac{\sigma^2}{\tau^2-\sigma^2}>0,\qquad
 h=\sqrt{1+q(q+1)},\qquad
 R(q)=\frac{q}{1+h}\exp\!\left(q+h+\frac12\right).
\]
Then the following is an exact necessary-and-sufficient condition, including the boundary:
\[
 \boxed{f_d\text{ is log-concave on }\mathbb R^d
 \quad\Longleftrightarrow\quad
 \frac{w}{1-w}Q^d\le R(q).}
\]
Equivalently, the sharp critical narrow-component mass is
\[
 \boxed{w_d=\frac{R(q)}{R(q)+Q^d}.}
\]
For \(w<w_d\) the negative log-density is **uniformly strongly convex**. At \(w=w_d\) its least radial Hessian eigenvalue vanishes on one sphere. For \(w>w_d\) the logarithmic Hessian has exactly one positive radial-eigenvalue shell; its remaining \(d-1\) tangential eigenvalues are negative everywhere. The density is strictly radially decreasing away from zero in all cases, so loss of log-concavity does not require multiple modes.

The threshold decreases strictly with dimension. In particular,
\[
 f_4=\frac9{10}\,\mathcal N(0,4I_4)+\frac1{10}\,\mathcal N(0,I_4)
\]
(as a density) is **not** log-concave, although the density of **every** rank-three linear projection of this four-dimensional law is log-concave. More generally, for any fixed \(Q>1\) and any integer \(d\ge2\), some interior weight produces a non-log-concave \(d\)-dimensional mixture for which every projection to fewer than \(d\) dimensions has a log-concave density.

## Assumptions and scope

All Gaussian covariance matrices above are positive scalar multiples of the identity; the two means coincide at zero. The Gaussian mixtures are probability densities with respect to Lebesgue measure. The weight \(w\) belongs to the **smaller-variance** component. Log-concavity means concavity of \(\log f_d\) on all of \(\mathbb R^d\); uniform strong log-concavity means \(-\nabla^2\log f_d\succeq cI_d\) for some \(c>0\). A rank-\(k\) linear projection means the pushforward under any surjective linear map \(\mathbb R^d\to\mathbb R^k\), \(1\le k<d\). Pure component limits and equal scales are Gaussian and log-concave; they are not part of the nondegenerate parameter domain of the criterion.

## Proof

**1. Exact Hessian.** Write \(\alpha=\tau^{-2}\), \(\beta=\sigma^{-2}\), \(\delta=\beta-\alpha>0\), and
\[
 r=\frac{w}{1-w}\left(\frac\tau\sigma\right)^d,\qquad
 t=t(x)=r\exp(-\delta\|x\|^2/2).
\]
The density is a positive constant times \(e^{-\alpha\|x\|^2/2}(1+t)\). Direct differentiation gives
\[
 u(t)=\frac{\alpha+\beta t}{1+t}>0,\qquad
 \nabla\log f_d(x)=-u(t)x,
\]
\[
 \boxed{\nabla^2\log f_d(x)
 =-u(t)I_d+\frac{\delta^2t}{(1+t)^2}xx^{\mathsf T}.}
\]
For \(x\ne0\), the \(d-1\) tangential eigenvalues equal \(-u(t)<0\). The radial eigenvalue is
\[
 H(t)=-\frac{\alpha+\beta t}{1+t}
 +\frac{2\delta t}{(1+t)^2}\log\frac rt,
 \qquad 0<t<r.
\]
At \(x=0\) the Hessian is \(-u(r)I_d\), strictly negative definite. As \(\|x\|\to\infty\), it tends to \(-\alpha I_d\).

**2. The sharp scalar minimization.** Since \(q=\alpha/\delta\), multiplication by the positive factor \((1+t)^2/(2\delta t)\) shows
\[
 H(t)>0\quad\Longleftrightarrow\quad
 \log r>F_q(t),
\]
where
\[
 F_q(t)=\log t+\frac12\left(\frac qt+2q+1+(q+1)t\right),\qquad t>0.
\]
Its derivative is
\[
 F_q'(t)=\frac{(q+1)t^2+2t-q}{2t^2}.
\]
The numerator has exactly one positive zero
\[
 t_* =\frac{\sqrt{1+q(q+1)}-1}{q+1}=\frac q{1+h}.
\]
Thus \(F_q\) strictly decreases to \(t_*\) and strictly increases afterwards; it diverges at both endpoints of \((0,\infty)\). Using \(q/t_*=1+h\) and \((q+1)t_*=h-1\), its minimum is
\[
 F_q(t_*)=\log t_*+q+h+\frac12=\log R(q).
\]
If \(r\le R(q)\), then \(\log r\le\min_{t>0}F_q(t)\), so all Hessian eigenvalues are nonpositive. If \(r>R(q)\), then \(r>t_*\), and at the accessible radius satisfying \(t(x)=t_*\), the radial eigenvalue is positive. This proves both directions and the exact weight threshold.

**3. Equality, shell, and strong convexity.** At \(r=R(q)\), the only Hessian degeneracy is radial, at radius
\[
 \rho_*^2=\frac2\delta\left(q+h+\frac12\right).
\]
When \(r>R(q)\), the equation \(F_q(t)=\log r\) has exactly two roots \(0<t_-<t_*<t_+<r\) (note that \(F_q(r)>\log r\)). The radial eigenvalue is positive exactly when
\[
 \frac2\delta\log\frac r{t_+}<\|x\|^2
 <\frac2\delta\log\frac r{t_-}.
\]
Below threshold the Hessian is negative definite at every point. Its eigenvalues depend continuously on radius, and approach \(-\alpha\) as radius tends to infinity, so the negative Hessian admits a uniform positive lower bound. Finally, \(\partial_{\rho}\log f_d=-\rho u(t)<0\) for every \(\rho>0\), proving strict radial decrease even above threshold.

**4. Dimension effect and a four-dimensional certificate.** Every rank-\(k\) image of the original mixture has conditional covariances \(\tau^2AA^{\mathsf T}\) and \(\sigma^2AA^{\mathsf T}\). Whitening gives an invertible affine image of the same isotropic two-scale mixture in dimension \(k\), with the same \(w,\sigma,\tau\). Therefore its exact condition is \(w\le R(q)/(R(q)+Q^k)\). Since \(Q>1\), these critical weights strictly decrease with \(k\). Choosing
\[
 w=\frac{R(q)}{R(q)+Q^{d-1/2}}
\]
places all dimensions at most \(d-1\) below threshold and dimension \(d\) strictly above it.

For the rational-weight example, take \(\sigma=1\), \(\tau=2\), and \(w=1/10\). Then \(q=1/3\), \(h=\sqrt{13}/3\), and \(r_k=2^k/9\). An elementary certified bracket is
\[
 1<R(1/3)<15/11.
\]
Indeed \(6/5<h<5/4\), so \(4/27<t_*<5/33\), while \(2<q+h+1/2<25/12<13/6\). The elementary exponential bounds \(7<e^2<15/2\) and \(e^{1/6}<6/5\) yield
\[
 \frac{28}{27}<R(1/3)<\frac5{33}\frac{15}{2}\frac65=\frac{15}{11}.
\]
For example \(e^2<15/2\) follows by summing terms \(0\) through \(6\) of its exponential series and bounding the positive remainder by a geometric series (the first ratio is at most \(1/4\)); the other exponential estimates follow from the same series and \(e^x<1/(1-x)\) for \(0<x<1\). Consequently \(r_3=8/9<R(1/3)<r_4=16/9\). This proves the announced four-dimensional counterexample without relying on decimal approximations.

## Verification

Run `python3 verify.py` using Python's standard library. The program checks the rational derivative identity at 390 parameter pairs, exact rational Taylor certificates for the exponential bracket, and direct two-exponential quotient differentiation against the Hessian identity over multiple dimensions, weights, and radii. It also checks the sharp witness and the four-versus-three-dimensional example. The run supplied with this result passed 3,042 checks. These tests are supplementary; the universal equivalence, eigenvalue analysis, strictness, and projection statements follow from the analytic proof above.

## Relationship to prior work

Eskenazis, Nayar and Tkocz (first arXiv posting 2016-11-15) study Gaussian scale mixtures through entropy, moments and geometric inequalities. Chasapis, Eskenazis and Tkocz (first arXiv posting 2022-03-08) obtain sharp Rosenthal-type moment bounds for mixtures, with Gaussian examples. Eskenazis and Gavalakis (first arXiv posting 2023-08-30) study concavity of entropy and convexity of Fisher information for centered Gaussian mixtures. None of the inspected available full-text results states the displayed necessary-and-sufficient *pointwise log-density Hessian* condition or the projection counterexample. Entropic convexity, moment comparison, and Fisher-information convexity do not imply this local curvature classification.

Boedihardjo and Xie (arXiv 2607.17368, 2026) discuss broad recoverability regimes for two log-concave component mixtures. Only an abstract-level comparison was possible here; the accessible description does not state an exact two-scale isotropic criterion, but full-text priority comparison remains a residual risk. The 2016 Gaussian-mixture paper was likewise not available as a complete readable manuscript during the check, so an unindexed equivalent statement cannot be categorically excluded. No claim of independent validation or definitive worldwide priority is made.

## Limitations

The result is confined to two positive centered **isotropic** Gaussian scales and interior weights. It does not classify unequal centers, nonproportional covariance matrices, three or more scale atoms, or general continuous mixing laws. Its numerical verification is finite and is not an infinite-domain certificate. An inaccessible relevant prior source and unindexed terminology remain originality risks; no external independent audit has been performed.

## References

1. A. Eskenazis, P. Nayar and T. Tkocz, *Gaussian mixtures: entropy and geometric inequalities*, arXiv:1611.04921 (first posted 2016-11-15); *Annals of Probability* 46 (2018), 2908–2945, DOI 10.1214/17-AOP1242.
2. G. Chasapis, A. Eskenazis and T. Tkocz, *Sharp Rosenthal-type inequalities for mixtures and log-concave variables*, arXiv:2203.04139 (first posted 2022-03-08); *Bulletin of the London Mathematical Society* 55 (2023), 1222–1239, DOI 10.1112/blms.12786.
3. A. Eskenazis and L. Gavalakis, *On the entropy and information of Gaussian mixtures*, arXiv:2308.15997 (first posted 2023-08-30); *Mathematika* 70 (2024), e12246, DOI 10.1112/mtk.12246.
4. M. T. Boedihardjo and Y. Xie, *Mixture and separation of log-concave measures*, arXiv:2607.17368 (first posted 2026-07-19; abstract-level comparison only).
