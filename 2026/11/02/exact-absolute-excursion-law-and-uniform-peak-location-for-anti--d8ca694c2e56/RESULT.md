# Exact absolute-excursion law and uniform peak location for anti-periodic Brownian motion

## Finding
Let \(W=(W_t)_{0\le t\le1}\) be standard Brownian motion started at zero, and set
\[
X_t=W_t-\tfrac12W_1,\qquad S=\max_{0\le t\le1}|X_t|.
\]
This is the anti-periodic Gaussian process: \(X_1=-X_0\), and its covariance is
\(K(s,t)=\tfrac14-\tfrac12|s-t|\). For every \(h>0\), its *entire* absolute-supremum distribution has the two equivalent, rapidly convergent representations
\[
\boxed{\Pr(S<h)=2\sum_{k=1}^{\infty}(-1)^{k+1}
  \exp\!\left(-\frac{k^2\pi^2}{8h^2}\right)
=1-4h\sqrt{\frac2\pi}\sum_{j=0}^{\infty}
  \exp\!\left(-2(2j+1)^2h^2\right).}
\]
Every positive real moment is explicit: for all \(q>0\),
\[
\boxed{\mathbb E S^q=\frac{q\,2^{1-q/2}}{\sqrt\pi}
 \Gamma\!\left(\frac{q+1}{2}\right)
 \left(1-2^{-(q+1)}\right)\zeta(q+1).}
\]
In particular, \(\mathbb ES=\pi^{3/2}/(4\sqrt2)\) and \(\mathbb ES^2=7\zeta(3)/8\).

There is also an exact peak-location law. With probability one, \(|X|\) has a unique maximizer \(U\) on the unit circle formed by identifying the endpoints \(0\) and \(1\). Its location \(U\in[0,1)\) is **uniformly distributed and independent of \(S\)**.

## Assumptions and scope
The path \(W\) is a real-valued standard Brownian motion on the closed unit interval, with variance normalization \(\operatorname{Var}(W_t-W_s)=|t-s|\). The supremum is over the entire continuous path, not a mesh. All series are ordinary absolutely convergent series at each fixed \(h>0\), and the moment identity holds for every real \(q>0\). The maximizing time is interpreted modulo the endpoint identification; the equality \(|X_0|=|X_1|\) makes this identification necessary. No separate independent endpoint noise is added.

## Proof
**1. Endpoint-dependent absorbing heat kernel.** Write \(z=W_1\). The path \(X\) starts at \(-z/2\), ends at \(z/2\), and has standard Brownian bridge fluctuations conditional on \(z\). Denote by \(p_{(-h,h)}(t;x,y)\) the transition density at time \(t\) of standard Brownian motion killed upon leaving \((-h,h)\). The usual Brownian bridge conditioning identity, including the endpoint density, yields
\[
\Pr(S<h)=\int_{-2h}^{2h}p_{(-h,h)}(1;-z/2,z/2)\,dz.
\]
For \(x,y\in(-h,h)\), Dirichlet eigenfunction expansion gives
\[
p_{(-h,h)}(1;x,y)=\frac1h\sum_{k=1}^{\infty}
\exp\!\left(-\frac{k^2\pi^2}{8h^2}\right)
\sin\!\left(\frac{k\pi(x+h)}{2h}\right)
\sin\!\left(\frac{k\pi(y+h)}{2h}\right).
\]
The series converges uniformly on the compact square for fixed \(h\), permitting integration. Setting \(x=-z/2\), \(y=z/2=-x\) and \(v=(x+h)/(2h)\) reduces the \(k\)-th spatial integral to
\[
2\int_0^1 2\sin(k\pi v)\sin(k\pi(1-v))\,dv
=2(-1)^{k+1}.
\]
This proves the first series with the exact diffusion factor \(1/2\) and interval width \(2h\).

**2. Gaussian image expansion and moments.** Jacobi's theta transformation (equivalently, Poisson summation for the half-integer Gaussian lattice) yields
\[
1-2\sum_{k\ge1}(-1)^{k+1}e^{-k^2\pi^2/(8h^2)}
=4h\sqrt{2/\pi}\sum_{j\ge0}e^{-2(2j+1)^2h^2}.
\]
The right-hand side is the nonnegative survival tail \(\Pr(S\ge h)\). Thus, for \(q>0\), Tonelli's theorem applies termwise in
\(\mathbb ES^q=q\int_0^{\infty}h^{q-1}\Pr(S>h)\,dh\). Using
\[
\int_0^{\infty}h^q e^{-2m^2h^2}\,dh
=\frac12(2m^2)^{-(q+1)/2}\Gamma\!\left(\frac{q+1}{2}\right)
\]
and \(\sum_{m\ge1,\;m\text{ odd}}m^{-(q+1)}=(1-2^{-(q+1)})\zeta(q+1)\) gives the stated all-order formula. The first terms of the spectral and image expansions also give the sharp tails
\[
\Pr(S<h)=2e^{-\pi^2/(8h^2)}\left(1+O(e^{-3\pi^2/(8h^2)})\right)
\quad(h\downarrow0),
\]
\[
\Pr(S>h)=4h\sqrt{2/\pi}\,e^{-2h^2}
\left(1+O(e^{-16h^2})\right)\quad(h\to\infty).
\]

