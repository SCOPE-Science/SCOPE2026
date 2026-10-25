# A unique decorrelation phase for regular-polygon projection widths

## Finding
Let \(P_n\) be the regular Euclidean \(n\)-gon of circumradius \(R>0\), with \(n\ge3\), and let \(w_n(\theta)\) be its orthogonal projection width in direction \(\theta\). For a uniformly distributed angle \(\Theta\in[0,2\pi)\), define the angular width autocovariance
\[
 C_n(\delta)=\operatorname{Cov}(w_n(\Theta),w_n(\Theta+\delta)).
\]
Set
\[
 N=\begin{cases}n,&n\text{ even},\\2n,&n\text{ odd},\end{cases}
 \qquad a=\frac{\pi}{N},\qquad
 \rho=\begin{cases}2R,&n\text{ even},\\2R\cos(\pi/(2n)),&n\text{ odd}.\end{cases}
\]
Then \(C_n\) is even and \(2a\)-periodic. For \(0\le d\le a\),
\[
\boxed{\displaystyle
 \frac{C_n(d)}{\rho^2}
 =\frac{(2a-d)\cos d+d\cos(2a-d)+\sin(2a-d)+\sin d}{4a}
 -\left(\frac{\sin a}{a}\right)^2.}
\tag{1}
\]
The covariance is **strictly decreasing** on \([0,a]\), from positive to negative values. Thus there exists **exactly one** \(d_n\in(0,a)\) with \(C_n(d_n)=0\). Positive width correlation occurs for \(0\le d<d_n\), and negative correlation for \(d_n<d\le a\); extension by evenness and periodicity gives the complete sign classification for all angular lags.

There is moreover a **universal sharp small-sector limit**. Uniformly for \(0\le q\le1\), as \(n\to\infty\),
\[
\boxed{\displaystyle
 \frac{C_n(aq)}{C_n(0)}
 =1-\frac{15}{8}q^2(2-q)^2+O(a^2).}
\tag{2}
\]
In particular, the unique decorrelation fraction and the strongest anticorrelation obey
\[
 \frac{d_n}{a}
 =1-\sqrt{1-\sqrt{8/15}}+O(a^2)
 =0.4806703776407718\ldots+O(a^2),
\tag{3}
\]
\[
 \frac{C_n(a)}{C_n(0)}=-\frac78+O(a^2).
\tag{4}
\]
The normalized correlation and the transition fraction are independent of circumradius. The width variance itself tends to zero with \(C_n(0)=\rho^2 a^4/45+O(\rho^2a^6)\), so (2)--(4) refer to normalized fluctuations, not nonvanishing absolute covariance.

## Assumptions and scope
Width is \(w_n(\theta)=\max_{x\in P_n}x\cdot u_\theta-\min_{x\in P_n}x\cdot u_\theta\), where \(u_\theta=(\cos\theta,\sin\theta)\). Covariance is with respect to the **same** uniform angle, shifted deterministically by \(\delta\), rather than two independent directions. The first signed half-period is \([0,a]\). The polygon is nondegenerate, and the result is exact for every integer \(n\ge3\), regardless of parity. The error terms are uniform in \(q\in[0,1]\), with absolute constants for sufficiently large \(n\).

## Proof
**A reduction to one cosine chamber.** For every planar convex body \(K\), its width is the support function of the difference body \(K-K\), since \(h_{K-K}(u)=h_K(u)+h_K(-u)\). If \(n\) is even, \(P_n=-P_n\) after centering, so \(P_n-P_n=2P_n\), a regular \(n\)-gon of circumradius \(2R\). If \(n\) is odd, the differences of its vertices have extremal length \(2R\cos(\pi/(2n))\); their extremal directions form a regular \(2n\)-gon, which is \(P_n-P_n\). To check this last assertion directly, write vertices as \(R e^{2\pi i j/n}\). For cyclic separations \(k\), the difference length is \(2R\sin(\pi k/n)\); its maximum is attained at \(k=(n\pm1)/2\), producing \(2n\) equally spaced extremal vectors whose convex hull contains every other vertex difference: every nonmaximal separation has length at most \(2R\cos(3\pi/(2n))\), which is less than the inradius \(2R\cos^2(\pi/(2n))\) of that regular \(2n\)-gon, because \(\cos(3x)<\cos^2x\) for \(0<x<\pi/6\). For \(n=3\) there are no nonmaximal separations. Therefore, after a harmless angular rotation, the width as a periodic function is
\[
 w_n(\theta)=\rho\cos t,
 \quad t\equiv\theta\pmod{2a},\quad -a\le t\le a.
\tag{5}
\]
In particular, its angular mean is \(\mu=\rho\sin a/a\).

**Exact two-direction product.** With a lag \(0\le d\le a\), only one chamber wrap occurs. The normalized mixed second moment is
\[
\frac{\mathbb E[w_n(\Theta)w_n(\Theta+d)]}{\rho^2}
 =\frac{1}{2a}\left[
 \int_{-a}^{a-d}\cos t\cos(t+d)\,dt
 +\int_{a-d}^{a}\cos t\cos(t+d-2a)\,dt\right].
\tag{6}
\]
Using \(2\cos x\cos y=\cos(x-y)+\cos(x+y)\) in both integrals gives the first term of (1). Subtracting \(\mu^2\) proves (1) without any finite sampling assumption.

