# Universal collision-tail and nugget moment laws for random exponential-kernel matrices

## Finding

Fix an integer \(n\ge2\), a correlation-decay parameter \(\gamma>0\), and a continuous probability density \(w:[0,1]\to[0,\infty)\). Draw \(X_1,\ldots,X_n\) independently from \(w\), and form the real symmetric exponential covariance matrix
\[
K_{ij}=\exp(-\gamma|X_i-X_j|),\qquad 1\le i,j\le n.
\]
It is positive definite almost surely. Set
\[
C_{n,w,\gamma}=\frac{n(n-1)}{\gamma}\int_0^1 w(x)^2\,dx.
\]
Then, at fixed \(n\), \(w\), and \(\gamma\),
\[
\lim_{t\to\infty}t\,\Pr\{\|K^{-1}\|_2>t\}=C_{n,w,\gamma},\qquad
\lim_{s\downarrow0}s^{-1}\Pr\{\lambda_{\min}(K)<s\}=C_{n,w,\gamma}.
\]
For every real \(q>0\),
\[
\mathbb E\|K^{-1}\|_2^q<\infty\quad\Longleftrightarrow\quad 0<q<1.
\]
For the positive nugget \(\tau\), define \(R_\tau=(K+\tau I_n)^{-1}\). As \(\tau\downarrow0\),
\[
\mathbb E\|R_\tau\|_2\sim C_{n,w,\gamma}\log(1/\tau),\qquad
\mathbb E\|R_\tau\|_2^q\sim\frac{C_{n,w,\gamma}}{q-1}\tau^{1-q}\quad(q>1).
\]
For \(0<q<1\), the nugget-regularized moments instead converge to the finite unregularized moment. Finally,
\[
C_{n,w,\gamma}\ge\frac{n(n-1)}{\gamma},
\]
with equality if and only if \(w=1\) almost everywhere on \([0,1]\). Thus uniform independent node sampling uniquely minimizes the *leading large-condition-amplification tail constant* among continuous sampling densities. This does not assert finite-threshold stochastic dominance or universal optimality for prediction.

For independent uniform nodes and their minimum adjacent ordered spacing \(\Delta\), an exact calibration identity is
\[
\Pr\{\Delta\le r\}=1-(1-(n-1)r)^n,
\qquad 0\le r\le 1/(n-1).
\]
When \(n=2\), an exact inverse-norm tail is available: for \(t>1\), with \(a=\min\{1,-\log(1-t^{-1})/\gamma\}\),
\[
\Pr\{\|K^{-1}\|_2>t\}=2a-a^2.
\]

## Assumptions and scope

The number of observations \(n\) is fixed and finite; it does not grow in any asserted asymptotic. The density \(w\) is continuous, nonnegative, integrates to one, and need not be strictly positive everywhere. No deterministic lower separation between sampling locations is imposed. All random-matrix claims concern the operator \(2\)-norm in exact real arithmetic; the nugget parameter is a positive scalar multiplying the identity. The covariance is the one-dimensional stationary Ornstein–Uhlenbeck kernel, equivalently the Matérn kernel with smoothness \(1/2\), normalized to have unit diagonal.

## Proof

**1. Exact precision factorization and a uniform spacing bound.** Sorting locations conjugates \(K\) by a permutation and does not change its eigenvalues. Hence write \(x_1<\cdots<x_n\), \(d_i=x_{i+1}-x_i>0\), and \(r_i=e^{-\gamma d_i}\). Independent standard normal innovations in the recursion \(Z_1\sim N(0,1)\), \(Z_{i+1}=r_iZ_i+\sqrt{1-r_i^2}\,\varepsilon_i\) generate exactly covariance \(K\). Completing their log-density squares gives, for all \(z\in\mathbb R^n\),
\[
z^{\mathsf T}K^{-1}z=z_1^2+\sum_{i=1}^{n-1}\frac{(z_{i+1}-r_i z_i)^2}{1-r_i^2}.
\tag{1}
\]
This verifies strict positive definiteness without an assumption about numerical invertibility. With \(\Delta=\min_i d_i\), the two-coordinate Rayleigh vector at its shortest gap yields
\[
\lambda_{\min}(K)\le 1-e^{-\gamma\Delta}\le\gamma\Delta,
\qquad\|K^{-1}\|_2\ge(\gamma\Delta)^{-1}.
\tag{2}
\]
Conversely, each summand in (1) has rank one and operator norm \((1+r_i^2)/(1-r_i^2)\). For \(d_i\le1\), the denominator obeys \(1-e^{-2\gamma d_i}\ge 2\gamma e^{-2\gamma}d_i\), and the numerator is at most \(2\). Consequently, for some finite constant \(L=L(n,\gamma)\),
\[
\|K^{-1}\|_2\le L/\Delta
\tag{3}
\]
for every distinct ordered configuration.

