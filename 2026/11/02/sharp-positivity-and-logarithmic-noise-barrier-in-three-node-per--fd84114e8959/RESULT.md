# Sharp positivity and logarithmic noise barrier in three-node perturbed trigonometric quadrature

## Finding

Let \(h=2\pi/3\). Independently draw \(\delta_{-1},\delta_0,\delta_1\) uniformly from \([-\alpha,\alpha]\) for \(0\le\alpha\le1/2\), with the convention that \(\alpha=0\) gives three deterministic equally spaced nodes. Form \(\theta_j=h(j+\delta_j)\) on the circle, and take the unique real interpolation-quadrature weights \(W_j\) satisfying
\[
\sum_{j=-1}^1 W_j=2\pi,\quad
\sum_{j=-1}^1 W_j\cos\theta_j=0,\quad
\sum_{j=-1}^1 W_j\sin\theta_j=0.
\]
Thus the rule is exact on \(\operatorname{span}\{1,\cos\theta,\sin\theta\}\). The weights exist and are finite almost surely, including at \(\alpha=1/2\). Their strict-positivity probability is exactly
\[
\mathbb P\{W_{-1}>0,W_0>0,W_1>0\}=
\begin{cases}
1,&0\le\alpha\le1/4,\\
1-\dfrac32\left(1-\dfrac1{4\alpha}\right)^2,&1/4<\alpha\le1/2.
\end{cases}
\]
In particular it equals \(5/8\) at \(\alpha=1/2\). For every real \(p>0\), the absolute-moment condition is
\[
\mathbb E\sum_{j=-1}^1|W_j|^p<\infty
\quad\Longleftrightarrow\quad
\bigl(\alpha<1/2\bigr)\ \text{or}\ \bigl(\alpha=1/2\ \text{and}\ p<2\bigr).
\]
At the upper perturbation endpoint the expected squared weight norm diverges, with the sharp approach from below
\[
\mathbb E\sum_{j=-1}^1 W_j^2
=54\left(\frac{2\sqrt3}{\pi}-1\right)
\log\frac1{1-2\alpha}+O(1),\qquad\alpha\uparrow1/2.
\]
This is a pair of distinct transitions: positivity can fail after perturbation fraction \(1/4\), whereas finite-variance noise robustness persists until the endpoint fraction \(1/2\).

## Assumptions and scope

The samples are independent and each perturbation is **uniform** on the indicated interval; the trigonometric rule is the *unique degree-one interpolatory rule*, not a reweighted positive rule or a polynomial quadrature. The integral is with respect to Lebesgue measure on a full \(2\pi\)-period. For \(\alpha=1/2\), collisions have probability zero and all assertions are interpreted almost surely. Numerical errors due to finite precision are not included. If observation noises are independent of one another and of the node jitters, and have common finite variance \(\sigma^2>0\), conditional on the nodes their contribution to the quadrature-output variance equals \(\sigma^2\sum_jW_j^2\); the moment results therefore govern unconditional observation-noise variance. No assertion is made about integration bias for arbitrary periodic integrands outside the exact three-dimensional space.

## Proof

**Step 1: circular-gap formula.** The three cyclic gaps in positive angular order are
\[
a=h(1+\delta_0-\delta_{-1}),\qquad
b=h(1+\delta_1-\delta_0),\qquad
c=h(1+\delta_{-1}-\delta_1),\qquad a+b+c=2\pi.
\]
Almost surely \(a,b,c\in(0,2\pi)\); their half-angle sines are positive. Solving the three linear moment equations gives
\[
(W_{-1},W_0,W_1)=\frac{2\pi}{S}(\sin b,\sin c,\sin a),\qquad
S=\sin a+\sin b+\sin c
=4\sin(a/2)\sin(b/2)\sin(c/2)>0.
\]
The formula also proves unique solvability because the three nodes are distinct and the associated points on the unit circle form a nondegenerate triangle. In particular all weights are positive if and only if all three gaps are smaller than \(\pi\). At most one gap can exceed \(\pi\).

**Step 2: the exact sign probability.** The event \(a>\pi\) is \(\delta_0-\delta_{-1}>1/2\). Its probability vanishes for \(\alpha\le1/4\). For \(1/4<\alpha\le1/2\), integration of the triangular difference density of two independent \(\operatorname{Uniform}[-\alpha,\alpha]\) variables gives
\[
\mathbb P(a>\pi)=\frac{(2\alpha-1/2)^2}{8\alpha^2}
=\frac12\left(1-\frac1{4\alpha}\right)^2.
\]
The analogous events for \(b,c\) are disjoint, since the positive gaps sum to \(2\pi\). Therefore subtracting three equal probabilities proves the displayed formula. Equality events have probability zero, so nonnegative versus strictly positive gives the same probability.

**Step 3: moment threshold.** When \(\alpha<1/2\), every gap is bounded below by \(h(1-2\alpha)>0\), and the continuous weight formula has a bounded range over the compact perturbation cube. Consequently every finite positive absolute moment exists.

