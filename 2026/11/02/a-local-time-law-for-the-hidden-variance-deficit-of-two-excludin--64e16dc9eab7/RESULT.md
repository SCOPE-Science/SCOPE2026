# A local-time law for the hidden variance deficit of two excluding walkers

## Finding
Consider two simple symmetric exclusion walkers on the integer line, each attempting each nearest-neighbour jump at rate \(1/2\), with deterministic ordered initial locations \(x_{1,n}<x_{2,n}\). Write \(C(s)=(X_1(s)+X_2(s))/2\), \(R(s)=X_2(s)-X_1(s)\), and assume \(R(0)/n\to\delta\in[0,\infty)\). Put
\[
C_n(t)=\frac{C(n^2t)-C(0)}{n},\quad R_n(t)=\frac{R(n^2t)}n,\quad H_n(t)=n\left(\frac t2-\langle C_n\rangle_t\right).
\]
Here \(\langle C_n\rangle\) denotes the *predictable* quadratic variation, not the optional quadratic variation. For every finite \(T>0\), jointly in \(D([0,T],\mathbb R^3)\) with the \(J_1\) topology,
\[
(C_n,R_n,H_n)\ \Longrightarrow\ \left(\frac{B^c}{\sqrt2},\ \delta+\sqrt2B^r+K,\ \frac K4\right),\qquad
K_t=\sup_{0\le s\le t}(-\delta-\sqrt2 B_s^r)_+,
\]
where \(B^c,B^r\) are **independent** standard Brownian motions. Thus the order-\(1/n\) bracket deficit has a nondegenerate, continuous and non-Gaussian process limit, independent of the leading Gaussian centre motion.

For \(t>0\) and \(z\ge0\), the limit has the exact tail
\[
\mathbb P(K_t>z)=2\left[1-\Phi\left(\frac{\delta+z}{\sqrt{2t}}\right)\right].
\]
In particular, it has an atom at zero of size \(2\Phi(\delta/\sqrt{2t})-1\); this atom disappears when \(\delta=0\). Writing \(a=\delta/\sqrt{2t}\), \(\phi\) and \(\Phi\) for the standard normal density and distribution,
\[
\lim_{n\to\infty} n\left(\frac t2-\operatorname{Var}(C_n(t))\right)
=\frac{\mathbb E K_t}{4}
=\frac12\left[\sqrt{2t}\,\phi(a)-\delta\bigl(1-\Phi(a)\bigr)\right].
\]
This limit is positive for all finite \(\delta\ge0\) and \(t>0\).

## Assumptions and scope
The microscopic dynamics live on the full infinite lattice \(\mathbb Z\). The two particles occupy distinct sites and only jump to vacant sites; the four left/right attempted jumps are independent rate-\(1/2\) clocks. The deterministic ordered initial locations may depend on \(n\), and the *only* needed initial condition is convergence of the rescaled gap \(R(0)/n\to\delta<\infty\). A deterministic initial centre may be arbitrary because it is subtracted. Time is accelerated by \(n^2\), space divided by \(n\), and \(t\in[0,T]\) for arbitrary fixed finite \(T\). The result is **not** a limit for positive-density equilibrium exclusion, for asymmetrically driven exclusion, or for an arbitrary number of particles.

## Proof
**1. Exact finite-lattice generator.** At a gap \(r\ge2\), the gap jumps to \(r+1\) and \(r-1\), each at rate \(1\); at \(r=1\), only the outward move \(1\to2\) occurs, at rate \(1\). If \(A_s:=\int_0^s\mathbf 1_{\{R(u)=1\}}\,du\), then
\[
R(s)=R(0)+M^r(s)+A_s,
\quad\langle M^r\rangle_s=2s-A_s.
\]
The centre is a square-integrable martingale, and direct enumeration of the four attempted moves gives
\[
\langle C\rangle_s=s/2-A_s/4,
\qquad\langle C,M^r\rangle_s=0.
\]
These are exact identities with no asymptotic approximations. Consequently \(H_n(t)=A_{n^2t}/(4n)\) identically.

**2. Reflected Skorokhod decomposition and the occupation estimate.** Define \(Q(s)=R(s)-1\ge0\). Its decomposition is
\[
Q(s)=Q(0)+M^r(s)+A_s,
\]
where \(A\) is continuous, nondecreasing, starts at zero, and increases only on \(\{Q=0\}\). Uniqueness of the one-dimensional Skorokhod reflection map therefore yields pathwise
\[
A_s=\sup_{0\le u\le s}\bigl[-Q(0)-M^r(u)\bigr]_+.
\]
By Doob's square-integrable martingale inequality and the bracket bound \(\langle M^r\rangle_s\le2s\),
\[
\mathbb E A_{n^2T}^{2}\le 4\mathbb E|M^r(n^2T)|^2\le 8n^2T.
\]
Thus \(A_{n^2T}/n\) is uniformly bounded in \(L^2\), while \(A_{n^2T}/n^2\to0\) in probability and in \(L^1\).

**3. Joint functional central limit theorem.** The rescaled martingales
\[
\left(\frac{C(n^2\cdot)-C(0)}n,\frac{M^r(n^2\cdot)}n\right)
\]
have jumps bounded by \(1/n\), respectively \(1/(2n)\) and \(1/n\). Their predictable covariance matrix converges uniformly in probability on \([0,T]\) to \(\mathrm{diag}(t/2,2t)\): the cross bracket is identically zero and the other errors equal multiples of \(A_{n^2T}/n^2\). The two-dimensional functional martingale central limit theorem consequently gives independent limits \((B^c/\sqrt2,\sqrt2B^r)\).