**Exactly one zero.** Differentiation of (1) gives
\[
 \frac{C_n'(d)}{\rho^2}
 =\frac{d\sin(2a-d)-(2a-d)\sin d}{4a}.
\tag{7}
\]
For \(0<d<a\), set \(x=d\), \(y=2a-d\). Then \(0<x<y\le2a\le\pi/2\). Since \(t\mapsto\sin t/t\) strictly decreases on \((0,\pi)\), we have \(x\sin y-y\sin x<0\). Thus (7) is strictly negative. The function \(w_n\) is nonconstant, so \(C_n(0)=\operatorname{Var}(w_n(\Theta))>0\). Also, periodicity and centering give
\[
 \int_0^{2a}C_n(d)\,dd
 =\int_0^{2a}\mathbb E[(w_n(\Theta)-\mu)(w_n(\Theta+d)-\mu)]\,dd=0.
\tag{8}
\]
Evenness and period \(2a\) imply that this is twice the integral over \([0,a]\). The strict decrease and positive starting value force \(C_n(a)<0\), since otherwise the integral could not vanish. Intermediate value and strict monotonicity yield the single zero and the complete sign classification.

**Universal quartic law.** Put \(t=as\), \(-1\le s\le1\), and \(f_a(s)=\cos(as)-\sin(a)/a\), periodically extended with period \(2\). Uniform Taylor expansion gives
\[
 f_a(s)=a^2\left(\frac16-\frac{s^2}{2}\right)+O(a^4).
\tag{9}
\]
Let \(f(s)=1/6-s^2/2\), of mean zero on \([-1,1]\), and let \(f\) be 2-periodic. Elementary splitting at the single wrap gives
\[
 \frac12\int_{-1}^1 f(s)f(s+q)\,ds
 =\frac{8-15q^2(2-q)^2}{360}
 =:H(q),\quad 0\le q\le1.
\tag{10}
\]
The integrals in (10) are ordinary polynomial integrals on \([-1,1-q]\) and \([1-q,1]\), with the latter using \(f(s+q-2)\). Equations (9)--(10) imply the uniform expansion
\[
 C_n(aq)=\rho^2a^4(H(q)+O(a^2)),\quad
 C_n(0)=\rho^2a^4(1/45+O(a^2)),
\tag{11}
\]
which proves (2), since \(H(0)=1/45\). Furthermore,
\[
 H'(q)=-\frac16 q(2-q)(1-q)<0\quad(0<q<1).
\]
Its unique zero is \(q_*=1-\sqrt{1-\sqrt{8/15}}\), whose derivative is nonzero. Uniformity of (11), uniqueness of the finite-\(n\) root, and the mean-value theorem give \(d_n/a=q_*+O(a^2)\). Finally \(H(1)=-7/360\), so \(H(1)/H(0)=-7/8\). This establishes (3)--(4).

## Verification
Run `python verify.py` with Python 3 standard library. The script independently constructs the polygon from its vertices, computes its widths as max-minus-min dot products, integrates the two-direction product on a fine deterministic angular mesh, and compares its covariance against (1) for integers \(3\le n\le12\) and five angular lags per polygon. It also checks finite-lag symmetries, strict interior sign changes and numerical roots, and the approach to the asymptotic value for three larger side counts. The actual run printed `VERIFY_OK: 223 finite numerical regression checks`. The program has no external inputs, no randomized tests, and no proof role for all infinitely many \(n\). The proof is entirely (5)--(11).

## Relationship to prior work
Akiyama and Kamae [1] study the deviation rate of random directional polygon widths. Their Theorem 1 gives a pairwise second-moment kernel for edge projection contributions and thereby supplies a general tool from which many second-order width identities can be calculated. Their main results concern the **unshifted variance** and its extrema over polygons. The scalar zero-lag variance in (11) is consistent with their work and is not claimed as a stand-alone new invariant. The present finding is the distinct **joint angular-lag** conclusion: the full piecewise covariance formula for the regular-polygon family, its global strict unimodality, the unique decorrelation threshold for every side count, and the universal asymptotic fourth-degree correlation profile. These conclusions are proved here directly and were not identified in the inspected primary paper. The general pairwise-moment technology is a genuine route by which similar formulas could be derived; this is a priority risk rather than evidence that this theorem is already published.

Relevant geometric research records on regular-polygon chord-width products [2] and on single-direction projection-width distributions of tangential polygons [3] study different observables. In particular, an orthogonal chord-width *product* and a marginal width distribution do not determine the centered covariance of two widths at a prescribed angular offset. No claim of global uniqueness in the literature is made.

## Limitations
The theorem is specific to regular planar polygons and uniform random orientation; it does not assert monotonic angular covariance or the same limit law for arbitrary convex polygons, ellipses, or nonuniform angular distributions. Formula (1) is a trigonometric second-moment computation; the asserted mathematical content is its exact all-side-count sign classification and limiting normalized decorrelation law, not the general concept of autocorrelation. Prior general second-moment formulas are a potential alternative derivation, and completeness of literature priority has not been independently established. The numerical tests cannot certify infinite quantifiers or originality. Independent mathematical audit has not been performed.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, first submitted 18 January 2022, especially Theorem 1 (edge second-moment kernel) and the results on width deviation. https://arxiv.org/abs/2201.06736
2. *Exact translative convex-hull profile of every regular polygon*, public research record (2026), `2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0
3. *Inverse classification of projection-width distributions for tangential symmetric polygons*, public research record (2026), `2026/10/11/SCOPE-inverse-classification-of-projection-width-distributions-for-tan--2ee871113939`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-inverse-classification-of-projection-width-distributions-for-tan--2ee871113939