**2. Precisely one collapsing gap.** Fix \(\varepsilon>0\). If an adjacent gap \(d_i=\delta\to0\) while all other adjacent gaps are at least \(\varepsilon\), then its single term in (1) expands in operator norm to
\[
K^{-1}=\frac{(e_{i+1}-e_i)(e_{i+1}-e_i)^{\mathsf T}}{2\gamma\delta}+O_{n,\gamma,\varepsilon}(1).
\tag{4}
\]
Indeed \(1-r_i^2=2\gamma\delta+O(\delta^2)\), and \((-r_i,1)=(-1,1)+O(\delta)\); every other denominator in (1) stays uniformly bounded below. The rank-one matrix in (4) has eigenvalue \(2\), proving the *uniform* estimate
\[
\|K^{-1}\|_2=\frac1{\gamma\delta}+O_{n,\gamma,\varepsilon}(1).
\tag{5}
\]

**3. Sharp collision probability.** For any distinct labelled pair and \(a\downarrow0\), boundedness and continuity of \(w\) imply, by dominated convergence,
\[
\Pr\{|X_1-X_2|<a\}=2a\int_0^1w(x)^2\,dx+o(a).
\tag{6}
\]
The intersection of any two different labelled pair-collision events of radius \(a\) has probability \(O(a^2)\), even if they share a node, because the joint density is bounded. The shortest pair is necessarily adjacent in sorted order; inclusion–exclusion therefore yields
\[
\Pr\{\Delta<a\}=n(n-1)a\int_0^1w(x)^2\,dx+o(a).
\tag{7}
\]
For a fixed \(\varepsilon>0\) and a fixed \(B<\infty\), configurations having a gap below \(B/t\) *and another distinct gap below* \(\varepsilon\) have probability at most \(O_{n,w,B}(\varepsilon/t)\); this follows by conditioning on the at most three or four labelled locations in the two pair-collision events, using the bounded joint density. By (3), the event \(\|K^{-1}\|_2>t\) requires \(\Delta<L/t\). Outside the just-bounded multiple-gap event, (5) sandwiches it, for any fixed \(\eta>0\) and sufficiently large \(t\), between the single-collision events \(\Delta<(1-\eta)/(\gamma t)\) and \(\Delta<(1+\eta)/(\gamma t)\). Inserting (7), multiplying by \(t\), then letting \(t\to\infty\), \(\varepsilon\downarrow0\), and \(\eta\downarrow0\), proves the first limit. Since \(\|K^{-1}\|_2=\lambda_{\min}(K)^{-1}\), the second follows immediately.

**4. Moments and nugget limits.** The tail layer-cake identity gives, for every \(q>0\), \(\mathbb E\|K^{-1}\|_2^q=q\int_0^\infty t^{q-1}\Pr\{\|K^{-1}\|_2>t\}\,dt\). The strictly positive constant in the proved \(C/t\) tail makes this integral finite exactly for \(0<q<1\). For \(Y=\lambda_{\min}(K)\), note \(0<Y\le1\) (unit diagonal). Put \(F(s)=\Pr\{Y\le s\}=Cs+o(s)\) as \(s\downarrow0\). Integration by parts gives exactly
\[
\mathbb E(Y+\tau)^{-q}=(1+\tau)^{-q}+q\int_0^1F(s)(s+\tau)^{-q-1}\,ds.
\tag{8}
\]
Split the integral at fixed small \(s_0>0\); the part above \(s_0\) is uniformly bounded. The substitution \(s=\tau u\) in the lower part, followed by \(F(s)/s\to C\), gives \(qC\int_0^\infty u(1+u)^{-q-1}du=C/(q-1)\) for \(q>1\), at scale \(\tau^{1-q}\). For \(q=1\), the same integral grows as \(C\log(1/\tau)\). Finally, for \(0<q<1\), monotone convergence as \(\tau\downarrow0\) gives the finite unregularized moment. The spectral theorem identifies \(\|R_\tau\|_2=(Y+\tau)^{-1}\).