**3. Uniqueness and uniformity of the peak.** Standard Brownian motion has almost surely unique maximum and minimum on \([0,1]\). A tie between the positive and negative extremes of \(X\) would require
\(\max W+\min W=W_1\). This has probability zero: for \(a<\min(0,z)\), \(b>\max(0,z)\), the joint probability density in \(z\) of \(\min W>a,\max W<b,W_1\in dz\) is the killed kernel \(p_{(a,b)}(1;0,z)\); this kernel is smooth in the two interior barrier parameters, so the joint law of the two strict extrema and endpoint has a density, which assigns zero mass to that equality surface. Brownian local oscillations also exclude an endpoint from being an absolute maximizer, almost surely. Hence the circular maximizing point is unique.

For \(a\in[0,1)\), define the signed rotation
\[
(R_aX)(t)=
\begin{cases}X(t+a),&t+a\le1,\\
-X(t+a-1),&t+a>1.
\end{cases}
\]
Its covariance is again \(K(s,t)=1/4-|s-t|/2\), by checking whether zero, one or both arguments wrap and using \(X(1)=-X(0)\). As these are centered Gaussian processes with continuous paths, \(R_aX\) and \(X\) have the same law. Absolute value removes the sign flip, so \(R_a\) acts on \(|X|\) by a circular rotation; it leaves \(S\) unchanged and translates its unique maximizer by \(-a\) modulo one. The joint law \((S,U)\) is thus invariant under every translation of \(U\). The unique translation-invariant probability measure on the circle is normalized Lebesgue measure, even after conditioning on any event determined by \(S\). Therefore \(U\) is uniform and independent of \(S\).

## Verification
The standalone standard-library program `verify.py` checks the covariance and its finite-grid signed rotation invariance by exact rational/integer arithmetic; independently compares the heat-kernel spectral and Poisson-transformed CDFs over hundreds of thresholds; checks the spatial Dirichlet eigenfunction integral by high-order quadrature; and reproduces the first two moments by tail integration. It reports **61,766 passed deterministic assertions**. These tests verify constants and formulas, while the infinite series identities, all-real-moment statement and peak-time independence are justified by the arguments above, not by enumeration.

## Relationship to prior work
Raket (2026), Section 4.2 and Proposition 4.3, specifies exactly this anti-periodic stationary Gaussian process, its endpoint tie and covariance, but not the distribution of its absolute path supremum or peak time. Biane, Pitman and Yor (1999/2001) give classical Jacobi-theta identities and extrema laws for Brownian bridge, excursion, meander and Bessel processes; those standard transformations are credited here, not presented as new. Perman and Wellner (2014), Theorem 6, derive Brownian-bridge extrema and Kuiper laws, involving different boundary conditions and distinct functionals. A previously established general small-ball asymptotic for Gaussian bridge mixtures supplies only the \(h\downarrow0\) scale, not this full distribution, all moments or the joint peak-height/location law. The proposed new contribution is the complete identification of this specific anti-periodic law and its location factorization, not the classical heat-kernel or theta machinery itself.

## Limitations
No originality assertion is made for the underlying theta transformation, killed heat kernel, or general stationarity/Haar argument. Historical-priority research has not excluded every unindexed formulation of anti-periodic confinement; independent literature verification is still needed. The result is specific to the centered anti-periodic law with no additive independent Gaussian offset; it does not cover the wider stationary Slepian family or multivariate Brownian processes. No convergence rate for numerical path discretization is asserted.

## References
1. Lars Lau Raket, *A Bestiary of Brownian Processes: A Field Guide to Boundary Conditions and Conditioning*, arXiv:2610.33747v1 (first public 2026-10-24), Section 4.2 and Proposition 4.3, https://arxiv.org/html/2610.33747v1.
2. Philippe Biane, Jim Pitman and Marc Yor, *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*, arXiv:math/9912170v1 (1999), especially Sections 2 and 4, https://arxiv.org/pdf/math/9912170.
3. Mihael Perman and Jon A. Wellner, *An excursion approach to maxima of the Brownian bridge*, *Stochastic Processes and their Applications* 124 (2014), 3106–3120, Theorem 6, https://pmc.ncbi.nlm.nih.gov/articles/PMC4847753/.