For \(\alpha=1/2\), possible unboundedness occurs only near the three pair-collision corners. Near the corner \(\delta_{-1}=1/2\), \(\delta_0=-1/2\), write
\[
\delta_{-1}=1/2-u,\qquad \delta_0=-1/2+v,
\qquad 0\le u,v\ll1,\qquad \delta_1=z\in[-1/2,1/2].
\]
Then \(a=h(u+v)\) and \(b=\pi+hz+O(v)\). Uniformly in \(z\) and sufficiently small \(u,v\), the two weights attached to the colliding pair have expansions
\[
W_{-1}=-\frac{2\pi}{h(u+v)}\tan\frac{hz}{2}+O(1),\qquad
W_0=\frac{2\pi}{h(u+v)}\tan\frac{hz}{2}+O(1),
\]
where \(W_1=O(1)\). This follows by inserting the gaps into the exact sine formula, noting \(1+\cos(hz)\ge1/2\). For any fixed subinterval of \(z\) bounded away from zero, the leading coefficient has positive magnitude. On the full compact \(z\)-interval the weights are \(O(1+(u+v)^{-1})\). Thus integrability is exactly the integrability of \((u+v)^{-p}\) over a two-dimensional corner, namely \(\int_0^\epsilon\int_0^\epsilon(u+v)^{-p}\,du\,dv<\infty\) precisely when \(p<2\). The other two corners are cyclic rotations; elsewhere the weights are bounded. This proves the asserted if-and-only-if condition.

**Step 4: exact logarithmic coefficient.** Put \(\Delta=1-2\alpha\downarrow0\). At the same collision corner take \(\delta_{-1}=\alpha-u\), \(\delta_0=-\alpha+v\), and \(\delta_1=z\in[-\alpha,\alpha]\). Then \(a=h(\Delta+u+v)\), and a uniform expansion on a fixed small corner square gives
\[
\sum_jW_j^2=
\frac{8\pi^2}{h^2}\frac{\tan^2(hz/2)}{(\Delta+u+v)^2}
+O\left(\frac1{\Delta+u+v}\right)+O(1),
\]
where the error is uniform in \(z\). The \(O((\Delta+u+v)^{-1})\) term is integrable uniformly as \(\Delta\downarrow0\), because the corner has two independent coordinates. The other parts of the cube contribute \(O(1)\), and the two additional collision corners have the same leading contribution. At any fixed \(\epsilon>0\),
\[
\int_0^\epsilon\int_0^\epsilon\frac{du\,dv}{(\Delta+u+v)^2}
=\log\frac1\Delta+O(1).
\]
The joint perturbation density is \((2\alpha)^{-3}=1+O(\Delta)\); changing the \(z\)-integration interval to \([-1/2,1/2]\) changes the integrated answer by \(O(1)\). As \(h=2\pi/3\), the coefficient from all three corners is
\[
3\frac{8\pi^2}{h^2}
\int_{-1/2}^{1/2}\tan^2(\pi z/3)\,dz
=54\left(\frac{2\sqrt3}{\pi}-1\right).
\]
This proves the logarithmic asymptotic with a bounded remainder. At \(\alpha=1/2\) the same corner estimates make the second moment infinite.

## Verification

Run `python verify.py` with the dependencies in `requirements.txt`. The verifier independently solves the trigonometric moment equations at a reproducible grid of random perturbations and checks normalization, exactness on both first harmonics, signs, and the analytical positivity probability against large independently sampled batches. Symbolic calculations verify the one-dimensional tangent-square integral and two-dimensional regularized corner integral. The packaged version passed 251 checks. These finite tests are diagnostics; the proof above supplies the all-parameter statements and the exact logarithmic coefficient.

## Relationship to prior work

Austin and Trefethen (2016 preprint; 2017 journal) establish smooth-function convergence of trigonometric interpolation/quadrature for arbitrary bounded perturbed grids when \(\alpha<1/2\). Their results concern asymptotic convergence in the number of nodes, not the three-node random sign probability or noise-amplification law derived here. Yu and Townsend (2022 preprint; 2023 journal), Sections 4.1–4.2 and Appendix B, analyze nonuniform Fourier sampling and quadrature, prove that *some sufficiently large* rules acquire negative weights for every \(\alpha>0\), and provide bounds for small perturbations. Those results do not imply this smallest-grid sharp \(1/4\) positivity threshold, its exact probability under independent uniform perturbations, or the critical \(1/2\) noise-moment divergence. They do not contradict the present three-node positivity interval: the number of points matters. Karvonen, Kanagawa and Särkkä (2019) study positivity and magnitudes of Bayesian quadrature weights for different kernel rules, not these trigonometric interpolation weights. Classical polynomial three-node random quadrature has different geometry and probability laws and does not imply the periodic result. Earlier general estimates about perturbed-node conditioning remain relevant background, not the exact distribution of this random quadrature rule.

## Limitations

The number of nodes is exactly three, the underlying grid equally spaced on a period, the jitter coordinates independent and identically uniform, and the weights are those of exact degree-one trigonometric interpolation. Neither the positivity probability nor the logarithmic coefficient is claimed for larger grids, nonuniform jitter distributions, adaptive positive-weight quadrature, or arbitrary observation-error covariance. The amplitude of noise may be small, but an unbounded second weight moment does not imply actual numerical divergence for every deterministic integrand. The asymptotic is at the upper parameter endpoint and should not be interpreted as a large-node limit. The mathematical result has not undergone independent review.

## References

1. A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (first public version 2016-12-13); *SIAM J. Numer. Anal.* 55 (2017), DOI: 10.1137/16M1107760. https://arxiv.org/abs/1612.04018
2. A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722 (first public version 2022-02-09); *BIT Numer. Math.* 63 (2023), DOI: 10.1007/s10543-023-00965-z. https://arxiv.org/abs/2202.04722
3. T. Karvonen, M. Kanagawa and S. Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, *Stat. Comput.* 29 (2019), DOI: 10.1007/s11222-019-09901-0. https://doi.org/10.1007/s11222-019-09901-0