**5. Sampling-density extremum and calibration.** Cauchy–Schwarz on an interval of length one gives \(\int w^2\ge(\int w)^2=1\), with equality only when \(w\equiv1\) almost everywhere. For uniform nodes, sorting gives constant density \(n!\) on the ordered simplex. Subtracting \((i-1)r\) from its \(i\)-th coordinate maps the region of all adjacent gaps greater than \(r\) bijectively onto an ordered simplex of length \(1-(n-1)r\), proving the spacing identity by volume scaling. For two nodes, the eigenvalues of \(K\) are \(1\pm e^{-\gamma|X_1-X_2|}\), and uniform-distance distribution \(\Pr\{|X_1-X_2|<a\}=2a-a^2\) for \(0\le a\le1\), giving the exact two-node tail.

## Verification

A standalone Python diagnostic `verify.py` verifies the Markov precision identity symbolically on three exact rational-correlation examples, tests 280 numerical precision inversions, 36 isolated collision limits, nine exact two-node tail comparisons, three finite-sample checks of the uniform-gap probability and four high-precision two-node nugget integral asymptotics. A successful run prints

`VERIFY_OK exact_precision=3 direct_precision=280 single_collisions=36 exact_two_node_tails=9 min_spacing=3 nugget_integrals=4`

Exact symbolic checks confirm finite-dimensional algebra; the analytical proof above, not simulation or finite numerical tests, establishes the distributional limits and infinite-moment boundary.

## Relationship to prior work

The OU/Matérn-\(1/2\) covariance structure and its tridiagonal Markov precision are classical (Rybicki and Press). Barnett, Greengard and Rachh study Matérn kernel approximation and matrix conditioning in Gaussian-process regression, including positive fixed-nugget bounds. Barthelmé and Usevich analyze spectral behavior in a different *flat-kernel* limit with fixed sites. Ranjan, Haynes and Karsten study numerical difficulties and nugget remedies for nearly singular Gaussian-process covariance matrices. These works motivate the present random-location question but the inspected statements do not give its fixed-node-count inverse-operator-norm exact tail coefficient, sharp moment threshold, and corresponding expectation-level nugget asymptotics. A study of smallest eigenvalues of random *minimum-kernel* matrices concerns a different kernel and growing-size regime; its complete text was inaccessible for comparison, so publication priority is not independently settled. The claimed contribution is the simultaneous random-design classification, not the known precision factorization, elementary collision counting, or general regular-variation principle.

## Limitations

This is an exact mathematical result only for a fixed finite number of iid points from a continuous bounded density on a one-dimensional interval, with the exponential covariance kernel and spectral norm. It is not a general theorem for squared-exponential, smoother Matérn or higher-dimensional kernels; nor does it analyze growing sample counts, floating-point error, Gaussian-process prediction MSE, or finite-threshold optimal sampling. A positive nugget restores deterministic bounded inverse norm at any fixed value but no uniform expected bound holds as it is removed. Originality has only the documented literature comparison and not independent publication-priority certification.

## References

1. A. H. Barnett, P. Greengard and M. Rachh, *Uniform approximation of common Gaussian process kernels using equispaced Fourier grids*, arXiv:2305.11065v1 (first public version 2023-05-18), https://arxiv.org/abs/2305.11065.
2. G. B. Rybicki and W. H. Press, *A Class of Fast Methods for Processing Irregularly Sampled or Otherwise Inhomogeneous One-Dimensional Data*, Physical Review Letters 74 (1995), 1060–1063, https://doi.org/10.1103/PhysRevLett.74.1060.
3. S. Barthelmé and K. Usevich, *Spectral properties of kernel matrices in the flat limit*, arXiv:1910.14067 (2019), https://arxiv.org/abs/1910.14067.
4. P. Ranjan, R. Haynes and R. Karsten, *A Computationally Stable Approach to Gaussian Process Interpolation of Deterministic Computer Simulation Data*, Technometrics 53 (2011), 366–378, https://doi.org/10.1198/TECH.2011.09141.
5. Y. Huang, H.-P. Liao, C.-H. Chang and T.-Y. Hwang, *The smallest eigenvalues of random kernel matrices: Asymptotic results on the min kernel*, Statistics & Probability Letters (2019), https://doi.org/10.1016/j.spl.2018.12.008.