**4. Reflection and exact deficit.** The Skorokhod regulator map \(w\mapsto \sup_{s\le t}(-w(s))_+\) is continuous at continuous paths for uniform convergence. Since \((R(0)-1)/n\to\delta\), the continuous mapping theorem gives
\[
A_{n^2\cdot}/n\Rightarrow K,
\qquad R(n^2\cdot)/n\Rightarrow\delta+\sqrt2B^r+K.
\]
Together with the exact equality \(H_n=A_{n^2\cdot}/(4n)\), this yields the asserted joint functional limit and independence of the first coordinate from the deficit process.

**5. Distribution and variance correction.** The reflection principle for Brownian motion gives \(\mathbb P(K_t>z)=2\bar\Phi((\delta+z)/\sqrt{2t})\). Integrating this tail yields
\[
\mathbb E K_t=2\left[\sqrt{2t}\phi(a)-\delta\bar\Phi(a)\right].
\]
Uniform \(L^2\) boundedness of \(A_{n^2t}/n\) implies uniform integrability and hence convergence of its expectation. Finally, since \(C_n\) is a centred square-integrable martingale, \(\operatorname{Var}(C_n(t))=\mathbb E\langle C_n\rangle_t\), proving the stated sharp finite-size variance correction.

## Verification
Run the supplied standalone `verification_checker.py` with Python 3. It exactly enumerates all allowed two-particle moves over \(819\) ordered configurations, reconstructs each generator, bracket and cross-bracket identity using rational arithmetic, and separately tests the Neumann image formula for the reflected gap walk through twenty discrete steps from fourteen initial gaps. It also checks Gaussian normalisation and selected numerical mean-convergence values using an independently computed Bessel heat kernel when SciPy is installed. The included `verification_output.txt` is the output of a fresh run of the packaged checker; finite tests supplement but do not establish the functional limit.

## Relationship to prior work
Ayala, Dirr and Zimmer (arXiv:2610.31319, first posted 22 October 2026, primary MSC 60K35) prove convergence of fixed-number exclusion empirical measures to independent diffusions. They bound but do not identify the vanishing near-collision contribution; their Proposition 6.8 gives an \(O(1/n)\) order in one dimension. This result resolves the next-order *random process law* for the predictable centre bracket in the two-particle nearest-neighbour case. It is neither a replacement for nor a claim of novelty for the standard reflected-walk invariance principle or the Brownian reflection principle.

Ayala and Renger (arXiv:2512.20412) study collision and flux hydrodynamic limits on tori under varying particle counts and product initial laws. Their limiting regimes and observables do not give the present two-particle infinite-line joint bracket-depletion law. Gess and Konarovskyi (arXiv:2610.13308) obtain higher-order Gaussian approximations for positive-density SSEP fluctuation fields, not the fixed-two-particle non-Gaussian correction. Fan (arXiv:1410.3585) establishes joint invariance of reflected walks and boundary local times for general reflected-diffusion approximations on bounded domains. Denisov and Wachtel (arXiv:1412.6184) study reflected-walk local-time universality. These results substantially cover the *regulator-convergence ingredient*, which is not presented as new here. Neither inspected result treats the exact two-particle exclusion centre-bracket identity or the joint independent Gaussian-centre/non-Gaussian bracket-deficit observable. The theorem uses standard martingale FCLT and Skorokhod reflection as tools; its model-specific bridge from blocked attempts to the first random variance correction is the contribution asserted here.

## Limitations
No independent mathematical review has been performed. General historical reflected-particle or local-time approximation results could imply parts of this specialization; the available searched literature did not establish an already-published statement implying the whole joint bracket correction. The theorem applies to exactly two nearest-neighbour exclusion walkers on \(\mathbb Z\) and to predictable (not optional) quadratic variation. It does not quantify convergence rates beyond the first asymptotic coefficient, extend to three or more walkers, or establish an analogous law for inclusion dynamics.

## References
1. M. Ayala, N. Dirr and J. Zimmer, *Atomic limits of empirical measures of interacting particle systems with self-duality*, arXiv:2610.31319v1 (submitted 22 October 2026), Sections 2, 4, 5 and 6.
2. M. Ayala and D. R. M. Renger, *Hydrodynamic limits of collisions and fluxes in the exclusion process*, arXiv:2512.20412v1 (submitted 23 December 2025), Sections 1, 2 and 6.
3. B. Gess and V. Konarovskyi, *Higher-Order Gaussian Approximations on Path Space for the Simple Symmetric Exclusion Process*, arXiv:2610.13308v1 (submitted 9 October 2026), Sections 1 and 3.
4. W.-T. L. Fan, *Discrete approximations to local times for reflected diffusions*, arXiv:1410.3585 (2014), Theorem 3.1.
5. D. Denisov and V. Wachtel, *Universality of local times of killed and reflected random walks*, arXiv:1412.6184 (2014).
6. P. Billingsley, *Convergence of Probability Measures*, second edition, Wiley, 1999 (functional convergence framework).
7. S. N. Ethier and T. G. Kurtz, *Markov Processes: Characterization and Convergence*, Wiley, 1986 (martingale functional convergence).
